#!/usr/bin/env python3
"""Compile a new-partner briefing from growth/ notes. Do not invent."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROWTH = ROOT / "growth"
OUT_DIR = ROOT / "output"

NEEDED = [
    "growth-core",
    "growth-rulings",
    "growth-partners",
    "growth-content",
    "growth-trends",
    "growth-playbooks",
]


def read(slug: str) -> str:
    path = GROWTH / f"{slug}.md"
    if not path.exists():
        raise SystemExit(f"missing {path}")
    return path.read_text(encoding="utf-8")


def strip_fm(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4 :].strip()
    return text.strip()


def strip_heading(text: str) -> str:
    body = strip_fm(text)
    return re.sub(r"^#\s+.+\n+", "", body, count=1).strip()


def brief(partner_hint: str) -> str:
    today = dt.date.today().isoformat()
    partners = strip_heading(read("growth-partners"))
    mira = strip_heading(read("growth-content-mira"))
    kai = strip_heading(read("growth-content-kai"))
    trend = strip_heading(read("growth-trend-2026-08-25"))
    playbooks = strip_heading(read("growth-playbooks"))

    return f"""---
type: output
tags:
  - growth
created: {today}
updated: {today}
---

# GrowthOS briefing · {today}

Generated from `growth/`. Not from chat memory. Target: **{partner_hint}**.

Cite: [[growth-core]]. Demo names are DEMO. Vault does not post, pay, send, or write live Whop objects.

## 1. Rulings (do not re-argue)

From [[growth-rulings]]:

- [[growth-ruling-revshare]]: never below 25% rev-share.
- [[growth-ruling-proof]]: never partner without proof of skill.
- [[growth-ruling-no-money]]: bot never deletes products, changes price, or moves money without a yes.
- [[growth-ruling-one-niche]]: one hyped niche at a time. Current pick is AI UGC.
- [[growth-ruling-conversion]]: write what sells the offer, not what only pulls views.

## 2. What prior partners taught

Roster from [[growth-partners]]:

{partners}

Elena is pipeline because of a 15% ask. Floor still 25%. See [[growth-partner-elena]].

Mira conversion table ([[growth-content-mira]]):

{mira.split('## Gap')[0].strip()}

Kai conversion table ([[growth-content-kai]]):

{kai.split('## Gap')[0].strip()}

Do not write sandwich/inbox spectacle for the next UGC partner. Copy the `sells` rows.

## 3. This week's formats

From [[growth-trend-2026-08-25]]:

{trend.split('## What this means')[0].strip()}

## 4. Playbooks to load

From [[growth-playbooks]]:

{playbooks}

## 5. Author insight (unverified as our data)

Chess example on [[growth-insights]]: 74k views / 51 sales vs 135k views / 2 sales. Use the shape. Do not treat those counts as ours.

## 6. Hard stops for this run

- If {partner_hint} has no inspectable work, stop. [[growth-ruling-proof]]
- If terms go below 25%, stop. [[growth-ruling-revshare]]
- If a command would delete, reprice, or move money, stop. [[growth-ruling-no-money]]
- File the next note under `growth/`. Do not send outreach.

## Sources used

[[growth-core]] · [[growth-rulings]] · [[growth-partners]] · [[growth-content-mira]] · [[growth-content-kai]] · [[growth-trend-2026-08-25]] · [[growth-playbooks]] · [[growth-insights]] · [[growth-partner-elena]] · [[src-deronin-growthos-vault]]
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--partner",
        default="next AI UGC creator (unnamed)",
        help="Who this briefing is for",
    )
    args = parser.parse_args()
    for slug in NEEDED:
        read(slug)
    text = brief(args.partner)
    today = dt.date.today().isoformat()
    out = OUT_DIR / f"growth-briefing-{today}.md"
    OUT_DIR.mkdir(exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(out.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
