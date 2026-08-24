---
type: project
tags:
  - project
created: 2026-08-24
updated: 2026-08-24
---

# arXiv potential tierlist

An arXiv paper tierlist site ranked by future development potential (runway), not citations or journal prestige.

Source: [[src-arxiv-tierlist-handoff]]. Ranking axis and formula: [[potential-ranking]].

## Corpus (2026-08-24 gap batch 6)

- Unique papers: 405856. This batch added 72800. Cursor 2022-06-08.
- Prior: 333056 (batch 5)
- Date range: 1990-01-01 to 2026-08-20
- Full-corpus tiers: S 16443 / A 42228 / B 197545 / C 113767 / D 35873
- Inventory counts. Known compiled papers are listed below, not the rest of the pile.
- Data root: `/workspace/arxiv-tierlist/`

## Known papers (BATCH01)

arxiv read these. Digest path `/workspace/arxiv-tierlist/digests/`. Source list: [[src-arxiv-batch01]].

| Paper | Page |
| --- | --- |
| 2507.08177 | [[causal-cps-anomaly]] |
| 2507.17886 | [[nmc-trace-complexity]] |
| 2507.20810 | [[flow-matching-pso]] |
| 2509.26507 | [[bdh]] |
| 2510.17928 | [[evosyn]] |

## Known papers (BATCH02)

Source list: [[src-arxiv-batch02]].

| Paper | Page |
| --- | --- |
| 2509.11016 | [[superde]] |
| 2509.21617 | [[lance]] |
| 2509.23982 | [[palrs]] |
| 2509.24844 | [[prednext]] |
| 2510.02345 | [[clustered-moe]] |

Tables 7–8 of 2510.02345 are `unverified`. Unread appendices and `.txt` extracts are not known.

## Known papers (BATCH03)

Source list: [[src-arxiv-batch03]].

| Paper | Page |
| --- | --- |
| 2510.03744 | [[hydrofusion-lmf]] |
| 2510.16851 | [[ngc]] |
| 2511.02241 | [[sapin]] |
| 2511.02864 | [[alphaevolve-math]] |
| 2511.02957 | [[pavement-gnn]] |

C9/C10 on [[contradictions]]. AlphaEvolve 6.24–6.67 not known.

## Known papers (BATCH04)

Source list: [[src-arxiv-batch04]].

| Paper | Page |
| --- | --- |
| 2511.05540 | [[tiwm]] |
| 2511.12922 | [[unitok]] |
| 2511.16485 | [[llm4eo]] |
| 2511.20500 | [[apt-siamese]] |
| 2511.20721 | [[foundry-3d]] |

C11/C12 on [[contradictions]]. OCR-unclean tables `unverified`.

## Known papers (BATCH05)

Source list: [[src-arxiv-batch05]].

| Paper | Page |
| --- | --- |
| 2512.00288 | [[portal]] |
| 2512.00341 | [[mpi-init]] |
| 2512.01249 | [[pwr-ga]] |
| 2512.02419 | [[brain-ai-convergence]] |
| 2512.03394 | [[vs-graph]] |

VS-Graph figure-only accuracy `unverified`.

## Display

The site must show all five tiers. Slice **per-tier top 800** (4000 cards) into `site/data/papers.json`. A global top-N list is all S.

Each card: title, authors, category, date, score, reason tags, abs and pdf links.

## Harvest

1. OAI-PMH `https://oaipmh.arxiv.org/oai` `metadataPrefix=arXiv` `set=cs`, oldest first. First lag of 48100 papers stopped at 2013-12.
2. Atom `https://export.arxiv.org/api/query` `sortBy=submittedDate&sortOrder=descending` added 17155 papers from 2025-06 to 2026-08 (about 2000 newest per class: cs.AI, cs.LG, cs.CL, cs.CV, cs.NE, cs.RO, cs.CR, stat.ML, cs.SE, cs.IR).
3. Remaining gap 2022-06 to 2025-06. Resume: `harvest_gap_state.json`. Next GAP_TARGET >> 325001.
4. Request interval about 3 seconds. Metadata only. No PDFs.
5. Dedup key is arXiv id. Total unique 405856.

## Ranking (essence)

`rank.py` is a keyword heuristic. No per-paper LLM. Baseline date 2026-08-23. Full write-up in `/workspace/arxiv-tierlist/RANKING.md`.

```
score = clamp(0, 100,
  38
  + recency_boost      # 0..30  last 18 months strongest
  + generality_boost   # 0..20
  + openness_boost     # 0..15
  + early_field_boost  # 0..12
  + novelty_boost      # 0..8
  - saturation_penalty # 0..28
)
```

Tiers: S ≥ 80, A ≥ 68, B ≥ 52, C ≥ 38, D < 38.

Known bias: recency overweights 2025–26 papers, so S is 16443. That is why display is per-tier, not global top-N. It is a product bias, not a source conflict.

## Public URL

Current site (2026-08-24, HTTP 200): https://elan7192.github.io/arxiv-potential-tierlist/
Repo: https://github.com/elan7192/arxiv-potential-tierlist
Same Pages URL. Local slice rebuilt. Do not assume the public page already shows 405856.

ZeroDeploy URLs are stale. Do not treat them as current. Do not record deploy tokens. Do not use `silent-wind-6359` (pre-2013 only) or `broken-flower-1108` (global top 4000, all S). Local serve: `python3 -m http.server 8765` in `site/`.

## Next priorities (from source; do not invent)

1. Fill the remaining 2022-06 to 2025-06 gap (continue OAI from harvest_gap_state.json).
2. Rescore: lower recency weight, or per-category percentile / z-score.
3. Product: search and category filters exist in draft; community vote as a second axis was not requested.

Do not re-fetch PDFs. Do not rank by citation. Do not clone extra repos; data is already on the box.
