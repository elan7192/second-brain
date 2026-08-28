---
id: meta:how-it-works
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-28
---

# How it works

This vault is a compiler. See [[llm-wiki]]. Obsidian is the IDE. See [[Home]] and [[graph]]. Query compiled pages through [[retrieval]]. Claim tables: [[claims]] and C17. Provenance labels: [[memory-system]].

## Loop

1. Human drops a source in `raw/` or pastes a URL.
2. Agent ingests. Raw is untrusted data. One source updates many pages, YAML claim rows, and CSV compile rows.
3. Human asks. Agent runs `python3 tools/sb ask`, then reads the evidence pages. Cite claim ids and kind when labeled. Named chain: [[claim-protocol]].
4. Useful answers go to `wiki/` or `output/`.
5. Periodic lint: orphans fail `python3 tools/lint-wiki.py`. Then `python3 tools/sb validate`, `python3 tools/compile-claims.py --check`, `python3 tools/sb contradictions`, `python3 tools/sb stale`.
6. Methods learned while doing work go into `wiki/` after the task. See [[src-play-methods-2026-08-25]].
7. GrowthOS operator notes live in `growth/`. Load [[growth-core]]. Do not mix DEMO partner figures into [[MEMORY]]. See [[growth-operator]].
8. After ingest, rebuild the local ontology: `python3 tools/rebuild-ontology.py`. See [[vault-ontology]] and [[palantir-aip]].

## What the model sees

Prefer compiled pages over raw dumps. Query them through [[retrieval]]. That is [[tokens-as-capital]], [[context-graph]], and [[claim-protocol]].
The paste on [[retrieval-second-brain]] (BM25 + vector + GraphRAG + LangChain) is a different product stack. See C25.
For object sets and links, query [[vault-ontology]] instead of walking every file.

[[MEMORY]] stays small. That is [[memory-ablation]].
Locked choices live in [[decisions]].

Schema rules stay checkable. That is [[verifiable-instructions]].

## What agents share

Not chat. An [[audited-task-contract]]. If several agents run, apply [[entropy-gate]].
