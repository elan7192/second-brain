---
id: concept:spacexai-grok-bot-keepers
type: concept
schema: memory-v1
tags:
  - wiki
created: 2026-09-02
updated: 2026-09-05
created_by: agent
confidence: high
source:
  - wiki/sources/src-iamtonyzhu-grok-bot-design-philosophy.md
  - wiki/sources/src-clorissignal-agent-eval-framework.md
  - wiki/sources/src-lingxi-grok-bot-engineering.md
  - wiki/sources/src-poteto-eliminate-interventions.md
  - wiki/sources/src-poteto-pstack-outer-loop.md
  - wiki/sources/src-samsokolin-browser-to-api.md
  - wiki/sources/src-yunta-tsai-quota-isolate.md
  - wiki/sources/src-xai-introducing-grok-bot.md
  - wiki/sources/src-adiix-grok-bot-org.md
  - wiki/sources/src-poteto-routine-frequency.md
  - wiki/sources/src-ericzakariasson-webhook-wake.md
  - wiki/sources/src-petergyang-agent-privacy.md
  - wiki/sources/src-cbdoge-designing-grok-bot-pointer.md
  - wiki/sources/src-av1dlive-awesome-grok-bot-pointer.md
  - wiki/sources/src-godofprompt-10-prompts-pointer.md
  - wiki/sources/src-petergyang-cloud-login-unease-pointer.md
  - wiki/sources/src-kloss-routine-audit.md
derived_from:
  - src-lingxi-grok-bot-engineering
  - src-poteto-eliminate-interventions
  - src-poteto-pstack-outer-loop
  - src-samsokolin-browser-to-api
  - src-yunta-tsai-quota-isolate
  - src-xai-introducing-grok-bot
  - src-adiix-grok-bot-org
  - raptor-dispatch
  - grok-bot-quota
  - work-per-cost
  - skill-as-sop
  - src-poteto-routine-frequency
  - src-ericzakariasson-webhook-wake
  - src-petergyang-agent-privacy
  - src-kloss-routine-audit
---

# SpaceXAI Grok Bot keepers

Ablation-clean principles from SpaceXAI engineer writeups. Apply the method. Do not copy their org chart. Product is LanBB; semantica is a tool.

Sources: [[src-lingxi-grok-bot-engineering]] · [[src-poteto-eliminate-interventions]] · [[src-poteto-pstack-outer-loop]] · [[src-samsokolin-browser-to-api]] · [[src-yunta-tsai-quota-isolate]] · [[src-xai-introducing-grok-bot]] · [[src-adiix-grok-bot-org]] · [[src-poteto-routine-frequency]] · [[src-ericzakariasson-webhook-wake]] · [[src-petergyang-agent-privacy]] · [[src-cbdoge-designing-grok-bot-pointer]] · [[x-misses-audit-2026-09-04]].

## FACT

[[src-lingxi-grok-bot-engineering]]: one domain per standing bot sharpens memory and design principles inside that lane.

[[src-lingxi-grok-bot-engineering]]: cloud agents launch with skills named and proof expected; the bot stays on the run and verifies its own result; repeating paths become repo skills.

[[src-poteto-eliminate-interventions]]: kill the same correction in order — architecture/data structure → lint/test CI → skill/rule → human review last.

[[src-samsokolin-browser-to-api]]: capture network once from a GUI/computer-use path; next time call the API. Prefer MCP/API over browserUse over computerUse.

[[src-yunta-tsai-quota-isolate]]: isolate one job in one context; file the method in the repo; stop. Do not spawn a room. Already folded on [[grok-bot-quota]].

[[src-poteto-pstack-outer-loop]]: routines farm context; outer loop chooses what the factory points at; /goal /loop /swarm (and poteto-mode when coding) own the how on cloud agents.

[[src-xai-introducing-grok-bot]]: bots have their own computer, finish work in tools, and return for approval; a chief of staff can sit above specialists.

[[src-adiix-grok-bot-org]]: Chief routes only (triage → delegate → watch → collect → escalate). Hire by bottleneck. Bot contract (job/sources/judgment/output/forbidden). Grow rules from repeatable mistakes. Shared box computer (own screen ≠ security boundary). `/workspace` as artifact bus. Three gates: source → evidence → action. Human only for money / publish / delete / irreversible. Ban constant polling, bad retries, too-many-bots.



[[src-poteto-routine-frequency]] / [[src-kloss-routine-audit]]: dense schedules and long-chat routines burn quota; recurring work on fresh bots. Detail on [[grok-bot-quota]].

[[src-ericzakariasson-webhook-wake]]: webhook triggers wake bots from outside chat — event over poll.

