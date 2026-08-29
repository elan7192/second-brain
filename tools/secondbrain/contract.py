"""Machine-readable audited task contract. Prose stays on the wiki page."""

from __future__ import annotations

from pathlib import Path

from .yamlutil import loads

REQUIRED = ("objective", "acceptance_checks", "write_scope", "state_version")
OPTIONAL = (
    "accepted_commit",
    "decisions",
    "failed_approaches",
    "blockers",
    "phase",
    "constraints",
    "assigned_route",
)
FORBIDDEN = frozenset(
    {
        "transcript",
        "transcripts",
        "secrets",
        "tool_dumps",
        "chat",
        "adjectives",
    }
)


def check_path(path: Path) -> list[str]:
    if not path.exists():
        return [f"missing contract file {path}"]
    text = path.read_text(encoding="utf-8")
    try:
        data = loads(text)
    except Exception as exc:  # noqa: BLE001
        return [f"{path}: yaml parse error: {exc}"]
    if not isinstance(data, dict):
        return [f"{path}: contract must be a mapping"]
    return [f"{path}: {err}" for err in check_data(data)]


def check_data(data: dict) -> list[str]:
    errors: list[str] = []
    for key in FORBIDDEN:
        if key in data:
            errors.append(f"forbidden field {key}")
    for key in REQUIRED:
        if key not in data or data[key] in (None, "", []):
            errors.append(f"missing {key}")
    checks = data.get("acceptance_checks")
    if checks is not None and not isinstance(checks, list):
        errors.append("acceptance_checks must be a list")
    version = data.get("state_version")
    if version is not None:
        try:
            number = int(version)
        except (TypeError, ValueError):
            errors.append("state_version must be an integer")
        else:
            if number < 1:
                errors.append("state_version must be >= 1")
    scope = data.get("write_scope")
    if scope is not None and not isinstance(scope, (str, list)):
        errors.append("write_scope must be a string or list")
    return errors


def check_dir(root: Path) -> tuple[int, str]:
    paths = sorted(root.glob("*.yaml")) + sorted(root.glob("*.yml"))
    if not paths:
        return 0, "0 contracts\n"
    errors: list[str] = []
    for path in paths:
        errors.extend(check_path(path))
    if errors:
        return 1, "FAIL contract-check\n" + "\n".join(f"  {item}" for item in errors) + "\n"
    return 0, f"ok contracts={len(paths)}\n"
