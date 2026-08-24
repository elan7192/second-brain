---
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-24
---
# Causal CPS anomaly detection

Vision paper, not a new detector. Treat CPS anomalies as structural breaks in a causal DAG, not residual spikes.

Source: [[src-arxiv-2507-08177]]. Project: [[arxiv-tierlist]].

## Kept

Opaque forecasting / reconstruction / GNN detectors misfire under adversarial CPS noise. Program: (1) graph-diff vs a normal graph (PC, GES, NOTEARS-style); (2) multi-view fusion; (3) continual causal graph updates under drift.

SWaT F1 0.75–0.82 vs 0.55–0.79 and WADI SMV-CGAD 0.79 are a literature table plus the authors' prior work, not a new bake-off in this PDF.

## Related

[[arxiv-tierlist]]
