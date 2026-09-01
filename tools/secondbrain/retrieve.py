"""Hybrid retrieval over the disposable FTS index.

Signals: FTS5, wikilink graph, recency, source/type quality.
Embeddings are out of scope.
"""

from __future__ import annotations

import re
import sqlite3
from datetime import date
from pathlib import Path

from . import schema
from .index import connect

OBJECT_SELECT = "SELECT id, type, title, path, slug, body, updated FROM objects"
DECIDE_TOKENS = {"decide", "decision", "decisions", "decided"}
CONFLICT_TOKENS = {"contradiction", "unresolved", "conflict"}
SKIP_NEIGHBOR_SLUGS = {"index", "log", "Home", "wiki"}
WS = re.compile(r"\s+")

STOP = {
    "a", "an", "the", "and", "or", "of", "to", "in", "on", "for", "is", "are",
    "was", "be", "we", "did", "do", "does", "what", "why", "how", "which",
    "about", "with", "from", "this", "that", "it", "as", "at", "by", "our",
    "should", "can", "could", "would",
}

ALIASES = {
    "posting": "post",
    "paying": "pay",
    "sending": "send",
    "deploying": "deploy",
    "decided": "decide",
    "decision": "decide",
    "decisions": "decide",
    "cloning": "clone",
    "writing": "write",
}

TOKEN = re.compile(r"[A-Za-z0-9_:-]+")


class Hit:
    """Slotted and mutable: scores are adjusted in place during ranking."""

    __slots__ = ("id", "type", "title", "path", "slug", "snippet", "score", "updated", "reasons")

    def __init__(
        self,
        id: str,
        type: str,
        title: str,
        path: str,
        slug: str,
        snippet: str,
        score: float,
        updated: str,
        reasons: tuple[str, ...],
    ) -> None:
        self.id = id
        self.type = type
        self.title = title
        self.path = path
        self.slug = slug
        self.snippet = snippet
        self.score = score
        self.updated = updated
        self.reasons = reasons

    def __repr__(self) -> str:
        return f"Hit({self.id!r}, score={self.score:.3f}, reasons={self.reasons})"


def search(
    query: str,
    *,
    limit: int = 8,
    db: Path | None = None,
    today: date | None = None,
) -> list[Hit]:
    conn = connect(db)
    try:
        return search_conn(conn, query, limit=limit, today=today)
    finally:
        conn.close()


def search_conn(
    conn: sqlite3.Connection,
    query: str,
    *,
    limit: int = 8,
    today: date | None = None,
) -> list[Hit]:
    today = today or date.today()
    fts = _fts_query(query)
    fts_hits: list[sqlite3.Row] = []
    if fts:
        try:
            fts_hits = conn.execute(
                """
                SELECT objects.id, objects.type, objects.title, objects.path,
                       objects.slug, objects.body, objects.updated,
                       bm25(objects_fts) AS rank
                FROM objects_fts
                JOIN objects ON objects.rowid = objects_fts.rowid
                WHERE objects_fts MATCH ?
                ORDER BY rank
                LIMIT 40
                """,
                (fts,),
            ).fetchall()
        except sqlite3.OperationalError:
            fts_hits = []
    tokens = _tokens(query)
    ranked: dict[str, Hit] = {}
    bodies: dict[str, str] = {}
    for row in fts_hits:
        ranked[row["id"]] = _hit_from_row(row, tokens, today, bodies, fts_rank=row["rank"])
    _expand_claim_links(conn, ranked, tokens, today, bodies)
    _expand_neighbors(conn, ranked, tokens, today, bodies)
    _boost_graph(conn, ranked)
    if not ranked:
        ranked.update(_substring_fallback(conn, tokens, today, bodies))
    hits = sorted(ranked.values(), key=lambda h: h.score, reverse=True)[:limit]
    # Snippets only for what is returned. Candidates that fall out of the top-k never pay for one.
    for hit in hits:
        hit.snippet = _snippet(bodies.get(hit.id, ""), tokens)
    return hits


