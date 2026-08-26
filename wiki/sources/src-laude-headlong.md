---
type: source
tags:
  - twitter
created: 2026-08-26
updated: 2026-08-26
---

# src-laude-headlong

- Tweet: https://x.com/andykonwinski/status/2091990178638496195 (2026-08-24, Andy Konwinski)
- Launch: https://www.laude.org/updates/headlong-a-microharness-for-persistent-agents
- Repo: https://github.com/laude-institute/headlong
- Installer: https://headlong.ai/install.sh
- Authors: Laude Institute / MIT
- Not copied into `raw/`.

## Claims kept

Headlong is an open-source Bash microharness for persistent agency. A Headlong agent is never asleep. Human messages are observations in one thought stream. The agent decides if and when to reply.

Core: Thinker loop, `shellm` (Bash RLM), `traj` (jsonl DAG), `context` (tiered projection). Launch post: core currently less than 10K lines of Bash (9.9K in `bin/` and `thinkers/`). README: 9.8K by cloc. Trial SHA `d8f83042c30ba34931259408077ead20e6bd93c3` cloc code in those dirs: 9883. See [[headlong]].

Install one-liner: `curl -fsSL https://headlong.ai/install.sh | bash`. Needs bash 3.2+, git, curl, jq, and an LLM API key. Docker is the sandbox. Without Docker, init stops unless `HEADLONG_UNSANDBOXED=1` or a typed yes. `HEADLONG_NO_THINKERS=1` and `HEADLONG_NO_DASH=1` skip those parts.

Author cost: $1 to $2 an hour background thinking at Audel's settings with GLM or Grok. Not measured here.

Author ops: team talks over Slack and Telegram; one stream, assume anything said is shared. Agent named Audel. Over 50 of its commits pulled into main (`unverified` here). 48-minute unattended recall fix 2026-08-05 (`unverified` as method). Self-stop three times; guard commits named `80cbb1e` and `da31e98` in the post, not re-read from git here.

Quoted by [[src-hxiao-headlong]].

## Pages updated

[[headlong]] · [[harness-routing]] · [[entropy-gate]] · [[agent-operating-system]] · [[contradictions]]
