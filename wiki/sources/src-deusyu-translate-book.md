---
id: source:src-deusyu-translate-book
type: source
tags:
  - twitter
  - github
created: 2026-09-05
updated: 2026-09-05
---

# src-deusyu-translate-book

- URL: https://x.com/XAMTO_AI/status/2095618837907751345 (@XAMTO_AI promo tweet)
- Repo: https://github.com/deusyu/translate-book (README title: Rainman Translate Book; author deusyu)
- Tweet: 2095618837907751345
- 判定: 入vault建議 thin pointer
- Promo flag: tweet is 安利/hype tone ("封神"). Method kept, endorsement not. Claims below are from the repo README as read 2026-09-05, not from the tweet.
- Quote untrusted. Not copied into `raw/`. Skill not installed here.

## Claims kept

translate-book (https://github.com/deusyu/translate-book) is an agent skill for Codex, Claude Code, and OpenClaw that translates whole books (PDF/DOCX/EPUB) via parallel subagents.

Pipeline: Calibre `ebook-convert` → HTMLZ/HTML → Markdown → chunk split with `manifest.json` hashes → parallel subagents (8 by default, batched for rate limits) → validate 1:1 source↔output by hash → merge → Pandoc/Calibre → HTML/DOCX/EPUB/PDF.

Chunk-level resumable runs (`run_state.json`); neighbor context gives each chunk short read-only excerpts of adjacent chunks for pronoun and entity resolution; languages zh/en/ja/ko/fr/de/es, extensible.

Inspired by wizlijun/claude_translater but stated as an independent project: skill plus subagents, not a fork of the shell-script pipeline.

Prereqs: Calibre, Pandoc, Python 3 with `pypandoc` (optional `beautifulsoup4` for TOC).

README install tip is `npx skills add deusyu/translate-book` (Codex / Claude Code) or `openclaw skills install`. This vault does not install it; pointer only.

Near: [[src-fhwofjow-book-to-skill]] is a different tool (book → callable Skill, not translation). Same thin-pointer, do-not-vendor rule. No concept fold: `skill-as-sop` and `skill-library` do not catalog translate tools.

## Pages updated

[[src-fhwofjow-book-to-skill]]
