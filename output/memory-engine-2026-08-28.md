# Memory engine 2026-08-28

Added stable `id:` on knowledge objects, a disposable SQLite FTS5 index, a claim/contradiction registry, and the `sb` CLI with `validate` and `eval`. Query now goes through `python3 tools/sb ask` to an evidence set instead of walking `wiki/index.md`.

Linked [[retrieval]], [[claims]], [[stable-ids]], and [[eval-suite]] into the catalog, D9, and `AGENTS.md`. Look at `python3 tools/sb eval` and unresolved `contradiction:c9` first.
