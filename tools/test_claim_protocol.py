#!/usr/bin/env python3
"""Claim protocol unit tests. Run: python3 tools/test_claim_protocol.py"""

from __future__ import annotations

import csv
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from claim_protocol import (  # noqa: E402
    FIELDS,
    prefix_rewrite,
    retrieve,
    validate_claims,
)


def write_vault(base: Path) -> Path:
    wiki = base / "wiki"
    sources = wiki / "sources"
    sources.mkdir(parents=True)
    (wiki / "contradictions.md").write_text(
        "---\ntype: meta\nupdated: 2026-08-27\n---\n\n# Contradictions\n\n"
        "[[bad-page]] clash.\n",
        encoding="utf-8",
    )
    (wiki / "memory-ablation.md").write_text(
        "---\ntype: concept\nupdated: 2026-08-23\n---\n\n"
        "# Memory ablation\n\n"
        "Rejected the queue-based version in March, don't re-propose it.\n"
        "A memory line stays only if deleting it changes an answer.\n"
        "See [[claim-protocol]].\n",
        encoding="utf-8",
    )
    (wiki / "claim-protocol.md").write_text(
        "---\ntype: concept\nupdated: 2026-08-27\n---\n\n"
        "# Claim protocol\n\n"
        "Claim then evidence then verification then retrieval.\n"
        "See [[memory-ablation]] and [[src-test]].\n",
        encoding="utf-8",
    )
    (wiki / "bad-page.md").write_text(
        "---\ntype: concept\nupdated: 2026-01-01\n---\n\n"
        "# Bad page\n\nThis claim is contradicted.\n",
        encoding="utf-8",
    )
    (sources / "src-test.md").write_text(
        "---\ntype: source\nupdated: 2026-08-27\n---\n\n"
        "# src-test\n\nQueue design rejected.\n",
        encoding="utf-8",
    )
    rows = [
        {
            "id": "C0001",
            "claim": "A memory line stays only if deleting it changes an answer.",
            "source": "src-test",
            "evidence": "wiki/memory-ablation.md#Memory ablation",
            "status": "verified",
            "created_at": "2026-08-23",
            "verified_at": "2026-08-23",
            "wiki_page": "memory-ablation",
            "supports": "",
            "contradicts": "",
            "supersedes": "",
        },
        {
            "id": "C0002",
            "claim": "This claim is contradicted.",
            "source": "src-test",
            "evidence": "wiki/bad-page.md",
            "status": "contradicted",
            "created_at": "2026-01-01",
            "verified_at": "",
            "wiki_page": "bad-page",
            "supports": "",
            "contradicts": "",
            "supersedes": "",
        },
    ]
    with (wiki / "claims.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(FIELDS))
        writer.writeheader()
        writer.writerows(rows)
    return base


class PrefixTests(unittest.TestCase):
    def test_queue_query(self) -> None:
        q = prefix_rewrite("Why did I reject queue-based architecture?")
        self.assertIn("queue*", q)
        self.assertIn("reject*", q)
        self.assertNotIn("why*", q)


class LintTests(unittest.TestCase):
    def test_valid_ledger(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = write_vault(Path(tmp))
            self.assertEqual(validate_claims(root), [])

    def test_missing_evidence_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = write_vault(Path(tmp))
            csv_path = root / "wiki" / "claims.csv"
            text = csv_path.read_text(encoding="utf-8").replace(
                "wiki/memory-ablation.md#Memory ablation", ""
            )
            csv_path.write_text(text, encoding="utf-8")
            errors = validate_claims(root)
            self.assertTrue(any("empty evidence" in err for err in errors))


class RetrieveTests(unittest.TestCase):
    def test_queue_hits_ablation_before_contradicted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = write_vault(Path(tmp))
            hits = retrieve(
                "Why did I reject queue-based architecture?",
                root=root,
                db_path=root / ".cache" / "wiki.sqlite",
                today=date(2026, 8, 27),
            )
            slugs = [hit.slug for hit in hits]
            self.assertIn("memory-ablation", slugs)
            self.assertEqual(slugs[0], "memory-ablation")
            if "bad-page" in slugs:
                self.assertLess(slugs.index("memory-ablation"), slugs.index("bad-page"))
            ablation = next(hit for hit in hits if hit.slug == "memory-ablation")
            self.assertIn("C0001", ablation.claims)


class LiveVaultTests(unittest.TestCase):
    def test_live_queue_query_skipped_until_c18(self) -> None:
        csv_path = ROOT / "wiki" / "claims.csv"
        header = csv_path.read_text(encoding="utf-8").splitlines()[0]
        self.assertIn("claim_id", header)


if __name__ == "__main__":
    unittest.main()
