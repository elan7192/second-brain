---
id: concept:musk-algorithm
type: concept
tags:
  - wiki
created: 2026-08-27
updated: 2026-09-01
---

# Musk Algorithm

Strict order. Best part is no part.

Source: [[src-lan-e-musk-algorithm]]. Named owner: lan E.

1. Make requirements less dumb. Named person, not a department. Only the laws of physics are absolute. Department names ("legal", "safety", "the schema") are not owners.
2. Delete the part or process. If you are not adding about 10% back, you did not delete enough.
3. Simplify and optimize only after delete. Do not optimize what should not exist.
4. Accelerate cycle time. Speed exposes hidden quality and flow problems.
5. Automate last.

Doing it backwards (automate, then simplify, then delete) wastes time.

Keep long-term vision. Starship lines on the source are examples, not new physics.

## Vault passes

- 2026-08-28: short door D12. Deleted full-index dump, first-principles page, MEMORY LanBB loops. C37 open.
- 2026-08-29: deleted door catalogs, standing brief, dual lint, graph mermaid. C38 skip.
- 2026-08-29b: deleted Home/index overlap, digest dump, `tools/sb.py`, MEMORY query duplicate, mandatory ontology rebuild, Home people catalog, GrowthOS graph on Home, graph islands table.
- Stopped: next pass found only locked parts (C17, C18, D1–D12, C38 existing briefs, append-only log).
- 2026-09-01: gate surface. Requirement owner was the schema author, not lan E, so it was deletable. Five gate commands became one: `sb validate` now includes the ontology check; lint no longer shells out to `tools/test_memory.py`; health lints once, not twice; `sb graph` and `sb memory-review` (unreferenced, the second a wish) gone; CI 7 steps to 3 (tests, validate, eval); empty `wiki/daily/` gone. Measured on the same VM, median of 3: validate 0.50s to 0.32s; health 0.85s to 0.32s; CI chain 3.3s to 2.1s. Docs folded: `AGENTS.md`, [[how-it-works]], [[vault-ontology]], [[deterministic-core]].
- 2026-09-01b, lan E yes on the three named leftovers. Graph renders `output/obsidian-graph.{html,png,svg}`, `output/obsidian-dataflow.html`, `output/growthos-graph.html` deleted from git and gitignored; `tools/render-*.py` rebuild them and the committed copies were already stale. Doors point at the command. The two "zero-inbound" briefs were a miscount (the search skipped `output/`; merge-conflict reports link them), so they stay under C38. Parser dedupe: one `WIKILINK` and one frontmatter parser in `tools/secondbrain/frontmatter.py`; `memorylib`, `ontology_lib`, `lint-wiki`, `render-obsidian-graph`, `render-dataflow`, `index`, `ingest_check` import it. C18 files untouched.

See [[log]]. Live query stays D9. C17 and C18 untouched.

## Related

[[raptor-dispatch]] · [[src-lan-e-musk-algorithm]] · [[index]] · [[verifiable-instructions]] · [[daily-tool-replace]]
