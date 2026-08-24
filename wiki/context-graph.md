---
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-24
---

# Context graph

Give the model the subgraph for this decision, not the whole dump.

Source: article quoted by [[src-avid-obsidian-agent-team]].

## Claim

A 1M-token window is not a reason to fill it. The useful unit is a small set of entities, relationships, events, and prior decisions.

Vector similarity is not a causal path. "Why did Project X fail?" may need a chain across people, suppliers, and releases that chunk search never joins.

Facts need validity windows. "Dan works on Project A" and "Dan works on Project B" can both exist in a store. Only one may be current.

## Split

- Graph: what is true, and when.
- Skills / schema: how we act.

## What agents actually open

[[src-dair-agent-friendly-docs]] measured the subgraph coding agents retrieve: instruction files and working notes, not API references. Give later agents `AGENTS.md` plus the wiki pages this decision needs. Do not fill the window with classical docs. See [[agent-facing-docs]].

## Related

[[tokens-as-capital]] · [[llm-wiki]] · [[memory-engineering]] · [[agent-facing-docs]]
