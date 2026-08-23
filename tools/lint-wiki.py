#!/usr/bin/env python3
"""Check wiki pages for missing wikilink targets and orphan pages."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
ROOT_PAGES = [ROOT / "Home.md", ROOT / "MEMORY.md", ROOT / "decisions.md"]
LINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")


def slug_map() -> dict[str, Path]:
    pages: dict[str, Path] = {}
    for path in list(WIKI.rglob("*.md")) + ROOT_PAGES:
        pages[path.stem] = path
    return pages


def main() -> int:
    pages = slug_map()
    missing: list[str] = []
    inbound: dict[str, int] = {slug: 0 for slug in pages}
    for path in pages.values():
        text = path.read_text(encoding="utf-8")
        for match in LINK.finditer(text):
            target = match.group(1).strip()
            if target not in pages:
                missing.append(f"{path.relative_to(ROOT)} -> [[{target}]]")
            else:
                inbound[target] += 1
    orphans = sorted(
        slug
        for slug, count in inbound.items()
        if count == 0 and slug not in {"index", "log", "Home", "lint-wiki"}
    )
    print(f"pages={len(pages)} missing={len(missing)} orphans={len(orphans)}")
    for item in missing:
        print(f"MISSING {item}")
    for slug in orphans:
        print(f"ORPHAN {slug}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
