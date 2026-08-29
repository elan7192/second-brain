"""Gates that live in code, not only in AGENTS.md."""

from __future__ import annotations

import importlib.util
from pathlib import Path

from . import frontmatter, ids
from .index import connect, rebuild
from .paths import ROOT, TOOLS_DIR, db_path
from .yamlutil import loads


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

    conn.close()
    status = "PASS" if errors == 0 else "FAIL"
    lines.append(f"{status} validate errors={errors}")
    return (0 if errors == 0 else 1), "\n".join(lines) + "\n"


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
