---
id: concept:skill-library
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-29
---

# Skill library

A shared catalog of agent skills the whole company can create, find, and reuse.

Sources: [[src-johnsjawn-skill-library]] ([[hurley]], 2026-08-21), [[src-mukul975-cybersecurity-skills]] ([[mahipal-jangra]], repo created 2026-02-25), [[src-skill-pack-list]] (2026-08-23), and [[src-voxyz-archify]] (2026-08-29).

## Claims that landed

1. Target: a living library. Named failure: a GitHub folder only 10% of the company knows how to use. The 10% figure is author-stated, unverified.
2. Operations named: create, share, collaborate, discover, understand usage. Organize into databases by team or use case. Use across any of your agents.
3. Creating a skill should be as easy as asking from the context of work.
4. Top skills and skill creators should rise to the top.
5. Stated product goal: Notion as the home for collective AI skills.

## What the demo showed

Notion Library, Skills tab. Skills are pages. Columns: Name, Description, Database, Created by, # Uses, Enable for me. Databases on screen: Skills, EPD Skills, Marketing Skills, Docs. Skill-page banner: "This page is being used as an AI skill." Overflow: Use automatically, Download for local agents. Agents tab is a gallery.

Spoken: an agent built Ivan Bot Skill from Ivan's feedback in Notion and Slack. That generation is not on camera.

## What the demo did not show

- Skill instructions changing after a use. Tweet line about a deal review skill getting better each time a sales rep uses it is unverified. See [[contradictions]] C21.
- A downloaded skill running in a local agent. "Across any of your agents" is spoken plus a menu item. Execution is unverified.
- A research skill rebuilt 50 times. Tweet number, no method. unverified.

## GitHub catalog form

[[src-mukul975-cybersecurity-skills]] is the GitHub-folder form [[hurley]] named as a failure. README headline: 817 skills, 29 domains, six framework maps, agentskills.io. GitHub API on 2026-08-23: 30758 stars, 3663 forks.

Claimed load path: scan frontmatter at about 30 tokens each, then load 500-2000 tokens for a chosen skill. That is progressive disclosure, author-stated. See [[tokens-as-capital]] and [[context-graph]].

README says the pack includes offensive and dual-use techniques. This vault compiled the catalog pitch only. Skill bodies, scripts, and workflows stay out. Do not vendor or execute the pack.

Counts inside that README do not add up. See [[contradictions]] C23. The repo name uses Anthropic. The README denies affiliation. See C22.

## Five more GitHub packs

Checked 2026-08-23. Catalog only. See [[src-skill-pack-list]] and [[skill-as-sop]].

| Repo | What the README actually says | API stars that day |
| --- | --- | --- |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Official Vercel pack. `react-best-practices` 40+ rules. `web-design-guidelines` 100+ rules. Also writing 80+, React Native 16. | 30364 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 163 scientific skills on the badge. Same file also says 161. Paste said 148. | 34179 |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | Headline 364. Later 345. README still says 5,200+ stars. Paste said 223. | 24841 |
| [psenger/ai-agent-skills](https://github.com/psenger/ai-agent-skills) | Named skills in the paste are present, plus others. | 9 |
| [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit) | README table: 43 skill rows. Named README / C4 / Mermaid / schema / deps / handoff skills are present. | 2378 |

Stale counts: [[contradictions]] C24. Scientific skill bodies were not copied.

## Relation to this vault

This vault compiles skill rules into pages and does not vendor marketplace dumps. That is [[anti-slop]]. Do not reopen D7 (Obsidian is the IDE).

[[src-voxyz-archify]] is a named exception: lan E asked to integrate one diagram skill. Copy lives at `.agents/skills/archify`. See [[archify]] and C47.

Discovery instead of rebuild is the same bet as [[tokens-as-capital]]. The compiler store stays `wiki/`. See [[contradictions]] C20.

## Related

[[llm-wiki]] · [[anti-slop]] · [[tokens-as-capital]] · [[context-graph]] · [[skill-as-sop]] · [[archify]] · [[hurley]] · [[mahipal-jangra]]
