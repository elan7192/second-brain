#!/usr/bin/env python3
"""Fetch the pinned Archify checkout. Do not commit upstream/."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIN_PATH = ROOT / ".agents" / "skills" / "archify" / "pin.json"
UPSTREAM = ROOT / ".agents" / "skills" / "archify" / "upstream"
REQUIRED = ("name", "upstream", "commit", "version", "license", "skill_path", "cli")


def load_pin() -> dict:
    data = json.loads(PIN_PATH.read_text(encoding="utf-8"))
    missing = [key for key in REQUIRED if not data.get(key)]
    if missing:
        raise SystemExit(f"pin.json missing {missing}")
    commit = str(data["commit"])
    if len(commit) != 40 or any(ch not in "0123456789abcdef" for ch in commit.lower()):
        raise SystemExit("pin.json commit must be a 40-char git SHA")
    return data


def current_head(path: Path) -> str:
    proc = subprocess.run(
        ["git", "-C", str(path), "rev-parse", "HEAD"],
        check=False,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        return ""
    return proc.stdout.strip()


def fetch(pin: dict) -> int:
    UPSTREAM.parent.mkdir(parents=True, exist_ok=True)
    commit = pin["commit"]
    url = pin["upstream"]
    if UPSTREAM.joinpath(".git").exists() and current_head(UPSTREAM) == commit:
        print(f"ok archify pin {commit}")
        return 0
    if UPSTREAM.exists():
        subprocess.run(["rm", "-rf", str(UPSTREAM)], check=True)
    subprocess.run(
        ["git", "clone", "--filter=blob:none", "--no-checkout", url, str(UPSTREAM)],
        check=True,
    )
    subprocess.run(["git", "-C", str(UPSTREAM), "fetch", "--depth", "1", "origin", commit], check=True)
    subprocess.run(["git", "-C", str(UPSTREAM), "checkout", "--detach", commit], check=True)
    print(f"fetched archify {commit}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate pin.json only")
    args = parser.parse_args()
    pin = load_pin()
    if args.check:
        print(f"ok pin {pin['commit']} {pin['version']}")
        return 0
    return fetch(pin)


if __name__ == "__main__":
    sys.exit(main())
