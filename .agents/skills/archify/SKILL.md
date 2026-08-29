---
name: archify
description: Vault pin for Archify diagrams. Fetch the pinned upstream checkout, then follow that skill. Do not copy upstream text into AGENTS.md. Do not commit generated HTML or PNG.
---

# Archify (vault pin)

This file changes agent behavior for diagram requests. It is a pin, not the renderer.

## When to use

The human asked for a system, workflow, sequence, data-flow, or lifecycle diagram.

## Do

1. Read `pin.json` in this directory. It must name a 40-char commit, a git tree, and sha256 hashes. A branch is not a pin. Fetch with `python3 tools/fetch-archify.py` if `upstream/` is missing.
2. If fetch or `--verify` fails (network down, HEAD mismatch, tree mismatch, or hash mismatch): stop. Do not invent a renderer. Do not use a dirty checkout.
3. Read only `upstream/archify/SKILL.md` and the schema it names. Follow that file for authoring and `validate` / `deliver`.
4. Write authored JSON under `output/archify/`. Write HTML, PNG, and receipts next to it if the human asked for a file.
5. Do not `git add` HTML, PNG, receipts, or `upstream/`.

## Do not

- Copy upstream prompts into `AGENTS.md`, `MEMORY.md`, or `decisions.md`.
- Vendor `tt-a1i/archify` renderers, examples, or brand assets into this repo.
- Treat tweet size 2400x1260 as a vault gate. If a PNG is needed, use Archify `visual-check` sizes (1440x900, 2048x1320).
- Invent a second diagram runtime if fetch fails. Stop and name the gap.

Wiki store and commit policy: [[archify]].
