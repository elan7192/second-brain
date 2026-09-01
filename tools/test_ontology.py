#!/usr/bin/env python3
"""Tests for the local Palantir-style ontology compiler."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ontology_lib import (  # noqa: E402
    check_ontology,
    compile_ontology,
    get_object,
    integrity_errors,
    link_type_for,
    links_for,
    search_objects,
    subgraph,
    verify,
    write_ontology,
)


MINI = {
    "wiki/index.md": """---
type: meta
---
# Index

| Page | One line |
| --- | --- |
| [[alpha]] | Alpha concept. |
""",
    "wiki/alpha.md": """---
type: concept
created: 2026-08-28
updated: 2026-08-28
---
# Alpha

Wraps a model. See [[src-palantir]] and [[karp]]. Claim is `unverified`.
""",
    "wiki/sources/src-palantir.md": """---
type: source
---
# src-palantir

- URL: https://www.palantir.com/aip/developers/

See [[alpha]].
""",
    "wiki/people/karp.md": """---
type: person
---
# Karp

See [[alpha]].
""",
    "wiki/contradictions.md": """---
type: meta
---
# Contradictions

## C1. Test clash

[[alpha]] vs the source. Resolution: `unverified`.
""",
    "decisions.md": """---
type: meta
---
# Decisions

## D1. Compiler vault

