---
id: concept:grok-bot-quota
type: concept
schema: memory-v1
tags:
  - wiki
created: 2026-08-27
updated: 2026-09-04
created_by: agent
confidence: high
source:
  - wiki/sources/src-benln-grok-bot-pro-tips.md
  - wiki/sources/src-yunta-tsai-quota-isolate.md
  - wiki/sources/src-samsokolin-browser-to-api.md
  - wiki/sources/src-lingxi-grok-bot-engineering.md
  - wiki/sources/src-adiix-grok-bot-org.md
  - wiki/sources/src-atenov-free-for-dev.md
  - wiki/sources/src-poteto-routine-frequency.md
  - wiki/sources/src-kloss-routine-audit.md
  - wiki/sources/src-ericzakariasson-webhook-wake.md
derived_from:
  - src-benln-grok-bot-pro-tips
  - src-yunta-tsai-quota-isolate
  - src-samsokolin-browser-to-api
  - src-lingxi-grok-bot-engineering
  - src-adiix-grok-bot-org
  - src-atenov-free-for-dev
  - raptor-dispatch
  - src-poteto-routine-frequency
  - src-kloss-routine-audit
  - src-ericzakariasson-webhook-wake
---

# Grok Bot quota

Grok Bot quota burns fastest on:

1. Cursor cloud agents in Max Mode
2. computerUse screenshot/vision loops
3. Long specialist transcripts reread every turn

Sources: [[src-benln-grok-bot-pro-tips]] (tips 4, 5, 9). [[src-yunta-tsai-quota-isolate]] (lan E 好, 2026-08-31). [[src-samsokolin-browser-to-api]]. Hub: [[spacexai-grok-bot-keepers]].

Also see [[quota-router]] for which provider to burn first.

## FACT

Quota burns fastest on Max Mode cloud agents, computerUse vision loops, and long specialist transcripts reread every turn. [[src-benln-grok-bot-pro-tips]].

[[src-yunta-tsai-quota-isolate]]: token burn gets a dedicated context for that task, then close when finished. Reuse means save the reflection and put it in the repo so it is repeatable.

Recurring fill does not belong on the lead chat. See [[grok-bot-pro-tips]].

[[src-samsokolin-browser-to-api]]: repeating GUI clicks burns tokens. Capture network once; next run hit the API. Prefer MCP/API over browserUse over computerUse.

[[src-adiix-grok-bot-org]]: constant polling, sync-everything, bad retries, and too many Bots burn quota and can slow the system. Prefer event triggers; quiet success.

[[src-atenov-free-for-dev]] · [[src-poteto-routine-frequency]] · [[src-kloss-routine-audit]] · [[src-ericzakariasson-webhook-wake]]: free-for-dev directory is a light Fill/lookup pointer. AI Compute Australia promo stays unverified.


[[src-poteto-routine-frequency]]: avoid over-dense scheduled routines (15 min ≈ 96–100 runs/day). Hourly or a few times a day is usually enough. Long chats make routines expensive — put recurring work on a fresh bot; keep CoS/main for steer.

[[src-kloss-routine-audit]]: audit checklist — 15-min routines, duplicate routines across bots, “inactive” bots whose routines still fire, long main-chat routines that re-read the whole thread.

[[src-ericzakariasson-webhook-wake]]: routines can wake from a webhook (WhatsApp, Notion change, sensor, GitHub Action, error-rate spike). Prefer event wake over dense polls.

[[src-poteto-routine-frequency]]: avoid scheduled routines that run too frequently. A 15-min routine is ~96–100 runs/day; hourly or a few times a day is usually enough. Long chats make attached routines expensive — put recurring work on a fresh bot; keep CoS for steer.

[[src-kloss-routine-audit]]: audit checklist — 15-min schedules, duplicate routines across bots, idle intent that does not stop routines, long CoS chat re-read by attached routines, untagged group replies, CoS multi-confirm, whole-skill rereads on eval, looping tasks in chat instead of a one-shot script.

[[src-ericzakariasson-webhook-wake]]: routines can wake from a webhook (WhatsApp, Notion, sensor, GitHub Action, error spike). Prefer event wake over dense scheduled polls.

## INFERENCE

Isolate one job in one context. When done, file the repeatable method in the repo (wiki or skill) and stop. Do not spawn a Grok Bot room or channel to do this. Isolation is end-the-stream, not open-a-room. derived_from: src-yunta-tsai-quota-isolate, raptor-dispatch.

The named `burn` fill bot is an existing role. Do not open a new room per task. See [[raptor-dispatch]] and [[botdirectory-scan]].

Cloud agent proof loop and domain map live on [[spacexai-grok-bot-keepers]]. derived_from: src-lingxi-grok-bot-engineering.

Webhook wake beats a 5/15-min poller for the same job. Still no standing dense pollers. derived_from: src-ericzakariasson-webhook-wake, src-adiix-grok-bot-org, grok-bot-pro-tips.

## OPINION

Leftover chat is not the store. The repo is.

## Check

If a job is done and the method is only in chat: file it into wiki or a skill, then stop. If someone asks to open a new Grok Bot room to isolate work: refuse. Use the current stream, then end it.

## Related

[[quota-router]] · [[grok-bot-pro-tips]] · [[tokens-as-capital]] · [[raptor-dispatch]] · [[work-per-cost]] · [[botdirectory-scan]] · [[spacexai-grok-bot-keepers]] · [[src-benln-grok-bot-pro-tips]] · [[src-yunta-tsai-quota-isolate]] · [[src-samsokolin-browser-to-api]] · [[src-adiix-grok-bot-org]] · [[src-atenov-free-for-dev]]
