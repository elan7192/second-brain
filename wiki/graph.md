---
id: meta:graph
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-24
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
| Compile | llm-wiki, tokens-as-capital, context-graph, retrieval, claims, stable-ids |
| Memory | memory-engineering, memory-ablation, portable-memory, eval-suite |
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
    context-graph
    llm-wiki
    src-bober-folder-workflow
    src-papa-couch-compiler
    tokens-as-capital
  end
  subgraph memory[Memory]
    MEMORY
    memory-ablation
    memory-engineering
    src-0xcodio-memory-ablation
  end
  subgraph verification[Verification]
    anti-slop
    jacky-kwok
    self-verification
    src-jacky-self-verification
    src-juampi-anti-slop-rank
    src-voxyz-verifiable-instructions
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
    maps
    ship
    src-avid-obsidian-agent-team
    src-deronin-growthos-vault
  end
  subgraph bridge[Synthesis]
    agent-operating-system
  end
  maps --> GrowthOS
  MEMORY --> memory-ablation
  MEMORY --> growth-operator
  ship --> ingest-brief-2026-08-23
  ship --> graph-clusters-2026-08-24
  hunt --> hunt-ship-loop
  ingest-brief-2026-08-24-arxiv-pages --> MEMORY
  ingest-brief-2026-08-24-trace --> memory-engineering
  ingest-brief-2026-08-24-trace --> context-graph
  ingest-brief-2026-08-24-trace --> tokens-as-capital
  ingest-brief-2026-08-25-play-methods --> hunt-ship-loop
  ingest-brief-2026-08-25-play-methods --> llm-wiki
  ingest-brief-2026-08-25-play-methods --> audited-task-contract
  ingest-brief-2026-08-25-play-methods --> harness-routing
  ingest-brief-2026-08-24-arxiv-281056 --> MEMORY
  ingest-brief-2026-08-24-arxiv-counts --> MEMORY
  ingest-brief-2026-08-24-arxiv-128956 --> MEMORY
  ingest-brief-2026-08-24-five-x --> llm-wiki
  ingest-brief-2026-08-24-five-x --> memory-engineering
  ingest-brief-2026-08-24-five-x --> harness-routing
  ingest-brief-2026-08-24-five-x --> anti-slop
  ingest-brief-2026-08-24-arxiv-156256 --> MEMORY
  ingest-brief-2026-08-25-growthos --> growth-operator
  ingest-brief-2026-08-25-growthos --> src-deronin-growthos-vault
  ingest-brief-2026-08-25-growthos --> GrowthOS
  ingest-brief-2026-08-25-growthos --> growth-briefing-2026-08-25
  growth-briefing-2026-08-25 --> src-deronin-growthos-vault
  memory-ablation --> src-0xcodio-memory-ablation
  memory-ablation --> memory-engineering
  memory-ablation --> verifiable-instructions
  self-verification --> src-jacky-self-verification
  self-verification --> jacky-kwok
  self-verification --> verifiable-instructions
  self-verification --> entropy-gate
  harness-routing --> src-rohit-harness-router
  harness-routing --> audited-task-contract
  harness-routing --> entropy-gate
  harness-routing --> rohit
  memory-engineering --> src-0xcodio-memory-ablation
  memory-engineering --> memory-ablation
  memory-engineering --> context-graph
  memory-engineering --> audited-task-contract
  memory-engineering --> entropy-gate
  hunt-ship-loop --> src-avid-obsidian-agent-team
  hunt-ship-loop --> hunt
  hunt-ship-loop --> ship
  hunt-ship-loop --> maps
  hunt-ship-loop --> growth-operator
  hunt-ship-loop --> llm-wiki
  hunt-ship-loop --> context-graph
  llm-wiki --> tokens-as-capital
  llm-wiki --> context-graph
  llm-wiki --> andrej-karpathy
  llm-wiki --> src-papa-couch-compiler
  llm-wiki --> src-bober-folder-workflow
  llm-wiki --> growth-operator
  tokens-as-capital --> src-papa-couch-compiler
  tokens-as-capital --> llm-wiki
  tokens-as-capital --> context-graph
  audited-task-contract --> src-rohit-harness-router
  audited-task-contract --> harness-routing
  audited-task-contract --> entropy-gate
  audited-task-contract --> memory-engineering
  anti-slop --> src-juampi-anti-slop-rank
  anti-slop --> verifiable-instructions
  entropy-gate --> src-hitu-entropy-engineering
  entropy-gate --> audited-task-contract
  entropy-gate --> harness-routing
  entropy-gate --> self-verification
  entropy-gate --> memory-engineering
  context-graph --> src-avid-obsidian-agent-team
  context-graph --> tokens-as-capital
  context-graph --> llm-wiki
  context-graph --> memory-engineering
  context-graph --> hunt-ship-loop
  verifiable-instructions --> src-voxyz-verifiable-instructions
  verifiable-instructions --> memory-ablation
  verifiable-instructions --> self-verification
  verifiable-instructions --> anti-slop
  agent-operating-system --> llm-wiki
  agent-operating-system --> memory-engineering
  agent-operating-system --> audited-task-contract
  agent-operating-system --> verifiable-instructions
  agent-operating-system --> hunt-ship-loop
  growth-operator --> src-deronin-growthos-vault
  growth-operator --> GrowthOS
  growth-operator --> growth-briefing-2026-08-25
  growth-operator --> llm-wiki
  growth-operator --> memory-engineering
  growth-operator --> hunt-ship-loop
  GrowthOS --> growth-operator
  GrowthOS --> src-deronin-growthos-vault
  rohit --> audited-task-contract
  rohit --> harness-routing
  rohit --> src-rohit-harness-router
  jacky-kwok --> self-verification
  jacky-kwok --> src-jacky-self-verification
  andrej-karpathy --> llm-wiki
  andrej-karpathy --> src-papa-couch-compiler
  andrej-karpathy --> src-bober-folder-workflow
  src-bober-folder-workflow --> llm-wiki
  src-bober-folder-workflow --> andrej-karpathy
  src-jacky-self-verification --> self-verification
  src-jacky-self-verification --> jacky-kwok
  src-juampi-anti-slop-rank --> anti-slop
  src-papa-couch-compiler --> llm-wiki
  src-papa-couch-compiler --> tokens-as-capital
  src-papa-couch-compiler --> andrej-karpathy
  src-hitu-entropy-engineering --> entropy-gate
  src-avid-obsidian-agent-team --> hunt-ship-loop
  src-avid-obsidian-agent-team --> context-graph
  src-rohit-harness-router --> audited-task-contract
  src-rohit-harness-router --> harness-routing
  src-rohit-harness-router --> rohit
  src-0xcodio-memory-ablation --> memory-engineering
  src-0xcodio-memory-ablation --> memory-ablation
  src-0xcodio-memory-ablation --> verifiable-instructions
  src-voxyz-verifiable-instructions --> verifiable-instructions
  src-deronin-growthos-vault --> growth-operator
```
<!-- graph-mermaid:end -->
