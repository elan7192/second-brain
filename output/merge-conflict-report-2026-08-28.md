---
type: ship
tags:
  - ship
created: 2026-08-28
updated: 2026-08-28
---

# Merge conflict report · skill-library ingest vs main

Fetched `origin/main` at the claim-protocol / D9 commit, then merged into `cursor/skill-library-ingest-955f`.

## Simple (fixed)

Catalog and related-link unions: [[Home]], [[Today]], [[index]], [[ship]], [[github]], [[anti-slop]], [[tokens-as-capital]], [[verifiable-instructions]], [[context-graph]], [[harness-routing]], [[memory-engineering]], [[llm-wiki]], [[how-it-works]], [[log]]. Graph snapshots regenerated from the merged wiki.

ID collision: this branch had used C8–C13 for skill-library flags. Main already used C8–C13 for anti-slop tens and arXiv papers. Remapped to C20–C25 on pages, [[contradictions]], `wiki/data/contradictions.yaml`, and the 2026-08-23 skill ingest log lines only. Paper C8–C13 were left alone.

`maps/Hooks.md` “compile, do not retrieve” was pre-D9 wording. Rewritten to compile, then retrieve the compiled set (D9). That is wording, not a new decision.

## Complicated (not silently picked)

**C25 vs D9.** This ingest compiled a hybrid BM25 + vector + GraphRAG + MemGPT/Letta/LangChain/LlamaIndex recipe onto [[retrieval-second-brain]]. Main locked D9: live query is `python3 tools/sb ask` on compiled markdown with disposable FTS5. AGENTS.md, [[retrieval]], and [[agent-operating-system]] stay on D9. C25 stays unresolved: does the park cover only GraphRAG/LangChain/vector runtimes, or does it also fight FTS5? Human yes needed.

**C17 / C18** arrived from main (two claim tables; two retrieve CLIs). Untouched. Not created by this branch.

Vector DB / Neo4j / MemGPT / GraphRAG as runtime stay parked on both sides. Compatible. Do not vendor those stacks. See `MEMORY.md` Rejected installs.
