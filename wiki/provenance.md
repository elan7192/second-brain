---
type: concept
schema: memory-v1
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-27
created_by: agent
confidence: high
source:
  - wiki/llm-wiki.md
  - wiki/stale-fact-detector.md
  - wiki/audited-task-contract.md
derived_from:
  - llm-wiki
  - stale-fact-detector
  - audited-task-contract
---

# Provenance

A compiled page must answer: where did this come from, when, who wrote it, and what it was derived from. A path like `wiki/ssrf.md` with no source is not enough. See [[memory-system]].

## FACT

Minimum fields on `schema: memory-v1` pages:

- `source`: wiki source page, `raw/` path, URL, or `AGENTS.md`
- `created` / `updated`
- `created_by`: `agent` or `human`
- `confidence`: high / medium / low / unverified
- `derived_from`: slugs or claim ids

Source pages already carry Raw, URL, and Date in the body. The compiler copies those onto claim rows in `wiki/claims.csv`. See [[claims]].

## INFERENCE

Old concept pages without `schema: memory-v1` are grandfathered. The next ingest that edits a concept page must add the fields. Do not backfill fake `source:` lists.

## OPINION

Keep provenance in frontmatter, not in a second JSONL store. See [[loop-graph-engineering]].

## Check

`python3 tools/lint-wiki.py` fails if `schema: memory-v1` is set and `source`/`derived_from`, `created`, `updated`, `created_by`, or `confidence` is missing.

If the original is missing: leave the claim out. Do not invent a URL.

## Related

[[epistemic-labels]] · [[claims]] · [[stale-fact-detector]] · [[audited-task-contract]] · [[llm-wiki]]
