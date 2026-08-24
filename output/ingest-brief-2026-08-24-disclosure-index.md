---
type: ship
tags:
  - ship
created: 2026-08-24
updated: 2026-08-24
---

# Ingest brief · Disclosure Index · 2026-08-24

The `#api` page documents a REST catalog. The live data is `data/catalog.js`.

## What changed

Parsed 11,338 public disclosure records into [[disclosure-index]] and `output/disclosure-index-stats-2026-08-23.json`. Locked D9: bibliographic stats only. Flagged C10: `/api/reports` and `/api/stats` returned 404.

## What linked

[[src-disclosure-index]] now points at [[disclosure-index]], C10, and D9. Hunt index: [[disclosures]].

## What to look at

1. [[disclosure-index]] for the compiled counts.
2. C10 before calling the documented REST API.
3. D9 before asking for report bodies or exploit steps.
