---
id: concept:archify
type: concept
schema: memory-v1
tags:
  - wiki
created: 2026-08-29
updated: 2026-09-04
created_by: agent
confidence: medium
source:
  - wiki/sources/src-voxyz-archify.md
  - https://github.com/tt-a1i/archify
  - wiki/sources/src-t20000622yy-egolite-design.md
derived_from:
  - src-voxyz-archify
  - skill-as-sop
  - skill-library
  - src-t20000622yy-egolite-design
---

# Archify

A project diagram skill. Agents write typed JSON. `node .agents/skills/archify/bin/archify.mjs` compiles HTML.

Source: [[src-voxyz-archify]] ([[vox]], 2026-08-29). Repo: https://github.com/tt-a1i/archify

## FACT

[[src-voxyz-archify]] names Archify as Vox's default system-map skill for Codex / Grok Bot.

The tweet quotes `npx skills add tt-a1i/archify -g`. This vault copied the skill to `.agents/skills/archify` after lan E asked to integrate the post. Global install was not used.

GitHub API on 2026-08-29: 29431 stars. MIT. README version string `v2.16.0-dev.0`. Five diagram types: architecture, workflow, sequence, dataflow, lifecycle.

Five vault map specs under `output/archify/`. Wiki markdown stays the store. JSON is the committed source. HTML is derived and gitignored, same class as a local compile. Rebuild with `python3 tools/deliver-archify.py`. See [[vault-ontology]] and [[graph]].

| Type | Spec |
| --- | --- |
| Architecture | `vault-architecture.json` |
| Workflow | `vault-ingest.workflow.json` |
| Sequence | `vault-query.sequence.json` |
| Data flow | `vault-claims.dataflow.json` |
| Lifecycle | `vault-claim.lifecycle.json` |

Tweet-requested PNG: `output/archify/vault-architecture-2400x1260.png`. Search and upstream/downstream tracing are viewer features in locally delivered HTML.

[[src-t20000622yy-egolite-design]]: author method uses ego lite browser passes over reference sites, then generates UI; names archify/openpi/skillroster as example repos. Pointer [[src-otterpal-egolite-crawl-pointer]] is crawl-speed testimony only.

## INFERENCE

A checked HTML map can show the ingest and query path without replacing `python3 tools/sb ask` (D9). derived_from: src-voxyz-archify, retrieval, llm-wiki.

## OPINION

Keep the skill local. Do not copy Archify prompts into `AGENTS.md`. Do not vendor other public packs from this yes. See C47 and [[skill-as-sop]].

## Check

`python3 tools/sb ingest-check src-voxyz-archify` exits 0. For each map, `node .agents/skills/archify/bin/archify.mjs validate <type> output/archify/<spec>.json --quality showcase --json` reports 0 composition errors. `python3 tools/deliver-archify.py` writes local HTML. If the skill is missing: stop and name the gap. Do not invent a second diagram runtime. Do not commit HTML.

## Related

[[skill-library]] · [[skill-as-sop]] · [[project-skill-stack]] · [[how-it-works]] · [[graph]] · [[llm-wiki]] · [[vox]] · [[src-voxyz-archify]]

· [[src-t20000622yy-egolite-design]] · [[src-otterpal-egolite-crawl-pointer]]