def evidence_set(query: str, *, limit: int = 8, db: Path | None = None) -> str:
    conn = connect(db)
    try:
        hits = search_conn(conn, query, limit=limit)
        return format_evidence(conn, query, hits)
    finally:
        conn.close()


def format_evidence(conn: sqlite3.Connection, query: str, hits: list[Hit]) -> str:
    lines = [f"# Evidence set", f"query: {query}", ""]
    if not hits:
        lines.append("empty. wiki is silent on this query.")
        return "\n".join(lines) + "\n"
    for i, hit in enumerate(hits, 1):
        lines.append(f"{i}. {hit.id}  {hit.path}  score={hit.score:.3f}")
        lines.append(f"   {hit.title}")
        if hit.snippet:
            lines.append(f"   {hit.snippet}")
        lines.append(f"   signals: {', '.join(hit.reasons)}")
        lines.append("")
    hit_ids = [h.id for h in hits]
    lines.append("## Claims")
    nearby = []
    if hit_ids:
        q = ",".join("?" * len(hit_ids))
        nearby = conn.execute(
            f"""
            SELECT DISTINCT claims.id, claims.subject, claims.predicate, claims.object,
                   claims.status, claims.confidence
            FROM claims
            LEFT JOIN claim_concepts ON claim_concepts.claim_id = claims.id
            LEFT JOIN claim_sources ON claim_sources.claim_id = claims.id
            WHERE claims.id IN ({q})
               OR claim_concepts.concept_id IN ({q})
               OR claim_sources.source_id IN ({q})
            """,
            hit_ids + hit_ids + hit_ids,
        ).fetchall()
    if not nearby:
        lines.append("none linked from this set.")
    else:
        seen: set[str] = set()
        for row in nearby:
            if row["id"] in seen:
                continue
            seen.add(row["id"])
            lines.append(
                f"- {row['id']} [{row['status']}/{row['confidence']}] "
                f"{row['subject']} {row['predicate']} {row['object']}"
            )
    lines.append("")
    contradictions = []
    if hit_ids:
        q = ",".join("?" * len(hit_ids))
        slugs = [h.slug for h in hits]
        sq = ",".join("?" * len(slugs))
        contradictions = conn.execute(
            f"""
            SELECT id, claim_a, claim_b, reason, status, severity
            FROM contradictions
            WHERE id IN ({q})
               OR claim_a IN ({q})
               OR claim_b IN ({q})
               OR page IN ({sq})
            """,
            hit_ids + hit_ids + hit_ids + slugs,
        ).fetchall()
    lines.append("## Contradictions")
    if not contradictions:
        lines.append("none linked from this set.")
    else:
        for row in contradictions:
            lines.append(
                f"- {row['id']} [{row['status']}/{row['severity']}] "
                f"{row['claim_a']} <-> {row['claim_b']} - {row['reason']}"
            )
    return "\n".join(lines) + "\n"


def _fts_query(query: str) -> str:
    tokens = _tokens(query)
    parts = []
    for tok in tokens:
        if ":" in tok:
            parts.append(f'"{tok}"')
            _, _, slug = tok.partition(":")
            if slug:
                parts.append(f"{slug}*")
            continue
        if len(tok) >= 3:
            parts.append(f"{tok}*")
        else:
            parts.append(f'"{tok}"')
    return " OR ".join(parts)


def _tokens(query: str) -> list[str]:
    out = []
    seen = set()
    for raw in TOKEN.findall(query.lower()):
        if raw in STOP:
            continue
        candidates = [raw]
        if raw in ALIASES:
            candidates.append(ALIASES[raw])
        for tok in candidates:
            if tok not in seen:
                seen.add(tok)
                out.append(tok)
    return out


