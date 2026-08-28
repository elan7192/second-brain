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
    link_type_for,
    links_for,
    search_objects,
    subgraph,
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


if __name__ == "__main__":
    unittest.main()
