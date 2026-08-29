---
id: concept:project-skill-stack
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-24
---

# Project skill stack

Projects hold context. Skills hold how the model acts.

Source: [[src-alexprompter-claude-projects]].

## Split

Projects are containers: files, instructions, decisions for one piece of work.

Skills are capabilities the model can call. Stack them. The project supplies context. The skill supplies method.

Same split as [[context-graph]]: graph is what is true, skills or schema are how we act.

## Claude product stack

Tweet-reported, not verified against Anthropic docs:

1. Global memory (account-level)
2. User-provided context files
3. Project instructions and files
4. Skills
5. Current prompt

Suggested folders in that tweet: `/reference`, `/analysis`, `/deliverables`. Those are not this vault's layout. See [[contradictions]] C42.

Cowork is named as the long-running execution surface. Product-only.

## What this tweet does not prove

No paper. GIF unread. Docs cited, not re-read. Do not treat Claude Projects as [[llm-wiki]]. Do not replace `raw/` + `wiki/` with a product workspace.

## Related

[[context-graph]] · [[memory-engineering]] · [[llm-wiki]] · [[src-chatchat-living-brain]]
