---
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-24
---

# Agent-facing docs

Coding agents spend most of their documentation attention on instruction files and their own working notes.

Source: [[src-dair-agent-friendly-docs]].

## What they read

Event-weighted shares from 3,033 documentation interactions in 557 SWE-chat sessions:

| Type | Share |
| --- | --- |
| Agent instructions (`AGENTS.md`, `CLAUDE.md`, `SKILL.md`, rule files) | 35.4% |
| Agent working notes (plans, `thoughts/`, brainstorms, review logs) | 25.1% |
| Agent-facing subtotal | 60.5% (cluster CI 53.9–66.5%) |
| Classical technical documentation | 10.6% |
| API references | 1.3% |

Agent-reweighted consultation for agent-facing files is 50.1%. Treat 60.5% as the event-weighted snapshot, not a constant. The working-notes share rests on unvalidated language-model path labels.

Instruction-file counts are lower bounds. Runtime-loaded context files appear only if the agent later reads them.

## What they do not do

- Adjacent read-then-edit-code: 0.002.
- Consultation followed by a test or build: 0 events under the authors' Validate definition.
- Immediate testing after consultation: adjusted OR 0.39 [0.25, 0.60]. Building: OR 0.25 [0.14, 0.44].
- Failure-driven consultation: 7.5%. First recovery action is a doc read in 5.4% of 2,034 failures.

Actionability and verifiability of "agent-friendly" docs have no consistent behavioural support in this corpus. See [[contradictions]] C9.

## Two-lobed cycle

Consultation circulates into more reading and reasoning. Production of documentation is 0.87× consultation. The two lobes are loosely coupled.

In multi-commit agentic PRs that change both and have order, code is first 4.7× more often than documentation. 42.6% touch both in one commit. See [[contradictions]] C8.

Agents also edit their own instructions. AIDev: `AGENTS.md` in 692 PRs, `CLAUDE.md` in 362.

## Use here

1. Put operational rules on the instruction and wiki surface. See D8 in `decisions.md`.
2. Do not treat reading `AGENTS.md` as the check. Run `python3 tools/lint-wiki.py`.
3. File working notes into `wiki/` or `output/`. They are a first-class maintenance surface.
4. Keep this vault's file-first ingest. Observed public agents touch code first.

## Related

[[verifiable-instructions]] · [[context-graph]] · [[tokens-as-capital]] · [[llm-wiki]] · [[self-verification]] · [[hunt-ship-loop]]
