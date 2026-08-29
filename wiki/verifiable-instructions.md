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

[[src-voxyz-codex-goal-quota]] ships five `/goal` prompts with checks. That thread is not the missing eight blocks. See [[codex-goal]].

[[src-voxyz-writing-system]] is a later `/goal` writing prompt. It does not supply those eight blocks. C6 stays open.

Instruction files get most of an agent's documentation attention. They do not trigger testing. [[src-dair-agent-friendly-docs]] records zero Validate events and an adjusted OR of 0.39 for immediate testing after consultation. The check must be executable (`python3 tools/lint-wiki.py`, `python3 tools/sb validate`). Reading `AGENTS.md` is not the check. See [[agent-facing-docs]] and C27.

A local skill SOP needs this shape or it is a wish. See [[skill-as-sop]].

## Related

[[memory-ablation]] · [[self-verification]] · [[skill-as-sop]] · [[anti-slop]] · [[agent-facing-docs]] · [[codex-goal]] · `AGENTS.md` · [[src-voxyz-writing-system]]
