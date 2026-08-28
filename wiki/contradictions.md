---
id: meta:contradictions
type: meta
tags:
  - wiki
updated: 2026-08-28
---

# Contradictions

Flag, do not silently merge. Machine form: `wiki/data/contradictions.yaml`. List with `python3 tools/sb contradictions`. CSV disputed rows live in `wiki/claims.csv` with a `C#` in `pages`. See [[claims]]. Dual claim store: C17.

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

## C8. Two anti-slop tens

[[src-juampi-anti-slop-rank]] ranked ten writing skills. Vault default is that list.

[[src-openagentskill-anti-slop]] is another ten, including a code lint skill (dmmulroy/anti-slop).

Resolution: keep juampi's list as D6 writing default. Do not vendor either list. Do not merge them.

## C9. NGC Table 1 vs Table 3 Mistral MMLU-pro

[[src-arxiv-2510-16851]] Table 1 NGC Mistral MMLU-pro is 24.50. Table 3 hybrid @0.3 lists 33.67 with the same GPQA/GSM/MATH as Table 1.

Resolution: unresolved. Do not pick a number. Claims `c-ngc-mmlu-table1` / `c-ngc-mmlu-table3`. See [[ngc]].

## C10. HydroFusion abstract years vs §4.1

[[src-arxiv-2510-03744]] abstract says a ~10-year daily dataset. §4.1 is Boluo 1988–2020.

Resolution: keep the §4.1 span. Mark the abstract phrase as a clash. Claims `c-hydrofusion-abstract-years` / `c-hydrofusion-section-41`. See [[hydrofusion-lmf]].

## C11. UniTok 51.89% N@10 is Toys, not Tools

[[src-arxiv-2511-12922]] body/abs say up to 51.89% NDCG@10 on Tools. Table 7: that cell is Toys. Tools is 42.99% N@10.

Resolution: keep the table. See [[unitok]].

## C12. TIWM Mini val14 vs full val14

[[src-arxiv-2511-05540]] Mini val14 NR/R 88.05/89.54. Full val14 30.46/34.64.

Resolution: do not quote Mini as full val14. See [[tiwm]].

## C13. 4MAS graphical abstract vs Table 1

[[src-arxiv-2608-19514]] graphical abstract quotes 96.2% / 80.2%. Table 1 is 98.3 / 84.9 / 29.29.

Resolution: keep Table 1. Do not use the abstract art numbers. See [[fourmas]].

## C14. eptwts $100k / 10 months

[[src-deronin-growthos-vault]] quotes a friend @eptwts making $100k in 10 months on Whop as a shadow growth operator.

Resolution: `unverified`. Do not use as a forecast or as proof the vault works. See [[growth-operator]].

## C15. Foundry 3D paper vs Palantir Foundry

[[foundry-3d]] is arXiv 2511.20721 SuperTokens / Point-JEPA.

[[palantir-aip]] Foundry is Palantir's data platform. No enrollment here.

Resolution: do not mix the names. Local object table is [[vault-ontology]].

## C16. Headlong one stream vs entropy gate

[[headlong]] / [[src-laude-headlong]]: one thought stream, no per-user sessions, assume anything said is shared. The agent keeps thinking when idle.

[[entropy-gate]]: isolated worktrees, structured diffs, an objective gate outside the model.

Operator yes 2026-08-26 started a 1-hour local Ollama identity `hour`. Nested Docker overlay failed. Local unsandboxed for that hour only. Harvest 02:07Z: mind stopped; tests did not run. Still not the wiki compiler. Do not restart without a new operator yes.

## C17. Two claim registries

This branch compiled source `## Claims kept` into `wiki/claims.csv` with FACT / INFERENCE / OPINION.

Main locked D9 and put structured claims in `wiki/data/claims.yaml` for `python3 tools/sb`.

Resolution: unresolved. Keep both. Do not delete either table. Cite the id you used. Human names the canonical store. See [[claims]] and [[memory-system]].

## C18. Two retrieve engines

This branch added `tools/retrieve.py` and `tools/claim_protocol.py`, plus a hand-edited claims.csv schema.

Main already ships `python3 tools/sb ask`, `.cache/secondbrain.sqlite`, and compiled `wiki/claims.csv`. See [[retrieval]] and [[claims]].

