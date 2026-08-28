---
id: concept:llm-wiki
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-28
---

# LLM Wiki

Andrej Karpathy's April 2026 pattern for a personal knowledge base.

RAG re-derives knowledge on every query. A compiled wiki derives it once and keeps it current.

## Three layers

1. **Raw sources.** Immutable. Human curated. The LLM reads and never writes.
2. **Wiki.** LLM-owned markdown. Entity pages, concept pages, synthesis, index, log.
3. **Schema.** `AGENTS.md` / `CLAUDE.md`. Conventions and workflows.

## Operations

- **Ingest.** One source can update 10-15 pages. Summary, entities, concepts, index, log, YAML claim rows, CSV compile rows.
- **Query.** Run `python3 tools/sb ask`. Answer from the evidence set. File good answers back.
- **Lint.** `python3 tools/sb validate`. Also `python3 tools/compile-claims.py --check`. Contradictions, stale claims, orphans, missing ids, injection phrases.
- **Methods.** Compile methods learned while doing work after the task. See [[src-play-methods-2026-08-25]].
- **Freshness.** Audit claims with [[stale-fact-detector]] against named sources. `raw/` stays immutable.
- **Memory system.** Provenance and FACT/INFERENCE/OPINION on new pages. See [[memory-system]]. Dual claim store is C17.
- **Ontology.** Compile objects and links with `tools/rebuild-ontology.py`. See [[vault-ontology]]. Do not treat the CSV as the wiki.

## Why it lasts

Humans abandon wikis because maintenance grows faster than value. The LLM can touch many files in one pass. The human curates sources and directs questions.

## Related

[[tokens-as-capital]] · [[context-graph]] · [[andrej-karpathy]] · [[src-papa-couch-compiler]] · [[src-bober-folder-workflow]] · [[src-mrgreenieybt3-llm-wiki]] · [[how-it-works]] · [[grok-bot-use-cases]] · [[growth-operator]] · [[file-memory]] · [[stale-fact-detector]] · [[botdirectory-scan]] · [[portable-memory]] · [[backlink-first]] · [[memory-system]] · [[claims]] · [[untrusted-ingest]] · [[retrieval]] · [[stable-ids]] · [[vault-ontology]] · [[palantir-aip]]
