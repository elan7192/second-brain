---
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-27
---

# Graph

The live Obsidian graph and the files in `output/` cluster by concept. Color still means folder family: gold wiki, teal maps, blue hunt/twitter, green people, coral ship.

## Cause

`tools/render-obsidian-graph.py` used to park every wiki page on one ring around Home. That is a folder ring, so unrelated gold notes sat in one blob.

`index`, `log`, and `twitter` are catalogs. They link across every layer. In a force layout those edges collapse islands. `raw/` notes also sat on the rim because source pages point at them.

Color groups in `.obsidian/graph.json` only paint nodes. They do not place them.

## Filter

Search in graph view:

`path:wiki OR path:maps OR path:hunt OR path:ship OR path:output OR file:Home OR file:MEMORY -file:index -file:log -file:twitter`

Those hidden files stay in the vault. They are doors and timelines, not concept peers.

Forces: low center pull, higher repel, longer link distance. Peer concept links on those pages do the clustering.

## Islands

Taken from [[agent-operating-system]].

| Island | Pages |
| --- | --- |
| Compile | llm-wiki, tokens-as-capital, context-graph, claim-protocol |
| Memory | memory-engineering, memory-ablation, portable-memory, file-memory |
| Verification | verifiable-instructions, self-verification, anti-slop |
| Harness | audited-task-contract, harness-routing, entropy-gate |
| Hunt / ship | hunt-ship-loop, plus maps / hunt / ship indexes |
| People / sources | Sit with the concept they already cite |

Home stays the door. agent-operating-system sits in the middle as the synthesis.

## Snapshot

Open `output/obsidian-graph.html` if you are not in Obsidian. Static copies: `output/obsidian-graph.svg`, `output/obsidian-graph.png`.

Growth operator graph is separate: `output/growthos-graph.html`. See [[growth-operator]]. Do not dump `growth/` notes onto this wiki snapshot.

