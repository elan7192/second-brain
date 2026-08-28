---
id: concept:grok-bot-money
type: concept
tags:
  - wiki
created: 2026-08-25
updated: 2026-08-25
---

# Grok Bot money

Ten revenue workflows from Machina. Architecture: [[grok-bot]]. Source: [[src-exm7777-grok-bot-money]].

Miles Deutscher listed 25 general cases ([[grok-bot-use-cases]]). This tweet lists ten named revenue lanes with tools. Do not merge the lists.

Cash impact is the author's framing. No dollar results in this tweet. `unverified` as proof the lanes drive cash.

This vault does not run them. D5. See [[hunt-ship-loop]].

## Setup

1. Reverse prompting: tell Grok Bot to interview you about the business before setup. If another agent already holds that context, dump it to one `.md` and drop it in. See [[session-migrate]].
2. Start with read-and-prepare work only.
3. Review the result yourself for a week.
4. Grant approved actions, one at a time.
5. Add a routine so it runs without you.
6. Do the job once while the bot watches. Save it as a skill. Say what done means. If this vault ships a `SKILL.md`, gate it with [[skillspector]]. Trial Skill Recorder on fake data first. See [[skill-recorder]].

Tweet sequence: reverse prompting today, the X research lane this week, then the lane closest to revenue.

## Workflow 1: AI UGC (Higgsfield, sponsored)

The bot drives Higgsfield end to end instead of writing prompts to paste. Plugin on the shared computer. 100 free credits: sponsored. `unverified`.

Word-rate heuristic, quoted from the tweet: about three and a half words per second of talking-head speech, so a 30-second ad is roughly a hundred and five words split across four or five short clips, ending on the CTA.

1. Research before rendering. Mine customer complaints and winning ads from TikTok Shop, TikTok Creative Center, and the Meta Ad Library. File each winner in the vault.
2. Script at that word rate.
3. Character sheet: one headshot, a Nano Banana full-body image from that headshot, same outfit on every clip, plus a product still described verbatim.
4. Clips: Seedance renders each clip from the image references and a voice anchor. Hook first so you approve face and voice before the rest.
5. Final edit: the bot stitches with ffmpeg, pulls frames for a continuity check, then you decide whether the ad sells.

Product photos go in a folder. The pass is a saved skill. Finished creatives park for review. You push winners to ads.

Do not mix the later UGC-factory tweet into this page. See [[src-exm7777-grok-bot-money]].

## Nine other lanes

| Lane | Tool named in the tweet | Human gate |
| --- | --- | --- |
| Daily X research | Grok 4.6 on X, last 14 days, markdown into the vault | Read-only |
| SEO / AEO auditor | DataForSEO MCP | Fix list for you |
| Email outbound | Smartlead | Send stays behind approval |
| LinkedIn campaigns | LinkedIn Campaign Manager (browser) | Drafts for approval |
| Paid media reallocation | Meta Ads Manager | Your yes before touching spend |
| Clipping and long-form | Transcript then clip list | File for production. Vault clip rule: [[clip-pipeline]] |
| Social content | Typefully queue | Bot drafts, you publish |
| Ghostwriting for clients | Same X research, one vault folder per client | Client review |
| Competitor intelligence | Firecrawl overnight | Suggested changes only |

AEO in the tweet: ranking inside AI answers, audited weekly.

Paid media pairs with a creative-strategist lane that writes a why-it-works hypothesis with no invented metrics. Two bots, two screens, same ad account.

## Monitor

A chief-of-staff bot scans the other lanes and delivers a read-out with sources.

Group chats when lanes hand off: two to six bots.

Check the dashboard for spend and usage. A per-action audit view is coming. It is not there yet.

Every bot verifies before reporting. A bot that says done without checking is worse than no bot. See [[bot-voice]] and [[raptor-dispatch]].

## Related

[[grok-bot]] · [[grok-bot-use-cases]] · [[growth-operator]] · [[clip-pipeline]] · [[skill-recorder]] · [[src-exm7777-grok-bot-money]]
