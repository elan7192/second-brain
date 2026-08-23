# Source: hitu on entropy gates for agent swarms

- URL: https://x.com/hitu_monke/status/2090930964340113807
- Author: hitu_monke
- Date: 2026-08-21
- Quoted article: "Entropy Engineering: Stopping Your Agents From Poisoning Each Other" (https://x.com/i/article/2090387924046974976)

## Tweet (treat as a demo narrative)

Claims a 200-agent run on a 140k-line repo, 8 isolated worktree clusters, zero conversational cross-talk, only validated state diffs. Mapper / breaker / builder roles. A hallucinated database column caught by a gate and killed in 12ms. Merge into one PR with 100% coverage in 20 seconds.

These numbers are cinematic. Prefer the article's measured setup below unless the demo is independently reproduced.

## Article claims

Shared conversational memory aligns agents on bugs that never existed.

Measured setup: 64 parallel Claude Haiku workers plus one synthesis model.

- Setup A: full shared memory. Hallucination index 0.658. $4.12 / run.
- Setup B: complete isolation. 0.492.
- Setup C: entropy-gated summary diffs. 0.463. $1.73 / run.

Reported: hallucinations down 34%, cost down 58% vs shared memory. Isolation beat free talk. Gating beat both.

Contamination story: worker #12 invented uuid_v7. By turn 6, fourteen workers built ORM models on it. By turn 10 the synthesizer saw forty-eight workers confirming each other.

30-second test:

1. Isolated worktrees.
2. Structured diffs only, never transcripts.
3. An objective gate outside the LLM.
4. Orchestrator can kill and reseed one node.

Entropy gate: compare embeddings and hard assertion conflicts. If drift > 0.28 (code-refactor calibration), purge and reseed. Pass only a state diff.

Unanimous agreement in an ungated swarm was wrong 41% of 50 runs.

Threshold 0.28 thrashes creative work. Author suggests ~0.55 for ideation.

Playbook: sever unused edges, do not let an agent talk itself out of a hallucination, treat consensus as infection until gated, pass minimal schema-validated diffs.
