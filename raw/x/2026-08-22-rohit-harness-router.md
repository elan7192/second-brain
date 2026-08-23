# Source: Rohit on a shared second brain for coding agents

- URL: https://x.com/rohit4verse/status/2091255118511686065
- Author: rohit4verse
- Date: 2026-08-22
- Quoted article: "How to give every coding agent the same second brain" (https://x.com/i/article/2083341896789995520)

## Tweet

I have five coding harnesses installed. Cursor, Claude Code, Codex, OpenCode, Prime Agent.

I still can't tell you which one deserves which task.

Claude Code will spin up a swarm of sub-agents to rename a variable. pi will bring four tools to do a job that needed the swarm.

So I stopped choosing. One setup, and every prompt lands on whichever one is actually best at it.

Quoted earlier line: switch from Claude Code to Codex mid-task and lose nothing. Move semantic state, never KV state.

## Article claims

The reset tax is the cost of moving a task between harnesses: re-reading the repo, reopening settled decisions, missed constraints.

The shared object should not be a universal transcript. It should be a small versioned contract: objective, verified facts, remaining work, allowed next actions.

Route the model and the harness as two independent choices. Mappings are local hypotheses, not internet leaderboards.

Copying every session is the wrong abstraction:

- Broad generated context files did not significantly improve SWE-bench / CTXbench in the cited 2026 study, and raised cost (~20-23%).
- Native sessions are not an interoperability layer.
- Unverified memory can poison later agents (AgentPoison). Treat retrieved memory as untrusted until verified.

Useful contract fields: objective, machine-checkable acceptance, scope, accepted commit, decisions with provenance, failed approaches, blockers, phase, route, monotonic `state_version`.

Control plane: planner proposes, controller (deterministic code) owns canonical state, executor changes a candidate worktree, auditor inspects with fresh context. Only the controller commits.

Route phases, not turns. Keep session affinity until a verified checkpoint. Transfer semantic state. Do not depend on transferring KV cache.

Test routing separately from audited state. If the control plane costs more than the reset tax it saves, keep a fixed pair.
