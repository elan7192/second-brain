---
type: ship
tags:
  - ship
created: 2026-08-28
updated: 2026-08-28
---

# Merge conflict report · maverick-ultramode ingest vs main

Fetched `origin/main` at `5927d29`, then merged into `cursor/ingest-maverick-ultramode-faac`.

## Simple (fixed)

Catalog and related-link unions: [[Home]], [[Today]], [[index]], [[twitter]], [[github]], [[ship]], [[log]], [[entropy-gate]], [[harness-routing]], [[self-verification]], [[agent-operating-system]], [[MEMORY]]. Graph snapshots regenerated from the merged wiki.

ID collision: this branch had used C8 for two Terminal-Bench lifts and C9 for the LLM-tournament apply gate. Main already used C8 for two anti-slop tens and C9 for NGC tables. Remapped to **C33** and **C34** on pages, [[contradictions]], and `wiki/data/contradictions.yaml`. Paper C8–C9 were left alone.

Add/add on `output/ingest-brief-2026-08-24.md`: main's file is the agent-facing-docs brief. This ingest's brief moved to [[ingest-brief-2026-08-24-maverick-ultramode]]. Both kept.

Layer 1 wording on [[agent-operating-system]] was pre-D9 ("compile, do not retrieve"). Kept main's D9 wording ("compile, then retrieve the compiled set") and kept the [[ultra-mode]] sentence on layer 4. That is wording, not a new decision.

## Complicated (not silently picked)

**C17 / C18 / C25** arrived from main (two claim tables; two retrieve CLIs; hybrid retrieval recipe vs D9 FTS). Untouched. Not created by this branch.

Vector DB / Neo4j / MemGPT / GraphRAG as runtime stay parked on both sides. Compatible. Do not vendor those stacks. See `MEMORY.md` Rejected installs.
