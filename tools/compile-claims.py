#!/usr/bin/env python3
"""Rebuild wiki/claims.csv from sources + curated claims."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import memorylib  # noqa: E402

CLAIMS_PATH = ROOT / "wiki" / "claims.csv"


def write_tables() -> int:
    claims_csv, errors = memorylib.compile_tables(ROOT)
    if errors:
        for item in errors:
            print(f"ERROR {item}")
        return 1
    CLAIMS_PATH.write_text(claims_csv, encoding="utf-8")
    claim_n = claims_csv.count("\n") - 1
    print(f"wrote {CLAIMS_PATH.relative_to(ROOT)} rows={claim_n}")
    return 0


def check_tables() -> int:
    claims_csv, errors = memorylib.compile_tables(ROOT)
    failed = 0
    for item in errors:
        print(f"ERROR {item}")
        failed = 1
    if not CLAIMS_PATH.exists():
        print("ERROR wiki/claims.csv missing. Run python3 tools/compile-claims.py")
        return 1
    if CLAIMS_PATH.read_text(encoding="utf-8") != claims_csv:
        print("STALE wiki/claims.csv. Run python3 tools/compile-claims.py")
        failed = 1
    if failed == 0:
        print("claims.csv matches compile")
    return failed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if CSV is missing or stale. Do not write.",
    )
    args = parser.parse_args()
    return check_tables() if args.check else write_tables()


if __name__ == "__main__":
    sys.exit(main())
