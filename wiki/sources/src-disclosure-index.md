---
id: source:src-disclosure-index
type: source
tags:
  - hunt
created: 2026-08-24
updated: 2026-08-28
---

# src-disclosure-index

- Raw: none. URL ingest. `raw/` is human-owned.
- URL: https://bug-bounty-disclosures.vercel.app/#api
- Catalog: https://bug-bounty-disclosures.vercel.app/data/catalog.js
- Site updated: 2026-08-23
- Fetched: 2026-08-24

## Claims kept

Public bibliographic catalog of platform disclosures, platform-associated writeups, and published audit results. Footer and parsed catalog both say 11,338 records.

Live data is `window.DISCLOSURE_REPORTS` in `data/catalog.js`. Documented `GET /api/reports` and `GET /api/stats` returned 404 on 2026-08-24. See [[contradictions]] C28.

The archive stores metadata and canonical URLs. It does not copy report bodies. Site note: educational and research use only. It does not grant permission to test third-party systems.

Compiled counts: `output/disclosure-index-stats-2026-08-23.json`.

## Pages updated

[[disclosure-index]] · [[contradictions]]
