#!/usr/bin/env python3
"""Query the local Palantir-style ontology. Rebuild first if the snapshot is missing."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ontology_lib import (  # noqa: E402
    get_object,
    links_for,
    list_objects,
    load_bundle,
    search_objects,
    subgraph,
    verify,
)


def dump(payload: object) -> None:
    print(json.dumps(payload, indent=2, ensure_ascii=True))


def main() -> int:
    parser = argparse.ArgumentParser(description="Query compiled ontology objects and links.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("counts", help="Object and link counts")

    list_p = sub.add_parser("list", help="List objects")
    list_p.add_argument("--type", dest="object_type", default=None)

    get_p = sub.add_parser("get", help="Get one object by primary key")
    get_p.add_argument("key")

    search_p = sub.add_parser("search", help="Substring search")
    search_p.add_argument("query")

    links_p = sub.add_parser("links", help="Inbound and outbound links")
    links_p.add_argument("key")

    sub_p = sub.add_parser("subgraph", help="N-hop subgraph for a seed object")
    sub_p.add_argument("key")
    sub_p.add_argument("--hops", type=int, default=1)

    sub.add_parser(
        "verify",
        help="Load the bundle into SQLite, check integrity, compare with the FTS index. Exit 1 on any error.",
    )

    args = parser.parse_args()
    try:
        bundle = load_bundle(ROOT)
    except FileNotFoundError as err:
        print(err, file=sys.stderr)
        return 1

    if args.cmd == "counts":
        dump(bundle["counts"])
        return 0
    if args.cmd == "list":
        rows = list_objects(bundle, args.object_type)
        dump(
            [
                {
                    "primaryKey": obj["primaryKey"],
                    "objectType": obj["objectType"],
                    "title": obj["title"],
                    "oneLiner": obj["oneLiner"],
                    "unverified": obj["unverified"],
                }
                for obj in rows
            ]
        )
        return 0
    if args.cmd == "get":
        obj = get_object(bundle, args.key)
        if obj is None:
            print(f"missing {args.key}", file=sys.stderr)
            return 1
        dump(obj)
        return 0
    if args.cmd == "search":
        dump(
            [
                {
                    "primaryKey": obj["primaryKey"],
                    "objectType": obj["objectType"],
                    "title": obj["title"],
                    "oneLiner": obj["oneLiner"],
                }
                for obj in search_objects(bundle, args.query)
            ]
        )
        return 0
    if args.cmd == "links":
        dump(links_for(bundle, args.key))
        return 0
    if args.cmd == "subgraph":
        dump(subgraph(bundle, args.key, args.hops))
        return 0
    if args.cmd == "verify":
        errors, counts = verify(bundle)
        dump({"counts": counts, "errors": errors, "status": "FAIL" if errors else "PASS"})
        return 1 if errors else 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
