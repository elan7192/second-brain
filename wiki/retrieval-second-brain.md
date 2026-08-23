---
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-23
---

# Retrieval second brain

A query-time stack for "read and recall": hybrid search, GraphRAG, three memory layers, agentic routing.

Source: [[src-retrieval-second-brain]].

## Four pillars in the paste

1. Hybrid search + rerank. BM25 for exact terms. Vector for sense. Cross-encoder to reorder. Accuracy gain is unverified.
2. GraphRAG. Walk entity links. Example path in the paste: project A depends on technique B owned by person C.
3. Layered memory. Working = current prompt. Episodic = past task logs. Semantic = the note base (Obsidian / Notion / files).
4. Agentic routing. Tool call. Split the question. Query. Reflect. Query again if thin.

Landing names: MemGPT / Letta, LangChain / LlamaIndex, Markdown/wikilink GraphRAG. YAML frontmatter: tags, summary, date. Metadata filter first.

Do not vendor those frameworks. See `MEMORY.md`.

## What this vault already does

Query path: read [[index]], follow page links, cite pages, write answers back. That is [[llm-wiki]] and [[how-it-works]].

Graph here is compiled pages plus Obsidian links, not a GraphRAG runtime. See [[context-graph]] and [[graph]].

Memory layers map onto existing files. See [[memory-engineering]].

Frontmatter already exists on compiled notes (`type`, `tags`, `created`, `updated`). The paste adds `summary` and `date`. That is a recommendation, not a schema lock.

## Relation to D1

This stack retrieves at question time. D1 compiles at ingest time. Do not reopen D1. See [[contradictions]] C13.

## Related

[[llm-wiki]] · [[tokens-as-capital]] · [[memory-engineering]] · [[context-graph]] · [[harness-routing]]
