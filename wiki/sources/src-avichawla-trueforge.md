---
id: source:src-avichawla-trueforge
type: source
tags:
  - twitter
created: 2026-08-24
updated: 2026-09-05
---

# src-avichawla-trueforge

- URL: https://x.com/_avichawla/status/2091804330118861239
- Author: _avichawla (Avi Chawla)
- Tweet: 2091804330118861239
- Created: 2026-08-24 08:26:30 UTC
- Article title: How to Cut Agent Tokens by 2.7x (using an open harness)
- Not copied into `raw/`.

## Claims kept

X article. Closing line thanks TrueFoundry for working on it. Sponsored. No paper.

Harness, not model, decides how much context the model sees, how often it is called, which tools it can reach, and what carries between steps. Fits [[harness-routing]].

Four named strategies plus compaction. Compiled on [[flat-context]].

Sandbox must not hold model keys or MCP credentials. Code Mode `call_tool` routes back through the harness, which applies stored credentials. Approvals still apply. Fits [[secret-gateway]].

Article-reported numbers, all `unverified`:

- LangChain deepagents-cli 52.8% to 66.5% on Terminal Bench 2.0 with gpt-5.2-codex, outside top 30 to rank 5.
- One 50,000-token tool payload re-read fifteen times is 800,000 tokens in the window. Caching makes the bill closer to 3x one read than to 16x. Window occupancy is unchanged.
- Title: 2.7x token cut.
- Body: TrueForge vs Claude Managed Agents vs deepagents on 14 DevRev Enterprise-Bench tasks, same model and tools, fresh session, LLM judge, all-criteria pass. Success is a three-way tie (one-task gap). TrueForge used about 40% of Claude Managed Agents tokens and under a quarter of deepagents'. 40 min per run vs 63 and 64.
- GLM-5.2 on TrueForge: roughly the same task count at 75% lower cost than Claude Agents on Opus 4.8.
- Conclusion: two harnesses, same 14 tasks, one spent 2.7x the tokens.

Linked vendor blog: https://www.truefoundry.com/blog/engineering/trueforge-vs-claude-managed-agents-benchmark/ also `unverified`. Table there (not line-read from the X images): TrueForge 3.8M tokens / $8.5 / 40 min; Claude Managed Agents 10M / $11.8 / 63 min; deepagents 16.5M / $21 / 64 min. Solved ~11 / ~11 / ~10 of 14.

See [[contradictions]] C41. Do not pick a multiplier.

Repo named in the article: https://github.com/truefoundry/trueforge. Docs: https://trueforge.dev/. MIT and self-hostable are article claims. Local: Node 22.13+, `npx @truefoundry/trueforge`, http://localhost:8790.

X article figures unread.

## Pages updated

[[flat-context]] · [[harness-routing]] · [[secret-gateway]] · [[entropy-gate]] · [[tokens-as-capital]] · [[agent-operating-system]] · [[contradictions]]

## Related

[[src-spotify-portal-claude-cheap-workers]] (Spotify Portal/AiKA + shunt cheap-workers; VERIFIED primary; ~90% bulk-read mean; hard gate SHUNT_MIN_LINES 350). Secondary cite: [[src-undefinedki-spotify-claude-cheap-workers]].
