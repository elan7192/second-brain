---
id: concept:portable-memory
type: concept
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-28
---

# Portable memory

Delta vs [[file-memory]] and [[llm-wiki]]. Do not clone Brain.

Source: [[src-av1dlive-portable-memory]]. lan E share.

Already in vault: git markdown is the store. Compiled wiki, not RAG dump.

New here:

- Git is source of truth. SQLite FTS5 is a disposable index, not a second memory. This vault's index is `.cache/secondbrain.sqlite`, rebuilt by `python3 tools/sb rebuild-index`.
- Redact rolls back. It does not erase.
- MCP tool descriptions say WHEN, not WHAT.
- FTS prefix rewrite for search.

Do not clone `github.com/codejunkie99/brain`. Do not install a Brain binary. Vault stays markdown + git. See [[session-migrate]], [[retrieval]], [[stable-ids]], [[claims]].

## Related

[[file-memory]] · [[llm-wiki]] · [[loop-graph-engineering]] · [[session-migrate]] · [[src-av1dlive-portable-memory]]
