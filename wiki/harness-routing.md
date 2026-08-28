---
id: concept:harness-routing
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-28
---

# Harness routing

A model and a harness are different knobs.

Source: [[src-rohit-harness-router]].

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

## Test before you believe it

Compare a fixed pair, a fixed pair with audited state, and routed executors. If routing loses to the reset tax, keep the fixed pair.

## Related

Identity `hour` 1h local Ollama trial ended 2026-08-26T02:07Z (operator yes). Nested Docker overlay failed on this VM. Tests did not run. Do not restart without a new operator yes. Not the wiki runtime. See C16.

[[audited-task-contract]] · [[entropy-gate]] · [[rohit]] · [[quota-router]] · [[raptor-dispatch]] · [[session-migrate]] · [[grok-bot]] · [[src-promptyx-llm-cpu]] · [[src-thewhizzai-avo]] · [[src-exm7777-grok-bot-money]] · [[daily-tool-replace]] · [[headlong]] · [[retrieval-second-brain]] · [[company-foundry]]

[[src-can1357-daily-tool-replace-2026-08-27]]: people who know better can replace daily-flow apps themselves. Hour tops is tweet wording. See [[daily-tool-replace]].

[[src-exm7777-grok-bot-money]] is a Grok Bot product how-to: persistent VM, computer use, one bot per workflow. Model named Grok 4.6. Pricing comparison `unverified`. See [[grok-bot]].
