---
id: concept:palantir-aip
type: concept
tags:
  - wiki
created: 2026-08-28
updated: 2026-08-28
---

# Palantir AIP

Palantir Artificial Intelligence Platform. Application layer on Foundry data and the Ontology.

Source: [[src-palantir-aip-developers-2026-08-28]]. Person: [[alex-karp]]. Local compile: [[vault-ontology]].

## What the pages say

AIP connects models to operational data. Named builder tools: AIP Logic, AIP Chatbot Studio (formerly AIP Agent Studio), AIP Evals. Foundry holds datasets. Apollo is named as mission control for deployment. See the AIP overview URL on the source page.

The Ontology is the operational layer: objects, properties, links (semantic); actions and functions (kinetic). OSDK treats Foundry as a backend. SuperRepo is ontology-as-code.

build.palantir.com publishes example pipelines: parse unstructured text into ontology objects, classify with LLM nodes, query via OSDK.

## What this vault does not do

No Foundry enrollment. No Developer Console app. No live AIP Logic, Workshop, or OSDK against Palantir. D5: the vault does not post, pay, send, or deploy.

Hosted AIP remains a gap until lan E creates an enrollment and says yes.

## Local mapping

[[llm-wiki]] markdown is the dataset. `tools/rebuild-ontology.py` is the pipeline. `output/ontology-objects.csv` is the object table. `tools/ontology.py` is the local query client. That is [[vault-ontology]].

[[ai-sovereignty]] already named Ontology / AIP as the wrap around rented models. Git wiki stays the sovereign store.

[[foundry-3d]] is unrelated. Do not mix it with Palantir Foundry.

## Related

[[vault-ontology]] · [[ai-sovereignty]] · [[alex-karp]] · [[llm-wiki]] · [[context-graph]] · [[file-memory]] · [[src-palantir-aip-developers-2026-08-28]]