Resolution: unresolved. Live Query stays `python3 tools/sb ask`. Do not wire the second CLI. Do not delete the PR tools without a human yes. Named chain: [[claim-protocol]].

## C19. Embeddings vs no vector DB

[[src-lan-e-claim-protocol-2026-08-27]] proposes BM25/FTS5 plus embeddings.

[[file-memory]] and main Deferred: vector DB only when too much to read. FTS5 is the disposable index.

Resolution: parked. Same as D9 and Deferred. See [[claim-protocol]].

## C20. Notion living skill library vs compiled git wiki

[[src-johnsjawn-skill-library]] says a GitHub folder known to 10% of the company fails, and Notion should be the home for collective AI skills.

This vault already locked D1 and D7: compile into `wiki/`, open the repo in Obsidian, do not vendor skill repos ([[anti-slop]]).

[[src-mukul975-cybersecurity-skills]] is that GitHub-folder form. GitHub API on 2026-08-23: 30758 stars, 3663 forks.

[[src-skill-pack-list]] adds five more GitHub folders, including an official Vercel pack.

Resolution: compile the product claims onto [[skill-library]]. Do not reopen D7. Do not vendor Notion or the GitHub packs. The 10% figure stays unverified. Star count does not authorize install.

Remap: this flag was C8 on the skill-library branch. Main C8 is the two anti-slop tens.

## C21. Skill improves with use vs usage count

[[src-johnsjawn-skill-library]] tweet: the best deal review skill gets better every time a sales rep uses it.

The attached demo shows a `# Uses` column and comments on skill pages. It does not show skill text changing after a use.

Resolution: keep the tweet line unverified. Cite the demo for usage visibility only.

Remap: was C9 on the skill-library branch. Main C9 is NGC tables.

## C22. Anthropic in the name, unaffiliated in the README

[[src-mukul975-cybersecurity-skills]] lives at `mukul975/Anthropic-Cybersecurity-Skills`.

The README says it is an independent community project, not affiliated with Anthropic PBC.

Resolution: cite [[mahipal-jangra]]. Do not call the pack an Anthropic product.

Remap: was C10 on the skill-library branch. Main C10 is HydroFusion years.

## C23. 817 skills vs the domain table

[[src-mukul975-cybersecurity-skills]] headline is 817 skills across 29 domains.

The same README's domain table sums to 785. The contributing section still says Deception Technology has 2 skills and Compliance & Governance has 5, against table values 6 and 9.

Resolution: treat 817 as author-stated. Quote C23 if a count is needed. Do not use the table as a proof of 817.

Remap: was C11 on the skill-library branch. Main C11 is UniTok Toys vs Tools.

## C24. Stale skill-pack counts

[[src-skill-pack-list]] paste: scientific 148, alirezarezvani 223 skills and 5,200+ stars.

READMEs and GitHub API on 2026-08-23:

- K-Dense badge 163. Same README also says 161. 148 is gone.
- alirezarezvani headline 364, convert section 345, API description 345 / 330+. README still says 5,200+ stars. API stars: 24841.
- vercel-labs 40+ and 100+ rule counts match the current README.

Resolution: quote the 2026-08-23 check on [[skill-library]]. Do not repeat the paste numbers as current.

Remap: was C12 on the skill-library branch. Main C12 is TIWM Mini vs full val14.

## C25. Retrieval paste vs D9 FTS query path

[[src-retrieval-second-brain]] says read-and-recall needs hybrid BM25 + vector + rerank, GraphRAG, and a MemGPT / Letta / LangChain / LlamaIndex landing.

D9 locks live query as `python3 tools/sb ask` over compiled markdown with disposable FTS5. AGENTS.md Deferred parks vector DB, Neo4j, MemGPT-style stores, and GraphRAG as a second memory.

The paste's "greatly raises retrieval accuracy" has no method. unverified.

Resolution: unresolved. Compile the four pillars onto [[retrieval-second-brain]]. Do not vendor those frameworks. Do not reopen D9 in this merge. Human should say whether C25 only parks GraphRAG/LangChain/vector, or also fights FTS5.

Remap: was C13 on the skill-library branch. Main C13 is 4MAS abstract art.
