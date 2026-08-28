# Second brain

Compiled personal wiki with a disposable FTS5 index. Open this repo as an Obsidian vault. `Home.md` is the door.

## Obsidian

1. Obsidian → Open folder as vault → this repo.
2. Open `Home.md`.
3. Open graph view. Colors: gold wiki, teal maps, blue hunt/twitter, green people, coral ship.

If you are not in Obsidian, open `output/obsidian-graph.html`.

## Agent

1. Ask questions from this repo root. The agent runs `python3 tools/sb ask` (D9). `wiki/index.md` is the Obsidian door. Paper and source catalogs are D12, not the query path.
2. Drop a source in `raw/` and say `ingest this`.
3. After ingest: `python3 tools/sb validate`. After retrieval changes: `python3 tools/sb eval`.

Schema: `AGENTS.md`. Claude Code also reads `CLAUDE.md` (pointer only, D2). Claims: `wiki/claims.csv` compile plus `wiki/data/claims.yaml`. C17.

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
python3 tools/rebuild-ontology.py
python3 tools/ontology.py counts
```

Markdown is canonical. `.cache/secondbrain.sqlite` is disposable.
`output/ontology-objects.csv` is a derived object table, not hosted Palantir AIP.

## Layout

```
Home.md       vault door
raw/          immutable sources (untrusted data)
wiki/         compiled pages
wiki/claims.csv  compile of source Claims kept (C17 vs yaml)
wiki/data/    claims and contradictions
eval/         retrieval gold sets
tools/sb      memory-engine CLI
maps/         Jarvis, Hooks, TELOS
hunt/         scout indexes
ship/         drafts, digests, angles, builds
output/       briefs and the rendered graph
.obsidian/    graph colors and workspace
```

Lint: `python3 tools/lint-wiki.py`. Rebuild claims: `python3 tools/compile-claims.py`. Schema: `AGENTS.md`.
