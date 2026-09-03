---
id: concept:spacexai-grok-bot-keepers
type: concept
schema: memory-v1
tags:
  - wiki
created: 2026-09-02
updated: 2026-09-02
created_by: agent
confidence: high
source:
  - wiki/sources/src-lingxi-grok-bot-engineering.md
  - wiki/sources/src-poteto-eliminate-interventions.md
  - wiki/sources/src-poteto-pstack-outer-loop.md
  - wiki/sources/src-samsokolin-browser-to-api.md
  - wiki/sources/src-yunta-tsai-quota-isolate.md
  - wiki/sources/src-xai-introducing-grok-bot.md
derived_from:
  - src-lingxi-grok-bot-engineering
  - src-poteto-eliminate-interventions
  - src-poteto-pstack-outer-loop
  - src-samsokolin-browser-to-api
  - src-yunta-tsai-quota-isolate
  - src-xai-introducing-grok-bot
  - raptor-dispatch
  - grok-bot-quota
  - work-per-cost
  - skill-as-sop
---

# SpaceXAI Grok Bot keepers

Ablation-clean principles from SpaceXAI engineer writeups. Apply the method. Do not copy their org chart. Product is LanBB; semantica is a tool.

Sources: [[src-lingxi-grok-bot-engineering]] · [[src-poteto-eliminate-interventions]] · [[src-poteto-pstack-outer-loop]] · [[src-samsokolin-browser-to-api]] · [[src-yunta-tsai-quota-isolate]] · [[src-xai-introducing-grok-bot]].

## FACT

[[src-lingxi-grok-bot-engineering]]: one domain per standing bot sharpens memory and design principles inside that lane.

[[src-lingxi-grok-bot-engineering]]: cloud agents launch with skills named and proof expected; the bot stays on the run and verifies its own result; repeating paths become repo skills.

[[src-poteto-eliminate-interventions]]: kill the same correction in order — architecture/data structure → lint/test CI → skill/rule → human review last.

[[src-samsokolin-browser-to-api]]: capture network once from a GUI/computer-use path; next time call the API. Prefer MCP/API over browserUse over computerUse.

[[src-yunta-tsai-quota-isolate]]: isolate one job in one context; file the method in the repo; stop. Do not spawn a room. Already folded on [[grok-bot-quota]].

[[src-poteto-pstack-outer-loop]]: routines farm context; outer loop chooses what the factory points at; /goal /loop /swarm (and poteto-mode when coding) own the how on cloud agents.

[[src-xai-introducing-grok-bot]]: bots have their own computer, finish work in tools, and return for approval; a chief of staff can sit above specialists.

## INFERENCE

Map domains to the existing roster: CoS (front door + ops/postmortem), Engineer (all code), Vault (wiki), Fill (leftover quota), Rutin (routine hygiene). Do not hire Jenny / Baltata / Shaoruru / Hogan / Craig / Quill clones. derived_from: src-lingxi-grok-bot-engineering, raptor-dispatch.

Daily playbook nudge runs through Morning OS / existing routines, not a new ops bot. derived_from: src-lingxi-grok-bot-engineering.

P0 means denser live steer on the cloud agent (MessageSubagent / CheckSubagent). Do not create a 5-minute or 15-minute polling routine. Those stay banned. derived_from: src-lingxi-grok-bot-engineering, grok-bot-pro-tips.

Outer loop folds into [[raptor-dispatch]]. Do not install pstack wholesale as a new bot farm. Skills do the how. derived_from: src-poteto-pstack-outer-loop, raptor-dispatch.

Last yes stays human. No auto-merge even when the source describes low-blast auto-merge. derived_from: src-lingxi-grok-bot-engineering, decisions.

## OPINION

Principles beat tweet dumps. One short hub is enough; detail lives on [[grok-bot-quota]], [[work-per-cost]], [[skill-as-sop]], and [[raptor-dispatch]].

## Check

If someone proposes a Jenny hire, a domain engineer bot clone, a 5/15-min poller, auto-merge, or a second product stream: refuse. Fold into CoS / Engineer / Vault / Fill / Rutin and existing pages.

## Related

[[raptor-dispatch]] · [[grok-bot-quota]] · [[work-per-cost]] · [[skill-as-sop]] · [[grok-bot]] · [[loop-graph-engineering]] · [[musk-algorithm]] · [[grok-bot-pro-tips]]
