# Source: Elvis on Adversarial Review

- URL: https://x.com/omarsar0/status/2091631620025647184
- Author: omarsar0 (elvis). Founder of dair.ai. Summarizing, not a paper author.
- Date: 2026-08-23
- Paper: https://arxiv.org/abs/2608.18167
- Paper title: Adversarial Review: Structured Disagreement for Grounded Agentic Code Review
- Paper authors: Eric S. Qiu (Cornell), Joyce Gill (Stanford)

## Tweet

Great paper on multi-agent systems for code review.

It's challenging to know how many coding agents to use to address a problem.

The default fix for weak agentic code review is more agents. Scaling agents to a large number gives diminishing returns on repository-level tasks.

This new work tries structured conflict instead. Adversarial Review runs three agents. A main coding agent writes, a reviewer evaluates, and a critic audits the review before any edits are done.

On LiveCodeBench it beats a five-agent baseline while using three agents.

On SWE-PRBench the naive version exposed a failure mode. The agents converged on agreement without enough evidence behind it. Making disagreement an explicit instruction recovered the highest F1 among tested methods.

They also find that cooperative review works when the disagreement is minimal, structured, and grounded in evidence.

Paper: https://arxiv.org/abs/2608.18167

## Paper claims the tweet points at

Abstract matches the tweet: reviewer evaluates, critic audits the review through structured disagreement before the main agent edits. LiveCodeBench highest pass rate among tested methods, beating a five-agent baseline with three agents. SWE-PRBench naive AR false-consensus; one prompt iteration that adds disagreement explicitly achieves the highest F1. Cooperative review requires disagreement that is minimal, structured, and evidence-grounded.

Figure 1 / method: inner loop freezes the artifact. Reviewer and critic exchange review text only. Main agent edits only in the outer loop. First-pass accept if they converge immediately and find no flaws. Inner cap 5 rounds.

LiveCodeBench, Claude Sonnet 4.5 Medium Reasoning, 105 stdin tasks (57 hard). Table 1:

| Method | pass / 105 | pass-on-hard / 57 | # agents |
| --- | --- | --- | --- |
| Zero-shot | 77% | 35/57 | 1 |
| Self-Refine | 77% | 35/57 | 1 |
| Single-reviewer | 77% | 36/57 | 2 |
| Two-reviewers | 75% | 34/57 | 3 |
| MARS | 82% | 39/57 | 5 |
| AR | 87% | 43/57 | 3 |

Self-Refine stays at 77% because critic and generator are the same model.

Five-agent baseline is MARS (author, three reviewers, meta-reviewer).

SWE-PRBench, N=100, GPT-5.2 judge vs human PR comments, Cohen's kappa 0.75. Table 2:

| Method | F1 |
| --- | --- |
| AR with text constraint | 0.533 |
| Two-reviewers | 0.503 |
| MARS | 0.501 |
| Single-reviewer | 0.495 |
| Naive AR | 0.457 |

Naive failure modes: over-decomposition (thin speculative flags) and critic yielding to a weak rebuttal (false agreement).

Text constraint: critic chooses AGREE, DISAGREE_EVIDENCE (cite contradicting code), or DISAGREE_CONCERN. Reviewer must cite code to keep or drop a flag on DISAGREE_CONCERN.

Abstract also: SWE-bench Verified improvements. Paper Table 3, Claude Code skills form, N=500: AR 75.2%, MARS 72.6%, Zero-shot 71.6%. AR uses about 4.5x the tokens of Zero-shot. Helps when disagreement finds the root cause. Hurts when disagreement expands scope.

Model for LCB and SWE-PRBench tables: Claude Sonnet 4.5 Medium Reasoning. SWE-bench Verified: Claude Code following SKILL.md.
