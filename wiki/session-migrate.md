---
type: concept
tags:
  - wiki
created: 2026-08-25
updated: 2026-08-27
---

# Session-migrate

Session-migrate transfers context only. Git is the source of truth.

Source: [[src-play-methods-2026-08-25]] (`/workspace/play-until-2pm/METHODS.md`). Dry-migrate rules: [[src-chatgpt-play-2026-08-25]] via lead.

## Dry-migrate

1. Secret-scan first. Do not dry-migrate until the scan is clean.
2. Never migrate prod keys or customer data.
3. If context is hidden, rebuild. Do not guess the hidden part.
4. Do not treat a compact blob as the vault. See [[context-compaction]].

## Related

[[audited-task-contract]] · [[harness-routing]] · [[raptor-dispatch]] · [[src-chatgpt-play-2026-08-25]] · [[context-compaction]]
