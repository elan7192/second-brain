---
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-24
---

# How it works

This vault is a compiler. See [[llm-wiki]]. Obsidian is the IDE. See [[Home]] and [[graph]].

## Loop

1. Human drops a source in `raw/` or pastes a URL.
2. Agent ingests. One source updates many pages. URL ingest writes a source page and leaves `raw/` untouched.
3. Human asks. Agent reads [[index]], then pages, then answers.
4. Useful answers go to `wiki/` or `output/`.
5. Periodic lint: orphans, stale claims, [[contradictions]]. Reading schema is not the check. See [[agent-facing-docs]] and D8.

## What the model sees

Prefer compiled pages over raw dumps. That is [[tokens-as-capital]] and [[context-graph]].

[[MEMORY]] stays small. That is [[memory-ablation]].
Locked choices live in [[decisions]].

Schema rules stay checkable. That is [[verifiable-instructions]].
Instruction files are the control surface. That is [[agent-facing-docs]] and D8.

External catalogs compile to stats pages. The Disclosure Index is [[disclosure-index]]. Re-fetch only when the human asks for a new snapshot.

## What agents share

Not chat. An [[audited-task-contract]]. If several agents run, apply [[entropy-gate]].
