---
id: source:src-spotify-portal-claude-cheap-workers
type: source
tags:
  - spotify
  - claude-code
  - cost
  - routing
created: 2026-09-05
updated: 2026-09-05
---

# src-spotify-portal-claude-cheap-workers

- Primary: https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90
- Title: Portal by Spotify cut my Claude Code token usage by 90%
- Author: Dimitri Mazmanov (Principal Product Manager, Spotify)
- Published: 2026-09-03 (Spotify Engineering blog)
- Companion code / marketplace: https://github.com/spotify/portal-ai-plugins (`portal@portal`, `shunt@portal`)
- Secondary cite (discovery trigger): Yarchi @undefinedKi https://x.com/undefinedKi/status/2095942506433089832 → thin pointer [[src-undefinedki-spotify-claude-cheap-workers]]
- Researchy verdict 2026-09-05: **Spotify published = TRUE** (official eng post + plugins). VERIFIED. Not a third-party paraphrase.
- Not copied into `raw/`.
- Do **not** conflate with Anthropic Spotify case study https://claude.com/customers/spotify (different ~90% claim: migration *time* / Honk / Agent SDK).

## Claims kept

Cheap-workers routing for Claude Code via Portal AiKA modes + `shunt` plugin:

1. **file→summary (bulk-read):** PreToolUse hook blocks large `Read`s; Claude must call `bulk-read`, which sends paths + question to a cheap AiKA mode (`bulk-reader`, e.g. Gemini 2.5 Flash) that returns structured bullets. Raw file corpus never enters Claude’s context.
2. **example→disk (code-write):** `code-write` sends spec + required reference file to `code-writer` mode; generated code is stripped of fences and written to `--target` on disk. Claude never sees the generated output tokens.
3. **Hard gate ~350 lines:** `check-file-size` blocks Read when file exceeds **`SHUNT_MIN_LINES` default 350** (configurable, e.g. 500). Targeted offset/limit reads and piped bash reads pass through; also blocks cat/head/tail/less/more on large files.

**~90% figure:** mean bulk-read token savings on Java monorepo test scenarios (Claude reading files directly vs consuming the bulk-reader summary). **Not** a company-wide Claude Code token bill cut. Code-write savings are harder to measure because output never enters Claude’s context.

Caveats from the post (kept): cannot delegate editing (need targeted reads for line-accurate edits); cannot delegate reasoning/debugging/architecture/safety-critical work; cheap workers can miss subtle bugs; latency 10–30s per delegation.

## Pages updated

[[index-sources]] · [[src-undefinedki-spotify-claude-cheap-workers]] · [[src-avichawla-trueforge]]

## Related

[[src-undefinedki-spotify-claude-cheap-workers]] · [[src-avichawla-trueforge]] · [[src-community-compaction]] · [[harness-routing]] · [[work-per-cost]] · [[tokens-as-capital]] · [[src-gabrielchua-astra-cross-window-notes]]
