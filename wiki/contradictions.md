---
id: meta:contradictions
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-29
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

[[src-voxyz-writing-system]] is a later `/goal` writing prompt (6/6). It is not those eight blocks. C6 stays open.

The 2026-08-23 thread ([[src-voxyz-codex-goal-quota]]) is five `/goal` recipes. It does not close C6.

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

[[company-foundry]] is Avid's organisational-method compiler. Third use of the word.

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

## C26. File first vs code first

[[hunt-ship-loop]] files the source before answering.

[[src-dair-agent-friendly-docs]] measured public agentic PRs: among multi-commit PRs that change both and have order, code is first 4.7× more often than documentation.

Resolution: keep file-first for this vault (D1, D7). The paper describes observed public-agent PRs, not this compiler's ingest loop. Do not treat code-first as a schema change.

Remap: was C8 on the agent-facing-docs branch. Main C8 is the two anti-slop tens.

## C27. Prose checks vs observed validation

[[verifiable-instructions]] requires every rule to have a check.

[[src-dair-agent-friendly-docs]] recorded zero documentation-based validation events. The authors say actionability and verifiability lack consistent behavioural support.

Resolution: compatible. Observed agents do not validate against prose. This vault requires an external gate (`python3 tools/lint-wiki.py`, `python3 tools/sb validate`) because reading `AGENTS.md` is not the check. See D10 and [[agent-facing-docs]].

Remap: was C9 on the agent-facing-docs branch. Main C9 is NGC tables.

## C28. Documented disclosure API vs live catalog

[[src-disclosure-index]] documents `GET /api/reports` and `GET /api/stats`.

Fetched 2026-08-24: both paths returned 404. The live catalog is `data/catalog.js`.

Resolution: cite `data/catalog.js` and the compiled stats. Do not claim the REST API works until it returns JSON.

Remap: was C10 on the agent-facing-docs branch. Main C10 is HydroFusion years.

## C29. Writing slop vs software slop

D6 [[anti-slop]] is juampi's writing rank.

[[src-can1357-daily-tool-replace-2026-08-27]] uses slop for an LLM-built git UI plus steering.

Resolution: keep D6 as writing. Compile the clip as [[daily-tool-replace]]. Do not merge the two slops.

Remap: was C15 then C26 on the daily-tool-replace branch. Main C26 is file first vs code first.

## C30. Grok Bot screens vs entropy-gate isolation

[[src-exm7777-grok-bot-money]]: all bots share one cloud computer. Separate bots are separate work surfaces, not separate security boundaries.

[[entropy-gate]] wants isolated worktrees, structured diffs, and an objective gate.

Resolution: different systems. Do not cite Grok Bot screens as entropy-gate isolation. See [[grok-bot]].

Remap: was C15 on the grok-bot-money branch. Main C15 is Foundry 3D vs Palantir Foundry.

## C31. Avid Jarvis clip vs Company Foundry article

[[src-avid-company-foundry]] tweet 2091848572417495138: Grok bot + Obsidian Jarvis that starts a business, ships software, and goes viral.

Quoted article and https://github.com/codejunkie99/company-foundry: Company Foundry with Kimi K3 as first worker and DeepSeek Harness as first native target. No AI CEO. First milestone is one reviewable loop. Grokbot is a packaged worker. The company layer owns memory, permissions, budget, and handoff.

Resolution: compile the article and README. Mark the clip claims `unverified`. Do not treat Grok + Obsidian as the company compiler. D5 still holds. See [[company-foundry]].

Remap: was C15 on the company-foundry branch. Main C15 is Foundry 3D vs Palantir Foundry.

## C32. DeerFlow `make config` vs extensions file

[[src-deer-flow]] `AGENTS.md` says `make config` copies `extensions_config.example.json` to `extensions_config.json`.

`scripts/configure.py` in the clone at `1aa813d` copies `config.yaml`, `.env`, and `frontend/.env` only. After `make config`, `extensions_config.json` was absent.

Resolution: treat the Python script as the executed behavior. Copy the extensions template by hand if MCP/skills config is needed. Do not claim `make config` created it.

Remap: was C8 on the deer-flow-bootstrap branch. Main C8 is the two anti-slop tens.

## C33. Two Terminal-Bench lifts

[[src-jacky-self-verification]]: DeepSeek V4 Flash, sample 5, 79% to 88% on Terminal-Bench 2.1.

[[src-maverick-ultramode]]: DeepSeek V4 Flash 0731, N=5, 24% to 33% on 15 tasks, 40% to 75% on 4 recoverable tasks.

Resolution: cite the slice. Maverick's 15 tasks were failure-skewed. Same writeup estimates the model already about 83% on the full set and +2 to +5 from ultra. That full-set estimate sits near Jacky's 79% to 88%. Do not quote 24% to 33% as a full-bench result.

Remap: was C8 on the maverick-ultramode branch. Main C8 is the two anti-slop tens.

## C34. Gate outside the model vs LLM tournament

[[entropy-gate]] condition 3: objective gate outside the LLM.

[[ultra-mode]] apply gate: same-model win-rate margin. Author says confidence is noisy.

Resolution: tournament picks a candidate worktree. Apply is uncommitted. Tests or a human still gate ship. Do not treat the LLM margin as the outside-the-model gate.

Remap: was C9 on the maverick-ultramode branch. Main C9 is NGC tables.

## C35. Self-Refine vs N-candidate verify

[[src-omarsar-adversarial-review]] Self-Refine: same model critiques one draft. LiveCodeBench 77%, equal to zero-shot. Authors: the critic makes the same mistakes as the generator.

