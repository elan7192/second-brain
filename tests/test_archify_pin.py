#!/usr/bin/env python3
"""Pin and commit-boundary checks for Archify."""

from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN_PATH = ROOT / ".agents" / "skills" / "archify" / "pin.json"
FETCH = ROOT / "tools" / "fetch-archify.py"
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


def _run_check(pin_path: Path) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["ARCHIFY_PIN_PATH"] = str(pin_path)
    return subprocess.run(
        [os.environ.get("PYTHON", "python3"), str(FETCH), "--check"],
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )


class ArchifyPinTest(unittest.TestCase):
    def test_pin_fields(self) -> None:
        pin = json.loads(PIN_PATH.read_text(encoding="utf-8"))
        for key in REQUIRED:
            self.assertTrue(pin.get(key), key)
        self.assertEqual(len(pin["commit"]), 40)
        self.assertEqual(len(pin["tree"]), 40)
        for key in ("skill_sha256", "cli_sha256", "license_sha256"):
            self.assertEqual(len(pin[key]), 64, key)
        self.assertNotIn("branch", pin)
        self.assertNotIn("ref", pin)
        self.assertEqual(pin["on_unavailable"], "fail-closed")
        self.assertEqual(pin["on_mismatch"], "fail-closed")
        self.assertTrue(pin["repository"].startswith("https://github.com/"))

    def test_check_passes(self) -> None:
        proc = _run_check(PIN_PATH)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("ok pin", proc.stdout)

    def test_branch_is_not_a_pin(self) -> None:
        pin = json.loads(PIN_PATH.read_text(encoding="utf-8"))
        pin["branch"] = "main"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "pin.json"
            path.write_text(json.dumps(pin), encoding="utf-8")
            proc = _run_check(path)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("must not use branch", proc.stderr)

    def test_short_ref_is_not_a_pin(self) -> None:
        pin = json.loads(PIN_PATH.read_text(encoding="utf-8"))
        pin["commit"] = "main"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "pin.json"
            path.write_text(json.dumps(pin), encoding="utf-8")
            proc = _run_check(path)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("commit must be 40-char hex", proc.stderr)

    def test_committed_skill_files_are_the_stub_only(self) -> None:
        proc = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", ".agents/skills/archify"],
            check=True,
            capture_output=True,
            text=True,
        )
        names = {Path(line).name for line in proc.stdout.splitlines() if line}
        self.assertEqual(names, {"LICENSE", "SKILL.md", "pin.json"})

    def test_pin_json_matches_skills_lock(self) -> None:
        pin = json.loads(PIN_PATH.read_text(encoding="utf-8"))
        lock = json.loads((ROOT / "skills-lock.json").read_text(encoding="utf-8"))
        skill = lock["skills"]["archify"]
        self.assertEqual(pin["commit"], skill["commit"])
        self.assertEqual(pin["tree"], skill["tree"])
        self.assertEqual(pin["skill_sha256"], skill["skill_sha256"])


if __name__ == "__main__":
    unittest.main()
