---
id: ship:merge-conflict-report-2026-08-28-deer-flow
type: ship
tags:
  - ship
created: 2026-08-28
updated: 2026-08-28
---

# Merge conflict report · deer-flow bootstrap vs main

Fetched `origin/main` at `db892ee` (Avid Company Foundry / C31), then merged into `cursor/deer-flow-bootstrap-fd24`.

## Simple (fixed)

Unions on Home, hunt/github, Today, index, and log. Today stayed 2026-08-28 from main; deer-flow went into Look at, not Done.

ID collision: this branch used C8 for DeerFlow `make config` vs `extensions_config.json`. Main C8 is two anti-slop tens. Remapped to **C32** on [[contradictions]], `wiki/data/contradictions.yaml`, [[deer-flow]], [[index]], [[log]], and [[Today]]. Anti-slop C8 left alone.

## Complicated (not silently picked)

**C17 / C18 / C25** still unresolved on main. Untouched.
