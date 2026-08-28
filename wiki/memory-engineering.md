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
3. **Retrieve.** Score relevance now. Dilution is a failure mode. Live tool: `python3 tools/sb ask`. See [[retrieval]] and [[claim-protocol]].
4. **Reconcile.** Supersede, coexist, or `flag_conflict`. Do not silently pick a side. Disputed rows live in `wiki/claims.csv`, `wiki/data/claims.yaml`, and [[contradictions]].
5. **Decay.** Idle memories lose confidence. Archive below a threshold.

## Failure of replay

Full-transcript replay does not scale, does not rank importance, and keeps both old and new facts with no current flag.

## Three layers from [[src-retrieval-second-brain]]

The paste names working, episodic, and semantic memory. This vault's files, not a new store:

- Working: the current prompt. Do not file it into `MEMORY.md`.
- Episodic: `wiki/log.md`, [[hunt]], [[ship]]. Task logs and experience.
- Semantic: compiled `wiki/` pages. That is the second brain.

Retrieve in this vault is `python3 tools/sb ask` (D9). It is not the paste's BM25 + vector + rerank. See [[retrieval-second-brain]] and [[contradictions]] C25.

## Related

[[memory-ablation]] · [[context-graph]] · [[claim-protocol]] · [[audited-task-contract]] · [[entropy-gate]] · [[trace]] · [[src-marfinxx-trace]] · [[file-memory]] · [[context-compaction]] · [[memory-system]] · [[epistemic-labels]] · [[claims]] · [[retrieval]] · [[retrieval-second-brain]] · [[company-foundry]]

TRACE ([[trace]]) repairs context files from trajectories. CRUD memory and Ebbinghaus decay appear in the quoted article on that source, not as TRACE eval numbers.

[[src-beamnxw-memory-stack]] is another stack tweet. Filesystem memory cost-halving is `unverified`.

[[src-agentmemoryl-aml-s2]] points at the Agent Memory Leaderboard. Season 2 numbers `unverified`.

[[src-chatchat-living-brain]] claims a Living Brain. Product-only. `unverified`.

[[src-avid-company-foundry]]: sessions end, companies continue. Do not treat generated summaries as customer fact. Record whether a decision came from evidence, inference, or a guess. See [[company-foundry]].

[[src-exm7777-grok-bot-money]]: Grok Bot memory holds preferences and summaries and is not a substitute for an authoritative source. The vault is. See [[grok-bot]].

[[headlong]] stores life as a jsonl DAG with tiered compaction. Author method, not a measured memory eval here.
