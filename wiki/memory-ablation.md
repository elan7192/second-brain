# Memory ablation

A memory line earns its place only by deleting an answer the model would otherwise give.

Source: [[src-0xcodio-memory-ablation]].

## Reported harness

- 40 real prompts from one person's history
- 104 memory lines
- Each prompt twice: full file vs one line removed
- 4,160 pairwise judgments
- $1.40 in judging
- A second model graded. The author model was not the auditor

Result: 71 of 104 lines never changed an answer. Author reports cutting 68% and getting better answers.

## Dead vs alive

Dead: "prefers concise answers." "Interested in AI and systems." "Likes clean, readable code."

Alive: "ships to production on Thursdays." "Rejected the queue-based version in March, don't re-propose it."

Every survivor was a fact. Every dead line was an adjective.

## Lab note

Do not ask a model to score memory it wrote. It defends its own prose.

## Related

[[memory-engineering]] · `MEMORY.md` · [[verifiable-instructions]]
