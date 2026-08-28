---
id: concept:claims
type: concept
tags:
  - wiki
created: 2026-08-28
updated: 2026-08-28
---

# Claims

Provenance unit. A page is not a claim.

Source of the model: this vault's 2026-08-28 memory-engine pass. Registry: `wiki/data/claims.yaml`.

## Chain

source → [[claims]] → concept → [[decisions]]

Ask `python3 tools/sb trace claim:…` for the evidence chain. Do not answer "why do we believe X" from page prose alone when a claim id exists.

## Fields

id, subject, predicate, object, confidence, sources, status, valid_from, valid_until, observed_at, superseded_by.

Status is supported, disputed, contradicted, stale, or superseded.

## Related

[[retrieval]] · [[stable-ids]] · [[contradictions]] · [[portable-memory]] · [[memory-ablation]]
