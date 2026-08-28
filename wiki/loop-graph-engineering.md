---
type: concept
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-28
---

# Loop and graph engineering

Failures are no owner of the return path, shared state, and a broken approval boundary. Not a weak model.

Source: [[src-av1dlive-loop-graph-2026-08-26]]. lan E share. Article not dumped.

## Useful loop

Owner + worker + verifier + stop rule.

## Three stores. Do not mix

- Knowledge graph: source-backed claims.
- DAG: order.
- `state.json`: progress.

One writer for the authoritative graph. Others propose.

## Harness bridge

File bridge between harnesses. No native Grok Bot to Kimi handoff. Author says undocumented.

Nested harness gap: outer approval does not see inner tool calls. No `kimi -p` write-capable. No yolo.

## Start small

Start one worker. Three-round cap. Same-fingerprint stop. Missing or stale source stop. Swarm / DAG / KG only after those are stable.

Author AGI claim is marketing. Not a fact.

## Local mapping

- PM = outer loop.
- Engineer (Cursor cloud) = inner coding round.
- Vault = KG writer.
- Do not install Kimi Code.
- Do not create Coordinator / Worker / Verifier bots.
- Do not replace wiki markdown with a second JSONL graph store.
- `output/ontology.json` is a derived snapshot of the wiki. Rebuild it. Do not write claims there first. See [[vault-ontology]].

See [[raptor-dispatch]], [[audited-task-contract]], [[context-graph]], [[llm-wiki]], [[work-per-cost]], [[musk-algorithm]], [[ai-sovereignty]], [[grok-bot-quota]].

## Related

[[raptor-dispatch]] · [[audited-task-contract]] · [[context-graph]] · [[llm-wiki]] · [[work-per-cost]] · [[musk-algorithm]] · [[ai-sovereignty]] · [[grok-bot-quota]] · [[src-av1dlive-loop-graph-2026-08-26]] · [[src-avid-obsidian-agent-team]] · [[vault-ontology]]
