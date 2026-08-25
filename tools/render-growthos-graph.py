#!/usr/bin/env python3
"""Render growth/ as a 3D orbit graph. Click a node to read the note."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROWTH = ROOT / "growth"
OUT = ROOT / "output" / "growthos-graph.html"
LINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)

LAYER_COLOR = {
    "core": "#f472b6",
    "rulings": "#fb923c",
    "playbooks": "#fbbf24",
    "niches": "#34d399",
    "creators": "#38bdf8",
    "partners": "#e879f9",
    "offers": "#c084fc",
    "content": "#facc15",
    "trends": "#22d3ee",
    "memories": "#f9a8d4",
    "insights": "#fde68a",
    "strategies": "#a78bfa",
    "competitors": "#818cf8",
    "journal": "#94a3b8",
}

LAYER_SIZE = {
    "core": 18,
    "partners": 10,
    "rulings": 9,
    "playbooks": 9,
    "niches": 8,
    "creators": 8,
    "content": 8,
    "trends": 8,
    "memories": 8,
    "offers": 7,
}


def layer_of(text: str) -> str:
    m = re.search(r"^growth_layer:\s*(\S+)", text, re.M)
    return m.group(1) if m else "journal"


def title_of(text: str, slug: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else slug


def body_of(text: str) -> str:
    m = FM.match(text)
    return text[m.end() :].strip() if m else text.strip()


def collect() -> tuple[list[dict], list[dict]]:
    pages: dict[str, Path] = {p.stem: p for p in sorted(GROWTH.glob("*.md"))}
    nodes = []
    for slug, path in pages.items():
        text = path.read_text(encoding="utf-8")
        layer = layer_of(text)
        nodes.append(
            {
                "id": slug,
                "label": title_of(text, slug),
                "layer": layer,
                "color": LAYER_COLOR.get(layer, "#94a3b8"),
                "val": LAYER_SIZE.get(layer, 6),
                "path": path.relative_to(ROOT).as_posix(),
                "body": body_of(text),
            }
        )
    edges = []
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
            edges.append({"source": slug, "target": target})
    return nodes, edges


def html(nodes: list[dict], edges: list[dict]) -> str:
    data = json.dumps({"nodes": nodes, "links": edges}, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>GROWTHOS / VAULT</title>
  <style>
    html, body {{ margin: 0; height: 100%; background: #050508; color: #e5e7eb; font-family: ui-sans-serif, system-ui, sans-serif; overflow: hidden; }}
    #graph {{ position: absolute; inset: 0; }}
    #hud-tl {{ position: absolute; top: 28px; left: 32px; z-index: 2; letter-spacing: 0.28em; font-size: 13px; font-weight: 600; color: #f9a8d4; }}
    #hud-br {{ position: absolute; bottom: 28px; left: 0; right: 0; text-align: center; z-index: 2; letter-spacing: 0.22em; font-size: 11px; color: #9ca3af; }}
    #labels {{ position: absolute; inset: 0; pointer-events: none; z-index: 1; overflow: hidden; }}
    .nlabel {{ position: absolute; transform: translate(-50%, -120%); font-size: 13px; font-weight: 700; white-space: nowrap; text-shadow: 0 0 8px #050508, 0 0 2px #050508; }}
    #side {{
      position: absolute; top: 0; right: 0; width: 380px; height: 100%;
      background: rgba(8, 8, 14, 0.92); border-left: 1px solid #27272a;
      transform: translateX(100%); transition: transform 0.2s ease;
      z-index: 3; overflow: auto; padding: 24px 22px 40px;
    }}
    #side.open {{ transform: translateX(0); }}
    #side .crumb {{ font-size: 11px; color: #a78bfa; letter-spacing: 0.08em; text-transform: uppercase; }}
    #side h1 {{ font-size: 18px; margin: 8px 0 12px; color: #fdf4ff; }}
    #side .meta {{ font-size: 12px; color: #9ca3af; margin-bottom: 16px; }}
    #side pre {{ white-space: pre-wrap; font-size: 13px; line-height: 1.45; color: #d4d4d8; font-family: ui-sans-serif, system-ui, sans-serif; }}
    #close {{ position: absolute; top: 16px; right: 16px; background: none; border: 0; color: #9ca3af; font-size: 20px; cursor: pointer; }}
  </style>
</head>
<body>
  <div id="hud-tl">GROWTHOS / VAULT / OBSIDIAN VAULT / SECOND BRAIN</div>
  <div id="hud-br">DRAG TO ORBIT · SCROLL TO FLY · CLICK A NODE TO OPEN THE NOTE</div>
  <div id="graph"></div>
  <div id="labels"></div>
  <aside id="side">
    <button id="close" type="button" aria-label="Close">×</button>
    <div class="crumb" id="crumb"></div>
    <h1 id="title"></h1>
    <div class="meta" id="meta"></div>
    <pre id="body"></pre>
  </aside>
  <script src="https://unpkg.com/3d-force-graph@1.73.3/dist/3d-force-graph.min.js"></script>
  <script>
    const DATA = {data};
    const side = document.getElementById('side');
    const labels = document.getElementById('labels');
    function openNote(node) {{
      document.getElementById('crumb').textContent = node.path;
      document.getElementById('title').textContent = node.label;
      document.getElementById('meta').textContent = node.layer + ' · ' + node.id;
      document.getElementById('body').textContent = node.body;
      side.classList.add('open');
    }}
    document.getElementById('close').onclick = () => side.classList.remove('open');
    const Graph = ForceGraph3D()(document.getElementById('graph'))
      .graphData(DATA)
      .backgroundColor('#050508')
      .showNavInfo(false)
      .linkColor(() => 'rgba(244,114,182,0.45)')
      .linkWidth(0.6)
      .linkOpacity(0.5)
      .nodeRelSize(5)
      .nodeVal('val')
      .nodeColor('color')
      .nodeOpacity(1)
      .nodeLabel(n => n.label)
      .onNodeClick(openNote);
    Graph.d3Force('charge').strength(-180);
    Graph.d3Force('link').distance(56);
    Graph.cameraPosition({{ x: 0, y: 80, z: 520 }});
    function paintLabels() {{
      const nodes = Graph.graphData().nodes;
      if (!labels.childElementCount) {{
        nodes.forEach(node => {{
          const el = document.createElement('div');
          el.className = 'nlabel';
          el.textContent = node.label.replace(/^#\\s*/, '');
          el.style.color = node.color;
          el.dataset.id = node.id;
          labels.appendChild(el);
        }});
      }}
      const kids = labels.children;
      for (let i = 0; i < nodes.length; i++) {{
        const node = nodes[i];
        const el = kids[i];
        if (node.x == null) continue;
        const c = Graph.graph2ScreenCoords(node.x, node.y, node.z);
        el.style.left = c.x + 'px';
        el.style.top = c.y + 'px';
      }}
    }}
    Graph.onEngineTick(paintLabels);
    let angle = 0;
    let holding = false;
    let ready = false;
    Graph.onEngineStop(() => {{ ready = true; paintLabels(); }});
    setTimeout(() => {{ ready = true; }}, 2500);
    const dist = 480;
    setInterval(() => {{
      if (holding || !ready) return;
      angle += 0.004;
      Graph.cameraPosition({{
        x: dist * Math.sin(angle),
        z: dist * Math.cos(angle),
        y: 60
      }});
      paintLabels();
    }}, 40);
    window.addEventListener('pointerdown', () => {{ holding = true; }});
    window.addEventListener('pointerup', () => {{ holding = false; }});
    window.GROWTHOS = {{
      open: (id) => {{
        const node = DATA.nodes.find(n => n.id === id);
        if (node) openNote(node);
      }},
      data: DATA
    }};
  </script>
</body>
</html>
"""


def main() -> int:
    nodes, edges = collect()
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(html(nodes, edges), encoding="utf-8")
    print(f"nodes={len(nodes)} links={len(edges)} -> {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
