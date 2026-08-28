#!/usr/bin/env python3
"""Claim ledger, disposable FTS5 index, hybrid retrieve.

Git markdown stays canonical. The SQLite file is disposable.
"""

from __future__ import annotations

import csv
import math
import re
import sqlite3
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAIMS_CSV = ROOT / "wiki" / "claims.csv"
CACHE_DB = ROOT / ".cache" / "wiki.sqlite"
LINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
FRONT_UPDATED = re.compile(r"^updated:\s*(\d{4}-\d{2}-\d{2})", re.M)
FRONT_TYPE = re.compile(r"^type:\s*(\S+)", re.M)
TOKEN = re.compile(r"[A-Za-z0-9_]+|[\u4e00-\u9fff]+")
CJK = re.compile(r"[\u4e00-\u9fff]")

FIELDS = (
    "id",
    "claim",
    "source",
    "evidence",
    "status",
    "created_at",
    "verified_at",
    "wiki_page",
    "supports",
    "contradicts",
    "supersedes",
)
STATUSES = {
    "extracted",
    "verified",
    "unverified",
    "contradicted",
    "superseded",
}
ID_RE = re.compile(r"^C\d{4}$")
SKIP_DIRS = {".git", ".obsidian", "templates", "raw", "growth", "output"}
SKIP_FILES = {"CLAUDE.md", "README.md"}
STOPWORDS = {
    "a",
    "an",
    "the",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "i",
    "me",
    "my",
    "we",
    "our",
    "you",
    "your",
    "he",
    "she",
    "it",
    "they",
    "them",
    "this",
    "that",
    "these",
    "those",
    "of",
    "in",
    "on",
    "for",
    "to",
    "from",
    "with",
    "by",
    "at",
    "as",
    "or",
    "and",
    "but",
    "not",
    "no",
    "do",
    "did",
    "does",
    "doing",
    "why",
    "how",
    "what",
    "when",
    "where",
    "who",
    "which",
    "can",
    "could",
    "should",
    "would",
    "will",
    "just",
    "about",
    "into",
    "over",
    "after",
    "before",
    "than",
    "then",
}

SKIP_INDEX_STEMS = {"log"}


@dataclass
class Claim:
    id: str
    claim: str
    source: str
    evidence: str
    status: str
    created_at: str
    verified_at: str
    wiki_page: str
    supports: str = ""
    contradicts: str = ""
    supersedes: str = ""

    def ids_in(self, field_name: str) -> list[str]:
        raw = getattr(self, field_name)
        return [part.strip() for part in raw.split("|") if part.strip()]


@dataclass
class Hit:
    slug: str
    path: str
    score: float
    via: list[str] = field(default_factory=list)
    claims: list[str] = field(default_factory=list)
    title: str = ""


def parse_claims(path: Path | None = None) -> list[Claim]:
    csv_path = path or CLAIMS_CSV
    if not csv_path.is_file():
        raise FileNotFoundError(f"missing claims ledger: {csv_path}")
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != list(FIELDS):
            raise ValueError(
                f"claims.csv columns must be {list(FIELDS)}; got {reader.fieldnames}"
            )
        rows = []
        for row in reader:
            rows.append(Claim(**{name: (row.get(name) or "").strip() for name in FIELDS}))
    return rows


def md_catalog(root: Path) -> dict[str, Path]:
    found: dict[str, Path] = {}
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        found[path.stem] = path
    return found


