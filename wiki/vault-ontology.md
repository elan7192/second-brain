---
type: concept
tags:
  - wiki
created: 2026-08-28
updated: 2026-08-28
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

The object CSV is the one derived table. See [[file-memory]]. Do not edit `output/ontology-objects.csv` by hand.

First compile on 2026-08-28: 301 objects, 1736 links. Re-run rebuild after ingest. Do not quote a stale count.

## Commands

```
python3 tools/rebuild-ontology.py
python3 tools/rebuild-ontology.py --check
python3 tools/ontology.py counts
python3 tools/ontology.py get llm-wiki
python3 tools/ontology.py subgraph ai-sovereignty --hops 1
```

`--check` must exit 0 after ingest. If it fails, rebuild from wiki. Do not patch the CSV.

Brief: [[ontology-rebuild-brief-2026-08-28]].

## Query use

Give the model a subgraph, not the dump. See [[context-graph]]. `ontology.py subgraph` is that cut.

Unverified pages keep a boolean on the object. Do not promote those rows to facts.

## Related

[[palantir-aip]] · [[llm-wiki]] · [[file-memory]] · [[context-graph]] · [[loop-graph-engineering]] · [[ai-sovereignty]] · [[how-it-works]] · [[src-palantir-aip-developers-2026-08-28]]
