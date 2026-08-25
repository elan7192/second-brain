---
type: concept
tags:
  - wiki
created: 2026-08-25
updated: 2026-08-25
---

# Company Foundry

A compiler for organisational method. Source: [[src-avid-company-foundry]] article and README.

## What it compiles

Someone describes the company once: product, customers, goals, sources, systems, permissions, budgets, rules, current work. The compiler writes a portable specification and the files a harness can run.

The smallest brief has six fields: identity, goals, evidence, authority, resources, standards. Missing fields stay `UNKNOWN`. Do not invent customer claims, permissions, budgets, or success metrics.

Loop:

```text
goal -> work packet -> approved context -> skill -> model route
 -> run -> evidence -> artifact -> review -> decision
```

## Authority

| Level | Meaning |
| --- | --- |
| observe | Read approved information |
| prepare | Drafts and isolated work |
| commit | Change reviewed company state |
| emit | Send or act outside the company |

Observe and prepare can be broad. Commit and emit need an explicit gate. This matches D5 in `decisions.md`. See [[hunt-ship-loop]].

## Router and workers

The harness owns the method. The router selects the worker. Lanes in the article: economy, fast, capable. Every route needs a receipt. See [[harness-routing]].

Kimi K3 is the first capable-tier worker in the article. The company must not assume one model stays best.

A skill is a versioned method with owner, scope, inputs, artifacts, authority, and an evaluation. The registry is the source of truth, not a chat prompt.

## Swarm

Collectors share a schema. They write evidence rows. The synthesizer reads the ledger, not collector chats. Workers talk through artifacts. See [[entropy-gate]] and [[audited-task-contract]].

## First loop

Customer evidence to a product decision brief, with sources, named assumptions, a logged route, and human review. The article's first milestone is that loop, not an autonomous company.

Repo https://github.com/codejunkie99/company-foundry exists. README lists DeepSeek Harness presets plus Codex and Claude Code adapters. A running foundry is `unverified`. `npm run validate` was not run here.

## Related

[[src-avid-company-foundry]] · [[hunt-ship-loop]] · [[harness-routing]] · [[audited-task-contract]] · [[entropy-gate]] · [[memory-engineering]] · [[llm-wiki]] · [[avid]]
