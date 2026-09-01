"""Gates that live in code, not only in AGENTS.md."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import re
from datetime import date

from . import frontmatter, ids, provenance
from .index import connect, rebuild
from .paths import ROOT, TOOLS_DIR, db_path
from .yamlutil import loads

ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_PREFIX = re.compile(r"^\d{4}")


def validate(root: Path | None = None, db: Path | None = None) -> tuple[int, str]:
    root = root or ROOT
    lines: list[str] = []
    errors = 0

    lint_code, lint_out = _run_lint(root)
    lines.append(lint_out.rstrip())
    if lint_code != 0:
        errors += 1
        lines.append("FAIL lint-wiki missing wikilink targets")

    missing_ids = []
    for path in ids.iter_knowledge_paths(root):
        text = path.read_text(encoding="utf-8")
        meta, _ = frontmatter.split(text)
        if not meta.get("id"):
            missing_ids.append(str(path.relative_to(root)))
    if missing_ids:
        errors += 1
        lines.append(f"FAIL missing id on {len(missing_ids)} pages")
        for item in missing_ids[:20]:
            lines.append(f"  {item}")
        if len(missing_ids) > 20:
            lines.append(f"  … {len(missing_ids) - 20} more")
    else:
        lines.append("ok ids")

    target = db or db_path()
    if not target.exists():
        rebuild(root, target)
    conn = connect(target)
    dup = conn.execute(
        """
        SELECT id, COUNT(*) AS n FROM objects
        GROUP BY id HAVING n > 1
        """
    ).fetchall()
    # UNIQUE should prevent this; still check claims vs objects mismatches
    if dup:
        errors += 1
        lines.append("FAIL duplicate object ids")
        for row in dup:
            lines.append(f"  {row['id']} x{row['n']}")
    else:
        lines.append("ok unique ids")

    unknown_sources = conn.execute(
        """
        SELECT claim_sources.claim_id, claim_sources.source_id
        FROM claim_sources
        LEFT JOIN objects ON objects.id = claim_sources.source_id
        WHERE objects.id IS NULL
        """
    ).fetchall()
    if unknown_sources:
        errors += 1
        lines.append("FAIL claim sources with no object")
        for row in unknown_sources:
            lines.append(f"  {row['claim_id']} -> {row['source_id']}")
    else:
        lines.append("ok claim sources")

    unknown_concepts = conn.execute(
        """
        SELECT claim_concepts.claim_id, claim_concepts.concept_id
        FROM claim_concepts
        LEFT JOIN objects ON objects.id = claim_concepts.concept_id
        WHERE objects.id IS NULL
        """
    ).fetchall()
    if unknown_concepts:
        errors += 1
        lines.append("FAIL claim concepts with no object")
        for row in unknown_concepts:
            lines.append(f"  {row['claim_id']} -> {row['concept_id']}")
    else:
        lines.append("ok claim concepts")

    unknown_contra = conn.execute(
        """
        SELECT id, claim_a, claim_b FROM contradictions
        WHERE (claim_a != '' AND claim_a NOT IN (SELECT id FROM objects))
           OR (claim_b != '' AND claim_b NOT IN (SELECT id FROM objects))
        """
    ).fetchall()
    if unknown_contra:
        errors += 1
        lines.append("FAIL contradiction endpoints with no object")
        for row in unknown_contra:
            lines.append(f"  {row['id']} {row['claim_a']} <-> {row['claim_b']}")
    else:
        lines.append("ok contradiction endpoints")

    yaml_ids = _contradiction_yaml_codes(root)
    md_ids = _contradiction_md_codes(root)
    if yaml_ids and md_ids and yaml_ids != md_ids:
        errors += 1
        lines.append("FAIL contradictions.yaml vs wiki/contradictions.md")
        lines.append(f"  yaml {sorted(yaml_ids)}")
        lines.append(f"  md   {sorted(md_ids)}")
    else:
        lines.append("ok contradiction catalog")

    temporal_errs = _temporal_errors(conn)
    if temporal_errs:
        errors += 1
        lines.append(f"FAIL temporal fields ({len(temporal_errs)})")
        for item in temporal_errs[:20]:
            lines.append(f"  {item}")
        if len(temporal_errs) > 20:
            lines.append(f"  … {len(temporal_errs) - 20} more")
    else:
        lines.append("ok temporal fields")

    prov_errs = _provenance_errors(root, conn)
    if prov_errs:
        errors += 1
        lines.append(f"FAIL provenance ({len(prov_errs)})")
        for item in prov_errs[:20]:
            lines.append(f"  {item}")
        if len(prov_errs) > 20:
            lines.append(f"  … {len(prov_errs) - 20} more")
    else:
        lines.append("ok provenance")

    onto_errs = _ontology_errors(root)
    if onto_errs:
        errors += 1
        lines.append(f"FAIL ontology ({len(onto_errs)})")
        for item in onto_errs:
            lines.append(f"  {item}")
    else:
        lines.append("ok ontology")

    conn.close()
    status = "PASS" if errors == 0 else "FAIL"
    lines.append(f"{status} validate errors={errors}")
    return (0 if errors == 0 else 1), "\n".join(lines) + "\n"


def _temporal_errors(conn) -> list[str]:
    errors: list[str] = []
    known = {row["id"] for row in conn.execute("SELECT id FROM objects")}
    rows = conn.execute(
        """
        SELECT id, type, created, updated, valid_from, valid_until
        FROM objects
        """
    ).fetchall()
    for row in rows:
        for field in ("created", "updated", "valid_from", "valid_until"):
            value = row[field] or ""
            err = _date_error(value)
            if err:
                errors.append(f"{row['id']} {field} {err}")
        start = row["valid_from"] or ""
        end = row["valid_until"] or ""
        if ISO_DATE.match(start) and ISO_DATE.match(end) and end < start:
            errors.append(f"{row['id']} valid_until {end} before valid_from {start}")
    claim_rows = conn.execute(
        """
        SELECT id, valid_from, valid_until, observed_at, superseded_by
        FROM claims
        """
    ).fetchall()
    for row in claim_rows:
        for field in ("valid_from", "valid_until", "observed_at"):
            value = row[field] or ""
            err = _date_error(value)
            if err:
                errors.append(f"{row['id']} {field} {err}")
        successor = row["superseded_by"] or ""
        if successor and successor not in known:
            errors.append(f"{row['id']} superseded_by unknown id {successor}")
    return errors


def _date_error(value: str) -> str:
    if not value or not DATE_PREFIX.match(value):
        return ""
    if not ISO_DATE.match(value):
        return f"{value!r} is not YYYY-MM-DD"
    try:
        date.fromisoformat(value)
    except ValueError:
        return f"{value!r} is not a real date"
    return ""


def _provenance_errors(root: Path, conn) -> list[str]:
    del conn
    errors: list[str] = []
    for claim_id in provenance.yaml_missing_sources(root):
        errors.append(f"{claim_id} yaml missing sources")
    for item in provenance.csv_missing_sources(root):
        errors.append(f"{item} csv missing source")
    return errors


def _ontology_errors(root: Path) -> list[str]:
    # Fixture roots have no output/. A repo root does, and then both derived files must be fresh.
    if not (root / "output").is_dir():
        return []
    lib_path = TOOLS_DIR / "ontology_lib.py"
    spec = importlib.util.spec_from_file_location("ontology_lib", lib_path)
    if spec is None or spec.loader is None:
        return ["cannot load tools/ontology_lib.py"]
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return list(module.check_ontology(root))


def orphans(root: Path | None = None) -> str:
    root = root or ROOT
    _, out = _run_lint(root)
    rows = [line for line in out.splitlines() if line.startswith("ORPHAN ")]
    return f"{len(rows)} orphans\n" + ("\n".join(rows) + "\n" if rows else "")


def _run_lint(root: Path) -> tuple[int, str]:
    lint_path = TOOLS_DIR / "lint-wiki.py"
    spec = importlib.util.spec_from_file_location("lint_wiki", lint_path)
    if spec is None or spec.loader is None:
        return 1, "FAIL cannot load tools/lint-wiki.py"
    module = importlib.util.module_from_spec(spec)
    # lint-wiki binds ROOT to its own parent. Monkeypatch after load.
    spec.loader.exec_module(module)
    original_root = module.ROOT
    module.ROOT = root
    try:
        from io import StringIO
        from contextlib import redirect_stdout

        buf = StringIO()
        with redirect_stdout(buf):
            code = module.main()
        return code, buf.getvalue()
    finally:
        module.ROOT = original_root


def _contradiction_yaml_codes(root: Path) -> set[str]:
    path = root / "wiki" / "data" / "contradictions.yaml"
    if not path.exists():
        return set()
    data = loads(path.read_text(encoding="utf-8")) or {}
    items = data.get("contradictions") if isinstance(data, dict) else data
    codes = set()
    for item in items or []:
        if not isinstance(item, dict):
            continue
        object_id = str(item.get("id", ""))
        _, _, slug = object_id.partition(":")
        if slug:
            codes.add(slug.upper())
    return codes


def _contradiction_md_codes(root: Path) -> set[str]:
    path = root / "wiki" / "contradictions.md"
    if not path.exists():
        return set()
    import re

    return set(re.findall(r"^## (C\d+)\.", path.read_text(encoding="utf-8"), re.MULTILINE))
