---
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-24
---

# Two-pass document processing

For a knowledge-work task over a data room, parse cheaply, retrieve a subset, then run a VLM only on those pages.

Source: [[src-jerry-two-pass-docs]].

## Passes

1. Light parse across tens to thousands of files with a free or OSS tool. Then grep or semantic retrieval.
2. Just-in-time VLM. Screenshot or re-parse the retrieved pages. Call a vision model or write code against those pages.

Full-dump VLM OCR on ad-hoc customer files is slow and expensive. JIT VLM keeps cost on the subset that the task needs.

## Defaults in current harnesses

[[src-jerry-two-pass-docs]] names Codex and Cowork. Out of the box: pdf2text as pass one, the harness model (Opus 5) as pass two. Author critique: Opus 5 is a weak OCR VLM, expensive at scale, and ungrounded. pypdf and pdf2text may be too thin. Agents then write throwaway chart, bounding-box, and confidence code.

## Vendor stack in the same post

LiteParse as pass one. LlamaParse as pass two, MCP or skill, page-number zoom-in. Accuracy, cost, and “faster than other OSS parsers” are author-reported. Mark `unverified`.

## Split from this vault

This pattern is for ad-hoc document dumps. The compiled wiki still pays ingest once. See [[llm-wiki]], [[tokens-as-capital]], and [[contradictions]] C8.

## Related

[[harness-routing]] · [[context-graph]] · [[jerry-liu]]
