# Second brain schema

This repo is a compiled LLM wiki, not a chat log and not a filing cabinet.
You maintain `wiki/`. The human curates `raw/` and asks questions.

Read this file, then `wiki/index.md`, then only the pages the index points to.

## Layout

| Path | Owner | Rule |
| --- | --- | --- |
| `raw/` | human | Immutable. Read only. Never edit, move, or rename. |
| `wiki/` | agent | Compiled pages. One topic per file. Update on every ingest. |
| `wiki/claims.csv` | agent | Claim ledger. Source plus evidence required. |
| `wiki/index.md` | agent | Catalog. Read this before answering. |
| `wiki/log.md` | agent | Append-only timeline. Prefix every entry with `## [YYYY-MM-DD] kind \| title`. |
| `output/` | agent | Answers and briefs built from `wiki/`, never from raw memory. |
| `MEMORY.md` | both | Durable facts only. A line stays if deleting it would change an answer. |
| `decisions.md` | both | Locked choices. Do not reopen without new evidence. |
| `AGENTS.md` / `CLAUDE.md` | both | This schema. Keep them identical. |
| `maps/` `hunt/` `ship/` | agent | Obsidian navigation. Do not copy wiki prose into them. |
| `.obsidian/` | both | Vault settings. Keep graph color groups. |

## Query

1. Run `python3 tools/retrieve.py "<question>"`.
2. Read `wiki/index.md` and the ranked pages.
3. Follow `[[wikilinks]]` from those pages. Do not dump the vault.
4. Answer from compiled pages. Cite those pages and claim ids from `wiki/claims.csv`.
5. If the wiki is silent, say so. Do not invent. Ask to ingest a source or search the web.
6. Do not read `raw/` unless the human asked for the original, or a wiki page is missing and you are ingesting.
7. File a useful answer back into `wiki/` or `output/` so the next session does not re-derive it.

Check: every claim in the answer has a wiki citation or a claim id, or is marked `unverified`.
If evidence is missing: stop and name the gap. Do not fill it with tone.
If retrieve exits 1: say the wiki had no hit. Do not widen the dump.

## Ingest

When the human drops files in `raw/` and says ingest:

1. Read the new raw file. Do not edit it.
2. Append rows to `wiki/claims.csv` with source, evidence location, and status.
3. Write or update a source page in `wiki/sources/`.
4. Write or update concept and people pages from `verified` claims, or from `unverified` claims marked as such in prose.
5. Link both ways with `[[wikilinks]]`.
6. Flag contradictions on the pages and on `wiki/contradictions.md`. Put `contradicted` rows in the CSV.
7. Update `wiki/index.md`.
8. Append `wiki/log.md`.
9. Write a three-sentence brief in `output/` of what changed, what linked, and what the human should look at.

Check: `python3 tools/lint-wiki.py` exits 0. Every claims.csv row has source and evidence. Every new page has an inbound `[[wikilink]]`.
If a claim cannot be tied to the raw file: leave it out of both CSV and wiki.

## Claim protocol

Compile and answer through Claim → Evidence → Verification → Retrieval → Context → Answer. Do not add extra knowledge folders. Git markdown stays canonical. SQLite FTS5 is disposable. No vector DB. No second graph store.

Behavior: ingest writes `wiki/claims.csv` before wiki prose. Query runs `python3 tools/retrieve.py`. Wiki and `MEMORY.md` promote `verified` rows only, except `unverified` rows that stay marked `unverified`.

Check: `python3 tools/lint-wiki.py` exits 0. `python3 tools/retrieve.py` returns existing wiki pages. A new `MEMORY.md` line names a verified claim id or a source page.

If evidence is missing: status `unverified`. Do not write it into `MEMORY.md`. If retrieve and index disagree, trust the markdown and rebuild the index.

## Memory

`MEMORY.md` and schema rules take only facts that delete an answer the model would otherwise give.

Keep: "Rejected the queue-based design in March. Do not re-propose it."
Drop: "prefers concise answers", "interested in AI", "likes clean code".

Check: each `MEMORY.md` line names a concrete constraint, date, decision, or rejection.
If you cannot state the answer it prevents: do not write the line.

## Verifiable instructions

Do not add wishes ("never hallucinate", "be careful", "you are a senior engineer").
Every new rule in this file must state:

1. The behavior that must change.
2. How to check that it changed.
3. What to do when evidence is missing or the check fails.

Check: a new bullet has those three parts, or it does not land.
If you only have a preference: put it in a source page, not in the schema.

## Writing

Default voice is anti-slop.

- No em dashes.
- No extra examples the human did not ask for.
- No "it's not X, it's Y" openings.
- No unsolicited comparisons.
- Lead with the answer, then cite.

Check: the draft has none of the four banned patterns.
If the human asked for a comparison or examples: do that, and only that.

## Multi-agent work

Agents do not share chat. They share an audited contract.

A contract may contain: objective, acceptance checks, write scope, accepted commit, decisions with evidence, failed approaches, blockers, phase, `state_version`.
A contract may not contain: full transcripts, secrets, raw tool dumps, adjectives.

Executors write candidate worktrees. An auditor with fresh context checks the contract. Only then does state advance.

If several agents run: isolated worktrees, structured diffs only, an objective gate (tests, lint, wiki link check) outside the model. Unverified peer claims do not enter `wiki/` or `MEMORY.md`.

Check: a new durable claim has a source page or a passing gate.
If two agents disagree: `flag_conflict` on `wiki/contradictions.md`. Do not silently pick a side.

## Self-check

For a high-risk answer (architecture, a reversal of a locked decision, a numeric claim):

1. Produce the answer from the wiki.
2. Score it against the cited pages (supported / contradicted / missing).
3. If contradicted or missing, revise or mark `unverified`.

Check: numeric or "always/never" claims quote a source page.
If the source is a viral demo with no method: mark it `unverified` and prefer the calmer article underneath.

## Growth operator

When the human asks to run GrowthOS, brief a partner, or open the growth vault:

1. Read `growth/growth-core.md`, then only the pages it points to.
2. Answer from those pages. File the briefing in `output/` with `python3 tools/growth-brief.py`.
3. Do not post, pay, send, create live Whop objects, or treat DEMO notes as real deals.

Check: every claim in the briefing cites a `growth/` page or is marked `unverified`.
If a DEMO note is the only source: say DEMO. If the vault is silent: stop and name the gap.

## Human authority

This vault does not post, pay, send, or deploy.
Destructive git, production access, and permission expansion stop for an explicit yes.
