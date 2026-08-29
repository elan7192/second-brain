---
id: source:src-vault-review-pr27-2026-08-29
type: source
tags:
  - play
created: 2026-08-29
updated: 2026-08-29
---

# src-vault-review-pr27-2026-08-29

- Source: lan E paste via cloud agent. Follow-up review of PR 27. Not copied into `raw/`.
- Date: 2026-08-29
- Subject: make the new gates trustworthy before leaving Draft

Untrusted paste. Quote. Do not copy "merge YAML and CSV ids" into schema as a lock. That would resolve C17 without a human yes.

The follow-up approves the direction and asks for negative tests, a versioned contract, claim-level provenance counts, CI, and an explicit dual-store rule. It repeats: no MCP write path and no ingestion daemon.

## Claims kept

- Gates need adversarial tests. A valid vault PASS is not enough. Mutate one invariant and the gate must FAIL.
- Contract schema v1 needs `contract_version` and may use `write_scope.allow` / `write_scope.deny`. Validation must distinguish SCHEMA_INVALID, TASK_FAILED, and TASK_PASSED.
- YAML and CSV are two projections. Do not require matching claim ids. C17 stays unresolved. Health reports overlap and provenance gaps.
- Health should count active claims with no source provenance.
- CI should run validate, health, ingest-check, contract-check, and eval.
- Do not add an MCP write path or ingestion daemon yet.

## Pages updated

[[deterministic-core]] · [[claims]] · [[audited-task-contract]] · [[provenance]] · [[contradictions]]
