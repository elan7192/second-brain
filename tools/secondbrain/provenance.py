"""Claim-level source provenance. Two registries stay two projections (C17)."""

from __future__ import annotations

import csv
from pathlib import Path

from .yamlutil import loads


def yaml_missing_sources(root: Path) -> list[str]:
    path = root / "wiki" / "data" / "claims.yaml"
    if not path.exists():
        return []
    data = loads(path.read_text(encoding="utf-8")) or {}
    items = data.get("claims") if isinstance(data, dict) else data
    missing: list[str] = []
    for item in items or []:
        if not isinstance(item, dict):
            continue
        claim_id = str(item.get("id") or "?")
        sources = item.get("sources") or []
        if isinstance(sources, str):
            sources = [sources]
        sources = [str(src).strip() for src in sources if str(src).strip()]
        if not sources:
            missing.append(claim_id)
    return missing


def csv_missing_sources(root: Path) -> list[str]:
    path = root / "wiki" / "claims.csv"
    if not path.exists():
        return []
    missing: list[str] = []
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            claim_id = row.get("claim_id") or "?"
            source = (row.get("source") or "").strip()
            if not source:
                missing.append(claim_id)
                continue
            if source.startswith(("wiki/", "raw/")) and not (root / source).exists():
                missing.append(f"{claim_id}->{source}")
    return missing


def counts(root: Path) -> dict[str, int]:
    yaml_gap = yaml_missing_sources(root)
    csv_gap = csv_missing_sources(root)
    return {
        "yaml_no_provenance": len(yaml_gap),
        "csv_no_provenance": len(csv_gap),
        "claims_without_provenance": len(yaml_gap) + len(csv_gap),
    }
