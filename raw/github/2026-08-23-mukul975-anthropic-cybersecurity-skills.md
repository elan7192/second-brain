# Source: mukul975 Anthropic-Cybersecurity-Skills

- URL: https://github.com/mukul975/Anthropic-Cybersecurity-Skills
- Author: Mahipal Jangra (@mukul975)
- Ingested: 2026-08-23
- Repo created: 2026-02-25
- Last push seen: 2026-08-20
- Homepage: https://mahipal.engineer/Anthropic-Cybersecurity-Skills/
- License: Apache-2.0
- Citation name in README: Jangra, Mahipal. "Anthropic Cybersecurity Skills" (2026)

GitHub API snapshot 2026-08-23: 30758 stars, 3663 forks, 47 open issues, default branch main, language Python.

This capture is the public README pitch plus API metadata. Skill bodies, scripts, payloads, and workflow commands were not copied.

## Affiliation

README: independent community project. Not affiliated with Anthropic PBC.

## Disclaimer on the README

The library includes offensive and dual-use techniques. README names red-team C2, phishing simulation, and exploitation. It says authorized and lawful use only, against systems you own or have explicit written permission to test.

## Headline claims

- 817 structured cybersecurity skills
- 29 security domains
- 6 framework mappings: MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, MITRE D3FEND, NIST AI RMF, MITRE F3
- agentskills.io standard
- Works with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI, and other listed platforms
- "largest open-source cybersecurity skills library for AI agents" (author slogan, unverified)

Framework coverage claimed across 817 skills: ATT&CK 805, NIST CSF 2.0 804, D3FEND 139, NIST AI RMF 97, F3 94, ATLAS 93.

ATT&CK claimed as v19.1, 805/817 skills mapped, zero revoked IDs. A later README note still says ATT&CK v19 lands April 28, 2026 and mappings will be updated.

## Domain table (author counts)

Cloud 66, Threat Hunting 58, Threat Intelligence 52, Network 43, Web Application 42, Digital Forensics 41, Malware Analysis 39, IAM 37, SOC 35, Red Teaming 33, Container 33, Security Operations 28, OT/ICS 28, API 28, Incident Response 26, Vulnerability Management 25, Penetration Testing 21, DevSecOps 18, Zero Trust 17, Endpoint 17, Cryptography 16, Phishing Defense 15, AI Security 14, Mobile 13, Ransomware Defense 13, Compliance 9, Supply Chain 8, Deception 6, Hardware & Firmware 4.

Those 29 numbers sum to 785, not 817.

Contributing section still says Deception Technology (2 skills) and Compliance & Governance (5 skills).

v1.0.0 release (2026-03-11): 734 skills, 26 domains.

## How agents use skills (README)

Each skill costs about 30 tokens to scan (frontmatter only) and 500-2000 tokens to fully load. Progressive disclosure: scan all frontmatters, load top matches, follow Workflow, then Verification.

Directory per skill: SKILL.md, references/, scripts/, assets/.

Body sections named: When to Use, Prerequisites, Workflow, Verification.

Frontmatter fields named: name, description, domain, subdomain, tags, atlas_techniques, d3fend_techniques, nist_ai_rmf, nist_csf. ATT&CK mappings said to live in references/standards.md.

## Why it exists (author)

ISC2 2024 workforce gap cited as 4.8 million unfilled roles. Agents lack practitioner playbooks. Author says existing repos give wordlists, payloads, or exploit code, and this repo gives decision workflows. "Every skill encodes real practitioner workflows, not generated summaries." unverified.

## Distribution

README advertises `npx skills add mukul975/Anthropic-Cybersecurity-Skills` and git clone. Also a Casky.ai playground and a GARS-2026 survey.

This vault does not install the pack and does not copy skill workflows.
