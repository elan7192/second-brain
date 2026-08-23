# Source: Couch on the second brain as a compiler

- URL: https://x.com/papa_couch/status/2090924446924026162
- Author: papa_couch
- Date: 2026-08-21
- Quoted: rvaniaaaa, "The Second Brain Is Not a Storage System. It's a Compiler." (https://x.com/i/article/2090496192136290304)

## Tweet

305,000 tokens VS 47,000 tokens.

Same task, same knowledge, the only difference is whether the system remembers what it already figured out.

Their model treats tokens as capital, not a per-query bill: one time ingestion cost gets amortized across every future lookup, good answers get written back into the wiki's synthesis pages, and outside search results get folded into the relevant entity pages instead of vanishing after one use.

Projected 30 day savings: 54% to 81%, depending on how concentrated your topics are.

## Quoted article claims

Most second brains are filing cabinets. That is retrieval, and retrieval has a ceiling.

Karpathy's April 2026 LLM Wiki: RAG re-derives knowledge on every query. A compiled wiki derives it once and keeps it current.

Architecture:

- `raw/` is the input buffer, not the brain.
- `wiki/` is where compilation happens. One source can touch 10-15 pages.
- `output/` is built from compiled knowledge.
- `CLAUDE.md` is a living compiled profile, read every session.

Why wikis rot: maintenance burden. Karpathy: collecting is effortless. Keeping fifty interlinked notes current is the work no human sustains.

Honest limits:

- Garbage in becomes garbage compiled, not just garbage retrieved. A bad source can touch many pages.
- Value shows after roughly 50-100 well-compiled sources.
- Scheduled file-system loops need a paid desktop agent in the author's setup.

Ingest prompt they publish: read the new raw file, extract concepts and claims, write wiki articles, link related pages, flag contradictions, summarize what changed in three sentences.
