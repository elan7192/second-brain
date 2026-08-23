---
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-23
---

# Skill library

A shared catalog of agent skills the whole company can create, find, and reuse.

Sources: [[src-johnsjawn-skill-library]] ([[hurley]], 2026-08-21) and [[src-mukul975-cybersecurity-skills]] ([[mahipal-jangra]], repo created 2026-02-25).

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

- Skill instructions changing after a use. Tweet line about a deal review skill getting better each time a sales rep uses it is unverified. See [[contradictions]] C9.
- A downloaded skill running in a local agent. "Across any of your agents" is spoken plus a menu item. Execution is unverified.
- A research skill rebuilt 50 times. Tweet number, no method. unverified.

## GitHub catalog form

[[src-mukul975-cybersecurity-skills]] is the GitHub-folder form [[hurley]] named as a failure. README headline: 817 skills, 29 domains, six framework maps, agentskills.io. GitHub API on 2026-08-23: 30758 stars, 3663 forks.

Claimed load path: scan frontmatter at about 30 tokens each, then load 500-2000 tokens for a chosen skill. That is progressive disclosure, author-stated. See [[tokens-as-capital]] and [[context-graph]].

README says the pack includes offensive and dual-use techniques. This vault compiled the catalog pitch only. Skill bodies, scripts, and workflows stay out. Do not vendor or execute the pack.

Counts inside that README do not add up. See [[contradictions]] C11. The repo name uses Anthropic. The README denies affiliation. See C10.

## Relation to this vault

This vault compiles skill rules into pages and does not vendor skill repos. That is [[anti-slop]] and D7 in `decisions.md`. Do not reopen D7.

Discovery instead of rebuild is the same bet as [[tokens-as-capital]]. The compiler store stays `wiki/`. See [[contradictions]] C8.

## Related

[[llm-wiki]] · [[anti-slop]] · [[tokens-as-capital]] · [[context-graph]] · [[hurley]] · [[mahipal-jangra]]
