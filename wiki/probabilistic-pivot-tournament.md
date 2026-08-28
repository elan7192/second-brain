---
id: concept:probabilistic-pivot-tournament
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-24
---

# Probabilistic Pivot Tournament

The ranking step in [[src-maverick-ultramode]]. Named in the tweet as the verifier that picks a winning diff. Reimplemented from [[jacky-kwok]] LLM-as-a-Verifier (arXiv:2607.05391).

## Steps in the product

From the [[ultra-mode]] README:

1. Ring pass. Each diff judged once against a neighbour. Seed pivots.
2. Pivot duels. The field against the top pivots. K reasoned votes per duel.
3. Score. Normalised win-rate. Confidence = top1 minus top2.

Used to pick among N isolated worktree diffs. See [[entropy-gate]].

## Paper vs this reimplementation

[[self-verification]] from Jacky's posts: fine score scale (1-20), expectation over score-token logprobs, repeated evaluation and criteria split.

[[maverick]] adaptation: reasoned pairwise votes, no logprobs, no separate verifier model. Confidence-gated apply and isolated git worktrees sit on top.

Author says the official paper-faithful implementation is TurboAgent: https://github.com/llm-as-a-verifier/TurboAgent. Use that for numbers that claim to match the paper.

## Related

[[ultra-mode]] · [[self-verification]] · [[src-maverick-ultramode]] · [[src-jacky-self-verification]]
