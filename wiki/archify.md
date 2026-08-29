---
id: concept:archify
type: concept
schema: memory-v1
tags:
  - wiki
created: 2026-08-29
updated: 2026-08-29
created_by: agent
confidence: medium
source:
  - wiki/sources/src-voxyz-archify.md
  - https://github.com/tt-a1i/archify
derived_from:
  - src-voxyz-archify
  - skill-as-sop
  - skill-library
---

# Archify

Pinned external diagram skill. Wiki is the store. The renderer is not vendored.

Source: [[src-voxyz-archify]] ([[vox]], 2026-08-29). Upstream: https://github.com/tt-a1i/archify

## FACT

[[src-voxyz-archify]] names Archify as Vox's default system-map skill for Codex / Grok Bot.

The tweet quotes `npx skills add tt-a1i/archify -g`. This vault does not keep a global install and does not vendor the renderer tree.

GitHub API on 2026-08-29: 29431 stars. MIT. Pin: `.agents/skills/archify/pin.json`. Commit `0853a805003514776bef3593ecca091409828902`. Version string `v2.16.0-dev.0`. LICENSE in that directory is upstream MIT (tt-a1i 2026; Cocoon AI 2025).

`.agents/skills/archify/SKILL.md` is a vault-authored behavior change. It tells an agent when to fetch the pin and to follow upstream `archify/SKILL.md` after fetch. It is not documentation-only.

Tweet size 2400x1260 is caption wording. It is not a vault gate. Archify `visual-check` uses 1440x900 and 2048x1320. Do not commit a PNG that claims to satisfy 2400x1260.

## Why not vendor the runtime

#28 copied renderers, schemas, examples, and scripts into git. That mixed ingest with an upstream checkout and hid the update boundary. C47 now pins the commit and fetches on demand. Wiki compile stays. See [[skill-library]].

## Commit boundary

| Path | Kind | Commit |
| --- | --- | --- |
| `wiki/` | ingested knowledge | yes |
| `.agents/skills/archify/pin.json` | vault pin | yes |
| `.agents/skills/archify/SKILL.md` | vault behavior stub | yes |
| `.agents/skills/archify/LICENSE` | upstream MIT copy | yes |
| `.agents/skills/archify/upstream/` | checkout of the pin | no |
| `output/archify/*.json` | authored IR | local only |
| `output/archify/*.html` `*.png` receipts | generated | no |
| `output/ontology-objects.csv` | vault ontology | yes, existing product |

Update: bump `commit` in `pin.json`, run `python3 tools/fetch-archify.py --check`, then fetch. Do not copy new upstream files into git.

## INFERENCE

A checked HTML map can show the ingest and query path without replacing `python3 tools/sb ask` (D9). derived_from: src-voxyz-archify, retrieval, llm-wiki.

## OPINION

Do not copy Archify prompts into `AGENTS.md`. Do not vendor other public packs from this yes. See C47 and [[skill-as-sop]].

## Check

`python3 tools/sb ingest-check src-voxyz-archify` exits 0. `python3 tools/fetch-archify.py --check` exits 0. `git ls-files .agents/skills/archify` is only `LICENSE`, `SKILL.md`, and `pin.json`. If fetch is needed and fails: stop and name the gap. Do not invent a second diagram runtime.

## Related

[[skill-library]] · [[skill-as-sop]] · [[project-skill-stack]] · [[how-it-works]] · [[graph]] · [[llm-wiki]] · [[vox]] · [[src-voxyz-archify]]
