#!/usr/bin/env python3
"""Hybrid retrieve: FTS5 + wikilink hops + recency + authority + contradiction penalty."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from claim_protocol import ROOT, format_hits, retrieve


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="+", help="question to retrieve against wiki/")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    query = " ".join(args.query).strip()
    if not query:
        print("empty query", file=sys.stderr)
        return 2
    hits = retrieve(query, root=args.root, limit=args.limit)
    if args.json:
        payload = {
            "query": query,
            "pages": [
                {
                    "slug": hit.slug,
                    "path": hit.path,
                    "score": round(hit.score, 4),
                    "via": hit.via,
                    "claims": hit.claims,
                    "title": hit.title,
                }
                for hit in hits
            ],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        sys.stdout.write(format_hits(query, hits))
    return 0 if hits else 1


if __name__ == "__main__":
    sys.exit(main())
