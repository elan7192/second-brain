---
type: concept
tags:
  - project
created: 2026-08-24
updated: 2026-08-24
---

# Potential ranking

The sort axis for [[arxiv-tierlist]] is future potential / room for further development, not quality, correctness, citations, or journal prestige. A 2017 Transformer ranking below a 2026 open-ended agent preprint is intended.

Source: [[src-arxiv-tierlist-handoff]].

## Formula (baseline 2026-08-23)

```
score = clamp(0, 100,
  38
  + recency_boost      # 0..30
  + generality_boost   # 0..20
  + openness_boost     # 0..15
  + early_field_boost  # 0..12
  + novelty_boost      # 0..8
  - saturation_penalty # 0..28
)
```

Tiers: S ≥ 80, A ≥ 68, B ≥ 52, C ≥ 38, D < 38.

Computed by `rank.py`. No per-paper LLM.

## Known bias

Recency is too strong on 2025–26 papers, so the S bucket is 15094. Global top-N looks like all S. Display must stay per-tier top 800, or later lower recency / use within-category relative scores.
