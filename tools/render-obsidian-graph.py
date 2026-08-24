#!/usr/bin/env python3
"""Render the vault graph as concept islands, not a folder ring."""

from __future__ import annotations

import json
import math
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "output"
GRAPH_PAGE = ROOT / "wiki" / "graph.md"
LINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
SKIP_DIRS = {".git", ".obsidian", "templates", "raw"}
SKIP_FILES = {"AGENTS.md", "CLAUDE.md", "README.md"}
# Catalog stars. They stay in the vault. They do not sit in this graph.
HIDDEN = {"index", "log", "twitter", "decisions"}
# Hunt/ship leaf indexes. Visible in Obsidian. Too many for the snapshot.
SNAPSHOT_HIDDEN = {
    "github",
    "hacker-news",
    "reddit",
    "product-hunt",
    "inbox",
    "digests",
    "drafts",
    "angles",
    "builds",
}
# Draw only the five-layer spokes from the synthesis node.
BRIDGE_KEEP = {
    "llm-wiki",
    "memory-engineering",
    "verifiable-instructions",
    "audited-task-contract",
    "hunt-ship-loop",
}

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

# Islands from wiki/agent-operating-system.md. Sources and people sit
# with the concept they already cite.
CLUSTER_SEEDS: dict[str, set[str]] = {
    "compile": {
        "llm-wiki",
        "tokens-as-capital",
        "context-graph",
        "how-it-works",
        "src-papa-couch-compiler",
        "src-bober-folder-workflow",
        "andrej-karpathy",
    },
    "memory": {
        "memory-engineering",
        "memory-ablation",
        "MEMORY",
        "src-0xcodio-memory-ablation",
    },
    "verification": {
        "verifiable-instructions",
        "self-verification",
        "anti-slop",
        "src-voxyz-verifiable-instructions",
        "src-jacky-self-verification",
        "src-juampi-anti-slop-rank",
        "jacky-kwok",
    },
    "harness": {
        "audited-task-contract",
        "harness-routing",
        "entropy-gate",
        "src-rohit-harness-router",
        "src-hitu-entropy-engineering",
        "rohit",
    },
    "hunt-ship": {
        "hunt-ship-loop",
        "hunt",
        "ship",
        "maps",
        "github",
        "hacker-news",
        "reddit",
        "product-hunt",
        "inbox",
        "digests",
        "drafts",
        "angles",
        "builds",
        "ingest-brief-2026-08-23",
        "graph-clusters-2026-08-24",
        "src-avid-obsidian-agent-team",
        "Jarvis",
        "TELOS",
        "Hooks",
    },
    "nav": {
        "Home",
        "Today",
        "graph",
        "wiki",
        "contradictions",
    },
    "bridge": {
        "agent-operating-system",
    },
}

CLUSTER_OF = {slug: cluster for cluster, slugs in CLUSTER_SEEDS.items() for slug in slugs}

CLUSTER_ANCHORS = {
    "compile": (-520.0, -280.0),
    "verification": (520.0, -280.0),
    "memory": (-520.0, 210.0),
    "harness": (520.0, 210.0),
    "hunt-ship": (0.0, 460.0),
    "nav": (0.0, -460.0),
    "bridge": (0.0, -20.0),
}

CLUSTER_LABELS = {
    "compile": "Compile",
    "memory": "Memory",
    "verification": "Verification",
    "harness": "Harness",
    "hunt-ship": "Hunt / ship",
    "nav": "Door",
    "bridge": "Synthesis",
}

MERMAID_SKIP = {
    "Home",
    "how-it-works",
    "contradictions",
    "Today",
    "graph",
    "wiki",
    "Jarvis",
    "TELOS",
    "Hooks",
    "github",
    "hacker-news",
    "reddit",
    "product-hunt",
    "inbox",
    "digests",
    "drafts",
    "angles",
    "builds",
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
            "graph.md",
        }:
            return "meta"
        return "concept"
    return "note"


def cluster_for(slug: str, path: Path) -> str:
    if slug in CLUSTER_OF:
        return CLUSTER_OF[slug]
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith("wiki/sources/") or rel.startswith("wiki/people/"):
        return "nav"
    if rel.startswith("hunt/") or rel.startswith("ship/") or rel.startswith("maps/") or rel.startswith("output/"):
        return "hunt-ship"
    if rel.startswith("wiki/"):
        return "nav"
    return "nav"


