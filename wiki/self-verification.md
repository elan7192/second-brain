---
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-24
---

# Self-verification

Generate several candidates. Score them. Keep the winner.

Source: [[src-jacky-self-verification]], [[jacky-kwok]]. Product: [[ultra-mode]], [[src-maverick-ultramode]].

## Reported Terminal-Bench 2.1 result

DeepSeek V4 Flash: sample 5 solutions, rank with the same model as LLM-as-a-Verifier. 79% to 88%. Author says this beat Claude Fable 5 and was about 11x cheaper. Author-reported.

Code: https://github.com/llm-as-a-verifier/llm-as-a-verifier
Paper: arXiv:2607.05391. Official agent impl: https://github.com/llm-as-a-verifier/TurboAgent

## Method

- Fine score scale (1-20, not 1-5)
- Expectation over score-token logprobs
- Repeat the judge and split criteria

[[probabilistic-pivot-tournament]] is the named ranking procedure. [[maverick]] reimplemented it with reasoned pairwise votes and no logprobs. The paper judge uses logprob expectation on a 1-20 scale.

## Second reported slice

[[src-maverick-ultramode]] ran DeepSeek V4 Flash 0731 as agent and verifier on 15 failure-skewed Terminal-Bench tasks, N=5: 24% to 33% overall, 40% to 75% on 4 recoverable tasks. Author estimates +2 to +5 on a full set where the model is already about 83%. See [[contradictions]] C8.

Planning-first best-of-N (pick a plan, execute once) changed 0 of 5 outcomes in that writeup. Do not propose it as the self-verify loop.

[[adversarial-review]] Self-Refine (same model critiques its own single draft) stayed at 77%, equal to zero-shot, on LiveCodeBench. Same-model ranking of N candidates is a different loop. See [[contradictions]] C10.

## Use here

For high-risk wiki claims and architecture answers: write the answer, score it against cited pages, revise if contradicted or missing. See `AGENTS.md` Self-check.

## Related

[[verifiable-instructions]] · [[entropy-gate]] · [[ultra-mode]] · [[adversarial-review]]
