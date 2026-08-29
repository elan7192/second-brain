---
id: concept:tokens-as-capital
type: concept
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-29
---

# Tokens as capital

Treat a token as an investment, not a per-query bill.

[[src-papa-couch-compiler]] cites 305,000 vs 47,000 tokens for the same task. The difference is whether the system already compiled the knowledge. Projected 30-day savings in that post: 54% to 81%, depending on topic concentration. Treat the exact percents as author-reported, not independently audited.

## Rules that follow

1. Pay understanding cost at ingest, not at every question.
2. Write good answers into synthesis pages.
3. Fold web search into entity pages. Do not let it vanish in chat.
4. Build `output/` from `wiki/`, not from a raw dump.
5. If live bot token usage is an issue, ask the chief of staff: `anyway we can improve token usage? thoughts?` See [[src-debs-obrien-token-usage]] and [[bot-voice]].
6. Compile instruction files and working notes. [[src-dair-agent-friendly-docs]] found those artefacts take most of an agent's documentation attention. API references take 1.3%. See [[agent-facing-docs]].

[[src-johnsjawn-skill-library]] makes the same bet as write-back: discover a research skill instead of rebuilding it. The "50 times" figure is author-stated, unverified. See [[skill-library]].

[[src-mukul975-cybersecurity-skills]] claims about 30 tokens to scan a skill frontmatter and 500-2000 tokens to load the body. Author-stated. The vault still compiles claims here instead of loading that pack.

[[src-skill-pack-list]] says a skill SOP stops the agent from retrying a known failure and burning tokens. Compile the SOP. Do not buy that claim by installing a marketplace. See [[skill-as-sop]].

[[src-retrieval-second-brain]] spends tokens at query time (search, rerank, reflect, search again). This vault spends them at ingest. See [[retrieval-second-brain]].

## Ad-hoc dumps are a different bill

[[src-jerry-two-pass-docs]] amortizes a data room by a cheap first pass and an expensive just-in-time VLM on the retrieved pages. Spend VLM tokens on the retrieved subset. See [[two-pass-document-processing]] and [[contradictions]] C44.

## Related

[[llm-wiki]] · [[context-graph]] · [[src-papa-couch-compiler]] · [[src-jerry-two-pass-docs]] · [[skill-library]] · [[skill-as-sop]] · [[retrieval-second-brain]] · [[src-mukul975-cybersecurity-skills]] · [[trace]] · [[bot-voice]] · [[src-debs-obrien-token-usage]] · [[context-compaction]] · [[work-per-cost]] · [[agent-facing-docs]] · [[flat-context]]

[[trace]] paper: one-pass attribution is 16x fewer LLM calls than iterative per-node. Tweet 4.2x token cut is `unverified`.

[[src-avichawla-trueforge]] 2.7x is agent-harness runtime tokens, not wiki compile tokens. Do not mix with 305k vs 47k. See [[flat-context]] and [[contradictions]] C41.
