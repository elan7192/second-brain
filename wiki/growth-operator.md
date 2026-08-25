---
type: concept
tags:
  - wiki
created: 2026-08-25
updated: 2026-08-25
---

# Growth operator

DeRonin GrowthOS: an Obsidian vault Grokbot reads before a new partner, so ops start with prior lessons.

Source: [[src-deronin-growthos-vault]]. Door: [[GrowthOS]]. Load: [[growth-core]].

## What landed in this vault

Operator notes live in `growth/`. Compiled claims about the system live here.

Seven layers from the tweet, plus hubs the video showed (memories, strategy, insights, journal):

| Layer | Hub |
| --- | --- |
| Niches | [[growth-niche-ai-ugc]] |
| Creators | [[growth-creators]] |
| Partners | [[growth-partners]] |
| Content | [[growth-content]] |
| Playbooks | [[growth-playbooks]] |
| Rulings | [[growth-rulings]] |
| Trends | [[growth-trends]] |

Rulings that are in the tweet: never below 25% rev-share ([[growth-ruling-revshare]]); never partner without proof of skill ([[growth-ruling-proof]]).

## Demo vs live

Partner names, handles, and dollar figures in `growth/` are **DEMO**. They exist so a briefing has something to read. They are not live deals.

Vault still does not post, pay, send, or create live Whop objects. See D5.

## 3D graph path

Not an Obsidian plugin. Not Electron or Tauri. Not a dump of thousands of wiki pages.

D7 is Obsidian as the IDE. D5 is no deploy. The live page is compiled HTML: `python3 tools/render-growthos-graph.py` reads `growth/*.md` and writes `output/growthos-graph.html`. Counted 2026-08-25: 39 notes. Do not fake tweet chrome counts such as "14 active / 24 in pipeline". Those are chrome on [[src-deronin-growthos-vault]], not facts.

Stack in the page: `3d-force-graph@1.73.3` UMD, HTML pills synced to the camera, GSAP for HUD and sidebar. Mixing SpriteText with HTML labels blanked nodes; stay on UMD + HTML overlays. See [[gsap-figma-note-2026-08-25]].

Do not merge this graph with the wiki snapshot. [[graph]] · [[context-graph]]

Existing "cyberpunk vault" clones: wiki silent. Web search 2026-08-25 hit Exa rate limit. Do not name tools from memory.

Fork answer: [[growthos-3d-gap-2026-08-25]].

## How to run it

1. Read [[growth-core]], then only the pages it points to.
2. `python3 tools/growth-brief.py --partner "…"`
3. Open `output/growthos-graph.html` for the 3D graph. Figma is not required for that page; see [[gsap-figma-note-2026-08-25]].
4. File the briefing. Do not send.

Latest briefing: [[growth-briefing-2026-08-25]]. Graph fork: [[growthos-3d-gap-2026-08-25]].

## Related

[[src-deronin-growthos-vault]] · [[grok-bot-use-cases]] · [[llm-wiki]] · [[memory-engineering]] · [[hunt-ship-loop]]
