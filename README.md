# Second brain

Compiled personal wiki. Open this repo as an Obsidian vault. `Home.md` is the door.

## Obsidian

1. Obsidian → Open folder as vault → this repo.
2. Open `Home.md`.
3. Open graph view. Colors: gold wiki, teal maps, blue hunt/twitter, green people, coral ship.

If you are not in Obsidian, open `output/obsidian-graph.html`.

## Agent

1. Ask questions from this repo root in Cursor, Claude Code, or Codex.
2. Drop a source in `raw/` and say `ingest this`.
3. Query retrieval: `python3 tools/retrieve.py "<question>"`.

Schema: `AGENTS.md`. Claude Code also reads `CLAUDE.md`. Claim ledger: `wiki/claims.csv`.

## Layout

```
Home.md       vault door
raw/          immutable sources
wiki/         compiled pages
maps/         Jarvis, Hooks, TELOS
hunt/         scout indexes
ship/         drafts, digests, angles, builds
output/       briefs and the rendered graph
.obsidian/    graph colors and workspace
```
