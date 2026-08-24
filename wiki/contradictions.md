---
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-24
---

# Contradictions

Flag, do not silently merge.

## C1. Karpathy did not say stop writing code

[[src-bober-folder-workflow]] says Karpathy told people to stop using AI to write code and build a second brain instead.

[[andrej-karpathy]]'s gist is about compiling a wiki. It does not ban coding agents.

Resolution: treat Bober's line as marketing. Keep the gist.

## C2. Two folder skeletons

Karpathy / [[src-papa-couch-compiler]] / Bober's tweet: `raw/`, `wiki/`, schema.

Bober's older article: `notes/`, `people/`, `projects/` plus `MEMORY.md`.

Avid: Hunt / Ship / Maps / CoS wiki.

Resolution: D1 plus D7. Compiler stays `raw/` + `wiki/`. Avid's Hunt / Ship / Maps exist as indexes and graph colors, not a second knowledge store. `MEMORY.md` and `decisions.md` stay at repo root.

## C3. 200-agent cinematic vs 64-worker study

[[src-hitu-entropy-engineering]] tweet: 200 agents, 20 seconds, 100% coverage.

Same author's article: 64 Haiku workers, measured hallucination index and cost.

Resolution: cite the 64-worker table. Mark the 200-agent clip `unverified`.

## C4. Shared memory vs shared contract

[[entropy-gate]]: shared conversational memory poisons swarms.

[[audited-task-contract]]: agents should share verified state.

Resolution: compatible. Share a small audited contract. Do not share transcripts or unverified peer claims.

## C5. Living CLAUDE.md profile vs adjective death

[[src-papa-couch-compiler]] wants a compiled profile of who you are and how you think.

[[memory-ablation]] kills "prefers concise answers" and "interested in AI".

Resolution: D3. Profile files may exist. They may only hold facts that change answers. Interview prompts that produce adjectives get filtered before `MEMORY.md`.

## C6. Exact Voxyz blocks missing

[[src-voxyz-verifiable-instructions]] promises eight copy-paste blocks. Retrieved text stops at the promise.

Resolution: encode the three-part rule in `AGENTS.md`. Re-ingest if the blocks appear.

## C7. Income claim

[[src-bober-folder-workflow]] claims $17k/month from the workflow.

Resolution: `unverified`. Do not use as evidence that the architecture works.

## C8. File first vs code first

[[hunt-ship-loop]] files the source before answering.

[[src-dair-agent-friendly-docs]] measured public agentic PRs: among multi-commit PRs that change both and have order, code is first 4.7× more often than documentation.

Resolution: keep file-first for this vault (D1, D7). The paper describes observed public-agent PRs, not this compiler's ingest loop. Do not treat code-first as a schema change.

## C9. Prose checks vs observed validation

[[verifiable-instructions]] requires every rule to have a check.

[[src-dair-agent-friendly-docs]] recorded zero documentation-based validation events. The authors say actionability and verifiability lack consistent behavioural support.

Resolution: compatible. Observed agents do not validate against prose. This vault requires an external gate (`python3 tools/lint-wiki.py`) because reading `AGENTS.md` is not the check. See D8 and [[agent-facing-docs]].
