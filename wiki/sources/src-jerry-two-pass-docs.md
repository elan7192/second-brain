---
type: source
tags:
  - twitter
created: 2026-08-24
updated: 2026-08-24
---

# src-jerry-two-pass-docs

- Raw: [[2026-08-23-jerry-two-pass-docs]] (`raw/x/2026-08-23-jerry-two-pass-docs.md`)
- URL: https://x.com/jerryjliu0/status/2091564183922077885
- Date: 2026-08-23
- Author: [[jerry-liu]]

## Claims kept

Agent harnesses (Codex, Cowork) default to two-pass document processing over a data room: cheap OSS parse, then retrieval (grep or semantic), then a just-in-time VLM pass on the pages that matter. Default tools named: pdf2text, then the harness model (Opus 5). Full-dump VLM OCR is slow and expensive. Default stack problems named by the author: Opus 5 is a weak OCR VLM, expensive, ungrounded; pypdf/pdf2text may be too thin as pass one; agents rewrite chart, box, and confidence work that an OCR tool already ships.

Vendor pitch, marked `unverified` as method: LiteParse (Rust, free/OSS, 50+ types, faster/more accurate than other OSS parsers) as pass one. LlamaParse as pass two, callable as MCP or skill, page-number zoom-in. Attached Cowork video was not transcribed.

## Pages updated

[[two-pass-document-processing]] · [[harness-routing]] · [[tokens-as-capital]] · [[context-graph]] · [[jerry-liu]] · [[contradictions]]
