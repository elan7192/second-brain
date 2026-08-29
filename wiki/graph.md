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

`path:wiki OR path:maps OR path:hunt OR path:ship OR path:output OR file:Home OR file:MEMORY -file:index -file:index-papers -file:index-sources -file:log -file:twitter`

Those hidden files stay in the vault. They are doors and timelines, not concept peers.

Forces: low center pull, higher repel, longer link distance. Peer concept links on those pages do the clustering.

## Islands

Taken from [[agent-operating-system]].

| Island | Pages |
| --- | --- |
| Compile | llm-wiki, tokens-as-capital, context-graph, retrieval, claims, stable-ids, claim-protocol |
| Memory | memory-engineering, memory-ablation, portable-memory, memory-system, claims, project-skill-stack |
| Verification | verifiable-instructions, self-verification, anti-slop |
| Harness | audited-task-contract, harness-routing, entropy-gate, secret-gateway, flat-context |
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
    project-skill-stack
    provenance
    src-0xcodio-memory-ablation
    src-alexprompter-claude-projects
    untrusted-ingest
  end
  subgraph verification[Verification]
    anti-slop
    jacky-kwok
    self-verification
    src-jacky-self-verification
    src-juampi-anti-slop-rank
    src-voxyz-verifiable-instructions
    src-voxyz-writing-system
    stale-fact-detector
    verifiable-instructions
  end
  subgraph harness[Harness]
    audited-task-contract
    can-boluk
    company-foundry
    daily-tool-replace
    entropy-gate
    grok-bot
    grok-bot-money
    grok-bot-use-cases
    harness-routing
    headlong
    rohit
    secret-gateway
    flat-context
    src-4ndrearossetti-openconnector
    src-avichawla-trueforge
    src-can1357-daily-tool-replace-2026-08-27
    src-exm7777-grok-bot-money
    src-hitu-entropy-engineering
    src-hxiao-headlong
    src-laude-headlong
    src-milesdeutscher-grok-bot-use-cases
    src-rohit-harness-router
  end
  subgraph hunt-ship[Hunt / ship]
    GrowthOS
    avid
    daily-tool-replace-vault-2026-08-27
    deer-flow-bootstrap-2026-08-24
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
    ingest-brief-2026-08-24-disclosure-index
    ingest-brief-2026-08-24-maverick-ultramode
    ingest-brief-2026-08-25-avid-company-foundry
    ingest-brief-2026-08-25-exm7777-grok-bot
    ingest-brief-2026-08-25-growthos
    ingest-brief-2026-08-25-play-methods
    ingest-brief-2026-08-25-skill-recorder
    ingest-brief-2026-08-26-headlong
    ingest-brief-2026-08-26-headlong-hour
    ingest-brief-2026-08-27-botdirectory
    ingest-brief-2026-08-27-can1357-daily-tool
    ingest-brief-2026-08-27-claim-protocol
    ingest-brief-2026-08-27-lanbb-bb
    ingest-brief-omarsar-2026-08-24
    maps
    memory-engine-2026-08-28
    memory-system-brief-2026-08-27
    merge-conflict-report-2026-08-28
    merge-conflict-report-2026-08-28-avid-foundry
    merge-conflict-report-2026-08-28-daily-tool
    merge-conflict-report-2026-08-28-daily-tool-2
    merge-conflict-report-2026-08-28-deer-flow
    merge-conflict-report-2026-08-28-grok-bot
    merge-conflict-report-2026-08-28-maverick-ultramode
    merge-conflict-report-2026-08-28-omarsar
    merge-conflict-report-agent-facing-2026-08-28
    merge-conflict-report-entropy-quiz-2026-08-28
    ontology-rebuild-brief-2026-08-28
    query-entropy-gate
    query-skills-and-slop
    ship
    src-avid-company-foundry
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
  MEMORY --> grok-bot-use-cases
  MEMORY --> headlong
  MEMORY --> growth-operator
  MEMORY --> company-foundry
  MEMORY --> grok-bot
  MEMORY --> entropy-gate
  MEMORY --> src-exm7777-grok-bot-money
  MEMORY --> grok-bot-money
  hunt --> hunt-ship-loop
  hunt --> disclosures
  maps --> GrowthOS
  ship --> ingest-brief-2026-08-23
  ship --> ingest-brief-2026-08-23-skill-library
  ship --> ingest-brief-2026-08-23-cybersecurity-skills
  ship --> ingest-brief-2026-08-23-skill-pack-list
  ship --> ingest-brief-2026-08-23-retrieval-second-brain
  ship --> graph-clusters-2026-08-24
  ship --> ingest-brief-2026-08-25-avid-company-foundry
  ship --> ontology-rebuild-brief-2026-08-28
  ship --> merge-conflict-report-2026-08-28
  ship --> merge-conflict-report-2026-08-28-avid-foundry
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
  ingest-brief-2026-08-25-growthos --> growth-operator
  ingest-brief-2026-08-25-growthos --> src-deronin-growthos-vault
  ingest-brief-2026-08-25-growthos --> GrowthOS
  ingest-brief-2026-08-25-growthos --> growth-briefing-2026-08-25
  ingest-brief-2026-08-25-play-methods --> hunt-ship-loop
  ingest-brief-2026-08-25-play-methods --> llm-wiki
  ingest-brief-2026-08-25-play-methods --> audited-task-contract
  ingest-brief-2026-08-25-play-methods --> harness-routing
  ingest-brief-2026-08-27-botdirectory --> stale-fact-detector
  merge-conflict-report-2026-08-28-avid-foundry --> company-foundry
  merge-conflict-report-2026-08-28-avid-foundry --> src-avid-company-foundry
  merge-conflict-report-2026-08-28-avid-foundry --> avid
  merge-conflict-report-2026-08-28-avid-foundry --> MEMORY
  ingest-brief-2026-08-26-headlong --> headlong
  ingest-brief-2026-08-26-headlong --> src-hxiao-headlong
  ingest-brief-2026-08-26-headlong --> src-laude-headlong
  ingest-brief-2026-08-24-disclosure-index --> disclosures
  ingest-brief-2026-08-23-retrieval-second-brain --> memory-engineering
  ingest-brief-2026-08-23-retrieval-second-brain --> context-graph
  ingest-brief-2026-08-23-retrieval-second-brain --> llm-wiki
  ontology-rebuild-brief-2026-08-28 --> llm-wiki
  ontology-rebuild-brief-2026-08-28 --> file-memory
  ontology-rebuild-brief-2026-08-28 --> context-graph
  daily-tool-replace-vault-2026-08-27 --> daily-tool-replace
  daily-tool-replace-vault-2026-08-27 --> src-can1357-daily-tool-replace-2026-08-27
  daily-tool-replace-vault-2026-08-27 --> file-memory
  daily-tool-replace-vault-2026-08-27 --> ingest-brief-2026-08-24-arxiv-405856
  daily-tool-replace-vault-2026-08-27 --> tokens-as-capital
  daily-tool-replace-vault-2026-08-27 --> can-boluk
  ingest-brief-2026-08-24 --> verifiable-instructions
  ingest-brief-2026-08-24 --> context-graph
  ingest-brief-2026-08-24 --> tokens-as-capital
  ingest-brief-2026-08-24 --> llm-wiki
  ingest-brief-2026-08-24 --> self-verification
  ingest-brief-2026-08-25-exm7777-grok-bot --> grok-bot
  ingest-brief-2026-08-25-exm7777-grok-bot --> grok-bot-money
  memory-system-brief-2026-08-27 --> memory-system
  memory-system-brief-2026-08-27 --> epistemic-labels
  memory-system-brief-2026-08-27 --> provenance
  memory-system-brief-2026-08-27 --> claims
  memory-system-brief-2026-08-27 --> untrusted-ingest
  memory-system-brief-2026-08-27 --> llm-wiki
  memory-system-brief-2026-08-27 --> file-memory
  memory-system-brief-2026-08-27 --> portable-memory
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
  memory-engine-2026-08-28 --> claims
  ingest-brief-2026-08-27-claim-protocol --> claim-protocol
  ingest-brief-2026-08-27-claim-protocol --> llm-wiki
  ingest-brief-2026-08-27-claim-protocol --> claims
  ingest-brief-2026-08-27-claim-protocol --> portable-memory
  ingest-brief-2026-08-27-claim-protocol --> file-memory
  ingest-brief-2026-08-23-skill-pack-list --> tokens-as-capital
  ingest-brief-2026-08-23-skill-pack-list --> verifiable-instructions
  ingest-brief-2026-08-27-can1357-daily-tool --> daily-tool-replace
  ingest-brief-2026-08-27-can1357-daily-tool --> src-can1357-daily-tool-replace-2026-08-27
  ingest-brief-2026-08-27-can1357-daily-tool --> can-boluk
  ingest-brief-2026-08-27-can1357-daily-tool --> anti-slop
  ingest-brief-2026-08-27-can1357-daily-tool --> harness-routing
  merge-conflict-report-2026-08-28 --> ship
  merge-conflict-report-2026-08-28 --> anti-slop
  merge-conflict-report-2026-08-28 --> tokens-as-capital
  merge-conflict-report-2026-08-28 --> verifiable-instructions
  merge-conflict-report-2026-08-28 --> context-graph
  merge-conflict-report-2026-08-28 --> harness-routing
  merge-conflict-report-2026-08-28 --> memory-engineering
  merge-conflict-report-2026-08-28 --> llm-wiki
  merge-conflict-report-2026-08-28-daily-tool-2 --> daily-tool-replace-vault-2026-08-27
  ingest-brief-2026-08-25-avid-company-foundry --> company-foundry
  ingest-brief-2026-08-25-avid-company-foundry --> hunt-ship-loop
  ingest-brief-2026-08-25-avid-company-foundry --> harness-routing
  ingest-brief-2026-08-25-avid-company-foundry --> audited-task-contract
  ingest-brief-2026-08-25-avid-company-foundry --> entropy-gate
  ingest-brief-2026-08-25-avid-company-foundry --> memory-engineering
  ingest-brief-omarsar-2026-08-24 --> entropy-gate
  ingest-brief-omarsar-2026-08-24 --> audited-task-contract
  ingest-brief-omarsar-2026-08-24 --> self-verification
  ingest-brief-2026-08-24-maverick-ultramode --> self-verification
  ingest-brief-2026-08-24-maverick-ultramode --> entropy-gate
  ingest-brief-2026-08-24-maverick-ultramode --> harness-routing
  ingest-brief-2026-08-24-maverick-ultramode --> jacky-kwok
  merge-conflict-report-entropy-quiz-2026-08-28 --> graph-clusters-2026-08-24
  merge-conflict-report-entropy-quiz-2026-08-28 --> query-entropy-gate
  merge-conflict-report-entropy-quiz-2026-08-28 --> query-skills-and-slop
  ingest-brief-2026-08-23-cybersecurity-skills --> tokens-as-capital
  ingest-brief-2026-08-23-cybersecurity-skills --> context-graph
  merge-conflict-report-2026-08-28-maverick-ultramode --> ship
  merge-conflict-report-2026-08-28-maverick-ultramode --> entropy-gate
  merge-conflict-report-2026-08-28-maverick-ultramode --> harness-routing
  merge-conflict-report-2026-08-28-maverick-ultramode --> self-verification
  merge-conflict-report-2026-08-28-maverick-ultramode --> MEMORY
  merge-conflict-report-2026-08-28-maverick-ultramode --> ingest-brief-2026-08-24-maverick-ultramode
  merge-conflict-report-agent-facing-2026-08-28 --> ship
  merge-conflict-report-agent-facing-2026-08-28 --> context-graph
  merge-conflict-report-agent-facing-2026-08-28 --> llm-wiki
  merge-conflict-report-agent-facing-2026-08-28 --> tokens-as-capital
  merge-conflict-report-agent-facing-2026-08-28 --> self-verification
  merge-conflict-report-agent-facing-2026-08-28 --> verifiable-instructions
  merge-conflict-report-agent-facing-2026-08-28 --> hunt-ship-loop
  merge-conflict-report-agent-facing-2026-08-28 --> MEMORY
  merge-conflict-report-2026-08-28-grok-bot --> grok-bot
  merge-conflict-report-2026-08-28-grok-bot --> entropy-gate
  merge-conflict-report-2026-08-28-grok-bot --> MEMORY
  merge-conflict-report-2026-08-28-omarsar --> ship
  merge-conflict-report-2026-08-28-omarsar --> entropy-gate
  merge-conflict-report-2026-08-28-omarsar --> audited-task-contract
  merge-conflict-report-2026-08-28-omarsar --> self-verification
  merge-conflict-report-2026-08-28-omarsar --> ingest-brief-omarsar-2026-08-24
  ingest-brief-2026-08-26-headlong-hour --> headlong
  ingest-brief-2026-08-26-headlong-hour --> harness-routing
  ingest-brief-2026-08-26-headlong-hour --> entropy-gate
  query-entropy-gate --> entropy-gate
  query-entropy-gate --> src-hitu-entropy-engineering
  query-entropy-gate --> audited-task-contract
  ingest-brief-2026-08-23-skill-library --> tokens-as-capital
  ingest-brief-2026-08-23-skill-library --> anti-slop
  ingest-brief-2026-08-23-skill-library --> llm-wiki
  merge-conflict-report-2026-08-28-daily-tool --> ship
  merge-conflict-report-2026-08-28-daily-tool --> anti-slop
  merge-conflict-report-2026-08-28-daily-tool --> harness-routing
  merge-conflict-report-2026-08-28-daily-tool --> daily-tool-replace
  merge-conflict-report-2026-08-28-daily-tool --> headlong
  merge-conflict-report-2026-08-28-daily-tool --> merge-conflict-report-2026-08-28
  merge-conflict-report-2026-08-28-daily-tool --> daily-tool-replace-vault-2026-08-27
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
  audited-task-contract --> src-avid-company-foundry
  audited-task-contract --> company-foundry
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
  entropy-gate --> src-avid-company-foundry
  entropy-gate --> company-foundry
  entropy-gate --> src-exm7777-grok-bot-money
  entropy-gate --> grok-bot
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
  grok-bot-use-cases --> src-milesdeutscher-grok-bot-use-cases
  grok-bot-use-cases --> llm-wiki
  grok-bot-use-cases --> growth-operator
  grok-bot-use-cases --> src-avid-company-foundry
  grok-bot-use-cases --> company-foundry
  grok-bot-use-cases --> src-exm7777-grok-bot-money
  grok-bot-use-cases --> grok-bot
  grok-bot-use-cases --> grok-bot-money
  grok-bot-use-cases --> hunt-ship-loop
  grok-bot-use-cases --> file-memory
  growth-operator --> src-deronin-growthos-vault
  growth-operator --> GrowthOS
  growth-operator --> src-exm7777-grok-bot-money
  growth-operator --> grok-bot-money
  growth-operator --> gsap-figma-note-2026-08-25
  growth-operator --> context-graph
  growth-operator --> growthos-3d-gap-2026-08-25
  growth-operator --> growth-briefing-2026-08-25
  growth-operator --> grok-bot-use-cases
  growth-operator --> llm-wiki
  growth-operator --> memory-engineering
  growth-operator --> hunt-ship-loop
  harness-routing --> src-rohit-harness-router
  harness-routing --> audited-task-contract
  harness-routing --> src-avid-company-foundry
  harness-routing --> company-foundry
  harness-routing --> entropy-gate
  harness-routing --> rohit
  harness-routing --> grok-bot
  harness-routing --> src-exm7777-grok-bot-money
  harness-routing --> daily-tool-replace
  harness-routing --> headlong
  harness-routing --> src-can1357-daily-tool-replace-2026-08-27
  hunt-ship-loop --> src-avid-obsidian-agent-team
  hunt-ship-loop --> src-avid-company-foundry
  hunt-ship-loop --> hunt
  hunt-ship-loop --> ship
  hunt-ship-loop --> maps
  hunt-ship-loop --> growth-operator
  hunt-ship-loop --> llm-wiki
  hunt-ship-loop --> context-graph
  hunt-ship-loop --> company-foundry
  hunt-ship-loop --> avid
  hunt-ship-loop --> grok-bot
  hunt-ship-loop --> src-exm7777-grok-bot-money
  hunt-ship-loop --> grok-bot-money
  llm-wiki --> claim-protocol
  llm-wiki --> stale-fact-detector
  llm-wiki --> memory-system
  llm-wiki --> tokens-as-capital
  llm-wiki --> context-graph
  llm-wiki --> andrej-karpathy
  llm-wiki --> src-papa-couch-compiler
  llm-wiki --> src-bober-folder-workflow
  llm-wiki --> grok-bot
  llm-wiki --> grok-bot-use-cases
  llm-wiki --> growth-operator
  llm-wiki --> file-memory
  llm-wiki --> portable-memory
  llm-wiki --> claims
  llm-wiki --> untrusted-ingest
  llm-wiki --> company-foundry
  llm-wiki --> src-exm7777-grok-bot-money
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
  memory-engineering --> company-foundry
  memory-engineering --> src-avid-company-foundry
  memory-engineering --> src-exm7777-grok-bot-money
  memory-engineering --> grok-bot
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
  untrusted-ingest --> memory-system
  untrusted-ingest --> entropy-gate
  untrusted-ingest --> verifiable-instructions
  untrusted-ingest --> provenance
  untrusted-ingest --> claims
  untrusted-ingest --> epistemic-labels
  untrusted-ingest --> llm-wiki
  grok-bot-money --> grok-bot
  grok-bot-money --> src-exm7777-grok-bot-money
  grok-bot-money --> grok-bot-use-cases
  grok-bot-money --> hunt-ship-loop
  grok-bot-money --> growth-operator
  epistemic-labels --> memory-system
  epistemic-labels --> claims
  epistemic-labels --> memory-ablation
  epistemic-labels --> provenance
  epistemic-labels --> verifiable-instructions
  epistemic-labels --> anti-slop
  company-foundry --> src-avid-company-foundry
  company-foundry --> hunt-ship-loop
  company-foundry --> harness-routing
  company-foundry --> entropy-gate
  company-foundry --> audited-task-contract
  company-foundry --> memory-engineering
  company-foundry --> llm-wiki
  company-foundry --> avid
  company-foundry --> grok-bot
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
  claims --> file-memory
  claims --> provenance
  claims --> epistemic-labels
  claims --> untrusted-ingest
  claims --> stale-fact-detector
  claims --> memory-system
  claims --> portable-memory
  claims --> memory-ablation
  headlong --> src-laude-headlong
  headlong --> src-hxiao-headlong
  headlong --> ingest-brief-2026-08-26-headlong-hour
  headlong --> entropy-gate
  headlong --> harness-routing
  headlong --> audited-task-contract
  headlong --> memory-engineering
  grok-bot --> src-exm7777-grok-bot-money
  grok-bot --> grok-bot-money
  grok-bot --> grok-bot-use-cases
  grok-bot --> memory-engineering
  grok-bot --> llm-wiki
  grok-bot --> entropy-gate
  grok-bot --> hunt-ship-loop
  grok-bot --> harness-routing
  grok-bot --> company-foundry
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
  avid --> src-avid-obsidian-agent-team
  avid --> src-avid-company-foundry
  avid --> company-foundry
  avid --> hunt-ship-loop
  can-boluk --> src-can1357-daily-tool-replace-2026-08-27
  can-boluk --> daily-tool-replace
  can-boluk --> anti-slop
  can-boluk --> harness-routing
  src-0xcodio-memory-ablation --> memory-engineering
  src-0xcodio-memory-ablation --> memory-ablation
  src-0xcodio-memory-ablation --> verifiable-instructions
  src-avid-obsidian-agent-team --> hunt-ship-loop
  src-avid-obsidian-agent-team --> context-graph
  src-avid-obsidian-agent-team --> avid
  src-avid-obsidian-agent-team --> src-avid-company-foundry
  src-bober-folder-workflow --> llm-wiki
  src-bober-folder-workflow --> andrej-karpathy
  src-deronin-growthos-vault --> growth-operator
  src-deronin-growthos-vault --> grok-bot-use-cases
  src-hitu-entropy-engineering --> entropy-gate
  src-jacky-self-verification --> self-verification
  src-jacky-self-verification --> jacky-kwok
  src-juampi-anti-slop-rank --> anti-slop
  src-milesdeutscher-grok-bot-use-cases --> grok-bot-use-cases
  src-milesdeutscher-grok-bot-use-cases --> llm-wiki
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
  src-avid-company-foundry --> entropy-gate
  src-avid-company-foundry --> company-foundry
  src-avid-company-foundry --> hunt-ship-loop
  src-avid-company-foundry --> harness-routing
  src-avid-company-foundry --> audited-task-contract
  src-avid-company-foundry --> memory-engineering
  src-avid-company-foundry --> grok-bot-use-cases
  src-avid-company-foundry --> avid
  src-exm7777-grok-bot-money --> grok-bot
  src-exm7777-grok-bot-money --> grok-bot-money
  src-exm7777-grok-bot-money --> grok-bot-use-cases
  src-exm7777-grok-bot-money --> memory-engineering
  src-exm7777-grok-bot-money --> llm-wiki
  src-exm7777-grok-bot-money --> entropy-gate
  src-exm7777-grok-bot-money --> hunt-ship-loop
  src-exm7777-grok-bot-money --> harness-routing
  src-exm7777-grok-bot-money --> growth-operator
  src-hxiao-headlong --> headlong
  src-hxiao-headlong --> src-laude-headlong
  src-hxiao-headlong --> harness-routing
  src-can1357-daily-tool-replace-2026-08-27 --> daily-tool-replace
  src-can1357-daily-tool-replace-2026-08-27 --> can-boluk
  src-can1357-daily-tool-replace-2026-08-27 --> anti-slop
  src-can1357-daily-tool-replace-2026-08-27 --> harness-routing
  src-laude-headlong --> headlong
  src-laude-headlong --> src-hxiao-headlong
  src-laude-headlong --> harness-routing
  src-laude-headlong --> entropy-gate
  secret-gateway --> src-4ndrearossetti-openconnector
  secret-gateway --> harness-routing
  secret-gateway --> audited-task-contract
  secret-gateway --> flat-context
  flat-context --> src-avichawla-trueforge
  flat-context --> harness-routing
  flat-context --> secret-gateway
  flat-context --> entropy-gate
  project-skill-stack --> src-alexprompter-claude-projects
  project-skill-stack --> context-graph
  project-skill-stack --> memory-engineering
  project-skill-stack --> llm-wiki
  src-4ndrearossetti-openconnector --> secret-gateway
  src-4ndrearossetti-openconnector --> harness-routing
  src-avichawla-trueforge --> flat-context
  src-avichawla-trueforge --> harness-routing
  src-avichawla-trueforge --> secret-gateway
  src-alexprompter-claude-projects --> project-skill-stack
  src-alexprompter-claude-projects --> context-graph
  src-alexprompter-claude-projects --> memory-engineering
  src-voxyz-writing-system --> anti-slop
  src-voxyz-writing-system --> verifiable-instructions
  src-voxyz-writing-system --> harness-routing
```
<!-- graph-mermaid:end -->