[[src-petergyang-agent-privacy]]: compare agent privacy policies; treat cloud-computer login/2FA as high risk; audit third-party Google apps. Pointer: [[src-petergyang-cloud-login-unease-pointer]].

[[src-cbdoge-designing-grok-bot-pointer]]: official designing-with-always-on-bot note (x.ai/news) — pointer only.
## INFERENCE

Map domains to the existing roster: CoS (front door + ops/postmortem), Engineer (all code), Vault (wiki), Fill (leftover quota), Rutin (routine hygiene). Do not hire Jenny / Baltata / Shaoruru / Hogan / Craig / Quill clones. derived_from: src-lingxi-grok-bot-engineering, raptor-dispatch.

Daily playbook nudge runs through Morning OS / existing routines, not a new ops bot. derived_from: src-lingxi-grok-bot-engineering.

P0 means denser live steer on the cloud agent (MessageSubagent / CheckSubagent). Do not create a 5-minute or 15-minute polling routine. Those stay banned. derived_from: src-lingxi-grok-bot-engineering, grok-bot-pro-tips.

Outer loop folds into [[raptor-dispatch]]. Do not install pstack wholesale as a new bot farm. Skills do the how. derived_from: src-poteto-pstack-outer-loop, raptor-dispatch.

Last yes stays human. No auto-merge even when the source describes low-blast auto-merge. Human gate matches AdiiX money/publish/delete/irreversible list. derived_from: src-lingxi-grok-bot-engineering, src-adiix-grok-bot-org, decisions.

Shared machine + `/workspace` bus: hand off files, not chat walls. Do not treat Bot identity as isolation. derived_from: src-adiix-grok-bot-org.

Privacy: cloud VM login and 2FA are blast-radius decisions. Prefer connectors/API with approval gates over typing secrets into computerUse. derived_from: src-petergyang-agent-privacy, src-samsokolin-browser-to-api.

## OPINION

Principles beat tweet dumps. One short hub is enough; detail lives on [[grok-bot-quota]], [[work-per-cost]], [[skill-as-sop]], and [[raptor-dispatch]].

## Check

If someone proposes a Jenny hire, a domain engineer bot clone, a 5/15-min poller, auto-merge, or a second product stream: refuse. Fold into CoS / Engineer / Vault / Fill / Rutin and existing pages.


## FACT (eval gate)

[[src-clorissignal-agent-eval-framework]] (miles_mazy share of @ClorisSignal): a running Agent is not a live Agent. Eval proves go-live. Author-reported OpenAI/Anthropic eval framing stays unverified without primary docs. Maps to this desk's proof loop: named skills + proof before done.


## FACT (design primitives)

[[src-iamtonyzhu-grok-bot-design-philosophy]] (Tony / x.ai Designing Grok Bot): persistent Bots; five surface primitives Bots/Chats/Prompts/Tools/Artifacts; roster not chat-history. Near [[src-cbdoge-designing-grok-bot-pointer]].

## Related

[[src-clorissignal-agent-eval-framework]]


Skip pointer (not keepers): [[src-ritonchain-regime-trading-skip]] — regime trading desk hype.
Skip pointer (not keepers): [[src-amitiitbhu-llm-papers-skip]] — generic LLM 101 paper list.
Skip pointer (not keepers): [[src-0xkvro-quant-sample-size-skip]] — quant sample-size / OOS pop science.

Batch hub: [[x-bookmark-sync-2026-09-05]] (CoS AMENDED 2026-09-05).
Skip pointer (not keepers): [[src-skip-l1vsun-twosigma-tease]] — Two Sigma tease hype/incomplete.
Skip pointer (not keepers): [[src-skip-preserver-7books]] — 7-books engagement bait.
Skip pointer (not keepers): [[src-skip-greg-astra-prompts]] — Astra prompts listicle.
Skip pointer (not keepers): [[src-anirudh-lingxi-amplify-skip]] — SpaceXAI specialists amplify (already; NOT 入vault).
Skip pointer (not keepers): [[src-skip-nrol-future-predict]] — future-predict.
Skip pointer (not keepers): [[src-skip-12wk-cyber-roadmap]] — 12wk cyber roadmap.
Skip pointer (not keepers): [[src-skip-webenstein-cyber-path]] — cyber path.

[[raptor-dispatch]] · [[grok-bot-quota]] · [[work-per-cost]] · [[skill-as-sop]] · [[grok-bot]] · [[loop-graph-engineering]] · [[musk-algorithm]] · [[grok-bot-pro-tips]] · [[graph-node-ablation]] · [[src-adiix-grok-bot-org]]
