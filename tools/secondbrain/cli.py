#!/usr/bin/env python3
"""sb - second-brain CLI."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .paths import ROOT, db_path

# Subcommand modules import lazily inside their branch. `ask` should not pay
# for the eval suite, the contract checker, or the lint bridge.


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
    sub.add_parser("health", help="Print knowledge integrity counts")
    p_ingest = sub.add_parser("ingest-check", help="Check a source slug against ingest gates")
    p_ingest.add_argument("slug")
    p_contract = sub.add_parser("contract-check", help="Validate a machine-readable task contract")
    p_contract.add_argument("path", nargs="?", default="")
    p_contract.add_argument(
        "--results",
        default="",
        help="YAML map of acceptance_check -> bool. Distinguishes TASK_PASSED vs TASK_FAILED.",
    )
    sub.add_parser("eval", help="Run the retrieval/claim eval suite")

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
        from . import claims

        _ensure_index()
        sys.stdout.write(claims.contradictions_report())
        return 0
    if args.cmd == "stale":
        from . import claims

        _ensure_index()
        sys.stdout.write(claims.stale_report())
        return 0
    if args.cmd == "orphans":
        from . import validate

        sys.stdout.write(validate.orphans())
        return 0
    if args.cmd == "validate":
        from . import validate

        _ensure_index()
        code, out = validate.validate()
        sys.stdout.write(out)
        return code
    if args.cmd == "health":
        from . import health

        _ensure_index()
        code, out = health.report()
        sys.stdout.write(out)
        return code
    if args.cmd == "ingest-check":
        from . import ingest_check

        code, out = ingest_check.check(args.slug)
        sys.stdout.write(out)
        return code
    if args.cmd == "contract-check":
        return cmd_contract(args.path, args.results)
    if args.cmd == "eval":
        from . import eval_suite

        code, out, _ = eval_suite.run_eval()
        sys.stdout.write(out)
        return code
    parser.error(f"unknown command {args.cmd}")
    return 2


def cmd_rebuild(write_ids: bool = False) -> int:
    from . import ids, index

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
    from . import retrieve

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
    from . import retrieve

    _ensure_index()
    sys.stdout.write(retrieve.evidence_set(query, limit=k))
    return 0


def cmd_trace(object_id: str) -> int:
    from . import claims

    _ensure_index()
    out = claims.trace(object_id)
    sys.stdout.write(out)
    return 1 if out.startswith("unknown id:") else 0


def cmd_contract(path: str, results_path: str = "") -> int:
    from . import contract

    results = _load_results(results_path) if results_path else None
    if path:
        status, errors = contract.evaluate_path(Path(path), results)
        sys.stdout.write(status + "\n")
        if errors:
            sys.stdout.write("\n".join(f"  {item}" for item in errors) + "\n")
        return 0 if status in {contract.SCHEMA_VALID, contract.TASK_PASSED} else 1
    for folder in (ROOT / "eval" / "contracts", ROOT / "agents"):
        if folder.is_dir():
            code, out = contract.check_dir(folder)
            sys.stdout.write(out)
            return code
    sys.stdout.write("0 contracts\n")
    return 0


def _load_results(path: str) -> dict[str, bool]:
    from .yamlutil import loads

    data = loads(Path(path).read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        return {}
    return {str(key): bool(value) for key, value in data.items()}


def _ensure_index() -> None:
    from . import index

    index.ensure()


if __name__ == "__main__":
    raise SystemExit(main())
