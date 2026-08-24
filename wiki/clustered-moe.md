---
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-24
---
# Clustered low-rank MoE

Cluster experts, store mean base plus rank-r residuals. 12-layer d=768 toy, not a production MoE LLM.

Source: [[src-arxiv-2510-02345]]. Project: [[arxiv-tierlist]].

## Kept

188M vs Switch 875M. GLUE 83.5 vs 85.1. WikiText PPL 26.8 vs 24.5. Abstract "matches standard MoE" is looser than the table.

Tables 7–8 incomplete. Those scores are `unverified`.

## Related

[[arxiv-tierlist]]
