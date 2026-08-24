---
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-24
---

# DeerFlow

ByteDance SuperAgent harness. Repo: https://github.com/bytedance/deer-flow. Source page: [[src-deer-flow]].

## Local bootstrap (2026-08-24)

Followed `Install.md` on this Cloud Agent VM.

Path used: local. Docker was not installed, so `docker info` failed and Docker init was skipped.

| Step | Result |
| --- | --- |
| Clone | `/home/ubuntu/deer-flow` at `1aa813d` |
| `make config` | created `config.yaml` (also `.env` and `frontend/.env`; those files were not opened) |
| `make check` | first fail: missing `uv` and `nginx` |
| Tooling | installed `uv` 0.12.5 user-space; installed `nginx` 1.24.0 via apt |
| `make check` retry | passed (Node 22.14.0, pnpm 10.26.2, uv 0.12.5, nginx 1.24.0) |
| `make install` | passed (backend `.venv`, frontend `node_modules`, pre-commit hook) |
| Services | not started. ports 2026 / 3000 / 8001 were idle |

## Remaining before launch

1. Add at least one uncommented entry under `models` in `config.yaml`. The template has 26 commented examples and 0 active models.
2. Put real values in the env vars that entry references (`$OPENAI_API_KEY`, `$ANTHROPIC_API_KEY`, `$VOLCENGINE_API_KEY`, or whichever provider you uncomment). Active `$VAR` placeholders were all commented; none need values until a model is enabled.
3. Copy `extensions_config.example.json` to `extensions_config.json` if you need MCP/skills config. `make config` does not create it. See [[contradictions]] C5.
4. Start with `make dev` from `/home/ubuntu/deer-flow`. UI: http://localhost:2026.

Optional later: `make setup-sandbox` if you use a Docker/container sandbox. Docker is still absent on this VM.

## Related

[[src-deer-flow]] · [[deer-flow-bootstrap-2026-08-24]] · [[github]]
