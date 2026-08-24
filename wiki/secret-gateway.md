---
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-24
---

# Secret gateway

Credentials stay in a runtime. The model context does not hold them.

Source: [[src-4ndrearossetti-openconnector]]. Also [[src-avichawla-trueforge]].

## Rule

An agent may request an action. A gateway or injector runs it. Raw passwords and API keys stay outside the prompt.

Steve Faulkner asked for that rule on computer-use: approval, then inject into a browser field.

The quoted OpenConnector pitch applies the same rule to SaaS actions: the agent sees a catalog, the gateway talks to Gmail/Slack/Notion/Airtable, the key never enters context.

[[src-avichawla-trueforge]] applies it inside a Code Mode sandbox: generated code calls `call_tool`; the harness applies stored credentials; the script never receives the key. Approvals still apply. Product is TrueForge, not OpenConnector. Do not merge them.

## What these sources do not prove

OpenConnector product counts are `unverified`. That tweet did not link a repo. Faulkner asked for browser field injection. The quote is an API-action catalog. See [[contradictions]] C14.

TrueForge 2.7x is `unverified`. Sponsored article. See C15.

## Related

[[harness-routing]] · [[audited-task-contract]] · [[agent-operating-system]] · [[hunt-ship-loop]] · [[flat-context]]
