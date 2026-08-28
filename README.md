# Second brain

Compiled personal wiki with a disposable FTS5 index. Open this repo as an Obsidian vault. `Home.md` is the door.

## Obsidian

1. Obsidian → Open folder as vault → this repo.
2. Open `Home.md`.
3. Open graph view. Colors: gold wiki, teal maps, blue hunt/twitter, green people, coral ship.

If you are not in Obsidian, open `output/obsidian-graph.html`.

## Agent

1. Ask questions from this repo root. The agent runs `python3 tools/sb ask`.
2. Drop a source in `raw/` and say `ingest this`.
3. After ingest: `python3 tools/sb validate`. After retrieval changes: `python3 tools/sb eval`.

Schema: `AGENTS.md`. Claude Code also reads `CLAUDE.md`.

## CLI

```
python3 tools/sb rebuild-index --write-ids
python3 tools/sb search "agent memory"
python3 tools/sb ask "What did we decide about retrieval?"
python3 tools/sb trace claim:fts5-index-is-disposable
python3 tools/sb contradictions
python3 tools/sb stale
python3 tools/sb orphans
python3 tools/sb validate
python3 tools/sb eval
```

Markdown is canonical. `.cache/secondbrain.sqlite` is disposable.

## Layout

```
Home.md       vault door
raw/          immutable sources
wiki/         compiled pages
wiki/data/    claims and contradictions
eval/         retrieval gold sets
tools/sb      memory-engine CLI
maps/         Jarvis, Hooks, TELOS
hunt/         scout indexes
ship/         drafts, digests, angles, builds
output/       briefs and the rendered graph
.obsidian/    graph colors and workspace
```
