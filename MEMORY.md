---
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-24
---

# Memory

Durable facts only. A line stays if deleting it would change an answer.
Adjectives and taste notes do not belong here. See [[memory-ablation]].

## Vault

- This repo is a compiled LLM wiki. Answer from `wiki/` first. Do not re-read `raw/` to answer a normal question.
- `raw/` is immutable. Never edit it.
- `decisions.md` is locked. Do not reopen a decision without new evidence.
- The vault does not post, pay, send, or deploy.
- Graph view and `tools/render-obsidian-graph.py` cluster by the five [[agent-operating-system]] layers. Do not place all wiki notes on one ring around Home. Filter excludes `raw/`, `templates/`, `index`, `log`, and `twitter`.
- Wiki agent must stay current on compiled `wiki/` pages. Other agents send improvement facts here; ingest them. Do not invent gaps.
- When GitHub updates this vault, pull the clone, lint, and stay current on `wiki/`.

## arXiv tierlist

- Ranking axis is future potential / runway, not citations or journal prestige. See [[arxiv-tierlist]] and [[potential-ranking]].
- Website display is per-tier top 800 (4000 cards), not a global top-N.
- Corpus 2026-08-24: 405856 unique. Tiers S 16443 / A 42228 / B 197545 / C 113767 / D 35873. Inventory only. See [[arxiv-tierlist]].
- Current public site is https://elan7192.github.io/arxiv-potential-tierlist/ (repo https://github.com/elan7192/arxiv-potential-tierlist). ZeroDeploy URLs are stale. Do not treat them as current.
- Never store ZeroDeploy or other deploy claim tokens in wiki, MEMORY, or chat.
- A selected paper must be digested into concept/source pages. Do not ingest counts-only or dump titles. Wiki does not harvest papers.
- Findings with substance go into wiki. arxiv must read a paper before sending it. Wiki does not harvest at random.
- Harvest stopped 2026-08-24. Do not ingest further count bumps. Only ingest when arxiv sends a read-paper digest. Counts-only is not knowledge.
- Known compiled papers (2026-08-24): TRACE plus BATCH01–09. Open contradictions C9–C14. Unread tables/figs not known. Do not treat the 405856 inventory as known.
- 2026-08-24: ChatGPT share `t_6a8cc267d5c08191942d394ac016763c` claimed `second-brain-upgraded-2026-08-25.zip` (100 papers 5×20, 9 skills, 25/25 memory tests, 0 lint errors) and said it was not pushed. Public download returned 401/403. Do not treat those 100 papers or 9 skills as known. Do not reconstruct or merge the ZIP from the claim list. Harvest remains digest-only. See [[src-chatgpt-t-6a8cc267]] and C14.

## LanBB

- The bounty/flow product is named LanBB. semantica is a tool inside it, not the project name.
- 2026-08-24: new repo https://github.com/elan7192/LanBB (main). semantica is submodule tools/semantica @ 6c2ccfd. Do not rename semantica-agi/semantica or elan7192/semantica. See [[lanbb]].

## Open questions

- No personal identity or goals have been captured yet. Do not invent them.
