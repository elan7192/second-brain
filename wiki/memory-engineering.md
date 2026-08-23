---
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-23
---

# Memory engineering

Memory is a pipeline, not a bigger context window.

Source: 0xWast3 article quoted by [[src-0xcodio-memory-ablation]].

## Five stages

1. **Capture.** Would this still be true and useful in three months? Session mood is not memory.
2. **Consolidate.** Merge near-duplicates. Skip if already stored.
3. **Retrieve.** Score relevance now. Dilution is a failure mode.
4. **Reconcile.** Supersede, coexist, or `flag_conflict`. Do not silently pick a side.
5. **Decay.** Idle memories lose confidence. Archive below a threshold.

## Failure of replay

Full-transcript replay does not scale, does not rank importance, and keeps both old and new facts with no current flag.

## Three layers from [[src-retrieval-second-brain]]

The paste names working, episodic, and semantic memory. This vault's files, not a new store:

- Working: the current prompt. Do not file it into `MEMORY.md`.
- Episodic: `wiki/log.md`, [[hunt]], [[ship]]. Task logs and experience.
- Semantic: compiled `wiki/` pages. That is the second brain.

Retrieve in this vault means open [[index]] and follow links. It does not mean BM25 + vector + rerank. See [[retrieval-second-brain]] and [[contradictions]] C13.

## Related

[[memory-ablation]] · [[audited-task-contract]] · [[entropy-gate]] · [[retrieval-second-brain]]
