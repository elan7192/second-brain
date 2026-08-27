---
type: concept
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-27
---

# Hunt-harden loop

CASE path on a local in-scope target. Find + report. Then harden. Not an exploit dump.

Sources: [[src-lanbb-pr9-loop1]] [[src-lanbb-pr10-loop2]] [[src-lanbb-pr11-loop3]] [[src-lanbb-pr13-loop4]] [[src-lanbb-pr15-loop5]] [[src-lanbb-pr16-loop6]] [[src-lanbb-pr17-loop7]] [[src-lanbb-pr18-loop8]] [[src-lanbb-pr19-loop9]] [[src-lanbb-pr20-loop10]] [[src-lanbb-pr21-loop11]] [[src-lanbb-pr22-loop12]] [[src-lanbb-pr23-loop13]] [[src-lanbb-pr24-loop14]] [[src-lanbb-pr25-loop15]] [[src-lanbb-pr26-loop16]]. Product: [[lanbb]]. Ethical hacking = in-scope find + report. See [[hunter-follows]].

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

## Loop7

- Report at 0/N. Studio applies pill.
- Wall: v6 → v7
- PR: https://github.com/elan7192/LanBB/pull/17 MERGED `7b009d6226d86040765f10a5b8dff99a49a2f845`
- Wall SHA: `7dd37e7`

v6 applied. v7 keeps apply constraints, then default-denies.

Harden named (defense): default-deny edge except score path. Leftover SPA/JS closed. Remaining `/api` `/rest` closed.

## Loop8

- Hunted: v7-hardened. Fill live 0/116. Score GET HTTP 200. Default-deny 403. POST score path 405.
- Report at 0/N. Wall applied.
- PR: https://github.com/elan7192/LanBB/pull/18 MERGED `7d98a3bae7d074b1683dd5aa5ad13f0d4ef7d7b8`
- Wall: v7 → v8-hardened. Next hunt uses v8.

v7 applied. v8 keeps apply constraints (no juice EROFS, no tmpfs over data/static, burst>=1, score GET stays open).

Harden named (defense): exact score path `^/api/Challenges/?$`, bind `127.0.0.1:3000` only, GET only (HEAD dropped), leftover SPA/Web3/payment closed, broader static deny, broader WAF signatures (no PoC). GET `/api/Challenges/` is the only proxied n/N path.

13 testing/UX skills. No `exploiting-*`. Coverage gaps named in PR: crypto, misc, misconfig, obscurity; docker-off deserialization/XXE. Not mixed into n/N.

## Loop9

- Report at 0/116.
- Wall: v8 → v9
- PR: https://github.com/elan7192/LanBB/pull/19 MERGED `75cb3bc98745a0057bca3a687a6ed900ba5aa290`
- Wall SHA: `dee7041`

v8 applied. v9 tightens score path + host allowlist.

Harden named (defense): exact-equals GET `/api/Challenges/`, host allowlist, leftover oauth/health/debug closed.

## Loop10

- Report at 0/116.
- Wall: v9 → v10
- PR: https://github.com/elan7192/LanBB/pull/20 MERGED `f8b4dbee63cd6d9931a2ced5c8e6b916684bcc52`
- Wall SHA: `0042064`

v9 applied. v10 tightens score path.

Harden named (defense): trailing-slash-only GET `/api/Challenges/`, empty-query/cookie-closed score path, leftover privacy/hidden/data HTTP closed.

## Loop11

- Hunted: v10-hardened. Fill live 0/116. Score GET HTTP 200. Default-deny 403.
- Report at 0/N. Wall applied.
- Wall: v10 → v11-hardened
- PR: https://github.com/elan7192/LanBB/pull/21 MERGED `484fbbeb64ae450b1fa5f1a56ebda5b24e22c070`
- Wall SHA: `3afb11b`

v10 applied. v11 closes extra headers on the score path. Next hunt uses v11.

