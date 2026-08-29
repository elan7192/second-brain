"""Object kinds and ID rules."""

from __future__ import annotations

from pathlib import Path

KINDS = (
    "source",
    "concept",
    "claim",
    "person",
    "project",
    "decision",
    "experiment",
    "contradiction",
    "meta",
    "memory",
)

TYPE_TO_KIND = {
    "source": "source",
    "concept": "concept",
    "person": "person",
    "project": "project",
    "decision": "decision",
    "experiment": "experiment",
    "claim": "claim",
    "contradiction": "contradiction",
    "meta": "meta",
    "home": "meta",
    "note": "concept",
}

INDEXED_ROOT_FILES = {"MEMORY.md", "decisions.md", "Home.md", "wiki.md"}
SKIP_DIR_NAMES = {".git", ".obsidian", "templates", "raw", "output", ".cache"}
SKIP_FILE_NAMES = {"AGENTS.md", "CLAUDE.md", "README.md"}

# Navigation indexes are not knowledge objects.
SKIP_DIR_PREFIXES = ("hunt/", "ship/", "maps/", "growth/")

TYPE_WEIGHT = {
    "decision": 1.25,
    "claim": 1.2,
    "contradiction": 1.15,
    "concept": 1.0,
    "memory": 1.05,
    "source": 0.9,
    "person": 0.7,
    "project": 0.85,
    "meta": 0.45,
    "experiment": 0.9,
}


def kind_for(path: Path, declared_type: str, root: Path) -> str:
    rel = path.relative_to(root).as_posix()
    if rel.startswith("wiki/sources/"):
        return "source"
    if rel.startswith("wiki/people/"):
        return "person"
    if declared_type in TYPE_TO_KIND:
        return TYPE_TO_KIND[declared_type]
    if path.name == "MEMORY.md":
        return "memory"
    if path.name == "decisions.md":
        return "meta"
    if path.name in {"Home.md", "wiki.md"}:
        return "meta"
    if rel.startswith("wiki/"):
        return "concept"
    return "concept"


def make_id(kind: str, slug: str) -> str:
    slug = slug.strip()
    prefix = f"{kind}:"
    if slug.startswith(prefix):
        return slug
    return f"{kind}:{slug}"


def split_id(object_id: str) -> tuple[str, str]:
    kind, _, slug = object_id.partition(":")
    if not slug:
        return "concept", kind
    return kind, slug
