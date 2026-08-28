---
id: concept:vending-bench
type: concept
tags:
  - wiki
created: 2026-08-27
updated: 2026-08-27
---

# Vending-Bench

Long-horizon agent eval: inventory, orders, pricing, daily fee.

Source: [[src-andonlabs-vending-bench]] https://andonlabs.com/evals/vending-bench

Fail modes: forget orders, stock-out, doom-loop (close the business, call the FBI).

## Method for this team

- W = units sold with proof (wiki SHA or URL). See [[work-per-cost]].
- E = daily fee (quota).
- Do not restock dead SKUs (token volume).
- Do not hallucinate inventory.

## Related

[[work-per-cost]] · [[multi-source-verdict]] · [[grok-bot-quota]]
