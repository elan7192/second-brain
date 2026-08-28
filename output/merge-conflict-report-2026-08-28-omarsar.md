---
type: ship
tags:
  - ship
created: 2026-08-28
updated: 2026-08-28
---

# Merge conflict report · omarsar-adversarial-review ingest vs main

Fetched `origin/main` at `4be06ef` (Maverick `#5` already on main), then merged into `cursor/ingest-omarsar-adversarial-review-faac`.

## Simple (fixed)

Catalog and related-link unions: [[Home]], [[Today]], [[index]], [[twitter]], [[ship]], [[log]], [[entropy-gate]], [[audited-task-contract]], [[self-verification]], [[agent-operating-system]], `MEMORY.md`. Graph snapshots regenerated from the merged wiki.

Maverick pages already on main (`[[ultra-mode]]`, [[maverick]], PPT, source). Kept main's copies (ids plus C33/C34). This branch's pre-remap C8/C9 text was dropped in favor of those.

ID collision: this branch had used C10 for Self-Refine vs N-candidate verify. Main C10 is HydroFusion years. Remapped to **C35** on pages, [[contradictions]], and `wiki/data/contradictions.yaml`. HydroFusion C10 left alone.

Add/add on `output/ingest-brief-2026-08-24.md`: kept main's agent-facing-docs brief. This ingest already had [[ingest-brief-omarsar-2026-08-24]].

Layer 1 wording on [[agent-operating-system]] was pre-D9. Kept main's D9 wording and kept the [[adversarial-review]] sentence on layer 3.

## Complicated (not silently picked)

**C17 / C18 / C25** arrived from main (two claim tables; two retrieve CLIs; hybrid retrieval recipe vs D9 FTS). Untouched. Not created by this branch.

Vector DB / Neo4j / MemGPT / GraphRAG as runtime stay parked on both sides. Compatible. Do not vendor those stacks. See `MEMORY.md` Rejected installs.

## Gate

`python3 tools/lint-wiki.py` exit 0. `python3 tools/sb.py validate` PASS. Graph snapshot regenerated (`skip png`: PIL not installed).
