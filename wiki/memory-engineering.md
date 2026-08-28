---
id: concept:memory-engineering
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-28
---

# Memory engineering

Memory is a pipeline, not a bigger context window.

Source: 0xWast3 article quoted by [[src-0xcodio-memory-ablation]].

## Five stages

1. **Capture.** Would this still be true and useful in three months? Session mood is not memory.
2. **Consolidate.** Merge near-duplicates. Skip if already stored.
3. **Retrieve.** Score relevance now. Dilution is a failure mode.
4. **Reconcile.** Supersede, coexist, or `flag_conflict`. Do not silently pick a side. Disputed rows live in `wiki/claims.csv`, `wiki/data/claims.yaml`, and [[contradictions]].
5. **Decay.** Idle memories lose confidence. Archive below a threshold.

## Failure of replay

Full-transcript replay does not scale, does not rank importance, and keeps both old and new facts with no current flag.

## Related

[[memory-ablation]] · [[context-graph]] · [[audited-task-contract]] · [[entropy-gate]] · [[trace]] · [[src-marfinxx-trace]] · [[file-memory]] · [[context-compaction]] · [[memory-system]] · [[epistemic-labels]] · [[claims]] · [[retrieval]]

TRACE ([[trace]]) repairs context files from trajectories. CRUD memory and Ebbinghaus decay appear in the quoted article on that source, not as TRACE eval numbers.

[[src-beamnxw-memory-stack]] is another stack tweet. Filesystem memory cost-halving is `unverified`.

[[src-agentmemoryl-aml-s2]] points at the Agent Memory Leaderboard. Season 2 numbers `unverified`.

[[src-chatchat-living-brain]] claims a Living Brain. Product-only. `unverified`.

[[headlong]] stores life as a jsonl DAG with tiered compaction. Author method, not a measured memory eval here.
