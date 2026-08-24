---
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-24
---

# Decisions

Locked choices. Reopen only with new evidence.

## D1. Compiler vault

Use the Karpathy LLM-wiki layout: immutable `raw/`, agent-owned `wiki/`, schema in `AGENTS.md`.

- Source: [[llm-wiki]], [[tokens-as-capital]]
- Locked: 2026-08-23
- Revalidate: if a later source shows the wiki is rotting or answers are worse than raw retrieval

## D2. One schema, two filenames

`AGENTS.md` is canonical. `CLAUDE.md` only points at it.

- Source: [[verifiable-instructions]], [[audited-task-contract]]
- Locked: 2026-08-23

## D3. Facts, not adjectives

`MEMORY.md` and schema rules must change an answer. Taste lines are rejected.

- Source: [[memory-ablation]]
- Locked: 2026-08-23

## D4. Shared state is a contract

Harnesses keep native sessions. They share an audited task contract, not transcripts or KV cache.

- Source: [[audited-task-contract]], [[entropy-gate]]
- Locked: 2026-08-23

## D5. Human final yes

Nothing in the vault posts, pays, or sends.

- Source: [[hunt-ship-loop]]
- Locked: 2026-08-23

## D6. Anti-slop by default

Writing follows [[anti-slop]] unless the human asks for another voice.

- Source: [[anti-slop]]
- Locked: 2026-08-23

## D7. Obsidian is the IDE

Open the repo as an Obsidian vault. `Home.md` is the door. Hunt / Ship / Maps are navigation. `wiki/` stays the compiled store.

- Source: [[hunt-ship-loop]], [[src-avid-obsidian-agent-team]]
- Locked: 2026-08-23

## D8. Instruction files are the control surface

Put steerage in `AGENTS.md`, `wiki/`, `MEMORY.md`, and `decisions.md`. Do not add a rule only in README or API docs. Reading those files is not the check. After they change, run `python3 tools/lint-wiki.py`.

- Source: [[agent-facing-docs]], [[verifiable-instructions]]
- Locked: 2026-08-24
- Revalidate: if a later source shows this vault's agents follow README or API docs, or that reading schema substitutes for lint and tests

## D9. Bibliographic catalog only

The Disclosure Index is compiled as stats, schema, and canonical URLs. Do not copy report bodies into `wiki/` or `output/`. Do not write exploit steps from those records.

- Source: [[disclosure-index]], [[src-disclosure-index]]
- Locked: 2026-08-24
- Revalidate: if the human asks for a specific public record's metadata fields already in the catalog snapshot
