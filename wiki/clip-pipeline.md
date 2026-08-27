---
type: concept
tags:
  - wiki
created: 2026-08-25
updated: 2026-08-27
---

# Clip pipeline

Work from captions and metadata. Do not rip copyrighted full films.

Source: [[src-play-methods-2026-08-25]] (`/workspace/play-until-2pm/METHODS.md`). lan E yes 2026-08-27: captions first. See [[daily-tool-replace-vault-2026-08-27]].

D5 is locked: the vault does not post, pay, or send. See [[hunt-ship-loop]].

## Sequence

1. Compile from caption and metadata.
2. Fetch video or frames only when a kept claim depends on the picture.
3. If frames are used, name that claim on the source page.
4. Do not dump clip file bodies.

Check: source page has caption or metadata. Frame use is named. `python3 tools/lint-wiki.py` still exits 0.
If the text already holds the claim: leave the video unfetched.

## Related

[[hunt-ship-loop]] · [[daily-tool-replace]] · [[grok-bot-quota]]

[[src-can1357-daily-tool-replace-2026-08-27]] 6.25s git-UI clip used frames because the UI layout was not in the caption. File body not dumped.
