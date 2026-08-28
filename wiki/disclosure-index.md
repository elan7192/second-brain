---
id: concept:disclosure-index
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-28
---

# Disclosure Index

Compiled snapshot of the public Disclosure Index catalog. Source: [[src-disclosure-index]]. Machine counts: `output/disclosure-index-stats-2026-08-23.json`.

Site updated 23 August 2026. Parsed 11,338 unique records on 2026-08-24. 4,798 researchers. Date span 2013-11-07 to 2026-08-21. Two records have no date.

## Collections

| Platform | Records | Indexed via |
| --- | ---: | --- |
| HackerOne | 10,019 | 9,979 HackerOne Disclosed Reports index; 40 PentesterLand archive |
| Bugcrowd | 809 | 800 CrowdStream; 9 PentesterLand archive |
| Code4rena | 411 | official reports |
| Immunefi | 92 | public sitemap |
| Intigriti | 6 | PentesterLand archive |
| YesWeHack | 1 | PentesterLand archive |

Kinds: 10,779 platform disclosures, 411 competitive audit reports, 92 bug-fix reviews, 56 historical writeups.

## Subjects and severity

Largest `vulnerabilityClass` values: Other 3,478; Cross-site scripting 1,740; Access control 1,364; Authentication 1,153; Information disclosure 1,122. Sixteen classes in total.

Severity: Unrated 3,200; Medium 3,047; Low 2,007; High 1,576; Critical 814; None 402; Informational 292.

Outcomes when present: Resolved 9,100; Informational 1,099; missing 559; Not applicable 321; Duplicate 228; Spam 23; Unresolved 8.

1,601 records list at least one CVE (1,867 mentions). 9,033 have a weakness string. No record has a native `technology` field. The site infers technology in the browser.

## Bounty field

2,277 records have a nonzero `bounty`. Catalog sum 3,792,071.62. Median 500. P90 4,000. Max 50,000. 23 values are 10 or less.

Treat these as catalog-reported. Some Immunefi values match title numerals, not a payment.

## API vs live data

Documented on `#api`:

- `GET /api/reports` with `q`, `platform`, `technology`, `status`, `severity`, `class`, `researcher`, `program`, `year`, `kind`, `sort`, `limit`, `offset`
- `GET /api/reports/{id}`
- `GET /api/stats`
- Claimed CORS and 120 requests per minute per client

Fetched 2026-08-24: those paths returned 404. The queryable surface is `data/catalog.js`. See C28.

## Use here

Answer count questions from this page or the stats JSON. Do not re-fetch the 5.6 MB catalog for a normal query.

Keep bibliographic metadata only. Do not copy report bodies. Do not write exploit steps. See D11.

This catalog does not authorize testing any system.

## Related

[[src-disclosure-index]] · [[contradictions]] · D5 in `decisions.md`
