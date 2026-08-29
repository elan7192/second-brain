#!/usr/bin/env python3
"""Fetch and verify the pinned Archify checkout. Do not commit upstream/.

Fail closed if the network is down, HEAD is not the pin, the git tree
does not match, or a hashed file changed. A branch name is not a pin.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIN_PATH = Path(
    os.environ.get("ARCHIFY_PIN_PATH") or ROOT / ".agents" / "skills" / "archify" / "pin.json"
)
UPSTREAM = Path(
    os.environ.get("ARCHIFY_UPSTREAM_PATH")
    or ROOT / ".agents" / "skills" / "archify" / "upstream"
)
REQUIRED = (
    "name",
    "repository",
    "commit",
    "tree",
    "skill_path",
    "cli",
    "license_path",
    "skill_sha256",
    "cli_sha256",
    "license_sha256",
    "license",
)
HASH_KEYS = ("skill_sha256", "cli_sha256", "license_sha256")
FORBIDDEN = ("branch", "ref", "tag")
SHA1 = 40
SHA256 = 64


class PinError(Exception):
    pass


def _hex(value: object, length: int, label: str) -> str:
    text = str(value).strip().lower()
    if len(text) != length or any(ch not in "0123456789abcdef" for ch in text):
        raise PinError(f"FAIL pin {label} must be {length}-char hex")
    return text


def load_pin(path: Path | None = None) -> dict:
    pin_path = path or PIN_PATH
    data = json.loads(pin_path.read_text(encoding="utf-8"))
    for key in FORBIDDEN:
        if key in data:
            raise PinError(f"FAIL pin must not use {key}; pin a commit SHA")
    missing = [key for key in REQUIRED if not data.get(key)]
    if missing:
        raise PinError(f"FAIL pin.json missing {missing}")
    data["commit"] = _hex(data["commit"], SHA1, "commit")
    data["tree"] = _hex(data["tree"], SHA1, "tree")
    for key in HASH_KEYS:
        data[key] = _hex(data[key], SHA256, key)
    if data.get("on_unavailable") not in (None, "fail-closed"):
        raise PinError("FAIL on_unavailable must be fail-closed")
    if data.get("on_mismatch") not in (None, "fail-closed"):
        raise PinError("FAIL on_mismatch must be fail-closed")
    repo = str(data["repository"])
    if not repo.startswith("https://github.com/"):
        raise PinError("FAIL repository must be an https://github.com URL")
    return data


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(args: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["GIT_TERMINAL_PROMPT"] = "0"
    return subprocess.run(
        ["git", *args],
        cwd=str(cwd) if cwd else None,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )


def current_head(path: Path) -> str:
    proc = git(["rev-parse", "HEAD"], cwd=path)
    if proc.returncode != 0:
        return ""
    return proc.stdout.strip().lower()


def current_tree(path: Path) -> str:
    proc = git(["rev-parse", "HEAD^{tree}"], cwd=path)
    if proc.returncode != 0:
        return ""
    return proc.stdout.strip().lower()


def verify_checkout(pin: dict, root: Path) -> None:
    head = current_head(root)
    if head != pin["commit"]:
        raise PinError(f"FAIL archify HEAD {head or 'missing'} != pin {pin['commit']}")
    tree = current_tree(root)
    if tree != pin["tree"]:
        raise PinError(f"FAIL archify tree {tree or 'missing'} != pin {pin['tree']}")
    pairs = (
        (pin["skill_path"], pin["skill_sha256"]),
        (pin["cli"], pin["cli_sha256"]),
        (pin["license_path"], pin["license_sha256"]),
    )
    for rel, expected in pairs:
        path = root / rel
        if not path.is_file():
            raise PinError(f"FAIL archify missing {rel}")
        got = sha256_file(path)
        if got != expected:
            raise PinError(f"FAIL archify content mismatch for {rel}")


def discard_checkout(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)


def fetch(pin: dict) -> int:
    if UPSTREAM.joinpath(".git").exists():
        try:
            verify_checkout(pin, UPSTREAM)
            print(f"ok archify pin {pin['commit']}")
            return 0
        except PinError:
            discard_checkout(UPSTREAM)
    UPSTREAM.parent.mkdir(parents=True, exist_ok=True)
    clone = git(
        ["clone", "--filter=blob:none", "--no-checkout", pin["repository"], str(UPSTREAM)]
    )
    if clone.returncode != 0:
        discard_checkout(UPSTREAM)
        raise PinError("FAIL archify upstream unavailable. Do not invent a renderer.")
    got = git(["fetch", "--depth", "1", "origin", pin["commit"]], cwd=UPSTREAM)
    if got.returncode != 0:
        discard_checkout(UPSTREAM)
        raise PinError("FAIL archify upstream unavailable. Do not invent a renderer.")
    checked = git(["checkout", "--detach", pin["commit"]], cwd=UPSTREAM)
    if checked.returncode != 0:
        discard_checkout(UPSTREAM)
        raise PinError("FAIL archify checkout failed. Do not invent a renderer.")
    try:
        verify_checkout(pin, UPSTREAM)
    except PinError:
        discard_checkout(UPSTREAM)
        raise PinError("FAIL archify content mismatch. Do not use this checkout.") from None
    print(f"fetched archify {pin['commit']}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate pin.json only")
    parser.add_argument("--verify", action="store_true", help="Verify an existing checkout")
    args = parser.parse_args()
    pin = load_pin()
    if args.check:
        print(f"ok pin {pin['commit']} tree {pin['tree']}")
        return 0
    if args.verify:
        if not UPSTREAM.joinpath(".git").exists():
            raise PinError("FAIL archify checkout missing. Run python3 tools/fetch-archify.py")
        verify_checkout(pin, UPSTREAM)
        print(f"ok archify verify {pin['commit']}")
        return 0
    return fetch(pin)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PinError as exc:
        print(exc, file=sys.stderr)
        raise SystemExit(1) from exc