Harden named (defense): Authorization/Origin/Referer closed on score path. Leftover continue-code/login/search/Baskets/nested SPA HTTP closed.

## Loop12

- Hunted: v11-hardened. Fill live 0/116. Score GET HTTP 200. Default-deny 403.
- Report at 0/N. Wall applied.
- Wall: v11 → v12-hardened
- PR: https://github.com/elan7192/LanBB/pull/22 MERGED `c201b5608eb82ac8a0b047d7634c9ec19257b485`
- Wall SHA: `e62fa4d`

v11 mem 4m / pids 4 failed (daemon min 6MB). v12 bakes `mem>=6m` `pids>=6`. Do not drop below.

Harden named (defense): extra hop/auth headers closed on score path. Leftover HTTP closed: hacking-instructor, juicy-nft, continue-code-xss, products-queries. Broader WAF/static deny and CSP/Permissions-Policy. No PoC.

Next hunt uses v12.

## Loop13

- Report at 0/116.
- Wall: v12 → v13-hardened
- PR: https://github.com/elan7192/LanBB/pull/23 MERGED `00ed19dde324fb766d3f0a7e5e2234a78397a923`
- Wall SHA: `e8c3a57`

v12 applied. Floor `mem>=6m` `pids>=6` held.

Harden named (defense): leftover rewrite/identity headers closed on score path. Leftover HTTP closed: continue-code-apply, tutorial, access_token, ftp-backup.

## Loop14

- Report at 0/116.
- Wall: v13 → v14-hardened
- PR: https://github.com/elan7192/LanBB/pull/24 MERGED `e1c2c581b5db1db08d6620762b0a109c8b6c37f9`
- Wall SHA: `4fd0b9f`

v13 applied. Floor `mem>=6m` `pids>=6` held.

Harden named (defense): leftover hop/session/token headers closed on score path. Leftover HTTP closed: continue-code-findIt-apply, fixIt-apply, snippets-fixes, 2FA-enter, web3-nft.

## Loop15

- Report at 0/116.
- Wall: v14 → v15-hardened
- PR: https://github.com/elan7192/LanBB/pull/25 MERGED `02f73dca18ca570f332904c2e5d3c35714c2978b`
- Wall SHA: `1801528`

v14 applied. Floor `mem>=6m` `pids>=6` held. `worker_processes 1` baked. Auto OOM 137 lesson.

Harden named (defense): leftover remote-user/oauth-proxy/tracing/cloud-auth headers closed. Leftover HTTP closed: web3-walletExploitAddress, 2FA-SPA, ftp-quarantine, solve-server-side, coupon.

## Loop16

- Report at 0/116.
- Wall: v15 → v16-hardened
- PR: https://github.com/elan7192/LanBB/pull/26 MERGED `9e8bbdcdc4657483dec100df8881865f53601724`
- Wall SHA: `75b62be`

v15 applied. Floor `mem>=6m` `pids>=6` held. `worker_processes 1` source `OOM=false`.

Harden named (defense): leftover tracing/cloud-auth headers closed. Leftover HTTP closed: CSAF, product-image, coupon-apply.

## Related

[[lanbb]] · [[file-memory]] · [[assign-execute-verify]] · [[hunter-follows]] · [[src-lanbb-pr9-loop1]] · [[src-lanbb-pr10-loop2]] · [[src-lanbb-pr11-loop3]] · [[src-lanbb-pr13-loop4]] · [[src-lanbb-pr15-loop5]] · [[src-lanbb-pr16-loop6]] · [[src-lanbb-pr17-loop7]] · [[src-lanbb-pr18-loop8]] · [[src-lanbb-pr19-loop9]] · [[src-lanbb-pr20-loop10]] · [[src-lanbb-pr21-loop11]] · [[src-lanbb-pr22-loop12]] · [[src-lanbb-pr23-loop13]] · [[src-lanbb-pr24-loop14]] · [[src-lanbb-pr25-loop15]] · [[src-lanbb-pr26-loop16]]