def validate_claims(
    root: Path | None = None, csv_path: Path | None = None
) -> list[str]:
    root = root or ROOT
    csv_path = csv_path or (root / "wiki" / "claims.csv")
    errors: list[str] = []
    try:
        rows = parse_claims(csv_path)
    except (OSError, ValueError) as exc:
        return [str(exc)]
    catalog = md_catalog(root)
    catalog_lower = {slug.lower(): slug for slug in catalog}
    seen: set[str] = set()
    contradicted_pages: set[str] = set()
    contradictions = root / "wiki" / "contradictions.md"
    contra_text = contradictions.read_text(encoding="utf-8") if contradictions.is_file() else ""
    for row in rows:
        loc = f"claims.csv:{row.id or '?'}"
        if not ID_RE.match(row.id):
            errors.append(f"{loc} id must match C0000")
        elif row.id in seen:
            errors.append(f"{loc} duplicate id")
        seen.add(row.id)
        if not row.claim:
            errors.append(f"{loc} empty claim")
        if not row.source:
            errors.append(f"{loc} empty source")
        if not row.evidence:
            errors.append(f"{loc} empty evidence")
        if row.status not in STATUSES:
            errors.append(f"{loc} bad status {row.status!r}")
        if row.status == "verified" and not row.verified_at:
            errors.append(f"{loc} verified row needs verified_at")
        source_slug = row.source
        if source_slug and source_slug not in catalog and source_slug.lower() not in catalog_lower:
            if source_slug not in {"AGENTS.md", "decisions.md", "MEMORY.md"}:
                errors.append(f"{loc} unknown source [[{source_slug}]]")
        if row.wiki_page and row.wiki_page not in catalog:
            errors.append(f"{loc} unknown wiki_page [[{row.wiki_page}]]")
        if row.status == "contradicted":
            contradicted_pages.add(row.wiki_page or row.source)
    for slug in sorted(p for p in contradicted_pages if p):
        if f"[[{slug}]]" not in contra_text:
            errors.append(f"contradicted {slug} missing from wiki/contradictions.md")
    return errors


def prefix_rewrite(query: str) -> str:
    tokens = TOKEN.findall(query.lower())
    kept = [tok for tok in tokens if tok not in STOPWORDS]
    if not kept:
        kept = tokens
    parts = []
    for tok in kept:
        if CJK.search(tok) or len(tok) < 2:
            parts.append(tok)
        else:
            parts.append(f"{tok}*")
    return " OR ".join(parts)


def _page_meta(text: str) -> tuple[str, str, date | None]:
    kind = "note"
    match = FRONT_TYPE.search(text)
    if match:
        kind = match.group(1)
    updated = None
    match = FRONT_UPDATED.search(text)
    if match:
        updated = date.fromisoformat(match.group(1))
    title = ""
    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break
    return title, kind, updated


def iter_index_pages(root: Path) -> list[Path]:
    pages = []
    extra = [root / "AGENTS.md", root / "MEMORY.md", root / "decisions.md"]
    for path in list(root.rglob("*.md")) + extra:
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        if path.stem in SKIP_INDEX_STEMS:
            continue
        pages.append(path)
    # de-dupe while keeping order
    seen: set[Path] = set()
    unique = []
    for path in pages:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        unique.append(path)
    return unique


def rebuild_index(root: Path | None = None, db_path: Path | None = None) -> Path:
    root = root or ROOT
    db_path = db_path or CACHE_DB
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()
    conn = sqlite3.connect(db_path)
    conn.execute(
        "CREATE VIRTUAL TABLE pages USING fts5("
        "slug, path, title, body, kind, updated, "
        "tokenize='porter unicode61', prefix='2 3 4')"
    )
    rows = []
    for path in iter_index_pages(root):
        text = path.read_text(encoding="utf-8")
        title, kind, updated = _page_meta(text)
        rel = path.resolve().relative_to(root.resolve()).as_posix()
        rows.append(
            (
                path.stem,
                rel,
                title or path.stem,
                text,
                kind,
                updated.isoformat() if updated else "",
            )
        )
    conn.executemany(
        "INSERT INTO pages(slug, path, title, body, kind, updated) VALUES (?,?,?,?,?,?)",
        rows,
    )
    conn.commit()
    conn.close()
    return db_path


def _wikilinks(text: str) -> set[str]:
    return {match.group(1).strip() for match in LINK.finditer(text)}


