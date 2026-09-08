---
id: source:src-desk-bots-skills-process-audit-fable-2026-09-08
type: source
tags:
  - wiki
  - ops
  - skills
created: 2026-09-08
updated: 2026-09-08
---

# src-desk-bots-skills-process-audit-fable-2026-09-08

- Artifact: lan E desk snapshot paste dated 2026-09-08 (operating contract, seat roster, 41 user skill names under `workflows/`, live routines, CoS process-pain notes). Paste only; not copied into `raw/`; no bot profile bodies or skill bodies were read.
- Author path: lan E → Cursor Claude Fable 5.1 (this run, on-demand quota, one focused PR) → Vault PR. Method notes only. No live profile edit, no skill delete, no new bot.
- Method frame: [[musk-algorithm]] in strict order (requirements → delete → simplify → accelerate → automate last). Best part is no part.
- 判定: 入vault建議 (audit METHOD; DELETE / PARK / KEEP lists are proposals for lan E yes, max one instruction or seat change per week).
- Quote untrusted: CoS process pain is CoS self-report; each item below carries a verify step. Snapshot may lag disk.
- Dedup: no existing desk bots+skills+process audit. Near (do not overwrite): [[src-cos-team-md-2026-09-05]] (board) · [[src-skills-cut-42-to-37-2026-09-05]] (applied skills cut) · [[src-algo-routines-audit-2026-09-05]] · [[src-routines-cut-playbook-2026-09-05]] (routines husks) · [[src-adiix-grok-bot-org]] (hire by bottleneck) · [[src-kloss-routine-audit]] (send once).
- Companion: [[src-desk-one-cut-proposal-2026-09-08]] (the single weekly-improve cut drawn from this audit).

## Claims kept

**Step 1, requirements (named owner lan E):** front door CoS only, last yes human, durable knowledge via Vault, Algorithm every round. All four survive the "who asked for this" test. One requirement is dumb on the evidence: **"standing seat = its own bot"**. Standing seats went **7 (board 2026-09-05) → 11 (snapshot 2026-09-08)** with Product Idea Stress Test, Copy Humanizer, Critiquito, GTM Loop Closer. Those four are review lenses, not domains with a distinct source set or approval boundary (adiix hire-by-bottleneck test). Requirement rewrite: a lens is a skill on an existing seat unless it has a recurring bottleneck with its own sources or yes-gate. Verify: per lens bot, count tasks in the last 14 days; zero → park.

**Step 2, delete (proposed, needs lan E yes, one per week):** (a) husk agent "New Agent" (empty description, id `2be5c2b6-29f9-40f7-b369-6467753cf64e`) — board already lists "New Bot husk" under Gone on 2026-09-05, so either the delete never landed or a husk was re-created; re-verify on disk and delete. Parked or gone means zero on disk, not `enabled:false` ([[src-algo-routines-audit-2026-09-05]]). (b) skill `x-scout-connect-onboarding` — one-shot onboarding; X Scout's live weekday digest proves the connection is done; same husk class as the `getting-started*` folders cut 2026-09-05. (c) skills `weekly-search-report` and `weekly-competitor-brief` — cadence recipes for seats with zero cron; they invent an optional cron surface, same class as `extra-recurring-checks` cut 2026-09-05. Net after these three skill deletes: 41 → 38.

**Step 2, skill count drift:** vault recorded **37** user skills after the 2026-09-05 cut; snapshot names **41**. Net +4 in three days, names not diffed (the 09-05 page kept no inventory on purpose). Method: the count itself is the metric; a cut that regrows in a week did not change the requirement. Add the count to the Monday weekly improve one-liner.

**Step 2, parked packs get a sunset:** 15 skills sit on parked seats (design ×7 for figma bro, SEO ×4 for SEO & AEO Desk, competitor ×4 for Competitor Watch) plus `last30days` for the parked last30days bot. The 2026-09-05 rule "keep until bot unparked with named job" has no expiry, so it is a permanent keep. Proposed: sunset **2026-10-05**; if the seat is still parked, delete the pack (git history and this catalog keep the text; re-create is cheap). OPINION until lan E yes.

**Step 3, simplify the GO–ACK loop (Fill/Engineer, CoS-reported, verify):** a STOP or revise message races a prior TASK and both sides ack. The loop needs two talkers. Delete one side: CoS sends TASK once with an id; revise or STOP is a new TASK id that names the superseded id, sent once; CoS replies only to an artifact path, a blocker, or a SHA, never to ACK / GO / received ([[raptor-dispatch]] no empty acks; [[src-kloss-routine-audit]] item 6). No new part. This is the one cut in [[src-desk-one-cut-proposal-2026-09-08]].

**Step 3, Engineer re-asking UX after defaults locked (CoS-reported, verify):** fix lives in the handoff packet, not a new skill. The adiix packet already has `decisions` and `do-not-assume` fields; locked UX defaults go there and the Engineer builds, listing assumptions in the PR body instead of asking. Aligns [[src-pvncher-rethinking-skills-gpt6-astra]] ("always ask" walls stop stronger models early; define completion up front). Queue as the following week's candidate (one line in `engineering-playbook`), not this week.

