---
id: concept:skill-as-sop
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-09-03
---

# Skill as SOP

A skill is a compiled SOP for a workflow that already failed once.

Source: [[src-skill-pack-list]].

## Claims that landed

1. The job is the repeated process, not extra generated code.
2. Named processes in the paste: review UI, check an API, plan a database, organize docs, review architecture, hand off a task.
3. A stable SOP is supposed to stop the agent from treating a known failure as new and burning tokens. That is the same bet as [[tokens-as-capital]].
4. The human already turned one Smoke problem into Hook + SOP, then asked whether to make their own skill. The script is not in `raw/`.

## Cloud agent → skill

[[src-lingxi-grok-bot-engineering]]: after a clean cloud-agent path, package what it learned as a repo skill (when, inputs, sequence, validation, proof). Agent verifies its own result before the skill is trusted.

[[src-poteto-eliminate-interventions]]: if the same correction happens twice, prefer architecture or CI over adding another skill line. Skill/rule is step 3; human review is last.

[[src-adiix-grok-bot-org]]: grow from mistakes — turn a repeatable failure into a permanent rule in the narrowest place. Earn Skills: real task → correction → Skill → test → Routine. Same correction three times manually is unpaid QA.

[[src-kaorixbt-harness-engineering]]: failures become rules. Encode the important rule twice — guide the agent can understand, then a mechanical check it cannot bypass. Past failure → permanent harness improvement; the next agent does not need to remember the incident.

## What to do in this vault

Compile the SOP into `wiki/` or `AGENTS.md` with the three-part shape on [[verifiable-instructions]]. Do not vendor a public marketplace to get that SOP. That is [[anti-slop]].

[[src-voxyz-archify]] is one local SOP lan E asked to install: [[archify]] at `.agents/skills/archify`. Do not copy its prompts into `AGENTS.md`. See C47.

If the next source is the Smoke script, ingest it. Until then do not invent the method.

## Related

[[skill-library]] · [[tokens-as-capital]] · [[verifiable-instructions]] · [[audited-task-contract]] · [[archify]] · [[spacexai-grok-bot-keepers]] · [[skill-improver]] · [[src-adiix-grok-bot-org]] · [[src-kaorixbt-harness-engineering]] · [[loop-graph-engineering]]
