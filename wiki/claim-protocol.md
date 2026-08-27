---
type: concept
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-27
---

# Claim protocol

Compile and answer through one chain: Claim → Evidence → Verification → Retrieval → Context → Answer.

Source: [[src-lan-e-claim-protocol-2026-08-27]]. Locked as D9 in [[decisions]].

## Ledger

Canonical rows live in `wiki/claims.csv`. That is the one CSV in [[file-memory]].

Each row: `id`, `claim`, `source`, `evidence`, `status`, `created_at`, `verified_at`, `wiki_page`, `supports`, `contradicts`, `supersedes`.

Statuses: `extracted` | `verified` | `unverified` | `contradicted` | `superseded`.

Evidence is a file location (`wiki/page.md#Heading` or `AGENTS.md#Query`). Provenance edges stay on the row. Do not add a second graph store. See [[loop-graph-engineering]].

## Ingest

1. Read the raw source. Do not edit `raw/`.
2. Append claim rows with source and evidence. Status starts as `extracted` or `unverified`.
3. Promote `verified` rows into wiki prose. `unverified` rows may appear only if the page marks them `unverified`.
4. `contradicted` rows go to [[contradictions]]. Do not silently pick a side.

`MEMORY.md` takes only `verified` rows that still pass [[memory-ablation]].

## Retrieval

Run `python3 tools/retrieve.py "<question>"`.

The index is disposable SQLite FTS5 under `.cache/wiki.sqlite`. Rebuild is cheap. Git markdown stays truth. See [[portable-memory]].

Score mix: BM25 with prefix rewrite, one-hop wikilinks, recency from `updated:`, source authority, verified-claim bonus, contradiction penalty.

Embeddings stay parked. See [[contradictions]] C15.

## Query

Read the ranked pages, then follow links. Do not dump the vault. That is [[context-graph]].

Cite wiki pages and claim ids. If retrieve returns nothing, say so.

## Check

`python3 tools/lint-wiki.py` exits 0. Every claims.csv row has source and evidence. `python3 tools/retrieve.py` returns existing wiki pages.

If evidence is missing: status `unverified`. Do not write the claim into `MEMORY.md`.

## Related

[[llm-wiki]] · [[memory-engineering]] · [[memory-ablation]] · [[portable-memory]] · [[file-memory]] · [[context-graph]] · [[stale-fact-detector]] · [[entropy-gate]] · [[self-verification]] · [[src-lan-e-claim-protocol-2026-08-27]]
