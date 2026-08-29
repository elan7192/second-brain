---
id: concept:claims
type: concept
schema: memory-v1
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-29
created_by: agent
confidence: medium
source:
  - wiki/file-memory.md
  - wiki/retrieval.md
  - wiki/contradictions.md
derived_from:
  - file-memory
  - retrieval
  - contradictions
---

# Claims

Provenance unit. A page is not a claim. Two registries exist. Do not pick one. See C17.

## FACT

`wiki/data/claims.yaml` is the subject / predicate / object registry used by `python3 tools/sb trace`. Fields: id, subject, predicate, object, confidence, sources, status, valid_from, valid_until, observed_at, superseded_by. Status is supported, disputed, contradicted, stale, or superseded.

`wiki/claims.csv` is a compile of source `## Claims kept` plus [[curated-claims]]. Columns: claim_id, kind (fact / inference / opinion), status (active / deprecated / disputed / unknown), confidence, text, source, raw, url, created_at, updated_at, created_by, derived_from, pages. Rebuild with `python3 tools/compile-claims.py`. Do not hand-edit.

[[contradictions]] stays the prose ledger. Machine form: `wiki/data/contradictions.yaml`. CSV disputed rows must cite a `C#` in `pages`. Example: [[ngc]] C9 rows `c-ngc-mmlu-table1` and `c-ngc-mmlu-table3`.

## INFERENCE

Both tables can describe the same source sentence. Until C17 is resolved, cite the id you used and do not treat the other table as absent.

## OPINION

Keep both until a human names one canonical store. Do not add a vector index to replace either. See [[file-memory]] and D9.

## Check

`python3 tools/sb validate` exits 0. Rebuild the CSV with `python3 tools/compile-claims.py` if stale.

If a statement cannot be tied to a source page: leave it out of both tables.

## Related

[[provenance]] · [[epistemic-labels]] · [[contradictions]] · [[untrusted-ingest]] · [[file-memory]] · [[stale-fact-detector]] · [[retrieval]] · [[stable-ids]] · [[memory-system]] · [[portable-memory]] · [[memory-ablation]]
