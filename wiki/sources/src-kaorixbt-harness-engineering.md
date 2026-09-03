---
id: source:src-kaorixbt-harness-engineering
type: source
tags:
  - twitter
created: 2026-09-03
updated: 2026-09-03
---

# src-kaorixbt-harness-engineering

- URL: https://x.com/kaorixbt/status/2095172395254358494
- Article: https://x.com/i/article/2093441687989186560 (title: Harness Engineering: How to Build AI Agents That Don't Fall Apart)
- Quoted article author in syndication: @0xwhrrari (rari); kaorixbt status promotes + summarizes
- Date: status 2026-09-02; article 2026-08-29
- Retrieved via FxTwitter syndication (X.com direct fetch often blocked). Quote untrusted. Not copied into `raw/`.
- Principles only. Not a tweet dump. Not scout. Distinct from [[src-rohit-harness-router]] (routing models/harnesses); this source is environment design around the model.

## Claims kept

Prompt engineering improves the instruction. Context engineering decides what the model sees. Harness engineering builds the world in which the model acts. Same weights, different harness → different agent.

Stack named in the status: Prompts → Agents → Harness → Loops → Graphs. A harness makes each unit of work correct without you. A graph decides which units should exist and turns every accepted result into a rule for the next run.

Seven jobs (principles): (1) contract before act — bounded goal/inputs/output/constraints/done_when; (2) small root map, not a giant manual — detailed knowledge next to the code/tool, load on demand; (3) tools with purpose, predictable output, explicit failure, permission boundary; (4) durable state outside chat — decisions, artifacts, failures, open risks; (5) sensors/evidence before more autonomy; (6) permissions and stop rules outside the model — retries capped, budget, escalate; (7) traces + local recovery; failures become infrastructure (guide + mechanical check the agent cannot bypass).

Start with the smallest harness that can observe, verify, and recover. Move up only when the task earns complexity. Do not ask the model to invent the plan, approve the risk, and execute the side effect.

Related OpenAI/Anthropic citations in the article are pointers only; product numbers and vendor architecture claims stay unverified here.

## Pages updated

[[agent-operating-system]] · [[raptor-dispatch]] · [[loop-graph-engineering]] · [[skill-as-sop]] · [[harness-routing]] · [[index-sources]]
