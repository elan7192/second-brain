---
id: concept:retrieval
type: concept
tags:
  - wiki
created: 2026-08-28
updated: 2026-09-01
---

# Retrieval

Hybrid search over compiled pages. Markdown stays canonical. SQLite FTS5 is disposable.

Signals: FTS5, wikilink graph, recency, type/source quality. Embeddings are not in this pass.

Command: `python3 tools/sb ask "…"`. Since 2026-09-01 `ask` rebuilds the database when any page, directory, or registry is newer than it (a 2 ms mtime scan; the rebuild itself is about 90 ms). `python3 tools/sb rebuild-index` forces one.

Do not walk [[index]] by hand when the index exists. If search is empty, the wiki is silent.

Ranking, 2026-09-01: an object found by FTS and cited by a ranked claim gets the same claim-link bonus as one reached only through the claim. Before, FTS finding it first cost it that bonus, and a gold source fell out of the top 8 when an unrelated page stopped lending it a graph boost.

See [[portable-memory]]. Do not clone Brain. Do not make the database a second memory. See [[eval-suite]] for the gate.

Paste foil: [[retrieval-second-brain]]. Hybrid BM25 + vector + GraphRAG is not this path. C25.

[[src-vault-review-2026-08-29]] rated this layer 5/10 and said there is no real retrieval. That clashes with D9. See C46. Integrity counts: `python3 tools/sb health`.

## Related

[[stable-ids]] · [[claims]] · [[llm-wiki]] · [[context-graph]] · [[tokens-as-capital]] · [[file-memory]] · [[claim-protocol]] · [[retrieval-second-brain]] · [[deterministic-core]] · [[src-vault-review-2026-08-29]]
