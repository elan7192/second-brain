---
id: concept:deterministic-core
type: concept
schema: memory-v1
tags:
  - wiki
created: 2026-08-29
updated: 2026-08-29
created_by: agent
confidence: medium
source:
  - wiki/sources/src-vault-review-2026-08-29.md
  - wiki/sources/src-vault-review-pr27-2026-08-29.md
derived_from:
  - src-vault-review-2026-08-29
  - src-vault-review-pr27-2026-08-29
  - llm-wiki
  - audited-task-contract
  - claims
  - retrieval
---

# Deterministic core

The model proposes wiki edits. Code accepts them.

Source: [[src-vault-review-2026-08-29]]. Live gates: `python3 tools/sb validate`, `python3 tools/sb health`, `python3 tools/sb ingest-check <slug>`, `python3 tools/sb contract-check [path]`. Markdown stays canonical (D9). Dual claim tables stay dual (C17).

## FACT

[[src-vault-review-2026-08-29]] says the authoring protocol is ahead of the runtime, and that ingest, contradiction, index, and brief steps are mostly instructions to the model.

The same source says the LLM should propose changes and deterministic code should validate them before they become canonical.

`python3 tools/sb health` prints page, claim, contradiction, stale, orphan, broken-link, missing-id, provenance-gap, and C17 dual-store counts. Dual store is labeled `two_projections`. IDs are not required to match. It does not replace `python3 tools/sb validate`. Source: [[src-vault-review-pr27-2026-08-29]].

`python3 tools/sb ingest-check <slug>` fails if a named source lacks `id:`, `## Claims kept`, a [[index-sources]] row, an inbound wikilink, or a compiled CSV claim row.

`python3 tools/sb contract-check` accepts contract schema v1: `contract_version`, `objective`, `acceptance_checks`, `write_scope` (string, list, or `{allow, deny}`), and `state_version`. Status is SCHEMA_INVALID, SCHEMA_VALID, TASK_FAILED, or TASK_PASSED. It rejects `transcript`, `secrets`, `tool_dumps`, and `chat`. See [[audited-task-contract]].

Validate fails when a dated `valid_until` is earlier than `valid_from`, when `superseded_by` names an unknown id, when a YAML claim has no `sources`, or when a CSV claim has no source path.

Adversarial tests live in `tests/test_gates.py`. CI runs validate, health, ingest-check, contract-check, and eval.

The review rated retrieval 5/10 and said there is no real retrieval layer. Live query is already `python3 tools/sb ask` (D9). See C46.

## INFERENCE

Moving ingest invariants into `sb validate` / `sb ingest-check` reduces trust in instruction-following. The wiki can still be wrong. The gate only proves the mechanical checklist ran. derived_from: src-vault-review-2026-08-29-03, src-vault-review-2026-08-29-04.

## OPINION

Do not add an MCP write path, an ingestion daemon, or `raw/public|private` from this review. Automate last. Do not resolve C17 or C18. Do not treat the review's numeric ratings as vault facts.

## Check

`python3 tools/sb validate` exits 0. After a named ingest, `python3 tools/sb ingest-check <slug>` exits 0. `python3 tools/sb health` prints `gate PASS` and `claims_without_provenance 0`. `python3 -m unittest tests.test_gates -q` exits 0. If health shows a dual-store overlap of 0: that is expected under C17 two_projections. If ingest-check fails: fix catalog, inbound link, or Claims kept before writing `output/`.

## Related

[[llm-wiki]] · [[claims]] · [[retrieval]] · [[audited-task-contract]] · [[verifiable-instructions]] · [[how-it-works]] · [[claim-protocol]] · [[memory-system]] · [[provenance]] · [[src-vault-review-2026-08-29]] · [[src-vault-review-pr27-2026-08-29]]
