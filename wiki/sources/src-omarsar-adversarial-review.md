---
type: source
tags:
  - twitter
created: 2026-08-24
updated: 2026-08-24
---

# src-omarsar-adversarial-review

- Raw: [[2026-08-23-omarsar-adversarial-review]] (`raw/x/2026-08-23-omarsar-adversarial-review.md`)
- URL: https://x.com/omarsar0/status/2091631620025647184
- Date: 2026-08-23
- Paper: https://arxiv.org/abs/2608.18167 (Qiu and Gill)

## Claims kept

Adding more agents is the default fix for weak review. The paper reports diminishing returns on repository-level tasks.

[[adversarial-review]] uses three agents. Writer. Reviewer. Critic of the review. Artifact stays frozen until the review converges.

LiveCodeBench: AR 87% with 3 agents. MARS 82% with 5. First four methods cluster at 75% to 77%. Self-Refine equals zero-shot at 77%.

SWE-PRBench: naive AR F1 0.457 (false consensus). Explicit disagreement types: F1 0.533, highest in the subset.

Cooperative review works when disagreement is minimal, structured, and evidence-grounded.

## Pages updated

[[adversarial-review]] · [[entropy-gate]] · [[audited-task-contract]] · [[self-verification]] · [[elvis]] · [[contradictions]]
