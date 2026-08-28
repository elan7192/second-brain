#!/usr/bin/env python3
"""Render growth/ as a GROWTHOS constellation graph matching the DeRonin vault chrome."""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROWTH = ROOT / "growth"
TEMPLATE = Path(__file__).resolve().parent / "growthos-graph.template.html"
OUT = ROOT / "output" / "growthos-graph.html"


def kb(slug: str) -> str:
    path = GROWTH / f"{slug}.md"
    n = max(1, round(path.stat().st_size / 1024))
    return f"{n} KB"


def body(slug: str) -> str:
    path = GROWTH / f"{slug}.md"
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4 :]
    return text.strip()


def file_item(name: str, slug: str, abbr: str) -> dict:
    return {
        "kind": "file",
        "name": name,
        "abbr": abbr,
        "right": kb(slug),
        "body": body(slug),
    }


def folder_item(name: str, abbr: str, count: str, open_id: str) -> dict:
    return {
        "kind": "folder",
        "name": name,
        "abbr": abbr,
        "right": count,
        "open": open_id,
    }


def html_label(text: str, count: str | None = None) -> str:
    extra = f'<span class="n">{count}</span>' if count else ""
    return f"{text}{extra}"


def build() -> dict:
    n_notes = len(list(GROWTH.glob("*.md")))
    hubs = [
        ("partners", "PARTNERS", "#ff4da6", "hub", '<span class="fold"></span> PARTNERS'),
        ("creators", "CREATORS", "#38bdf8", "cyan", "CREATORS"),
        ("playbooks", "PLAYBOOKS", "#7aa2ff", "cyan", "PLAYBOOKS"),
        ("rulings", "RULINGS", "#ff9f1a", "ruling", "RULINGS"),
        ("memories", "MEMORIES", "#f9a8d4", "hub", "MEMORIES"),
        ("content", "CONTENT ENGINE", "#ffe566", "metric", "CONTENT ENGINE"),
        ("trends", "TREND RADAR", "#2ee6d6", "cyan", "TREND RADAR"),
        ("offers", "OFFERS", "#c084fc", "violet", "OFFERS"),
        ("strategies", "STRATEGIES", "#fb7185", "hub", "STRATEGIES"),
        ("insights", "INSIGHTS", "#fde047", "metric", "INSIGHTS"),
        ("journal", "JOURNAL", "#a78bfa", "violet", "JOURNAL"),
        ("niches", "NICHES", "#4ade80", "hub", "NICHES"),
        ("competitors", "COMPETITORS", "#818cf8", "leaf", "COMPETITORS"),
    ]
    leaves = [
        ("partner-1", "partners", "PARTNER #1", "#ff4da6", "leaf", "PARTNER #1", None),
        ("partner-2", "partners", "PARTNER #2", "#ff4da6", "leaf", "PARTNER #2", None),
        ("partner-3", "partners", "PARTNER #3", "#ff4da6", "leaf", "PARTNER #3", None),
        ("pipeline", "partners", "PIPELINE · 1", "#ff4da6", "leaf", "PIPELINE", "1"),
        ("shortlist", "creators", "SHORTLIST · 3", "#38bdf8", "cyan", "SHORTLIST", "3"),
        ("passed", "creators", "PASSED · 1", "#38bdf8", "leaf", "PASSED", "1"),
        ("pb-scout", "playbooks", "SCOUT", "#7aa2ff", "leaf", "SCOUT", None),
        ("pb-content", "playbooks", "SCRIPTS", "#7aa2ff", "leaf", "SCRIPTS", None),
        ("pb-whop", "playbooks", "WHOP CLI", "#7aa2ff", "leaf", "WHOP CLI", None),
        ("pb-outreach", "playbooks", "OUTREACH", "#7aa2ff", "leaf", "OUTREACH", None),
        ("r-rev", "rulings", "REV-SHARE ≥ 25%", "#ff9f1a", "ruling", "REV-SHARE ≥ 25%", None),
        ("r-proof", "rulings", "PROOF OF SKILL", "#ff9f1a", "ruling", "PROOF OF SKILL", None),
        ("r-money", "rulings", "BOT NEVER MOVES MONEY", "#ff9f1a", "ruling", "BOT NEVER MOVES MONEY", None),
        ("r-niche", "rulings", "ONE NICHE AT A TIME", "#ff9f1a", "ruling", "ONE NICHE AT A TIME", None),
        ("r-conv", "rulings", "CONVERSION OVER VIEWS", "#ff9f1a", "ruling", "CONVERSION OVER VIEWS", None),
        ("wins", "memories", "WINS", "#f9a8d4", "leaf", "WINS", None),
        ("first-check", "memories", "FIRST CHECK", "#f9a8d4", "leaf", "FIRST CHECK", None),
        ("referral", "memories", "REFERRAL", "#f9a8d4", "leaf", "REFERRAL", None),
        ("fail", "memories", "VIEW-CHASE", "#f9a8d4", "leaf", "VIEW-CHASE", None),
        ("view-sale", "content", "VIEW-SALE GAP", "#ffe566", "metric", "VIEW-SALE GAP", None),
        ("mira-hooks", "content", "MIRA HOOKS", "#ffe566", "leaf", "MIRA HOOKS", None),
        ("kai-hooks", "content", "KAI HOOKS", "#ffe566", "leaf", "KAI HOOKS", None),
        ("week", "trends", "THIS WEEK", "#2ee6d6", "leaf", "THIS WEEK", None),
        ("formats", "trends", "FORMATS · 5", "#2ee6d6", "leaf", "FORMATS", "5"),
        ("o-mira", "offers", "COMMUNITY $49/MO", "#c084fc", "violet", "COMMUNITY $49/MO", None),
        ("o-kai", "offers", "OPS $99/MO", "#c084fc", "leaf", "OPS $99/MO", None),
        ("shadow", "strategies", "SHADOW OPERATOR", "#fb7185", "leaf", "SHADOW OPERATOR", None),
        ("costs", "strategies", "COSTS MUST NOT SCALE", "#ffe566", "metric", "COSTS MUST NOT SCALE", None),
        ("chess", "insights", "74k ≠ SALES", "#fde047", "metric", "74k ≠ SALES", None),
        ("talent", "insights", "TALENT > BUDGET", "#fde047", "leaf", "TALENT > BUDGET", None),
        ("daily", "journal", "DAILY NOTES", "#a78bfa", "leaf", "DAILY NOTES", None),
        ("n-ugc", "niches", "AI UGC", "#4ade80", "leaf", "AI UGC", None),
        ("n-ops", "niches", "AI OPS", "#4ade80", "leaf", "AI OPS", None),
    ]

    nodes: list[dict] = [
        {
            "id": "core",
            "val": 7.5,
            "color": "#ffffff",
            "kind": "core",
            "panel": "core",
            "html": f'VAULT CORE <span class="n">{n_notes} notes</span>',
            "x": 0,
            "y": 0,
            "z": 0,
            "fx": 0,
            "fy": 0,
            "fz": 0,
        }
    ]
    links: list[dict] = []
    n_hubs = len(hubs)
    for i, (hid, _label, color, kind, html) in enumerate(hubs):
        ang = 2 * math.pi * i / n_hubs - math.pi / 2
        elev = 18 * math.sin(i * 1.7)
        x, y, z = 95 * math.cos(ang), elev, 95 * math.sin(ang)
        nodes.append(
            {
                "id": hid,
                "val": 4.2,
                "color": color,
                "kind": kind,
                "panel": hid,
                "html": html,
                "x": x,
                "y": y,
                "z": z,
            }
        )
        links.append({"source": "core", "target": hid, "distance": 100})

    hub_pos = {n["id"]: n for n in nodes}
    kids: dict[str, list[tuple]] = {}
    for leaf in leaves:
        kids.setdefault(leaf[1], []).append(leaf)
    for hid, group in kids.items():
        hx, hy, hz = hub_pos[hid]["x"], hub_pos[hid]["y"], hub_pos[hid]["z"]
        for j, (lid, parent, _lab, color, kind, html, count) in enumerate(group):
            a = 2 * math.pi * j / max(len(group), 1)
            nodes.append(
                {
                    "id": lid,
                    "val": 2.2,
                    "color": color,
                    "kind": kind,
                    "panel": lid,
                    "html": html_label(html, count) if count else html,
                    "x": hx + 38 * math.cos(a),
                    "y": hy + 10 * math.sin(a * 1.4),
                    "z": hz + 38 * math.sin(a),
                }
            )
            links.append({"source": parent, "target": lid, "distance": 42})

    panels = {
        "core": {
            "crumb": "vault /",
            "title": "VAULT CORE",
            "meta": f"folder · {n_notes} notes · operator memory",
            "items": [
                folder_item("partners/", "PAR", "3 items", "partners"),
                folder_item("creators/", "CRE", "4 items", "creators"),
                folder_item("playbooks/", "PLA", "4 items", "playbooks"),
                folder_item("rulings/", "RUL", "5 items", "rulings"),
                folder_item("memories/", "MEM", "4 items", "memories"),
                folder_item("content/", "CON", "3 items", "content"),
                folder_item("trends/", "TRD", "2 items", "trends"),
                folder_item("offers/", "OFF", "2 items", "offers"),
                folder_item("niches/", "NIC", "2 items", "niches"),
                file_item("_core.md", "growth-core", "COR"),
            ],
        },
        "partners": {
            "crumb": "vault / partners /",
            "title": "PARTNERS",
            "meta": "folder · 2 live · 1 pipeline",
            "items": [
                folder_item("partner-#1/", "P1", "3 items", "partner-1"),
                folder_item("partner-#2/", "P2", "3 items", "partner-2"),
                folder_item("partner-#3/", "P3", "2 items", "partner-3"),
                file_item("_overview.md", "growth-partners", "PAR"),
            ],
        },
        "partner-1": {
            "crumb": "vault / partners / partner-#1 /",
            "title": "PARTNER #1",
            "meta": "folder · bot-maintained · DEMO",
            "items": [
                file_item("_index.md", "growth-partner-mira", "P1"),
                file_item("scout.md", "growth-scout-mira", "SC"),
                file_item("offer.md", "growth-offer-mira", "OF"),
                file_item("content.md", "growth-content-mira", "CT"),
            ],
        },
        "partner-2": {
            "crumb": "vault / partners / partner-#2 /",
            "title": "PARTNER #2",
            "meta": "folder · bot-maintained · DEMO",
            "items": [
                file_item("_index.md", "growth-partner-kai", "P2"),
                file_item("scout.md", "growth-scout-kai", "SC"),
                file_item("offer.md", "growth-offer-kai", "OF"),
                file_item("content.md", "growth-content-kai", "CT"),
            ],
        },
        "partner-3": {
            "crumb": "vault / partners / partner-#3 /",
            "title": "PARTNER #3",
            "meta": "folder · bot-maintained · DEMO",
            "items": [
                file_item("_index.md", "growth-partner-elena", "P3"),
                file_item("scout.md", "growth-scout-elena", "SC"),
            ],
        },
        "pipeline": {
            "crumb": "vault / partners / pipeline /",
            "title": "PIPELINE",
            "meta": "folder · 1 in pipeline",
            "items": [folder_item("partner-#3/", "P3", "2 items", "partner-3")],
        },
        "creators": {
            "crumb": "vault / creators /",
            "title": "CREATORS",
            "meta": "folder · shortlist 3 · passed 1",
            "items": [
                file_item("_overview.md", "growth-creators", "CRE"),
                file_item("mira.md", "growth-scout-mira", "MI"),
                file_item("kai.md", "growth-scout-kai", "KA"),
                file_item("elena.md", "growth-scout-elena", "EL"),
                file_item("passed-viewfarmer.md", "growth-passed-viewfarmer", "PS"),
            ],
        },
        "shortlist": {
            "crumb": "vault / creators / shortlist /",
            "title": "SHORTLIST",
            "meta": "folder · 3 keeps",
            "items": [
                file_item("mira.md", "growth-scout-mira", "MI"),
                file_item("kai.md", "growth-scout-kai", "KA"),
                file_item("elena.md", "growth-scout-elena", "EL"),
            ],
        },
        "passed": {
            "crumb": "vault / creators / passed /",
            "title": "PASSED",
            "meta": "folder · 1 pass",
            "items": [file_item("viewfarmer.md", "growth-passed-viewfarmer", "PS")],
        },
        "playbooks": {
            "crumb": "vault / playbooks /",
            "title": "PLAYBOOKS",
            "meta": "folder · do not send · do not run live Whop",
            "items": [
                file_item("_overview.md", "growth-playbooks", "PLA"),
                file_item("scout.md", "growth-playbook-scout", "SC"),
                file_item("content.md", "growth-playbook-content", "CT"),
                file_item("whop.md", "growth-playbook-whop", "WH"),
                file_item("outreach.md", "growth-playbook-outreach", "OR"),
            ],
        },
        "pb-scout": {
            "crumb": "vault / playbooks /",
            "title": "SCOUT",
            "meta": "file · playbook",
            "items": [file_item("scout.md", "growth-playbook-scout", "SC")],
        },
        "pb-content": {
            "crumb": "vault / playbooks /",
            "title": "SCRIPTS",
            "meta": "file · playbook",
            "items": [file_item("content.md", "growth-playbook-content", "CT")],
        },
        "pb-whop": {
            "crumb": "vault / playbooks /",
            "title": "WHOP CLI",
            "meta": "file · do not run live",
            "items": [file_item("whop.md", "growth-playbook-whop", "WH")],
        },
        "pb-outreach": {
            "crumb": "vault / playbooks /",
            "title": "OUTREACH",
            "meta": "file · do not send",
            "items": [file_item("outreach.md", "growth-playbook-outreach", "OR")],
        },
        "rulings": {
            "crumb": "vault / rulings /",
            "title": "RULINGS",
            "meta": "folder · one dated line each",
            "items": [
                file_item("_overview.md", "growth-rulings", "RUL"),
                file_item("rev-share.md", "growth-ruling-revshare", "25"),
                file_item("proof.md", "growth-ruling-proof", "PR"),
                file_item("no-money.md", "growth-ruling-no-money", "$$"),
                file_item("one-niche.md", "growth-ruling-one-niche", "1N"),
                file_item("conversion.md", "growth-ruling-conversion", "CV"),
            ],
        },
        "r-rev": {
            "crumb": "vault / rulings /",
            "title": "REV-SHARE ≥ 25%",
            "meta": "ruling · 2026-08-24",
            "items": [file_item("rev-share.md", "growth-ruling-revshare", "25")],
        },
        "r-proof": {
            "crumb": "vault / rulings /",
            "title": "PROOF OF SKILL",
            "meta": "ruling · 2026-08-24",
            "items": [file_item("proof.md", "growth-ruling-proof", "PR")],
        },
        "r-money": {
            "crumb": "vault / rulings /",
            "title": "BOT NEVER MOVES MONEY",
            "meta": "ruling · 2026-08-24",
            "items": [file_item("no-money.md", "growth-ruling-no-money", "$$")],
        },
        "r-niche": {
            "crumb": "vault / rulings /",
            "title": "ONE NICHE AT A TIME",
            "meta": "ruling · 2026-08-24",
            "items": [file_item("one-niche.md", "growth-ruling-one-niche", "1N")],
        },
        "r-conv": {
            "crumb": "vault / rulings /",
            "title": "CONVERSION OVER VIEWS",
            "meta": "ruling · 2026-08-24",
            "items": [file_item("conversion.md", "growth-ruling-conversion", "CV")],
        },
        "memories": {
            "crumb": "vault / memories /",
            "title": "MEMORIES",
            "meta": "folder · bot-maintained",
            "items": [
                folder_item("wins/", "WIN", "3 items", "wins"),
                file_item("_overview.md", "growth-memories", "MEM"),
                file_item("view-chase.md", "growth-fail-view-chase", "FL"),
            ],
        },
        "wins": {
            "crumb": "vault / memories / wins /",
            "title": "WINS",
            "meta": "folder · bot-maintained",
            "items": [
                file_item("_index.md", "growth-memories", "IX"),
                file_item("first-check.md", "growth-win-first-check", "FC"),
                file_item("referral.md", "growth-win-referral", "RF"),
            ],
        },
        "first-check": {
            "crumb": "vault / memories / wins /",
            "title": "FIRST CHECK",
            "meta": "file · DEMO",
            "items": [file_item("first-check.md", "growth-win-first-check", "FC")],
        },
        "referral": {
            "crumb": "vault / memories / wins /",
            "title": "REFERRAL",
            "meta": "file · DEMO",
            "items": [file_item("referral.md", "growth-win-referral", "RF")],
        },
        "fail": {
            "crumb": "vault / memories /",
            "title": "VIEW-CHASE",
            "meta": "file · failure",
            "items": [file_item("view-chase.md", "growth-fail-view-chase", "FL")],
        },
        "content": {
            "crumb": "vault / content /",
            "title": "CONTENT ENGINE",
            "meta": "folder · views vs sales",
            "items": [
                file_item("_overview.md", "growth-content", "CON"),
                file_item("mira.md", "growth-content-mira", "MI"),
                file_item("kai.md", "growth-content-kai", "KA"),
            ],
        },
        "view-sale": {
            "crumb": "vault / content /",
            "title": "VIEW-SALE GAP",
            "meta": "file · conversion",
            "items": [
                file_item("mira.md", "growth-content-mira", "MI"),
                file_item("kai.md", "growth-content-kai", "KA"),
            ],
        },
        "mira-hooks": {
            "crumb": "vault / content /",
            "title": "MIRA HOOKS",
            "meta": "file · DEMO",
            "items": [file_item("mira.md", "growth-content-mira", "MI")],
        },
        "kai-hooks": {
            "crumb": "vault / content /",
            "title": "KAI HOOKS",
            "meta": "file · DEMO",
            "items": [file_item("kai.md", "growth-content-kai", "KA")],
        },
        "trends": {
            "crumb": "vault / trends /",
            "title": "TREND RADAR",
            "meta": "folder · this week",
            "items": [
                file_item("_overview.md", "growth-trends", "TRD"),
                file_item("2026-08-25.md", "growth-trend-2026-08-25", "WK"),
            ],
        },
        "week": {
            "crumb": "vault / trends /",
            "title": "THIS WEEK",
            "meta": "file · 2026-08-25",
            "items": [file_item("2026-08-25.md", "growth-trend-2026-08-25", "WK")],
        },
        "formats": {
            "crumb": "vault / trends /",
            "title": "FORMATS",
            "meta": "file · 5 converting this week",
            "items": [file_item("2026-08-25.md", "growth-trend-2026-08-25", "WK")],
        },
        "offers": {
            "crumb": "vault / offers /",
            "title": "OFFERS",
            "meta": "folder · DEMO prices",
            "items": [
                file_item("_overview.md", "growth-offers", "OFF"),
                file_item("mira.md", "growth-offer-mira", "M$"),
                file_item("kai.md", "growth-offer-kai", "K$"),
            ],
        },
        "o-mira": {
            "crumb": "vault / offers /",
            "title": "COMMUNITY $49/MO",
            "meta": "file · DEMO",
            "items": [file_item("mira.md", "growth-offer-mira", "M$")],
        },
        "o-kai": {
            "crumb": "vault / offers /",
            "title": "OPS $99/MO",
            "meta": "file · DEMO",
            "items": [file_item("kai.md", "growth-offer-kai", "K$")],
        },
        "strategies": {
            "crumb": "vault / strategies /",
            "title": "STRATEGIES",
            "meta": "folder",
            "items": [file_item("shadow-operator.md", "growth-strategy", "SH")],
        },
        "shadow": {
            "crumb": "vault / strategies /",
            "title": "SHADOW OPERATOR",
            "meta": "file",
            "items": [file_item("shadow-operator.md", "growth-strategy", "SH")],
        },
        "costs": {
            "crumb": "vault / strategies /",
            "title": "COSTS MUST NOT SCALE",
            "meta": "ruling · strategy",
            "items": [file_item("shadow-operator.md", "growth-strategy", "SH")],
        },
        "insights": {
            "crumb": "vault / insights /",
            "title": "INSIGHTS",
            "meta": "folder",
            "items": [file_item("_overview.md", "growth-insights", "IN")],
        },
        "chess": {
            "crumb": "vault / insights /",
            "title": "74k ≠ SALES",
            "meta": "file · author example unverified",
            "items": [file_item("_overview.md", "growth-insights", "IN")],
        },
        "talent": {
            "crumb": "vault / insights /",
            "title": "TALENT > BUDGET",
            "meta": "file",
            "items": [file_item("_overview.md", "growth-insights", "IN")],
        },
        "journal": {
            "crumb": "vault / journal /",
            "title": "JOURNAL",
            "meta": "folder",
            "items": [file_item("2026-08-25.md", "growth-journal-2026-08-25", "JL")],
        },
        "daily": {
            "crumb": "vault / journal /",
            "title": "DAILY NOTES",
            "meta": "file",
            "items": [file_item("2026-08-25.md", "growth-journal-2026-08-25", "JL")],
        },
        "niches": {
            "crumb": "vault / niches /",
            "title": "NICHES",
            "meta": "folder · one live",
            "items": [
                file_item("ai-ugc.md", "growth-niche-ai-ugc", "UG"),
                file_item("ai-ops.md", "growth-niche-ai-ops", "OP"),
            ],
        },
        "n-ugc": {
            "crumb": "vault / niches /",
            "title": "AI UGC",
            "meta": "file · current pick",
            "items": [file_item("ai-ugc.md", "growth-niche-ai-ugc", "UG")],
        },
        "n-ops": {
            "crumb": "vault / niches /",
            "title": "AI OPS",
            "meta": "file · watch-only",
            "items": [file_item("ai-ops.md", "growth-niche-ai-ops", "OP")],
        },
        "competitors": {
            "crumb": "vault / competitors /",
            "title": "COMPETITORS",
            "meta": "folder · empty of named firms",
            "items": [file_item("_overview.md", "growth-competitors", "CP")],
        },
    }
    return {"nodes": nodes, "links": links, "panels": panels}


def main() -> int:
    data = build()
    html = TEMPLATE.read_text(encoding="utf-8").replace(
        "__GROWTH_DATA__", json.dumps(data, ensure_ascii=False)
    )
    OUT.write_text(html, encoding="utf-8")
    print(f"nodes={len(data['nodes'])} links={len(data['links'])} panels={len(data['panels'])} -> {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