Use wiki markdown. Source: [[alpha]].
""",
}


def write_mini(root: Path) -> None:
    for rel, text in MINI.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    (root / "output").mkdir(exist_ok=True)


class OntologyCompileTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        write_mini(self.root)
        self.bundle = compile_ontology(self.root)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_object_types(self) -> None:
        self.assertEqual(get_object(self.bundle, "alpha")["objectType"], "Concept")
        self.assertEqual(get_object(self.bundle, "src-palantir")["objectType"], "Source")
        self.assertEqual(get_object(self.bundle, "karp")["objectType"], "Person")
        self.assertEqual(get_object(self.bundle, "D1")["objectType"], "Decision")
        self.assertEqual(get_object(self.bundle, "C1")["objectType"], "Contradiction")

    def test_index_one_liner(self) -> None:
        self.assertEqual(get_object(self.bundle, "alpha")["oneLiner"], "Alpha concept.")

    def test_unverified_flag(self) -> None:
        self.assertTrue(get_object(self.bundle, "alpha")["unverified"])
        self.assertTrue(get_object(self.bundle, "C1")["unverified"])
        self.assertFalse(get_object(self.bundle, "src-palantir")["unverified"])

    def test_cites_and_person_links(self) -> None:
        kinds = {(link["from"], link["linkType"], link["to"]) for link in self.bundle["links"]}
        self.assertIn(("alpha", "cites", "src-palantir"), kinds)
        self.assertIn(("alpha", "aboutPerson", "karp"), kinds)
        self.assertIn(("C1", "extractedFrom", "contradictions"), kinds)
        self.assertIn(("D1", "extractedFrom", "decisions"), kinds)

    def test_link_type_helper(self) -> None:
        self.assertEqual(link_type_for("Concept", "Source"), "cites")
        self.assertEqual(link_type_for("Concept", "Person"), "aboutPerson")
        self.assertEqual(link_type_for("Concept", "Concept"), "relatedTo")

    def test_search_and_subgraph(self) -> None:
        hits = search_objects(self.bundle, "palantir")
        self.assertTrue(any(obj["primaryKey"] == "src-palantir" for obj in hits))
        graph = subgraph(self.bundle, "alpha", hops=1)
        keys = {obj["primaryKey"] for obj in graph["objects"]}
        self.assertIn("src-palantir", keys)
        self.assertIn("karp", keys)

    def test_check_detects_stale_csv(self) -> None:
        write_ontology(self.bundle, self.root)
        self.assertEqual(check_ontology(self.root), [])
        csv_path = self.root / "output" / "ontology-objects.csv"
        csv_path.write_text("primaryKey\nbroken\n", encoding="utf-8")
        errors = check_ontology(self.root)
        self.assertTrue(any("CSV stale" in err for err in errors))

    def test_degrees_count_emitted_links_only(self) -> None:
        # alpha links to src-palantir and karp (both objects) and nothing else.
        alpha = get_object(self.bundle, "alpha")
        outbound = [link for link in self.bundle["links"] if link["from"] == "alpha"]
        self.assertEqual(alpha["outbound"], len(outbound))
        total_out = sum(obj["outbound"] for obj in self.bundle["objects"])
        total_in = sum(obj["inbound"] for obj in self.bundle["objects"])
        self.assertEqual(total_out, len(self.bundle["links"]))
        self.assertEqual(total_in, len(self.bundle["links"]))

    def test_dangling_target_does_not_inflate_outbound(self) -> None:
        (self.root / "wiki" / "alpha.md").write_text(
            "---\ntype: concept\n---\n# Alpha\n\nSee [[src-palantir]] and [[nowhere]].\n",
            encoding="utf-8",
        )
        bundle = compile_ontology(self.root)
        self.assertEqual(get_object(bundle, "alpha")["outbound"], 1)
        self.assertEqual(integrity_errors(bundle), [])

    def test_integrity_errors_catch_corruption(self) -> None:
        self.assertEqual(integrity_errors(self.bundle), [])
        broken = json.loads(json.dumps(self.bundle))
        broken["links"].append({"from": "alpha", "linkType": "relatedTo", "to": "ghost"})
        broken["objects"][0]["inbound"] += 1
        broken["links"].append({"from": "src-palantir", "linkType": "extractedFrom", "to": "karp"})
        errors = integrity_errors(broken)
        self.assertTrue(any("missing endpoint" in err for err in errors))
        self.assertTrue(any("inbound/outbound disagree" in err for err in errors))
        self.assertTrue(any("extractedFrom links Source -> Person" in err for err in errors))

    def test_verify_sqlite_passes_and_detects_duplicates(self) -> None:
        errors, counts = verify(self.bundle, db_path=self.root / "missing.sqlite")
        self.assertEqual(errors, [])
        self.assertEqual(counts["objects"], len(self.bundle["objects"]))
        self.assertEqual(counts["dangling_dst"], 0)
        self.assertEqual(counts["index_compared"], 0)
        broken = json.loads(json.dumps(self.bundle))
        broken["objects"].append(dict(broken["objects"][0]))
        errors, _ = verify(broken, db_path=self.root / "missing.sqlite")
        self.assertTrue(any("duplicate primaryKey" in err for err in errors))

    def test_rebuild_keeps_built_at_when_unchanged(self) -> None:
        write_ontology(self.bundle, self.root)
        json_path = self.root / "output" / "ontology.json"
        first = json_path.read_bytes()
        later = dict(self.bundle, builtAt="2999-01-01T00:00:00Z")
        write_ontology(later, self.root)
        self.assertEqual(json_path.read_bytes(), first)

    def test_query_helpers_use_adjacency(self) -> None:
        links = links_for(self.bundle, "alpha")
        self.assertEqual({l["to"] for l in links["outbound"]}, {"src-palantir", "karp"})
        self.assertEqual(
            {l["from"] for l in links["inbound"]},
            {"index", "src-palantir", "karp", "C1", "D1", "contradictions", "decisions"},
        )
        two = subgraph(self.bundle, "D1", hops=2)
        self.assertIn("src-palantir", {obj["primaryKey"] for obj in two["objects"]})
        self.assertEqual(links_for(self.bundle, "nope"), {"outbound": [], "inbound": []})


class VaultIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.bundle = compile_ontology(ROOT)

    def test_known_pages(self) -> None:
        wiki = get_object(self.bundle, "llm-wiki")
        self.assertIsNotNone(wiki)
        self.assertEqual(wiki["objectType"], "Concept")
        src = get_object(self.bundle, "src-papa-couch-compiler")
        self.assertEqual(src["objectType"], "Source")
        self.assertIsNotNone(get_object(self.bundle, "D5"))
        self.assertIsNotNone(get_object(self.bundle, "C9"))

    def test_tokens_cite_papa(self) -> None:
        links = links_for(self.bundle, "tokens-as-capital")
        cites = {(link["linkType"], link["to"]) for link in links["outbound"]}
        self.assertIn(("cites", "src-papa-couch-compiler"), cites)

    def test_hosted_aip_off(self) -> None:
        self.assertFalse(self.bundle["hostedAip"])
        schema = json.loads((ROOT / "tools" / "ontology_schema.json").read_text(encoding="utf-8"))
        self.assertFalse(schema["hostedAip"])
        self.assertEqual(schema["sourceOfTruth"], "wiki markdown")

    def test_vault_integrity_and_index_agreement(self) -> None:
        self.assertEqual(integrity_errors(self.bundle), [])
        db = ROOT / ".cache" / "secondbrain.sqlite"
        sys.path.insert(0, str(ROOT / "tools"))
        from secondbrain import index as sb_index

        sb_index.ensure(ROOT, db)
        errors, counts = verify(self.bundle, db_path=db)
        self.assertEqual(errors, [])
        self.assertGreater(counts["index_compared"], 1000)
        self.assertEqual(counts["links_only_in_index"], 0)
        self.assertEqual(counts["links_only_in_ontology"], 0)


if __name__ == "__main__":
    unittest.main()
