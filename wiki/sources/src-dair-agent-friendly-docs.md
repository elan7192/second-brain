---
type: source
tags:
  - twitter
created: 2026-08-24
updated: 2026-08-24
---

# src-dair-agent-friendly-docs

- Raw: none. URL ingest. `raw/` is human-owned.
- URL: https://x.com/dair_ai/status/2091661799737446864
- Paper: [From Agent Behaviour to Agent-Friendly Documentation](https://arxiv.org/abs/2608.20195) (Gao and Chen, Peking University)
- Date: 2026-08-23 (tweet)

## Claims kept

557 SWE-chat sessions, 94,813 events, 3,033 documentation interactions. 33,097 AIDev agentic pull requests, 690,260 file-level change records.

Agent instruction files 35.4%. Agent working notes 25.1%. Agent-facing subtotal 60.5% of documentation interactions (session-cluster 95% CI 53.9–66.5%). Classical technical documentation 10.6%. API references 1.3%.

Consultation is self-initiated 70.2% (CI 66.7–73.3%), failure-driven 7.5% (CI 6.0–9.3%). Immediate testing after consultation: adjusted OR 0.39 [0.25, 0.60]. Building: OR 0.25 [0.14, 0.44]. Zero events match the authors' Validate pattern (read then test or build). Adjacent $P(\text{edit code}\mid\text{read doc})=0.002$.

Production is 0.87× consultation. Among multi-commit PRs that change both and have order, code is first 4.7× more often than documentation. Agents edit their own `AGENTS.md` (692 PRs) and `CLAUDE.md` (362).

Actionability and verifiability of "agent-friendly" documentation lack consistent behavioural support in this corpus.

## Caveats

The working-notes share rests on unvalidated language-model path labels. Treat the exact percent as provisional.

Agent-reweighted consultation for agent-facing files is 50.1%. 60.5% is the event-weighted snapshot, not a constant.

Instruction-file counts are lower bounds. Runtime-loaded context files appear only if later read.

The instrument misses websites, model weights, and in-source docstrings. SWE-chat is opt-in. 87% of that corpus is one agent family.

## Pages updated

[[agent-facing-docs]] · [[verifiable-instructions]] · [[context-graph]] · [[tokens-as-capital]] · [[llm-wiki]] · [[self-verification]] · [[hunt-ship-loop]] · [[contradictions]]
