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

## Corpus (2026-08-23 UTC snapshot)

- Unique papers: 66555
- Date range: 1990-01-01 to 2026-08-20
- Full-corpus tiers: S 15051 / A 3418 / B 17758 / C 20746 / D 9582
- Data root: `/workspace/arxiv-tierlist/`

## Display

The site must show all five tiers. Slice **per-tier top 800** (4000 cards) into `site/data/papers.json`. A global top-N list is all S.

Each card: title, authors, category, date, score, reason tags, abs and pdf links.

## Harvest

1. OAI-PMH `https://oaipmh.arxiv.org/oai` `metadataPrefix=arXiv` `set=cs`, oldest first. First lag of 48100 papers stopped at 2013-12.
2. Atom `https://export.arxiv.org/api/query` `sortBy=submittedDate&sortOrder=descending` added 17155 papers from 2025-06 to 2026-08 (about 2000 newest per class: cs.AI, cs.LG, cs.CL, cs.CV, cs.NE, cs.RO, cs.CR, stat.ML, cs.SE, cs.IR).
3. Gap remains about 2014 to mid 2025.
4. Request interval about 3 seconds. Metadata only. No PDFs.
5. Dedup key is arXiv id. `seen_ids.txt` has 66555 lines.

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

Known bias: recency overweights 2025–26 papers, so S is 15051. That is why display is per-tier, not global top-N. It is a product bias, not a source conflict.

## Public URL

Current site (2026-08-24, HTTP 200): https://elan7192.github.io/arxiv-potential-tierlist/
Repo: https://github.com/elan7192/arxiv-potential-tierlist

ZeroDeploy URLs are stale. Do not treat them as current. Do not record deploy tokens. Do not use `silent-wind-6359` (pre-2013 only) or `broken-flower-1108` (global top 4000, all S). Local serve: `python3 -m http.server 8765` in `site/`.

## Next priorities (from source; do not invent)

1. Fill the 2014–mid-2025 gap (continue OAI or yearly/category Atom).
2. Rescore: lower recency weight, or per-category percentile / z-score.
3. Product: search and category filters exist in draft; community vote as a second axis was not requested.

Do not re-fetch PDFs. Do not rank by citation. Do not clone extra repos; data is already on the box.
