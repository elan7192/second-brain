#!/usr/bin/env python3
"""Render the vault graph to HTML and SVG for a result you can open without Obsidian."""

from __future__ import annotations

import json
import math
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "output"
LINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
SKIP_DIRS = {".git", ".obsidian", "templates"}
SKIP_FILES = {"AGENTS.md", "CLAUDE.md", "README.md"}

COLORS = {
    "home": "#d4af37",
    "meta": "#d4af37",
    "concept": "#d4af37",
    "wiki": "#d4af37",
    "map": "#14b8a6",
    "source": "#3b82f6",
    "hunt": "#3b82f6",
    "person": "#22c55e",
    "ship": "#eb6b54",
    "note": "#94a3b8",
}


def note_type(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if path.name == "Home.md":
        return "home"
    if rel.startswith("wiki/sources/") or rel.startswith("hunt/") or path.name == "hunt.md":
        return "source" if rel.startswith("wiki/sources/") else "hunt"
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
        slug: {
            "id": slug,
            "label": slug,
            "type": note_type(path),
            "path": path.relative_to(ROOT).as_posix(),
        }
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


def layout(nodes: dict[str, dict], edges: list[tuple[str, str]]) -> None:
    rings = {
        "home": 0,
        "meta": 140,
        "concept": 260,
        "map": 340,
        "source": 420,
        "hunt": 420,
        "person": 500,
        "ship": 340,
        "note": 500,
    }
    grouped: dict[str, list[str]] = defaultdict(list)
    for slug, node in nodes.items():
        grouped[node["type"]].append(slug)
    for kind, slugs in grouped.items():
        slugs.sort()
        radius = rings.get(kind, 480)
        for i, slug in enumerate(slugs):
            angle = (2 * math.pi * i / max(len(slugs), 1)) - math.pi / 2
            if radius == 0:
                nodes[slug]["x"] = 0
                nodes[slug]["y"] = 0
            else:
                jitter = 18 if i % 2 else 0
                nodes[slug]["x"] = math.cos(angle) * (radius + jitter)
                nodes[slug]["y"] = math.sin(angle) * (radius + jitter)


def vault_stats(nodes: dict[str, dict], edges: list[tuple[str, str]]) -> dict:
    by_type: dict[str, int] = defaultdict(int)
    for node in nodes.values():
        by_type[node["type"]] += 1
    raw_x = len(list((ROOT / "raw" / "x").glob("*.md"))) if (ROOT / "raw" / "x").exists() else 0
    sources = sum(1 for n in nodes.values() if n["type"] == "source")
    people = sum(1 for n in nodes.values() if n["type"] == "person")
    decisions = 0
    memory_lines = 0
    dec = ROOT / "decisions.md"
    if dec.exists():
        decisions = len(re.findall(r"^## D\d+", dec.read_text(encoding="utf-8"), re.M))
    mem = ROOT / "MEMORY.md"
    if mem.exists():
        memory_lines = sum(
            1
            for line in mem.read_text(encoding="utf-8").splitlines()
            if line.startswith("- ")
        )
    return {
        "pages": len(nodes),
        "edges": len(edges),
        "raw_x": raw_x,
        "sources": sources,
        "people": people,
        "concepts": by_type.get("concept", 0),
        "meta": by_type.get("meta", 0),
        "hunt": by_type.get("hunt", 0),
        "ship": by_type.get("ship", 0),
        "maps": by_type.get("map", 0),
        "decisions": decisions,
        "memory": memory_lines,
        "bus_readers": sum(1 for src, dst in edges if dst in {"index", "context-graph", "Home"}),
    }


def pipeline(stats: dict) -> tuple[list[dict], list[dict]]:
    """Map this vault onto the dark dataflow layout from the Bober clip."""
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
            {"k": "locked", "v": f"D1–D{s['decisions']}", "bar": 90, "color": "#c8a24a"},
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
            {"k": "today", "v": "08-23", "bar": 40},
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
            {"k": "flag", "v": "C1–C7", "bar": 45, "color": "#c45a4a"},
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


def write_dataflow(nodes: dict[str, dict], edges: list[tuple[str, str]], dest: Path) -> dict:
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


def write_svg(nodes: dict[str, dict], edges: list[tuple[str, str]], dest: Path) -> None:
    width, height = 1400, 1100
    cx, cy = width / 2, height / 2 + 20
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '<rect width="100%" height="100%" fill="#0f1115"/>',
        '<text x="40" y="48" fill="#e7e5e4" font-family="ui-sans-serif,system-ui,sans-serif" font-size="22">Second brain · Obsidian graph</text>',
        '<text x="40" y="74" fill="#a8a29e" font-family="ui-sans-serif,system-ui,sans-serif" font-size="13">gold wiki · teal maps · blue hunt/twitter · green people · coral ship</text>',
    ]
    for src, dst in edges:
        a, b = nodes[src], nodes[dst]
        lines.append(
            f'<line x1="{cx+a["x"]:.1f}" y1="{cy+a["y"]:.1f}" x2="{cx+b["x"]:.1f}" y2="{cy+b["y"]:.1f}" stroke="#3f3f46" stroke-width="1.1"/>'
        )
    for node in nodes.values():
        color = COLORS.get(node["type"], "#94a3b8")
        r = 9 if node["type"] in {"home", "meta"} else 6
        x, y = cx + node["x"], cy + node["y"]
        lines.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"/>')
        lines.append(
            f'<text x="{x+10:.1f}" y="{y+4:.1f}" fill="#d6d3d1" font-family="ui-sans-serif,system-ui,sans-serif" font-size="11">{node["label"]}</text>'
        )
    lines.append("</svg>")
    dest.write_text("\n".join(lines), encoding="utf-8")


