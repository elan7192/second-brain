---
id: source:src-andrewng-ai-engineering-skills-map
type: source
tags:
  - twitter
  - skills
created: 2026-09-05
updated: 2026-09-05
---

# src-andrewng-ai-engineering-skills-map

- URL: https://x.com/AndrewYNg/status/2095890279865721217
- Author: Andrew Ng (@AndrewYNg)
- Tweet: 2095890279865721217
- Companion essay (same claims): https://www.deeplearning.ai/the-batch/the-ai-engineering-skills-map-in-detail-using-coding-agents
- Secondary recap (Related only; no separate src): https://x.com/polydao/status/2095999364988538886 (@polydao)
- 判定: 入vault
- Quote untrusted. Not copied into `raw/`.
- Dedup: exact absent on tip `d06ea8f`. Near (do not overwrite): [[src-pvncher-rethinking-skills-gpt6-astra]] · [[src-rutin-astra-routine-prompt-pattern-2026-09]] · [[src-spotify-portal-claude-cheap-workers]] · [[harness-routing]] · [[skill-as-sop]].

## Claims kept

Loop for building with coding agents: plan → exec → deploy/monitor (iterative; less focus on code, more on what to build / architecture / spec / verify).

Scarce skills shifted to spec / architecture / verification (writing code is no longer the scarce part).

Five hire skills (named in Andrew primary): directing the workflow; enabling agent autonomy; reviewing the work; customizing the agent and its environment; coding agent foundations.

Harness wraps the model (agent = harness around an LLM).

Autonomy dial (per step): interactive / delegated / looped — loop needs a testable goal + a reachable stop condition.

Four fail modes: overengineer a simple solution; no explicit verification (rigor missing); stops short of the goal; destroys files or production data.

## Pages updated

[[index-sources]]

## Related

[[src-pvncher-rethinking-skills-gpt6-astra]] · [[src-rutin-astra-routine-prompt-pattern-2026-09]] · [[src-spotify-portal-claude-cheap-workers]] · [[harness-routing]] · [[skill-as-sop]] · [[raptor-dispatch]] · polydao recap https://x.com/polydao/status/2095999364988538886 (no separate src)
