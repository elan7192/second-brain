"""Deterministic ingest gates. The model proposes; this command accepts."""

from __future__ import annotations

import re
from pathlib import Path

from . import frontmatter
from .paths import ROOT

CLAIMS_RE = re.compile(r"^## Claims kept", re.M)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
CATALOG_NAMES = frozenset(
    {"index.md", "index-sources.md", "index-papers.md", "log.md", "Home.md"}
)


def normalize_slug(raw: str) -> str:
    text = raw.strip()
    if text.endswith(".md"):
        text = Path(text).stem
    if "/" in text:
        text = Path(text).stem
    if text.startswith("source:"):
        text = text.split(":", 1)[1]
    return text


def check(slug: str, root: Path | None = None) -> tuple[int, str]:
    root = root or ROOT
    slug = normalize_slug(slug)
    errors: list[str] = []
    source = root / "wiki" / "sources" / f"{slug}.md"
    if not source.exists():
        return 1, f"FAIL ingest-check missing wiki/sources/{slug}.md\n"

    text = source.read_text(encoding="utf-8")
    meta, body = frontmatter.split(text)
    object_id = str(meta.get("id") or "")
    if not object_id:
        errors.append("source page missing id:")
    elif object_id != f"source:{slug}":
        errors.append(f"id {object_id!r} does not match source:{slug}")
    if not CLAIMS_RE.search(body):
        errors.append("missing ## Claims kept")

    catalog = (root / "wiki" / "index-sources.md").read_text(encoding="utf-8")
    if f"[[{slug}]]" not in catalog:
        errors.append(f"not listed in wiki/index-sources.md")

    inbound = _inbound_from_living(root, slug, source)
    if not inbound:
        errors.append("no inbound wikilink from a living page")

    if not _has_compiled_claim(root, slug):
        errors.append("no compiled claim row in wiki/claims.csv")

    if errors:
        return 1, f"FAIL ingest-check {slug}\n" + "\n".join(f"  {item}" for item in errors) + "\n"
    living = ", ".join(inbound[:5])
    return 0, f"ok ingest-check {slug} inbound={living}\n"


def _inbound_from_living(root: Path, slug: str, source: Path) -> list[str]:
    hits: list[str] = []
    skip = {source.resolve()}
    for path in root.rglob("*.md"):
        if path.resolve() in skip:
            continue
        if any(part in {".git", ".obsidian", "templates", "raw", ".agents", ".cursor"} for part in path.parts):
            continue
        if path.name in CATALOG_NAMES:
            continue
        text = path.read_text(encoding="utf-8")
        if slug in WIKILINK_RE.findall(text):
            hits.append(path.relative_to(root).as_posix())
    return hits


def _has_compiled_claim(root: Path, slug: str) -> bool:
    csv_path = root / "wiki" / "claims.csv"
    if not csv_path.exists():
        return False
    text = csv_path.read_text(encoding="utf-8")
    return slug in text or f"wiki/sources/{slug}.md" in text
