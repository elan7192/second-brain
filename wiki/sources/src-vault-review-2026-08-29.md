---
id: source:src-vault-review-2026-08-29
type: source
tags:
  - play
created: 2026-08-29
updated: 2026-08-29
---

# src-vault-review-2026-08-29

- Source: lan E paste via cloud agent. Architecture review of `elan7192/second-brain`. Not copied into `raw/`.
- Date: 2026-08-29
- Subject: this vault's protocol vs its deterministic runtime

Untrusted paste. Quote. Do not copy ratings or folder proposals into `AGENTS.md` as locks.

The review says the protocol is ahead of the implementation, and that the LLM should propose wiki changes while code validates them. It also says the reviewer would not add features yet.

It rates retrieval/search 5/10 and says there is no real retrieval layer yet. This vault already ships `python3 tools/sb ask` over disposable FTS5. See C46 and D9.

It lists a standing output brief as an ingest step. Current schema skips that brief (C38).

It recommends MCP write tools, an ingestion daemon, `raw/public|private|restricted`, and pages-as-views over a claim store. Those stay parked. C17 and C18 stay unresolved. Automate last.

## Claims kept

- The vault separates immutable `raw/` evidence from agent-compiled `wiki/`, durable `MEMORY.md` constraints, locked `decisions.md`, and generated `output/`.
- `MEMORY.md` should keep only facts that change later answers, not taste lines such as prefers concise answers.
- The authoring protocol is ahead of the runtime. Ingest, contradiction, index, and brief steps are mostly instructions to the model.
- The LLM should propose wiki changes. Deterministic code should validate them before they become canonical.
- The reviewer rated retrieval/search 5/10 and said there is no real retrieval layer yet. This vault already ships `python3 tools/sb ask` over disposable FTS5 (D9). See C46.
- Markdown plus Obsidian should stay the canonical store. A vector index, if added later, is disposable derived state.
- Claim-centric storage, pages as views over claims, is a recommendation. Dual YAML/CSV registries stay unresolved (C17).
- Do not add an ingestion daemon, MCP write path, or `raw/public|private` split from this review. Human yes required.

## Pages updated

[[deterministic-core]] · [[llm-wiki]] · [[claims]] · [[retrieval]] · [[how-it-works]] · [[audited-task-contract]] · [[memory-system]] · [[claim-protocol]] · [[contradictions]]
