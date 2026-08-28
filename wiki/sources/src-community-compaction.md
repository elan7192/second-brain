---
id: source:src-community-compaction
type: source
tags:
  - community
created: 2026-08-27
updated: 2026-08-27
---

# src-community-compaction

Community notes, not an OpenAI paper. Compiled from PM 2026-08-27. Not copied into `raw/`.

Named: Codex Knowledge Base 2026-03/04, gist badlogic compact research. Gist URL not supplied. Treat path-level details as `unverified` until a URL or SHA is on file.

## Claims kept (community)

- OpenAI path `POST /v1/responses/compact` returns an AES-encrypted blob. `unverified`.
- Local fallback: plaintext `_summary` handoff. Keep recent user messages (~20k tokens) plus 1 summary. `unverified`.
- Auto: `model_auto_compact_token_limit`. v0.100+ clamped to 90% of the window. `unverified`.
- Session-memory compact can skip the LLM. `unverified`.
- Many compacts lose accuracy. Warn.
- OpenCode: model `Compress` tool. Claude Code: auto-compact too. Product names, not papers.

See [[context-compaction]].

## Pages updated

[[context-compaction]]
