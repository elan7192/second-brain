#!/usr/bin/env python3
"""Adversarial tests for ingest, validate, health, and contract gates."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import memorylib  # noqa: E402
from secondbrain import contract, health, index, ingest_check  # noqa: E402
from secondbrain.validate import validate  # noqa: E402


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _valid_contract() -> dict:
    return {
        "contract_version": 1,
        "objective": "ingest a source",
        "acceptance_checks": ["python3 tools/sb validate"],
        "write_scope": {"allow": ["wiki/"], "deny": ["raw/"]},
        "state_version": 1,
    }


class GateFixture(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.db = self.root / "index.sqlite"
        self._build_valid()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _build_valid(self) -> None:
        _write(
            self.root / "wiki" / "memory-ablation.md",
            "---\nid: concept:memory-ablation\ntype: concept\n"
            "created: 2026-08-23\nupdated: 2026-08-23\n---\n\n"
            "# Memory ablation\n\nSource: [[src-0xcodio-memory-ablation]].\n",
        )
        _write(
            self.root / "wiki" / "sources" / "src-0xcodio-memory-ablation.md",
            "---\nid: source:src-0xcodio-memory-ablation\ntype: source\n"
            "created: 2026-08-22\nupdated: 2026-08-22\n---\n\n"
            "# src-0xcodio-memory-ablation\n\n"
            "See [[memory-ablation]].\n\n"
            "## Claims kept\n\n- Facts survived.\n",
        )
        _write(
            self.root / "wiki" / "index.md",
            "---\nid: meta:index\ntype: meta\n---\n\n"
            "# Index\n\n[[memory-ablation]] [[src-0xcodio-memory-ablation]]\n",
        )
        _write(
            self.root / "wiki" / "index-sources.md",
            "---\nid: meta:index-sources\ntype: meta\n---\n\n"
            "# Index sources\n\n[[src-0xcodio-memory-ablation]]\n",
        )
        _write(
            self.root / "wiki" / "data" / "claims.yaml",
            "claims:\n"
            "  - id: claim:memory-line-retained-iff-changes-answer\n"
            "    subject: Memory line\n"
            "    predicate: retained_iff\n"
            "    object: deleting it changes an answer\n"
            "    sources:\n"
            "      - source:src-0xcodio-memory-ablation\n"
            "    concepts:\n"
            "      - concept:memory-ablation\n"
            "    status: supported\n"
            "    valid_from: 2026-08-22\n",
        )
        _write(self.root / "wiki" / "data" / "contradictions.yaml", "contradictions: []\n")
        csv_text, errors = memorylib.compile_tables(self.root)
        if errors:
            raise RuntimeError(errors)
        _write(self.root / "wiki" / "claims.csv", csv_text)

    def _rebuild(self) -> None:
        if self.db.exists():
            self.db.unlink()
        index.rebuild(self.root, self.db)

    def test_valid_vault_passes_all_gates(self) -> None:
        self._rebuild()
        code, out = validate(self.root, self.db)
        self.assertEqual(code, 0, out)
        hcode, hout = health.report(self.root, self.db)
        self.assertEqual(hcode, 0, hout)
        self.assertIn("claims_without_provenance 0", hout)
        icode, iout = ingest_check.check("src-0xcodio-memory-ablation", self.root)
        self.assertEqual(icode, 0, iout)

    def test_agents_skill_markdown_is_not_a_wiki_orphan(self) -> None:
        _write(
            self.root / ".agents" / "skills" / "archify" / "SKILL.md",
            "# Archify\n\nSkill body. Not a wiki page.\n",
        )
        self._rebuild()
        code, out = validate(self.root, self.db)
        self.assertEqual(code, 0, out)
        self.assertNotIn("ORPHAN SKILL", out)

    def test_missing_id_fails_ingest(self) -> None:
        path = self.root / "wiki" / "sources" / "src-0xcodio-memory-ablation.md"
        text = path.read_text(encoding="utf-8").replace(
            "id: source:src-0xcodio-memory-ablation\n", ""
        )
        path.write_text(text, encoding="utf-8")
        code, out = ingest_check.check("src-0xcodio-memory-ablation", self.root)
        self.assertEqual(code, 1, out)
        self.assertIn("missing id", out)

    def test_missing_claims_kept_fails_ingest(self) -> None:
        path = self.root / "wiki" / "sources" / "src-0xcodio-memory-ablation.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("## Claims kept", "## Notes"),
            encoding="utf-8",
        )
        code, out = ingest_check.check("src-0xcodio-memory-ablation", self.root)
        self.assertEqual(code, 1, out)
        self.assertIn("Claims kept", out)

    def test_missing_index_row_fails_ingest(self) -> None:
        (self.root / "wiki" / "index-sources.md").write_text(
            "---\nid: meta:index-sources\ntype: meta\n---\n\n# Index sources\n\n",
            encoding="utf-8",
        )
        code, out = ingest_check.check("src-0xcodio-memory-ablation", self.root)
        self.assertEqual(code, 1, out)
        self.assertIn("index-sources", out)

    def test_missing_inbound_link_fails_ingest(self) -> None:
        (self.root / "wiki" / "index.md").write_text(
            "---\nid: meta:index\ntype: meta\n---\n\n# Index\n\n[[memory-ablation]]\n",
            encoding="utf-8",
        )
        (self.root / "wiki" / "memory-ablation.md").write_text(
            "---\nid: concept:memory-ablation\ntype: concept\n"
            "created: 2026-08-23\nupdated: 2026-08-23\n---\n\n"
            "# Memory ablation\n\nNo source link.\n",
            encoding="utf-8",
        )
        code, out = ingest_check.check("src-0xcodio-memory-ablation", self.root)
        self.assertEqual(code, 1, out)
        self.assertIn("inbound", out)

    def test_missing_compiled_claim_fails_ingest(self) -> None:
        (self.root / "wiki" / "claims.csv").write_text(
            "claim_id,kind,status,confidence,text,source,raw,url,"
            "created_at,updated_at,created_by,derived_from,pages\n",
            encoding="utf-8",
        )
        code, out = ingest_check.check("src-0xcodio-memory-ablation", self.root)
        self.assertEqual(code, 1, out)
        self.assertIn("compiled claim", out)

    def test_bad_valid_until_fails_validate(self) -> None:
        path = self.root / "wiki" / "data" / "claims.yaml"
        path.write_text(
            path.read_text(encoding="utf-8") + "    valid_until: 2025-01-01\n",
            encoding="utf-8",
        )
        self._rebuild()
        code, out = validate(self.root, self.db)
        self.assertEqual(code, 1, out)
        self.assertIn("valid_until", out)

    def test_unknown_superseded_by_fails_validate(self) -> None:
        path = self.root / "wiki" / "data" / "claims.yaml"
        text = path.read_text(encoding="utf-8")
        path.write_text(text + "    superseded_by: claim:does-not-exist\n", encoding="utf-8")
        self._rebuild()
        code, out = validate(self.root, self.db)
        self.assertEqual(code, 1, out)
        self.assertIn("superseded_by", out)

    def test_malformed_iso_date_fails_validate(self) -> None:
        path = self.root / "wiki" / "memory-ablation.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("created: 2026-08-23", "created: 2026-13-40"),
            encoding="utf-8",
        )
        self._rebuild()
        code, out = validate(self.root, self.db)
        self.assertEqual(code, 1, out)
        self.assertIn("2026-13-40", out)

    def test_yaml_claim_without_source_fails_validate(self) -> None:
        _write(
            self.root / "wiki" / "data" / "claims.yaml",
            "claims:\n"
            "  - id: claim:orphan-fact\n"
            "    subject: Orphan\n"
            "    predicate: has\n"
            "    object: no source\n"
            "    status: supported\n",
        )
        self._rebuild()
        code, out = validate(self.root, self.db)
        self.assertEqual(code, 1, out)
        self.assertIn("missing sources", out)

    def test_health_fails_after_deliberate_corruption(self) -> None:
        self._rebuild()
        code, out = health.report(self.root, self.db)
        self.assertEqual(code, 0, out)
        page = self.root / "wiki" / "memory-ablation.md"
        page.write_text(
            page.read_text(encoding="utf-8") + "\nSee [[page-that-does-not-exist]].\n",
            encoding="utf-8",
        )
        self._rebuild()
        code, out = health.report(self.root, self.db)
        self.assertEqual(code, 1, out)
        self.assertIn("gate                  FAIL", out)
        self.assertIn("broken_wikilinks      1", out)

    def test_pass_then_mutate_id_fails(self) -> None:
        self._rebuild()
        code, _ = validate(self.root, self.db)
        self.assertEqual(code, 0)
        icode, _ = ingest_check.check("src-0xcodio-memory-ablation", self.root)
        self.assertEqual(icode, 0)
        path = self.root / "wiki" / "sources" / "src-0xcodio-memory-ablation.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "id: source:src-0xcodio-memory-ablation\n", ""
            ),
            encoding="utf-8",
        )
        icode, out = ingest_check.check("src-0xcodio-memory-ablation", self.root)
        self.assertEqual(icode, 1, out)


class ContractGateTests(unittest.TestCase):
    def test_secret_field_fails(self) -> None:
        data = _valid_contract()
        data["secrets"] = {"token": "x"}
        errors = contract.check_data(data)
        self.assertTrue(any("forbidden" in err for err in errors))
        status, _ = contract.evaluate(data)
        self.assertEqual(status, contract.SCHEMA_INVALID)

    def test_transcript_field_fails(self) -> None:
        data = _valid_contract()
        data["transcript"] = "full chat"
        status, errors = contract.evaluate(data)
        self.assertEqual(status, contract.SCHEMA_INVALID)
        self.assertTrue(any("forbidden" in err for err in errors))

    def test_missing_contract_version_fails(self) -> None:
        data = _valid_contract()
        del data["contract_version"]
        status, errors = contract.evaluate(data)
        self.assertEqual(status, contract.SCHEMA_INVALID)
        self.assertTrue(any("contract_version" in err for err in errors))

    def test_schema_valid_without_results(self) -> None:
        status, errors = contract.evaluate(_valid_contract())
        self.assertEqual(status, contract.SCHEMA_VALID)
        self.assertEqual(errors, [])

    def test_task_failed_when_check_false(self) -> None:
        status, errors = contract.evaluate(
            _valid_contract(), {"python3 tools/sb validate": False}
        )
        self.assertEqual(status, contract.TASK_FAILED)
        self.assertTrue(errors)

    def test_task_passed_when_checks_true(self) -> None:
        status, errors = contract.evaluate(
            _valid_contract(), {"python3 tools/sb validate": True}
        )
        self.assertEqual(status, contract.TASK_PASSED)
        self.assertEqual(errors, [])

    def test_write_scope_requires_allow(self) -> None:
        data = _valid_contract()
        data["write_scope"] = {"deny": ["raw/"]}
        errors = contract.check_data(data)
        self.assertTrue(any("allow" in err for err in errors))


class DualStoreTests(unittest.TestCase):
    def test_id_mismatch_is_not_a_validate_failure(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        root = Path(tmp.name)
        db = root / "index.sqlite"
        _write(
            root / "wiki" / "memory-ablation.md",
            "---\nid: concept:memory-ablation\ntype: concept\n"
            "created: 2026-08-23\nupdated: 2026-08-23\n---\n\n"
            "# Memory ablation\n\n[[src-x]]\n",
        )
        _write(
            root / "wiki" / "sources" / "src-x.md",
            "---\nid: source:src-x\ntype: source\n"
            "created: 2026-08-22\nupdated: 2026-08-22\n---\n\n"
            "# src-x\n\n[[memory-ablation]]\n\n"
            "## Claims kept\n\n- A is B.\n",
        )
        _write(
            root / "wiki" / "index.md",
            "---\nid: meta:index\ntype: meta\n---\n\n# Index\n\n[[memory-ablation]] [[src-x]]\n",
        )
        _write(
            root / "wiki" / "data" / "claims.yaml",
            "claims:\n"
            "  - id: claim:yaml-only-id\n"
            "    subject: A\n"
            "    predicate: is\n"
            "    object: B\n"
            "    sources:\n"
            "      - source:src-x\n"
            "    status: supported\n",
        )
        _write(root / "wiki" / "data" / "contradictions.yaml", "contradictions: []\n")
        csv_text, errors = memorylib.compile_tables(root)
        if errors:
            raise RuntimeError(errors)
        _write(root / "wiki" / "claims.csv", csv_text)
        index.rebuild(root, db)
        code, out = validate(root, db)
        self.assertEqual(code, 0, out)
        hcode, hout = health.report(root, db)
        self.assertEqual(hcode, 0, hout)
        self.assertIn("two_projections", hout)
        self.assertIn("id_overlap=0", hout)
        tmp.cleanup()


if __name__ == "__main__":
    unittest.main()
