---
id: concept:musk-algorithm
type: concept
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-29
---

# Musk Algorithm

Strict order. Best part is no part.

Source: [[src-lan-e-musk-algorithm]]. Named owner: lan E.

1. Make requirements less dumb. Named person, not a department. Only the laws of physics are absolute. Department names ("legal", "safety", "the schema") are not owners.
2. Delete the part or process. If you are not adding about 10% back, you did not delete enough.
3. Simplify and optimize only after delete. Do not optimize what should not exist.
4. Accelerate cycle time. Speed exposes hidden quality and flow problems.
5. Automate last.

Doing it backwards (automate, then simplify, then delete) wastes time.

Keep long-term vision.

## Starship examples (not new physics)

- Grid fins stay deployed.
- Interstage pushers deleted via booster gimbal.
- Autogenous pressurization instead of helium.
- Landing legs deleted in favor of tower catch.
- Raptor 3 subtracts plumbing.

## Vault pass 2026-08-28

lan E ordered this sequence on the second-brain repo. Requirements questioned against a named person. Physics of this vault: git markdown, token cost of every forced read, D1 compiler, D5 human yes.

Deleted:

- Mandatory full-index read on every query (agent folklore, not lan E).
- Mandatory `output/` ingest brief (schema author, not lan E).
- `MEMORY.md` copy of LanBB loops 1–16 (failed [[memory-ablation]]; history lives on [[hunt-harden-loop]]).
- Separate `wiki/first-principles.md` page (same order as step 1 here).
- `tools/add-frontmatter.py` (unused automation).
- "Keep `CLAUDE.md` identical to `AGENTS.md`" (contradicted D2).
- Standing "pull the GitHub clone and stay current" wiki-agent order (unnamed department).
- Home default "file a clip in inbox" (scout paused; lan E, [[assign-execute-verify]]).
- Nineteen orphan `output/ingest-brief-2026-08-24-*.md` files (no inbound wikilink; knowledge is on concept pages).
- Seventeen-section hunt-harden prose on the living page (process leftover; table + current wall remain).

Added back (~10%):

- [[index-papers]] and [[index-sources]] so catalogs still exist, opt-in.
- Origin + current LanBB source links on [[hunt-harden-loop]].
- File-back only when the next session would re-derive the answer.
- Lint as the ingest gate.
- Six ingest briefs that still have inbound wikilinks.

Not automated: no new bot, hook, or renderer. `tools/lint-wiki.py` stays a manual/CI gate.

Locked as D12 in [[decisions]] (was D9 on this branch; main already locked D9 as FTS). Live query stays D9. See C37. Ingest brief is C38.

## Vault pass 2026-08-29

lan E sent the five steps again. Requirements questioned against a named person. Physics unchanged: git markdown, token cost of every forced read, D1 compiler, D5 human yes.

Questioned and deleted:

- Full concept and people catalogs on the short [[index]] (agents walking the door, not lan E). D12 already split papers and sources.
- Home / Today merge-report dumps (merge process leftover). Timeline stays on [[log]].
- Standing `output/` ingest brief (schema author). C38 resolved: skip. Existing briefs stay.
- Dual standing gate `lint-wiki.py` then `sb validate` (lint already runs inside validate).
- `compile-claims.py --check` as a third standing command (lint already runs it).
- Mermaid dump inside [[graph]] plus the renderer write (html/svg snapshots remain).
- DeerFlow `make dev` as a Home next action (other VM, needs keys, D5).

Added back (~10%):

- Projects table on [[index]] (active work).
- Start operating pages on [[index]] and [[Home]].
- Existing historical briefs and merge reports.
- `tools/sb` so the documented `python3 tools/sb` command runs.

Accelerated: one gate (`python3 tools/sb validate`), one query command that exists on disk.

Not automated: no new bot, hook, or renderer. C17 and C18 untouched. C37 still open.

## Related

[[raptor-dispatch]] · [[src-lan-e-musk-algorithm]] · [[index]] · [[verifiable-instructions]] · [[daily-tool-replace]]
