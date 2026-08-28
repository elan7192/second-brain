---
type: output
tags:
  - growth
created: 2026-08-25
---

# GrowthOS 3D: plugin vs clone vs this vault

Neither an Obsidian plugin nor a hunt for an existing cyberpunk clone. This vault already compiles a subgraph graph from `growth/` into `output/growthos-graph.html`. [[growth-operator]]

## Why that fork is closed here

D7: Obsidian is the IDE for this repo. That is not a license to ship a 3D plugin. [[decisions]] · [[how-it-works]]

D5: the vault does not post, pay, send, or deploy. A plugin store listing or a Tauri app is a product. [[hunt-ship-loop]]

[[context-graph]]: give the model the subgraph for the decision, not the dump. A hairball of hundreds or thousands of nodes is the failure mode D8 already rejected on the 2D wiki snapshot. [[graph]]

The DeRonin clip is operator-memory chrome (VAULT CORE, PARTNERS, RULINGS). Partner counts on screen were not ingested as facts. The bodies live in markdown. [[src-deronin-growthos-vault]]

Counted 2026-08-25: 39 files in `growth/`. The renderer prints that count on VAULT CORE. Do not pad it to look like the tweet.

## Score of the three "gaps"

| Claim | This vault |
| --- | --- |
| Need WebGL + Three.js + 3d-force-graph for 60fps thousands of bloom nodes | Stack is already UMD 3d-force-graph. Target is the `growth/` subgraph, not thousands of wiki pages. 60fps-at-thousands is `unverified` here. |
| Must use SpriteText or CSS2DRenderer | HTML pills facing the camera are already in the page. SpriteText mixed with HTML labels blanked nodes. Stay off that mix. [[gsap-figma-note-2026-08-25]] |
| Must read the local FS as an Obsidian plugin or Electron/Tauri app | Compile step already parses `growth/*.md` and wiki links. Live FS watch and plugin API are not in scope. |
| Click a sidebar file, camera flies to the node | Missing in the current page. File click opens the note body. Camera tween is a later edit if the human asks. |
| "Months of engineering" is why no one built the tweet | `unverified`. The blocker in this vault is product scope (D5) and subgraph ( [[context-graph]] ), not GPU bloom. |

`image_2.png` was not in the workspace this turn. If it is the tweet constellation, treat on-screen partner counts as chrome. [[src-deronin-growthos-vault]]

## Existing tools

Wiki has no page that names a 3D Obsidian graph product to copy. Exa search 2026-08-25 returned a free-tier rate limit. Do not invent a clone list. Drop a URL in `raw/` or reconnect Exa if that hunt should start.

## What to do next if the human wants more chrome

Stay on the compiled HTML page. Do not open a plugin repo. Do not dump `wiki/` into GrowthOS. Optional: GSAP `cameraPosition` tween when a sidebar file maps to a node id.