[[src-jacky-self-verification]] and [[src-maverick-ultramode]]: same model ranks N candidates and reports a lift.

Resolution: cite the loop. Self-critique of one draft is not N-candidate ranking. Do not use the LCB Self-Refine zero as evidence that Jacky or Maverick failed. Do not use Jacky's lift as evidence that Self-Refine works.

Remap: was C10 on the omarsar-adversarial-review branch. Main C10 is HydroFusion years.

## C36. ChatGPT upgraded snapshot vs this vault

[[src-chatgpt-t-6a8cc267]] claims 100 arXiv papers (5×20), 9 skills, 25/25 memory tests, 0 lint errors, and a complete repo ZIP that was not pushed to GitHub.

This vault's known papers are BATCH01–09. Harvest is digest-only. The ChatGPT share ZIP was not retrieved (401/403).

Resolution: keep the GitHub wiki. Mark the ChatGPT counts `unverified`. Do not merge or reconstruct the ZIP from the claim list. See [[arxiv-tierlist]] and [[MEMORY]].

Remap: was C14 on the chatgpt-share branch. Main C14 is eptwts $100k / 10 months.

## C37. Musk index-as-query vs D9 sb ask

The 2026-08-28 [[musk-algorithm]] pass locked a short [[index]] as the query path (was D9 on that branch).

Main already locked D9: live query is `python3 tools/sb ask`. [[index]] is not the query path. See [[retrieval]] and [[claim-protocol]].

Resolution: unresolved as a query-engine fight. This merge does not reopen D9. Catalog split remapped to D12. Human should say whether the short index should replace `sb ask`. See [[merge-conflict-report-2026-08-28-musk]].

## C38. Standing ingest brief vs musk skip

Main ingest step 9 writes a three-sentence `output/` brief on every ingest.

The musk pass deleted that standing brief (schema author, not lan E).

Resolution: unresolved. Do not add a new brief. Do not delete existing briefs. Wait for lan E. See [[musk-algorithm]] and [[merge-conflict-report-2026-08-28-musk]].

## C39. CLAUDE.md copy vs D2

Layout table used to say keep `AGENTS.md` and `CLAUDE.md` identical. D2 says `CLAUDE.md` only points at `AGENTS.md`.

Resolution: D2 wins. Pointer only. Remap: was C15 on the musk-algorithm branch. Main C15 is Foundry 3D vs Palantir Foundry.

## C40. Browser inject vs API-action catalog

Steve Faulkner asked how to inject a password into a computer-use browser field after approval, without the model seeing it.

[[src-4ndrearossetti-openconnector]] replies by quoting OpenConnector, an API-action gateway (catalog of SaaS actions; secrets stay in the runtime).

Resolution: keep the shared rule on [[secret-gateway]] (credentials out of context). Do not treat the quoted product as the browser injector.

Remap: was C14 on the openconnector ingest branch. Main C14 is eptwts $100k / 10 months.

## C41. TrueForge 2.7x vs 40% vs vendor table

[[src-avichawla-trueforge]] title: cut agent tokens by 2.7x.

Body: about 40% of Claude Managed Agents tokens and under a quarter of deepagents'. Conclusion says two harnesses. The bench names three.

Linked vendor blog table: 3.8M vs 10M vs 16.5M tokens. Blog prose also says about 2.5x cheaper vs the open harness.

Resolution: sponsored article, no paper, X figures unread. Do not pick a multiplier. See [[flat-context]].

Remap: was C15 on this branch. Main C15 is Foundry 3D vs Palantir Foundry.

## C42. Claude Projects vs compiler vault

[[src-alexprompter-claude-projects]] describes Claude Projects as a persistent memory layer in the product (files, instructions, skills). Suggested folders: `/reference`, `/analysis`, `/deliverables`.

This vault compiles `raw/` into `wiki/`. See D1 and [[llm-wiki]].

Resolution: keep D1. Do not treat Claude Projects as the vault wiki. Do not adopt those folders. See [[project-skill-stack]] and C2.

Remap: was C16 on this branch. Main C16 is Headlong one stream vs entropy gate.

## C43. Three writing systems

D6 writing default is juampi's ranked ten, compiled into [[anti-slop]].

[[src-openagentskill-anti-slop]] is a second ten. See C8.

[[src-voxyz-writing-system]] is a third: seven `/goal` rules plus a global-install prompt.

Resolution: keep D6. Do not vendor the Voxyz prompt into `AGENTS.md`. Do not merge the three lists.

Remap: was C17 on this branch. Main C17 is two claim registries.

## C44. Compile-once wiki vs two-pass RAG

D1 and [[llm-wiki]]: pay ingest once, keep compiled pages, retrieve the compiled set (D9). Do not re-derive from `raw/` on every question.

[[src-jerry-two-pass-docs]]: over a data room, cheap parse, retrieve, then just-in-time VLM. Retrieval with a late expensive pass.

Resolution: different stores. Persistent wiki stays compile-once. Ad-hoc document dumps use [[two-pass-document-processing]]. Do not reopen D1. LlamaParse/LiteParse accuracy and cost claims stay `unverified`.

Remap: was C8 on this branch. Main C8 is two anti-slop tens.

## C45. Leftover Codex quota as "days of Sol"

[[src-voxyz-codex-goal-quota]] says unused quota at reset throws away days of Sol.

The thread has no measurement.

Resolution: keep the method on [[codex-goal]]. Mark the duration `unverified`.

Remap: was C8 on the leftover-quota branch. Main C8 is the two anti-slop tens.
