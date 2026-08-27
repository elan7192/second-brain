---
type: source
tags:
  - project
created: 2026-08-27
updated: 2026-08-27
---

# src-lanbb-pr10-loop2

- PR: https://github.com/elan7192/LanBB/pull/10
- Date: 2026-08-27
- Via PM. Merging. Not a chat dump. Not copied into `raw/`.

## Claims kept

Loop2. Score 0/116. Wall v1-hardened → v2-hardened. Keep v1.

Harden named (defense): digest pin, stronger headers, broader rate limits, WAF-ish query block, close `/encryptionkeys` `/metrics` `/support` `/redirect`.

Cloud agent VM cannot hit local Juice Shop (connection refused). Score 0/N is still a valid report path.

Next loops: Fill reads live `GET /api/Challenges` on the box. Cloud agent only ships overlays + CASE UX.

See [[hunt-harden-loop]].

## Pages updated

[[hunt-harden-loop]] · [[lanbb]] · [[file-memory]]
