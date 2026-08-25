---
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-25
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

## Test before you believe it

Compare a fixed pair, a fixed pair with audited state, and routed executors. If routing loses to the reset tax, keep the fixed pair.

## Related

[[audited-task-contract]] · [[entropy-gate]] · [[rohit]] · [[quota-router]] · [[raptor-dispatch]] · [[session-migrate]] · [[src-promptyx-llm-cpu]] · [[src-thewhizzai-avo]]
