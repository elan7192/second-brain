---
type: source
tags:
  - project
created: 2026-08-27
updated: 2026-08-27
---

# src-lanbb-pr18-loop8

- PR: https://github.com/elan7192/LanBB/pull/18 MERGED
- Merge SHA: `7d98a3bae7d074b1683dd5aa5ad13f0d4ef7d7b8`
- Date: 2026-08-27
- Via PM. PR body is the source. Not a chat dump. Not copied into `raw/`.

## Claims kept

Loop8 hunted v7-hardened. Fill live 0/116. Score GET HTTP 200. Default-deny 403. POST on score path 405. `docker_disabled=18`. N=116. docker-solvable=98.

v7 wall applied. Report at 0/N still wrote.

Wall raised to v8-hardened. Next hunt must use v8.

v8 keeps apply constraints. Score path exact `^/api/Challenges/?$`. Bind `127.0.0.1:3000` only. GET only. Leftover SPA/Web3/payment closed. Broader static deny. Broader WAF signatures (no PoC). GET `/api/Challenges/` is the only proxied n/N path.

13 testing/UX skills. No `exploiting-*`. No C2/phishing/malware/sqlmap. Lab only.

See [[hunt-harden-loop]].

## Pages updated

[[hunt-harden-loop]] · [[lanbb]]
