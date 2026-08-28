---
type: ship
tags:
  - ship
created: 2026-08-24
updated: 2026-08-24
---

# Query · What is the entropy piece about?

Human quiz, 2026-08-24. Answer compiled from wiki, not from `raw/`.

## Answer

[[entropy-gate]] is Hitu's swarm-isolation method: unverified cross-talk makes agents agree on bugs that never existed. Prefer the 64-worker table. Mark the 200-agent clip `unverified`.

Source page: [[src-hitu-entropy-engineering]] (2026-08-21). Locked into D4: share an [[audited-task-contract]], not transcripts.

## Numbers to cite

From [[entropy-gate]], 64 Claude Haiku workers, one synthesis model:

| Setup | Hallucination index | Cost / run |
| --- | --- | --- |
| Full shared memory | 0.658 | $4.12 |
| Complete isolation | 0.492 | — |
| Entropy-gated diffs | 0.463 | $1.73 |

Author: isolation beat free talk. Gating beat both. Cost down 58% vs shared memory.

Gate: compare assertion maps and embedding drift. Code-refactor calibration: drift > 0.28 means purge. Creative tasks ~0.55. Ungated unanimous agreement was wrong in 41% of 50 runs.

## Four conditions

1. Isolated worktrees.
2. Structured diffs only.
3. Objective gate outside the LLM.
4. Kill and reseed one node without restarting the fleet.

## Conflicts already flagged

- [[contradictions]] C3: tweet (200 agents, 20 seconds, 100% coverage) vs article (64 workers). Cite the table.
- C4: shared conversational memory poisons swarms; a small audited contract is compatible.

## What this quiz did not prove

`MEMORY.md` still has no personal identity. The vault remembered the ingested Hitu source. It did not remember anything about the human.
