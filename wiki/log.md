---
id: meta:log
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-27
---

# Log

Append-only. Each entry starts with `## [YYYY-MM-DD] kind | title`.

## [2026-08-28] engine | stable ids, FTS5, claims, sb validate, sb eval

Memory engine pass. Markdown stays canonical. `.cache/secondbrain.sqlite` is disposable. Claim registry in `wiki/data/claims.yaml`. CLI: `python3 tools/sb`. D9 locked. See [[retrieval]] [[claims]] [[stable-ids]] [[eval-suite]] [[memory-engine-2026-08-28]].

## [2026-08-27] loop17 | 0/116 ad6f669 v17-hardened

Floor held. worker_processes 1 source OOM=false. Leftover tracing/auth/TLS client-cert headers closed. chatbot-respond/2FA-verify/codefixes HTTP closed. v16 applied. PR27 merged 94ac04c. Last loop this window. See [[hunt-harden-loop]] [[src-lanbb-pr27-loop17]].

## [2026-08-27] loop16 | 0/116 75b62be v16-hardened

Floor held. worker_processes 1 source OOM=false. Leftover tracing/cloud-auth headers closed. CSAF/product-image/coupon-apply HTTP closed. v15 applied. PR26 merged 9e8bbdc. See [[hunt-harden-loop]] [[src-lanbb-pr26-loop16]].

## [2026-08-27] loop15 | 0/116 1801528 v15-hardened

worker_processes 1 baked. Floor held. Auto OOM 137 lesson. Leftover remote-user/oauth-proxy/tracing/cloud-auth headers closed. web3-walletExploitAddress/2FA-SPA/ftp-quarantine/solve-server-side/coupon HTTP closed. v14 applied. PR25 merged 02f73dc. See [[hunt-harden-loop]] [[src-lanbb-pr25-loop15]].

## [2026-08-27] loop14 | 0/116 4fd0b9f v14-hardened

Floor held. Leftover hop/session/token headers closed on score path. continue-code-findIt-apply/fixIt-apply/snippets-fixes/2FA-enter/web3-nft HTTP closed. v13 applied. PR24 merged e1c2c58. See [[hunt-harden-loop]] [[src-lanbb-pr24-loop14]].

## [2026-08-27] loop13 | 0/116 e8c3a57 v13-hardened

Floor mem>=6m pids>=6 held. Leftover rewrite/identity headers closed on score path. continue-code-apply/tutorial/access_token/ftp-backup HTTP closed. v12 applied. PR23 merged 00ed19d. See [[hunt-harden-loop]] [[src-lanbb-pr23-loop13]].

## [2026-08-27] loop12 | 0/116 v12-hardened

Fill v11 live 0/116 score 200 deny 403. Bake mem>=6m pids>=6. PR22 merged c201b56. See [[hunt-harden-loop]] [[src-lanbb-pr22-loop12]].

## [2026-08-27] loop11 | 0/116 3afb11b v11

Authorization/Origin/Referer closed on score path + leftover continue-code/login/search/Baskets/nested SPA HTTP closed. v10 applied (score 200, deny 403). PR21 merged 484fbbe. See [[hunt-harden-loop]] [[src-lanbb-pr21-loop11]].

## [2026-08-27] loop10 | 0/116 0042064 v10

trailing-slash-only GET /api/Challenges/ + empty-query/cookie-closed score path + leftover privacy/hidden/data HTTP closed. v9 applied. PR20 merged f8b4dbe. See [[hunt-harden-loop]] [[src-lanbb-pr20-loop10]].

## [2026-08-27] loop9 | 0/116 dee7041 v9

exact-equals GET /api/Challenges/ + host allowlist + leftover oauth/health/debug closed. v8 applied. PR19 merged 75cb3bc. See [[hunt-harden-loop]] [[src-lanbb-pr19-loop9]].

## [2026-08-27] loop8 | 0/116 v8-hardened

v7 wall applied (score GET 200, default-deny 403, POST 405). Report at 0/N. PR18 merged 7d98a3b. Next hunt v8. See [[hunt-harden-loop]] [[src-lanbb-pr18-loop8]].

## [2026-08-27] loop7 | 0/116 7dd37e7 v7

default-deny edge except score path + leftover SPA/JS + remaining /api /rest closed. v6 applied. v7 keeps apply then default-denies. PR17 merged 7b009d6. See [[hunt-harden-loop]] [[src-lanbb-pr17-loop7]].

