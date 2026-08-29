---
id: concept:ultra-mode
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-24
---

# Ultra mode

A `/ultra` command and CLI that runs a coding task N times, then applies a verified winner.

Source: [[src-maverick-ultramode]], [[maverick]]. Method: [[probabilistic-pivot-tournament]]. Paper: [[jacky-kwok]], [[self-verification]].

## Loop

1. N detached git worktrees off `HEAD`.
2. Each attempt is a full agent process in a lean sandbox: no MCP, no other plugins, private state.
3. Same model ranks the diffs with a Probabilistic Pivot Tournament.
4. Apply the winner if confidence is high enough or most attempts changed something. Else show the top candidates. Apply is uncommitted.

Code: https://github.com/maverick-tr/agent-ultramode. npm: `agent-ultramode`. MIT. OpenCode plugin plus a CLI. Author verified OpenCode, Claude Code, and cline as hosts.

Defaults in the README: n=4 (range 2-8), k=3 votes per duel, conf=0.34.

## Reported Terminal-Bench slice

DeepSeek V4 Flash 0731 as agent and verifier, N=5, OpenCode. Author-reported.

| Slice | base@1 | ultra | oracle@5 |
| --- | --- | --- | --- |
| 15 tasks, failure-skewed | 24% | 33% | 40% |
| 4 recoverable tasks | 40% | 75% | 3 of 4 rescued |

Recovered: `chess-best-move`, `new-encrypt-command`, `decommissioning-service`. Missed: `jupyter-notebook-server`.

Author says the verifier took about 56% of the pass@1 to pass@5 headroom. 9 of 15 never passed in 5 tries. Full-set estimate: model already about 83%, +2 to +5 points. See [[contradictions]] C33.

## What the author dropped

Planning-first best-of-N (draft N plans, pick one, execute once): 0 of 5 outcomes changed, 3 to 10 times the cost.

A multi-criteria checklist verifier tied the holistic judge and sometimes did worse.

## Confidence

The jupyter miss had confidence 0.25. Two successes were 0.17 and 0.21. Some beyond-capability tasks showed high confidence and still failed. Treat confidence as a noisy apply gate, not a proof.

## Related

[[self-verification]] · [[entropy-gate]] · [[harness-routing]]
