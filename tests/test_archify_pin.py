#!/usr/bin/env python3
"""Pin and commit-boundary checks for Archify."""

from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN_PATH = ROOT / ".agents" / "skills" / "archify" / "pin.json"
REQUIRED = ("name", "upstream", "commit", "version", "license", "skill_path", "cli")


class ArchifyPinTest(unittest.TestCase):
    def test_pin_fields(self) -> None:
        pin = json.loads(PIN_PATH.read_text(encoding="utf-8"))
        for key in REQUIRED:
            self.assertTrue(pin.get(key), key)
        commit = pin["commit"]
        self.assertEqual(len(commit), 40)
        self.assertEqual(pin["name"], "archify")
        self.assertEqual(pin["license"], "MIT")
        self.assertTrue(pin["upstream"].startswith("https://github.com/"))

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
        self.assertEqual(pin["version"], skill["version"])


if __name__ == "__main__":
    unittest.main()