## [2026-08-27] loop6 | 0/116 9795cd9 v6

juice root writable + tmpfs only /tmp + read-only edge + login closed + GET/HEAD only + SPA/static leak closed. v5 skipped EROFS/tmpfs. PR16 merged 2019d6c. See [[hunt-harden-loop]] [[src-lanbb-pr16-loop6]].

## [2026-08-27] loop5 | 0/116 17ca40d v5-hardened

juice read-only + drop OPTIONS + login WAF + identity/Web3/catalog/search/info-leak closed + burst>=1. GET /api/Challenges open. Login remaining auth door. PR15 merged 9227b47. See [[hunt-harden-loop]] [[src-lanbb-pr15-loop5]].

## [2026-08-27] loop4 | 0/116 821e998 v4-hardened

app/edge caps + broader URI WAF + GraphQL/basket/reviews/captcha/data-export closed. GET /api/Challenges stays open. PR12 dup closed. See [[hunt-harden-loop]] [[src-lanbb-pr13-loop4]].

## [2026-08-27] loop3 | 0/116 b5bfb4d v3-hardened

method allowlist + URI WAF + cookie/COEP/HSTS + read-only edge + upload/PII/chatbot/B2B/snippets/continue-code closed. GET /api/Challenges stays open. See [[hunt-harden-loop]] [[src-lanbb-pr11-loop3]].

## [2026-08-27] loop2 | 0/116 PR10 v2-hardened

keep v1 + digest pin + stronger headers + broader rate limits + WAF-ish query block + close /encryptionkeys /metrics /support /redirect. See [[hunt-harden-loop]] [[src-lanbb-pr10-loop2]].

## [2026-08-27] loop1 | 0/116 ee8da04 v1-hardened

headers + login rate-limit + extra-file /ftp closed. Local Juice Shop. PR9. See [[hunt-harden-loop]] [[src-lanbb-pr9-loop1]].
## [2026-08-27] ingest | LanBB BB = bug bounty flow

lan E 07:36 Taipei. Identity, not contamination. Hunter follows as input sources, not exploit dump. Ethical hacking = in-scope find + report. Ignore porn/adult lists. Do not write exploit methods. Presence Lab recon/IDOR/nuclei unverified. Brief: [[ingest-brief-2026-08-27-lanbb-bb]]. Not pushed.

## [2026-08-27] ingest | portable-memory, pipeline-honesty, assign-execute-verify

Delta only. No Brain clone. No Hawkes. 24h intel OFF. Skip listicle, Claude-AD, Kimi, Browser Use plugin.

## [2026-08-27] ingest | vending-bench + four method notes

[[vending-bench]], [[backlink-first]], [[views-vs-sales]], [[buying-signal]], [[drafts-not-publish]]. No Whop clone. Not dumped.

## [2026-08-27] ingest | grok bot tape

lan E share. Article not dumped. 58min video not ingested. See [[grok-bot-tape]] and [[src-0xcarnagee-tape-2026-08-27]]. Not pushed.

## [2026-08-27] ingest | multi-source verdict

lan E share. Article not dumped. Whop skip. See [[multi-source-verdict]] and [[src-everestchris6-revenue-2026-08-26]]. Not pushed.

## [2026-08-27] ingest | loop-graph engineering

lan E share. Article not dumped. See [[loop-graph-engineering]] and [[src-av1dlive-loop-graph-2026-08-26]]. No Kimi install. Not pushed.

## [2026-08-27] ingest | ai sovereignty

lan E paste. No primary Karp URL. Unverified. See [[ai-sovereignty]], [[alex-karp]], [[src-lan-e-karp-sovereignty-2026-08-27]]. work-per-cost already compiled. Not pushed.

## [2026-08-27] ingest | work per cost

Catalog of token-save methods already in wiki. KPI W/E counts. See [[work-per-cost]]. Not pushed.

## [2026-08-27] ingest | context compaction

Chat may be fuzzy. Vault must be precise. No transcript dumps. See [[context-compaction]]. Official vs community sources labeled. Not pushed.

## [2026-08-27] ingest | musk algorithm

lan E motto. Strict order. Best part is no part. See [[musk-algorithm]], [[first-principles]], [[src-lan-e-musk-algorithm]]. Not pushed.

## [2026-08-27] ingest | botdirectory scan + stale-fact-detector

