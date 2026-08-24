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

## C8. Two Terminal-Bench lifts

[[src-jacky-self-verification]]: DeepSeek V4 Flash, sample 5, 79% to 88% on Terminal-Bench 2.1.

[[src-maverick-ultramode]]: DeepSeek V4 Flash 0731, N=5, 24% to 33% on 15 tasks, 40% to 75% on 4 recoverable tasks.

Resolution: cite the slice. Maverick's 15 tasks were failure-skewed. Same writeup estimates the model already about 83% on the full set and +2 to +5 from ultra. That full-set estimate sits near Jacky's 79% to 88%. Do not quote 24% to 33% as a full-bench result.

## C9. Gate outside the model vs LLM tournament

[[entropy-gate]] condition 3: objective gate outside the LLM.

[[ultra-mode]] apply gate: same-model win-rate margin. Author says confidence is noisy.

Resolution: tournament picks a candidate worktree. Apply is uncommitted. Tests or a human still gate ship. Do not treat the LLM margin as the outside-the-model gate.
