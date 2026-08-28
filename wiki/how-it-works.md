---
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-28
---

# How it works

This vault is a compiler. See [[llm-wiki]]. Obsidian is the IDE. See [[Home]] and [[graph]].

## Loop

1. Human drops a source in `raw/` or pastes a URL.
2. Agent ingests. One source updates many pages.
3. Human asks. Agent reads [[index]], then pages, then answers.
4. Useful answers go to `wiki/` or `output/`.
5. Periodic lint: orphans, stale claims, [[contradictions]].
6. Methods learned while doing work go into `wiki/` after the task. See [[src-play-methods-2026-08-25]].
7. GrowthOS operator notes live in `growth/`. Load [[growth-core]]. Do not mix DEMO partner figures into [[MEMORY]]. See [[growth-operator]].
8. After ingest, rebuild the local ontology: `python3 tools/rebuild-ontology.py`. See [[vault-ontology]] and [[palantir-aip]].

## What the model sees

Prefer compiled pages over raw dumps. That is [[tokens-as-capital]] and [[context-graph]].
For object sets and links, query [[vault-ontology]] instead of walking every file.

[[MEMORY]] stays small. That is [[memory-ablation]].
Locked choices live in [[decisions]].

Schema rules stay checkable. That is [[verifiable-instructions]].

## What agents share

Not chat. An [[audited-task-contract]]. If several agents run, apply [[entropy-gate]].