**Step 3, one path per job:** Copy Humanizer bot and `unslop` skill are two paths for the same job (vault already folds anti-slop sources into "Copy Humanizer / Unslop"; see [[anti-slop]]). Keep one. Verify `wake-creative-discussion` and `coral-bay-peer-dm` against the anti-swarm bus on [[lan-e-desk-team]] (2026-09-06: no improvised peer side-channels, no N-way brainstorm); if either spawns peer chat, delete.

**Step 4, accelerate (only after the deletes land):** one metric, hours from TASK id to first artifact path per seat, read from transcripts on demand with `transcript-healthcheck`. No dashboard, no new routine.

**Step 5, automate last:** nothing this round. Event beats cron (Vault `pr-merged` is the model). No new cron, no new bot, no MCP write path.

## Skill overlap clusters (names only)

| Cluster | Skills | Seat | Verdict |
|---|---|---|---|
| Design pack (parked figma bro; Designer / Motion / Product gone) | build-a-screen-from-a-brief · component-library-audit · design-to-code-handoff-notes · design-token-audit · frame-to-build-spec · motion-and-prototype-notes · senior-design | none live | PARK with sunset 2026-10-05 |
| SEO / AEO pack (parked) | answer-engine-question-map · keyword-and-question-research · page-audit-and-refresh-plan · weekly-search-report | none live | DELETE `weekly-search-report`; PARK rest with sunset |
| Competitor pack (parked) | build-the-watch-list · competitor-page-diff · pricing-and-packaging-comparison · weekly-competitor-brief | none live | DELETE `weekly-competitor-brief`; PARK rest with sunset |
| last30days | last30days | parked bot | PARK with sunset; Researchy can run it on demand |
| Engineer | browser-to-api · codebase-hardening-auditor · engineering-playbook · file-structure-cleanup-plan · github-issue-drafter · github-pr-triage · show-code-shape · make-bot-ui · design-grok-bot | Lingxi Engineer / CoS | KEEP; `make-bot-ui` and `design-grok-bot` are bot-building recipes, confirm one owner |
| Research | grok-cli-research-pass (Researchy) · x-deep-research-pass (X Scout) · stale-fact-detector · ai-residual-capture · x-scout-connect-onboarding | Researchy / X Scout | KEEP one research pass per seat; DELETE onboarding |
| Vault | vault-knowledge-sync | Vault | KEEP |
| Meta / instruction | the-algorithm · skill-improver · grok-bot-lessons · routine-healthcheck · transcript-healthcheck | CoS / Rutin | KEEP; open simplify from 09-05 still pending (strip Algorithm block from `grok-bot-lessons`, it duplicates `the-algorithm`) |
| Writing / outreach | unslop · writer-content-brief · gmail-draft-not-send · coral-bay-peer-dm · wake-creative-discussion | Copy Humanizer / CoS | one path with Copy Humanizer; VERIFY the two peer/wake skills vs anti-swarm |

Counts: 41 named; 16 on parked seats; 3 DELETE now; sunset covers 13 more if seats stay parked.

## Process bottlenecks (verify before acting)

1. GO–ACK loop on STOP/revise races: CoS confirms, bot acks, CoS acks the ack. Cut CoS's side. Baseline: count chains in the last 7 days before applying.
2. Engineer re-asks locked UX: defaults not in the packet. Put them in `decisions` / `do-not-assume`; assumptions go in the PR body.
3. Seat inflation: 7 → 11 standing in three days while skill count regrew 37 → 41. Hire-by-bottleneck test per new seat.
4. Skill packs for parked seats with no expiry: permanent keep by default. Sunset rule.
5. Husk re-appearance: "Gone" on the board but present on disk. Board and disk drift; re-verify on Monday.

## Routing cheat sheet (proposed additions)

Existing: X → X Scout · research → Researchy · code → Lingxi Engineer · wiki → Vault · quota and shared-box ops → Fill · routines CUT → Rutin.

Add: copy or tone → one path only (Copy Humanizer or `unslop`, after the one-path decision) · product idea → Product Idea Stress Test · red-team or critique → Critiquito · GTM follow-through → GTM Loop Closer · higher-end reasoning → Cursor Fable via Engineer, one focused PR, sparingly (on-demand quota).

Tie-breaks: source set wins (X content is X Scout even when the ask says research) · skill before seat (if an existing seat has the skill, do not wake a lens bot) · no fit → CoS stays quiet or asks lan E; CoS does not do the work ([[src-adiix-grok-bot-org]]) · revise = new TASK id, never a chat correction.

## Pages updated

[[index-sources]] · [[lan-e-desk-team]] · [[src-desk-one-cut-proposal-2026-09-08]]

## Related

[[lan-e-desk-team]] · [[musk-algorithm]] · [[raptor-dispatch]] · [[src-cos-team-md-2026-09-05]] · [[src-skills-cut-42-to-37-2026-09-05]] · [[src-algo-routines-audit-2026-09-05]] · [[src-routines-cut-playbook-2026-09-05]] · [[src-adiix-grok-bot-org]] · [[src-kloss-routine-audit]] · [[src-pvncher-rethinking-skills-gpt6-astra]] · [[skill-improver]] · [[anti-slop]] · [[grok-bot-quota]] · [[src-desk-one-cut-proposal-2026-09-08]]
