---
type: ship
tags:
  - ship
created: 2026-08-28
updated: 2026-08-28
---

# Merge conflict report · entropy-gate quiz vs main

Fetched `origin/main` at `c5714e8`, then merged into `cursor/entropy-gate-quiz-b17d`.

## Simple (fixed)

One file conflicted: [[log]]. Both sides appended. Frontmatter `id: meta:log` and `updated: 2026-08-28` kept from main. This branch's two 2026-08-24 query entries sit after [[graph-clusters-2026-08-24]] and before the 2026-08-23 skill/retrieval ingest block.

New files from this branch merged clean: [[query-entropy-gate]], [[query-skills-and-slop]].

C3 on main is still the 200-agent clip vs 64-worker table. The entropy quiz answer still cites the right flag.

## Complicated (not silently picked)

**C25 vs D9.** Arrived from main. Hybrid retrieval recipe vs live query `python3 tools/sb ask` on compiled markdown with disposable FTS5. This branch did not reopen it.

**Dated quiz snapshots vs current catalog.** [[query-skills-and-slop]] says the vault had nine X posts and no personal skill inventory. That was true on 2026-08-24. Main now has skill-library ingest, C8 (two anti-slop tens), and D9. Left the 2026-08-24 answers unedited so they stay a snapshot, not a silent rewrite.

**C17 / C18** arrived from main. Untouched.
