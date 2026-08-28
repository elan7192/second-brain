#!/usr/bin/env python3
"""Rebuild derived ontology files from wiki markdown."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ontology_lib import check_ontology, compile_ontology, write_ontology  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile wiki pages into a local AIP ontology.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if output/ontology-objects.csv is stale. Do not write.",
    )
    args = parser.parse_args()
    if args.check:
        errors = check_ontology(ROOT)
        if errors:
            for err in errors:
                print(err)
            return 1
        print("ontology check ok")
        return 0
    bundle = compile_ontology(ROOT)
    csv_path, json_path = write_ontology(bundle, ROOT)
    counts = bundle["counts"]
    print(
        f"objects={counts.get('objects', 0)} links={counts.get('links', 0)} "
        f"csv={csv_path.relative_to(ROOT)} json={json_path.relative_to(ROOT)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
