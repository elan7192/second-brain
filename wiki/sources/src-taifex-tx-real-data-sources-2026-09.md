---
id: source:src-taifex-tx-real-data-sources-2026-09
type: source
tags:
  - research
  - taiwan
  - trading
  - data
created: 2026-09-05
updated: 2026-09-05
---

# src-taifex-tx-real-data-sources-2026-09

- Topic: TAIFEX TX (臺股期貨) real historical data sources catalog: free official, paid official, TEJ, community, brokers
- Brief artifact (box, not in repo): `/workspace/fill/tx-real-data-sources-2026-09-05.md` (Researchy via CoS 2026-09-05). Not mounted in this agent session; figures below come from lan E's ingest brief and are cited to that path.
- 判定: 入vault建議 thin-medium catalog
- Symbols: TAIFEX **TX** = 臺股期貨. Vendors often label it TXF.
- Quote untrusted. Not copied into `raw/`. **Educational catalog only. Not financial advice. Not a vendor endorsement.**
- Prices are public list prices as of the research date (2026-09-05). They may change. Do not extend or invent prices beyond this brief.
- Motivation: [[src-itrading-acer-trading-doctor-sop-2026-09]] ran its desk PROXY backtest on community TX 1m bars ending 2023-12-08. This page catalogs the licensed paths to real TX history so a later run does not depend on that dump.
- Dedup: no `src-taifex*`, TEJ, or eDataShop catalog on main. Near (different topic; do not overwrite): [[src-itrading-acer-trading-doctor-sop-2026-09]] · [[src-last30days-quant-algo-trading-2026-09]].

## Claims kept

- Free official TAIFEX (futures incl. TX): yearly **daily** market ZIPs (about 1998 to 2025) plus a **rolling 30 trading days** of futures ticks (time and sales). Endpoints named in the brief: `futDailyMarketView` and `futPrevious30DaysSalesData`. Same pattern as the free options offerings.
- No free official multi-year 1-minute or tick archive exists for TX. TAIFEX FAQ states there is no public historical database API. Deep history is paid.
- Paid official eDataShop: futures trade and tick files run about **NT$9k to 10k per month of data** (TX centisecond ticks about NT$9k per month from 2013-07; full futures trades about NT$10k per month from 1998, with a lag). Single-user license, no redistribution. Full 2011 to 2026 official ticks at list price is about **NT$1.4M to 1.8M**, so the usual pattern is to buy spot-check months only.
- TEJ TQuant Lab futures: minute bars plus a `continuous_future` TX series. Top plan about **NT$14.4k per year** (NT$1,200 per month on a 12-month lock; history from about 2005). This is the practical legal path for multi-year 1m backtests. A 14-day trial exists. No redistribution.
- Community MEGA / Drive / COCO dumps: fail on ToS and quality versus TAIFEX. Do not treat them as a licensed replacement for official or TEJ data. The community TX_1m file used in the Acer PROXY run falls in this class.
- Brokers (e.g. Yuanta Spark): recent 1m lookback only (about 20 days). Not a 2011 to 2026 backfill.
- Practical hygiene (brief recommendation, OPINION): archive the free daily ZIPs and pull the 30-day tick window nightly going forward; use TEJ for historical 1m; use eDataShop for official tick spot-checks.

## Not kept

- Vendor URLs beyond the two TAIFEX endpoint names, plan tables, and per-product SKU lists. The brief holds them.
- Any price not listed above. No extrapolation to other contracts, years, or vendors.
- Any quality benchmark of the community dumps. The brief flags ToS and quality fail without a measured table.

## Pages updated

[[index-sources]] · [[src-itrading-acer-trading-doctor-sop-2026-09]]

## Related

[[src-itrading-acer-trading-doctor-sop-2026-09]] · [[src-last30days-quant-algo-trading-2026-09]] · [[src-0xkvro-quant-sample-size-skip]]
