---
id: project:lanbb
type: project
tags:
  - project
created: 2026-08-24
updated: 2026-08-27
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

## Related

[[MEMORY]] · [[ai-sovereignty]] · [[work-per-cost]] · [[hunter-follows]] · [[src-lan-e-lanbb-bb-2026-08-27]] · [[hunt-harden-loop]] · [[src-lanbb-pr9-loop1]] · [[src-lanbb-pr27-loop17]]
