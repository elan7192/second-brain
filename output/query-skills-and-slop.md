---
type: ship
tags:
  - ship
created: 2026-08-24
updated: 2026-08-24
---

# Query · Skills, forgetting, anti-slop

Human asked three things on 2026-08-24. Answer compiled from wiki, not from `raw/`.

## 1. Did the vault record every skill the human inputted?

It recorded Juampi's ranked list of ten anti-slop skills as URLs, then compiled five writing rules into [[anti-slop]] and `AGENTS.md`. The skill repos were not copied into the vault. [[src-juampi-anti-slop-rank]]

The nine ingested sources are the X posts listed on [[index]]. Other posts mention skills as schema ("how we act"), not as a catalog of installed packages. [[context-graph]] [[src-voxyz-verifiable-instructions]]

`MEMORY.md` has no personal skill inventory. Wiki is silent on any Cursor skill files the human may have used outside this ingest.

## 2. How agents use this, and how forgetting is handled

Loop: read [[index]], follow page links, answer from compiled pages, file the answer into `wiki/` or `output/`. [[how-it-works]] [[llm-wiki]] [[tokens-as-capital]]

Facts live on wiki pages with validity windows. How-we-act lives in schema / skills. Give the model the subgraph for this decision, not the dump. [[context-graph]]

Capture is a filter: keep what would still be true in three months. Consolidate duplicates. Retrieve by relevance now. Reconcile or `flag_conflict`. Decay idle lines. Full-transcript replay is a named failure. [[memory-engineering]]

A memory line stays only if deleting it changes an answer. Reported harness: 104 lines, 71 never changed an answer, author cut 68%. Survivors were facts. Dead lines were adjectives. [[memory-ablation]] D3.

Lint: orphans, stale claims, [[contradictions]]. Periodic, not chat replay.

## Named gaps

- Ten upstream skill bodies are not in the repo. If those packages change, this vault still has only the compiled rules on [[anti-slop]].
- Voxyz promised eight paste-ready blocks. They were not retrieved. C6.
- Nine sources so far. [[agent-operating-system]] cites [[src-papa-couch-compiler]] that value shows after roughly 50-100 well-compiled sources. Treat the graph as a seed.

## 3. How slop is reduced

D6: writing follows [[anti-slop]] unless the human asks for another voice.

Compiled rules:

- No em dashes.
- No extra examples the human did not ask for.
- No unsolicited comparisons.
- No "it's not X, it's Y" openings.
- Lead with the answer, then cite.

Check in `AGENTS.md`: the draft has none of the four banned patterns. If the human asked for a comparison or examples, do that and only that.

Wishes in schema do not steer. Every instruction needs a behavior, a check, and a failure path. [[verifiable-instructions]]

High-risk answers: write from the wiki, score against cited pages, revise if contradicted or missing. [[self-verification]]
