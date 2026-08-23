# Second brain

Compiled personal wiki. Raw sources stay immutable. The agent maintains interlinked markdown in `wiki/`.

## Start

1. Open `Home.md` or `wiki/index.md`.
2. Ask questions in Cursor, Claude Code, or Codex from this repo root.
3. Drop a source in `raw/` and say `ingest this`.

The schema is `AGENTS.md`. Claude Code also reads `CLAUDE.md`, which points at the same rules.

## Layout

```
raw/          immutable sources
wiki/         compiled pages, index, log
output/       briefs and answers built from the wiki
AGENTS.md     schema
MEMORY.md     durable facts only
decisions.md  locked choices
```

## Why this shape

RAG re-derives knowledge on every query. A compiled wiki derives it once and keeps it current. See [[llm-wiki]] and [[tokens-as-capital]].
