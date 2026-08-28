---
id: concept:context-graph
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-28
---

# Context graph

Give the model the subgraph for this decision, not the whole dump.

Source: article quoted by [[src-avid-obsidian-agent-team]].

## Claim

A 1M-token window is not a reason to fill it. The useful unit is a small set of entities, relationships, events, and prior decisions.

Vector similarity is not a causal path. "Why did Project X fail?" may need a chain across people, suppliers, and releases that chunk search never joins. Hybrid retrieve here is FTS5 plus one-hop wikilinks, not embeddings. See [[claim-protocol]] and [[retrieval]].

Local cut: `python3 tools/ontology.py subgraph <slug> --hops 1`. See [[vault-ontology]].

[[src-retrieval-second-brain]] names the same walk as GraphRAG. This vault walks compiled page links. That is a compile-time graph, not a query-time GraphRAG runtime. See [[retrieval-second-brain]] and [[contradictions]] C25.

Facts need validity windows. "Dan works on Project A" and "Dan works on Project B" can both exist in a store. Only one may be current.

## Split

- Graph: what is true, and when.
- Skills / schema: how we act.

[[src-mukul975-cybersecurity-skills]] describes the same split as a load order: scan all skill frontmatters, then load a few full workflows. Token numbers there are author-stated. This vault applies the split by compiling into [[skill-library]], not by installing that pack.

## Related

[[tokens-as-capital]] · [[llm-wiki]] · [[memory-engineering]] · [[skill-library]] · [[retrieval-second-brain]] · [[claim-protocol]] · [[hunt-ship-loop]] · [[trace]] · [[vault-ontology]]

[[trace]] treats a conversation trajectory as a context graph for attribution, then edits the named source. Same idea as a subgraph, used for repair. · [[loop-graph-engineering]]
