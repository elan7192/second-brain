---
id: concept:verifiable-instructions
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-24
---

# Verifiable instructions

Wishes in `AGENTS.md` do not change behavior. Checks do.

Source: [[src-voxyz-verifiable-instructions]].

## Banned wishes

- "Don't make mistakes."
- "Never hallucinate."
- "You are a software engineer with 15 years of experience."
- Any new "never…" stacked on after a failure

## Required shape

Every instruction states:

1. What behavior must change.
2. How to check that it changed.
3. What to do when evidence is missing or the check fails.

This vault's schema follows that shape. The tweet's eight paste-ready blocks were not in the fetched body. See [[contradictions]] C6.

## Related

[[memory-ablation]] · [[self-verification]] · [[anti-slop]] · `AGENTS.md`
