---
id: ship:merge-conflict-report-2026-08-29-jerry-two-pass
type: ship
tags:
  - ship
created: 2026-08-29
updated: 2026-08-29
---

# Merge conflict report · Jerry two-pass vs main

Fetched `origin/main` at `dbf957b`, then merged into `cursor/ingest-jerry-two-pass-2f90`.

## Simple (fixed)

Unions kept main’s later pages and this branch’s Jerry Liu ingest. Short [[index]] door stays (D12). Source prepended to [[index-sources]]. Concept [[two-pass-document-processing]] added to the Concepts table. Person [[jerry-liu]] added.

Related links restored on [[agent-operating-system]], [[harness-routing]], [[tokens-as-capital]], [[llm-wiki]], [[context-graph]], [[graph]], [[Home]], [[hunt]] / [[twitter]], [[ship]], and [[Hooks]].

Generated graph files taken from main, then regenerated.

## ID collision (remapped, both contents kept)

This branch used C8 for compile-once wiki vs two-pass RAG. Main already uses C8 for two anti-slop tens.

- Branch C8 → **C44**. Main C8 stays two anti-slop tens.

## Filename collision (renamed, both briefs kept)

Both sides added `output/ingest-brief-2026-08-24.md`. Main’s file is the DAIR agent-facing-docs brief. This branch’s Jerry brief moved to [[ingest-brief-2026-08-24-jerry-two-pass]]. Main [[ingest-brief-2026-08-24]] left in place (C38: do not delete existing briefs).

## Complicated (not silently picked)

**C17. Two claim registries.** `wiki/data/claims.yaml` vs `wiki/claims.csv`. Untouched.

**C18. Two retrieve engines.** Live query is `python3 tools/sb ask`. `tools/retrieve.py` stays parked. Untouched.

**C25. Retrieval paste vs D9 FTS.** Untouched.

**C37. Musk short index as query path vs D9 `sb ask`.** This merge does not reopen D9. Catalog split stays D12.

**C38. Standing ingest brief vs musk skip.** Frozen: do not add a new standing-brief rule; do not delete existing briefs; wait for lan E. This file is a merge-conflict report, not a new standing-brief rule.