Catalog scan, not dump. Vault methods: [[stale-fact-detector]], [[botdirectory-scan]]. See [[src-botdirectory-picks-2026-08-27]] and [[ingest-brief-2026-08-27-botdirectory]]. No new bots. Not pushed.

## [2026-08-27] ingest | composio + file memory

lan E share. [[composio-mcp]] not installed. [[file-memory]] four kinds. See [[src-coreyganim-composio]] and [[src-pawelhuryn-file-memory]]. Not scout. Not pushed.

## [2026-08-27] ingest | benln grok bot pro tips

lan E share. 10 tips + quota method. See [[grok-bot-pro-tips]], [[grok-bot-quota]], [[src-benln-grok-bot-pro-tips]]. Not scout. Not pushed.

## [2026-08-27] note | hxiao Headlong share

lan E share. URL parked. No Headlong method yet. See [[src-hxiao-headlong-share]]. Wait for experiments.

## [2026-08-27] ingest | debs_obrien token usage

lan E share. If bot usage is high, ask chief of staff: anyway we can improve token usage? thoughts? See [[src-debs-obrien-token-usage]], [[bot-voice]], [[tokens-as-capital]]. Not scout.

## [2026-08-25] implement | GrowthOS orb materials

Default Lambert spheres and CSS blur orbs looked cheap. Fresnel shader spheres, additive sprite halos, ACES + antialias. See [[growth-operator]].

## [2026-08-25] query | GrowthOS 3D plugin vs clone

Neither. Compiled subgraph HTML, not a plugin and not a product hunt. D5, D7, [[context-graph]]. See [[growthos-3d-gap-2026-08-25]] and [[growth-operator]].

## [2026-08-25] implement | GrowthOS GSAP chrome

Sidebar was always on-screen (`#side.open` had no CSS). GSAP `xPercent` open/close, compositor overlay paint, core flare. Figma MCP needs auth and is 2D; not used. See [[gsap-figma-note-2026-08-25]] and [[growth-operator]].

## [2026-08-25] implement | GrowthOS vault

Seven-layer operator notes in `growth/` from [[src-deronin-growthos-vault]]. DEMO partners. 3D graph `output/growthos-graph.html`. Briefing [[growth-briefing-2026-08-25]]. See [[growth-operator]] and [[ingest-brief-2026-08-25-growthos]].

## [2026-08-25] ingest | milesdeutscher grok bot use cases

lan E share. 25 use cases. Overlap: skill trainer, overnight coder, knowledge base. See [[grok-bot-use-cases]] and [[src-milesdeutscher-grok-bot-use-cases]]. Not scout.

## [2026-08-25] ingest | bot voice caveman

Bot-to-bot caveman. Facts, paths, SHAs. Style URL not ingested. See [[bot-voice]].

## [2026-08-25] ingest | bot voice

Bot-to-bot fluent language, English OK. Do not force Chinese between bots. lan E still gets Traditional Chinese from lead. See [[bot-voice]].

## [2026-08-25] ingest | surprise spot-check

Lead inspects without warning. Stay on-lane. Lessons go to wiki and a shared skill. [[raptor-dispatch]] also: no empty acks. See [[spot-check]].

## [2026-08-25] ingest | dry-migrate

Secret-scan first. Never migrate prod keys or customer data. Rebuild if context is hidden. See [[session-migrate]].

## [2026-08-25] ingest | skill recorder

Trial on a clean desktop with fake data, then [[skillspector]], then enable. See [[skill-recorder]], [[src-chatgpt-play-2026-08-25]], and [[ingest-brief-2026-08-25-skill-recorder]].

## [2026-08-25] ingest | play methods

Compiled [[skillspector]], [[quota-router]], [[raptor-dispatch]], [[session-migrate]], [[clip-pipeline]] from `/workspace/play-until-2pm/METHODS.md`. Reinforced D4 on [[audited-task-contract]] and [[harness-routing]]. Not copied into raw/. See [[src-play-methods-2026-08-25]] and [[ingest-brief-2026-08-25-play-methods]].

## [2026-08-24] ingest | BATCH09 five paper digests

Compiled [[camf-mft]], [[draftfm]], [[dmd-safety]], [[vgi-bench]], [[orthoskillvla]]. Figs unread. See [[src-arxiv-batch09]].

## [2026-08-24] ingest | BATCH08 five paper digests

