---
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-24
---

# Agent operating system

Synthesis of the 2026-08-17 to 2026-08-24 ingest. File this back so later sessions do not rebuild it from the posts.

## Stack

Five layers, one vault.

1. **Compile, do not retrieve.** [[llm-wiki]] + [[tokens-as-capital]]. `raw/` is input. `wiki/` is the brain. `output/` is built from the wiki. [[agent-facing-docs]] measured that instruction files and working notes take most of an agent's documentation attention.
2. **Remember only what changes answers.** [[memory-engineering]] + [[memory-ablation]]. Capture is a filter. Adjectives die. Conflicts `flag_conflict`.
3. **Share a contract, not a chat.** [[audited-task-contract]] + [[harness-routing]] + [[entropy-gate]]. Planner proposes. Deterministic controller commits. Isolated worktrees. Validated diffs.
4. **Check instead of wishing.** [[verifiable-instructions]] + [[self-verification]] + [[anti-slop]]. Every schema rule has a check. High-risk answers get scored against citations. Reading `AGENTS.md` is not the check. See D8.
5. **Keep a human gate.** [[hunt-ship-loop]]. File first. Scouts write quietly. Vault does not post, pay, or send.

## What this batch does not prove

Viral clips are not methods. See [[contradictions]].

The wiki is still below the 50-100 source density [[src-papa-couch-compiler]] says is needed before compilation beats a good search. Treat today's pages as a seed, not a finished graph.

## Related

[[how-it-works]] · [[index]] · [[contradictions]] · [[agent-facing-docs]]
