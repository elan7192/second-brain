---
id: source:src-lanbb-pr22-loop12
type: source
tags:
  - project
created: 2026-08-27
updated: 2026-08-27
---

# src-lanbb-pr22-loop12

- PR: https://github.com/elan7192/LanBB/pull/22 MERGED
- Merge SHA: `c201b5608eb82ac8a0b047d7634c9ec19257b485`
- Wall SHA: `e62fa4d`
- Date: 2026-08-27
- Via PM + PR body. Not a chat dump. Not copied into `raw/`.

## Claims kept

Loop12 hunted v11-hardened. Fill live 0/116. Score GET HTTP 200. Default-deny 403. Report at 0/N.

v11 compose edge mem 4m / pids 4 FAILED (daemon min 6MB). Live floor mem 6m pids 6. v12 bakes `mem>=6m` and `pids>=6`. Do not drop below.

Wall raised to v12-hardened. Next hunt uses v12.

Harden named (defense): extra hop/auth headers closed on score path. Leftover HTTP closed: hacking-instructor, juicy-nft, continue-code-xss, products-queries. Broader WAF/static deny and CSP/Permissions-Policy. No PoC.

Apply constraints kept. 13 testing/UX skills. No `exploiting-*`.

See [[hunt-harden-loop]].

## Pages updated

[[hunt-harden-loop]] · [[lanbb]]
