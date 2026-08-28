#!/usr/bin/env python3
"""sb - second-brain CLI."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import claims, eval_suite, ids, index, retrieve, validate
from .paths import ROOT, db_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="sb",
        description="Second-brain memory engine. Markdown is canonical; SQLite is disposable.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_rebuild = sub.add_parser("rebuild-index", help="Rebuild the disposable FTS5 index")
    p_rebuild.add_argument("--write-ids", action="store_true", help="Stamp missing id: frontmatter")

    p_search = sub.add_parser("search", help="Hybrid search over compiled pages")
    p_search.add_argument("query")
    p_search.add_argument("-k", type=int, default=8)

    p_ask = sub.add_parser("ask", help="Return an evidence set for a question")
    p_ask.add_argument("query")
    p_ask.add_argument("-k", type=int, default=8)

    p_trace = sub.add_parser("trace", help="Print the evidence chain for an id")
    p_trace.add_argument("id")

    sub.add_parser("contradictions", help="List structured contradictions")
    sub.add_parser("stale", help="List objects past valid_until")
    sub.add_parser("orphans", help="List pages with no inbound wikilink")
    sub.add_parser("validate", help="Run lint, id, claim, and contradiction gates")
    sub.add_parser("eval", help="Run the retrieval/claim eval suite")
    sub.add_parser("graph", help="Print link degree for indexed objects")
    sub.add_parser("memory-review", help="Print MEMORY.md ablation reminder")

    args = parser.parse_args(argv)
    if args.cmd == "rebuild-index":
        return cmd_rebuild(write_ids=args.write_ids)
    if args.cmd == "search":
        return cmd_search(args.query, args.k)
    if args.cmd == "ask":
        return cmd_ask(args.query, args.k)
    if args.cmd == "trace":
        return cmd_trace(args.id)
    if args.cmd == "contradictions":
        _ensure_index()
        sys.stdout.write(claims.contradictions_report())
        return 0
    if args.cmd == "stale":
        _ensure_index()
        sys.stdout.write(claims.stale_report())
        return 0
    if args.cmd == "orphans":
        sys.stdout.write(validate.orphans())
        return 0
    if args.cmd == "validate":
        _ensure_index()
        code, out = validate.validate()
        sys.stdout.write(out)
        return code
    if args.cmd == "eval":
        code, out, _ = eval_suite.run_eval()
        sys.stdout.write(out)
        return code
    if args.cmd == "graph":
        return cmd_graph()
    if args.cmd == "memory-review":
        sys.stdout.write(_memory_review())
        return 0
    parser.error(f"unknown command {args.cmd}")
    return 2


def cmd_rebuild(write_ids: bool = False) -> int:
    if write_ids:
        written = ids.write_missing_ids()
        print(f"wrote {len(written)} ids")
    stats = index.rebuild()
    print(
        "index "
        f"objects={stats['objects']} claims={stats['claims']} "
        f"contradictions={stats['contradictions']} links={stats['links']} "
        f"db={db_path()}"
    )
    return 0


def cmd_search(query: str, k: int) -> int:
    _ensure_index()
    hits = retrieve.search(query, limit=k)
    if not hits:
        print("no hits")
        return 1
    for hit in hits:
        print(f"{hit.score:7.3f}  {hit.id:40}  {hit.path}")
        print(f"         {hit.title}")
        if hit.snippet:
            print(f"         {hit.snippet}")
    return 0


def cmd_ask(query: str, k: int) -> int:
    _ensure_index()
    sys.stdout.write(retrieve.evidence_set(query, limit=k))
    return 0


def cmd_trace(object_id: str) -> int:
    _ensure_index()
    out = claims.trace(object_id)
    sys.stdout.write(out)
    return 1 if out.startswith("unknown id:") else 0


def cmd_graph() -> int:
    _ensure_index()
    conn = index.connect()
    try:
        rows = conn.execute(
            """
            SELECT objects.id, objects.type, objects.path,
                   COUNT(links.dst_id) AS degree
            FROM objects
            LEFT JOIN links ON links.src_id = objects.id
            GROUP BY objects.id
            ORDER BY degree DESC, objects.id
            LIMIT 40
            """
        ).fetchall()
        print("id                                      type           degree  path")
        for row in rows:
            print(
                f"{row['id']:40}  {row['type']:12}  {row['degree']:6}  {row['path']}"
            )
    finally:
        conn.close()
    return 0


def _ensure_index() -> None:
    if not db_path().exists():
        index.rebuild()


def _memory_review() -> str:
    path = ROOT / "MEMORY.md"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    bullets = [ln for ln in text.splitlines() if ln.startswith("- ")]
    return (
        "A memory line stays only if deleting it would change an answer.\n"
        f"MEMORY.md bullets: {len(bullets)}\n"
        "Re-read MEMORY.md. Drop adjectives. Keep constraints, decisions, rejections.\n"
    )


if __name__ == "__main__":
    raise SystemExit(main())
