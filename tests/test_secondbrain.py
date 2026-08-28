#!/usr/bin/env python3
"""Unit tests for the second-brain memory engine. Stdlib only."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from secondbrain import frontmatter, ids, index, retrieve, yamlutil  # noqa: E402
from secondbrain.eval_suite import run_eval  # noqa: E402
from secondbrain.validate import validate  # noqa: E402


class YamlTests(unittest.TestCase):
    def test_claim_registry_shape(self) -> None:
        sample = """
claims:
  - id: claim:foo
    subject: Memory
    predicate: has
    object: provenance
    sources:
      - source:src-x
    concepts:
      - concept:y
    status: supported
"""
        data = yamlutil.loads(sample)
        self.assertEqual(data["claims"][0]["id"], "claim:foo")
        self.assertEqual(data["claims"][0]["sources"], ["source:src-x"])
        self.assertEqual(data["claims"][0]["object"], "provenance")


class FrontmatterTests(unittest.TestCase):
    def test_insert_id_preserves_body(self) -> None:
        text = "---\ntype: concept\n---\n\n# Hello\n\nBody [[link]]\n"
        new, changed = frontmatter.insert_id(text, "concept:hello")
        self.assertTrue(changed)
        self.assertTrue(new.startswith("---\nid: concept:hello\n"))
        self.assertIn("# Hello", new)
        again, changed2 = frontmatter.insert_id(new, "concept:hello")
        self.assertFalse(changed2)
        self.assertEqual(again, new)


class EngineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "wiki" / "sources").mkdir(parents=True)
        (self.root / "wiki" / "data").mkdir(parents=True)
        (self.root / "eval").mkdir()
        (self.root / "wiki" / "memory-ablation.md").write_text(
            "---\nid: concept:memory-ablation\ntype: concept\n"
            "created: 2026-08-23\nupdated: 2026-08-23\n---\n\n"
            "# Memory ablation\n\n"
            "A memory line earns its place only by deleting an answer "
            "the model would otherwise give. Source: [[src-0xcodio-memory-ablation]].\n",
            encoding="utf-8",
        )
        (self.root / "wiki" / "sources" / "src-0xcodio-memory-ablation.md").write_text(
            "---\nid: source:src-0xcodio-memory-ablation\ntype: source\n"
            "created: 2026-08-22\nupdated: 2026-08-22\n---\n\n"
            "# src-0xcodio-memory-ablation\n\n"
            "Line-level ablation. Facts survived. See [[memory-ablation]].\n",
            encoding="utf-8",
        )
        (self.root / "wiki" / "index.md").write_text(
            "---\nid: meta:index\ntype: meta\n---\n\n"
            "# Index\n\n[[memory-ablation]] [[src-0xcodio-memory-ablation]]\n",
            encoding="utf-8",
        )
        (self.root / "wiki" / "data" / "claims.yaml").write_text(
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
            "    valid_from: 2026-01-01\n"
            "    valid_until: 2026-01-02\n",
            encoding="utf-8",
        )
        (self.root / "wiki" / "data" / "contradictions.yaml").write_text(
            "contradictions: []\n",
            encoding="utf-8",
        )
        self.db = self.root / "index.sqlite"

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_rebuild_and_search(self) -> None:
        stats = index.rebuild(self.root, self.db)
        self.assertGreaterEqual(stats["objects"], 3)
        self.assertEqual(stats["claims"], 1)
        hits = retrieve.search("memory ablation", limit=5, db=self.db)
        ids_found = [h.id for h in hits]
        self.assertIn("concept:memory-ablation", ids_found)

    def test_trace_and_stale(self) -> None:
        index.rebuild(self.root, self.db)
        from secondbrain import claims

        traced = claims.trace(
            "claim:memory-line-retained-iff-changes-answer", db=self.db
        )
        self.assertIn("source:src-0xcodio-memory-ablation", traced)
        stale = claims.stale_report(self.db, today="2026-08-28")
        self.assertIn("claim:memory-line-retained-iff-changes-answer", stale)

    def test_validate_fixture(self) -> None:
        index.rebuild(self.root, self.db)
        code, out = validate(self.root, self.db)
        self.assertEqual(code, 0, out)


class LiveVaultTests(unittest.TestCase):
    def test_live_index_search(self) -> None:
        db = ROOT / ".cache" / "test-secondbrain.sqlite"
        stats = index.rebuild(ROOT, db)
        self.assertGreater(stats["objects"], 50)
        self.assertGreater(stats["claims"], 5)
        hits = retrieve.search("portable memory FTS5 disposable", limit=8, db=db)
        ids_found = [h.id for h in hits]
        self.assertTrue(
            any(item in ids_found for item in ("concept:portable-memory", "claim:fts5-index-is-disposable")),
            ids_found,
        )

    def test_live_eval_gate(self) -> None:
        db = ROOT / ".cache" / "test-secondbrain-eval.sqlite"
        code, out, scores = run_eval(root=ROOT, eval_dir=ROOT / "eval", db=db)
        self.assertEqual(code, 0, out)
        self.assertGreaterEqual(scores.retrieval_recall, 0.8)
        self.assertLessEqual(scores.unsupported_rate, 0.1)


if __name__ == "__main__":
    unittest.main()
