---
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-23
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

## C8. Notion living skill library vs compiled git wiki

[[src-johnsjawn-skill-library]] says a GitHub folder known to 10% of the company fails, and Notion should be the home for collective AI skills.

This vault already locked D1 and D7: compile into `wiki/`, open the repo in Obsidian, do not vendor skill repos ([[anti-slop]]).

[[src-mukul975-cybersecurity-skills]] is that GitHub-folder form. GitHub API on 2026-08-23: 30758 stars, 3663 forks.

[[src-skill-pack-list]] adds five more GitHub folders, including an official Vercel pack.

Resolution: compile the product claims onto [[skill-library]]. Do not reopen D7. Do not vendor Notion or the GitHub packs. The 10% figure stays unverified. Star count does not authorize install.

## C9. Skill improves with use vs usage count

[[src-johnsjawn-skill-library]] tweet: the best deal review skill gets better every time a sales rep uses it.

The attached demo shows a `# Uses` column and comments on skill pages. It does not show skill text changing after a use.

Resolution: keep the tweet line unverified. Cite the demo for usage visibility only.

## C10. Anthropic in the name, unaffiliated in the README

[[src-mukul975-cybersecurity-skills]] lives at `mukul975/Anthropic-Cybersecurity-Skills`.

The README says it is an independent community project, not affiliated with Anthropic PBC.

Resolution: cite [[mahipal-jangra]]. Do not call the pack an Anthropic product.

## C11. 817 skills vs the domain table

[[src-mukul975-cybersecurity-skills]] headline is 817 skills across 29 domains.

The same README's domain table sums to 785. The contributing section still says Deception Technology has 2 skills and Compliance & Governance has 5, against table values 6 and 9.

Resolution: treat 817 as author-stated. Quote C11 if a count is needed. Do not use the table as a proof of 817.

## C12. Stale skill-pack counts

[[src-skill-pack-list]] paste: scientific 148, alirezarezvani 223 skills and 5,200+ stars.

READMEs and GitHub API on 2026-08-23:

- K-Dense badge 163. Same README also says 161. 148 is gone.
- alirezarezvani headline 364, convert section 345, API description 345 / 330+. README still says 5,200+ stars. API stars: 24841.
- vercel-labs 40+ and 100+ rule counts match the current README.

Resolution: quote the 2026-08-23 check on [[skill-library]]. Do not repeat the paste numbers as current.
