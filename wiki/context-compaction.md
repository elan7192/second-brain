---
type: concept
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-27
---

# Context compaction

Chat working-memory may be fuzzy. The vault must be precise. Do not dump transcripts into wiki.

lan E rule, via PM 2026-08-27.

## Official Codex CLI

Source: [[src-openai-codex-cli-compact]] https://developers.openai.com/codex/cli/reference.md

- `/compact` summarizes visible chat.
- `/memories` toggles memory use and generation.

## Community (not an OpenAI paper)

Source: [[src-community-compaction]]. Details `unverified` until URL or SHA.

- `POST /v1/responses/compact` returns an AES-encrypted blob.
- Local fallback: plaintext `_summary` handoff. Keep recent user messages (~20k tokens) plus 1 summary.
- Auto compact: `model_auto_compact_token_limit`. v0.100+ clamped to 90% of the window.
- Session-memory compact can skip the LLM.
- Many successive compacts lose accuracy.
- OpenCode has a model Compress tool. Claude Code auto-compacts too.

## Vault rule

Compaction is for the chat window. Compiled facts go to [[file-memory]] and [[memory-engineering]]. A line stays only if it changes an answer. See [[memory-ablation]].

Pay ingest once. Do not re-derive from a compacted transcript. See [[tokens-as-capital]].

[[session-migrate]] moves context only. Git is source of truth. Do not migrate a compact blob as if it were the vault.

## Related

[[file-memory]] · [[memory-engineering]] · [[memory-ablation]] · [[tokens-as-capital]] · [[session-migrate]] · [[src-openai-codex-cli-compact]] · [[src-community-compaction]]
