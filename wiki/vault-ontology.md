---
id: concept:vault-ontology
type: concept
tags:
  - wiki
created: 2026-08-28
updated: 2026-09-01
---

# Vault ontology

Local Palantir-style Ontology compiled from this wiki. Derived output. Not a second knowledge graph.

Source: [[src-palantir-aip-developers-2026-08-28]]. Product: [[palantir-aip]]. Schema: `tools/ontology_schema.json`.

## Mapping

| Palantir | This vault |
| --- | --- |
| Foundry dataset | wiki markdown. `raw/` stays immutable and off the object table |
| Pipeline Builder | `python3 tools/rebuild-ontology.py` |
| Object types | Concept, Source, Person, Project, Meta, Map, Hunt, Ship, Decision, Contradiction |
| Links | `cites`, `aboutPerson`, `relatedTo`, `extractedFrom` |
| Actions | rebuild, lint, subgraph. Local only |
| OSDK | `python3 tools/ontology.py` |
| Hosted AIP / Developer Console | absent. D5 |

Wiki markdown stays the store. See [[llm-wiki]] and [[loop-graph-engineering]]. Do not replace pages with JSONL.

Query still goes through `python3 tools/sb ask`. See [[retrieval]] and D9. `ontology.py` is for object sets and links.

The object CSV is the one derived table. See [[file-memory]]. Do not edit `output/ontology-objects.csv` by hand.

First compile on 2026-08-28: 301 objects, 1736 links. After merge with the FTS engine: 307 objects, 1796 links. Re-run rebuild after ingest. Do not quote a stale count.

`inbound` and `outbound` both count emitted links, so their sums equal the link count. Before 2026-09-01 `outbound` counted every wikilink target, including pages the compiler skips, and was wrong on 24 objects.

## Commands

```
python3 tools/rebuild-ontology.py
python3 tools/rebuild-ontology.py --check
python3 tools/ontology.py verify
python3 tools/ontology.py counts
python3 tools/ontology.py get llm-wiki
python3 tools/ontology.py subgraph ai-sovereignty --hops 1
```

`python3 tools/sb validate` runs this `--check` since 2026-09-01. If it reports a stale ontology, rebuild from wiki. Do not patch the CSV. The check also fails on a dangling link, a degree that disagrees with the links, or a link type the schema forbids.

## Verify

`python3 tools/ontology.py verify` is the proof that the ontology works. It loads the bundle into an in-memory SQLite database and runs the checks as SQL: unique keys, both link endpoints present, `inbound`/`outbound` equal to the actual links, no isolated object. Then it attaches `.cache/secondbrain.sqlite` and compares every page-to-page edge with the FTS index, which `tools/secondbrain/index.py` derives from the same markdown through separate code. On 2026-09-01: 430 objects, 3024 links, 2270 page edges compared, 0 disagreements. The in-memory database is dropped on exit. It is not a second store (D9).

Brief: [[ontology-rebuild-brief-2026-08-28]].

## Query use

Give the model a subgraph, not the dump. See [[context-graph]]. `ontology.py subgraph` is that cut.

Unverified pages keep a boolean on the object. Do not promote those rows to facts.

## Related

[[palantir-aip]] · [[llm-wiki]] · [[file-memory]] · [[context-graph]] · [[loop-graph-engineering]] · [[ai-sovereignty]] · [[how-it-works]] · [[retrieval]] · [[src-palantir-aip-developers-2026-08-28]]
