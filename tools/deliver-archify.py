#!/usr/bin/env python3
"""Compile Archify JSON specs to local HTML. Do not commit the HTML."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIN = ROOT / ".agents/skills/archify/bin/archify.mjs"
SPEC_DIR = ROOT / "output/archify"

MAPS = (
    ("architecture", "vault-architecture.json", "vault-architecture.html"),
    ("workflow", "vault-ingest.workflow.json", "vault-ingest.html"),
    ("sequence", "vault-query.sequence.json", "vault-query.html"),
    ("dataflow", "vault-claims.dataflow.json", "vault-claims.html"),
    ("lifecycle", "vault-claim.lifecycle.json", "vault-claim.html"),
)


def run(args: list[str]) -> None:
    completed = subprocess.run(["node", str(BIN), *args], cwd=ROOT)
    if completed.returncode != 0:
        sys.exit(completed.returncode)


def main() -> None:
    if not BIN.is_file():
        print("missing .agents/skills/archify/bin/archify.mjs", file=sys.stderr)
        sys.exit(1)
    for diagram_type, spec_name, html_name in MAPS:
        spec = SPEC_DIR / spec_name
        html = SPEC_DIR / html_name
        run(["validate", diagram_type, str(spec), "--quality", "showcase"])
        run(["deliver", diagram_type, str(spec), str(html), "--quality", "showcase"])
    print("ok deliver-archify")


if __name__ == "__main__":
    main()