def write_html(nodes: dict[str, dict], edges: list[tuple[str, str]], dest: Path) -> None:
    payload = {
        "nodes": list(nodes.values()),
        "edges": [{"source": a, "target": b} for a, b in edges],
        "colors": COLORS,
    }
    dest.write_text(
        """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>Second brain graph</title>
  <style>
    html, body { margin: 0; height: 100%; background: #0f1115; color: #e7e5e4; font-family: ui-sans-serif, system-ui, sans-serif; }
    header { position: fixed; top: 20px; left: 24px; z-index: 2; }
    h1 { margin: 0 0 6px; font-size: 22px; font-weight: 600; }
    p { margin: 0; color: #a8a29e; font-size: 13px; }
    canvas { display: block; width: 100%; height: 100%; }
  </style>
</head>
<body>
  <header>
    <h1>Second brain · Obsidian graph</h1>
    <p>gold wiki · teal maps · blue hunt/twitter · green people · coral ship</p>
  </header>
  <canvas id="g"></canvas>
  <script>
  const data = """
        + json.dumps(payload)
        + """;
  const canvas = document.getElementById('g');
  const ctx = canvas.getContext('2d');
  const nodes = data.nodes;
  const byId = Object.fromEntries(nodes.map(n => [n.id, n]));
  function resize() {
    canvas.width = window.innerWidth * devicePixelRatio;
    canvas.height = window.innerHeight * devicePixelRatio;
    ctx.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);
  }
  window.addEventListener('resize', resize);
  resize();
  const cx = () => window.innerWidth / 2;
  const cy = () => window.innerHeight / 2 + 10;
  function draw() {
    ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);
    ctx.strokeStyle = '#3f3f46';
    ctx.lineWidth = 1;
    for (const e of data.edges) {
      const a = byId[e.source], b = byId[e.target];
      ctx.beginPath();
      ctx.moveTo(cx() + a.x, cy() + a.y);
      ctx.lineTo(cx() + b.x, cy() + b.y);
      ctx.stroke();
    }
    for (const n of nodes) {
      ctx.fillStyle = data.colors[n.type] || '#94a3b8';
      ctx.beginPath();
      ctx.arc(cx() + n.x, cy() + n.y, n.type === 'home' || n.type === 'meta' ? 8 : 5.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#d6d3d1';
      ctx.font = '12px ui-sans-serif, system-ui, sans-serif';
      ctx.fillText(n.label, cx() + n.x + 9, cy() + n.y + 4);
    }
  }
  draw();
  </script>
</body>
</html>
""",
        encoding="utf-8",
    )


def write_mermaid(nodes: dict[str, dict], edges: list[tuple[str, str]], dest: Path) -> None:
    lines = [
        "---",
        "type: meta",
        "tags:",
        "  - wiki",
        "created: 2026-08-23",
        "updated: 2026-08-23",
        "---",
        "",
        "# Graph",
        "",
        "Open Obsidian graph view for the live version. Dark dataflow: `output/obsidian-graph.html`. Canvas: `maps/dataflow.canvas`. This mermaid is the compiled snapshot.",
        "",
        "```mermaid",
        "flowchart LR",
    ]
    keep_types = {"home", "meta", "concept", "map", "person"}
    keep = {slug for slug, node in nodes.items() if node["type"] in keep_types}
    keep.update({"twitter", "ship", "hunt", "agent-operating-system"})
    for src, dst in edges:
        if src in keep and dst in keep:
            lines.append(f"  {src} --> {dst}")
    lines.append("```")
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    nodes, edges = collect()
    layout(nodes, edges)
    OUT_DIR.mkdir(exist_ok=True)
    write_svg(nodes, edges, OUT_DIR / "obsidian-graph.svg")
    write_dataflow(nodes, edges, OUT_DIR / "obsidian-graph.html")
    write_mermaid(nodes, edges, ROOT / "wiki" / "graph.md")
    print(f"nodes={len(nodes)} edges={len(edges)}")


if __name__ == "__main__":
    main()
