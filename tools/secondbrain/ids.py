"""Assign and persist stable IDs. Filenames are not identity."""

from __future__ import annotations

from pathlib import Path

from . import frontmatter, schema
from .paths import ROOT


def iter_knowledge_paths(root: Path | None = None) -> list[Path]:
    root = root or ROOT
    found: list[Path] = []
    wiki = root / "wiki"
    if wiki.is_dir():
        for path in sorted(wiki.rglob("*.md")):
            if any(part in schema.SKIP_DIR_NAMES for part in path.parts):
                continue
            found.append(path)
    for name in schema.INDEXED_ROOT_FILES:
        path = root / name
        if path.exists():
            found.append(path)
    return found


SPECIAL_IDS = {
    "MEMORY.md": "memory:root",
    "decisions.md": "meta:decisions",
    "Home.md": "meta:Home",
    "wiki.md": "meta:wiki",
}


def id_for(path: Path, root: Path | None = None) -> str:
    root = root or ROOT
    meta, _ = frontmatter.parse_file(path)
    if meta.get("id"):
        return str(meta["id"]).strip()
    if path.name in SPECIAL_IDS:
        return SPECIAL_IDS[path.name]
    kind = schema.kind_for(path, str(meta.get("type", "")), root)
    return schema.make_id(kind, path.stem)


def write_missing_ids(root: Path | None = None) -> list[str]:
    root = root or ROOT
    written: list[str] = []
    for path in iter_knowledge_paths(root):
        text = path.read_text(encoding="utf-8")
        object_id = id_for(path, root)
        new, changed = frontmatter.insert_id(text, object_id)
        if changed:
            path.write_text(new, encoding="utf-8")
            written.append(f"{path.relative_to(root)} {object_id}")
    return written
