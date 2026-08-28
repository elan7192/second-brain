"""Claims, contradictions, and evidence chains."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from .index import connect
from .paths import db_path


def trace(claim_id: str, db: Path | None = None) -> str:
    conn = connect(db)
    try:
        return format_trace(conn, claim_id)
    finally:
        conn.close()


def format_trace(conn: sqlite3.Connection, claim_id: str) -> str:
    row = conn.execute("SELECT * FROM claims WHERE id = ?", (claim_id,)).fetchone()
    if not row:
        obj = conn.execute("SELECT * FROM objects WHERE id = ?", (claim_id,)).fetchone()
        if not obj:
            return f"unknown id: {claim_id}\n"
        return (
            f"{obj['id']}\n"
            f"type: {obj['type']}\n"
            f"title: {obj['title']}\n"
            f"path: {obj['path']}\n"
            f"status: {obj['status']}\n"
        )
    sources = conn.execute(
        "SELECT source_id FROM claim_sources WHERE claim_id = ?", (claim_id,)
    ).fetchall()
    concepts = conn.execute(
        "SELECT concept_id FROM claim_concepts WHERE claim_id = ?", (claim_id,)
    ).fetchall()
    cons = conn.execute(
        """
        SELECT * FROM contradictions
        WHERE claim_a = ? OR claim_b = ?
        """,
        (claim_id, claim_id),
    ).fetchall()
    lines = [
        claim_id,
        f"subject: {row['subject']}",
        f"predicate: {row['predicate']}",
        f"object: {row['object']}",
        f"confidence: {row['confidence']}",
        f"status: {row['status']}",
        f"valid_from: {row['valid_from'] or ''}",
        f"valid_until: {row['valid_until'] or ''}",
        f"observed_at: {row['observed_at'] or ''}",
        f"superseded_by: {row['superseded_by'] or ''}",
        "sources:",
    ]
    for src in sources:
        path = _path_for(conn, src["source_id"])
        lines.append(f"  - {src['source_id']}  {path}")
    lines.append("concepts:")
    for concept in concepts:
        path = _path_for(conn, concept["concept_id"])
        lines.append(f"  - {concept['concept_id']}  {path}")
    lines.append("contradictions:")
    if not cons:
        lines.append("  none")
    for item in cons:
        lines.append(
            f"  - {item['id']} [{item['status']}] "
            f"{item['claim_a']} <-> {item['claim_b']} - {item['reason']}"
        )
    return "\n".join(lines) + "\n"


def contradictions_report(db: Path | None = None) -> str:
    conn = connect(db)
    try:
        rows = conn.execute(
            """
            SELECT * FROM contradictions
            ORDER BY CASE lower(severity)
              WHEN 'high' THEN 0
              WHEN 'medium' THEN 1
              ELSE 2
            END, id
            """
        ).fetchall()
        open_rows = [r for r in rows if (r["status"] or "").lower() in {"unresolved", "open"}]
        lines = [f"{len(open_rows)} unresolved contradictions", ""]
        for severity in ("HIGH", "MEDIUM", "LOW"):
            bucket = [
                r
                for r in open_rows
                if (r["severity"] or "medium").upper() == severity
            ]
            if not bucket:
                continue
            lines.append(severity)
            for row in bucket:
                page = row["page"] or ""
                lines.append(f"  {page}")
                lines.append(f"  {row['id']}")
                lines.append(f"  {row['claim_a']} <-> {row['claim_b']}")
                if row["reason"]:
                    lines.append(f"  {row['reason']}")
                lines.append("")
        others = [r for r in rows if r not in open_rows]
        if others:
            lines.append("resolved / unverified")
            for row in others:
                lines.append(f"  {row['id']} [{row['status']}] {row['reason']}")
        return "\n".join(lines).rstrip() + "\n"
    finally:
        conn.close()


def stale_report(db: Path | None = None, today: str | None = None) -> str:
    from datetime import date as date_cls

    conn = connect(db)
    try:
        cutoff = today or date_cls.today().isoformat()
        rows = conn.execute(
            """
            SELECT id, type, title, path, valid_until, updated, status
            FROM objects
            WHERE (valid_until IS NOT NULL AND valid_until != '' AND valid_until < ?)
               OR (type = 'claim' AND status IN ('stale', 'superseded'))
            ORDER BY valid_until, id
            """,
            (cutoff,),
        ).fetchall()
        lines = [f"{len(rows)} potentially stale objects (valid_until < {cutoff})", ""]
        for row in rows:
            lines.append(
                f"- {row['id']}  {row['path']}  until={row['valid_until'] or row['status']}"
            )
        if not rows:
            lines.append("none")
        return "\n".join(lines).rstrip() + "\n"
    finally:
        conn.close()


def _path_for(conn: sqlite3.Connection, object_id: str) -> str:
    row = conn.execute("SELECT path FROM objects WHERE id = ?", (object_id,)).fetchone()
    return row["path"] if row else ""
