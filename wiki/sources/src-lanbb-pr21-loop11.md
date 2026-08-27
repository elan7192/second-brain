---
type: source
tags:
  - project
created: 2026-08-27
updated: 2026-08-27
---

# src-lanbb-pr21-loop11

- PR: https://github.com/elan7192/LanBB/pull/21 MERGED
- Merge SHA: `484fbbeb64ae450b1fa5f1a56ebda5b24e22c070`
- Wall SHA: `3afb11b`
- Date: 2026-08-27
- Via PM + PR body. Not a chat dump. Not copied into `raw/`.

## Claims kept

Loop11 hunted v10-hardened. Fill live 0/116. Score GET HTTP 200. Default-deny 403. Report at 0/N.

v10 applied. Wall raised to v11-hardened. Next hunt uses v11.

Harden named (defense): Authorization/Origin/Referer closed on score path. Leftover continue-code/login/search/Baskets/nested SPA HTTP closed.

Apply constraints kept: no juice EROFS, tmpfs `/tmp` only, burst>=1, exact GET `/api/Challenges/` stays open for n/N.

See [[hunt-harden-loop]].

## Pages updated

[[hunt-harden-loop]] · [[lanbb]]
