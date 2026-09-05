---
id: source:src-itrading-acer-trading-doctor-sop-2026-09
type: source
tags:
  - research
  - taiwan
  - trading
created: 2026-09-05
updated: 2026-09-05
---

# src-itrading-acer-trading-doctor-sop-2026-09

- Topic: 交易醫生 / Acer / 徐國華 台指期當沖 research SOP (public structure only)
- Brief artifact (box, not in repo): `/workspace/fill/交易醫生-research-sop-2026-09-05.md` (Researchy via CoS vault_sync 2026-09-05)
- Backtest artifact (box, not in repo; notebooks, CSVs, PNGs stay there): `/workspace/fill/acer-doctor-bt-2026-09-05/STATUS.md` (desk PROXY gap-fade run 2026-09-05)
- 判定: 入vault建議 thin-medium
- Key URLs: https://itrading.tw/about · https://itrading.tw/post/100 · https://www.facebook.com/iamacer2266/ · https://www.books.com.tw/products/0011021468 · court reporting mirror https://www.cmmedia.com.tw/home/articles/37152
- Quote untrusted. Not copied into `raw/`. **Educational use only. Not financial advice.**
- Paywalled / private SOP parameter sheets are not copied. Method map only.
- Dedup: none on main for 交易醫生 / trading-doctor. Near (different topic; do not overwrite): [[src-0xkvro-quant-sample-size-skip]] · [[src-ritonchain-regime-trading-skip]] · [[src-last30days-quant-algo-trading-2026-09]].

## Claims kept

- Identity: 徐國華 is the person behind the brand 交易醫生 / iTrader / Dr.Trading (handles Acer / Acer2266 / Alex SHU). Entity on itrading.tw is 璞思管理顧問有限公司. Focus is 台指期當沖 education, plus 現股 and 程式交易. Book: 《100張圖學會期貨交易》增訂版 (books.com.tw/products/0011021468).
- Disambiguation: the Researchy pass found no primary-source evidence linking 交易醫生 to 善甲狼 or 投機ok. Treat them as separate brands until contrary evidence.
- Research method (public structure): long-sample backtest framing before trusting an idea; book marketing cites roughly 2,000 to 3,000 trading days. Day-trading framing prefers price, K bars, volume, psychology, and money management over stacked TA indicators. Publisher and press summary only; the stats stay labeled marketing, unverified.
- Daily SOP family from free 盤前 posts: 利多 / 利空 / 今日對策; 五線 support and resistance; named 跳空 SOP1 / SOP2 / SOPX (book TOC plus free posts such as itrading.tw/post/100); 0915 / 0945 A轉 watches appear in free posts. Fine parameters sit in the book or paid tiers and are not compiled here.
- Intraday discipline from public blurbs and guides: prefer one direction per day; about 3 to 5 trades max and stop after 2 consecutive losses (LINE guidance cited in the brief); APP checklist (2025 Acer CMoney): 08:00 盤前, 08:45 mark lines, 09:00 外資異常股, and so on.
- Compliance flag: Taipei District Court 110金訴42 convicted the defendant of running an illegal futures advisory business under 期貨交易法. Reporting around 2022-11 (信傳媒 mirror above) ties the defendant to 交易醫生 / Alex Shu / 璞思. This vault keeps an educational method map only. Not an endorsement.
- Name collision: a separate open-data judgment naming 徐國華 (114審訴4147) is an unconfirmed name collision. Do not equate it with 交易醫生 without a primary link.

### Desk PROXY gap-fade backtest (2026-09-05)

- PROXY scope: an educational desk reconstruction of the public blurb gap-fade plus SOPX-first ordering, run on community TX 1m bars, session 08:45 to 13:25. Labels PROXY_SOPX / PROXY_SOP1 are name-only. They are not the official paywalled SOP1 / SOP2 / SOPX parameters. SOP2 was not coded. Source: STATUS.md artifact above.
- PROXY cost assumption: 2 pts per side (4 pts round trip), TX 1 lot, NT$200 per pt. Results below are net of this assumption only.
- PROXY verdict: the train-selected variant (grid fit on train only, bars before 2021) shows train WR about 38% and PF about 1.19. Holdout 2023 PF about 0.92 loses after costs (WR about 32%, net pts negative). Validate 2021 to 2022 PF about 0.93 also loses. The blurb-fixed baseline (N=5, no SOP1 flip) is worse on holdout. Desk PROXY result only. Not a verification or refutation of Acer marketing figures.
- PROXY data window: bars end 2023-12-08. No 2024 to 2026 bars in this run.
- PROXY gaps: 五線, 外資, news, Friday size, and segmented 停利 are not modeled. Paywalled SOP1 / SOP2 / SOPX are not tested.
- Compliance restated: 110金訴42 flag above stands. The PROXY run is educational only. Not financial advice. Not an endorsement.

## Not kept

- Private or paywalled SOP parameter sheets (五線 values, 跳空 thresholds, position sizing tables).
- Any Acer marketing performance or win-rate figure. The brief carries none that trace to a primary source. The desk PROXY metrics above are kept as PROXY only, not as verification of any marketed claim.
- Full PROXY parameter grid, result CSVs, and PNGs. They stay in the box artifact directory.

## Pages updated

[[index-sources]] · [[src-0xkvro-quant-sample-size-skip]] · [[src-ritonchain-regime-trading-skip]] · [[src-last30days-quant-algo-trading-2026-09]]

## Related

[[src-last30days-quant-algo-trading-2026-09]] · [[src-0xkvro-quant-sample-size-skip]] · [[src-ritonchain-regime-trading-skip]] · [[src-ridark-trading-floor-skip]] · [[skill-as-sop]]
