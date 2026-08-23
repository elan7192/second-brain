#!/usr/bin/env python3
"""Render the dark shared-context-bus dashboard. Does not touch wiki/graph.md or the island snapshot."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "output"
LINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
SKIP_DIRS = {".git", ".obsidian", "templates", "raw", ".agents", ".cursor"}
SKIP_FILES = {"AGENTS.md", "CLAUDE.md", "README.md"}


def note_type(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if path.name == "Home.md":
        return "home"
    if rel.startswith("wiki/sources/"):
        return "source"
    if rel.startswith("hunt/") or path.name == "hunt.md":
        return "hunt"
    if rel.startswith("wiki/people/"):
        return "person"
    if rel.startswith("maps/") or path.name == "maps.md":
        return "map"
    if rel.startswith("ship/") or rel.startswith("output/") or path.name == "ship.md":
        return "ship"
    if rel.startswith("wiki/"):
        if path.name in {
            "index.md",
            "how-it-works.md",
            "log.md",
            "contradictions.md",
            "agent-operating-system.md",
            "Today.md",
        }:
            return "meta"
        return "concept"
    return "note"


def collect() -> tuple[dict[str, dict], list[tuple[str, str]]]:
    pages: dict[str, Path] = {}
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        pages[path.stem] = path
    nodes = {
        slug: {"id": slug, "type": note_type(path), "path": path.relative_to(ROOT).as_posix()}
        for slug, path in pages.items()
    }
    edges: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for slug, path in pages.items():
        for match in LINK.finditer(path.read_text(encoding="utf-8")):
            target = match.group(1).strip()
            if target not in pages or target == slug:
                continue
            pair = (slug, target)
            if pair in seen:
                continue
            seen.add(pair)
            edges.append(pair)
    return nodes, edges


def vault_stats(nodes: dict[str, dict], edges: list[tuple[str, str]]) -> dict:
    by_type: dict[str, int] = defaultdict(int)
    for node in nodes.values():
        by_type[node["type"]] += 1
    raw_x = len(list((ROOT / "raw" / "x").glob("*.md"))) if (ROOT / "raw" / "x").exists() else 0
    dec = ROOT / "decisions.md"
    decisions = len(re.findall(r"^## D\d+", dec.read_text(encoding="utf-8"), re.M)) if dec.exists() else 0
    mem = ROOT / "MEMORY.md"
    memory_lines = 0
    if mem.exists():
        memory_lines = sum(1 for line in mem.read_text(encoding="utf-8").splitlines() if line.startswith("- "))
    return {
        "pages": len(nodes),
        "edges": len(edges),
        "raw_x": raw_x,
        "sources": by_type.get("source", 0),
        "people": by_type.get("person", 0),
        "concepts": by_type.get("concept", 0),
        "meta": by_type.get("meta", 0),
        "hunt": by_type.get("hunt", 0),
        "ship": by_type.get("ship", 0),
        "maps": by_type.get("map", 0),
        "decisions": decisions,
        "memory": memory_lines,
        "bus_readers": sum(1 for _src, dst in edges if dst in {"index", "context-graph", "Home"}),
    }


def pipeline(stats: dict) -> tuple[list[dict], list[dict]]:
    s = stats
    nodes = [
        {"id": "brief", "kind": "node", "title": "brief", "href": "../Home.md", "color": "#3f5a38", "x": 36, "y": 28, "rows": [
            {"k": "sources", "v": s["raw_x"], "bar": 70, "color": "#6f8f5a"},
            {"k": "pages", "v": s["pages"], "bar": 82},
            {"k": "mode", "v": "compile", "bar": 60},
        ]},
        {"id": "sources", "kind": "node", "title": "sources", "href": "../wiki/index.md", "color": "#2d4a3a", "x": 36, "y": 148, "rows": [
            {"k": "raw/x", "v": s["raw_x"], "bar": 58, "color": "#3b82f6"},
            {"k": "wiki/src", "v": s["sources"], "bar": 58},
            {"k": "people", "v": s["people"], "bar": 36, "color": "#22c55e"},
        ]},
        {"id": "constraints", "kind": "node", "title": "constraints", "href": "../decisions.md", "color": "#4a4a2d", "x": 36, "y": 268, "rows": [
            {"k": "locked", "v": f"D1-D{s['decisions']}", "bar": 90, "color": "#c8a24a"},
            {"k": "memory", "v": s["memory"], "bar": 40},
            {"k": "gate", "v": "human", "bar": 100},
        ]},
        {"id": "tokens", "kind": "node", "title": "tokens", "href": "../wiki/tokens-as-capital.md", "color": "#8a6d2a", "x": 36, "y": 388, "rows": [
            {"k": "pay", "v": "once", "bar": 72, "color": "#c8a24a"},
            {"k": "write", "v": "wiki", "bar": 80},
            {"k": "rederive", "v": "0", "bar": 8, "color": "#c45a4a"},
        ]},
        {"id": "prior", "kind": "node", "title": "prior runs", "href": "../wiki/log.md", "color": "#2a4a4a", "x": 36, "y": 508, "rows": [
            {"k": "log", "v": "open", "bar": 55},
            {"k": "today", "v": "08-30", "bar": 40},
            {"k": "depth", "v": 2, "bar": 30},
        ]},
        {"id": "bus", "kind": "bus", "title": "shared context bus  ·  index  ·  context-graph  ·  contract", "x": 268, "y": 20, "h": 620},
        {"id": "planner", "kind": "node", "title": "planner", "href": "../wiki/how-it-works.md", "color": "#2a3d5a", "x": 360, "y": 28, "rows": [
            {"k": "read", "v": "index", "bar": 88, "color": "#6ea0d4"},
            {"k": "follow", "v": "links", "bar": 70},
            {"k": "cite", "v": "wiki", "bar": 75},
        ]},
        {"id": "decompose", "kind": "node", "title": "decompose", "href": "../wiki/hunt-ship-loop.md", "color": "#3a4a6a", "x": 360, "y": 148, "rows": [
            {"k": "hunt", "v": s["hunt"], "bar": 50, "color": "#3b82f6"},
            {"k": "ship", "v": s["ship"], "bar": 45, "color": "#eb6b54"},
            {"k": "maps", "v": s["maps"], "bar": 40, "color": "#14b8a6"},
        ]},
        {"id": "route", "kind": "node", "title": "route", "href": "../wiki/harness-routing.md", "color": "#8a5a2a", "x": 580, "y": 28, "rows": [
            {"k": "by", "v": "phase", "bar": 64, "color": "#eb6b54"},
            {"k": "share", "v": "contract", "bar": 80},
            {"k": "not", "v": "chat", "bar": 12, "color": "#c45a4a"},
        ]},
        {"id": "scout-x", "kind": "node", "title": "scout 01  twitter", "href": "../hunt/twitter.md", "color": "#6a4a2a", "x": 800, "y": 28, "w": 176, "rows": [
            {"k": "in", "v": s["raw_x"], "bar": 70, "color": "#3b82f6"},
            {"k": "status", "v": "filed", "bar": 100, "color": "#6f8f5a"},
        ]},
        {"id": "scout-gh", "kind": "node", "title": "scout 02  github", "href": "../hunt/github.md", "color": "#6a4a2a", "x": 800, "y": 128, "w": 176, "rows": [
            {"k": "in", "v": 0, "bar": 8},
            {"k": "status", "v": "quiet", "bar": 20},
        ]},
        {"id": "scout-hn", "kind": "node", "title": "scout 03  hn", "href": "../hunt/hacker-news.md", "color": "#6a4a2a", "x": 800, "y": 228, "w": 176, "rows": [
            {"k": "in", "v": 0, "bar": 8},
            {"k": "status", "v": "quiet", "bar": 20},
        ]},
        {"id": "scout-rd", "kind": "node", "title": "scout 04  reddit", "href": "../hunt/reddit.md", "color": "#6a4a2a", "x": 1020, "y": 28, "w": 176, "rows": [
            {"k": "in", "v": 0, "bar": 8},
            {"k": "status", "v": "quiet", "bar": 20},
        ]},
        {"id": "scout-ph", "kind": "node", "title": "scout 05  ph", "href": "../hunt/product-hunt.md", "color": "#6a4a2a", "x": 1020, "y": 128, "w": 176, "rows": [
            {"k": "in", "v": 0, "bar": 8},
            {"k": "status", "v": "quiet", "bar": 20},
        ]},
        {"id": "merge", "kind": "node", "title": "merge", "href": "../wiki/entropy-gate.md", "color": "#2a3a5a", "x": 360, "y": 268, "rows": [
            {"k": "isolate", "v": "on", "bar": 90, "color": "#6ea0d4"},
            {"k": "diff", "v": "gate", "bar": 70},
            {"k": "peer", "v": "drop", "bar": 15, "color": "#c45a4a"},
        ]},
        {"id": "dedupe", "kind": "node", "title": "dedupe", "href": "../wiki/memory-ablation.md", "color": "#3a3a3a", "x": 360, "y": 388, "rows": [
            {"k": "keep", "v": "facts", "bar": 85},
            {"k": "drop", "v": "adj", "bar": 20, "color": "#c45a4a"},
            {"k": "lines", "v": s["memory"], "bar": 35},
        ]},
        {"id": "rank", "kind": "node", "title": "rank", "href": "../wiki/anti-slop.md", "color": "#3a3a3a", "x": 580, "y": 268, "rows": [
            {"k": "voice", "v": "tight", "bar": 78},
            {"k": "score", "v": "cite", "bar": 72},
            {"k": "wish", "v": "0", "bar": 6, "color": "#c45a4a"},
        ]},
        {"id": "cite", "kind": "node", "title": "cite check", "href": "../wiki/verifiable-instructions.md", "color": "#4a4a2a", "x": 580, "y": 388, "rows": [
            {"k": "rule", "v": "3-part", "bar": 90, "color": "#c8a24a"},
            {"k": "gap", "v": "stop", "bar": 40, "color": "#c45a4a"},
            {"k": "lint", "v": "0 miss", "bar": 100, "color": "#6f8f5a"},
        ]},
        {"id": "writer", "kind": "node", "title": "writer", "href": "../wiki/llm-wiki.md", "color": "#3a4a5a", "x": 800, "y": 348, "rows": [
            {"k": "out", "v": "wiki/", "bar": 88, "color": "#d4af37"},
            {"k": "concepts", "v": s["concepts"], "bar": 65},
            {"k": "meta", "v": s["meta"], "bar": 40},
        ]},
        {"id": "verify", "kind": "node", "title": "verify", "href": "../wiki/self-verification.md", "color": "#4a3a3a", "x": 1020, "y": 348, "rows": [
            {"k": "sample", "v": "n", "bar": 55},
            {"k": "keep", "v": "best", "bar": 70, "color": "#6f8f5a"},
            {"k": "flag", "v": "C1-C7", "bar": 45, "color": "#c45a4a"},
        ]},
        {"id": "ship", "kind": "node", "title": "ship", "href": "../ship.md", "color": "#6a3a32", "x": 800, "y": 488, "rows": [
            {"k": "post", "v": "no", "bar": 6, "color": "#c45a4a"},
            {"k": "pay", "v": "no", "bar": 6, "color": "#c45a4a"},
            {"k": "human", "v": "yes", "bar": 100, "color": "#eb6b54"},
        ]},
    ]
    edges: list[dict] = []

    def fan(src: str, dst: str, n: int = 6, hot: bool = False, from_side: str = "right", to_side: str = "left") -> None:
        for i in range(n):
            t0 = 0.12 + 0.76 * i / max(n - 1, 1)
            t1 = 0.08 + 0.84 * ((i * 3) % n) / max(n - 1, 1)
            edges.append({"from": src, "to": dst, "t0": t0, "t1": t1, "hot": hot and i % 3 == 0, "fromSide": from_side, "toSide": to_side})

    for src in ("brief", "sources", "constraints", "tokens", "prior"):
        fan(src, "bus", 8, hot=True)
    for dst in ("planner", "decompose", "route", "merge", "dedupe", "rank", "cite", "writer", "verify", "ship"):
        fan("bus", dst, 5, hot=dst in {"planner", "writer", "verify"})
    for dst in ("scout-x", "scout-gh", "scout-hn", "scout-rd", "scout-ph"):
        fan("bus", dst, 4)
    fan("planner", "decompose", 3, hot=True)
    fan("decompose", "route", 3)
    fan("route", "scout-x", 3, hot=True)
    fan("scout-x", "merge", 3)
    fan("merge", "dedupe", 3)
    fan("dedupe", "cite", 3)
    fan("cite", "writer", 3, hot=True)
    fan("writer", "verify", 3)
    fan("verify", "ship", 3, hot=True)
    return nodes, edges


def write_dataflow(dest: Path) -> dict:
    nodes, edges = collect()
    stats = vault_stats(nodes, edges)
    pipe_nodes, pipe_edges = pipeline(stats)
    payload = {
        "hud": [
            ["GRAPH", "second-brain"],
            ["NODES", stats["pages"]],
            ["EDGES", stats["edges"]],
            ["BUS READERS", stats["bus_readers"]],
            ["DEPTH", 2],
            ["SCOUTS", stats["hunt"]],
            ["LOCKED", f"D{stats['decisions']}"],
        ],
        "nodes": pipe_nodes,
        "edges": pipe_edges,
        "log": [
            {"t": "15:34", "m": f"graph.load pages={stats['pages']} edges={stats['edges']}"},
            {"t": "15:34", "m": "bus.attach index · context-graph · audited-task-contract"},
            {"t": "15:35", "m": f"scout.twitter returned raw/x={stats['raw_x']}"},
            {"t": "15:35", "m": "planner.read Home → index → how-it-works"},
            {"t": "15:36", "m": "cite.check lint missing=0 orphans=0"},
            {"t": "15:36", "m": "ship.gate post=no pay=no send=no"},
        ],
        "workers": [
            {"id": "w1", "pct": 100, "ok": True, "label": "twitter  ok"},
            {"id": "w2", "pct": 20, "ok": True, "label": "github  quiet"},
            {"id": "w3", "pct": 20, "ok": True, "label": "hn  quiet"},
            {"id": "w4", "pct": 20, "ok": True, "label": "reddit  quiet"},
            {"id": "w5", "pct": 20, "ok": True, "label": "ph  quiet"},
            {"id": "w6", "pct": 100, "ok": True, "label": "lint  0 miss"},
            {"id": "w7", "pct": 100, "ok": True, "label": "writer  wiki"},
            {"id": "w8", "pct": 100, "ok": True, "label": "human  gate"},
        ],
        "cost": [
            ["pages", stats["pages"]],
            ["wikilinks", stats["edges"]],
            ["bus readers", stats["bus_readers"]],
            ["raw clips", stats["raw_x"]],
            ["relative cost", "compile once"],
        ],
    }
    template = (ROOT / "tools" / "dataflow-template.html").read_text(encoding="utf-8")
    dest.write_text(template.replace("__PAYLOAD__", json.dumps(payload)), encoding="utf-8")
    return payload


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    dest = OUT_DIR / "obsidian-dataflow.html"
    payload = write_dataflow(dest)
    hud = dict(payload["hud"])
    print(f"wrote {dest} pages={hud['NODES']} edges={hud['EDGES']}")


if __name__ == "__main__":
    main()
