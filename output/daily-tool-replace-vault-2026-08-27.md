---
type: ship
tags:
  - ship
created: 2026-08-27
updated: 2026-08-27
---

# Daily-tool-replace vs this vault

Question: room to optimize this project with [[daily-tool-replace]]?

Answer: yes, as delete and skip. No, as a new git GUI. Human verdict still required. See [[multi-source-verdict]].

Sources: [[src-can1357-daily-tool-replace-2026-08-27]], [[musk-algorithm]], [[grok-bot-quota]], [[clip-pipeline]], D7 in `decisions.md`. Lint run 2026-08-27: `python3 tools/lint-wiki.py` `pages=326 missing=0 orphans=19`.

## Kill

- Clone omp.sh / oh-my-pi. [[daily-tool-replace]]
- GitKraken-class git UI for this repo. Wiki silent that this vault's daily flow is GitKraken. D7 is Obsidian.
- Composio install. Writes need lan E. [[composio-mcp]]
- Coordinator / Worker / Verifier bots. Second JSONL graph store. [[loop-graph-engineering]]
- Scheduled X scan. Autopublish. [[assign-execute-verify]] D5
- Automate ingest first. [[musk-algorithm]] step 5
- Treat hour tops as a vault SLA. Tweet wording. No timed study.

## Watch

- [[file-memory]] setup is markdown + one CSV. This clone has 0 CSV. Do not invent the table.
- Graph PNG path imports Pillow. This ingest needed `pip install pillow` or mermaid never wrote. Delete PNG vs pin dep: no bake-off. `unverified` which is cheaper.
- Lint prints 19 `ORPHAN ingest-brief-2026-08-24-*` lines and still exits 0. Gate ignores orphans. Tightening it would force link or delete. Wait for lan E.

## Pursue

- Next URL ingest: captions and metadata first. Skip video/vision unless a claim depends on frames. This pair's 6.25s clip burned vision. [[clip-pipeline]] [[grok-bot-quota]]
- Link or delete those 19 orphan briefs. Delete before a new ingest app. [[musk-algorithm]]
- Keep compiling into `wiki/`. This vault already pays ingest once. [[tokens-as-capital]]

## Related

[[daily-tool-replace]] · [[can-boluk]] · [[work-per-cost]]
