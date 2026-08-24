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
        "updated: 2026-08-24",
        "---",
        "",
        "# Graph",
        "",
        "Open Obsidian graph view for the live version. This page is the compiled snapshot.",
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
    write_html(nodes, edges, OUT_DIR / "obsidian-graph.html")
    write_mermaid(nodes, edges, ROOT / "wiki" / "graph.md")
    print(f"nodes={len(nodes)} edges={len(edges)}")


if __name__ == "__main__":
    main()
