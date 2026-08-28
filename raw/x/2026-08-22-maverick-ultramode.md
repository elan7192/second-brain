# Source: Maverick on /ultra and LLM-as-a-Verifier

- URL: https://x.com/mavericktr24/status/2091147176017563673
- Author: mavericktr24 (Maverick)
- Date: 2026-08-22
- Repo: https://github.com/maverick-tr/agent-ultramode
- npm: agent-ultramode
- Quoted: jackyk02, LLM-as-a-Verifier (https://x.com/jackyk02/status/2074969820739805275)
- Video: 55.2s demo attached to the tweet

## Tweet

Took the LLM-as-a-Verifier paper and turned it into a simple /ultra command for coding agents

Run your task N times in parallel, each in its own git worktree. The same model then verifies the diffs (a Probabilistic Pivot Tournament) and applies the winner.

Terminal-Bench, DeepSeek V4 Flash 0731 as both agent and verifier:

24% → 33% overall
40% → 75% on recoverable tasks

Model-agnostic: it pushes whatever model you run to its best.

An opencode plugin + a CLI for any agent (Claude Code, Grok, Cline, Pi). Spread attempts across one or several models in a single pass.

MIT. npm: agent-ultramode
Repo + how it works below.

## Quoted Jacky post (2026-07-08)

LLM-as-a-Verifier:

- Fine-grained score scale (1-20, not 1-5)
- Expectation over the full logprob distribution of score tokens
- Scale repeated evaluation and criteria decomposition

Claimed SOTA on Terminal-Bench V2, SWE-Bench Verified, RoboRewardBench, MedAgentBench in that post.

## Repo README claims (same author, same day)

https://github.com/maverick-tr/agent-ultramode README, npm 0.1.4 published 2026-08-22.

Benchmark: Terminal-Bench, DeepSeek V4 Flash 0731 as agent and verifier, inside opencode, N=5. Numbers are the OpenCode run. OpenCode, Claude Code, and cline verified end to end as hosts.

| Slice | base@1 | ultra | oracle@5 |
| --- | --- | --- | --- |
| All 15 tasks | 24% | 33% | 40% |
| 4 recoverable tasks | 40% | 75% | rescued 3 of 4 |

Verifier captured about 56% of pass@1 to pass@5 headroom. Recovered `chess-best-move`, `new-encrypt-command`, `decommissioning-service`. Missed `jupyter-notebook-server`.

15 tasks were deliberately failure-skewed. Author estimate for a full run: model already about 83%, modest +2 to +5 points. 9 of 15 never passed in 5 tries.

Method named Probabilistic Pivot Tournament, reimplemented from Kwok et al. 2026 (arXiv:2607.05391):

1. Fan out N detached git worktrees off HEAD. Lean sandbox: no MCP, no other plugins, private state.
2. Ring pass: each diff judged once vs a neighbour, seed pivots.
3. Pivot duels: field vs top pivots, K reasoned votes per duel.
4. Score: normalised win-rate. Confidence = top1 minus top2.
5. Apply the winner if confident or most attempts changed something. Else show top candidates. Apply is uncommitted.

Defaults: n=4 (2-8), k=3, conf=0.34.

Adaptation vs paper: reasoned pairwise votes, no logprobs, no separate verifier model, plus confidence-gated apply and isolated worktrees. Author says official paper-faithful impl is TurboAgent (https://github.com/llm-as-a-verifier/TurboAgent).

Failed approaches the author dropped:

- Planning-first best-of-N (draft N plans, pick one, execute once): 0 of 5 outcomes changed, 3 to 10 times the cost.
- Multi-criteria checklist verifier: tied the holistic judge and sometimes did worse.

Confidence caveat: the jupyter miss had confidence 0.25, higher than two tasks it got right (0.17, 0.21). Some beyond-capability tasks showed high confidence while failing.
