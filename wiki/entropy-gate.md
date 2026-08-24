---
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-24
---

# Entropy gate

Unverified cross-talk is how swarms agree on bugs that never existed.

Source: [[src-hitu-entropy-engineering]]. [[src-maverick-ultramode]] uses isolated worktrees and structured diffs. [[src-omarsar-adversarial-review]] reports diminishing returns from adding agents, and false consensus when they talk.

## Prefer these numbers

64 Claude Haiku workers, one synthesis model.

| Setup | Hallucination index | Cost / run |
| --- | --- | --- |
| Full shared memory | 0.658 | $4.12 |
| Complete isolation | 0.492 | — |
| Entropy-gated diffs | 0.463 | $1.73 |

Author: isolation beat free talk. Gating beat both. Cost down 58% vs shared memory.

The 200-agent, 20-second, 100% coverage clip is `unverified`. See [[contradictions]] C3.

## Four conditions

1. Isolated worktrees.
2. Structured diffs only.
3. Objective gate outside the LLM.
4. Kill and reseed one node without restarting the fleet.

## Gate

Compare assertion maps and embedding drift. On the author's code-refactor calibration, drift > 0.28 means purge. Creative tasks need a higher threshold (~0.55) or the gate thrashes.

Unanimous ungated agreement was wrong in 41% of 50 runs.

## What [[ultra-mode]] adds

Isolated worktrees and diffs-only ranking match conditions 1 and 2. The apply gate is an LLM win-rate margin, not an objective check outside the model. Confidence is noisy. See [[contradictions]] C9.

## What [[adversarial-review]] adds

A third source for "more agents is the wrong default." LiveCodeBench: 3-agent AR 87%, 5-agent MARS 82%. Naive reviewer-critic talk produced false consensus (SWE-PRBench F1 0.457). Explicit disagreement types recovered 0.533. Inner loop exchanges review text only. That is a structured channel, still an LLM gate.

## Related

[[audited-task-contract]] · [[self-verification]] · [[memory-engineering]] · [[ultra-mode]] · [[adversarial-review]]
