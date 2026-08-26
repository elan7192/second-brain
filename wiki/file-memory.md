---
type: concept
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-27
---

# File memory

Git markdown memory, shared across harnesses. Not a lab's built-in store.

Source: [[src-pawelhuryn-file-memory]]. Image: `wiki/sources/pawel-huryn-memory.jpg`. lan E share.

Four kinds. Three live in files:

1. Semantic: markdown + index
2. Working: the context window
3. Episodic: append-only log, then a table
4. Procedural: skills

Vector DB only when there is too much to read. Linked markdown is already a graph.

Setup: markdown + one CSV. No vector DB.

This vault already does semantic wiki + index + append-only [[log]] + schema. See [[llm-wiki]] and [[memory-engineering]].

Do not add a second memory writer. Catalog `persistent-bot-memory` is the same job. No PAT daily-push. See [[botdirectory-scan]].

## Related

[[llm-wiki]] · [[memory-engineering]] · [[memory-ablation]] · [[context-graph]] · [[src-pawelhuryn-file-memory]] · [[botdirectory-scan]]
