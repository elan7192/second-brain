---
id: concept:eval-suite
type: concept
tags:
  - wiki
created: 2026-08-28
updated: 2026-08-28
---

# Eval suite

Measures whether retrieval and provenance work. Files live in `eval/`.

Command: `python3 tools/sb eval`.

Scores: retrieval recall, retrieval precision, citation coverage, unsupported claims, contradiction handling, stale-fact detection.

A retrieval change that fails this gate does not ship. See [[retrieval]] and [[verifiable-instructions]].

## Related

[[retrieval]] · [[claims]] · [[self-verification]] · [[stale-fact-detector]]
