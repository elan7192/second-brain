#!/usr/bin/env python3
"""Check wiki pages, claims tables, provenance, orphans, and untrusted-data isolation.

Exit 1 if any missing link, non-hub orphan, or extra gate failure.
Hubs: index, log, Home, lint-wiki, graph, claims.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import memorylib  # noqa: E402
from secondbrain.frontmatter import WIKILINK as LINK  # noqa: E402
from secondbrain.paths import rel_posix  # noqa: E402

SKIP_DIRS = {".git", ".obsidian", "templates", ".agents", ".cursor", "eval"}
SKIP_FILES = {"AGENTS.md", "CLAUDE.md", "README.md"}
HUBS = {"index", "index-papers", "index-sources", "log", "Home", "lint-wiki", "graph", "claims"}
SOURCE_CLAIMS_RE = re.compile(r"^## Claims kept", re.M)

# One read per file per lint run. main() clears it so repeated in-process
# runs (validate, tests) always see the current tree.
_TEXTS: dict[Path, str] = {}


def read_text(path: Path) -> str:
    text = _TEXTS.get(path)
    if text is None:
        text = path.read_text(encoding="utf-8")
        _TEXTS[path] = text
    return text


def pages() -> dict[str, Path]:
    found: dict[str, Path] = {}
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        found[path.stem] = path
    return found


def check_links(catalog: dict[str, Path]) -> tuple[list[str], list[str]]:
    missing: list[str] = []
    inbound: dict[str, int] = {slug: 0 for slug in catalog}
    for path in catalog.values():
        text = read_text(path)
        for match in LINK.finditer(text):
            target = match.group(1).strip()
            if target not in catalog:
                missing.append(f"{path.relative_to(ROOT)} -> [[{target}]]")
            else:
                inbound[target] += 1
    orphans = sorted(
        slug for slug, count in inbound.items() if count == 0 and slug not in HUBS
    )
    return missing, orphans


def check_source_claims() -> list[str]:
    errors: list[str] = []
    sources = ROOT / "wiki" / "sources"
    compile_layer = (ROOT / "wiki" / "claims.csv").exists() or (
        ROOT / "wiki" / "claims"
    ).is_dir()
    if not sources.exists() or not compile_layer:
        return []
    for path in sorted(sources.glob("*.md")):
        text = read_text(path)
        if not SOURCE_CLAIMS_RE.search(text):
            errors.append(f"{path.relative_to(ROOT)} missing ## Claims kept")
    return errors


def check_injection() -> list[str]:
    errors: list[str] = []
    for name in memorylib.TRUSTED_SCHEMA_FILES:
        path = ROOT / name
        if not path.exists():
            continue
        hits = memorylib.injection_hits(path.read_text(encoding="utf-8"))
        for hit in hits:
            errors.append(f"{name} untrusted-instruction phrase {hit!r}")
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS or part == "raw" for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        rel = rel_posix(path, ROOT)
        if rel.startswith("raw/"):
            continue
        hits = memorylib.injection_hits(read_text(path))
        for hit in hits:
            errors.append(f"{rel} unquoted injection phrase {hit!r}")
    return errors


def check_memory_v1(catalog: dict[str, Path]) -> list[str]:
    errors: list[str] = []
    for path in catalog.values():
        errors.extend(memorylib.validate_memory_v1(rel_posix(path, ROOT), read_text(path)))
    return errors


def check_disputed_in_conflicts() -> list[str]:
    errors: list[str] = []
    claims_path = ROOT / "wiki" / "claims.csv"
    if not claims_path.exists():
        return errors
    import csv

    conflict_ids = memorylib.contradiction_ids(ROOT)
    with claims_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        if row.get("status") != "disputed":
            continue
        pages = row.get("pages", "")
        listed = [part for part in pages.split("|") if re.fullmatch(r"C\d+", part)]
        if not listed:
            errors.append(f"{row['claim_id']} status=disputed needs a C# id in pages")
            continue
        for cid in listed:
            if cid not in conflict_ids:
                errors.append(
                    f"{row['claim_id']} pages {cid} missing from wiki/contradictions.md"
                )
    return errors


def check_compile() -> list[str]:
    compile_layer = (ROOT / "wiki" / "claims.csv").exists() or (
        ROOT / "wiki" / "claims"
    ).is_dir()
    if not compile_layer:
        return []
    errors: list[str] = []
    claims_csv, compile_errors = memorylib.compile_tables(ROOT)
    errors.extend(compile_errors)
    claims_path = ROOT / "wiki" / "claims.csv"
    if not claims_path.exists():
        errors.append("wiki/claims.csv missing. Run python3 tools/compile-claims.py")
    elif claims_path.read_text(encoding="utf-8") != claims_csv:
        errors.append("STALE wiki/claims.csv. Run python3 tools/compile-claims.py")
    return errors


def check_instruction_budget() -> list[str]:
    import instruction_budget

    return instruction_budget.check(ROOT)


def main() -> int:
    _TEXTS.clear()
    catalog = pages()
    missing, orphans = check_links(catalog)
    extra: list[str] = []
    extra.extend(check_source_claims())
    extra.extend(check_injection())
    extra.extend(check_memory_v1(catalog))
    extra.extend(check_compile())
    extra.extend(check_disputed_in_conflicts())
    extra.extend(check_instruction_budget())
    print(
        f"pages={len(catalog)} missing={len(missing)} orphans={len(orphans)} extra={len(extra)}"
    )
    for item in missing:
        print(f"MISSING {item}")
    for slug in orphans:
        print(f"ORPHAN {slug}")
    for item in extra:
        print(f"FAIL {item}")
    return 1 if missing or orphans or extra else 0


if __name__ == "__main__":
    sys.exit(main())
