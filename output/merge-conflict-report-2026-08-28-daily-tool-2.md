---
type: ship
tags:
  - ship
created: 2026-08-28
updated: 2026-08-28
---

# Merge conflict report · daily-tool-replace vs main (2)

Fetched `origin/main` at `a0e5609` (agent-facing docs / Disclosure Index), then merged into `cursor/can1357-daily-tool-replace-186d`.

## Simple (fixed)

Log union: kept this branch's prior merge entry and main's agent-facing plus entropy-quiz entries. Graph and ontology snapshots regenerated.

ID collision: this branch had remapped writing slop vs software slop to C26. Main C26 is file first vs code first (from agent-facing-docs). Remapped to **C29**. Main C26–C28 left alone.

## Complicated (not silently picked)

**C17 / C18 / C25** still unresolved on main. Untouched.

Watch items from [[daily-tool-replace-vault-2026-08-27]] (0 CSV, graph PNG Pillow) stayed watch.
