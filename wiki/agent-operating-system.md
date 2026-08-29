---
id: meta:agent-operating-system
type: meta
tags:
  - wiki
created: 2026-08-23
updated: 2026-08-29
---

# Agent operating system

Synthesis of the compiled posts through [[src-omarsar-adversarial-review]] and [[src-jerry-two-pass-docs]]. File this back so later sessions do not rebuild it from the posts.

## Stack

Five layers, one vault.

1. **Compile, then retrieve the compiled set.** [[llm-wiki]] + [[tokens-as-capital]] + [[retrieval]] + [[claim-protocol]]. `raw/` is input. `wiki/` is the brain. `output/` is built from the wiki. The agent queries through `python3 tools/sb ask`, not by walking [[index]] (D9, C37). [[agent-facing-docs]] measured that instruction files and working notes take most of an agent's documentation attention.
2. **Remember only what changes answers.** [[memory-engineering]] + [[memory-ablation]] + [[memory-system]]. Capture is a filter. Adjectives die. Conflicts `flag_conflict`. New claims are FACT, INFERENCE, or OPINION.
3. **Share a contract, not a chat.** [[audited-task-contract]] + [[harness-routing]] + [[entropy-gate]] + [[raptor-dispatch]] + [[secret-gateway]]. Planner proposes. Deterministic controller commits. Isolated worktrees. Validated diffs. One owner per job. Credentials stay in a runtime, not in the prompt. [[adversarial-review]] freezes the artifact while a reviewer and critic argue, then the writer edits.
4. **Check instead of wishing.** [[verifiable-instructions]] + [[self-verification]] + [[anti-slop]]. Every schema rule has a check. High-risk answers get scored against citations. Reading `AGENTS.md` is not the check. See D10 and [[agent-facing-docs]]. [[ultra-mode]] is the coding-agent product of that loop: N isolated worktrees, [[probabilistic-pivot-tournament]], uncommitted apply.
5. **Keep a human gate.** [[hunt-ship-loop]] + [[clip-pipeline]] + [[skillspector]]. File first. Scouts write quietly. Vault does not post, pay, or send. Generated skills wait for SkillSpector. Operating order: [[musk-algorithm]].

[[growth-operator]] is this stack applied to partner ops: compiled notes in `growth/`, rulings instead of re-arguing, human yes before money.

[[skill-library]] is adjacent: discover and reuse known patterns instead of rebuilding them. It does not replace compile-into-`wiki/`. A starred GitHub skill dump is still a dump. A local SOP is [[skill-as-sop]]. A retrieval stack is [[retrieval-second-brain]]. D1 stays.

Document dumps are a separate layer. [[two-pass-document-processing]] covers ad-hoc data rooms. See [[contradictions]] C44.

## What this batch does not prove

Viral clips are not methods. See [[contradictions]]. Planning-first best-of-N changed 0 of 5 outcomes in [[src-maverick-ultramode]]. Adding more agents is the wrong first review fix in [[src-omarsar-adversarial-review]].
The [[src-johnsjawn-skill-library]] demo shows usage counts. It does not show skills rewriting themselves after use.

The wiki is still below the 50-100 source density [[src-papa-couch-compiler]] says is needed before compilation beats a good search. Treat today's pages as a seed, not a finished graph.

## Related

[[how-it-works]] · [[index]] · [[claim-protocol]] · [[contradictions]] · [[two-pass-document-processing]] · [[ultra-mode]] · [[adversarial-review]] · [[src-play-methods-2026-08-25]] · [[growth-operator]] · [[memory-system]] · [[retrieval]] · [[claims]] · [[eval-suite]] · [[vault-ontology]] · [[agent-facing-docs]]

[[src-thewhizzai-avo]] is a harness-vs-model score tweet. 30.2→100 is `unverified` (no paper).

[[src-chatchat-living-brain]] is a product tweet for persistent agent context.

[[src-avid-company-foundry]] is a Grok + Obsidian Jarvis clip quoting Company Foundry. Compile [[company-foundry]]. Clip claims `unverified`. C31.

[[src-can1357-daily-tool-replace-2026-08-27]] is a daily-flow replace tweet. Hour tops is `unverified` as a general bound. See [[daily-tool-replace]].

[[headlong]] is a persistent Bash microharness (Laude/MIT). 2026-08-26 installed tools; 1h identity `hour` ran on local Ollama and stopped 02:07Z; tests did not run. One shared stream vs layer 3 isolation: C16. Not the wiki compiler.

[[src-exm7777-grok-bot-money]] is a Grok Bot product how-to. One bot per workflow. Vault over bot memory. Approvals. Shared computer is not an entropy gate. See [[grok-bot]] and C30.

[[src-4ndrearossetti-openconnector]] is a secret-gateway tweet. OpenConnector counts `unverified`. Browser inject vs API catalog is C40.

[[src-avichawla-trueforge]] is a harness-token article. 2.7x is `unverified`. See [[flat-context]] and C41.

[[src-alexprompter-claude-projects]] is a Claude Projects how-to. Product workspace, not this wiki. See [[project-skill-stack]] and C42.

[[src-voxyz-writing-system]] is a 6/6 `/goal` writing prompt. Third list. Keep D6. See C43. C6 stays open.
