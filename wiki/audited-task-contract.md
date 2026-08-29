---
id: concept:audited-task-contract
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-29
---

# Audited task contract

The portable unit between coding agents is verified task state, not a transcript.

Source: [[src-rohit-harness-router]]. Codex `/goal` is a same-harness form of this. See [[codex-goal]] and [[src-voxyz-codex-goal-quota]].

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

Machine form: contract schema v1. Required: `contract_version`, `objective`, `acceptance_checks`, `write_scope`, `state_version`. `write_scope` may be a string, a list, or `{allow, deny}`. Check with `python3 tools/sb contract-check <path>`. With `--results`, the status is TASK_PASSED or TASK_FAILED. Without results, SCHEMA_VALID or SCHEMA_INVALID. Forbidden keys: `transcript`, `secrets`, `tool_dumps`, `chat`. See [[deterministic-core]] and [[src-vault-review-pr27-2026-08-29]].

[[src-4ndrearossetti-openconnector]] applies the same exclusion at tool time: the executor may call a gateway; the model still does not see the key. See [[secret-gateway]].

From use 2026-08-25: agents share contract, not free agent chat. See [[raptor-dispatch]].

## Control plane

- Planner proposes a bounded unit.
- Controller is deterministic code. It owns canonical state.
- Executor changes a candidate worktree. It cannot write canonical state.
- Auditor uses fresh context and independent evidence.

Rule: the planner proposes. The executor changes a candidate. The auditor verifies. Only the controller commits.

[[adversarial-review]] is the same shape on one artifact: M writes, R reviews, C audits the review, then M may edit. The inner loop is review text only. Source: [[src-omarsar-adversarial-review]].

`/goal` keeps outcome, check, constraints, and a stop list in one Codex prompt. It does not move state to another harness. Use this page's contract fields when the task leaves Codex. See [[codex-goal]].

## Why not a shared brain dump

Generated repo summaries in a 2026 AGENTS.md study did not significantly raise resolve rate and raised cost. Native sessions are not a standard. Unverified memory can poison later agents.

[[src-avid-company-foundry]]: the folder is not the product. The contracts inside it are. Workers write artifacts, not private summaries. A chat answer is not a company artifact. See [[company-foundry]].

## Related

[[harness-routing]] · [[entropy-gate]] · [[memory-engineering]] · [[adversarial-review]] · [[company-foundry]] · [[secret-gateway]] · [[codex-goal]] · [[deterministic-core]] · [[src-vault-review-pr27-2026-08-29]]
