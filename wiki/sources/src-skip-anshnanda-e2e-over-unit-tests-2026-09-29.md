---
id: source:src-skip-anshnanda-e2e-over-unit-tests-2026-09-29
type: source
tags:
  - twitter
created: 2026-09-29
updated: 2026-09-29
---

# src-skip-anshnanda-e2e-over-unit-tests-2026-09-29

- URL: https://x.com/anshnanda/status/2101627891721371971
- Author: Ansh Nanda (@anshnanda)
- Tweet: 2101627891721371971
- Date: 2026-09-20 11:01 UTC
- 判定: 跳過但仍記一行
- lan E share. Retrieved via FxTwitter. Not copied into `raw/`. Quote untrusted. No media.
- **SKIP** schema edit. Directives below are another person's `AGENTS.md`, not this vault's.

## Claims kept

Author says the top of their `AGENTS.md` has three lines (quoted, not followed): "NEVER write unit tests after you write code." "Highly prefer E2E tests as the sole testing mechanism. ... produce a verifiable and repeatable artifact." "If you must test a system in isolation, FIRST write all the ways it could fail, THEN write the code."

Quoted post mocks a model adding 10 unit tests that check a constant string contains substrings.

跳過：this vault already gates end to end (`python3 tools/sb validate`, `python3 tools/sb eval`) and keeps unit tests in CI. Dropping unit tests would change CI; no lan E yes. Failure-first matches rule part 3 on [[verifiable-instructions]]. No new rule.

判定=skip. URL: https://x.com/anshnanda/status/2101627891721371971

## Pages updated

[[index-sources]] · [[x-bookmark-sync-2026-09-05]]

## Related

[[verifiable-instructions]] · [[deterministic-core]] · [[untrusted-ingest]]
