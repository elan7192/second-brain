---
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-24
---

# Secret gateway

Credentials stay in a runtime. The model context does not hold them.

Source: [[src-4ndrearossetti-openconnector]].

## Rule

An agent may request an action. A gateway or injector runs it. Raw passwords and API keys stay outside the prompt.

Steve Faulkner asked for that rule on computer-use: approval, then inject into a browser field.

The quoted OpenConnector pitch applies the same rule to SaaS actions: the agent sees a catalog, the gateway talks to Gmail/Slack/Notion/Airtable, the key never enters context.

## What this tweet does not prove

Product counts are `unverified`. No paper. No repo URL in the tweet.

Faulkner asked for browser field injection. The quote is an API-action gateway. Do not treat OpenConnector as the computer-use injector. See [[contradictions]] C14.

## Related

[[harness-routing]] · [[audited-task-contract]] · [[agent-operating-system]] · [[hunt-ship-loop]]
