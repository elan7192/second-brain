---
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-24
---
# EvoSyn

Evolves a test/solution filter from seed oracles, then synthesizes executably checkable training items.

Source: [[src-arxiv-2510-17928]]. Project: [[arxiv-tierlist]].

## Kept

MAP-Elites + islands, fitness against human seed tests. LiveCodeBench 231 items; AgentBench-OS 673 items. GRPO and distillation beat same-size random-test controls on the numbers in the digest.

Executable tests only. Small datasets. Appendix prompts not inspected one-by-one.

## Related

[[arxiv-tierlist]] · [[self-verification]]
