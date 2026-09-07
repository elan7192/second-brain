---
id: source:src-code-stack-genspark-fable-factcheck-2026-09-07
type: source
tags:
  - researchy
  - method
created: 2026-09-07
updated: 2026-09-07
---

# src-code-stack-genspark-fable-factcheck-2026-09-07

- Provenance: Researchy `/workspace/fill/code-stack-genspark-fable-factcheck-2026-09-07.md` against GenSpark `models/model-fable-5.1-code-stack.md` (CoS → Vault). Not copied into `raw/`.
- 判定: METHOD deltas / long-form SoR pointer
- Date: 2026-09-07
- Grade: **A / ~90–93%** — superset of [[src-code-stack-language-ai-correctness-2026-09-07]] (TLDR).
- **Adopt Fable code-stack as desk curriculum long-form SoR**; keep TLDR src as short door.
- **SKIP** free-threaded as box default; pad everything 128B on Apple without measure; assume TS7 replaced all `tsc`; trust Fable µs syscall numbers without local 〔实测〕.

## Claims kept (resolved version facts)

1. **Go 1.25 GOMAXPROCS:** container-aware default (cgroup CPU bandwidth) + periodic update. Pre-1.25 still needs `uber-go/automaxprocs` on older toolchains. https://go.dev/doc/go1.25 · https://go.dev/blog/container-aware-gomaxprocs
2. **CPython free-threaded:** 3.13 experimental; **3.14** officially supported **opt-in** (PEP 779); default install still GIL. https://docs.python.org/3/howto/free-threading-python.html
3. **YJIT:** still **off by default** (flag / `RUBY_YJIT_ENABLE` / `RubyVM::YJIT.enable`). https://docs.ruby-lang.org/en/3.4/yjit/yjit_md.html
4. **JDK 24 JEP 491:** Synchronize Virtual Threads without Pinning — Delivered in 24. JNI/native still pins. https://openjdk.org/jeps/491
5. **Apple cacheline nuance:** sysctl often 128; L1 false-sharing cliff often 64B; LLVM Apple CacheLineSize=64 — measure; not a single padding law.
6. **TS Corsa / tsgo:** real Go-port checker; “TS7 default tsc everywhere” stay Unverified.

Also STEAL: AI veto / T0–T4 last-yes table; profiler cheat sheet + bottleneck taxonomy. Keep Green Tea GC / ZJIT / GraalVM licensing Unverified.

Skim (ai-recog followup): three-state outputs 已判定 / 不可判定 / 不可观测 — Product A aligned; fold note on [[src-ai-recog-valuation-knowledge-2026-09-07]].

判定=METHOD. Long-form SoR = GenSpark Fable file via this pointer; TLDR = [[src-code-stack-language-ai-correctness-2026-09-07]].

Do not dump Fable essay into wiki. Do not rewrite desk.

## Pages updated

[[index-sources]] · [[src-code-stack-language-ai-correctness-2026-09-07]] · [[src-python-agent-systems-map-2026-09-07]] · [[harness-routing]] · [[src-ai-recog-valuation-knowledge-2026-09-07]] · [[src-skip-genspark-fable-picker-2026-09-07]]

## Related

[[src-code-stack-language-ai-correctness-2026-09-07]] · [[src-python-agent-systems-map-2026-09-07]] · [[harness-routing]] · [[src-ai-recog-valuation-knowledge-2026-09-07]] · [[src-skip-genspark-fable-picker-2026-09-07]] · [[audited-task-contract]] · [[verifiable-instructions]]
