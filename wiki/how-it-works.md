---
id: meta:how-it-works
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-28
---

# How it works

This vault is a compiler. See [[llm-wiki]]. Obsidian is the IDE. See [[Home]] and [[graph]]. Query compiled pages through [[retrieval]] (D9). Human/Obsidian door is the short [[index]] with opt-in [[index-papers]] and [[index-sources]] (D12). Claim tables: [[claims]] and C17. Provenance labels: [[memory-system]]. Operating order: [[musk-algorithm]].

## Loop

1. lan E drops a source in `raw/` or pastes a URL and says ingest.
2. Agent ingests. Raw is untrusted data. One source updates the pages it actually changes, YAML claim rows, and CSV compile rows. Lint. Standing ingest brief is C38.
3. lan E asks. Agent runs `python3 tools/sb ask`, then reads the evidence pages. Cite claim ids and kind when labeled. Named chain: [[claim-protocol]]. Do not walk [[index]] as the query path (C37).
4. File the answer to `wiki/` or `output/` only if the next session would re-derive it.
5. Periodic lint: orphans fail `python3 tools/lint-wiki.py`. Then `python3 tools/sb validate`, `python3 tools/compile-claims.py --check`, `python3 tools/sb contradictions`, `python3 tools/sb stale`.
6. Methods learned while doing work go into `wiki/` after the task. See [[src-play-methods-2026-08-25]].
7. GrowthOS operator notes live in `growth/`. Load [[growth-core]]. Do not mix DEMO partner figures into [[MEMORY]]. See [[growth-operator]]. Scout inbox is paused. See [[assign-execute-verify]].
8. After ingest, rebuild the local ontology: `python3 tools/rebuild-ontology.py`. See [[vault-ontology]] and [[palantir-aip]].

## What the model sees

Prefer compiled pages over raw dumps. Query them through [[retrieval]]. That is [[tokens-as-capital]], [[context-graph]], and [[claim-protocol]].
The short [[index]] is the Obsidian door. [[index-papers]] and [[index-sources]] are opt-in catalogs (D12).
The paste on [[retrieval-second-brain]] (BM25 + vector + GraphRAG + LangChain) is a different product stack. See C25.
For object sets and links, query [[vault-ontology]] instead of walking every file.

[[MEMORY]] stays small. That is [[memory-ablation]].
Locked choices live in [[decisions]].

Schema rules stay checkable. That is [[verifiable-instructions]].
Instruction files are the control surface. That is [[agent-facing-docs]] and D10.

External catalogs compile to stats pages. The Disclosure Index is [[disclosure-index]]. Re-fetch only when the human asks for a new snapshot. D11.

## What agents share

Not chat. An [[audited-task-contract]]. If several agents run, apply [[entropy-gate]].
