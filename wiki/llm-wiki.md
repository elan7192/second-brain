---
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-23
---

# LLM Wiki

Andrej Karpathy's April 2026 pattern for a personal knowledge base.

RAG re-derives knowledge on every query. A compiled wiki derives it once and keeps it current.

## Three layers

1. **Raw sources.** Immutable. Human curated. The LLM reads and never writes.
2. **Wiki.** LLM-owned markdown. Entity pages, concept pages, synthesis, index, log.
3. **Schema.** `AGENTS.md` / `CLAUDE.md`. Conventions and workflows.

## Operations

- **Ingest.** One source can update 10-15 pages. Summary, entities, concepts, index, log.
- **Query.** Read [[index]] first. Answer with citations. File good answers back.
- **Lint.** Contradictions, stale claims, orphans, missing concept pages.

## Why it lasts

Humans abandon wikis because maintenance grows faster than value. The LLM can touch many files in one pass. The human curates sources and directs questions.

A company skill catalog in Notion, or a GitHub folder of agent skills, is a product claim. Neither replaces this compiler. A local SOP does, if compiled here. See [[skill-library]], [[skill-as-sop]], and [[contradictions]] C8.

[[src-retrieval-second-brain]] is the retrieval foil: hybrid search, GraphRAG, layered memory, agentic routing. Query path here stays compile-then-read. See [[retrieval-second-brain]] and C13.

## Related

[[tokens-as-capital]] · [[andrej-karpathy]] · [[src-papa-couch-compiler]] · [[src-bober-folder-workflow]] · [[how-it-works]] · [[skill-library]] · [[retrieval-second-brain]]
