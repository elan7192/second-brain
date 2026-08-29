"""Knowledge integrity dashboard. Counts only. Does not replace validate."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from . import claims as claims_mod
from . import frontmatter, ids, validate
from .index import connect, rebuild
from .paths import ROOT, db_path
from .yamlutil import loads


def report(root: Path | None = None, db: Path | None = None) -> str:
    root = root or ROOT
    target = db or db_path()
    if not target.exists():
        rebuild(root, target)
    conn = connect(target)
    try:
        page_n = conn.execute(
            "SELECT COUNT(*) FROM objects WHERE type NOT IN ('claim')"
        ).fetchone()[0]
        yaml_rows = conn.execute("SELECT status FROM claims").fetchall()
        yaml_status = Counter((row["status"] or "").lower() or "unset" for row in yaml_rows)
        contra_rows = conn.execute("SELECT status FROM contradictions").fetchall()
        contra_status = Counter(
            (row["status"] or "").lower() or "unset" for row in contra_rows
        )
    finally:
        conn.close()

    csv_status, csv_conf = _csv_counts(root)
    stale_n = _count_stale(target)
    missing, orphans = _link_health(root)
    missing_ids = _missing_ids(root)
    yaml_ids, csv_ids = _claim_id_sets(root)
    gate_code, _ = validate.validate(root, target)

    lines = [
        "Knowledge health",
        f"pages                 {page_n}",
        f"yaml_claims           {sum(yaml_status.values())}"
        + _bucket(yaml_status, ("supported", "disputed", "contradicted", "stale", "superseded")),
        f"csv_claims            {sum(csv_status.values())}"
        + _bucket(csv_status, ("active", "disputed", "deprecated", "unknown")),
        f"csv_unverified_conf   {csv_conf.get('unverified', 0)}",
        f"contradictions        {sum(contra_status.values())}"
        + _bucket(contra_status, ("unresolved", "resolved", "unverified", "open")),
        f"stale_objects         {stale_n}",
        f"orphans               {len(orphans)}",
        f"broken_wikilinks      {len(missing)}",
        f"missing_ids           {len(missing_ids)}",
        "dual_store            C17 both present; "
        f"yaml={len(yaml_ids)} csv={len(csv_ids)} id_overlap={len(yaml_ids & csv_ids)}",
        f"gate                  {'PASS' if gate_code == 0 else 'FAIL'}",
    ]
    return "\n".join(lines) + "\n"


def _bucket(counter: Counter[str], keys: tuple[str, ...]) -> str:
    parts = [f"{key}={counter.get(key, 0)}" for key in keys]
    extra = sorted(k for k in counter if k not in keys)
    parts.extend(f"{key}={counter[key]}" for key in extra)
    return "  " + " ".join(parts) if parts else ""


def _csv_counts(root: Path) -> tuple[Counter[str], Counter[str]]:
    path = root / "wiki" / "claims.csv"
    status: Counter[str] = Counter()
    conf: Counter[str] = Counter()
    if not path.exists():
        return status, conf
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            status[(row.get("status") or "").lower() or "unset"] += 1
            conf[(row.get("confidence") or "").lower() or "unset"] += 1
    return status, conf


def _count_stale(db: Path) -> int:
    text = claims_mod.stale_report(db)
    first = text.splitlines()[0] if text else "0"
    try:
        return int(first.split()[0])
    except ValueError:
        return 0


def _link_health(root: Path) -> tuple[list[str], list[str]]:
    lint_code, lint_out = validate._run_lint(root)
    del lint_code
    missing = [line[8:] for line in lint_out.splitlines() if line.startswith("MISSING ")]
    orphans = [line[7:] for line in lint_out.splitlines() if line.startswith("ORPHAN ")]
    return missing, orphans


def _missing_ids(root: Path) -> list[str]:
    missing: list[str] = []
    for path in ids.iter_knowledge_paths(root):
        text = path.read_text(encoding="utf-8")
        meta, _ = frontmatter.split(text)
        if not meta.get("id"):
            missing.append(str(path.relative_to(root)))
    return missing


def _claim_id_sets(root: Path) -> tuple[set[str], set[str]]:
    yaml_ids: set[str] = set()
    path = root / "wiki" / "data" / "claims.yaml"
    if path.exists():
        data = loads(path.read_text(encoding="utf-8")) or {}
        items = data.get("claims") if isinstance(data, dict) else data
        for item in items or []:
            if isinstance(item, dict) and item.get("id"):
                yaml_ids.add(str(item["id"]))
    csv_ids: set[str] = set()
    csv_path = root / "wiki" / "claims.csv"
    if csv_path.exists():
        with csv_path.open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                if row.get("claim_id"):
                    csv_ids.add(row["claim_id"])
    return yaml_ids, csv_ids
