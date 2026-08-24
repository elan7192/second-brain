---
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-24
---

# Adversarial review

Three agents. A writer, a reviewer, and a critic of the review. The artifact stays frozen until the review converges.

Source: [[src-omarsar-adversarial-review]], [[elvis]]. Paper: Qiu and Gill, arXiv:2608.18167.

## Loop

1. Main agent M writes artifact version N (code or plan) plus a change log.
2. Inner loop: reviewer R writes a review. Critic C audits that review. R may revise. Artifact is not edited. Cap 5 inner rounds.
3. First-pass accept if they converge immediately and find no flaws.
4. Else M edits to version N+1 and the inner loop runs again.

The tweet's rule: cooperative review works when disagreement is minimal, structured, and evidence-grounded.

## LiveCodeBench table

Claude Sonnet 4.5 Medium Reasoning. 105 stdin tasks, 57 hard. Author-reported.

| Method | pass / 105 | hard / 57 | agents |
| --- | --- | --- | --- |
| Zero-shot | 77% | 35 | 1 |
| Self-Refine | 77% | 35 | 1 |
| Single-reviewer | 77% | 36 | 2 |
| Two-reviewers | 75% | 34 | 3 |
| MARS | 82% | 39 | 5 |
| AR | 87% | 43 | 3 |

The five-agent baseline in the tweet is MARS.

Self-Refine stays at 77%. Same model critiques its own single draft. See [[contradictions]] C10.

## SWE-PRBench

N=100. Naive AR F1 0.457, lowest in the subset. Agents agreed without enough evidence.

Text constraint: critic must pick AGREE, DISAGREE_EVIDENCE, or DISAGREE_CONCERN. F1 0.533, highest in the subset.

## SWE-bench Verified

Abstract: AR improves over baselines. Paper table, Claude Code SKILL.md form, N=500: AR 75.2%, MARS 72.6%, Zero-shot 71.6%. About 4.5x the tokens of Zero-shot. Helps when disagreement finds the root cause. Hurts when it expands scope.

## Related

[[entropy-gate]] · [[audited-task-contract]] · [[self-verification]]
