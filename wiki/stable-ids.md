---
id: concept:stable-ids
type: concept
tags:
  - wiki
created: 2026-08-28
updated: 2026-08-28
---

# Stable IDs

Every knowledge object has `id:` in frontmatter. Filenames can change without destroying identity.

Shape: `kind:slug`. Kinds: source, concept, claim, person, project, decision, experiment, contradiction, meta, memory.

Stamp missing ids with `python3 tools/sb rebuild-index --write-ids`. `python3 tools/sb validate` fails if a compiled page lacks `id:`.

## Related

[[claims]] · [[retrieval]] · [[llm-wiki]]
