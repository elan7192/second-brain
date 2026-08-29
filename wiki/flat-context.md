---
id: concept:flat-context
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-24
---

# Flat context

Load what the run needs. Offload the rest.

Source: [[src-avichawla-trueforge]].

## Cost lever

A tool result that stays in the conversation is processed again on every later call. Prompt caching discounts a stable prefix. It does not remove those tokens from the window.

Tool schemas occupy the prompt before any work starts. A larger context window does not change the per-call bill.

## Strategies named

1. **Deferred load.** Skills start as name and description (`SKILL.md` body read when relevant). MCP tools default to server name and description. Then `list_tools`, `get_tool_info`, `get_tool_output_schema`, `call_tool`. Unused tools never enter the prompt.
2. **Offload.** Large tool responses go to a sandbox file. Context keeps a preview and a path. Parallel batches offload the largest first until the batch fits.
3. **Subagents.** Intermediate records stay in child context. The root sees summaries.
4. **Code Mode.** A script calls tools and joins data. Only the script output enters context. Credentials still stay in the harness. See [[secret-gateway]].

Compaction past a default 50,000-token threshold replaces older messages with a structured summary (intent, decisions, files, errors, next steps). Full event history stays on the server.

## What this article does not prove

2.7x and the Enterprise-Bench token table are `unverified`. Sponsored. No paper. X figures unread. See [[contradictions]] C41.

## Related

[[harness-routing]] · [[secret-gateway]] · [[entropy-gate]] · [[tokens-as-capital]] · [[src-thewhizzai-avo]]
