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
SKIP_DIRS = {".git", ".obsidian", "templates", "raw", "node_modules"}
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
    "compile": (-120.0, 8.0),
    "verification": (110.0, -48.0),
    "memory": (-8.0, 88.0),
    "harness": (108.0, 48.0),
    "hunt-ship": (28.0, 138.0),
    "nav": (-10.0, -108.0),
    "bridge": (-6.0, 20.0),
}
CLUSTER_Z = {
    "compile": 18.0,
    "verification": -20.0,
    "memory": 26.0,
    "harness": -10.0,
    "hunt-ship": 8.0,
    "nav": -22.0,
    "bridge": 6.0,
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
    assign_depth(nodes)


def stable_jitter(slug: str) -> float:
    total = sum((i + 1) * ord(ch) for i, ch in enumerate(slug))
    return float((total % 21) - 10)


def assign_depth(nodes: dict[str, dict]) -> None:
    for node in nodes.values():
        node["z"] = CLUSTER_Z.get(node["cluster"], 0.0) + stable_jitter(node["id"])


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
        "heights": {
            cluster: sum(n["z"] for n in nodes.values() if n["cluster"] == cluster)
            / max(sum(1 for n in nodes.values() if n["cluster"] == cluster), 1)
            for cluster in CLUSTER_LABELS
        },
    }
    template = (ROOT / "tools" / "graph-page.html").read_text(encoding="utf-8")
    dest.write_text(
        template.replace("__GRAPH_DATA__", json.dumps(payload).replace("<", "\\u003c")),
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


def copy_vendors() -> None:
    dest_dir = OUT_DIR / "vendor"
    dest_dir.mkdir(exist_ok=True)
    files = [
        ROOT / "tools" / "vendor" / "gsap.min.js",
        ROOT / "tools" / "vendor" / "three.module.min.js",
        ROOT / "tools" / "vendor" / "OrbitControls.js",
    ]
    nm = ROOT / "node_modules" / "three"
    if (nm / "build" / "three.module.min.js").exists():
        shutil.copyfile(nm / "build" / "three.module.min.js", ROOT / "tools" / "vendor" / "three.module.min.js")
        shutil.copyfile(
            nm / "examples" / "jsm" / "controls" / "OrbitControls.js",
            ROOT / "tools" / "vendor" / "OrbitControls.js",
        )
    for src in files:
        if src.exists():
            shutil.copyfile(src, dest_dir / src.name)


def main() -> None:
    nodes, edges = collect()
    layout(nodes, edges)
    OUT_DIR.mkdir(exist_ok=True)
    copy_vendors()
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
