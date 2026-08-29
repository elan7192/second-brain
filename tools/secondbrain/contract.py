"""Machine-readable audited task contract. Schema v1.

Statuses:
  SCHEMA_INVALID  contract does not satisfy the schema
  SCHEMA_VALID    schema ok; no task results supplied
  TASK_FAILED     schema ok; an acceptance check failed or is missing
  TASK_PASSED     schema ok; every acceptance check has a true result
"""

from __future__ import annotations

from pathlib import Path

from .yamlutil import loads

CONTRACT_VERSION = 1
SCHEMA_INVALID = "SCHEMA_INVALID"
SCHEMA_VALID = "SCHEMA_VALID"
TASK_FAILED = "TASK_FAILED"
TASK_PASSED = "TASK_PASSED"

REQUIRED = (
    "contract_version",
    "objective",
    "acceptance_checks",
    "write_scope",
    "state_version",
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
    data, errors = _load(path)
    if errors:
        return errors
    return [f"{path}: {err}" for err in check_data(data)]


def check_data(data: dict) -> list[str]:
    errors: list[str] = []
    for key in FORBIDDEN:
        if key in data:
            errors.append(f"forbidden field {key}")
    for key in REQUIRED:
        if key not in data or data[key] in (None, "", []):
            errors.append(f"missing {key}")
    version = data.get("contract_version")
    if version is not None:
        try:
            number = int(version)
        except (TypeError, ValueError):
            errors.append("contract_version must be an integer")
        else:
            if number != CONTRACT_VERSION:
                errors.append(f"unsupported contract_version {number}")
    checks = data.get("acceptance_checks")
    if checks is not None and not isinstance(checks, list):
        errors.append("acceptance_checks must be a list")
    state = data.get("state_version")
    if state is not None:
        try:
            number = int(state)
        except (TypeError, ValueError):
            errors.append("state_version must be an integer")
        else:
            if number < 1:
                errors.append("state_version must be >= 1")
    errors.extend(_check_write_scope(data.get("write_scope")))
    return errors


def evaluate(data: dict, results: dict[str, bool] | None = None) -> tuple[str, list[str]]:
    errors = check_data(data)
    if errors:
        return SCHEMA_INVALID, errors
    if results is None:
        return SCHEMA_VALID, []
    checks = [str(item) for item in (data.get("acceptance_checks") or [])]
    missing = [item for item in checks if item not in results]
    if missing:
        return TASK_FAILED, [f"missing result for {item}" for item in missing]
    failed = [item for item in checks if not results[item]]
    if failed:
        return TASK_FAILED, [f"failed {item}" for item in failed]
    return TASK_PASSED, []


def evaluate_path(path: Path, results: dict[str, bool] | None = None) -> tuple[str, list[str]]:
    data, errors = _load(path)
    if errors:
        return SCHEMA_INVALID, errors
    return evaluate(data, results)


def check_dir(root: Path) -> tuple[int, str]:
    paths = sorted(root.glob("*.yaml")) + sorted(root.glob("*.yml"))
    if not paths:
        return 0, "0 contracts\n"
    errors: list[str] = []
    for path in paths:
        errors.extend(check_path(path))
    if errors:
        return 1, "FAIL SCHEMA_INVALID\n" + "\n".join(f"  {item}" for item in errors) + "\n"
    return 0, f"SCHEMA_VALID contracts={len(paths)}\n"


def _check_write_scope(scope: object) -> list[str]:
    if scope is None:
        return []
    if isinstance(scope, str):
        return [] if scope.strip() else ["write_scope is empty"]
    if isinstance(scope, list):
        return [] if scope else ["write_scope is empty"]
    if isinstance(scope, dict):
        errors: list[str] = []
        allow = scope.get("allow")
        deny = scope.get("deny")
        if not isinstance(allow, list) or not allow:
            errors.append("write_scope.allow must be a non-empty list")
        if deny is not None and not isinstance(deny, list):
            errors.append("write_scope.deny must be a list")
        return errors
    return ["write_scope must be a string, list, or {allow, deny}"]


def _load(path: Path) -> tuple[dict, list[str]]:
    if not path.exists():
        return {}, [f"missing contract file {path}"]
    try:
        data = loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return {}, [f"{path}: yaml parse error: {exc}"]
    if not isinstance(data, dict):
        return {}, [f"{path}: contract must be a mapping"]
    return data, []
