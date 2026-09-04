---
id: concept:graph-node-ablation
type: concept
schema: memory-v1
tags:
  - wiki
created: 2026-09-03
updated: 2026-09-04
created_by: agent
confidence: medium
source:
  - wiki/sources/src-0xwast3-ablation-schema.md
derived_from:
  - src-0xwast3-ablation-schema
  - musk-algorithm
  - memory-ablation
  - loop-graph-engineering
---

# Graph node ablation

Ablation test for multi-agent / workflow graphs: keep a node only if removing it changes the outcome.

Source: [[src-0xwast3-ablation-schema]]. Same delete spirit as [[musk-algorithm]] and [[memory-ablation]].

## FACT

[[src-0xwast3-ablation-schema]]: schema is RUN → PULL → DELTA → RANK → CUT.

- RUN: execute with the full graph
- PULL: rerun with one node removed
- DELTA: measure how much worse the output got
- RANK: sort nodes by damage from absence
- CUT: retire a node whose removal changes nothing

Do not measure a node only by what it produces. Measure by what breaks when it is gone.

Author-reported production anecdote (17 nodes, 4 no-ops, one perpetual token burner) stays author-reported / unverified counts.

## INFERENCE

Apply before adding a specialist Bot, Skill step, or graph node: if PULL leaves W/E and acceptance unchanged, CUT. Prefer fold into an existing owner over a new node. derived_from: src-0xwast3-ablation-schema, work-per-cost, raptor-dispatch.

Pairs with [[loop-graph-engineering]] start-small (one worker, three-round cap) and house ban on Coordinator/Worker/Verifier bot farms. derived_from: loop-graph-engineering.

## OPINION

Frameworks that only add nodes without a CUT step grow dead weight. Park wholesale graph-framework installs until ablation is cheap to run.

## Check

If someone proposes a new Bot, poller, or graph node: ask what DELTA its absence would show. If none, CUT / refuse.

[[src-0xcodio-memory-collapse-pointer]]: TAGGER/ROOT/AUDIT/SWEEP memory-collapse writeup — pointer; pair with [[src-0xwast3-ablation-schema]].

## Related

[[loop-graph-engineering]] · [[musk-algorithm]] · [[memory-ablation]] · [[work-per-cost]] · [[raptor-dispatch]] · [[spacexai-grok-bot-keepers]] · [[src-0xwast3-ablation-schema]]
