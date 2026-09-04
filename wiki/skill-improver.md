---
id: concept:skill-improver
type: concept
schema: memory-v1
tags:
  - wiki
created: 2026-08-30
updated: 2026-09-04
created_by: agent
confidence: medium
source:
  - wiki/sources/src-voxyz-skill-improver.md
derived_from:
  - src-voxyz-skill-improver
  - verifiable-instructions
  - deterministic-core
  - memory-ablation
---

# Skill improver

Instruction files rot when every correction becomes a new Never line.

Source: [[src-voxyz-skill-improver]] ([[vox]], 2026-08-29). Caption only. Video not fetched. Pointer: optimize skill writing with mattpocock [writing-for-agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md); do not install whole `mattpocock/skills` ([[src-sukiea-writing-for-agents]]).

## FACT

[[src-voxyz-skill-improver]] says a Skill that appends a rule on every correction grows, then conflicts, then gets worse.

The worker Skill does not edit itself. A separate improver reads trusted human feedback that includes why, proposes one small focused change as a PR, and a human merges it.

Three gates named in the tweet: trusted feedback plus reason; principles, not one-off rigid rules; the same eval, and no merge if the score drops.

A wish still needs a behavior, a check, and a failure path. See [[verifiable-instructions]].

Chat dumps are not this file. See [[context-compaction]]. Compiled facts stay in [[file-memory]] and [[portable-memory]]. A line stays only if it changes an answer. See [[memory-ablation]].

## INFERENCE

This vault maps that loop onto existing jobs. Worker ingest/ask/compile leaves `AGENTS.md` and instruction wiki pages alone. A later improver pass may fold one principle as a PR. `python3 tools/sb validate` runs the instruction-budget gate. `python3 tools/sb eval` is the same benchmark. derived_from: src-voxyz-skill-improver, verifiable-instructions, deterministic-core.

Do not add an Improver bot. See [[botdirectory-scan]].

## OPINION

Park a one-off Never. Fold a principle or leave the file.

## Check

`python3 tools/sb validate` exits 0. That run includes the instruction-budget gate. The append-only fixture in `eval/instruction-budget/` must fail. A fold of an existing principle may pass. After a retrieve or ingest change, `python3 tools/sb eval` exits 0. If feedback has no why: stop. If eval is worse: do not merge.

## Related

[[verifiable-instructions]] · [[context-compaction]] · [[file-memory]] · [[portable-memory]] · [[memory-ablation]] · [[deterministic-core]] · [[src-voxyz-skill-improver]] · [[src-sukiea-writing-for-agents]]
