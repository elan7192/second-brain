"""Parse and splice YAML frontmatter without rewriting the rest of the file."""

from __future__ import annotations

import re
from pathlib import Path

# Annotations only; `from __future__ import annotations` keeps them unevaluated,
# so the typing module never loads on the query path.
Any = object

FRONT_RE = re.compile(r"\A---\n(.*?)\n---(?:\n|$)", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
# The one wikilink pattern for every tool. Group 1 is the target slug; alias and heading are dropped.
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")


def split(text: str) -> tuple[dict[str, Any], str]:
    match = FRONT_RE.match(text)
    if not match:
        return {}, text
    return _parse_front(match.group(1)), text[match.end() :]


def parse_file(path: Path) -> tuple[dict[str, Any], str]:
    return split(path.read_text(encoding="utf-8"))


def title_of(meta: dict[str, Any], body: str, fallback: str) -> str:
    if meta.get("title"):
        return str(meta["title"]).strip()
    match = H1_RE.search(body)
    if match:
        return match.group(1).strip()
    return fallback


def has_id(text: str) -> bool:
    meta, _ = split(text)
    return bool(meta.get("id"))


def insert_id(text: str, object_id: str) -> tuple[str, bool]:
    """Insert `id:` as the first frontmatter key. Preserve original YAML body."""
    if not text.startswith("---\n"):
        stamped = f"---\nid: {object_id}\n---\n\n{text}"
        return stamped, True
    end = text.find("\n---\n", 4)
    if end == -1:
        if text.endswith("\n---"):
            block = text[4:-4]
            if re.search(r"^id:\s*\S", block, re.MULTILINE):
                return text, False
            return f"---\nid: {object_id}\n{block}\n---\n", True
        return text, False
    block = text[4:end]
    if re.search(r"^id:\s*\S", block, re.MULTILINE):
        return text, False
    new = f"---\nid: {object_id}\n{block}{text[end:]}"
    return new, True


def _parse_front(block: str) -> dict[str, Any]:
    meta: dict[str, Any] = {}
    key: str | None = None
    sequence: list[str] | None = None
    for raw in block.splitlines():
        if not raw.strip():
            continue
        if sequence is not None and raw.startswith("  - "):
            sequence.append(raw[4:].strip().strip("'\""))
            continue
        sequence = None
        if ":" not in raw:
            continue
        key, _, rest = raw.partition(":")
        key = key.strip()
        rest = rest.strip()
        if rest == "":
            sequence = []
            meta[key] = sequence
        else:
            meta[key] = rest.strip("'\"")
    return meta
