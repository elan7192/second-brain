---
id: project:lanbb
type: project
tags:
  - project
created: 2026-08-24
updated: 2026-09-06
---

# LanBB

Product name for the bounty/flow work. **BB = bug bounty flow.** That line is identity, not contamination.

Source: [[src-lan-e-lanbb-bb-2026-08-27]] (lan E 2026-08-27 07:36 Taipei).

semantica is a tool inside it, not the project name.

Presence Lab ChatGPT mapping LanBB → bounty was closer than PM denials. Skills it listed (recon / IDOR / nuclei) stay `unverified` Free-chat hallucination. Do not compile them. Do not dump exploits.

Hunter input sources: [[lostsec]] (coffinxp, @lostsec_) and [[zack0x01]]. See [[hunter-follows]].

Ethical hacking = in-scope find + report. Ignore porn/adult on bounty lists. Do not write exploit methods.

Repo (2026-08-24, lanbb): [elan7192/LanBB](https://github.com/elan7192/LanBB), default branch `main`.

semantica is nested as submodule `tools/semantica` → https://github.com/semantica-agi/semantica.git @ `6c2ccfd`.

Did not rename `semantica-agi/semantica` or `elan7192/semantica`. No extra PRs for the nest.

Human decision 2026-08-24: new repo named LanBB; do not in-place rename an existing GitHub repo.

The vault did not create this repo. Wiki is still silent on whether any semantica remote is a fork.

Hunt→harden: [[hunt-harden-loop]]. Current wall: PR27 merged `94ac04c` wall `ad6f669` v17. Floor held. worker_processes 1 source OOM=false. Report 0/N. No more loops this window. Procedural stays in LanBB.


## White-hat learning (zack0x01_ digest → LanBB)

lan E 2026-09-06: fold zack digest into LanBB knowledge (not a loose src only). White-hat / learning only — **never** exploit steps / PoCs / payloads.

**Where to look (desk entry):**

| Need | Path |
| --- | --- |
| Curriculum map + learn-first order | [[src-lanbb-zack0x01-hackerz-space-learning-2026-09-06]] |
| AI hunter workflow (human recon → scoped AI → scripts collect / AI analyze → manual validate) | [[src-zack0x01-ai-hunter-workflow-2026-08-29]] |
| Burp MCP tooling note | [[src-zack0x01-burp-mcp-ai-pointer-2026-09-06]] — **no auto-wire** |
| Person / handle | [[zack0x01]] — active `@zack0x01_`; old `@zack0x01` suspended |
| Follow list | [[hunter-follows]] |

**Hubs:** https://hackerz.space (academy / roadmap CTA; courses often paid/Sold out) · free RECOX https://recox.hackerz.space (passive-recon UI; stay in-scope + report-only).

**Learn-first order (desk):**
1. Responsible disclosure + program scope / rules of engagement.
2. Classic web app security fundamentals (roadmap framing: recon → discovery → report → disclosure).
3. Passive recon literacy (public-data inventory concepts) before any active testing.
4. AI as multiplier for *reading* code and reports — never auto-exploit.

**KEEP for skills:** methodology checklist (scope → passive inventory → document → clear bounty report); AI sink-spotting as read-only review aid with human confirm; adversary-AI threat awareness (defensive).

**SKIP/KILL:** auto “AI hacker” bundles without human gates; payload/exploit/PoC dumps; blind buy of sold-out $99 “AI Hacker” upsell without syllabus audit.

Provenance: Researchy `/workspace/fill/lanbb-zack0x01-ai-cyber-learning-2026-09-06.md` → vaulted src above (PR96 method + Burp; PR97 curriculum src).

## Related

Hunter method: [[src-zack0x01-ai-hunter-workflow-2026-08-29]]. Curriculum map: [[src-lanbb-zack0x01-hackerz-space-learning-2026-09-06]]. Burp MCP: [[src-zack0x01-burp-mcp-ai-pointer-2026-09-06]] (no auto-wire).
[[MEMORY]] · [[ai-sovereignty]] · [[work-per-cost]] · [[hunter-follows]] · [[src-lan-e-lanbb-bb-2026-08-27]] · [[hunt-harden-loop]] · [[src-lanbb-pr9-loop1]] · [[src-lanbb-pr27-loop17]]
