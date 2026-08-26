---
type: concept
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-27
---

# Work per cost

Catalog of token-save methods already in this vault. No new physics. Author-reported numbers stay labeled.

PM operational KPI 2026-08-27 is at the bottom.

## Author-reported numbers (cite the page)

- [[tokens-as-capital]] / [[src-papa-couch-compiler]]: 305,000 vs 47,000 tokens for the same task. Projected 30-day savings 54% to 81%. Author-reported, not independently audited.
- [[entropy-gate]] / [[src-hitu-entropy-engineering]]: 64 Haiku workers. Shared memory $4.12 / hallucination 0.658. Gated diffs $1.73 / 0.463. Isolation 0.492, cost blank on that row. 200-agent clip `unverified` (C3).
- [[trace]] paper: 16x fewer LLM calls than iterative per-node. Tweet 4.2x token cut `unverified`.
- [[memory-ablation]]: 71 of 104 lines never changed an answer. Author reports cutting 68%.

## Methods already in force (no extra numbers)

- [[llm-wiki]]: compile once. Do not re-retrieve raw every question.
- [[memory-engineering]]: pipeline, not a bigger window. Full-transcript replay does not scale.
- [[file-memory]]: git markdown. Vector DB only when too much to read.
- [[context-compaction]]: chat may be fuzzy. Vault must be precise. Do not dump transcripts.
- [[grok-bot-quota]]: burns fastest on Max Mode cloud agents, computerUse vision loops, long specialist transcripts reread every turn. Recurring fill on dedicated `burn`, not the PM chat.
- [[grok-bot-pro-tips]]: hourly or a few times a day. Never every 5 minutes. Recurring work to a fresh bot.
- [[quota-router]]: burn expiring OpenCode Go, then ChatGPT/Gemini, then Cursor.
- [[raptor-dispatch]]: one owner, report once, no empty acks.
- [[entropy-gate]]: isolated worktrees, structured diffs, objective gate.
- [[harness-routing]]: route by phase, not by turn. Transfer semantic state, not KV.
- [[session-migrate]]: context only. Git is truth. Do not migrate a compact blob as the vault.
- [[audited-task-contract]]: share a contract, not a transcript. Avoid reset tax.
- [[musk-algorithm]]: delete before optimize. Automate last.

## Deletes already in force (PM 2026-08-27)

- Hourly idle paused.
- No 5-minute pollers.
- Fill not on PM chat.
- No transcript dump into the vault.

## This team KPI (PM applies)

Wallet split: Grok Bot scarce vs Fill leftover. Do not mix ledgers.

- Numerator **W** = completed jobs with proof: wiki SHA, PR URL, spec path, Figma URL, or artifact path. No vibes.
- Denominator **E** = expensive Grok Bot units: cloud-agent launches + computerUse sessions. Do not invent dollar weights.
- Metric **W/E**. Report counts, not fake dollars.
- Fill Go / Plus / Gemini is leftover burn. Separate ledger.

## Related

[[tokens-as-capital]] · [[llm-wiki]] · [[memory-ablation]] · [[memory-engineering]] · [[file-memory]] · [[context-compaction]] · [[grok-bot-quota]] · [[grok-bot-pro-tips]] · [[quota-router]] · [[raptor-dispatch]] · [[entropy-gate]] · [[harness-routing]] · [[trace]] · [[musk-algorithm]] · [[session-migrate]] · [[audited-task-contract]]
