---
type: ship
tags:
  - ship
created: 2026-08-24
updated: 2026-08-24
---

# DeerFlow bootstrap · 2026-08-24

Status report after following [[src-deer-flow]] `Install.md`. Compiled page: [[deer-flow]].

1. **Setup path used:** local. Docker was not available.
2. **Setup level reached:** local dependencies installed. `make check` passed. `make install` passed.
3. **Files created or detected:** `config.yaml` created. `.env` and `frontend/.env` created and not inspected. `extensions_config.json` was not created.
4. **Remaining user action:** add at least one `models` entry in `config.yaml`, then set the env var names that entry references. No active `$VAR` placeholders until a model is uncommented.
5. **Exact next command to start DeerFlow:** `cd /home/ubuntu/deer-flow && make dev`

Checkout: `/home/ubuntu/deer-flow` at `1aa813d`.
