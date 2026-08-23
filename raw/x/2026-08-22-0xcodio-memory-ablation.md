# Source: 0xCodio on memory ablation

- URL: https://x.com/0xcodio/status/2091122604115394925
- Author: 0xCodio
- Date: 2026-08-22
- Quoted: 0xWast3, "Memory Engineering: The Discipline That Decides Whether Your AI Agent Has a Past" (https://x.com/0xWast3/status/2084625810112032849)

## Tweet

A guy in Seoul deleted 68% of his AI's memory file and the answers got better.

He didn't guess which lines to cut. He made OpenAI grade Claude's memory, one line at a time. He published the harness.

Forty real prompts from his own history. Each run twice - once with the full file, once with a single line pulled out. 104 lines, 4,160 head-to-head comparisons, $1.40 in judging.

The other lab is the part people skip. Ask a model to score its own memory and it defends it. It wrote those lines. It's the author, not the auditor.

The result: 71 of the 104 lines never changed a single answer. Not once, across forty prompts. They rode along on every call he made that month.

Dead on arrival: "prefers concise answers." "Interested in AI and systems." "Likes clean, readable code."

Survived: "ships to production on Thursdays." "Rejected the queue-based version in March, don't re-propose it."

Every line that survived was a fact. Every line that died was an adjective.

Adjectives feel like memory and narrow nothing. A memory line earns its place only by deleting an answer the model would otherwise have given.

## Quoted article claims (0xWast3)

Memory is a system with its own architecture, separate from context and from the model.

Re-reading a full transcript is not memory. It does not scale, does not discriminate, and does not update.

Five stages:

1. Capture. Filter at write time. Keep what would still be true and useful in three months.
2. Consolidate. Merge duplicates. Ten mentions become one confident entry.
3. Retrieve. Surface what is relevant now, not everything stored.
4. Reconcile. Newer facts can supersede, coexist, or flag_conflict. Do not silently guess.
5. Decay. Unused memories lose weight. Archive below a threshold. Do not delete outright.

A memory line that never changes an answer is dead weight.
