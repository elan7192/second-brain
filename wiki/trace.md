---
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-24
---

# TRACE

TRajectory Attribution for Automated Context Engineering. Amazon authors Zhao, Misra, Pandey. KDD 2026. Paper: https://arxiv.org/abs/2608.09153

Source: [[src-marfinxx-trace]].

Repair the context layer (prompts, KB, tools, skills) from historical trajectories. Do not retrain the model.

## Four pieces

1. Implicit dissatisfaction in traces (corrections, rephrase, abandonment).
2. Delta-guided holistic attribution. Trajectory as a context graph. One LLM pass. Paper: 16x fewer calls than iterative TextGrad-style.
3. Exploratory verification. Agent reads the named files before CRUD. Paper: 83% vs 33% on KB GAP vs STALE.
4. Six-category fault taxonomy on a synthetic 60-trace set.

## Paper numbers

On 60 synthetic DSAT traces: 72.7% node attribution, 82% fix effectiveness, 96% operation accuracy.

Eval is simulated with ground truth. Not production Amazon logs.

Tweet claims 84% autonomous fix, 76% less debug time, 4.2x fewer tokens are `unverified`.

## Related

[[context-graph]] · [[memory-engineering]] · [[tokens-as-capital]]
