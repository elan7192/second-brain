---
id: concept:epistemic-labels
type: concept
schema: memory-v1
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-27
created_by: agent
confidence: high
source:
  - wiki/memory-ablation.md
  - wiki/memory-engineering.md
  - wiki/llm-wiki.md
derived_from:
  - memory-ablation
  - memory-engineering
  - llm-wiki
---

# Epistemic labels

Every new compiled claim is one of FACT, INFERENCE, or OPINION. Mixing them in unlabeled prose is how knowledge pollution starts. See [[memory-system]].

## FACT

Source S explicitly says X. The wiki may record that S said X. It may not upgrade a guess into this bucket. Source pages keep this under `## Claims kept`. See [[claims]].

## INFERENCE

The compiler infers Z from named claims X and Y. `derived_from` must list those claim ids or source slugs. Confidence is not `high` unless the sources already entail Z.

## OPINION

A recommended next research step or a parked design choice. It does not enter `MEMORY.md`. See [[memory-ablation]].

## Check

New `schema: memory-v1` concept pages must have at least one of `## FACT`, `## INFERENCE`, or `## OPINION`. `python3 tools/lint-wiki.py` fails if none of those headings exist.

If the source is silent: do not write a FACT. Write nothing, or mark `unverified` on an inference.

## Related

[[provenance]] · [[claims]] · [[memory-system]] · [[verifiable-instructions]] · [[anti-slop]]
