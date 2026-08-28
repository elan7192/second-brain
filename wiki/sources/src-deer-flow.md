---
id: source:src-deer-flow
type: source
tags:
  - github
created: 2026-08-24
updated: 2026-08-28
---

# src-deer-flow

- Raw: none in `raw/`. Read from the public repo at clone time.
- URL: https://github.com/bytedance/deer-flow
- Install guide: https://github.com/bytedance/deer-flow/blob/main/Install.md
- Date: 2026-08-24
- Clone: `/home/ubuntu/deer-flow` at `1aa813d` (`feat: add managed subagents and delegation scopes (#4887)`)

## Claims kept

DeerFlow is ByteDance's open-source SuperAgent harness (research, code, create). Local bootstrap is defined in `Install.md`: clone if needed, `make config`, prefer Docker (`make docker-init` then `make docker-start`) else local (`make check`, `make install`, then `make dev`). Do not assume API keys. Do not start long-running services during bootstrap. `config.yaml` is generated from `config.example.yaml`. The template `models:` block is examples only; every `- name:` line is commented. `make config` copies `config.yaml`, `.env`, and `frontend/.env`. It does not copy `extensions_config.example.json`.

## Pages updated

[[deer-flow]] · [[contradictions]]
