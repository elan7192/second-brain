---
id: concept:claim-protocol
type: concept
schema: memory-v1
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-29
created_by: agent
confidence: medium
source:
  - wiki/sources/src-lan-e-claim-protocol-2026-08-27.md
derived_from:
  - src-lan-e-claim-protocol-2026-08-27
  - retrieval
  - claims
  - portable-memory
---

# Claim protocol

Named compile chain: Claim → Evidence → Verification → Retrieval → Context → Answer.

Source: [[src-lan-e-claim-protocol-2026-08-27]]. Live tools on main are [[retrieval]] (`python3 tools/sb ask`) and [[claims]] (`python3 tools/compile-claims.py`). D9 on main is markdown canonical plus disposable FTS, not this page. See C18.

## FACT

The chain is Claim → Evidence → Verification → Retrieval → Context → Answer.

Live query is `python3 tools/sb ask`. Live claim compile is `python3 tools/compile-claims.py`. Do not hand-edit `wiki/claims.csv`. Dual store with `wiki/data/claims.yaml` is C17.

Git markdown stays canonical. SQLite FTS5 is disposable. See [[portable-memory]] and D9.

## INFERENCE

Compilation can inject error before any query. A claim needs a source page and evidence before it is treated as memory. Persistence is not truth.

## OPINION

`tools/retrieve.py` and `tools/claim_protocol.py` on this branch overlap [[retrieval]]. Do not wire them as the query path. Do not delete them without a human yes. See C18.

Embeddings stay parked. See C19 and [[file-memory]].

## Check

`python3 tools/sb ask` is Query step 1 in `AGENTS.md`. `python3 tools/sb validate` matches. If evidence is missing: mark `unverified`. Do not write it into `MEMORY.md`.

## Related

[[llm-wiki]] · [[retrieval]] · [[claims]] · [[memory-engineering]] · [[memory-ablation]] · [[portable-memory]] · [[file-memory]] · [[context-graph]] · [[stale-fact-detector]] · [[entropy-gate]] · [[self-verification]] · [[src-lan-e-claim-protocol-2026-08-27]]