def _hit_from_row(
    row: sqlite3.Row,
    tokens: list[str],
    today: date,
    bodies: dict[str, str],
    *,
    fts_rank: object = None,
    extra_score: float = 0.0,
    extra_reasons: tuple[str, ...] = (),
) -> Hit:
    score = extra_score
    reasons = list(extra_reasons)
    if fts_rank is not None:
        score += -float(fts_rank)
        reasons.append("fts")
    extra, lex_reasons = _lexical_bonus(row, tokens)
    score += extra
    reasons.extend(lex_reasons)
    kind = row["type"]
    if kind == "decision" and not DECIDE_TOKENS.isdisjoint(tokens):
        score += 4.0
        reasons.append("decision-intent")
    if kind == "contradiction" and not CONFLICT_TOKENS.isdisjoint(tokens):
        score += 3.0
        reasons.append("contradiction-intent")
    score *= schema.TYPE_WEIGHT.get(kind, 0.8)
    recency, recency_reason = _recency_bonus(row["updated"], today)
    score += recency
    if recency_reason:
        reasons.append(recency_reason)
    object_id = row["id"]
    bodies[object_id] = row["body"] or ""
    return Hit(
        id=object_id,
        type=kind,
        title=row["title"] or object_id,
        path=row["path"],
        slug=row["slug"],
        snippet="",
        score=score,
        updated=row["updated"] or "",
        reasons=tuple(reasons),
    )


def _fetch_objects(conn: sqlite3.Connection, object_ids: list[str]) -> dict[str, sqlite3.Row]:
    """One IN query instead of one query per id. Order of the result is by rowid."""
    if not object_ids:
        return {}
    q = ",".join("?" * len(object_ids))
    rows = conn.execute(f"{OBJECT_SELECT} WHERE id IN ({q}) ORDER BY rowid", object_ids).fetchall()
    return {row["id"]: row for row in rows}


def _expand_claim_links(
    conn: sqlite3.Connection,
    ranked: dict[str, Hit],
    tokens: list[str],
    today: date,
    bodies: dict[str, str],
) -> None:
    if not ranked:
        return
    ids = list(ranked)
    q = ",".join("?" * len(ids))
    rows = conn.execute(
        f"""
        SELECT concept_id AS id FROM claim_concepts WHERE claim_id IN ({q})
        UNION
        SELECT source_id AS id FROM claim_sources WHERE claim_id IN ({q})
        UNION
        SELECT claim_id AS id FROM claim_concepts WHERE concept_id IN ({q})
        UNION
        SELECT claim_id AS id FROM claim_sources WHERE source_id IN ({q})
        """,
        ids + ids + ids + ids,
    ).fetchall()
    wanted: list[str] = []
    for row in rows:
        object_id = row["id"]
        if not object_id:
            continue
        hit = ranked.get(object_id)
        if hit is None:
            wanted.append(object_id)
        elif "claim-link" not in hit.reasons:
            # Found by FTS and cited by a ranked claim. Same evidence as an
            # object reached only through the claim, so it earns the same bonus.
            hit.score += 3.5 * schema.TYPE_WEIGHT.get(hit.type, 0.8)
            hit.reasons = hit.reasons + ("claim-link",)
    objects = _fetch_objects(conn, wanted)
    for object_id in wanted:
        obj = objects.get(object_id)
        if obj is not None:
            ranked[object_id] = _hit_from_row(
                obj, tokens, today, bodies, extra_score=3.5, extra_reasons=("claim-link",)
            )


def _expand_neighbors(
    conn: sqlite3.Connection,
    ranked: dict[str, Hit],
    tokens: list[str],
    today: date,
    bodies: dict[str, str],
) -> None:
    if not ranked:
        return
    top = sorted(ranked.values(), key=lambda h: h.score, reverse=True)[:5]
    ids = [h.id for h in top]
    q = ",".join("?" * len(ids))
    rows = conn.execute(
        f"""
        SELECT dst_id AS id FROM links WHERE src_id IN ({q}) AND dst_id IS NOT NULL
        UNION
        SELECT src_id AS id FROM links WHERE dst_id IN ({q}) AND src_id IS NOT NULL
        """,
        ids + ids,
    ).fetchall()
    # UNION output is sorted; keep that order so the 12-neighbor cap picks the same rows as before.
    wanted = [row["id"] for row in rows if row["id"] and row["id"] not in ranked]
    objects = _fetch_objects(conn, wanted)
    added = 0
    for object_id in wanted:
        obj = objects.get(object_id)
        if obj is None:
            continue
        if obj["type"] == "meta" and obj["slug"] in SKIP_NEIGHBOR_SLUGS:
            continue
        ranked[object_id] = _hit_from_row(
            obj, tokens, today, bodies, extra_score=1.5, extra_reasons=("graph-expand",)
        )
        added += 1
        if added >= 12:
            break


