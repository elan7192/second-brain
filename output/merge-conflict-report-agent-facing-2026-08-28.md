---
type: ship
tags:
  - ship
created: 2026-08-28
updated: 2026-08-28
---

# Merge conflict report · agent-facing-docs vs main

Fetched `origin/main` at `c9172cf`, then merged into `cursor/agent-facing-docs-8473`.

## Simple (fixed)

Catalog and related-link unions: [[Home]], [[Today]], [[index]], [[ship]], [[twitter]], [[how-it-works]], [[log]], [[agent-operating-system]], [[context-graph]], [[llm-wiki]], [[tokens-as-capital]], [[self-verification]], [[verifiable-instructions]], [[hunt-ship-loop]], [[MEMORY]], [[Hooks]]. Graph snapshots taken from main, then regenerated.

`tools/render-obsidian-graph.py` kept main (concept islands / PNG). This branch only bumped a date.

## ID collisions (remapped, both contents kept)

This branch locked D8 (instruction files are the control surface) and D9 (bibliographic catalog only). Main already locked D8 (graph clusters by concept) and D9 (markdown canonical, FTS disposable). Contents do not fight. IDs do.

Remap, same pattern as skill-library C8–C13 → C20–C25:

- Branch D8 → **D10**. Main D8 stays graph clusters.
- Branch D9 → **D11**. Main D9 stays live query `python3 tools/sb ask`.
- Branch C8 → **C26** (file first vs code first). Main C8 stays two anti-slop tens.
- Branch C9 → **C27** (prose checks vs observed validation). Main C9 stays NGC tables.
- Branch C10 → **C28** (disclosure API 404). Main C10 stays HydroFusion years.

## Complicated (not silently picked)

**C25 vs D9.** Arrived from main via the skill-library merge. Unresolved there. Untouched here. Human yes still needed: does the park cover only GraphRAG/LangChain/vector runtimes, or does it also fight FTS5?

**C17 / C18.** Two claim tables; two retrieve CLIs. Untouched. Not created by this branch.

No decision content was dropped. D10 and D11 are new IDs for the two locks this branch added. D8 and D9 on main stay in force.
