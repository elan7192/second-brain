---
id: concept:grok-bot
type: concept
tags:
  - wiki
created: 2026-08-25
updated: 2026-09-04
---

# Grok Bot

Product harness from Machina. One persistent named agent. One job.

Source: [[src-exm7777-grok-bot-money]]. Revenue lanes: [[grok-bot-money]]. Miles list: [[grok-bot-use-cases]].

## Architecture

Each bot runs on a persistent cloud VM with a browser, a filesystem, and a terminal. Work finishes inside the tools.

All bots share one cloud computer on the account. Files, browser sessions, and logins carry across the roster.

Each bot gets its own screen. One bot runs one computer-use task on its screen at a time.

The tweet names Grok 4.6. Pricing versus Claude Fable 5 and GPT-5.6 Sol is `unverified`.

Product launch: [[src-xai-introducing-grok-bot]]. Engineer keepers (not org chart): [[spacexai-grok-bot-keepers]]. Privacy/2FA on cloud computers: [[src-petergyang-agent-privacy]] (pointer [[src-petergyang-cloud-login-unease-pointer]]). Official design note pointer: [[src-cbdoge-designing-grok-bot-pointer]].

xAI line as quoted in the tweet: “Bots are AI teammates that do real work for you. They sign in to your tools, use them just like you do, and come back with finished work.” Product copy. Not a paper.

## Config

description, conversation, memory, connectors, computer use, skills, routines, approvals.

Memory holds preferences and summaries. The tweet says memory is not a substitute for an authoritative source. Sync the Obsidian vault onto that computer. The vault is the source of truth. See [[memory-engineering]] and [[llm-wiki]].

Require Approval always stops matching actions. When an allow rule and an approval rule both match, approval wins.

## One bot per workflow

The tweet's failure mode: one giant agent, operators cannot keep up, they lose trust.

OpenClaw, as described there, bloats when complex business workflows stack. Grok Bot isolates lanes: each bot carries only its lane's context, tools, and memory.

Quoted docs rule: the best roles own a repeatable outcome, not a loose category of questions.

This matches [[raptor-dispatch]] (one owner per job). It does not match [[entropy-gate]] isolated worktrees. Separate screens are work surfaces, not security boundaries. See [[contradictions]] C30.

## Limits

Early beta. Tweet list:

- Shared computer is one machine. Separate bots are separate work surfaces, not separate security boundaries.
- Passwords, 2FA, CAPTCHAs, payments: the bot hands you the computer.
- Browser work is slower than an API and stalls when a site changes its UI.
- No Grok Bot-specific spend cap yet. Watch the usage page.
- An approval controls the proposed action. It does not reverse work already completed.

Start with one valuable, reversible workflow. Read-and-prepare first. Actions behind approval. Money moves never automated on day one. Aligns with D5. See [[hunt-ship-loop]].

## Related

[[grok-bot-money]] · [[harness-routing]] · [[entropy-gate]] · [[raptor-dispatch]] · [[memory-engineering]] · [[llm-wiki]] · [[src-exm7777-grok-bot-money]] · [[company-foundry]] · [[spacexai-grok-bot-keepers]] · [[src-xai-introducing-grok-bot]] · [[src-exm7777-advanced-x-research-grok-bot]]
