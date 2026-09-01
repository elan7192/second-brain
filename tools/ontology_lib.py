#!/usr/bin/env python3
"""Compile wiki markdown into a Palantir-style ontology. Wiki stays the store."""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from secondbrain import frontmatter  # noqa: E402
from secondbrain.frontmatter import WIKILINK as LINK  # noqa: E402
from secondbrain.paths import rel_posix  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = Path(__file__).resolve().parent / "ontology_schema.json"
CSV_PATH = ROOT / "output" / "ontology-objects.csv"
JSON_PATH = ROOT / "output" / "ontology.json"

HEADING = re.compile(r"^#\s+(.+)$", re.M)
DECISION = re.compile(r"^## (D\d+)\.\s+(.+)$", re.M)
CONTRADICTION = re.compile(r"^## (C\d+)\.\s+(.+)$", re.M)
UNVERIFIED = re.compile(r"\bunverified\b", re.I)
INDEX_ROW = re.compile(r"^\|\s*\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]\s*\|\s*(.+?)\s*\|")

SKIP_DIRS = {".git", ".obsidian", "templates", "raw", "growth", ".agents", ".cursor", "eval"}
SKIP_FILES = {"AGENTS.md", "CLAUDE.md", "README.md"}

TYPE_MAP = {
    "concept": "Concept",
    "source": "Source",
    "person": "Person",
    "project": "Project",
    "meta": "Meta",
    "home": "Meta",
    "map": "Map",
    "hunt": "Hunt",
    "ship": "Ship",
    "note": "Note",
}

