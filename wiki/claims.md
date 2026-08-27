---
type: concept
schema: memory-v1
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-27
created_by: agent
confidence: high
source:
  - wiki/file-memory.md
  - wiki/llm-wiki.md
  - wiki/contradictions.md
derived_from:
  - file-memory
  - llm-wiki
  - contradictions
---

# Claims

The rebuildable evidence layer. Source pages stay human-readable. `wiki/claims.csv` is the table an agent can lint and recompile. Extra vault-level rows live in [[curated-claims]]. See [[memory-system]].

## FACT

Each row has `claim_id`, `kind` (fact / inference / opinion), `status` (active / deprecated / disputed / unknown), `confidence`, `text`, `source`, `raw`, `url`, `created_at`, `updated_at`, `created_by`, `derived_from`, `pages`.

Source `## Claims kept` paragraphs compile to `kind=fact`. If the paragraph says `unverified`, confidence is `unverified`.

`wiki/contradictions.md` stays the conflict ledger. The compiler does not pick a winner. Disputed claim rows must put a `C#` id in `pages` so they join that ledger. Example: [[ngc]] C9 rows `c-ngc-mmlu-table1` and `c-ngc-mmlu-table3`.

## INFERENCE

A wiki page can be rebuilt from claims plus synthesis. Today only the CSV is mechanically rebuilt. Concept prose is still agent-compiled. That is Phase 2, not Phase 7.

## OPINION

Keep one CSV. Do not add a second JSONL graph or a vector index for retrieval. See [[file-memory]] and [[loop-graph-engineering]].

## Check

`python3 tools/compile-claims.py` writes `wiki/claims.csv`. `python3 tools/compile-claims.py --check` and `python3 tools/lint-wiki.py` fail on stale or invalid tables.

If a statement cannot be tied to a source page or to [[curated-claims]]: leave it out.

## Related

[[provenance]] · [[epistemic-labels]] · [[contradictions]] · [[untrusted-ingest]] · [[file-memory]] · [[stale-fact-detector]]
