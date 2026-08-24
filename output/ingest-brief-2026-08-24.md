---
type: ship
tags:
  - ship
created: 2026-08-24
updated: 2026-08-24
---

# Ingest brief · 2026-08-24

DAIR.AI pointed at Gao and Chen, arXiv:2608.20195. Compiled into the vault.

## What changed

Agents read `AGENTS.md` and working notes, not API docs. This vault now treats instruction files and `wiki/` as the control surface, and treats reading them as not verification. Locked D8. Flagged C8 and C9.

## What linked

[[agent-facing-docs]] now sits between [[verifiable-instructions]], [[context-graph]], [[tokens-as-capital]], [[llm-wiki]], and [[self-verification]]. The measured 60.5% agent-facing share is cited from [[src-dair-agent-friendly-docs]], with the weighting and label caveats on that page.

## What to look at

1. [[agent-facing-docs]] and D8 in `decisions.md`.
2. [[contradictions]] C8 (file first vs code first) and C9 (prose checks vs observed validation).
3. `AGENTS.md` Control surface. Then `python3 tools/lint-wiki.py`.
