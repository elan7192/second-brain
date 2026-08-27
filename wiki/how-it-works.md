---
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-27
---

# How it works

This vault is a compiler. See [[llm-wiki]]. Obsidian is the IDE. See [[Home]] and [[graph]]. Claims are a rebuildable table. See [[claims]] and [[memory-system]].

## Loop

1. Human drops a source in `raw/` or pastes a URL.
2. Agent ingests. Raw is untrusted data. One source updates many pages and claim rows.
3. Human asks. Agent reads [[index]], then pages, then answers. Cite claim ids when used.
4. Useful answers go to `wiki/` or `output/`.
5. Periodic lint: orphans, stale claims, [[contradictions]], `python3 tools/lint-wiki.py`.
6. Methods learned while doing work go into `wiki/` after the task. See [[src-play-methods-2026-08-25]].
7. GrowthOS operator notes live in `growth/`. Load [[growth-core]]. Do not mix DEMO partner figures into [[MEMORY]]. See [[growth-operator]].

## What the model sees

Prefer compiled pages over raw dumps. That is [[tokens-as-capital]] and [[context-graph]].

[[MEMORY]] stays small. That is [[memory-ablation]].
Locked choices live in [[decisions]].

Schema rules stay checkable. That is [[verifiable-instructions]].

## What agents share

Not chat. An [[audited-task-contract]]. If several agents run, apply [[entropy-gate]].