def _days_ago(updated: str, today: date) -> float | None:
    if not updated:
        return None
    try:
        then = date.fromisoformat(updated)
    except ValueError:
        return None
    return max((today - then).days, 0)


def retrieve(
    query: str,
    root: Path | None = None,
    db_path: Path | None = None,
    limit: int = 8,
    today: date | None = None,
) -> list[Hit]:
    root = root or ROOT
    db_path = db_path or (root / ".cache" / "wiki.sqlite")
    today = today or date.today()
    claims = parse_claims(root / "wiki" / "claims.csv")
    by_page: dict[str, list[Claim]] = {}
    for row in claims:
        if row.wiki_page:
            by_page.setdefault(row.wiki_page, []).append(row)
    rebuild_index(root, db_path)
    terms = [part for part in prefix_rewrite(query).split(" OR ") if part]
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    catalog_body = {
        row["slug"]: (row["body"], row["path"], row["title"], row["kind"], row["updated"])
        for row in conn.execute(
            "SELECT slug, path, title, body, kind, updated FROM pages"
        )
    }

    scores: dict[str, Hit] = {}

    def bump(slug: str, amount: float, why: str) -> None:
        if slug not in catalog_body:
            return
        _body, path, title, _kind, _updated = catalog_body[slug]
        hit = scores.get(slug)
        if hit is None:
            hit = Hit(slug=slug, path=path, score=0.0, title=title)
            scores[slug] = hit
        hit.score += amount
        if why not in hit.via:
            hit.via.append(why)

    for term in terms:
        try:
            rows = conn.execute(
                "SELECT slug, bm25(pages) AS rank FROM pages WHERE pages MATCH ? "
                "ORDER BY rank LIMIT 24",
                (term,),
            ).fetchall()
        except sqlite3.OperationalError:
            continue
        common = len(rows) >= 24
        for row in rows:
            amount = max(0.5, 8.0 - float(row["rank"]))
            if common:
                amount *= 0.2
            bump(row["slug"], amount, "fts")

    fts_slugs = sorted(
        (slug for slug, hit in scores.items() if "fts" in hit.via),
        key=lambda slug: scores[slug].score,
        reverse=True,
    )[:8]
    for slug in fts_slugs:
        body = catalog_body.get(slug, ("", "", "", "", ""))[0]
        for dest in _wikilinks(body):
            if dest == slug:
                continue
            bump(dest, 1.2, f"graph:{slug}")

    for slug, hit in list(scores.items()):
        body, path, title, kind, updated = catalog_body[slug]
        days = _days_ago(updated, today)
        if days is not None:
            hit.score += 2.0 * math.exp(-days / 180.0)
            hit.via.append("recency")
        if kind in {"source", "decision"} or slug in {"decisions", "MEMORY", "AGENTS"}:
            hit.score += 1.5
            hit.via.append("authority")
        page_claims = by_page.get(slug, [])
        for row in page_claims:
            hit.claims.append(row.id)
            if row.status == "verified":
                hit.score += 2.0
                hit.via.append(f"claim:{row.id}")
            elif row.status == "contradicted":
                hit.score -= 4.0
                hit.via.append(f"contradicted:{row.id}")
            elif row.status == "unverified":
                hit.score -= 0.5

    ranked = sorted(scores.values(), key=lambda hit: hit.score, reverse=True)
    conn.close()
    return ranked[:limit]


def format_hits(query: str, hits: list[Hit]) -> str:
    lines = [f"# retrieve: {query}", f"pages={len(hits)}"]
    if not hits:
        lines.append("no hits")
        return "\n".join(lines) + "\n"
    for i, hit in enumerate(hits, 1):
        via = ",".join(hit.via)
        claims = ",".join(hit.claims)
        extra = f"  claims={claims}" if claims else ""
        lines.append(
            f"{i}. {hit.slug}  score={hit.score:.2f}  via={via}{extra}\n   {hit.path}"
        )
    return "\n".join(lines) + "\n"
