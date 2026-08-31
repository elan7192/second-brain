---
id: concept:grok-bot-quota
type: concept
schema: memory-v1
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-31
created_by: agent
confidence: high
source:
  - wiki/sources/src-benln-grok-bot-pro-tips.md
  - wiki/sources/src-yunta-tsai-quota-isolate.md
derived_from:
  - src-benln-grok-bot-pro-tips
  - src-yunta-tsai-quota-isolate
  - raptor-dispatch
---

# Grok Bot quota

Grok Bot quota burns fastest on:

1. Cursor cloud agents in Max Mode
2. computerUse screenshot/vision loops
3. Long specialist transcripts reread every turn

Sources: [[src-benln-grok-bot-pro-tips]] (tips 4, 5, 9). [[src-yunta-tsai-quota-isolate]] (lan E 好, 2026-08-31).

Also see [[quota-router]] for which provider to burn first.

## FACT

Quota burns fastest on Max Mode cloud agents, computerUse vision loops, and long specialist transcripts reread every turn. [[src-benln-grok-bot-pro-tips]].

[[src-yunta-tsai-quota-isolate]]: token burn gets a dedicated context for that task, then close when finished. Reuse means save the reflection and put it in the repo so it is repeatable.

Recurring fill does not belong on the lead chat. See [[grok-bot-pro-tips]].

## INFERENCE

Isolate one job in one context. When done, file the repeatable method in the repo (wiki or skill) and stop. Do not spawn a Grok Bot room or channel to do this. Isolation is end-the-stream, not open-a-room. derived_from: src-yunta-tsai-quota-isolate, raptor-dispatch.

The named `burn` fill bot is an existing role. Do not open a new room per task. See [[raptor-dispatch]] and [[botdirectory-scan]].

## OPINION

Leftover chat is not the store. The repo is.

## Check

If a job is done and the method is only in chat: file it into wiki or a skill, then stop. If someone asks to open a new Grok Bot room to isolate work: refuse. Use the current stream, then end it.

## Related

[[quota-router]] · [[grok-bot-pro-tips]] · [[tokens-as-capital]] · [[raptor-dispatch]] · [[work-per-cost]] · [[botdirectory-scan]] · [[src-benln-grok-bot-pro-tips]] · [[src-yunta-tsai-quota-isolate]]
