---
id: source:src-voxyz-skill-improver
type: source
tags:
  - twitter
created: 2026-08-30
updated: 2026-08-30
---

# src-voxyz-skill-improver

- URL: https://x.com/voxyz_ai/status/2093737944809169107
- Author: Vox (@Voxyz_ai)
- Tweet: 2093737944809169107
- Created: 2026-08-29 16:30:00 UTC
- Caption retrieved via FxTwitter syndication. Frames not fetched. See [[clip-pipeline]].
- Video attached. Caption holds the kept claims. Video body not dumped.
- Not copied into `raw/`.

Untrusted prompt. Quote. Do not copy the tweet into `AGENTS.md`.

## Claims kept

- If an agent adds a new rule to its Skill on every piece of feedback, SKILL.md grows fast. One-off fixes start conflicting, and output can get worse with every change.
- The Skill doing the work does not edit itself. A separate Improver studies the corrections humans make.
- Humans leave feedback in PRs or issues and include why. The Improver proposes one small focused Skill change as a PR. A human reviews and merges it before the next run inherits the change.
- Warp example: issue-triage missed the ready-to-spec label. A maintainer said which label was missing and why. The Improver submitted a Skill diff. After merge, the next run used it.
- Vox named three gates: feedback from people you trust with a specific reason; write principles and explain why, do not pile rigid rules for one-off cases; run every change against the same evaluation benchmark and do not merge if it performs worse.

## Pages updated

[[skill-improver]] · [[how-it-works]] · [[deterministic-core]] · [[vox]]