Compiled [[dbosc]], [[fourmas]], [[hear2act]], [[unilang]], [[cvsd-reg]]. C13. Table 11 / Fig. 4 unread. See [[src-arxiv-batch08]].

## [2026-08-24] ingest | BATCH07 five paper digests

Compiled [[g-carl]], [[concept-guard]], [[r2-opd]], [[scape]], [[vla-self-demo]]. Table 4 of 2608.19490 not known. See [[src-arxiv-batch07]].

## [2026-08-24] ingest | BATCH06 five paper digests

Compiled [[two-stage-nn-tl]], [[dics]], [[skill-transfer]], [[iar]], [[bert-ler]]. Unread appendices/Gemma/LoRA/figs not known. See [[src-arxiv-batch06]].

## [2026-08-24] ingest | BATCH05 five paper digests

Compiled [[portal]], [[mpi-init]], [[pwr-ga]], [[brain-ai-convergence]], [[vs-graph]]. Figure-only accuracy `unverified`. See [[src-arxiv-batch05]].

## [2026-08-24] ingest | BATCH04 five paper digests

Compiled [[tiwm]], [[unitok]], [[llm4eo]], [[apt-siamese]], [[foundry-3d]]. Flagged C11 and C12. OCR-unclean tables `unverified`. See [[src-arxiv-batch04]].

## [2026-08-24] ingest | BATCH03 five paper digests

Compiled [[hydrofusion-lmf]], [[ngc]], [[sapin]], [[alphaevolve-math]], [[pavement-gnn]]. Flagged C9 and C10. AlphaEvolve 6.24–6.67 not known. See [[src-arxiv-batch03]].

## [2026-08-24] ingest | BATCH02 five paper digests

Compiled [[superde]], [[lance]], [[palrs]], [[prednext]], [[clustered-moe]]. Tables 7–8 of 2510.02345 marked `unverified`. See [[src-arxiv-batch02]].

## [2026-08-24] ingest | BATCH01 five paper digests

Compiled [[causal-cps-anomaly]], [[nmc-trace-complexity]], [[flow-matching-pso]], [[bdh]], [[evosyn]] from `/workspace/arxiv-tierlist/digests/`. Linked [[arxiv-tierlist]]. Unread appendices not treated as known. See [[src-arxiv-batch01]].

## [2026-08-24] update | arXiv corpus 405856

Counts-only. Gap batch 6 +72800. Total 405856. Tiers S 16443 / A 42228 / B 197545 / C 113767 / D 35873. Cursor 2022-06-08. No paper known. See [[arxiv-tierlist]].

## [2026-08-24] update | arXiv corpus 333056

Counts-only. Gap batch 5 +52000. Total 333056. Tiers S 15929 / A 31021 / B 157813 / C 96860 / D 31433. Cursor 2021-06-25. See [[arxiv-tierlist]].

## [2026-08-24] rule | digest selected papers

Human: every selected paper needs a digest. Do not blindly dump or update counts only. Wiki still does not harvest. See [[MEMORY]].

## [2026-08-24] update | arXiv corpus 281056

Gap batch 4: +124800. Total 281056. Tiers S 15611 / A 23345 / B 129379 / C 84566 / D 28155. Cursor 2020-10-15. Remaining gap 2020-10 to 2025-06. Pages URL unchanged. See [[arxiv-tierlist]].

## [2026-08-24] ingest | three new X URLs

TheWhizzAI ARC-AGI-3 30.2→100 marked `unverified` (NVIDIA blog exists, no paper). chatchat Living Brain linked to [[memory-engineering]] and [[agent-operating-system]]. g3t0ffmyl4wn body not retrieved. raw/ not written.

## [2026-08-24] ingest | five X scouts

Ingested Mrgreenieybt3, beamnxw, promptyx_ai, openagentskill, AgentMemoryL. Linked [[llm-wiki]], [[memory-engineering]], [[harness-routing]], [[anti-slop]]. Flagged C8. No papers invented. raw/ not written.

## [2026-08-24] update | arXiv Pages live at 156256

https://elan7192.github.io/arxiv-potential-tierlist/ shows 156256. Cursor 2018-04. Batch 3 +27300. See [[arxiv-tierlist]].

## [2026-08-24] update | arXiv corpus 156256

Total 156256 from `stats.json`. Tiers S 15167 / A 8719 / B 60883 / C 52306 / D 19181. Remaining gap 2018-04 to 2025-06. URL unchanged. Handoff md had not yet grown a batch-3 section. See [[arxiv-tierlist]].

