---
id: concept:entropy-gate
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-28
---

# Entropy gate

Unverified cross-talk is how swarms agree on bugs that never existed.

Source: [[src-hitu-entropy-engineering]].

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

[[src-avid-company-foundry]] research swarm: collectors share a schema and write evidence rows. The synthesizer reads the ledger, not collector chats. Authority on that packet is observe and prepare only. See [[company-foundry]].

[[src-exm7777-grok-bot-money]] isolates Grok Bot lanes on one shared computer. Separate screens are not isolated worktrees and not separate security boundaries. Do not cite that product as this gate. See [[contradictions]] C30 and [[grok-bot]].

## Related

[[headlong]] is one mind, one stream, many people. Flag, do not merge: C16. Vault keeps isolation. Headlong stays a trial CLI, not the compiler runtime.

[[audited-task-contract]] · [[harness-routing]] · [[self-verification]] · [[memory-engineering]] · [[claim-protocol]] · [[headlong]] · [[grok-bot]] · [[company-foundry]]
