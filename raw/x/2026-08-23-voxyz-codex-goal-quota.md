# Source: Voxyz on leftover Codex quota and /goal

- URL: https://x.com/voxyz_ai/status/2091603024817062192
- Author: Vox (@Voxyz_ai)
- Date: 2026-08-23
- Retrieved: 2026-08-24 via fxtwitter (header) and threadreaderapp.com/thread/2091603024817062192.html (five replies). Official X API returned pay-per-use forbidden.

## Header

𝗖𝗼𝗱𝗲𝘅 𝘁𝗶𝗽: if you still have half your quota left when it resets, you’re throwing away days of Sol.

Use `/goal` to squeeze every last bit out of it: audit your entire site, map your codebase, speed up your app, or even clear out the half-finished work in your workspace.

Here are 5 copy-paste prompts. ↓

## 1/5 Run a complete UI/UX audit with 3 skills

/goal Launch the real site for this project and use the three skills below to audit and improve it: → `$ux-audit`: click, type, and complete the core flows like a real user. Find anything confusing, hard to use, or simply broken. → `$impeccable`: review the visual hierarchy, typography, spacing, component consistency, mobile experience, and every important UI state. → `$transitions-dev`: review the existing motion and add the right transitions wherever feedback or a state change needs to feel clearer. First check whether all three skills are available. If one is missing, use the skill installer to install it from the original source, load it, and continue. If `$ux-audit` is marked Claude Code-only and can’t be called directly, read its `SKILL.md` and follow its interaction-first workflow. Start with `$ux-audit` to walk through the entire product. Then use `$impeccable` to fix the visual and UX issues. Finish with `$transitions-dev` to review dropdowns, modals, tabs, loading, success, error, and other state changes. Don’t stop at a report. Fix the issues, then run through the core flows again. Finish with: → Desktop and mobile before/after screenshots → The 5 most important improvements → Anything still unresolved → A final version I can open and test

## 2/5 Build a clickable map of the entire codebase

/goal Analyze the current codebase and generate an interactive code map that opens directly in a browser. The map should include: → Major modules, services, databases, and external dependencies → Calls and data flows between modules → The 3–5 most important end-to-end flows → The tests and source evidence behind each module Clicking any module should show its role, upstream callers, dependencies, downstream impact, and related tests. Keep the first screen to no more than 20 primary nodes. Group lower-level files under their parent modules so the map doesn’t turn into a tangled mess. Output: → docs/codemap/codemap.html → docs/codemap/codemap.json → docs/codemap/codemap.lock When finished, open the map and verify that every path, node, and flow matches the current codebase.

## 3/5 Make the app measurably faster

/goal Make this app measurably faster. Launch the real app and run through [CORE FLOW]. Record the current load time, interaction responsiveness, CPU usage, memory usage, and any visible stutters. Use those measurements to find the worst bottlenecks. Don’t guess. Change one thing at a time. After every change, rerun the exact same flow. Keep the change if the app gets faster. Revert it if nothing improves. Continue until the core flow no longer has any obvious bottlenecks. Finish with a simple before/after report: → The original measurements → What you changed → The new measurements → Any bottlenecks you didn’t address

## 4/5 Clean up the entire workspace

/goal Review every project under [WORKSPACE PATH] and clean up the half-finished work that has piled up. Create a short card for every project: → What it does → When the last meaningful change happened → Whether it still runs → What remains unfinished → Whether it overlaps with another project Then classify each one as: → Keep working → Finish soon → Merge candidate → Archive candidate → Delete candidate Pick the 3 highest-value unfinished tasks and complete the obvious parts. Do not delete, merge, push, or deploy anything. Leave those actions in the final list. Finish with an overview of the entire workspace and the 10 most valuable things to work on next.

## 5/5 Clean up Codex itself

/goal Audit my current Codex setup, including AGENTS.md, skills, custom agents, commands, plugins, MCP servers, and automations. Find: → Duplicated functionality → Stale or unused items → Conflicting rules → Anything consuming unnecessary context → Workflows that still require manual cleanup Back up the current configuration first. Then merge obvious duplicates, shorten bloated rules, move stale items into an archive, and fix broken paths or configuration. Next, generate a clickable toolkit map. Clicking any item should show its purpose, trigger, scope, source, and overlap with other tools. Finish by telling me: → What you cleaned up → How much context you saved → What should still be deleted or rewritten → The 10 tools most worth keeping
