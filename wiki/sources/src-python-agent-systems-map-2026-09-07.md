---
id: source:src-python-agent-systems-map-2026-09-07
type: source
tags:
  - method
  - python
created: 2026-09-07
updated: 2026-09-07
---

# src-python-agent-systems-map-2026-09-07

- Provenance: Researchy fact-check pack `/workspace/fill/python-agent-factcheck-knowhow-2026-09-07.md` (CoS → Vault). Essay = systems collage; not copied into `raw/`.
- 判定: METHOD map
- Date: 2026-09-07
- Grade: **B+** (~75–85%) as systems essay collage — stronger than atom pack. Not a production runbook.
- **SKIP** Mojo desk rewrite; free-threaded as box default without Fill/lan E yes; Medium/G4G as SoR.

## Claims kept

**Architecture metaphor:** Agent = nondeterministic cognition ↔ deterministic tool loop. **Python = control plane**; C++/CUDA/Triton/(aspirational Mojo) = hot compute path.

**Desk STEAL:** leave Python when µs tools / huge object graphs; asyncio for I/O-bound agents; free-threading as **opt-in experiment** (wheel/`t` ABI caveats — not flip default); nanobind for new C++ helpers + `gil_scoped_release`; expandable_segments literacy when GPU burns.

**Fixes / caveats (verify vs PEP/docs):**
- pymalloc arenas: **256 KiB (32-bit) or 1 MiB (64-bit)** — not “256KB alone” on modern 64-bit (https://docs.python.org/3/c-api/memory.html).
- Free-threaded default allocator = **mimalloc** (3.13+).
- PEP 744: Tier-1 bytecode → Tier-2 uops → optional copy-and-patch JIT — not marketed as “hierarchical JIT” (https://peps.python.org/pep-0744/).
- PEP 703 free-threading: opt-in; single-thread ±memory tradeoffs; unmarked C-ext may re-enable GIL (https://peps.python.org/pep-0703/).
- Fragmentation “>0.35” empty_cache heuristic = **unverified folklore** — prefer memory snapshots.

Vault SoR: **PEP + docs.python.org + CPython** > Medium/G4G.

## Primaries (PEP / docs)

- Memory / pymalloc / mimalloc: https://docs.python.org/3/c-api/memory.html
- PEP 703: https://peps.python.org/pep-0703/
- Free-threading HOWTO: https://docs.python.org/3/howto/free-threading-python.html
- PEP 744: https://peps.python.org/pep-0744/
- nanobind: https://nanobind.readthedocs.io/

Pointer map only. Do not dump essay body. Do not mandate Mojo rewrite.

判定=METHOD map. Provenance: Researchy 2026-09-07.

## Pages updated

[[index-sources]] · [[harness-routing]] · [[work-per-cost]] · [[src-spotify-portal-claude-cheap-workers]] · [[src-googlecloud-long-horizon-agent-harness-5-patterns]] · [[src-code-stack-language-ai-correctness-2026-09-07]]

## Related

[[harness-routing]] · [[work-per-cost]] · [[quota-router]] · [[tokens-as-capital]] · [[src-spotify-portal-claude-cheap-workers]] · [[src-googlecloud-long-horizon-agent-harness-5-patterns]] · [[agent-operating-system]] · [[src-rudijr-gemini-video-route-2026-09-06]] · [[src-code-stack-language-ai-correctness-2026-09-07]]
