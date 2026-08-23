#!/usr/bin/env python3
"""Add Obsidian properties to compiled notes that lack frontmatter."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {".git", ".obsidian", "raw", "templates"}
SKIP_FILES = {"AGENTS.md", "CLAUDE.md", "README.md"}


def kind_for(path: Path) -> tuple[str, list[str]]:
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith("wiki/sources/"):
        return "source", ["twitter"]
    if rel.startswith("wiki/people/"):
        return "person", ["person"]
    if rel.startswith("wiki/"):
        meta = {
            "index.md",
            "how-it-works.md",
            "log.md",
            "contradictions.md",
            "agent-operating-system.md",
            "Today.md",
        }
        if path.name in meta:
            return "meta", ["wiki"]
        return "concept", ["wiki"]
    if rel.startswith("maps/") or path.name == "maps.md":
        return "map", ["map"]
    if rel.startswith("hunt/") or path.name == "hunt.md":
        return "hunt", ["hunt"]
    if rel.startswith("ship/") or path.name in {"ship.md", "Home.md"}:
        if path.name == "Home.md":
            return "home", ["wiki"]
        return "ship", ["ship"]
    if path.name in {"MEMORY.md", "decisions.md", "wiki.md"}:
        return "meta", ["wiki"]
    return "note", ["wiki"]


def main() -> None:
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        text = path.read_text(encoding="utf-8")
        if text.startswith("---\n"):
            continue
        note_type, tags = kind_for(path)
        tag_yaml = "\n".join(f"  - {tag}" for tag in tags)
        front = (
            "---\n"
            f"type: {note_type}\n"
            "tags:\n"
            f"{tag_yaml}\n"
            "created: 2026-08-23\n"
            "updated: 2026-08-23\n"
            "---\n\n"
        )
        path.write_text(front + text, encoding="utf-8")
        print(f"frontmatter {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
