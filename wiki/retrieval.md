---
id: concept:retrieval
type: concept
tags:
  - wiki
created: 2026-08-28
updated: 2026-08-28
---

# Retrieval

Hybrid search over compiled pages. Markdown stays canonical. SQLite FTS5 is disposable.

Signals: FTS5, wikilink graph, recency, type/source quality. Embeddings are not in this pass.

Command: `python3 tools/sb ask "…"`. Rebuild: `python3 tools/sb rebuild-index`.

Do not walk [[index]] by hand when the index exists. If the database is missing, rebuild it. If search is empty, the wiki is silent.

See [[portable-memory]]. Do not clone Brain. Do not make the database a second memory. See [[eval-suite]] for the gate.

## Related

[[stable-ids]] · [[claims]] · [[llm-wiki]] · [[context-graph]] · [[tokens-as-capital]] · [[file-memory]] · [[claim-protocol]]
