---
id: source:src-desk-one-cut-proposal-2026-09-08
type: source
tags:
  - wiki
  - ops
created: 2026-09-08
updated: 2026-09-08
---

# src-desk-one-cut-proposal-2026-09-08

- Artifact: weekly-improve proposal drawn from [[src-desk-bots-skills-process-audit-fable-2026-09-08]] (lan E desk snapshot 2026-09-08). Proposal only; nothing applied.
- Author path: Cursor Claude Fable 5.1 (this run) → Vault PR → CoS carries it into the Monday 10:00 Taipei weekly improve → lan E yes or no.
- Rule honored: **≤1 instruction or seat change per week**, human yes before apply, board updated after ([[lan-e-desk-team]]). Live bot profile edits are never auto-applied from this vault.
- **Status 2026-09-08:** **SUPERSEDED / not applied live.** Captain (via Firstmate task `pr129-skip-live`) skipped live CoS GO–ACK profile edit — CoS seat delete supersedes this cut. Page remains historical proposal only.
- 判定: 入vault建議 (thin; one cut, one gate, one rollback).
- Dedup: no prior one-cut page. Near: [[src-skills-cut-42-to-37-2026-09-05]] (applied cut record) · [[src-routines-cut-playbook-2026-09-05]].

## Claims kept

**The cut:** delete CoS's side of the GO–ACK loop. One instruction change, on the Chief of Staff profile only. Proposed text (three lines): "TASK once, with an id. Revise or STOP is a new TASK id that names the id it supersedes, sent once. Reply only to an artifact path, a blocker, or a SHA. Do not reply to ACK, GO, or received." Why this and not the husk: the husk costs zero fires; each GO–ACK chain costs Fill or Engineer turns plus CoS turns on a long thread ([[src-kloss-routine-audit]] item 4 and 6). Delete the part that burns.

**Why one side is enough:** a loop needs two talkers. Fill and Engineer profiles stay untouched this week; when CoS stops answering acks, the chain ends at the bot's ack. No new skill, no new routine, no new bot. Aligns [[raptor-dispatch]] (report once, no empty acks) and the anti-swarm bus (2026-09-06) on [[lan-e-desk-team]].

**Gate before apply (quiet clause):** CoS runs `transcript-healthcheck` on demand over the last 7 days of desk chat and counts GO–ACK chains (a chain = CoS message whose body is only confirm / go / received, followed by a bot ack, followed by another CoS confirm). Baseline **≥ 2** → propose the cut. Baseline **0 or 1** → this week is **quiet**; the CoS-reported pain is not confirmed and the slot is not spent.

**Owner:** CoS proposes with the baseline number in the Monday one-liner; lan E says yes or no; CoS edits the one profile line after yes and updates the board. Vault records the result on [[lan-e-desk-team]] and appends [[log]].

**Done-proof (7 days after apply):** same count on the following Monday. Pass = **0** GO–ACK chains and no task lost (every TASK id sent in the week has an artifact path, a blocker, or an explicit lan E cancel). Fail = chains still ≥ 1, or a TASK id with no terminal state, which means bots wait for a confirm that no longer comes.

**Rollback:** restore the previous CoS profile text (one line diff, kept in the board note). No data, cron, or seat is touched, so rollback is the same size as apply. If rollback happens, the failure reason goes on the board and the next candidate is the Fill/Engineer-side rule instead.

**Not this week (queued in order):** (1) delete husk agent "New Agent" `2be5c2b6-29f9-40f7-b369-6467753cf64e` — only bundle now if lan E rules the 2026-09-05 "Gone" yes already covers it; (2) delete skills `x-scout-connect-onboarding` · `weekly-search-report` · `weekly-competitor-brief`; (3) one line in `engineering-playbook`: locked defaults are not questions, list assumptions in the PR body; (4) sunset 2026-10-05 for parked-seat skill packs; (5) one path for Copy Humanizer vs `unslop`.

## Pages updated

[[index-sources]] · [[lan-e-desk-team]]

## Related

[[src-desk-bots-skills-process-audit-fable-2026-09-08]] · [[lan-e-desk-team]] · [[raptor-dispatch]] · [[musk-algorithm]] · [[src-kloss-routine-audit]] · [[src-skills-cut-42-to-37-2026-09-05]] · [[src-routines-cut-playbook-2026-09-05]] · [[skill-improver]]
