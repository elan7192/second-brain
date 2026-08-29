---
id: meta:graph
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-29
---

# Graph

The live Obsidian graph and the files in `output/` cluster by concept. Color still means folder family: gold wiki, teal maps, blue hunt/twitter, green people, coral ship.

## Cause

`tools/render-obsidian-graph.py` used to park every wiki page on one ring around Home. That is a folder ring, so unrelated gold notes sat in one blob.

`index`, `log`, and `twitter` are catalogs. They link across every layer. In a force layout those edges collapse islands. `raw/` notes also sat on the rim because source pages point at them.

Color groups in `.obsidian/graph.json` only paint nodes. They do not place them.

## Filter

Search in graph view:

`path:wiki OR path:maps OR path:hunt OR path:ship OR path:output OR file:Home OR file:MEMORY -file:index -file:index-papers -file:index-sources -file:log -file:twitter`

Those hidden files stay in the vault. They are doors and timelines, not concept peers.

Forces: low center pull, higher repel, longer link distance. Peer concept links on those pages do the clustering.

## Islands

Taken from [[agent-operating-system]]. Home stays the door. agent-operating-system sits in the middle as the synthesis.

## Snapshot

Open `output/obsidian-graph.html` if you are not in Obsidian. Static copies: `output/obsidian-graph.svg`, `output/obsidian-graph.png`. Do not dump the graph into this page.

[[archify]] HTML under `output/archify/` is a checked component map. It is not this Obsidian cluster view.

Growth operator graph is separate: `output/growthos-graph.html`. See [[growth-operator]]. Do not dump `growth/` notes onto this wiki snapshot.
