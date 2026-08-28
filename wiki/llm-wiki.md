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

- **Ingest.** One source updates the pages it actually changes. Source page, concepts, matching index, log, lint. No ingest brief unless lan E asked. See [[musk-algorithm]].
- **Query.** Read the short [[index]] first. Open [[index-papers]] or [[index-sources]] only when the question is a paper or a source. Answer with citations. File back only if the next session would re-derive it.
- **Lint.** Contradictions, stale claims, orphans, missing concept pages.
- **Methods.** Compile methods learned while doing work after the task. See [[src-play-methods-2026-08-25]].
- **Freshness.** Audit claims with [[stale-fact-detector]] against named sources. `raw/` stays immutable.

## Why it lasts

Humans abandon wikis because maintenance grows faster than value. The LLM can touch many files in one pass. The human curates sources and directs questions.

## Related

[[tokens-as-capital]] · [[context-graph]] · [[andrej-karpathy]] · [[src-papa-couch-compiler]] · [[src-bober-folder-workflow]] · [[src-mrgreenieybt3-llm-wiki]] · [[how-it-works]] · [[grok-bot-use-cases]] · [[growth-operator]] · [[file-memory]] · [[stale-fact-detector]] · [[botdirectory-scan]] · [[portable-memory]] · [[backlink-first]]
