---
id: source:src-code-stack-language-ai-correctness-2026-09-07
type: source
tags:
  - researchy
  - method
created: 2026-09-07
updated: 2026-09-07
---

# src-code-stack-language-ai-correctness-2026-09-07

- Provenance: Researchy `/workspace/fill/code-stack-language-ai-correctness-2026-09-07.md` (CoS → Vault). Not copied into `raw/`.
- 判定: METHOD
- Date: 2026-09-07
- Related prior: [[src-python-agent-systems-map-2026-09-07]]
- GenSpark model-fable code-stack output: **PENDING** (prompt staged; file missing).
- **SKIP** desk-wide Mojo/Rust rewrite; free-threaded as box default without Fill/lan E yes; “AI code needs no tests.”

## Claims kept

**Execution-layer atoms:** ISA → OS → runtime → language → libraries → your code → process topology → human/AI loop. “Language X is fast” is meaningless without naming **which layer** you pay.

**Language-by-plane:** Python = control bus / agent I/O; C++/CUDA/Rust = hot path **after** profile. Align [[src-python-agent-systems-map-2026-09-07]] · [[harness-routing]].

**Measure-first:** reproduce → profile → Amdahl ceiling → one hypothesis → remeasure. Prefer delete work / batch I/O / better algo before language hop.

**AI code guilty until tests + last-yes:** generate → typecheck → pytest/CI → (mutation if critical) → human review → last-yes merge. Prefer independent oracles over dual-model self-agree. Sandbox untrusted AI code off prod creds.

判定=METHOD. Primaries: PEP 703/744 · https://docs.python.org/3/c-api/memory.html · language docs · Amdahl.

Pointer map only. Do not dump Researchy body. Do not rewrite desk from this note.

## Pages updated

[[index-sources]] · [[src-python-agent-systems-map-2026-09-07]] · [[harness-routing]]

## Related

[[src-python-agent-systems-map-2026-09-07]] · [[harness-routing]] · [[work-per-cost]] · [[audited-task-contract]] · [[verifiable-instructions]] · [[musk-algorithm]] · [[src-skip-genspark-fable-picker-2026-09-07]]