## [2026-08-24] ingest | marfinxx TRACE

Ingested https://x.com/marfinxx/status/2091496044961968275. Paper exists: arXiv 2608.09153. Kept 72.7 / 82 / 96 / 16x / 83 vs 33. Marked 84 / 76 / 4.2x `unverified`. Linked [[trace]] [[memory-engineering]] [[context-graph]] [[tokens-as-capital]]. raw/ not written.

## [2026-08-24] update | arXiv Pages live at 128956

https://elan7192.github.io/arxiv-potential-tierlist/ shows 128956. Cursor 2017-04. See [[arxiv-tierlist]].

## [2026-08-24] update | arXiv corpus 128956

Gap batch 2: +22100 unique. Total 128956. Tiers S 15114 / A 6509 / B 46431 / C 43858 / D 17044. Remaining gap 2017-04 to 2025-06. URL unchanged. See [[arxiv-tierlist]].

## [2026-08-24] update | arXiv Pages live at 106856

https://elan7192.github.io/arxiv-potential-tierlist/ is current. Counts already on [[arxiv-tierlist]]. No tokens. raw/ not written.

## [2026-08-24] update | arXiv corpus 106856

Gap batch 1: +26001 unique. Total 106856. Tiers S 15094 / A 5274 / B 35515 / C 36167 / D 14806. Remaining gap 2016-06 to 2025-06. Pages URL unchanged until push lands. See [[arxiv-tierlist]].

## [2026-08-24] rule | wiki stays current, takes bot improvements

Human: wiki must know the compiled vault. Other bots send improvements here for ingest. Do not invent. See [[MEMORY]].

## [2026-08-24] update | arXiv tierlist GitHub Pages

Durable URL https://elan7192.github.io/arxiv-potential-tierlist/ (HTTP 200). Repo https://github.com/elan7192/arxiv-potential-tierlist. ZeroDeploy marked stale on [[arxiv-tierlist]] and [[MEMORY]]. No tokens stored.

## [2026-08-24] update | LanBB repo landed

[elan7192/LanBB](https://github.com/elan7192/LanBB) exists on main. semantica is `tools/semantica` @ 6c2ccfd. Recorded on [[lanbb]].

## [2026-08-24] decision | LanBB new repo, semantica as tool

Human: create a new GitHub repo named LanBB and put semantica in as a tool. Recorded on [[lanbb]] and [[MEMORY]]. Vault does not create the repo.

## [2026-08-24] ingest | arXiv potential tierlist

Compiled `/workspace/arxiv-tierlist/ARXIV_TIERLIST_HANDOFF.md` into [[src-arxiv-tierlist-handoff]], [[arxiv-tierlist]], and [[potential-ranking]]. Display is per-tier top 800. Ranking axis is potential, not citation. Public ZeroDeploy URL is temporary. No deploy tokens stored.

## [2026-08-24] lint | Concept clusters in the graph

The hairball was ring-by-folder layout plus catalog stars (`index`, `log`, `twitter`). Graph filter now keeps wiki/maps/hunt/ship and drops `raw/`, `index`, `log`, and `twitter`. Renderer places nodes on the five [[agent-operating-system]] layers. Added peer concept links already supported by those pages. Locked D8.

## [2026-08-23] lint | Obsidian vault layer

Added `.obsidian` graph colors, [[Home]] as door, [[maps]] / [[hunt]] / [[ship]] indexes, and rendered `output/obsidian-graph.html`. Locked D7.

## [2026-08-23] ingest | Nine X posts into compiler vault

Created Karpathy layout (`raw/`, `wiki/`, `AGENTS.md`). Ingested nine X URLs from 2026-08-17 to 2026-08-22. Wrote 12 concept pages, 9 source pages, 3 people pages, [[contradictions]], [[agent-operating-system]], and `output/ingest-brief-2026-08-23.md`. Locked D1–D6 in `decisions.md`.

Pages touched: [[llm-wiki]], [[tokens-as-capital]], [[memory-engineering]], [[memory-ablation]], [[verifiable-instructions]], [[audited-task-contract]], [[harness-routing]], [[entropy-gate]], [[self-verification]], [[anti-slop]], [[hunt-ship-loop]], [[context-graph]], all `wiki/sources/*`, [[andrej-karpathy]], [[jacky-kwok]], [[rohit]].
