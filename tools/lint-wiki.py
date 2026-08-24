#!/usr/bin/env python3
"""Check wiki pages for missing wikilink targets and orphan pages."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
SKIP_DIRS = {".git", ".obsidian", "templates", "node_modules"}
SKIP_FILES = {"AGENTS.md", "CLAUDE.md", "README.md"}
HUBS = {"index", "log", "Home", "lint-wiki", "graph"}


def pages() -> dict[str, Path]:
    found: dict[str, Path] = {}
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        found[path.stem] = path
    return found


def main() -> int:
    catalog = pages()
    missing: list[str] = []
    inbound: dict[str, int] = {slug: 0 for slug in catalog}
    for path in catalog.values():
        text = path.read_text(encoding="utf-8")
        for match in LINK.finditer(text):
            target = match.group(1).strip()
            if target not in catalog:
                missing.append(f"{path.relative_to(ROOT)} -> [[{target}]]")
            else:
                inbound[target] += 1
    orphans = sorted(
        slug for slug, count in inbound.items() if count == 0 and slug not in HUBS
    )
    print(f"pages={len(catalog)} missing={len(missing)} orphans={len(orphans)}")
    for item in missing:
        print(f"MISSING {item}")
    for slug in orphans:
        print(f"ORPHAN {slug}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
