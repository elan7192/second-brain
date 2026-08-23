---
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-23
---

# How it works

This vault is a compiler. See [[llm-wiki]]. Obsidian is the IDE. See [[Home]] and [[graph]].

## Loop

1. Human drops a source in `raw/` or pastes a URL.
2. Agent ingests. One source updates many pages.
3. Human asks. Agent reads [[index]], then pages, then answers.
4. Useful answers go to `wiki/` or `output/`.
5. Periodic lint: orphans, stale claims, [[contradictions]].

## What the model sees

Prefer compiled pages over raw dumps. That is [[tokens-as-capital]] and [[context-graph]]. Hybrid search and GraphRAG are a different query path. See [[retrieval-second-brain]] and C13.

[[MEMORY]] stays small. That is [[memory-ablation]].
Locked choices live in [[decisions]].

Schema rules stay checkable. That is [[verifiable-instructions]].

## What agents share

Not chat. An [[audited-task-contract]]. If several agents run, apply [[entropy-gate]].