def _lexical_bonus(row: sqlite3.Row, tokens: list[str]) -> tuple[float, list[str]]:
    if not tokens:
        return 0.0, []
    title = (row["title"] or "").lower()
    object_id = (row["id"] or "").lower()
    slug = (row["slug"] or "").lower()
    blob = f"{title} {object_id} {slug}"
    hits = sum(1 for tok in tokens if tok in blob)
    if hits == 0:
        return 0.0, []
    ratio = hits / len(tokens)
    bonus = 6.0 * ratio
    reasons = ["title"] if any(tok in title for tok in tokens) else ["id"]
    if ratio == 1:
        bonus += 4.0
        reasons.append("all-terms")
    return bonus, reasons


def _recency_bonus(updated: str, today: date) -> tuple[float, str]:
    parsed = _parse_date(updated)
    if not parsed:
        return 0.0, ""
    age = (today - parsed).days
    if age <= 7:
        return 1.2, "recency"
    if age <= 30:
        return 0.6, "recency"
    if age >= 365:
        return -0.4, "stale"
    return 0.0, ""


def _boost_graph(conn: sqlite3.Connection, ranked: dict[str, Hit]) -> None:
    if not ranked:
        return
    ids = list(ranked)
    placeholders = ",".join("?" * len(ids))
    rows = conn.execute(
        f"""
        SELECT src_id, dst_id FROM links
        WHERE src_id IN ({placeholders}) OR dst_id IN ({placeholders})
        """,
        ids + ids,
    ).fetchall()
    neighbors: dict[str, set[str]] = {i: set() for i in ids}
    for row in rows:
        src, dst = row["src_id"], row["dst_id"]
        if src in neighbors and dst:
            neighbors[src].add(dst)
        if dst in neighbors and src:
            neighbors[dst].add(src)
    top = sorted(ranked.values(), key=lambda h: h.score, reverse=True)[:5]
    top_ids = {h.id for h in top}
    for object_id, hit in ranked.items():
        if object_id in top_ids:
            continue
        overlap = neighbors.get(object_id, set()) & top_ids
        if overlap:
            hit.score += 1.4 * len(overlap)
            hit.reasons = hit.reasons + ("graph",)


def _substring_fallback(
    conn: sqlite3.Connection, tokens: list[str], today: date, bodies: dict[str, str]
) -> dict[str, Hit]:
    if not tokens:
        return {}
    clauses = []
    params: list[str] = []
    for tok in tokens[:6]:
        like = f"%{tok}%"
        clauses.append("(lower(title) LIKE lower(?) OR lower(id) LIKE lower(?) OR lower(body) LIKE lower(?))")
        params.extend([like, like, like])
    sql = f"{OBJECT_SELECT} WHERE {' OR '.join(clauses)} LIMIT 30"
    rows = conn.execute(sql, params).fetchall()
    ranked: dict[str, Hit] = {}
    for row in rows:
        ranked[row["id"]] = _hit_from_row(
            row, tokens, today, bodies, extra_score=1.0, extra_reasons=("fallback",)
        )
    return ranked


def _snippet(body: str, tokens: list[str], width: int = 180) -> str:
    compact = WS.sub(" ", body).strip()
    if not compact:
        return ""
    lower = compact.lower()
    idx = -1
    for tok in tokens:
        idx = lower.find(tok)
        if idx >= 0:
            break
    if idx < 0:
        idx = 0
    start = max(0, idx - 40)
    chunk = compact[start : start + width]
    if start > 0:
        chunk = "…" + chunk
    if start + width < len(compact):
        chunk = chunk + "…"
    return chunk


def _parse_date(value: str) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(value[:10])
    except ValueError:
        return None
