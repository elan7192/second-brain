---
type: concept
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-27
---

# Hunt-harden loop

CASE path on a local in-scope target. Find + report. Then harden. Not an exploit dump.

Sources: [[src-lanbb-pr9-loop1]] [[src-lanbb-pr10-loop2]] [[src-lanbb-pr11-loop3]] [[src-lanbb-pr13-loop4]] [[src-lanbb-pr15-loop5]] [[src-lanbb-pr16-loop6]]. Product: [[lanbb]]. Ethical hacking = in-scope find + report. See [[hunter-follows]].

## Loop1

- Target: local OWASP Juice Shop
- Score: 0/116. Report still writes at 0/N
- Wall: v0 → v1-hardened
- PR: https://github.com/elan7192/LanBB/pull/9 SHA `ee8da04`

Harden named (defense): headers, login rate-limit, extra-file `/ftp` closed.

Fail-closed scope. Recon skip loopback. Studio score pill.

Procedural is in LanBB, not this vault: parse-scope, passive-recon, write-report. Engineer owns SKILL.md. Vault writes semantic + one [[log]] row. No chat dump. No vector DB. See [[file-memory]].

## Loop2

- Score: 0/116. Report still writes at 0/N
- Wall: v1-hardened → v2-hardened (keep v1)
- PR: https://github.com/elan7192/LanBB/pull/10

Harden named (defense): digest pin, stronger headers, broader rate limits, WAF-ish query block, close `/encryptionkeys` `/metrics` `/support` `/redirect`.

Cloud agent VM cannot hit local Juice Shop (connection refused). 0/N is still a valid report path.

Next loops: Fill reads live `GET /api/Challenges` on the box. Cloud agent only ships overlays + CASE UX.

## Loop3

- Hunted: v2. Fill live 0/116. Report path wrote.
- Wall: v2-hardened → v3-hardened
- PR: https://github.com/elan7192/LanBB/pull/11 SHA `b5bfb4d`
- Studio shows hunt vs current wall

Harden named (defense): method allowlist, URI WAF, cookie/COEP/HSTS, read-only edge. Closed: upload, PII, chatbot, B2B, snippets, continue-code.

`GET /api/Challenges` stays open.

## Loop4

- Hunted: v3. Report at 0/N. Studio hunted + fill pills.
- Wall: v3-hardened → v4-hardened
- PR: https://github.com/elan7192/LanBB/pull/13 SHA `821e998`
- PR12 duplicate, closed

Harden named (defense): app/edge caps, broader URI WAF. Closed: GraphQL, basket, reviews, captcha, data-export.

`GET /api/Challenges` stays open.

## Loop5

- Hunted: v4. Report at 0/N. Studio next-hunt pill.
- Wall: v4-hardened → v5-hardened
- PR: https://github.com/elan7192/LanBB/pull/15 MERGED `9227b4731a991db1017cfcbbbc79144f5343c943`
- Wall SHA: `17ca40d`

Harden named (defense): juice read-only, drop OPTIONS, login WAF, burst>=1. Closed: identity, Web3, catalog, search, info-leak.

`GET /api/Challenges` stays open. Login is the remaining auth door.

v5 juice read-only skipped EROFS/tmpfs. Not fully applied until v6.

## Loop6

- Report at 0/N. Studio coding-snippets pill.
- Wall: v5-hardened → v6
- PR: https://github.com/elan7192/LanBB/pull/16 MERGED `2019d6c76df9b80a3bf63c5025d4a974dc70a0a3`
- Wall SHA: `9795cd9`

Harden named (defense): juice root writable, tmpfs only `/tmp`, read-only edge, login closed, GET/HEAD only, SPA/static leak closed. v6 actually applies the read-only wall v5 skipped.

## Related

[[lanbb]] · [[file-memory]] · [[assign-execute-verify]] · [[hunter-follows]] · [[src-lanbb-pr9-loop1]] · [[src-lanbb-pr10-loop2]] · [[src-lanbb-pr11-loop3]] · [[src-lanbb-pr13-loop4]] · [[src-lanbb-pr15-loop5]] · [[src-lanbb-pr16-loop6]]
