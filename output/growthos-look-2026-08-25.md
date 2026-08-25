---
type: output
tags:
  - growth
created: 2026-08-25
---

# GrowthOS graph look (main 8857622)

Opened `output/growthos-graph.html` after #15 squash into main. Cinematic metal chrome is what is on the page. [[growth-operator]]

## What is on screen

Iris core: clipped metal sphere, concentric iris rings, pink glow. Tapering tentacles with additive veins. Planet spheres in lava / green / pink / ice. HUD: SHORTLIST · 3, GROWTHOS, Grokbot · Obsidian Vault · Second Brain, VAULT CORE 39 NOTES, pills Costs must not scale and View-sale gap. Hint: Drag to orbit · Scroll to fly · Click a node to open the file.

Counted 39 notes on the core pill. Matches [[growth-operator]]. Do not treat tweet chrome "14 active / 24 in pipeline" as a fact. [[src-deronin-growthos-vault]]

## What was clicked

| Control | Result |
| --- | --- |
| Drag canvas | Orbit around the core |
| Scroll | Fly (zoom). Planets become readable |
| VAULT CORE | Sidebar `vault /` folders: partners, creators, playbooks, rulings, memories, content, trends, offers, niches, `_core.md` |
| partners/ | DEMO folders partner-#1/#2/#3. Meta: 2 live · 1 pipeline |
| View-sale gap | `vault / content /` mira.md, kai.md |
| Costs must not scale | shadow-operator.md. eptwts $100k stays `unverified` |
| Green planet | NICHES: ai-ugc.md, ai-ops.md |
| Another planet | JOURNAL |

Partner names and dollars in those notes are DEMO. Vault still does not post, pay, send, or create live Whop objects. [[growth-core]]

## Stack that is actually in the file

`three@0.160.0` UMD from unpkg. Custom meshes. Rebuild: `python3 tools/render-growthos-graph.py`.

Not in this file: `3d-force-graph`, GSAP, camera-synced node name pills. Planet spheres have no in-scene labels. You click a color, then read the sidebar.

unpkg three.min.js logs a deprecation warning (r160). Favicon 404. GPU ReadPixels stall only showed under screenshot tools.

## What to look at next

If labels on planets are required, that is a later edit. Camera tween from a sidebar file to a node is still missing. [[growthos-3d-gap-2026-08-25]]
