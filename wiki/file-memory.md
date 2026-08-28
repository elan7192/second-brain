---
id: concept:file-memory
type: concept
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-28
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

Setup: markdown + one disposable index. This vault uses SQLite FTS5, not a CSV. No vector DB. See [[retrieval]] and D9.

`output/ontology-objects.csv` is a derived object table, not the memory index. Rebuild from wiki. Do not hand-edit. See [[vault-ontology]].

This vault already does semantic wiki + index + append-only [[log]] + schema. See [[llm-wiki]], [[memory-engineering]], and [[retrieval]].

Do not add a second memory writer. Catalog `persistent-bot-memory` is the same job. No PAT daily-push. See [[botdirectory-scan]].

Delta: [[portable-memory]]. Git truth. FTS5 disposable. Do not clone Brain.

2026-08-27 standing closed after loop17. Each hunt→harden: Vault writes Pawel semantic plus one episodic [[log]] row. Do not write procedural SKILL.md. Do not dump chat. No vector DB. See [[hunt-harden-loop]].

## Related

[[llm-wiki]] · [[memory-engineering]] · [[memory-ablation]] · [[context-graph]] · [[src-pawelhuryn-file-memory]] · [[botdirectory-scan]] · [[context-compaction]] · [[portable-memory]] · [[hunt-harden-loop]] · [[retrieval]] · [[vault-ontology]]
