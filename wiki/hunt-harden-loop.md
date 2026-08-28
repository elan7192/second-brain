---
type: concept
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-28
---

# Hunt-harden loop

CASE path on a local in-scope target. Find + report. Then harden. Not an exploit dump.

Product: [[lanbb]]. Ethical hacking = in-scope find + report. See [[hunter-follows]]. Origin: [[src-lanbb-pr9-loop1]]. Current: [[src-lanbb-pr27-loop17]]. Intermediate loop source pages stay in [[index-sources]]; this page does not list all 17.

## Current wall

- Target: local OWASP Juice Shop
- Score: 0/116. Report still writes at 0/N
- Wall: v17-hardened `ad6f669`
- PR: https://github.com/elan7192/LanBB/pull/27 MERGED `94ac04c986723ad34560e5ca7abb4d652f8a6eef`
- Floor: `mem>=6m` `pids>=6`. Do not drop below. v11 tried 4m/4 and the daemon died.
- `worker_processes 1` source `OOM=false`
- Cloud agent VM cannot hit local Juice Shop (connection refused). Fill live GET is on the box. Cloud agent ships overlays + CASE UX only.
- Fail-closed scope. Recon skip loopback.
- No `exploiting-*` skills.
- Last loop this window. No more until PM says.

Procedural is in LanBB, not this vault: parse-scope, passive-recon, write-report. Engineer owns SKILL.md. Vault writes semantic + one [[log]] row. No chat dump. No vector DB. See [[file-memory]].

## Loops 1–17

| Loop | PR | Merged | Wall | Note |
| --- | --- | --- | --- | --- |
| 1 | [9](https://github.com/elan7192/LanBB/pull/9) | | `ee8da04` v1 | headers, login rate-limit, `/ftp` closed |
| 2 | [10](https://github.com/elan7192/LanBB/pull/10) | | v2 | digest pin, broader rate limits, WAF-ish; VM connection refused |
| 3 | [11](https://github.com/elan7192/LanBB/pull/11) | | `b5bfb4d` v3 | method allowlist, URI WAF; upload/PII/chatbot closed |
| 4 | [13](https://github.com/elan7192/LanBB/pull/13) | | `821e998` v4 | GraphQL/basket/reviews closed. PR12 dup closed |
| 5 | [15](https://github.com/elan7192/LanBB/pull/15) | `9227b47` | `17ca40d` v5 | juice read-only skipped EROFS/tmpfs until v6 |
| 6 | [16](https://github.com/elan7192/LanBB/pull/16) | `2019d6c` | `9795cd9` v6 | juice root writable, tmpfs only `/tmp`; read-only actually applies |
| 7 | [17](https://github.com/elan7192/LanBB/pull/17) | `7b009d6` | `7dd37e7` v7 | default-deny except score path |
| 8 | [18](https://github.com/elan7192/LanBB/pull/18) | `7d98a3b` | v8 | exact score path, bind `127.0.0.1:3000`, GET only |
| 9 | [19](https://github.com/elan7192/LanBB/pull/19) | `75cb3bc` | `dee7041` v9 | exact-equals GET `/api/Challenges/`, host allowlist |
| 10 | [20](https://github.com/elan7192/LanBB/pull/20) | `f8b4dbe` | `0042064` v10 | trailing-slash-only score path |
| 11 | [21](https://github.com/elan7192/LanBB/pull/21) | `484fbbe` | `3afb11b` v11 | Authorization/Origin/Referer closed on score path |
| 12 | [22](https://github.com/elan7192/LanBB/pull/22) | `c201b56` | `e62fa4d` v12 | bake `mem>=6m` `pids>=6` |
| 13 | [23](https://github.com/elan7192/LanBB/pull/23) | `00ed19d` | `e8c3a57` v13 | leftover rewrite/identity headers closed |
| 14 | [24](https://github.com/elan7192/LanBB/pull/24) | `e1c2c58` | `4fd0b9f` v14 | leftover hop/session/token headers closed |
| 15 | [25](https://github.com/elan7192/LanBB/pull/25) | `02f73dc` | `1801528` v15 | `worker_processes 1` baked. Auto OOM 137 |
| 16 | [26](https://github.com/elan7192/LanBB/pull/26) | `9e8bbdc` | `75b62be` v16 | `OOM=false` |
| 17 | [27](https://github.com/elan7192/LanBB/pull/27) | `94ac04c` | `ad6f669` v17 | current. Last this window |

Every loop reported 0/116. Leftover HTTP paths per loop stay on the loop source page in [[index-sources]].

## Related

[[lanbb]] · [[file-memory]] · [[assign-execute-verify]] · [[hunter-follows]] · [[src-lanbb-pr9-loop1]] · [[src-lanbb-pr27-loop17]] · [[musk-algorithm]]
