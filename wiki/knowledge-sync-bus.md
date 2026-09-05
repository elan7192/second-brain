---
id: concept:knowledge-sync-bus
type: concept
schema: memory-v1
tags:
  - wiki
created: 2026-09-05
updated: 2026-09-05
created_by: agent
confidence: high
source:
  - wiki/sources/src-cos-knowledge-sync-bus-2026-09-05.md
derived_from:
  - src-cos-knowledge-sync-bus-2026-09-05
  - raptor-dispatch
  - spacexai-grok-bot-keepers
---

# Knowledge sync bus

Specialist → **CoS last look** → **Vault** writes `wiki/sources` (and folds). Vault never invents. Source: [[src-cos-knowledge-sync-bus-2026-09-05]]. Skill: vault-knowledge-sync.

## FACT

| Seat | When | Vault action |
| --- | --- | --- |
| X Scout | 入vault建議 / 只記一筆 / 跳過但仍記 | src (+ skip reason if skip) |
| Researchy | Durable research brief or fact pack | src or fold into existing note |
| Fill | Quota find worth keeping | src pointer |
| Engineer | Method/playbook (not code) | skill and/or vault fold via CoS |
| Competitor Watch / last30days / SEO & AEO | Only if CoS says durable | src |
| Parked seats | Idle until CoS named job | no sync |

Ephemeral chat, hype, NSFW, pure ads → skip仍記 or no file (CoS decides).

User-pasted X status triage is X Scout. Vault files only packets CoS forwards.

## Skip仍記一行

Must include: source URL, one-line why skipped, judgment date. Never blank.

## Merge

Routine src/skip pointer PRs: `python3 tools/sb validate` PASS → auto-merge. Exceptions (schema change, mass delete, uncertain): Hold and report CoS.

## CoS packet

Verdict, URL(s), suggested `src-*.md` name, 1–5 line summary, fold targets if any. One PR when packing several. Dedup before new src.

## INFERENCE

Same outer loop as [[raptor-dispatch]] / [[spacexai-grok-bot-keepers]]: CoS owns return path; Vault is one writer for the knowledge graph. derived_from: raptor-dispatch, spacexai-grok-bot-keepers.

## Check

If a specialist asks Vault to ingest without a CoS packet: refuse and point them to CoS. If skip page lacks URL or reason or date: reject. If validate fails: do not auto-merge.

## Related

[[raptor-dispatch]] · [[spacexai-grok-bot-keepers]] · [[src-cos-knowledge-sync-bus-2026-09-05]] · [[src-adiix-grok-bot-org]]
