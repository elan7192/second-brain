# Second brain schema

This repo is a compiled LLM wiki, not a chat log and not a filing cabinet.
You maintain `wiki/`. The human curates `raw/` and asks questions.

Read this file, then `wiki/index.md`, then only the pages the index points to.

## Layout

| Path | Owner | Rule |
| --- | --- | --- |
| `raw/` | human | Immutable. Read only. Never edit, move, or rename. |
| `wiki/` | agent | Compiled pages. One topic per file. Update on every ingest. |
| `wiki/index.md` | agent | Catalog. Read this before answering. |
| `wiki/log.md` | agent | Append-only timeline. Prefix every entry with `## [YYYY-MM-DD] kind \| title`. |
| `output/` | agent | Answers and briefs built from `wiki/`, never from raw memory. |
| `MEMORY.md` | both | Durable facts only. A line stays if deleting it would change an answer. |
| `decisions.md` | both | Locked choices. Do not reopen without new evidence. |
| `AGENTS.md` / `CLAUDE.md` | both | This schema. Keep them identical. |
| `maps/` `hunt/` `ship/` | agent | Obsidian navigation. Do not copy wiki prose into them. |
| `.obsidian/` | both | Vault settings. Keep graph color groups. |

## Query

1. Read `wiki/index.md`.
2. Open the linked pages. Follow `[[wikilinks]]`.
3. Answer from compiled pages. Cite those pages.
4. If the wiki is silent, say so. Do not invent. Ask to ingest a source or search the web.
5. Do not read `raw/` unless the human asked for the original, or a wiki page is missing and you are ingesting.
6. File a useful answer back into `wiki/` or `output/` so the next session does not re-derive it.
7. For object/link questions, read `output/ontology.json` or run `python3 tools/ontology.py`. Rebuild first if `--check` fails.

Check: every claim in the answer has a wiki citation, or is marked `unverified`.
If evidence is missing: stop and name the gap. Do not fill it with tone.

## Ingest

When the human drops files in `raw/` and says ingest:

1. Read the new raw file. Do not edit it.
2. Write or update a source page in `wiki/sources/`.
3. Write or update concept and people pages the source actually changes.
4. Link both ways with `[[wikilinks]]`.
5. Flag contradictions on the pages and on `wiki/contradictions.md`.
6. Update `wiki/index.md`.
7. Append `wiki/log.md`.
8. Write a three-sentence brief in `output/` of what changed, what linked, and what the human should look at.

Check: `python3 tools/lint-wiki.py` exits 0. Every new page has an inbound `[[wikilink]]`.
Then `python3 tools/rebuild-ontology.py` and `python3 tools/rebuild-ontology.py --check` exits 0.
If a claim cannot be tied to the raw file: leave it out.

## Ontology rebuild

`output/ontology-objects.csv` is a derived Palantir-style object table. Wiki markdown stays the store. No live Foundry or AIP objects.

1. After ingest or a structural wiki edit, run `python3 tools/rebuild-ontology.py`.
2. Check: `python3 tools/rebuild-ontology.py --check` exits 0.
3. If the check fails: rebuild from wiki. Do not edit the CSV by hand. If Foundry credentials are missing: keep the local ontology. Do not create a Palantir account (D5).

Check: lint-wiki 0 and rebuild-ontology --check 0.
If the CSV and wiki disagree: wiki wins.

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