<!-- graph-mermaid:begin -->
```mermaid
flowchart TB
  subgraph compile[Compile]
    andrej-karpathy
    claim-protocol
    context-graph
    llm-wiki
    src-bober-folder-workflow
    src-lan-e-claim-protocol-2026-08-27
    src-papa-couch-compiler
    tokens-as-capital
  end
  subgraph memory[Memory]
    MEMORY
    file-memory
    memory-ablation
    memory-engineering
    portable-memory
    src-0xcodio-memory-ablation
  end
  subgraph verification[Verification]
    anti-slop
    jacky-kwok
    self-verification
    src-jacky-self-verification
    src-juampi-anti-slop-rank
    src-voxyz-verifiable-instructions
    stale-fact-detector
    verifiable-instructions
  end
  subgraph harness[Harness]
    audited-task-contract
    entropy-gate
    harness-routing
    rohit
    src-hitu-entropy-engineering
    src-rohit-harness-router
  end
  subgraph hunt-ship[Hunt / ship]
    GrowthOS
    graph-clusters-2026-08-24
    growth-briefing-2026-08-25
    growth-operator
    growthos-3d-gap-2026-08-25
    gsap-figma-note-2026-08-25
    hunt
    hunt-ship-loop
    ingest-brief-2026-08-23
    ingest-brief-2026-08-24-arxiv-128956
    ingest-brief-2026-08-24-arxiv-156256
    ingest-brief-2026-08-24-arxiv-281056
    ingest-brief-2026-08-24-arxiv-405856
    ingest-brief-2026-08-24-arxiv-counts
    ingest-brief-2026-08-24-arxiv-pages
    ingest-brief-2026-08-24-arxiv-tierlist
    ingest-brief-2026-08-24-batch01
    ingest-brief-2026-08-24-batch02
    ingest-brief-2026-08-24-batch03
    ingest-brief-2026-08-24-batch04
    ingest-brief-2026-08-24-batch05
    ingest-brief-2026-08-24-batch06
    ingest-brief-2026-08-24-batch07
    ingest-brief-2026-08-24-batch08
    ingest-brief-2026-08-24-batch09
    ingest-brief-2026-08-24-five-x
    ingest-brief-2026-08-24-three-x
    ingest-brief-2026-08-24-trace
    ingest-brief-2026-08-25-growthos
    ingest-brief-2026-08-25-play-methods
    ingest-brief-2026-08-25-skill-recorder
    ingest-brief-2026-08-27-botdirectory
    ingest-brief-2026-08-27-claim-protocol
    ingest-brief-2026-08-27-lanbb-bb
    maps
    ship
    src-avid-obsidian-agent-team
    src-deronin-growthos-vault
  end
  subgraph bridge[Synthesis]
    agent-operating-system
  end
  MEMORY --> memory-ablation
  MEMORY --> portable-memory
  MEMORY --> claim-protocol
  MEMORY --> stale-fact-detector
  MEMORY --> file-memory
  MEMORY --> growth-operator
  hunt --> hunt-ship-loop
  maps --> GrowthOS
  ship --> ingest-brief-2026-08-23
  ship --> graph-clusters-2026-08-24
  GrowthOS --> growth-operator
  GrowthOS --> src-deronin-growthos-vault
  growth-briefing-2026-08-25 --> src-deronin-growthos-vault
  growthos-3d-gap-2026-08-25 --> growth-operator
  growthos-3d-gap-2026-08-25 --> hunt-ship-loop
  growthos-3d-gap-2026-08-25 --> context-graph
  growthos-3d-gap-2026-08-25 --> src-deronin-growthos-vault
  growthos-3d-gap-2026-08-25 --> gsap-figma-note-2026-08-25
  gsap-figma-note-2026-08-25 --> growth-operator
  gsap-figma-note-2026-08-25 --> context-graph
  gsap-figma-note-2026-08-25 --> anti-slop
  gsap-figma-note-2026-08-25 --> src-deronin-growthos-vault
  ingest-brief-2026-08-24-arxiv-128956 --> MEMORY
  ingest-brief-2026-08-24-arxiv-156256 --> MEMORY
  ingest-brief-2026-08-24-arxiv-281056 --> MEMORY
  ingest-brief-2026-08-24-arxiv-counts --> MEMORY
  ingest-brief-2026-08-24-arxiv-pages --> MEMORY
  ingest-brief-2026-08-24-five-x --> llm-wiki
  ingest-brief-2026-08-24-five-x --> memory-engineering
  ingest-brief-2026-08-24-five-x --> harness-routing
  ingest-brief-2026-08-24-five-x --> anti-slop
  ingest-brief-2026-08-24-trace --> memory-engineering
  ingest-brief-2026-08-24-trace --> context-graph
  ingest-brief-2026-08-24-trace --> tokens-as-capital
  ingest-brief-2026-08-25-growthos --> growth-operator
  ingest-brief-2026-08-25-growthos --> src-deronin-growthos-vault
  ingest-brief-2026-08-25-growthos --> GrowthOS
  ingest-brief-2026-08-25-growthos --> growth-briefing-2026-08-25
  ingest-brief-2026-08-25-play-methods --> hunt-ship-loop
  ingest-brief-2026-08-25-play-methods --> llm-wiki
  ingest-brief-2026-08-25-play-methods --> audited-task-contract
  ingest-brief-2026-08-25-play-methods --> harness-routing
  ingest-brief-2026-08-27-botdirectory --> stale-fact-detector
  ingest-brief-2026-08-27-claim-protocol --> claim-protocol
  ingest-brief-2026-08-27-claim-protocol --> llm-wiki
  ingest-brief-2026-08-27-claim-protocol --> portable-memory
  ingest-brief-2026-08-27-claim-protocol --> file-memory
  ingest-brief-2026-08-27-claim-protocol --> memory-engineering
  ingest-brief-2026-08-27-claim-protocol --> context-graph
  ingest-brief-2026-08-27-claim-protocol --> stale-fact-detector
  ingest-brief-2026-08-27-claim-protocol --> entropy-gate
  agent-operating-system --> llm-wiki
  agent-operating-system --> memory-engineering
  agent-operating-system --> audited-task-contract
  agent-operating-system --> verifiable-instructions
  agent-operating-system --> hunt-ship-loop
  anti-slop --> src-juampi-anti-slop-rank
  anti-slop --> verifiable-instructions
  audited-task-contract --> src-rohit-harness-router
  audited-task-contract --> harness-routing
  audited-task-contract --> entropy-gate
  audited-task-contract --> memory-engineering
  context-graph --> src-avid-obsidian-agent-team
  context-graph --> claim-protocol
  context-graph --> tokens-as-capital
  context-graph --> llm-wiki
  context-graph --> memory-engineering
  context-graph --> hunt-ship-loop
  entropy-gate --> src-hitu-entropy-engineering
  entropy-gate --> audited-task-contract
  entropy-gate --> harness-routing
  entropy-gate --> self-verification
  entropy-gate --> memory-engineering
  entropy-gate --> claim-protocol
  file-memory --> llm-wiki
  file-memory --> memory-engineering
  file-memory --> claim-protocol
  file-memory --> portable-memory
  file-memory --> memory-ablation
  file-memory --> context-graph
  growth-operator --> src-deronin-growthos-vault
  growth-operator --> GrowthOS
  growth-operator --> gsap-figma-note-2026-08-25
  growth-operator --> context-graph
  growth-operator --> growthos-3d-gap-2026-08-25
  growth-operator --> growth-briefing-2026-08-25
  growth-operator --> llm-wiki
  growth-operator --> memory-engineering
  growth-operator --> hunt-ship-loop
  harness-routing --> src-rohit-harness-router
  harness-routing --> audited-task-contract
  harness-routing --> entropy-gate
  harness-routing --> rohit
  hunt-ship-loop --> src-avid-obsidian-agent-team
  hunt-ship-loop --> hunt
  hunt-ship-loop --> ship
  hunt-ship-loop --> maps
  hunt-ship-loop --> growth-operator
  hunt-ship-loop --> llm-wiki
  hunt-ship-loop --> context-graph
  llm-wiki --> stale-fact-detector
  llm-wiki --> claim-protocol
  llm-wiki --> tokens-as-capital
  llm-wiki --> context-graph
  llm-wiki --> andrej-karpathy
  llm-wiki --> src-papa-couch-compiler
  llm-wiki --> src-bober-folder-workflow
  llm-wiki --> growth-operator
  llm-wiki --> file-memory
  llm-wiki --> portable-memory
  memory-ablation --> src-0xcodio-memory-ablation
  memory-ablation --> memory-engineering
  memory-ablation --> verifiable-instructions
  memory-ablation --> claim-protocol
  memory-engineering --> src-0xcodio-memory-ablation
  memory-engineering --> claim-protocol
  memory-engineering --> memory-ablation
  memory-engineering --> context-graph
  memory-engineering --> audited-task-contract
  memory-engineering --> entropy-gate
  memory-engineering --> file-memory
  portable-memory --> file-memory
  portable-memory --> llm-wiki
  portable-memory --> claim-protocol
  self-verification --> src-jacky-self-verification
  self-verification --> jacky-kwok
  self-verification --> verifiable-instructions
  self-verification --> entropy-gate
  self-verification --> claim-protocol
  stale-fact-detector --> claim-protocol
  stale-fact-detector --> llm-wiki
  stale-fact-detector --> memory-ablation
  stale-fact-detector --> verifiable-instructions
  tokens-as-capital --> src-papa-couch-compiler
  tokens-as-capital --> llm-wiki
  tokens-as-capital --> context-graph
  verifiable-instructions --> src-voxyz-verifiable-instructions
  verifiable-instructions --> memory-ablation
  verifiable-instructions --> self-verification
  verifiable-instructions --> anti-slop
  claim-protocol --> src-lan-e-claim-protocol-2026-08-27
  claim-protocol --> file-memory
  claim-protocol --> memory-ablation
  claim-protocol --> portable-memory
  claim-protocol --> context-graph
  claim-protocol --> llm-wiki
  claim-protocol --> memory-engineering
  claim-protocol --> stale-fact-detector
  claim-protocol --> entropy-gate
  claim-protocol --> self-verification
  andrej-karpathy --> llm-wiki
  andrej-karpathy --> src-papa-couch-compiler
  andrej-karpathy --> src-bober-folder-workflow
  jacky-kwok --> self-verification
  jacky-kwok --> src-jacky-self-verification
  rohit --> audited-task-contract
  rohit --> harness-routing
  rohit --> src-rohit-harness-router
  src-0xcodio-memory-ablation --> memory-engineering
  src-0xcodio-memory-ablation --> memory-ablation
  src-0xcodio-memory-ablation --> verifiable-instructions
  src-avid-obsidian-agent-team --> hunt-ship-loop
  src-avid-obsidian-agent-team --> context-graph
  src-bober-folder-workflow --> llm-wiki
  src-bober-folder-workflow --> andrej-karpathy
  src-deronin-growthos-vault --> growth-operator
  src-hitu-entropy-engineering --> entropy-gate
  src-jacky-self-verification --> self-verification
  src-jacky-self-verification --> jacky-kwok
  src-juampi-anti-slop-rank --> anti-slop
  src-papa-couch-compiler --> llm-wiki
  src-papa-couch-compiler --> tokens-as-capital
  src-papa-couch-compiler --> andrej-karpathy
  src-rohit-harness-router --> audited-task-contract
  src-rohit-harness-router --> harness-routing
  src-rohit-harness-router --> rohit
  src-voxyz-verifiable-instructions --> verifiable-instructions
  src-lan-e-claim-protocol-2026-08-27 --> memory-ablation
  src-lan-e-claim-protocol-2026-08-27 --> portable-memory
  src-lan-e-claim-protocol-2026-08-27 --> file-memory
  src-lan-e-claim-protocol-2026-08-27 --> claim-protocol
  src-lan-e-claim-protocol-2026-08-27 --> llm-wiki
  src-lan-e-claim-protocol-2026-08-27 --> memory-engineering
  src-lan-e-claim-protocol-2026-08-27 --> context-graph
  src-lan-e-claim-protocol-2026-08-27 --> stale-fact-detector
```
<!-- graph-mermaid:end -->
