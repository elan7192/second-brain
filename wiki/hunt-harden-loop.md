---
type: concept
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-27
---

# Hunt-harden loop

CASE path on a local in-scope target. Find + report. Then harden. Not an exploit dump.

Source: [[src-lanbb-pr9-loop1]]. Product: [[lanbb]]. Ethical hacking = in-scope find + report. See [[hunter-follows]].

## Loop1

- Target: local OWASP Juice Shop
- Score: 0/116. Report still writes at 0/N
- Wall: v0 → v1-hardened
- PR: https://github.com/elan7192/LanBB/pull/9 SHA `ee8da04`

Harden named (defense): headers, login rate-limit, extra-file `/ftp` closed.

Fail-closed scope. Recon skip loopback. Studio score pill.

Procedural is in LanBB, not this vault: parse-scope, passive-recon, write-report. Engineer owns SKILL.md. Vault writes semantic + one [[log]] row. No chat dump. No vector DB. See [[file-memory]].

## Related

[[lanbb]] · [[file-memory]] · [[assign-execute-verify]] · [[hunter-follows]] · [[src-lanbb-pr9-loop1]]