def collect() -> tuple[dict[str, dict], list[tuple[str, str]]]:
    pages: dict[str, Path] = {}
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        if path.stem in HIDDEN or path.stem in SNAPSHOT_HIDDEN:
            continue
        pages[path.stem] = path

    nodes = {
        slug: {
            "id": slug,
            "label": slug,
            "type": note_type(path),
            "cluster": cluster_for(slug, path),
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


def seed_positions(nodes: dict[str, dict]) -> None:
    grouped: dict[str, list[str]] = defaultdict(list)
    for slug, node in nodes.items():
        grouped[node["cluster"]].append(slug)
    for cluster, slugs in grouped.items():
        slugs.sort()
        ax, ay = CLUSTER_ANCHORS.get(cluster, (0.0, 0.0))
        n = max(len(slugs), 1)
        if n == 1:
            nodes[slugs[0]]["x"] = ax
            nodes[slugs[0]]["y"] = ay
            continue
        rx = 70 + 11 * n
        ry = 52 + 8 * n
        if cluster == "hunt-ship":
            rx, ry = 300.0, 120.0
        if cluster == "nav":
            rx, ry = 160.0, 55.0
        for i, slug in enumerate(slugs):
            angle = (2 * math.pi * i / n) - math.pi / 2
            nodes[slug]["x"] = ax + math.cos(angle) * rx
            nodes[slug]["y"] = ay + math.sin(angle) * ry


def visible_edge(src: str, dst: str) -> bool:
    if src == "agent-operating-system":
        return dst in BRIDGE_KEEP
    if dst == "agent-operating-system":
        return src in BRIDGE_KEEP
    if src in {"Home", "how-it-works", "contradictions", "graph", "Today", "wiki"}:
        return False
    if dst in {"Home", "how-it-works", "contradictions", "graph", "Today", "wiki"}:
        return False
    return True


def edge_weight(nodes: dict[str, dict], src: str, dst: str) -> float:
    a, b = nodes[src]["cluster"], nodes[dst]["cluster"]
    if a == b:
        return 1.0
    if "bridge" in {a, b}:
        return 0.18
    if "nav" in {a, b}:
        return 0.08
    return 0.12


def layout(nodes: dict[str, dict], edges: list[tuple[str, str]]) -> None:
    seed_positions(nodes)
    slugs = list(nodes)
    for _ in range(180):
        force: dict[str, list[float]] = {slug: [0.0, 0.0] for slug in slugs}
        for slug, node in nodes.items():
            ax, ay = CLUSTER_ANCHORS[node["cluster"]]
            force[slug][0] += (ax - node["x"]) * 0.14
            force[slug][1] += (ay - node["y"]) * 0.14
        for i, a in enumerate(slugs):
            na = nodes[a]
            for b in slugs[i + 1 :]:
                nb = nodes[b]
                dx = na["x"] - nb["x"]
                dy = na["y"] - nb["y"]
                dist = math.hypot(dx, dy) or 0.01
                same = na["cluster"] == nb["cluster"]
                strength = 420.0 if same else 900.0
                push = strength / (dist * dist)
                push = min(push, 8.0)
                ux, uy = dx / dist, dy / dist
                force[a][0] += ux * push
                force[a][1] += uy * push
                force[b][0] -= ux * push
                force[b][1] -= uy * push
        for src, dst in edges:
            if not visible_edge(src, dst):
                continue
            na, nb = nodes[src], nodes[dst]
            dx = nb["x"] - na["x"]
            dy = nb["y"] - na["y"]
            dist = math.hypot(dx, dy) or 0.01
            pull = 0.016 * dist * edge_weight(nodes, src, dst)
            ux, uy = dx / dist, dy / dist
            force[src][0] += ux * pull
            force[src][1] += uy * pull
            force[dst][0] -= ux * pull
            force[dst][1] -= uy * pull
        for slug, node in nodes.items():
            node["x"] += force[slug][0] * 0.65
            node["y"] += force[slug][1] * 0.65


def write_svg(nodes: dict[str, dict], edges: list[tuple[str, str]], dest: Path) -> None:
    width, height = 1700, 1300
    cx, cy = width / 2, height / 2 + 10
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '<rect width="100%" height="100%" fill="#0f1115"/>',
        '<text x="40" y="48" fill="#e7e5e4" font-family="ui-sans-serif,system-ui,sans-serif" font-size="22">Second brain · concept clusters</text>',
        '<text x="40" y="74" fill="#a8a29e" font-family="ui-sans-serif,system-ui,sans-serif" font-size="13">gold wiki · teal maps · blue hunt/twitter · green people · coral ship</text>',
    ]
    for cluster, (ax, ay) in CLUSTER_ANCHORS.items():
        label = CLUSTER_LABELS[cluster]
        x, y = cx + ax, cy + ay - (150 if cluster == "hunt-ship" else 95)
        if cluster == "bridge":
            y = cy + ay - 36
        lines.append(
            f'<text x="{x:.1f}" y="{y:.1f}" fill="#78716c" font-family="ui-sans-serif,system-ui,sans-serif" font-size="13" text-anchor="middle">{label}</text>'
        )
    drawn = [(src, dst) for src, dst in edges if visible_edge(src, dst)]
    for src, dst in drawn:
        a, b = nodes[src], nodes[dst]
        intra = a["cluster"] == b["cluster"]
        stroke = "#52525b" if intra else "#3f3f46"
        width_s = "1.4" if intra else "0.9"
        lines.append(
            f'<line x1="{cx+a["x"]:.1f}" y1="{cy+a["y"]:.1f}" x2="{cx+b["x"]:.1f}" y2="{cy+b["y"]:.1f}" stroke="{stroke}" stroke-width="{width_s}"/>'
        )
    for node in nodes.values():
        color = COLORS.get(node["type"], "#94a3b8")
        r = 10 if node["type"] in {"home", "meta"} and node["cluster"] == "bridge" else 7
        if node["id"] == "Home":
            r = 9
        x, y = cx + node["x"], cy + node["y"]
        lines.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"/>')
        lines.append(
            f'<text x="{x+11:.1f}" y="{y+4:.1f}" fill="#d6d3d1" font-family="ui-sans-serif,system-ui,sans-serif" font-size="11">{node["label"]}</text>'
        )
    lines.append("</svg>")
    dest.write_text("\n".join(lines), encoding="utf-8")


def write_html(nodes: dict[str, dict], edges: list[tuple[str, str]], dest: Path) -> None:
    payload = {
        "nodes": list(nodes.values()),
        "edges": [{"source": a, "target": b} for a, b in edges if visible_edge(a, b)],
        "colors": COLORS,
        "anchors": CLUSTER_ANCHORS,
        "labels": CLUSTER_LABELS,
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
    <h1>Second brain · concept clusters</h1>
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
    ctx.fillStyle = '#78716c';
    ctx.font = '13px ui-sans-serif, system-ui, sans-serif';
    ctx.textAlign = 'center';
    for (const [cluster, pos] of Object.entries(data.anchors)) {
      const lift = cluster === 'hunt-ship' ? 150 : cluster === 'bridge' ? 36 : 95;
      ctx.fillText(data.labels[cluster], cx() + pos[0], cy() + pos[1] - lift);
    }
    ctx.textAlign = 'left';
    for (const e of data.edges) {
      const a = byId[e.source], b = byId[e.target];
      ctx.strokeStyle = a.cluster === b.cluster ? '#52525b' : '#27272a';
      ctx.lineWidth = a.cluster === b.cluster ? 1.3 : 0.8;
      ctx.beginPath();
      ctx.moveTo(cx() + a.x, cy() + a.y);
      ctx.lineTo(cx() + b.x, cy() + b.y);
      ctx.stroke();
    }
    for (const n of nodes) {
      ctx.fillStyle = data.colors[n.type] || '#94a3b8';
      const r = n.id === 'agent-operating-system' ? 9 : n.id === 'Home' ? 8 : 5.5;
      ctx.beginPath();
      ctx.arc(cx() + n.x, cy() + n.y, r, 0, Math.PI * 2);
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


def write_png(nodes: dict[str, dict], edges: list[tuple[str, str]], dest: Path) -> None:
    from PIL import Image, ImageDraw, ImageFont

    width, height = 1700, 1300
    cx, cy = width / 2, height / 2 + 10
    img = Image.new("RGB", (width, height), "#0f1115")
    draw = ImageDraw.Draw(img)
    font_title = ImageFont.truetype(
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 28
    )
    font_sub = ImageFont.truetype(
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 16
    )
    font_label = ImageFont.truetype(
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 14
    )
    font_node = ImageFont.truetype(
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 13
    )
    draw.text((40, 28), "Second brain · concept clusters", fill="#e7e5e4", font=font_title)
    draw.text(
        (40, 66),
        "gold wiki · teal maps · blue hunt/twitter · green people · coral ship",
        fill="#a8a29e",
        font=font_sub,
    )
    for cluster, (ax, ay) in CLUSTER_ANCHORS.items():
        lift = 150 if cluster == "hunt-ship" else 36 if cluster == "bridge" else 95
        x, y = cx + ax, cy + ay - lift
        label = CLUSTER_LABELS[cluster]
        bbox = draw.textbbox((0, 0), label, font=font_label)
        draw.text((x - (bbox[2] - bbox[0]) / 2, y), label, fill="#78716c", font=font_label)
    for src, dst in edges:
        if not visible_edge(src, dst):
            continue
        a, b = nodes[src], nodes[dst]
        intra = a["cluster"] == b["cluster"]
        draw.line(
            [(cx + a["x"], cy + a["y"]), (cx + b["x"], cy + b["y"])],
            fill="#52525b" if intra else "#27272a",
            width=2 if intra else 1,
        )
    for node in nodes.values():
        color = COLORS.get(node["type"], "#94a3b8")
        r = 10 if node["id"] == "agent-operating-system" else 8 if node["id"] == "Home" else 6
        x, y = cx + node["x"], cy + node["y"]
        draw.ellipse((x - r, y - r, x + r, y + r), fill=color)
        draw.text((x + 11, y - 7), node["label"], fill="#d6d3d1", font=font_node)
    img.save(dest)


def mermaid_lines(nodes: dict[str, dict], edges: list[tuple[str, str]]) -> list[str]:
    keep = {
        slug
        for slug, node in nodes.items()
        if slug not in MERMAID_SKIP and node["cluster"] != "nav"
    }
    keep.add("agent-operating-system")
    order = ["compile", "memory", "verification", "harness", "hunt-ship", "bridge"]
    grouped: dict[str, list[str]] = defaultdict(list)
    for slug in keep:
        grouped[nodes[slug]["cluster"]].append(slug)
    lines = ["flowchart TB"]
    for cluster in order:
        slugs = sorted(grouped.get(cluster, []))
        if not slugs:
            continue
        lines.append(f"  subgraph {cluster}[{CLUSTER_LABELS[cluster]}]")
        for slug in slugs:
            lines.append(f"    {slug}")
        lines.append("  end")
    for src, dst in edges:
        if src in keep and dst in keep and visible_edge(src, dst):
            lines.append(f"  {src} --> {dst}")
    return lines


def write_mermaid(nodes: dict[str, dict], edges: list[tuple[str, str]], dest: Path) -> None:
    text = dest.read_text(encoding="utf-8")
    begin = "<!-- graph-mermaid:begin -->"
    end = "<!-- graph-mermaid:end -->"
    block = (
        begin
        + "\n```mermaid\n"
        + "\n".join(mermaid_lines(nodes, edges))
        + "\n```\n"
        + end
    )
    if begin in text and end in text:
        pre, rest = text.split(begin, 1)
        _, post = rest.split(end, 1)
        dest.write_text(pre + block + post, encoding="utf-8")
        return
    dest.write_text(text.rstrip() + "\n\n" + block + "\n", encoding="utf-8")


def main() -> None:
    nodes, edges = collect()
    layout(nodes, edges)
    OUT_DIR.mkdir(exist_ok=True)
    write_svg(nodes, edges, OUT_DIR / "obsidian-graph.svg")
    write_html(nodes, edges, OUT_DIR / "obsidian-graph.html")
    write_png(nodes, edges, OUT_DIR / "obsidian-graph.png")
    write_mermaid(nodes, edges, GRAPH_PAGE)
    counts: dict[str, int] = defaultdict(int)
    for node in nodes.values():
        counts[node["cluster"]] += 1
    drawn = sum(1 for a, b in edges if visible_edge(a, b))
    print(f"nodes={len(nodes)} edges={len(edges)} drawn={drawn} hidden={sorted(HIDDEN)}")
    print("clusters", dict(sorted(counts.items())))


if __name__ == "__main__":
    main()
