---
type: source
tags:
  - project
created: 2026-08-27
updated: 2026-08-27
---

# src-lanbb-pr16-loop6

- PR: https://github.com/elan7192/LanBB/pull/16 MERGED
- Merge SHA: `2019d6c76df9b80a3bf63c5025d4a974dc70a0a3`
- Wall SHA: `9795cd9`
- Date: 2026-08-27
- Via PM. Not a chat dump. Not copied into `raw/`.

## Claims kept

Loop6. Report at 0/N. Studio coding-snippets pill.

v5 juice read-only skipped EROFS/tmpfs. v6 actually applies.

Wall v5-hardened → v6. `9795cd9`.

Harden named (defense): juice root writable, tmpfs only `/tmp`, read-only edge, login closed, GET/HEAD only, SPA/static leak closed.

See [[hunt-harden-loop]].

## Pages updated

[[hunt-harden-loop]] · [[lanbb]]
