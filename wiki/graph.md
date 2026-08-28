---
id: meta:graph
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-28
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
| Compile | llm-wiki, tokens-as-capital, context-graph, retrieval, claims, stable-ids, claim-protocol |
| Memory | memory-engineering, memory-ablation, portable-memory, memory-system, claims |
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
    claims
    epistemic-labels
    file-memory
    memory-ablation
    memory-engineering
    memory-system
    portable-memory
    provenance
    src-0xcodio-memory-ablation
    untrusted-ingest
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
    can-boluk
    daily-tool-replace
    entropy-gate
    harness-routing
    headlong
    rohit
    src-can1357-daily-tool-replace-2026-08-27
    src-hitu-entropy-engineering
    src-hxiao-headlong
    src-laude-headlong
    src-rohit-harness-router
  end
  subgraph hunt-ship[Hunt / ship]
    GrowthOS
    daily-tool-replace-vault-2026-08-27
    disclosures
    graph-clusters-2026-08-24
    growth-briefing-2026-08-25
    growth-operator
    growthos-3d-gap-2026-08-25
    gsap-figma-note-2026-08-25
    hunt
    hunt-ship-loop
    ingest-brief-2026-08-23
    ingest-brief-2026-08-23-cybersecurity-skills
    ingest-brief-2026-08-23-retrieval-second-brain
    ingest-brief-2026-08-23-skill-library
    ingest-brief-2026-08-23-skill-pack-list
    ingest-brief-2026-08-24
    ingest-brief-2026-08-24-arxiv-405856
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
    ingest-brief-2026-08-24-disclosure-index
    ingest-brief-2026-08-24-five-x
    ingest-brief-2026-08-24-three-x
    ingest-brief-2026-08-24-trace
    ingest-brief-2026-08-25-growthos
    ingest-brief-2026-08-25-play-methods
    ingest-brief-2026-08-25-skill-recorder
    ingest-brief-2026-08-26-headlong
    ingest-brief-2026-08-26-headlong-hour
    ingest-brief-2026-08-27-botdirectory
    ingest-brief-2026-08-27-can1357-daily-tool
    ingest-brief-2026-08-27-claim-protocol
    ingest-brief-2026-08-27-lanbb-bb
    maps
    memory-engine-2026-08-28
    memory-system-brief-2026-08-27
    merge-conflict-report-2026-08-28
    merge-conflict-report-2026-08-28-daily-tool
    merge-conflict-report-2026-08-28-daily-tool-2
    merge-conflict-report-agent-facing-2026-08-28
    merge-conflict-report-entropy-quiz-2026-08-28
    ontology-rebuild-brief-2026-08-28
    query-entropy-gate
    query-skills-and-slop
    ship
    src-avid-obsidian-agent-team
    src-deronin-growthos-vault
  end
  subgraph bridge[Synthesis]
    agent-operating-system
  end
  MEMORY --> memory-ablation
  MEMORY --> portable-memory
  MEMORY --> claims
  MEMORY --> memory-system
  MEMORY --> claim-protocol
  MEMORY --> epistemic-labels
  MEMORY --> provenance
  MEMORY --> untrusted-ingest
  MEMORY --> file-memory
  MEMORY --> daily-tool-replace
  MEMORY --> daily-tool-replace-vault-2026-08-27
  MEMORY --> stale-fact-detector
  MEMORY --> headlong
  MEMORY --> growth-operator
  hunt --> hunt-ship-loop
  hunt --> disclosures
  maps --> GrowthOS
  ship --> ingest-brief-2026-08-23
  ship --> ingest-brief-2026-08-23-skill-library
  ship --> ingest-brief-2026-08-23-cybersecurity-skills
  ship --> ingest-brief-2026-08-23-skill-pack-list
  ship --> ingest-brief-2026-08-23-retrieval-second-brain
  ship --> graph-clusters-2026-08-24
  ship --> ontology-rebuild-brief-2026-08-28
  ship --> merge-conflict-report-2026-08-28
  disclosures --> hunt-ship-loop
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
  ingest-brief-2026-08-26-headlong-hour --> headlong
  ingest-brief-2026-08-26-headlong-hour --> harness-routing
  ingest-brief-2026-08-26-headlong-hour --> entropy-gate
  query-skills-and-slop --> anti-slop
  query-skills-and-slop --> src-juampi-anti-slop-rank
  query-skills-and-slop --> context-graph
  query-skills-and-slop --> src-voxyz-verifiable-instructions
  query-skills-and-slop --> llm-wiki
  query-skills-and-slop --> tokens-as-capital
  query-skills-and-slop --> memory-engineering
  query-skills-and-slop --> memory-ablation
  query-skills-and-slop --> src-papa-couch-compiler
  query-skills-and-slop --> verifiable-instructions
  query-skills-and-slop --> self-verification
  merge-conflict-report-2026-08-28-daily-tool-2 --> daily-tool-replace-vault-2026-08-27
  ingest-brief-2026-08-23-cybersecurity-skills --> tokens-as-capital
  ingest-brief-2026-08-23-cybersecurity-skills --> context-graph
  ingest-brief-2026-08-23-skill-library --> tokens-as-capital
  ingest-brief-2026-08-23-skill-library --> anti-slop
  ingest-brief-2026-08-23-skill-library --> llm-wiki
  ingest-brief-2026-08-23-retrieval-second-brain --> memory-engineering
  ingest-brief-2026-08-23-retrieval-second-brain --> context-graph
  ingest-brief-2026-08-23-retrieval-second-brain --> llm-wiki
  ingest-brief-2026-08-23-skill-pack-list --> tokens-as-capital
  ingest-brief-2026-08-23-skill-pack-list --> verifiable-instructions
  merge-conflict-report-2026-08-28-daily-tool --> ship
  merge-conflict-report-2026-08-28-daily-tool --> anti-slop
  merge-conflict-report-2026-08-28-daily-tool --> harness-routing
  merge-conflict-report-2026-08-28-daily-tool --> daily-tool-replace
  merge-conflict-report-2026-08-28-daily-tool --> headlong
  merge-conflict-report-2026-08-28-daily-tool --> merge-conflict-report-2026-08-28
  merge-conflict-report-2026-08-28-daily-tool --> daily-tool-replace-vault-2026-08-27
  merge-conflict-report-agent-facing-2026-08-28 --> ship
  merge-conflict-report-agent-facing-2026-08-28 --> context-graph
  merge-conflict-report-agent-facing-2026-08-28 --> llm-wiki
  merge-conflict-report-agent-facing-2026-08-28 --> tokens-as-capital
  merge-conflict-report-agent-facing-2026-08-28 --> self-verification
  merge-conflict-report-agent-facing-2026-08-28 --> verifiable-instructions
  merge-conflict-report-agent-facing-2026-08-28 --> hunt-ship-loop
  merge-conflict-report-agent-facing-2026-08-28 --> MEMORY
  ontology-rebuild-brief-2026-08-28 --> llm-wiki
  ontology-rebuild-brief-2026-08-28 --> file-memory
  ontology-rebuild-brief-2026-08-28 --> context-graph
  ingest-brief-2026-08-24-disclosure-index --> disclosures
  merge-conflict-report-entropy-quiz-2026-08-28 --> graph-clusters-2026-08-24
  merge-conflict-report-entropy-quiz-2026-08-28 --> query-entropy-gate
  merge-conflict-report-entropy-quiz-2026-08-28 --> query-skills-and-slop
  daily-tool-replace-vault-2026-08-27 --> daily-tool-replace
  daily-tool-replace-vault-2026-08-27 --> src-can1357-daily-tool-replace-2026-08-27
  daily-tool-replace-vault-2026-08-27 --> file-memory
  daily-tool-replace-vault-2026-08-27 --> ingest-brief-2026-08-24-arxiv-405856
  daily-tool-replace-vault-2026-08-27 --> tokens-as-capital
  daily-tool-replace-vault-2026-08-27 --> can-boluk
  ingest-brief-2026-08-26-headlong --> headlong
  ingest-brief-2026-08-26-headlong --> src-hxiao-headlong
  ingest-brief-2026-08-26-headlong --> src-laude-headlong
  ingest-brief-2026-08-27-claim-protocol --> claim-protocol
  ingest-brief-2026-08-27-claim-protocol --> llm-wiki
  ingest-brief-2026-08-27-claim-protocol --> claims
  ingest-brief-2026-08-27-claim-protocol --> portable-memory
  ingest-brief-2026-08-27-claim-protocol --> file-memory
  ingest-brief-2026-08-24 --> verifiable-instructions
  ingest-brief-2026-08-24 --> context-graph
  ingest-brief-2026-08-24 --> tokens-as-capital
  ingest-brief-2026-08-24 --> llm-wiki
  ingest-brief-2026-08-24 --> self-verification
  ingest-brief-2026-08-27-can1357-daily-tool --> daily-tool-replace
  ingest-brief-2026-08-27-can1357-daily-tool --> src-can1357-daily-tool-replace-2026-08-27
  ingest-brief-2026-08-27-can1357-daily-tool --> can-boluk
  ingest-brief-2026-08-27-can1357-daily-tool --> anti-slop
  ingest-brief-2026-08-27-can1357-daily-tool --> harness-routing
  memory-engine-2026-08-28 --> claims
  memory-system-brief-2026-08-27 --> memory-system
  memory-system-brief-2026-08-27 --> epistemic-labels
  memory-system-brief-2026-08-27 --> provenance
  memory-system-brief-2026-08-27 --> claims
  memory-system-brief-2026-08-27 --> untrusted-ingest
  memory-system-brief-2026-08-27 --> llm-wiki
  memory-system-brief-2026-08-27 --> file-memory
  memory-system-brief-2026-08-27 --> portable-memory
  merge-conflict-report-2026-08-28 --> ship
  merge-conflict-report-2026-08-28 --> anti-slop
  merge-conflict-report-2026-08-28 --> tokens-as-capital
  merge-conflict-report-2026-08-28 --> verifiable-instructions
  merge-conflict-report-2026-08-28 --> context-graph
  merge-conflict-report-2026-08-28 --> harness-routing
  merge-conflict-report-2026-08-28 --> memory-engineering
  merge-conflict-report-2026-08-28 --> llm-wiki
  query-entropy-gate --> entropy-gate
  query-entropy-gate --> src-hitu-entropy-engineering
  query-entropy-gate --> audited-task-contract
  agent-operating-system --> llm-wiki
  agent-operating-system --> memory-engineering
  agent-operating-system --> audited-task-contract
  agent-operating-system --> verifiable-instructions
  agent-operating-system --> hunt-ship-loop
  anti-slop --> src-juampi-anti-slop-rank
  anti-slop --> verifiable-instructions
  anti-slop --> daily-tool-replace
  anti-slop --> src-can1357-daily-tool-replace-2026-08-27
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
  entropy-gate --> headlong
  entropy-gate --> audited-task-contract
  entropy-gate --> harness-routing
  entropy-gate --> self-verification
  entropy-gate --> memory-engineering
  entropy-gate --> claim-protocol
  file-memory --> claims
  file-memory --> memory-system
  file-memory --> claim-protocol
  file-memory --> llm-wiki
  file-memory --> memory-engineering
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
  harness-routing --> daily-tool-replace
  harness-routing --> headlong
  harness-routing --> src-can1357-daily-tool-replace-2026-08-27
  hunt-ship-loop --> src-avid-obsidian-agent-team
  hunt-ship-loop --> hunt
  hunt-ship-loop --> ship
  hunt-ship-loop --> maps
  hunt-ship-loop --> growth-operator
  hunt-ship-loop --> llm-wiki
  hunt-ship-loop --> context-graph
  llm-wiki --> claim-protocol
  llm-wiki --> stale-fact-detector
  llm-wiki --> memory-system
  llm-wiki --> tokens-as-capital
  llm-wiki --> andrej-karpathy
  llm-wiki --> src-papa-couch-compiler
  llm-wiki --> src-bober-folder-workflow
  llm-wiki --> growth-operator
  llm-wiki --> file-memory
  llm-wiki --> portable-memory
  llm-wiki --> claims
  llm-wiki --> untrusted-ingest
  memory-ablation --> src-0xcodio-memory-ablation
  memory-ablation --> memory-engineering
  memory-ablation --> verifiable-instructions
  memory-ablation --> claim-protocol
  memory-ablation --> claims
  memory-engineering --> src-0xcodio-memory-ablation
  memory-engineering --> claim-protocol
  memory-engineering --> hunt
  memory-engineering --> ship
  memory-engineering --> memory-ablation
  memory-engineering --> context-graph
  memory-engineering --> audited-task-contract
  memory-engineering --> entropy-gate
  memory-engineering --> file-memory
  memory-engineering --> memory-system
  memory-engineering --> epistemic-labels
  memory-engineering --> claims
  memory-engineering --> headlong
  portable-memory --> file-memory
  portable-memory --> llm-wiki
  portable-memory --> claims
  portable-memory --> claim-protocol
  portable-memory --> memory-system
  self-verification --> src-jacky-self-verification
  self-verification --> jacky-kwok
  self-verification --> verifiable-instructions
  self-verification --> entropy-gate
  self-verification --> claim-protocol
  stale-fact-detector --> claims
  stale-fact-detector --> claim-protocol
  stale-fact-detector --> llm-wiki
  stale-fact-detector --> memory-ablation
  stale-fact-detector --> verifiable-instructions
  stale-fact-detector --> provenance
  tokens-as-capital --> src-papa-couch-compiler
  tokens-as-capital --> llm-wiki
  tokens-as-capital --> context-graph
  verifiable-instructions --> src-voxyz-verifiable-instructions
  verifiable-instructions --> memory-ablation
  verifiable-instructions --> self-verification
  verifiable-instructions --> anti-slop
  epistemic-labels --> memory-system
  epistemic-labels --> claims
  epistemic-labels --> memory-ablation
  epistemic-labels --> provenance
  epistemic-labels --> verifiable-instructions
  epistemic-labels --> anti-slop
  headlong --> src-laude-headlong
  headlong --> src-hxiao-headlong
  headlong --> ingest-brief-2026-08-26-headlong-hour
  headlong --> entropy-gate
  headlong --> harness-routing
  headlong --> audited-task-contract
  headlong --> memory-engineering
  memory-system --> file-memory
  memory-system --> portable-memory
  memory-system --> llm-wiki
  memory-system --> memory-ablation
  memory-system --> memory-engineering
  memory-system --> untrusted-ingest
  memory-system --> claims
  memory-system --> epistemic-labels
  memory-system --> provenance
  memory-system --> stale-fact-detector
  daily-tool-replace --> src-can1357-daily-tool-replace-2026-08-27
  daily-tool-replace --> can-boluk
  daily-tool-replace --> anti-slop
  daily-tool-replace --> daily-tool-replace-vault-2026-08-27
  daily-tool-replace --> harness-routing
  provenance --> memory-system
  provenance --> claims
  provenance --> epistemic-labels
  provenance --> stale-fact-detector
  provenance --> audited-task-contract
  provenance --> llm-wiki
  untrusted-ingest --> memory-system
  untrusted-ingest --> entropy-gate
  untrusted-ingest --> verifiable-instructions
  untrusted-ingest --> provenance
  untrusted-ingest --> claims
  untrusted-ingest --> epistemic-labels
  untrusted-ingest --> llm-wiki
  claims --> file-memory
  claims --> provenance
  claims --> epistemic-labels
  claims --> untrusted-ingest
  claims --> stale-fact-detector
  claims --> memory-system
  claims --> portable-memory
  claims --> memory-ablation
  claim-protocol --> src-lan-e-claim-protocol-2026-08-27
  claim-protocol --> claims
  claim-protocol --> portable-memory
  claim-protocol --> file-memory
  claim-protocol --> llm-wiki
  claim-protocol --> memory-engineering
  claim-protocol --> memory-ablation
  claim-protocol --> context-graph
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
  can-boluk --> src-can1357-daily-tool-replace-2026-08-27
  can-boluk --> daily-tool-replace
  can-boluk --> anti-slop
  can-boluk --> harness-routing
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
  src-lan-e-claim-protocol-2026-08-27 --> claims
  src-lan-e-claim-protocol-2026-08-27 --> llm-wiki
  src-lan-e-claim-protocol-2026-08-27 --> memory-engineering
  src-lan-e-claim-protocol-2026-08-27 --> context-graph
  src-lan-e-claim-protocol-2026-08-27 --> stale-fact-detector
  src-laude-headlong --> headlong
  src-laude-headlong --> src-hxiao-headlong
  src-laude-headlong --> harness-routing
  src-laude-headlong --> entropy-gate
  src-hxiao-headlong --> headlong
  src-hxiao-headlong --> src-laude-headlong
  src-hxiao-headlong --> harness-routing
  src-can1357-daily-tool-replace-2026-08-27 --> daily-tool-replace
  src-can1357-daily-tool-replace-2026-08-27 --> can-boluk
  src-can1357-daily-tool-replace-2026-08-27 --> anti-slop
  src-can1357-daily-tool-replace-2026-08-27 --> harness-routing
```
<!-- graph-mermaid:end -->
