#!/usr/bin/env python3
"""Instruction line ceilings and anti-append Never-rule gate.

Called from tools/lint-wiki.py, which python3 tools/sb validate already runs.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from secondbrain.yamlutil import loads  # noqa: E402

BUDGET_DIR = Path("eval") / "instruction-budget"
CEILINGS_NAME = "ceilings.yaml"
CASES_DIRNAME = "cases"
NEVER_RE = re.compile(
    r"^\s*(?:[-*+]\s+)?(?:Never\b|Do not\b|Don't\b|Do-not\b|Don\u2019t\b)",
    re.I,
)
REASON_RE = re.compile(
    r"\b(because|why|so that|which means|the reason|belongs there)\b",
    re.I,
)


def line_count(text: str) -> int:
    if not text:
        return 0
    return text.count("\n") + (0 if text.endswith("\n") else 1)


def is_never_line(line: str) -> bool:
    return bool(NEVER_RE.match(line))


def classify_edit(old: str, new: str) -> dict[str, object]:
    old_lines = old.splitlines()
    new_lines = new.splitlines()
    old_set = set(old_lines)
    new_set = set(new_lines)
    added = [ln for ln in new_lines if ln not in old_set]
    removed = [ln for ln in old_lines if ln not in new_set]
    added_never = [ln for ln in added if is_never_line(ln)]
    removed_principle = [ln for ln in removed if ln.strip()]
    append_only_never = bool(added_never) and not removed_principle
    return {
        "append_only_never": append_only_never,
        "added_never": added_never,
        "removed": removed_principle,
        "added": added,
    }


def feedback_errors(feedback: str, trusted: bool) -> list[str]:
    errors: list[str] = []
    if not trusted:
        errors.append("feedback is not from a trusted reviewer")
    text = (feedback or "").strip()
    if not text:
        errors.append("feedback is empty")
    elif not REASON_RE.search(text):
        errors.append("feedback missing a specific reason")
    return errors


def check_proposal(old: str, new: str, feedback: str, trusted: bool) -> list[str]:
    errors = feedback_errors(feedback, trusted)
    classified = classify_edit(old, new)
    if classified["append_only_never"]:
        errors.append("append-only never-rule; fold or edit an existing principle")
    return errors


def check_ceilings(root: Path) -> list[str]:
    path = root / BUDGET_DIR / CEILINGS_NAME
    if not path.exists():
        return []
    data = loads(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        return [f"{BUDGET_DIR}/{CEILINGS_NAME} must be a map of path -> max lines"]
    errors: list[str] = []
    for rel, ceiling in data.items():
        target = root / str(rel)
        if not target.exists():
            continue
        try:
            max_lines = int(ceiling)
        except (TypeError, ValueError):
            errors.append(f"{rel} ceiling {ceiling!r} is not an int")
            continue
        n = line_count(target.read_text(encoding="utf-8"))
        if n > max_lines:
            errors.append(f"{rel} lines={n} exceeds ceiling={max_lines}")
    return errors


def run_fixtures(root: Path) -> list[str]:
    cases = root / BUDGET_DIR / CASES_DIRNAME
    if not cases.is_dir():
        return []
    errors: list[str] = []
    for case_dir in sorted(p for p in cases.iterdir() if p.is_dir()):
        errors.extend(_run_case(case_dir))
    return errors


def _run_case(case_dir: Path) -> list[str]:
    slug = case_dir.name
    meta_path = case_dir / "meta.yaml"
    before_path = case_dir / "before.md"
    after_path = case_dir / "after.md"
    feedback_path = case_dir / "feedback.txt"
    missing = [
        name
        for name, path in (
            ("meta.yaml", meta_path),
            ("before.md", before_path),
            ("after.md", after_path),
            ("feedback.txt", feedback_path),
        )
        if not path.exists()
    ]
    if missing:
        return [f"fixture {slug} missing {', '.join(missing)}"]
    meta = loads(meta_path.read_text(encoding="utf-8")) or {}
    if not isinstance(meta, dict):
        return [f"fixture {slug} meta.yaml must be a map"]
    expect = str(meta.get("expect") or "").strip().lower()
    trusted = bool(meta.get("trusted"))
    proposal_errors = check_proposal(
        before_path.read_text(encoding="utf-8"),
        after_path.read_text(encoding="utf-8"),
        feedback_path.read_text(encoding="utf-8"),
        trusted,
    )
    if expect == "fail":
        if not proposal_errors:
            return [f"fixture {slug} should have failed"]
        return []
    if expect == "pass":
        if proposal_errors:
            return [f"fixture {slug}: {'; '.join(proposal_errors)}"]
        return []
    return [f"fixture {slug} expect must be pass or fail"]


def check(root: Path | None = None) -> list[str]:
    root = root or ROOT
    errors: list[str] = []
    errors.extend(check_ceilings(root))
    errors.extend(run_fixtures(root))
    return errors


def main() -> int:
    errors = check(ROOT)
    if errors:
        for item in errors:
            print(f"FAIL {item}")
        return 1
    print("ok instruction-budget")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
