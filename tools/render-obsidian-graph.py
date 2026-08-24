#!/usr/bin/env python3
"""Render the vault graph as concept islands, not a folder ring."""

from __future__ import annotations

import json
import math
import re
import shutil
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "output"
GRAPH_PAGE = ROOT / "wiki" / "graph.md"
LINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
HEADING = re.compile(r"^#\s+(.+)$", re.M)
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
    "home": "#c6a35a",
    "meta": "#c6a35a",
    "concept": "#c6a35a",
    "wiki": "#c6a35a",
    "map": "#6f9e92",
    "source": "#6f87a8",
    "hunt": "#6f87a8",
    "person": "#7d9a6e",
    "ship": "#c48472",
    "note": "#8b8478",
}

TYPE_LABELS = {
    "home": "Door",
    "meta": "Meta",
    "concept": "Concept",
    "wiki": "Wiki",
    "map": "Map",
    "source": "Source",
    "hunt": "Hunt",
    "person": "Person",
    "ship": "Ship",
    "note": "Note",
}

COLOR_LEGEND = [
    {"key": "wiki", "label": "Wiki", "color": "#c6a35a"},
    {"key": "map", "label": "Maps", "color": "#6f9e92"},
    {"key": "hunt", "label": "Hunt / sources", "color": "#6f87a8"},
    {"key": "person", "label": "People", "color": "#7d9a6e"},
    {"key": "ship", "label": "Ship", "color": "#c48472"},
]

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
        "graph-ui-2026-08-24",
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
    "compile": (-165.0, -10.0),
    "verification": (145.0, -85.0),
    "memory": (-30.0, 120.0),
    "harness": (150.0, 60.0),
    "hunt-ship": (50.0, 185.0),
    "nav": (-25.0, -160.0),
    "bridge": (-12.0, 28.0),
}
CLUSTER_PHASE = {
    "compile": 0.4,
    "verification": 1.7,
    "memory": 2.5,
    "harness": 3.8,
    "hunt-ship": 0.9,
    "nav": 5.1,
    "bridge": 0.0,
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


def page_title(path: Path, slug: str) -> str:
    match = HEADING.search(path.read_text(encoding="utf-8"))
    return match.group(1).strip() if match else slug


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
            "title": page_title(path, slug),
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
    golden = math.pi * (3.0 - math.sqrt(5.0))
    for cluster, slugs in grouped.items():
        slugs.sort()
        ax, ay = CLUSTER_ANCHORS.get(cluster, (0.0, 0.0))
        n = max(len(slugs), 1)
        if n == 1:
            nodes[slugs[0]]["x"] = ax
            nodes[slugs[0]]["y"] = ay
            continue
        spread = 22.0 + 5.2 * math.sqrt(n)
        if cluster == "hunt-ship":
            spread = 30.0 + 6.0 * math.sqrt(n)
        phase = CLUSTER_PHASE.get(cluster, 0.0)
        for i, slug in enumerate(slugs):
            radius = spread * math.sqrt((i + 0.35) / n)
            angle = i * golden + phase
            nodes[slug]["x"] = ax + math.cos(angle) * radius
            nodes[slug]["y"] = ay + math.sin(angle) * radius


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
        return 1.05
    if "bridge" in {a, b}:
        return 0.42
    if "nav" in {a, b}:
        return 0.16
    return 0.3


def layout(nodes: dict[str, dict], edges: list[tuple[str, str]]) -> None:
    seed_positions(nodes)
    slugs = list(nodes)
    drawn = [(src, dst) for src, dst in edges if visible_edge(src, dst)]
    for _ in range(240):
        force: dict[str, list[float]] = {slug: [0.0, 0.0] for slug in slugs}
        for slug, node in nodes.items():
            ax, ay = CLUSTER_ANCHORS[node["cluster"]]
            force[slug][0] += (ax - node["x"]) * 0.07
            force[slug][1] += (ay - node["y"]) * 0.07
        for i, a in enumerate(slugs):
            na = nodes[a]
            for b in slugs[i + 1 :]:
                nb = nodes[b]
                dx = na["x"] - nb["x"]
                dy = na["y"] - nb["y"]
                dist = math.hypot(dx, dy) or 0.01
                same = na["cluster"] == nb["cluster"]
                min_d = 38.0 if same else 52.0
                strength = 260.0 if same else 420.0
                push = min(strength / (dist * dist), 12.0)
                if dist < min_d:
                    push += (min_d - dist) * 0.42
                ux, uy = dx / dist, dy / dist
                force[a][0] += ux * push
                force[a][1] += uy * push
                force[b][0] -= ux * push
                force[b][1] -= uy * push
        for src, dst in drawn:
            na, nb = nodes[src], nodes[dst]
            dx = nb["x"] - na["x"]
            dy = nb["y"] - na["y"]
            dist = math.hypot(dx, dy) or 0.01
            pull = 0.018 * dist * edge_weight(nodes, src, dst)
            ux, uy = dx / dist, dy / dist
            force[src][0] += ux * pull
            force[src][1] += uy * pull
            force[dst][0] -= ux * pull
            force[dst][1] -= uy * pull
        for slug, node in nodes.items():
            node["x"] += force[slug][0] * 0.6
            node["y"] += force[slug][1] * 0.6


def cluster_centers(nodes: dict[str, dict]) -> dict[str, tuple[float, float, float]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for node in nodes.values():
        grouped[node["cluster"]].append(node)
    centers: dict[str, tuple[float, float, float]] = {}
    for cluster, items in grouped.items():
        mx = sum(item["x"] for item in items) / len(items)
        my = sum(item["y"] for item in items) / len(items)
        radius = max(math.hypot(item["x"] - mx, item["y"] - my) for item in items) + 20.0
        centers[cluster] = (mx, my, radius)
    return centers


def cluster_headers(nodes: dict[str, dict]) -> dict[str, tuple[float, float]]:
    centers = cluster_centers(nodes)
    if not centers:
        return {}
    gx = sum(item[0] for item in centers.values()) / len(centers)
    gy = sum(item[1] for item in centers.values()) / len(centers)
    headers: dict[str, tuple[float, float]] = {}
    placed: list[tuple[float, float, float, float]] = []
    for cluster, (mx, my, radius) in sorted(centers.items(), key=lambda item: item[0]):
        dx, dy = mx - gx, my - gy
        dist = math.hypot(dx, dy) or 1.0
        ux, uy = dx / dist, dy / dist
        if cluster == "bridge":
            hx, hy = mx + radius + 46.0, my - 8.0
        else:
            hx, hy = mx + ux * (radius + 28.0), my + uy * (radius + 20.0)
        box = (hx - 58.0, hy - 12.0, 116.0, 24.0)
        extra = 0.0
        while any(
            not (box[0] + box[2] < px or px + pw < box[0] or box[1] + box[3] < py or py + ph < box[1])
            for px, py, pw, ph in placed
        ) and extra < 90.0:
            extra += 14.0
            hx, hy = mx + ux * (radius + 28.0 + extra), my + uy * (radius + 20.0 + extra)
            box = (hx - 58.0, hy - 12.0, 116.0, 24.0)
        headers[cluster] = (hx, hy)
        placed.append(box)
    return headers


def edge_records(nodes: dict[str, dict], edges: list[tuple[str, str]]) -> list[dict]:
    centers = cluster_centers(nodes)
    records: list[dict] = []
    for src, dst in edges:
        if not visible_edge(src, dst):
            continue
        a, b = nodes[src], nodes[dst]
        mx = (a["x"] + b["x"]) / 2
        my = (a["y"] + b["y"]) / 2
        dx = b["x"] - a["x"]
        dy = b["y"] - a["y"]
        dist = math.hypot(dx, dy) or 1.0
        intra = a["cluster"] == b["cluster"]
        if intra:
            sign = 1.0 if ((hash(src) + hash(dst)) % 2) else -1.0
            bend = min(36.0, 12.0 + dist * 0.14)
            cx = mx - (dy / dist) * bend * sign
            cy = my + (dx / dist) * bend * sign
        else:
            ca = centers[a["cluster"]]
            cb = centers[b["cluster"]]
            bx = (ca[0] + cb[0]) / 2
            by = (ca[1] + cb[1]) / 2
            cx = mx * 0.28 + bx * 0.72
            cy = my * 0.28 + by * 0.72
        records.append({"source": src, "target": dst, "cx": cx, "cy": cy, "intra": intra})
    return records


def quad_points(
    x1: float, y1: float, cx: float, cy: float, x2: float, y2: float, steps: int = 18
) -> list[tuple[float, float]]:
    pts: list[tuple[float, float]] = []
    for i in range(steps + 1):
        t = i / steps
        u = 1.0 - t
        pts.append(
            (
                u * u * x1 + 2 * u * t * cx + t * t * x2,
                u * u * y1 + 2 * u * t * cy + t * t * y2,
            )
        )
    return pts


def write_svg(nodes: dict[str, dict], edges: list[tuple[str, str]], dest: Path) -> None:
    width, height = 1600, 1200
    ox, oy = width / 2, height / 2 + 20
    centers = cluster_centers(nodes)
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '<rect width="100%" height="100%" fill="#090b10"/>',
        '<text x="40" y="48" fill="#f4efe4" font-family="ui-sans-serif,system-ui,sans-serif" font-size="22">Second brain · concept clusters</text>',
        '<text x="40" y="74" fill="#9a9386" font-family="ui-sans-serif,system-ui,sans-serif" font-size="13">gold wiki · teal maps · blue hunt/sources · green people · coral ship</text>',
    ]
    headers = cluster_headers(nodes)
    for cluster, (mx, my, radius) in centers.items():
        lines.append(
            f'<circle cx="{ox+mx:.1f}" cy="{oy+my:.1f}" r="{radius:.1f}" fill="rgba(198,163,90,0.04)" stroke="rgba(198,163,90,0.14)" stroke-width="1"/>'
        )
        hx, hy = headers[cluster]
        label = CLUSTER_LABELS[cluster].upper()
        lines.append(
            f'<text x="{ox+hx:.1f}" y="{oy+hy:.1f}" fill="#c4bba8" font-family="ui-sans-serif,system-ui,sans-serif" font-size="13" letter-spacing="0.12em" text-anchor="middle">{label}</text>'
        )
    for rec in edge_records(nodes, edges):
        bridge = rec["source"] == "agent-operating-system" or rec["target"] == "agent-operating-system"
        if not rec["intra"] and not bridge:
            continue
        a, b = nodes[rec["source"]], nodes[rec["target"]]
        stroke = "#c4bba8" if rec["intra"] else "#9a9080"
        width_s = "2.0" if rec["intra"] else "1.45"
        lines.append(
            f'<path d="M {ox+a["x"]:.1f} {oy+a["y"]:.1f} Q {ox+rec["cx"]:.1f} {oy+rec["cy"]:.1f} {ox+b["x"]:.1f} {oy+b["y"]:.1f}" fill="none" stroke="{stroke}" stroke-width="{width_s}" stroke-opacity="0.88"/>'
        )
    for node in nodes.values():
        color = COLORS.get(node["type"], "#8b8478")
        r = 10 if node["id"] == "agent-operating-system" else 8 if node["id"] == "Home" else 6
        x, y = ox + node["x"], oy + node["y"]
        lines.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"/>')
    lines.append("</svg>")
    dest.write_text("\n".join(lines), encoding="utf-8")


def write_html(nodes: dict[str, dict], edges: list[tuple[str, str]], dest: Path) -> None:
    centers = cluster_centers(nodes)
    payload = {
        "nodes": list(nodes.values()),
        "edges": edge_records(nodes, edges),
        "colors": COLORS,
        "labels": CLUSTER_LABELS,
        "types": TYPE_LABELS,
        "legend": COLOR_LEGEND,
        "centers": {key: [mx, my, radius] for key, (mx, my, radius) in centers.items()},
        "headers": {key: [x, y] for key, (x, y) in cluster_headers(nodes).items()},
    }
    dest.write_text(
        GRAPH_HTML.replace("__GRAPH_DATA__", json.dumps(payload).replace("<", "\\u003c")),
        encoding="utf-8",
    )


def write_png(nodes: dict[str, dict], edges: list[tuple[str, str]], dest: Path) -> None:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("skip png: Pillow not installed")
        return

    width, height = 1600, 1200
    ox, oy = width / 2, height / 2 + 20
    font_title = ImageFont.truetype(
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 28
    )
    font_sub = ImageFont.truetype(
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 16
    )
    font_label = ImageFont.truetype(
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 14
    )
    img = Image.new("RGB", (width, height), "#090b10")
    draw = ImageDraw.Draw(img)
    draw.text((40, 28), "Second brain · concept clusters", fill="#f4efe4", font=font_title)
    draw.text(
        (40, 66),
        "gold wiki · teal maps · blue hunt/sources · green people · coral ship",
        fill="#9a9386",
        font=font_sub,
    )
    headers = cluster_headers(nodes)
    for cluster, (mx, my, radius) in cluster_centers(nodes).items():
        draw.ellipse(
            (ox + mx - radius, oy + my - radius, ox + mx + radius, oy + my + radius),
            outline="#4a4338",
            width=1,
        )
        hx, hy = headers[cluster]
        label = CLUSTER_LABELS[cluster].upper()
        bbox = draw.textbbox((0, 0), label, font=font_label)
        draw.text(
            (ox + hx - (bbox[2] - bbox[0]) / 2, oy + hy - 8),
            label,
            fill="#c4bba8",
            font=font_label,
        )
    for rec in edge_records(nodes, edges):
        bridge = rec["source"] == "agent-operating-system" or rec["target"] == "agent-operating-system"
        if not rec["intra"] and not bridge:
            continue
        a, b = nodes[rec["source"]], nodes[rec["target"]]
        pts = [
            (ox + x, oy + y)
            for x, y in quad_points(a["x"], a["y"], rec["cx"], rec["cy"], b["x"], b["y"])
        ]
        draw.line(
            pts,
            fill="#c4bba8" if rec["intra"] else "#9a9080",
            width=3 if rec["intra"] else 2,
        )
    for node in nodes.values():
        color = COLORS.get(node["type"], "#8b8478")
        r = 10 if node["id"] == "agent-operating-system" else 8 if node["id"] == "Home" else 6
        x, y = ox + node["x"], oy + node["y"]
        draw.ellipse((x - r, y - r, x + r, y + r), fill=color)
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


GRAPH_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Second brain · concept clusters</title>
  <style>
    :root {
      --bg: #090b10;
      --ink: #f4efe4;
      --muted: #9a9386;
      --dim: #6d675c;
      --panel: rgba(14, 16, 22, 0.78);
      --stroke: rgba(255, 255, 255, 0.08);
      --gold: #c6a35a;
      --font: "Segoe UI Variable", "SF Pro Text", "Helvetica Neue", ui-sans-serif, system-ui, sans-serif;
      --mono: "SF Mono", "Cascadia Code", ui-monospace, Menlo, Consolas, monospace;
    }
    * { box-sizing: border-box; }
    html, body { margin: 0; height: 100%; background: var(--bg); color: var(--ink); font-family: var(--font); }
    body { overflow: hidden; }
    canvas { display: block; width: 100%; height: 100%; cursor: grab; }
    canvas.grabbing { cursor: grabbing; }
    canvas.hot { cursor: pointer; }
    .vignette {
      position: fixed; inset: 0; pointer-events: none; z-index: 1;
      background:
        radial-gradient(1100px 640px at 50% 42%, transparent 38%, rgba(0,0,0,0.5) 100%),
        linear-gradient(180deg, rgba(9,11,16,0.28), transparent 16%, transparent 84%, rgba(9,11,16,0.4));
    }
    .bar, .rail, .card, .hint, .tools {
      position: fixed; z-index: 3;
      background: var(--panel);
      border: 1px solid var(--stroke);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
    }
    .bar {
      top: 16px; left: 16px; right: 16px;
      display: flex; align-items: center; gap: 22px;
      min-height: 64px; padding: 10px 14px 10px 16px;
      border-radius: 16px;
    }
    .brand { min-width: 220px; }
    .kicker {
      margin: 0 0 3px;
      color: var(--gold);
      font-size: 10px; font-weight: 600;
      letter-spacing: 0.16em; text-transform: uppercase;
    }
    h1 { margin: 0; font-size: 18px; font-weight: 600; letter-spacing: -0.02em; }
    .legend { display: flex; flex-wrap: wrap; gap: 8px; flex: 1; }
    .swatch {
      display: inline-flex; align-items: center; gap: 7px;
      padding: 5px 10px; border-radius: 999px;
      border: 1px solid var(--stroke); color: var(--muted); font-size: 12px;
    }
    .swatch i { width: 8px; height: 8px; border-radius: 50%; display: block; }
    .search {
      display: flex; align-items: center; gap: 8px;
      min-width: 240px; padding: 8px 12px; border-radius: 12px;
      border: 1px solid var(--stroke); background: rgba(255,255,255,0.03);
    }
    .search input {
      flex: 1; border: 0; outline: 0; background: transparent;
      color: var(--ink); font: inherit; font-size: 13px;
    }
    .search input::placeholder { color: var(--dim); }
    .count { color: var(--dim); font-size: 12px; font-variant-numeric: tabular-nums; white-space: nowrap; }
    .rail {
      top: 96px; left: 16px; width: 176px;
      padding: 12px; border-radius: 16px;
    }
    .rail button, .tools button {
      appearance: none; border: 0; background: transparent;
      color: var(--muted); font: inherit; text-align: left; cursor: pointer;
    }
    .rail button {
      display: flex; justify-content: space-between; align-items: center;
      width: 100%; padding: 7px 8px; border-radius: 10px; font-size: 13px;
    }
    .rail button:hover, .rail button.active { background: rgba(255,255,255,0.05); color: var(--ink); }
    .rail button span { color: var(--dim); font-size: 11px; font-variant-numeric: tabular-nums; }
    .card {
      top: 96px; right: 16px; width: 320px;
      padding: 16px 16px 14px; border-radius: 16px;
      min-height: 168px;
    }
    .card h2 { margin: 0 0 6px; font-size: 20px; letter-spacing: -0.03em; line-height: 1.2; }
    .path {
      margin: 0 0 14px; color: var(--gold);
      font-family: var(--mono); font-size: 11px; word-break: break-all;
    }
    .meta { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 14px; }
    .meta div { padding: 8px 10px; border-radius: 10px; background: rgba(255,255,255,0.03); }
    .meta dt { color: var(--dim); font-size: 10px; letter-spacing: 0.12em; text-transform: uppercase; }
    .meta dd { margin: 3px 0 0; font-size: 13px; }
    .empty { margin: 10px 0 0; color: var(--muted); font-size: 13px; line-height: 1.45; }
    .links { list-style: none; margin: 0; padding: 0; }
    .links li { margin: 0; }
    .links button {
      appearance: none; border: 0; background: transparent;
      color: var(--ink); font: inherit; font-size: 13px;
      padding: 5px 0; cursor: pointer; text-align: left; width: 100%;
    }
    .links button:hover { color: var(--gold); }
    .tools {
      bottom: 16px; right: 16px; display: flex; gap: 4px;
      padding: 6px; border-radius: 14px;
    }
    .tools button {
      width: 36px; height: 36px; border-radius: 10px;
      text-align: center; font-size: 16px; color: var(--ink);
    }
    .tools button:hover { background: rgba(255,255,255,0.06); }
    .hint {
      bottom: 16px; left: 50%; transform: translateX(-50%);
      padding: 8px 14px; border-radius: 999px;
      color: var(--muted); font-size: 12px; white-space: nowrap;
    }
    @media (max-width: 980px) {
      .legend, .rail, .hint { display: none; }
      .bar { right: 16px; }
      .card { width: calc(100% - 32px); top: auto; bottom: 72px; }
    }
  </style>
</head>
<body>
  <canvas id="g"></canvas>
  <div class="vignette"></div>
  <header class="bar">
    <div class="brand">
      <p class="kicker">Compiled wiki</p>
      <h1>Second brain</h1>
    </div>
    <div class="legend" id="legend"></div>
    <label class="search">
      <input id="q" type="search" placeholder="Find a page" autocomplete="off"/>
      <span class="count" id="count"></span>
    </label>
  </header>
  <nav class="rail" id="islands"></nav>
  <aside class="card" id="card">
    <p class="kicker" id="card-kicker">Page</p>
    <h2 id="card-title">Concept clusters</h2>
    <p class="path" id="card-path">Hover or click a node</p>
    <div class="meta" id="card-meta" hidden>
      <div><dt>Island</dt><dd id="card-island"></dd></div>
      <div><dt>Type</dt><dd id="card-type"></dd></div>
    </div>
    <p class="empty" id="card-empty">Islands follow the five agent-operating-system layers. Color is folder family: gold wiki, teal maps, blue hunt/sources, green people, coral ship.</p>
    <ul class="links" id="card-links"></ul>
  </aside>
  <div class="tools">
    <button type="button" id="zoom-out" title="Zoom out">−</button>
    <button type="button" id="zoom-in" title="Zoom in">+</button>
    <button type="button" id="fit" title="Fit graph">⤢</button>
  </div>
  <p class="hint">Scroll to zoom · Labels appear on zoom-in · Click a node for title and path</p>
  <script src="vendor/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
  <script>
  const data = __GRAPH_DATA__;
  const canvas = document.getElementById('g');
  const ctx = canvas.getContext('2d');
  const nodes = data.nodes;
  const byId = Object.fromEntries(nodes.map(n => [n.id, n]));
  const adj = new Map();
  for (const e of data.edges) {
    if (!adj.has(e.source)) adj.set(e.source, []);
    if (!adj.has(e.target)) adj.set(e.target, []);
    adj.get(e.source).push(e.target);
    adj.get(e.target).push(e.source);
  }
  const view = { x: 0, y: 0, scale: 1 };
  const motion = { appear: 0, headerAlpha: 1, labelAlpha: 0, hoverAmt: 0 };
  let hover = null;
  let selected = null;
  let query = '';
  let island = '';
  let drag = null;
  let moved = false;
  let lodOpen = false;
  const clusterOrder = ['bridge', 'compile', 'memory', 'verification', 'harness', 'hunt-ship', 'nav'];
  function hasGsap() { return typeof gsap !== 'undefined'; }
  function tween(target, vars) {
    if (hasGsap()) return gsap.to(target, vars);
    const skip = { duration: 1, ease: 1, onUpdate: 1, onComplete: 1, overwrite: 1 };
    for (const [key, val] of Object.entries(vars)) {
      if (!skip[key]) target[key] = val;
    }
    if (vars.onUpdate) vars.onUpdate();
    if (vars.onComplete) vars.onComplete();
    return null;
  }

  const legend = document.getElementById('legend');
  for (const item of data.legend) {
    const el = document.createElement('span');
    el.className = 'swatch';
    el.innerHTML = '<i style="background:' + item.color + '"></i>' + item.label;
    legend.appendChild(el);
  }
  const islands = document.getElementById('islands');
  const islandCounts = {};
  for (const n of nodes) islandCounts[n.cluster] = (islandCounts[n.cluster] || 0) + 1;
  for (const [id, label] of Object.entries(data.labels)) {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.dataset.island = id;
    btn.innerHTML = label + '<span>' + (islandCounts[id] || 0) + '</span>';
    btn.addEventListener('click', () => {
      island = island === id ? '' : id;
      for (const b of islands.querySelectorAll('button')) {
        b.classList.toggle('active', b.dataset.island === island);
      }
      animateCamera(fitTarget(island ? nodes.filter(n => n.cluster === island) : nodes), 0.7);
    });
    islands.appendChild(btn);
  }
  document.getElementById('count').textContent = nodes.length + ' pages';

  function cx() { return window.innerWidth / 2; }
  function cy() { return window.innerHeight / 2 + 18; }
  function toScreen(x, y) {
    return { x: cx() + view.x + x * view.scale, y: cy() + view.y + y * view.scale };
  }
  function radius(n) {
    if (n.id === 'agent-operating-system') return 10;
    if (n.id === 'Home') return 8;
    if (n.type === 'concept' || n.type === 'meta') return 6.4;
    return 5.4;
  }
  function matches(n) {
    if (!query) return true;
    const hay = (n.title + ' ' + n.id + ' ' + n.path).toLowerCase();
    return hay.includes(query);
  }
  function related(n) {
    if (!n) return new Set();
    return new Set([n.id, ...(adj.get(n.id) || [])]);
  }
  function fitTarget(set) {
    const items = set && set.length ? set : nodes;
    let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
    for (const n of items) {
      minX = Math.min(minX, n.x); minY = Math.min(minY, n.y);
      maxX = Math.max(maxX, n.x); maxY = Math.max(maxY, n.y);
    }
    const pad = 120;
    const w = Math.max(maxX - minX, 80) + pad * 2;
    const h = Math.max(maxY - minY, 80) + pad * 2;
    const cap = items.length <= 18 ? 1.28 : 0.88;
    const scale = Math.min((window.innerWidth - 360) / w, (window.innerHeight - 180) / h, cap);
    const midX = (minX + maxX) / 2;
    const midY = (minY + maxY) / 2;
    return { scale, x: -midX * scale, y: -midY * scale };
  }
  function applyView(next) {
    view.scale = next.scale;
    view.x = next.x;
    view.y = next.y;
  }
  function syncLod() {
    const open = view.scale >= 1.08 || !!query;
    if (open === lodOpen) return;
    lodOpen = open;
    tween(motion, {
      headerAlpha: open ? 0 : 1,
      labelAlpha: open ? 1 : 0,
      duration: 0.38,
      ease: 'power2.out',
      overwrite: 'auto',
      onUpdate: draw
    });
  }
  function animateCamera(next, duration) {
    if (hasGsap()) {
      gsap.killTweensOf(view);
      gsap.to(view, {
        scale: next.scale,
        x: next.x,
        y: next.y,
        duration: duration,
        ease: 'power3.out',
        overwrite: 'auto',
        onUpdate: function() { syncLod(); draw(); }
      });
      return;
    }
    applyView(next);
    syncLod();
    draw();
  }
  function show(n) {
    document.getElementById('card-kicker').textContent = n ? 'Selected page' : 'Page';
    document.getElementById('card-title').textContent = n ? n.title : 'Concept clusters';
    document.getElementById('card-path').textContent = n ? n.path : 'Hover or click a node';
    document.getElementById('card-meta').hidden = !n;
    document.getElementById('card-empty').hidden = !!n;
    document.getElementById('card-island').textContent = n ? (data.labels[n.cluster] || n.cluster) : '';
    document.getElementById('card-type').textContent = n ? (data.types[n.type] || n.type) : '';
    const list = document.getElementById('card-links');
    list.innerHTML = '';
    if (!n) return;
    for (const id of (adj.get(n.id) || [])) {
      const other = byId[id];
      if (!other) continue;
      const li = document.createElement('li');
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.textContent = other.title;
      btn.addEventListener('click', () => { selected = other; show(other); draw(); });
      li.appendChild(btn);
      list.appendChild(li);
    }
  }
  function hit(mx, my) {
    let best = null, bestD = 18;
    for (const n of nodes) {
      const p = toScreen(n.x, n.y);
      const d = Math.hypot(p.x - mx, p.y - my);
      const r = Math.max(radius(n) * view.scale, 9) + 8;
      if (d <= r && d < bestD) { best = n; bestD = d; }
    }
    return best;
  }
  function drawGrid() {
    const step = 48 * view.scale;
    if (step < 18) return;
    const ox = (cx() + view.x) % step;
    const oy = (cy() + view.y) % step;
    ctx.strokeStyle = 'rgba(255,255,255,0.028)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    for (let x = ox; x < window.innerWidth; x += step) {
      ctx.moveTo(x, 0); ctx.lineTo(x, window.innerHeight);
    }
    for (let y = oy; y < window.innerHeight; y += step) {
      ctx.moveTo(0, y); ctx.lineTo(window.innerWidth, y);
    }
    ctx.stroke();
  }
  function overlap(a, b) {
    const p = 6;
    return !(a.x + a.w + p < b.x || b.x + b.w + p < a.x || a.y + a.h + p < b.y || b.y + b.h + p < a.y);
  }
  function labelsOpen() {
    return motion.labelAlpha > 0.08 || view.scale >= 1.08 || !!query;
  }
  function appearFor(cluster) {
    const i = Math.max(clusterOrder.indexOf(cluster), 0);
    const start = i * 0.07;
    const t = (motion.appear - start) / 0.42;
    return Math.max(0, Math.min(1, t));
  }
  function nodePos(n) {
    const spec = data.centers[n.cluster];
    const t = appearFor(n.cluster);
    if (!spec || t >= 1) return { x: n.x, y: n.y, t: t };
    return {
      x: spec[0] + (n.x - spec[0]) * t,
      y: spec[1] + (n.y - spec[1]) * t,
      t: t
    };
  }
  function draw() {
    ctx.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);
    ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);
    drawGrid();
    const focus = selected || hover;
    const keep = related(focus);
    const font = getComputedStyle(document.body).fontFamily;
    const placed = [];
    for (const [cluster, spec] of Object.entries(data.centers)) {
      const p = toScreen(spec[0], spec[1]);
      const r = spec[2] * view.scale;
      const faded = island && island !== cluster;
      const glow = ctx.createRadialGradient(p.x, p.y, r * 0.12, p.x, p.y, r);
      glow.addColorStop(0, faded ? 'rgba(198,163,90,0.02)' : 'rgba(198,163,90,0.07)');
      glow.addColorStop(1, 'rgba(9,11,16,0)');
      ctx.fillStyle = glow;
      ctx.beginPath();
      ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
      ctx.fill();
    }
    if (motion.headerAlpha > 0.02) {
      ctx.font = '600 12px ' + font;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.globalAlpha = motion.headerAlpha * motion.appear;
      for (const [cluster, pos] of Object.entries(data.headers)) {
        const p = toScreen(pos[0], pos[1]);
        const faded = island && island !== cluster;
        const title = data.labels[cluster].toUpperCase();
        const tw = ctx.measureText(title).width;
        placed.push({ x: p.x - tw / 2 - 6, y: p.y - 9, w: tw + 12, h: 18 });
        ctx.fillStyle = faded ? '#4a453c' : '#d2c9b4';
        ctx.fillText(title, p.x, p.y);
      }
      ctx.globalAlpha = 1;
    }
    const zoomed = view.scale >= 1.08;
    for (const e of data.edges) {
      const a = byId[e.source], b = byId[e.target];
      const bridge = e.source === 'agent-operating-system' || e.target === 'agent-operating-system';
      const relatedEdge = !!(focus && keep.has(a.id) && keep.has(b.id));
      if (!zoomed && !e.intra && !bridge && !relatedEdge) continue;
      const pa = nodePos(a);
      const pb = nodePos(b);
      const p = toScreen(pa.x, pa.y);
      const q = toScreen(pb.x, pb.y);
      const c = toScreen(e.cx, e.cy);
      const hot = focus && keep.has(a.id) && keep.has(b.id);
      const dim = (focus && !hot) || (query && !(matches(a) || matches(b))) || (island && a.cluster !== island && b.cluster !== island);
      ctx.strokeStyle = hot ? 'rgba(198,163,90,0.98)' : e.intra ? '#ddd4bf' : '#b4aa97';
      ctx.lineWidth = hot ? 2.4 : e.intra ? 2.05 : 1.55;
      ctx.globalAlpha = (dim ? 0.16 : 0.94) * Math.min(pa.t, pb.t);
      ctx.beginPath();
      ctx.moveTo(p.x, p.y);
      ctx.quadraticCurveTo(c.x, c.y, q.x, q.y);
      ctx.stroke();
      ctx.globalAlpha = 1;
    }
    for (const n of nodes) {
      const np = nodePos(n);
      const p = toScreen(np.x, np.y);
      const r = radius(n) * Math.max(view.scale, 0.8) * (0.35 + 0.65 * np.t);
      const color = data.colors[n.type] || '#8b8478';
      const on = !focus || keep.has(n.id);
      const shown = matches(n) && (!island || n.cluster === island);
      const hotNode = n === selected || n === hover;
      ctx.globalAlpha = (shown ? (on ? 1 : 0.2) : 0.08) * np.t;
      if (hotNode) {
        ctx.beginPath();
        ctx.arc(p.x, p.y, r + 6 + 10 * motion.hoverAmt, 0, Math.PI * 2);
        ctx.fillStyle = color + '33';
        ctx.fill();
      }
      ctx.beginPath();
      ctx.arc(p.x, p.y, r * (hotNode ? 1 + 0.18 * motion.hoverAmt : 1), 0, Math.PI * 2);
      ctx.fillStyle = color;
      ctx.fill();
      ctx.lineWidth = 1.2;
      ctx.strokeStyle = 'rgba(9,11,16,0.55)';
      ctx.stroke();
      ctx.globalAlpha = 1;
    }
    const candidates = [];
    for (const n of nodes) {
      const must = n === hover || n === selected || (!!query && matches(n));
      if (!must && motion.labelAlpha < 0.08) continue;
      if (!matches(n) && !must) continue;
      if (island && n.cluster !== island && !must) continue;
      candidates.push({ n, must, deg: (adj.get(n.id) || []).length });
    }
    candidates.sort((a, b) => Number(b.must) - Number(a.must) || b.deg - a.deg);
    let shownLabels = 0;
    const labeled = [];
    for (const item of candidates) {
      const n = item.n;
      if (!item.must && shownLabels >= 12) continue;
      if (!item.must && labeled.some(pt => Math.hypot(pt.x - n.x, pt.y - n.y) * view.scale < 78)) continue;
      const np = nodePos(n);
      const p = toScreen(np.x, np.y);
      const r = radius(n) * Math.max(view.scale, 0.8);
      ctx.font = (n === selected || n === hover ? '600 ' : '') + '12px ' + font;
      ctx.textAlign = 'left';
      ctx.textBaseline = 'middle';
      const label = n.title;
      const tw = ctx.measureText(label).width;
      const slots = [
        [p.x + r + 8, p.y],
        [p.x - tw - r - 8, p.y],
        [p.x - tw / 2, p.y - r - 16],
        [p.x - tw / 2, p.y + r + 16],
        [p.x + r + 8, p.y - 18],
        [p.x + r + 8, p.y + 18]
      ];
      let box = null;
      for (const [lx, ly] of slots) {
        const rect = { x: lx - 5, y: ly - 9, w: tw + 10, h: 18, lx, ly };
        if (!placed.some(prev => overlap(prev, rect))) { box = rect; break; }
      }
      if (!box) continue;
      placed.push(box);
      labeled.push(n);
      shownLabels += 1;
      ctx.globalAlpha = item.must ? 1 : motion.labelAlpha;
      ctx.fillStyle = 'rgba(9,11,16,0.82)';
      ctx.beginPath();
      ctx.roundRect(box.x, box.y, box.w, box.h, 6);
      ctx.fill();
      ctx.fillStyle = n === selected || n === hover ? '#f8f4ea' : '#ddd6c8';
      ctx.fillText(label, box.lx, box.ly);
      ctx.globalAlpha = 1;
    }
  }
  function resize() {
    canvas.width = window.innerWidth * devicePixelRatio;
    canvas.height = window.innerHeight * devicePixelRatio;
    draw();
  }
  function zoomAt(mx, my, factor) {
    const cur = view.scale;
    const nextScale = Math.min(2.8, Math.max(0.35, cur * factor));
    const worldX = (mx - cx() - view.x) / cur;
    const worldY = (my - cy() - view.y) / cur;
    animateCamera({
      scale: nextScale,
      x: mx - cx() - worldX * nextScale,
      y: my - cy() - worldY * nextScale
    }, 0.28);
  }
  window.addEventListener('resize', () => { resize(); });
  canvas.addEventListener('wheel', (ev) => {
    ev.preventDefault();
    zoomAt(ev.clientX, ev.clientY, ev.deltaY < 0 ? 1.08 : 0.92);
  }, { passive: false });
  canvas.addEventListener('pointerdown', (ev) => {
    drag = { x: ev.clientX, y: ev.clientY, vx: view.x, vy: view.y };
    moved = false;
    canvas.classList.add('grabbing');
    canvas.setPointerCapture(ev.pointerId);
  });
  canvas.addEventListener('pointermove', (ev) => {
    if (drag) {
      const dx = ev.clientX - drag.x;
      const dy = ev.clientY - drag.y;
      if (Math.hypot(dx, dy) > 3) moved = true;
      view.x = drag.vx + dx;
      view.y = drag.vy + dy;
      draw();
      return;
    }
    const next = hit(ev.clientX, ev.clientY);
    canvas.classList.toggle('hot', !!next);
    if ((next && next.id) !== (hover && hover.id)) {
      hover = next;
      tween(motion, { hoverAmt: next ? 1 : 0, duration: 0.22, ease: 'power2.out', overwrite: 'auto', onUpdate: draw });
      if (!selected) show(hover);
    }
    draw();
  });
  canvas.addEventListener('pointerup', (ev) => {
    canvas.classList.remove('grabbing');
    drag = null;
    if (moved) return;
    const n = hit(ev.clientX, ev.clientY);
    selected = n && selected && selected.id === n.id ? null : n;
    show(selected || hover);
    draw();
  });
  canvas.addEventListener('pointerleave', () => {
    hover = null;
    tween(motion, { hoverAmt: 0, duration: 0.2, ease: 'power2.out', overwrite: 'auto', onUpdate: draw });
    if (!selected) show(null);
    draw();
  });
  document.getElementById('q').addEventListener('input', (ev) => {
    query = ev.target.value.trim().toLowerCase();
    const hits = nodes.filter(matches);
    document.getElementById('count').textContent = query ? hits.length + ' match' : nodes.length + ' pages';
    if (hits.length === 1) { selected = hits[0]; show(selected); }
    draw();
  });
  document.getElementById('zoom-in').addEventListener('click', () => zoomAt(cx(), cy(), 1.15));
  document.getElementById('zoom-out').addEventListener('click', () => zoomAt(cx(), cy(), 0.87));
  document.getElementById('fit').addEventListener('click', () => {
    animateCamera(fitTarget(island ? nodes.filter(n => n.cluster === island) : nodes), 0.7);
  });
  window.addEventListener('keydown', (ev) => {
    if (ev.key === 'Escape') { selected = null; show(hover); draw(); }
    if (ev.key === '0') animateCamera(fitTarget(nodes), 0.7);
    if (ev.key === '+' || ev.key === '=') zoomAt(cx(), cy(), 1.15);
    if (ev.key === '-' || ev.key === '_') zoomAt(cx(), cy(), 0.87);
  });
  show(null);
  const start = fitTarget(nodes);
  applyView({ scale: start.scale * 0.78, x: start.x, y: start.y });
  lodOpen = false;
  motion.headerAlpha = 1;
  motion.labelAlpha = 0;
  resize();
  tween(motion, { appear: 1, duration: 1.12, ease: 'power3.out', onUpdate: draw });
  animateCamera(start, 1.18);
  </script>
</body>
</html>
"""


def copy_gsap() -> None:
    src = ROOT / "tools" / "vendor" / "gsap.min.js"
    dest = OUT_DIR / "vendor" / "gsap.min.js"
    if not src.exists():
        return
    dest.parent.mkdir(exist_ok=True)
    shutil.copyfile(src, dest)


def main() -> None:
    nodes, edges = collect()
    layout(nodes, edges)
    OUT_DIR.mkdir(exist_ok=True)
    copy_gsap()
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
