---
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-24
---

# Memory

Durable facts only. A line stays if deleting it would change an answer.
Adjectives and taste notes do not belong here. See [[memory-ablation]].

## Vault

- This repo is a compiled LLM wiki. Answer from `wiki/` first. Do not re-read `raw/` to answer a normal question.
- `raw/` is immutable. Never edit it.
- `decisions.md` is locked. Do not reopen a decision without new evidence.
- The vault does not post, pay, send, or deploy.
- Operational rules live in `AGENTS.md`, `wiki/`, `MEMORY.md`, and `decisions.md`. Do not steer this vault through README or API docs.
- Reading instruction or wiki pages is not verification. After those files change, run `python3 tools/lint-wiki.py`. Observed agents test less after reading docs (adjusted OR 0.39). See [[agent-facing-docs]].

## Open questions

- No personal identity, goals, or project constraints have been captured yet. Do not invent them.
