---
type: ship
tags:
  - ship
created: 2026-08-28
updated: 2026-08-28
---

# Merge conflict report · chatgpt-share ingest vs main

Fetched `origin/main` at `96f7138` (Omarsar `#6` already on main), then merged into `cursor/ingest-chatgpt-share-ff83`.

## Simple (fixed)

Catalog and related-link unions: [[index]], [[log]], [[llm-wiki]], [[entropy-gate]], `MEMORY.md`, [[arxiv-tierlist]].

ID collision: this branch had used C14 for the ChatGPT upgraded snapshot vs GitHub wiki. Main C14 is eptwts $100k / 10 months. Remapped to **C36** on pages, [[contradictions]], and `wiki/data/contradictions.yaml`. Eptwts C14 left alone.

Local vault zip later delivered to Drive is a different file. Not applied. Wiki stays frozen except this merge remap.

## Complicated (not silently picked)

**C17 / C18 / C25** arrived from main (two claim tables; two retrieve CLIs; hybrid retrieval recipe vs D9 FTS). Untouched. Not created by this branch.

The ChatGPT share ZIP (`second-brain-upgraded-2026-08-25.zip`) is still 401/403. Do not reconstruct 100 papers from the claim list.

## Gate

`python3 tools/lint-wiki.py` exit 0. `python3 tools/sb.py validate` PASS. Ontology rebuilt.