CSV_FIELDS = [
    "primaryKey",
    "objectType",
    "title",
    "path",
    "created",
    "updated",
    "tags",
    "island",
    "inbound",
    "outbound",
    "unverified",
    "oneLiner",
]


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Flat string view of the shared parser. Only tags keep list items, comma-joined."""
    parsed, body = frontmatter.split(text)
    meta: dict[str, str] = {}
    for key, value in parsed.items():
        if isinstance(value, list):
            if key == "tags" and value:
                meta[key] = ",".join(str(item) for item in value)
            elif key != "tags":
                meta[key] = ""
        else:
            meta[key] = str(value)
    return meta, body


def first_heading(body: str, fallback: str) -> str:
    match = HEADING.search(body)
    return match.group(1).strip() if match else fallback


def one_liner_from_body(body: str) -> str:
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("[["):
            continue
        if stripped.startswith("|") or stripped.startswith("- "):
            continue
        return re.sub(r"\s+", " ", stripped)[:200]
    return ""


def parse_index_lines(root: Path) -> dict[str, str]:
    path = root / "wiki" / "index.md"
    if not path.is_file():
        return {}
    found: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = INDEX_ROW.match(line)
        if match:
            found[match.group(1).strip()] = match.group(2).strip()
    return found


def infer_type(path: Path, root: Path, front_type: str) -> str:
    if front_type in TYPE_MAP:
        return TYPE_MAP[front_type]
    rel = rel_posix(path, root)
    if rel.startswith("wiki/sources/"):
        return "Source"
    if rel.startswith("wiki/people/"):
        return "Person"
    if rel.startswith("maps/") or path.name == "maps.md":
        return "Map"
    if rel.startswith("hunt/") or path.name == "hunt.md":
        return "Hunt"
    if rel.startswith("ship/") or rel.startswith("output/") or path.name == "ship.md":
        return "Ship"
    if rel.startswith("wiki/") or path.name in {"MEMORY.md", "decisions.md", "wiki.md", "Home.md"}:
        return "Meta" if path.name in {"MEMORY.md", "decisions.md", "index.md", "log.md", "Home.md"} else "Concept"
    return "Note"


def island_for(object_type: str, rel: str) -> str:
    if rel.startswith("wiki/sources/"):
        return "sources"
    if rel.startswith("wiki/people/"):
        return "people"
    if object_type == "Project":
        return "projects"
    if object_type == "Concept":
        return "concepts"
    if object_type in {"Meta", "Decision", "Contradiction"}:
        return "meta"
    if object_type in {"Hunt", "Ship", "Map"}:
        return "hunt-ship"
    return "nav"


def collect_pages(root: Path) -> dict[str, Path]:
    found: dict[str, Path] = {}
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        found[path.stem] = path
    return found


def section_blocks(text: str, pattern: re.Pattern[str]) -> list[tuple[str, str, str]]:
    matches = list(pattern.finditer(text))
    blocks: list[tuple[str, str, str]] = []
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        blocks.append((match.group(1), match.group(2).strip(), text[start:end]))
    return blocks


def link_type_for(src_type: str, dst_type: str) -> str:
    if dst_type == "Source":
        return "cites"
    if dst_type == "Person":
        return "aboutPerson"
    return "relatedTo"


def compile_ontology(root: Path | None = None) -> dict:
    root = root or ROOT
    schema = load_schema()
    pages = collect_pages(root)
    index_lines = parse_index_lines(root)
    objects: dict[str, dict] = {}
    outgoing: dict[str, list[str]] = defaultdict(list)

    for slug, path in pages.items():
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        object_type = infer_type(path, root, meta.get("type", ""))
        rel = rel_posix(path, root)
        title = first_heading(body, slug)
        targets = [match.group(1).strip() for match in LINK.finditer(body)]
        outgoing[slug] = targets
        objects[slug] = {
            "primaryKey": slug,
            "objectType": object_type,
            "title": title,
            "path": rel,
            "created": meta.get("created", ""),
            "updated": meta.get("updated", ""),
            "tags": meta.get("tags", ""),
            "island": island_for(object_type, rel),
            "inbound": 0,
            "outbound": 0,
            "unverified": bool(UNVERIFIED.search(body)),
            "oneLiner": index_lines.get(slug) or one_liner_from_body(body),
        }

    extra_links: list[tuple[str, str, str]] = []
    decisions_path = root / "decisions.md"
    if decisions_path.is_file() and "decisions" in objects:
        text = decisions_path.read_text(encoding="utf-8")
        for key, title, block in section_blocks(text, DECISION):
            objects[key] = {
                "primaryKey": key,
                "objectType": "Decision",
                "title": title,
                "path": "decisions.md",
                "created": objects["decisions"].get("created", ""),
                "updated": objects["decisions"].get("updated", ""),
                "tags": "decision",
                "island": "meta",
                "inbound": 0,
                "outbound": 0,
                "unverified": bool(UNVERIFIED.search(block)),
                "oneLiner": one_liner_from_body(block) or title,
            }
            extra_links.append((key, "decisions", "extractedFrom"))
            outgoing[key] = [m.group(1).strip() for m in LINK.finditer(block)]

    contradictions_path = root / "wiki" / "contradictions.md"
    if contradictions_path.is_file() and "contradictions" in objects:
        text = contradictions_path.read_text(encoding="utf-8")
        for key, title, block in section_blocks(text, CONTRADICTION):
            objects[key] = {
                "primaryKey": key,
                "objectType": "Contradiction",
                "title": title,
                "path": "wiki/contradictions.md",
                "created": objects["contradictions"].get("created", ""),
                "updated": objects["contradictions"].get("updated", ""),
                "tags": "contradiction",
                "island": "meta",
                "inbound": 0,
                "outbound": 0,
                "unverified": bool(UNVERIFIED.search(block)),
                "oneLiner": one_liner_from_body(block) or title,
            }
            extra_links.append((key, "contradictions", "extractedFrom"))
            outgoing[key] = [m.group(1).strip() for m in LINK.finditer(block)]

    inbound: dict[str, int] = defaultdict(int)
    links: list[dict[str, str]] = []
    seen: set[tuple[str, str, str]] = set()

    def add_link(src: str, dst: str, kind: str) -> None:
        key = (src, kind, dst)
        if key in seen or src not in objects or dst not in objects:
            return
        seen.add(key)
        links.append({"from": src, "linkType": kind, "to": dst})
        inbound[dst] += 1

    for src, targets in outgoing.items():
        src_type = objects.get(src, {}).get("objectType", "")
        for dst in dict.fromkeys(targets):
            dst_type = objects.get(dst, {}).get("objectType", "")
            add_link(src, dst, link_type_for(src_type, dst_type))

    for src, dst, kind in extra_links:
        add_link(src, dst, kind)

    # Both degree properties count emitted links, so sum(outbound) == sum(inbound) == len(links).
    outbound: dict[str, int] = defaultdict(int)
    for link in links:
        outbound[link["from"]] += 1
    for slug, obj in objects.items():
        obj["inbound"] = inbound.get(slug, 0)
        obj["outbound"] = outbound.get(slug, 0)

    links.sort(key=lambda link: (link["from"], link["linkType"], link["to"]))
    counts: dict[str, int] = defaultdict(int)
    for obj in objects.values():
        counts[obj["objectType"]] += 1
        if obj["unverified"]:
            counts["unverified"] += 1
    counts["objects"] = len(objects)
    counts["links"] = len(links)

    built = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "ontology": schema["ontology"],
        "builtAt": built,
        "sourceOfTruth": schema["sourceOfTruth"],
        "hostedAip": False,
        "objectTypes": schema["objectTypes"],
        "linkTypes": schema["linkTypes"],
        "actionTypes": schema["actionTypes"],
        "counts": dict(counts),
        "objects": [objects[k] for k in sorted(objects)],
        "links": links,
    }


def csv_rows(bundle: dict) -> list[dict]:
    rows = []
    for obj in bundle["objects"]:
        row = {field: obj.get(field, "") for field in CSV_FIELDS}
        row["inbound"] = str(int(obj.get("inbound") or 0))
        row["outbound"] = str(int(obj.get("outbound") or 0))
        row["unverified"] = "true" if obj.get("unverified") else "false"
        rows.append(row)
    return rows


def write_ontology(bundle: dict, root: Path | None = None) -> tuple[Path, Path]:
    root = root or ROOT
    out_dir = root / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "ontology-objects.csv"
    json_path = out_dir / "ontology.json"
    if json_path.is_file():
        # Keep the old timestamp when nothing else changed, so a rebuild on an
        # unchanged wiki leaves the committed file byte-identical.
        try:
            previous = json.loads(json_path.read_text(encoding="utf-8"))
        except ValueError:
            previous = None
        if previous and stable_payload(previous) == stable_payload(bundle):
            bundle = dict(bundle, builtAt=previous.get("builtAt", bundle["builtAt"]))
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(csv_rows(bundle))
    json_path.write_text(json.dumps(bundle, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    return csv_path, json_path


def stable_payload(bundle: dict) -> dict:
    return {
        "ontology": bundle.get("ontology"),
        "sourceOfTruth": bundle.get("sourceOfTruth"),
        "hostedAip": bundle.get("hostedAip"),
        "counts": bundle.get("counts"),
        "objects": bundle.get("objects"),
        "links": bundle.get("links"),
    }


def check_ontology(root: Path | None = None) -> list[str]:
    root = root or ROOT
    errors: list[str] = []
    csv_path = root / "output" / "ontology-objects.csv"
    json_path = root / "output" / "ontology.json"
    if not csv_path.is_file():
        errors.append("missing output/ontology-objects.csv")
    if not json_path.is_file():
        errors.append("missing output/ontology.json")
    if errors:
        return errors
    bundle = compile_ontology(root)
    expected_rows = csv_rows(bundle)
    expected_rows.sort(key=lambda row: row["primaryKey"])
    with csv_path.open(encoding="utf-8", newline="") as handle:
        actual_rows = list(csv.DictReader(handle))
    actual_rows.sort(key=lambda row: row.get("primaryKey", ""))
    if json.dumps(actual_rows, sort_keys=True) != json.dumps(expected_rows, sort_keys=True):
        errors.append("ontology CSV stale vs wiki; run python3 tools/rebuild-ontology.py")
    stored = json.loads(json_path.read_text(encoding="utf-8"))
    if stable_payload(stored) != stable_payload(bundle):
        errors.append("ontology JSON stale vs wiki; run python3 tools/rebuild-ontology.py")
    errors.extend(integrity_errors(bundle))
    return errors


def integrity_errors(bundle: dict) -> list[str]:
    """Structural checks the compiler must always satisfy.

    Keys unique, every link endpoint an object, degree properties equal to the
    emitted links, and every link legal under the bundle's own linkTypes.
    """
    errors: list[str] = []
    keys = [obj["primaryKey"] for obj in bundle["objects"]]
    by_key = {obj["primaryKey"]: obj for obj in bundle["objects"]}
    if len(keys) != len(by_key):
        dupes = sorted({k for k in keys if keys.count(k) > 1})
        errors.append(f"ontology duplicate primaryKey: {dupes[:5]}")
    inbound: dict[str, int] = defaultdict(int)
    outbound: dict[str, int] = defaultdict(int)
    link_types = bundle.get("linkTypes", {})
    dangling = 0
    illegal: dict[tuple[str, str, str], int] = defaultdict(int)
    for link in bundle["links"]:
        src, dst, kind = link["from"], link["to"], link["linkType"]
        if src not in by_key or dst not in by_key:
            dangling += 1
            continue
        inbound[dst] += 1
        outbound[src] += 1
        rule = link_types.get(kind)
        if rule is None:
            illegal[(kind, "?", "?")] += 1
            continue
        src_type = by_key[src]["objectType"]
        dst_type = by_key[dst]["objectType"]
        ok_from = "WikiNote" in rule["from"] or src_type in rule["from"]
        ok_to = "WikiNote" in rule["to"] or dst_type in rule["to"]
        if not (ok_from and ok_to):
            illegal[(kind, src_type, dst_type)] += 1
    if dangling:
        errors.append(f"ontology {dangling} links with a missing endpoint")
    bad_degree = [
        k for k, obj in by_key.items()
        if obj.get("inbound") != inbound.get(k, 0) or obj.get("outbound") != outbound.get(k, 0)
    ]
    if bad_degree:
        errors.append(f"ontology inbound/outbound disagree with links on {len(bad_degree)} objects: {bad_degree[:5]}")
    for (kind, src_type, dst_type), n in sorted(illegal.items()):
        errors.append(f"ontology {n} {kind} links {src_type} -> {dst_type} not allowed by linkTypes")
    return errors


def load_bundle(root: Path | None = None) -> dict:
    root = root or ROOT
    path = root / "output" / "ontology.json"
    if not path.is_file():
        raise FileNotFoundError("output/ontology.json missing; run python3 tools/rebuild-ontology.py")
    return json.loads(path.read_text(encoding="utf-8"))


# Single-entry cache: (bundle, by_key, outbound adjacency, inbound adjacency).
# Query helpers keep their (bundle, key) signatures but stop rescanning every
# object and link per call.
_INDEXED: tuple[dict, dict[str, dict], dict[str, list[dict]], dict[str, list[dict]]] | None = None


def _indexed(bundle: dict) -> tuple[dict[str, dict], dict[str, list[dict]], dict[str, list[dict]]]:
    global _INDEXED
    if _INDEXED is not None and _INDEXED[0] is bundle:
        return _INDEXED[1], _INDEXED[2], _INDEXED[3]
    by_key = {obj["primaryKey"]: obj for obj in bundle["objects"]}
    out_adj: dict[str, list[dict]] = defaultdict(list)
    in_adj: dict[str, list[dict]] = defaultdict(list)
    for link in bundle["links"]:
        out_adj[link["from"]].append(link)
        in_adj[link["to"]].append(link)
    _INDEXED = (bundle, by_key, out_adj, in_adj)
    return by_key, out_adj, in_adj


def objects_by_key(bundle: dict) -> dict[str, dict]:
    return _indexed(bundle)[0]


def list_objects(bundle: dict, object_type: str | None = None) -> list[dict]:
    rows = bundle["objects"]
    if object_type:
        rows = [obj for obj in rows if obj["objectType"] == object_type]
    return rows


def get_object(bundle: dict, primary_key: str) -> dict | None:
    return objects_by_key(bundle).get(primary_key)


def search_objects(bundle: dict, query: str) -> list[dict]:
    needle = query.lower()
    hits = []
    for obj in bundle["objects"]:
        hay = " ".join(
            str(obj.get(field, ""))
            for field in ("primaryKey", "title", "oneLiner", "tags", "path")
        ).lower()
        if needle in hay:
            hits.append(obj)
    return hits


def links_for(bundle: dict, primary_key: str) -> dict[str, list[dict]]:
    _, out_adj, in_adj = _indexed(bundle)
    return {"outbound": list(out_adj.get(primary_key, ())), "inbound": list(in_adj.get(primary_key, ()))}


def subgraph(bundle: dict, primary_key: str, hops: int = 1) -> dict:
    _, out_adj, in_adj = _indexed(bundle)
    keys = {primary_key}
    frontier = {primary_key}
    for _ in range(max(hops, 0)):
        nxt: set[str] = set()
        for key in frontier:
            nxt.update(link["to"] for link in out_adj.get(key, ()))
            nxt.update(link["from"] for link in in_adj.get(key, ()))
        nxt -= keys
        keys |= nxt
        frontier = nxt
        if not frontier:
            break
    objs = [obj for obj in bundle["objects"] if obj["primaryKey"] in keys]
    links = [
        link
        for link in bundle["links"]
        if link["from"] in keys and link["to"] in keys
    ]
    return {"seed": primary_key, "hops": hops, "objects": objs, "links": links}


def verify(bundle: dict, db_path: Path | None = None) -> tuple[list[str], dict[str, int]]:
    """Load the bundle into an in-memory SQLite database and prove it with SQL.

    Relational checks: unique keys, referential integrity on both link
    endpoints, degree properties versus actual links. Then the page-to-page
    edges are compared with the disposable FTS index, which derives the same
    graph from the same markdown through separate code (tools/secondbrain).
    Two builders agreeing is the evidence that the ontology works.
    """
    import sqlite3

    errors: list[str] = []
    conn = sqlite3.connect(":memory:")
    conn.executescript(
        """
        CREATE TABLE obj (pk TEXT PRIMARY KEY, type TEXT, path TEXT, inbound INT, outbound INT);
        CREATE TABLE link (src TEXT, kind TEXT, dst TEXT, PRIMARY KEY (src, kind, dst));
        """
    )
    try:
        conn.executemany(
            "INSERT INTO obj VALUES (?, ?, ?, ?, ?)",
            ((o["primaryKey"], o["objectType"], o["path"], o["inbound"], o["outbound"]) for o in bundle["objects"]),
        )
    except sqlite3.IntegrityError as err:
        errors.append(f"duplicate primaryKey: {err}")
    try:
        conn.executemany(
            "INSERT INTO link VALUES (?, ?, ?)",
            ((l["from"], l["linkType"], l["to"]) for l in bundle["links"]),
        )
    except sqlite3.IntegrityError as err:
        errors.append(f"duplicate link: {err}")
    counts = {
        "objects": conn.execute("SELECT COUNT(*) FROM obj").fetchone()[0],
        "links": conn.execute("SELECT COUNT(*) FROM link").fetchone()[0],
        "dangling_src": conn.execute(
            "SELECT COUNT(*) FROM link WHERE src NOT IN (SELECT pk FROM obj)"
        ).fetchone()[0],
        "dangling_dst": conn.execute(
            "SELECT COUNT(*) FROM link WHERE dst NOT IN (SELECT pk FROM obj)"
        ).fetchone()[0],
        "degree_mismatch": conn.execute(
            """
            SELECT COUNT(*) FROM obj
            WHERE inbound != (SELECT COUNT(*) FROM link WHERE dst = obj.pk)
               OR outbound != (SELECT COUNT(*) FROM link WHERE src = obj.pk)
            """
        ).fetchone()[0],
        "isolated": conn.execute(
            """
            SELECT COUNT(*) FROM obj
            WHERE pk NOT IN (SELECT src FROM link) AND pk NOT IN (SELECT dst FROM link)
            """
        ).fetchone()[0],
    }
    for key in ("dangling_src", "dangling_dst", "degree_mismatch"):
        if counts[key]:
            errors.append(f"{key}={counts[key]}")
    errors.extend(integrity_errors(bundle))

    db_path = db_path or ROOT / ".cache" / "secondbrain.sqlite"
    counts["index_compared"] = 0
    if db_path.is_file():
        conn.execute("ATTACH DATABASE ? AS fts", (str(db_path),))
        # The FTS index keys objects by id and stores links by id. Compare on
        # slug, restricted to page objects both builders cover.
        conn.executescript(
            """
            CREATE TEMP TABLE idx_obj AS
              SELECT id, slug, path FROM fts.objects
              WHERE type NOT IN ('claim', 'decision', 'contradiction');
            CREATE TEMP TABLE idx_link AS
              SELECT DISTINCT s.slug AS src, d.slug AS dst
              FROM fts.links l
              JOIN idx_obj s ON s.id = l.src_id
              JOIN idx_obj d ON d.id = l.dst_id;
            CREATE TEMP TABLE onto_link AS
              SELECT DISTINCT l.src, l.dst FROM link l
              JOIN idx_obj s ON s.slug = l.src
              JOIN idx_obj d ON d.slug = l.dst;
            """
        )
        missing_pages = conn.execute(
            "SELECT COUNT(*) FROM idx_obj WHERE slug NOT IN (SELECT pk FROM obj)"
        ).fetchone()[0]
        path_mismatch = conn.execute(
            "SELECT COUNT(*) FROM idx_obj i JOIN obj o ON o.pk = i.slug WHERE o.path != i.path"
        ).fetchone()[0]
        only_index = conn.execute(
            "SELECT COUNT(*) FROM idx_link WHERE (src, dst) NOT IN (SELECT src, dst FROM onto_link)"
        ).fetchone()[0]
        only_onto = conn.execute(
            "SELECT COUNT(*) FROM onto_link WHERE (src, dst) NOT IN (SELECT src, dst FROM idx_link)"
        ).fetchone()[0]
        counts["index_compared"] = conn.execute("SELECT COUNT(*) FROM idx_link").fetchone()[0]
        counts["index_pages_missing"] = missing_pages
        counts["index_path_mismatch"] = path_mismatch
        counts["links_only_in_index"] = only_index
        counts["links_only_in_ontology"] = only_onto
        for key in ("index_pages_missing", "index_path_mismatch", "links_only_in_index", "links_only_in_ontology"):
            if counts[key]:
                errors.append(f"{key}={counts[key]}")
    conn.close()
    return errors, counts
