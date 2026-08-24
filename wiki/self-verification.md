---
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-23
---

# Self-verification

Generate several candidates. Score them. Keep the winner.

Source: [[src-jacky-self-verification]], [[jacky-kwok]].

## Reported Terminal-Bench 2.1 result

DeepSeek V4 Flash: sample 5 solutions, rank with the same model as LLM-as-a-Verifier. 79% to 88%. Author says this beat Claude Fable 5 and was about 11x cheaper. Author-reported.

Code: https://github.com/llm-as-a-verifier/llm-as-a-verifier

## Method

- Fine score scale (1-20, not 1-5)
- Expectation over score-token logprobs
- Repeat the judge and split criteria

## Use here

For high-risk wiki claims and architecture answers: write the answer, score it against cited pages, revise if contradicted or missing. See `AGENTS.md` Self-check.

## Related

[[verifiable-instructions]] · [[entropy-gate]]

Related later source: [[evosyn]] synthesizes executable tests; not the same as sampling several answers.
