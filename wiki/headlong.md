---
type: concept
tags:
  - wiki
created: 2026-08-26
updated: 2026-08-26
---

# Headlong

Laude Institute / MIT Bash microharness for persistent agency. One thought stream. The agent keeps generating thoughts when nobody is talking to it.

Sources: [[src-laude-headlong]], [[src-hxiao-headlong]]. Repo `https://github.com/laude-institute/headlong`. Launch post `https://www.laude.org/updates/headlong-a-microharness-for-persistent-agents`.

## What it is

A message does not start a session. It lands as an observation. The agent decides if and when to reply. Idle thought backs off exponentially (5s, 10s, 20s, to a cap) and resets when a message arrives.

Core loop: a Thinker calls `shellm` (Bash recursive LM). `shellm` calls `llm`, may run a bash block, repeats until `FINAL` or no bash. `traj` stores a DAG of jsonl. `context` projects that DAG with tiered compaction (recent verbatim, older summarized).

Author line counts for `bin/` plus `thinkers/`: launch post 9.9K, README 9.8K by cloc. This trial at SHA `d8f83042c30ba34931259408077ead20e6bd93c3`: cloc code 9883 (18 bash files 9616, 2 sh 202, plus markdown/json). Quote 9883 at that SHA. See [[src-laude-headlong]].

## Author claims not measured here

- Background thought $1 to $2 an hour at Audel's settings with GLM or Grok. `unverified` here.
- Over 50 of the agent's commits pulled into main. `unverified` here.
- 48-minute unattended recall-process fix, 2026-08-05. Anecdote from the launch post. `unverified` as a method.
- Audel stopped its own service three times. Author lesson. Guard added (commits named `80cbb1e` and `da31e98` in the post). Not re-read from git here.

## Trial 2026-08-26 on this host

Installed from a checkout, `./install.sh --symlinks`, no `--init`. 25 of 25 tools in `~/.local/bin`. Core skills under `~/.skills/core-skills`. Thinker templates under `~/.headlong-thinkers`. TUI `headlong-tui` built. `status.sh`: dash stopped, no Headlong processes, no API key, no `.env`.

Docker daemon was down. `HEADLONG_NO_TTY=1 HEADLONG_FAKE_DOCKER=missing headlong-init --dry-run` exited 1 and named `HEADLONG_UNSANDBOXED=1`. That flag was not set. The 24/7 mind was not started. Slack and Telegram bridges were not started. D5.

`llm ping` with no key: `No model specified and no API key found.` `identity list`: no identities.

Harness tests run on this host (all pass): `test_sandbox_gate.sh` 26, `test_status.sh` 23, `test_context.sh` 21, `test_recap_context_upgrade.sh` 30.

## Hour trial 2026-08-26

Operator yes for one hour. No cloud API key on this host. Local Ollama `qwen2.5-coder:7b` aliased as `gpt-4o`. `LLM_API_URL=http://127.0.0.1:11434/v1/chat/completions`. Dummy OpenAI key name only, not a cloud secret.

Identity `hour`. `headlong-init` with `HEADLONG_NO_DASH=1`. Nested Docker overlay mount failed (`invalid argument` on this VM's overlay root). Dockerd stopped. `SHELLM_REQUIRE_DOCKER=0`. Local unsandboxed for this hour only.

Trial patch in `~/.headlong/app/thinkers/_lib/common.sh`: forward `LLM_API_URL` and `HEADLONG_HOME` as shellm `--var`. Without it, `llm` hit api.openai.com and failed.

Started 2026-08-26T01:06:25Z. Timer `headlong-hour-stop` fired 2026-08-26T02:07:16Z. Harvest ran `hour stop` then `headlong-killall` (19 processes). `hour status` after harvest: mind stopped, dash stopped. Slack and Telegram were not started. Do not restart without a new operator yes.

Trajectory `~/.headlong/app/.identities/hour/trajectories/6cf0dedb-root/trajectory.jsonl`: 37 rows, 45493 bytes. First ts 2026-08-26T01:01:21Z. Last durable row 2026-08-26T01:12:08Z. Processes kept running until harvest ~02:08Z. Types: trajectory 1, thought 12, error 5, shellm-run 2, prompt 2, action 2, reasoning 4, shell-output 4, result 2, fork 2, merge 1. Sources: seed 11, monolith 10, empty 16.

Durable monolith steps: 4× error rc=125 (Docker overlay); 1× error rc=1 (`llm` hit real OpenAI before URL forward); thought 01:05:44Z "I'll run the Headlong tests."; action `cd ~/.headlong/app/tests && ./run_tests.sh` (appended traj intent only); action 01:07:06Z nested `shellm 'Analyze the failed tests and suggest fixes' --max-iterations 2`; merge 01:12:08Z stalled (same failing command 3 times). Shell-output included `cat: /tmp/approach_a.txt: No such file or directory` from a literal copy of the shellm docs example.

Tests did not run. No `run-all.sh` / `test_sandbox` / `passed:` in the trajectory. Workdir empty. Notes under `~/.headlong/hour-notes/` are operator RUN.md plus harvest STOPPED_UTC. Brief: [[ingest-brief-2026-08-26-headlong-hour]].

## Vault rule

Headlong is a trial install, not the wiki runtime. One shared mind fights [[entropy-gate]] isolation and D4. See [[contradictions]] C15. The 2026-08-26 hour ended at 02:07Z. Do not restart without a new operator yes. Do not start Slack or Telegram bridges.

## Related

[[harness-routing]] · [[audited-task-contract]] · [[entropy-gate]] · [[memory-engineering]] · [[agent-operating-system]] · [[src-chatchat-living-brain]] · [[src-promptyx-llm-cpu]]
