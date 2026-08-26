---
type: concept
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-27
---

# Stale fact detector

Audit compiled wiki claims against named sources. Internally consistent notes can still be dead.

Source: [[src-botdirectory-picks-2026-08-27]] (gap 4, owner Vault). Skill file: `stale-fact-detector`.

## When

lan E or Product asks to audit a vault topic, or doubts a number.

## Sequence

1. Load the named notes.
2. Extract factual claims.
3. Check against the trusted-source list they named.
4. Flag stale items with evidence and file paths.
5. Propose exact replacement sentences.

## Rules

- Quote the note and the newer source, with dates.
- Freshness report. No file writes in the same pass as the audit.
- A wiki patch may be drafted after. Push still needs PM / lan E.
- `raw/` is immutable.
- If the trusted source is silent, mark unverifiable. Do not update from model memory.
- Sensitive topics are off-limits.

## Related

[[llm-wiki]] · [[memory-ablation]] · [[verifiable-instructions]] · [[botdirectory-scan]]
