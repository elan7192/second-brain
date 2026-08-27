---
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-27
---

# LLM Wiki

Andrej Karpathy's April 2026 pattern for a personal knowledge base.

RAG re-derives knowledge on every query. A compiled wiki derives it once and keeps it current.

## Three layers

1. **Raw sources.** Immutable. Human curated. The LLM reads and never writes.
2. **Wiki.** LLM-owned markdown. Entity pages, concept pages, synthesis, index, log.
3. **Schema.** `AGENTS.md` / `CLAUDE.md`. Conventions and workflows.

## Operations

- **Ingest.** One source can update 10-15 pages. Summary, entities, concepts, index, log, claim rows.
- **Query.** Read [[index]] first. Answer with citations. File good answers back.
- **Lint.** Contradictions, stale claims, orphans, missing concept pages, stale `wiki/claims.csv`.
- **Methods.** Compile methods learned while doing work after the task. See [[src-play-methods-2026-08-25]].
- **Freshness.** Audit claims with [[stale-fact-detector]] against named sources. `raw/` stays immutable.
- **Memory system.** Provenance and FACT/INFERENCE/OPINION on new pages. See [[memory-system]].

## Why it lasts

Humans abandon wikis because maintenance grows faster than value. The LLM can touch many files in one pass. The human curates sources and directs questions.

## Related

[[tokens-as-capital]] · [[context-graph]] · [[andrej-karpathy]] · [[src-papa-couch-compiler]] · [[src-bober-folder-workflow]] · [[src-mrgreenieybt3-llm-wiki]] · [[how-it-works]] · [[grok-bot-use-cases]] · [[growth-operator]] · [[file-memory]] · [[stale-fact-detector]] · [[botdirectory-scan]] · [[portable-memory]] · [[backlink-first]] · [[memory-system]] · [[claims]] · [[untrusted-ingest]]
