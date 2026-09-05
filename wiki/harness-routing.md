---
id: concept:harness-routing
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-09-05
---

# Harness routing

A model and a harness are different knobs.

Source: [[src-rohit-harness-router]]. Related environment-design source (not a router): [[src-kaorixbt-harness-engineering]].

## Two choices

1. Which model fits difficulty, risk, latency, budget.
2. Which harness supplies tools, permissions, discovery, and loop.

Example from the article: Claude Code loads nested `CLAUDE.md` files. Codex takes at most one instruction file per directory with a 32 KiB default cap. pi exposes four tools by default.

Those differences change the prompt prefix and the available actions. The same model can behave differently in two harnesses.

## Routing rules

1. Route before a phase starts. Do not switch every few turns.
2. Keep session affinity until the phase ends, fails, or crosses a risk line.
3. Switch only at a verified checkpoint from the [[audited-task-contract]].

Transfer semantic state. Do not depend on KV cache or prompt-cache reuse across harnesses.
From use 2026-08-25: agents share contract, not free agent chat. See [[raptor-dispatch]] and [[session-migrate]].

[[src-avid-company-foundry]]: the harness owns the company method. The router selects the worker. Article lanes: economy, fast, capable. Every route needs a receipt. Kimi K3 is a first capable-tier worker, not a locked owner. See [[company-foundry]] and [[quota-router]].

[[src-retrieval-second-brain]] agentic routing: split the question, call tools, reflect, query again. This vault's split is `python3 tools/sb ask` then the evidence set (D9). A second pass is ingest or lint, not a reranker. See [[retrieval-second-brain]] and C25.

[[ultra-mode]] can spread the N attempts across harness commands in one pass and judge them with one verifier. That is routing inside a single task, not a mid-turn harness swap. Source: [[src-maverick-ultramode]].

## Document dumps

[[src-jerry-two-pass-docs]] says Codex and Cowork already two-pass a data room: pdf2text, then the harness model as VLM (Opus 5 named). File that under harness defaults. See [[two-pass-document-processing]].

## Test before you believe it

Compare a fixed pair, a fixed pair with audited state, and routed executors. If routing loses to the reset tax, keep the fixed pair.

## Related

Identity `hour` 1h local Ollama trial ended 2026-08-26T02:07Z (operator yes). Nested Docker overlay failed on this VM. Tests did not run. Do not restart without a new operator yes. Not the wiki runtime. See C16. · [[src-googlecloud-long-horizon-agent-harness-5-patterns]]

[[audited-task-contract]] · [[entropy-gate]] · [[rohit]] · [[jerry-liu]] · [[ultra-mode]] · [[quota-router]] · [[raptor-dispatch]] · [[session-migrate]] · [[grok-bot]] · [[src-promptyx-llm-cpu]] · [[src-thewhizzai-avo]] · [[src-exm7777-grok-bot-money]] · [[daily-tool-replace]] · [[headlong]] · [[retrieval-second-brain]] · [[company-foundry]] · [[secret-gateway]] · [[flat-context]] · [[src-voxyz-writing-system]] · [[src-kaorixbt-harness-engineering]] · [[agent-operating-system]] · [[loop-graph-engineering]]

[[src-can1357-daily-tool-replace-2026-08-27]]: people who know better can replace daily-flow apps themselves. Hour tops is tweet wording. See [[daily-tool-replace]].

[[src-exm7777-grok-bot-money]] is a Grok Bot product how-to: persistent VM, computer use, one bot per workflow. Model named Grok 4.6. Pricing comparison `unverified`. See [[grok-bot]].

[[src-4ndrearossetti-openconnector]] puts credentials in a runtime, not in the prompt. Product counts `unverified`. See [[secret-gateway]].

[[src-avichawla-trueforge]] treats the harness as the token-cost knob. 2.7x is `unverified`. See [[flat-context]].

[[src-andrewng-ai-engineering-skills-map]]: harness wraps the model; autonomy dial interactive/delegated/looped; Related only (no deep fold).

[[src-voxyz-writing-system]] audits global vs project `CLAUDE.md` / `AGENTS.md` that Codex and Claude Code actually load. Keep project voice local. See [[contradictions]] C43.
