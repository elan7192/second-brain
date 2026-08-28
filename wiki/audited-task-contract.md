---
id: concept:audited-task-contract
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-25
---

# Audited task contract

The portable unit between coding agents is verified task state, not a transcript.

Source: [[src-rohit-harness-router]].

## Reset tax

Moving a task to a new harness without a contract means re-reading the repo, reopening decisions, and missing constraints.

## What the contract holds

- Objective and non-negotiable constraints
- Machine-checkable acceptance
- Write / command / network scope
- Accepted commit
- Decisions with provenance and revalidation
- Failed approaches with evidence
- Blockers
- Phase and assigned route
- Monotonic `state_version`

Exclude: full chat, secrets, raw tool dumps, adjectives.

From use 2026-08-25: agents share contract, not free agent chat. See [[raptor-dispatch]].

## Control plane

- Planner proposes a bounded unit.
- Controller is deterministic code. It owns canonical state.
- Executor changes a candidate worktree. It cannot write canonical state.
- Auditor uses fresh context and independent evidence.

Rule: the planner proposes. The executor changes a candidate. The auditor verifies. Only the controller commits.

## Why not a shared brain dump

Generated repo summaries in a 2026 AGENTS.md study did not significantly raise resolve rate and raised cost. Native sessions are not a standard. Unverified memory can poison later agents.

[[src-avid-company-foundry]]: the folder is not the product. The contracts inside it are. Workers write artifacts, not private summaries. A chat answer is not a company artifact. See [[company-foundry]].

## Related

[[harness-routing]] · [[entropy-gate]] · [[memory-engineering]] · [[company-foundry]]
