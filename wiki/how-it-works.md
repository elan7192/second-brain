---
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-27
---

# How it works

This vault is a compiler. See [[llm-wiki]]. Obsidian is the IDE. See [[Home]] and [[graph]].

## Loop

1. Human drops a source in `raw/` or pastes a URL.
2. Agent extracts claims into `wiki/claims.csv`, then ingests. One source updates many pages.
3. Human asks. Agent runs `python3 tools/retrieve.py`, reads [[index]] and ranked pages, then answers.
4. Useful answers go to `wiki/` or `output/`.
5. Periodic lint: orphans, stale claims, claim ledger, [[contradictions]].
6. Methods learned while doing work go into `wiki/` after the task. See [[src-play-methods-2026-08-25]].
7. GrowthOS operator notes live in `growth/`. Load [[growth-core]]. Do not mix DEMO partner figures into [[MEMORY]]. See [[growth-operator]].

## What the model sees

Prefer compiled pages over raw dumps. That is [[tokens-as-capital]], [[context-graph]], and [[claim-protocol]].

[[MEMORY]] stays small. That is [[memory-ablation]].
Locked choices live in [[decisions]].

Schema rules stay checkable. That is [[verifiable-instructions]].

## What agents share

Not chat. An [[audited-task-contract]]. If several agents run, apply [[entropy-gate]].
