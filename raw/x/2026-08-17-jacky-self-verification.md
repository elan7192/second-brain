# Source: Jacky Kwok on self-verification scaling

- URL: https://x.com/jackyk02/status/2089421448784023553
- Author: jackyk02 (Jacky Kwok)
- Date: 2026-08-17
- Code: https://github.com/llm-as-a-verifier/llm-as-a-verifier#self-verification-terminal-bench-21
- Quoted earlier post: LLM-as-a-Verifier (https://x.com/jackyk02/status/2074969820739805275)

## Tweet

Scaling self-verification with DeepSeek V4 Flash beats Claude Fable 5 on Terminal-Bench 2.1, while being 11x cheaper.

Open-source models can generate many candidate solutions and verify their own outputs at low cost.

Sampling 5 solutions with DeepSeek V4 Flash and ranking them with the same model as LLM-as-a-Verifier: 79% to 88% on Terminal-Bench, beating closed frontier models in the reported comparison.

## Earlier method claims

LLM-as-a-Verifier:

- Fine-grained score scale (for example 1-20, not 1-5).
- Expectation over the full logprob distribution of score tokens.
- Repeated evaluation and criteria decomposition.

Reported use: test-time scaling, RL, agent monitoring. Claimed SOTA on Terminal-Bench V2, SWE-Bench Verified, RoboRewardBench, MedAgentBench in the author's posts.
