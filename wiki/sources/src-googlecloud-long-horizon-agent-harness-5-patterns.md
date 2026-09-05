---
id: source:src-googlecloud-long-horizon-agent-harness-5-patterns
type: source
tags:
  - twitter
  - harness
created: 2026-09-05
updated: 2026-09-05
---

# src-googlecloud-long-horizon-agent-harness-5-patterns

- Canonical: https://x.com/GoogleCloudTech/status/2090248297214525569
- Article: https://x.com/i/article/2090246025403408384 — *5 design patterns for long-horizon agent harness*
- Authors named in article: @Saboo_Shubham_ · @secchi_elia · @lavinigam
- Reference impl (article): https://github.com/google/adk-samples/tree/main/core/python/long-horizon-harness (Apache 2.0; pointer only — not installed here)
- Secondary ZH digest: https://x.com/shao__meng/status/2096055921218879530 → thin [[src-shao-meng-long-horizon-harness-zh]]
- 判定: 入vault建議
- Quote untrusted. Not copied into `raw/`.
- Dedup: exact absent. Near: [[harness-routing]] · [[src-andrewng-ai-engineering-skills-map]] · [[src-pvncher-rethinking-skills-gpt6-astra]] · [[src-spotify-portal-claude-cheap-workers]] · [[lan-e-desk-team]].

## Claims kept

Long-horizon = agent keeps going across days/sessions; one-shot breaks in front of you, long-horizon breaks quietly and keeps running.

Five design patterns (Google Cloud Tech / Long Horizon harness):

1. **Stable prefix / cache** — sort prompt by change rate: frozen top (instructions, tools) · slow middle (profile) · volatile tail (memories, counters). Dynamic memory in the prefix kills cache; move to tail. Audit: turn-2 cached tokens still 0 ⇒ prefix moving.
2. **Write-behind memory** — reply first; extract memories async after. Safeguards: strong task refs; isolated sibling agent (min tools, no recurse hooks); throttle (~120s). Shutdown drain timeout < host cleanup limit.
3. **Persistent workspace** — scope to user not conversation; outlive turns via execution interface (local FS ↔ sandbox). Do not key liveness on status codes shared by dead vs booting (e.g. both 502).
4. **Explicit INCOMPLETE ≠ done + hard caps** — name terminal states; rewrite summary text so models cannot misread timeout as success (`INCOMPLETE: … Do not report this work as done`). Cap tool calls/iteration and iterations/session; at limit strip tools for plain-text handoff.
5. **Guard chain — no model in the chain** — normalize before compare (string-match metadata IP bypassed via integer form). Cheap→expensive short-circuit: exfil hard ban → policy allow/ask/deny → human ask last. Fully deterministic/auditable. Design credentials as if guards already beaten (env injection, sandbox egress off, placeholders to model).

## Pages updated

[[index-sources]] · [[harness-routing]]

## Related

[[src-shao-meng-long-horizon-harness-zh]] · [[harness-routing]] · [[src-andrewng-ai-engineering-skills-map]] · [[src-pvncher-rethinking-skills-gpt6-astra]] · [[src-rutin-astra-routine-prompt-pattern-2026-09]] · [[src-spotify-portal-claude-cheap-workers]] · [[lan-e-desk-team]] · [[src-openai-hf-agents-incident-2026]]
