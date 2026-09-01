"""Build and query the disposable SQLite FTS5 index."""

from __future__ import annotations

import os
import re
import sqlite3
from datetime import date
from pathlib import Path

from . import frontmatter, ids, schema
from .frontmatter import WIKILINK
from .paths import CLAIMS_PATH, CONTRADICTIONS_PATH, ROOT, db_path, rel_posix

DECISION_HEAD = re.compile(r"^## (D\d+)\.\s+(.+)$", re.MULTILINE)
CONTRA_HEAD = re.compile(r"^## (C\d+)\.\s+(.+)$", re.MULTILINE)

# Link targets resolve against slug, full id, or any of these prefixes on the id.
ID_PREFIXES = (
    "concept:", "source:", "person:", "meta:", "memory:", "decision:", "contradiction:", "claim:",
)

OBJECT_COLUMNS = (
    "id", "type", "title", "path", "slug", "status", "created", "updated",
    "valid_from", "valid_until", "body",
)
INSERT_OBJECT = (
    f"INSERT INTO objects ({', '.join(OBJECT_COLUMNS)}) "
    f"VALUES ({', '.join('?' * len(OBJECT_COLUMNS))})"
)


class ObjectRow:
    """Plain slotted row. dataclasses would drag in inspect at import time."""

    __slots__ = OBJECT_COLUMNS + ("links",)

    def __init__(
        self,
        id: str,
        type: str,
        title: str,
        path: str,
        slug: str,
        status: str,
        created: str,
        updated: str,
        valid_from: str,
        valid_until: str,
        body: str,
        links: tuple[str, ...],
    ) -> None:
        self.id = id
        self.type = type
        self.title = title
        self.path = path
        self.slug = slug
        self.status = status
        self.created = created
        self.updated = updated
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.body = body
        self.links = links

    def values(self) -> tuple[str, ...]:
        return tuple(getattr(self, name) for name in OBJECT_COLUMNS)


def connect(path: Path | None = None) -> sqlite3.Connection:
    target = path or db_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(target))
    conn.row_factory = sqlite3.Row
    return conn


def is_stale(root: Path | None = None, db: Path | None = None) -> bool:
    """True when the index is missing or any indexed input is newer than it.

    Compares mtimes of every knowledge page, the directories that hold them
    (a delete or rename touches the directory, not the file), and the claim
    and contradiction registries. About 2 ms for 300 pages.
    """
    root = root or ROOT
    target = db or db_path()
    try:
        built = target.stat().st_mtime_ns
    except FileNotFoundError:
        return True
    paths = ids.iter_knowledge_paths(root)
    paths.extend(
        p for p in (root / "wiki" / "data" / "claims.yaml", root / "wiki" / "data" / "contradictions.yaml")
        if p.exists()
    )
    newest = 0
    for path in paths:
        newest = max(newest, path.stat().st_mtime_ns)
    for folder in {path.parent for path in paths}:
        newest = max(newest, folder.stat().st_mtime_ns)
    return newest > built


def ensure(root: Path | None = None, db: Path | None = None) -> bool:
    """Rebuild only when stale. Returns True if a rebuild happened."""
    if not is_stale(root, db):
        return False
    rebuild(root, db)
    return True


def rebuild(root: Path | None = None, db: Path | None = None) -> dict[str, int]:
    """Build into a sibling temp file, then atomically replace the index.

    Readers never see a half-built database. The index is disposable, so
    journaling and fsync are off while building.
    """
    root = root or ROOT
    target = db or db_path()
    tmp = target.with_name(target.name + ".tmp")
    if tmp.exists():
        tmp.unlink()
    conn = connect(tmp)
    conn.executescript("PRAGMA journal_mode = OFF; PRAGMA synchronous = OFF;")
    _create(conn)
    objects = _iter_objects(root)
    conn.executemany(INSERT_OBJECT, (obj.values() for obj in objects))
    conn.executemany(
        "INSERT INTO links (src_id, dst_slug) VALUES (?, ?)",
        ((obj.id, dest) for obj in objects for dest in obj.links),
    )
    # Page links resolve here, before claims land. Claim edges keep dst_id NULL
    # and reach retrieval through claim_sources / claim_concepts instead.
    # Resolving them too changed eval recall (95% to 91%), so the order stays.
    _resolve_link_ids(conn)
    claims = _load_yaml_list(root / "wiki" / "data" / "claims.yaml", "claims")
    if not claims and (root / CLAIMS_PATH.relative_to(ROOT)).exists():
        claims = _load_yaml_list(root / CLAIMS_PATH.relative_to(ROOT), "claims")
    for claim in claims:
        _insert_claim(conn, claim)
    contradictions = _load_yaml_list(
        root / "wiki" / "data" / "contradictions.yaml", "contradictions"
    )
    for item in contradictions:
        _insert_contradiction(conn, item)
    conn.execute("INSERT INTO objects_fts (objects_fts) VALUES ('rebuild')")
    conn.executescript(
        """
        CREATE INDEX objects_slug ON objects (slug);
        CREATE INDEX links_src ON links (src_id);
        CREATE INDEX links_dst ON links (dst_id);
        CREATE INDEX claim_sources_claim ON claim_sources (claim_id);
        CREATE INDEX claim_sources_source ON claim_sources (source_id);
        CREATE INDEX claim_concepts_claim ON claim_concepts (claim_id);
        CREATE INDEX claim_concepts_concept ON claim_concepts (concept_id);
        """
    )
    conn.commit()
    stats = {
        "objects": conn.execute("SELECT COUNT(*) FROM objects").fetchone()[0],
        "claims": conn.execute("SELECT COUNT(*) FROM claims").fetchone()[0],
        "contradictions": conn.execute("SELECT COUNT(*) FROM contradictions").fetchone()[0],
        "links": conn.execute("SELECT COUNT(*) FROM links").fetchone()[0],
    }
    conn.close()
    os.replace(tmp, target)
    return stats


def _create(conn: sqlite3.Connection) -> None:
    # objects_fts is an external-content table: it indexes objects in place
    # instead of storing a second copy of every body.
    conn.executescript(
        """
        CREATE TABLE objects (
          id TEXT PRIMARY KEY,
          type TEXT NOT NULL,
          title TEXT,
          path TEXT NOT NULL,
          slug TEXT NOT NULL,
          status TEXT,
          created TEXT,
          updated TEXT,
          valid_from TEXT,
          valid_until TEXT,
          body TEXT NOT NULL
        );
        CREATE VIRTUAL TABLE objects_fts USING fts5(
          id,
          title,
          body,
          type,
          content='objects',
          content_rowid='rowid',
          tokenize='porter unicode61'
        );
        CREATE TABLE links (
          src_id TEXT NOT NULL,
          dst_slug TEXT NOT NULL,
          dst_id TEXT
        );
        CREATE TABLE claims (
          id TEXT PRIMARY KEY,
          subject TEXT,
          predicate TEXT,
          object TEXT,
          confidence TEXT,
          status TEXT,
          valid_from TEXT,
          valid_until TEXT,
          observed_at TEXT,
          superseded_by TEXT
        );
        CREATE TABLE claim_sources (
          claim_id TEXT NOT NULL,
          source_id TEXT NOT NULL
        );
        CREATE TABLE claim_concepts (
          claim_id TEXT NOT NULL,
          concept_id TEXT NOT NULL
        );
        CREATE TABLE contradictions (
          id TEXT PRIMARY KEY,
          claim_a TEXT,
          claim_b TEXT,
          reason TEXT,
          status TEXT,
          severity TEXT,
          resolution TEXT,
          resolution_source TEXT,
          page TEXT
        );
        """
    )


def _iter_objects(root: Path) -> list[ObjectRow]:
    rows: list[ObjectRow] = []
    seen: set[str] = set()
    for path in ids.iter_knowledge_paths(root):
        text = path.read_text(encoding="utf-8")
        meta, body = frontmatter.split(text)
        rel = rel_posix(path, root)
        kind = schema.kind_for(path, str(meta.get("type", "")), root)
        object_id = str(meta.get("id") or ids.id_for(path, root))
        title = frontmatter.title_of(meta, body, path.stem)
        links = tuple(_unique(WIKILINK.findall(text)))
        rows.append(
            ObjectRow(
                id=object_id,
                type=kind,
                title=title,
                path=rel,
                slug=path.stem,
                status=str(meta.get("status") or "active"),
                created=str(meta.get("created") or ""),
                updated=str(meta.get("updated") or ""),
                valid_from=str(meta.get("valid_from") or meta.get("created") or ""),
                valid_until=str(meta.get("valid_until") or ""),
                body=body.strip(),
                links=links,
            )
        )
        seen.add(object_id)
        if path.name == "decisions.md":
            rows.extend(_split_decisions(rel, text, object_id))
        if path.name == "contradictions.md":
            rows.extend(_split_contradictions_page(rel, text, object_id))
    return rows


def _split_decisions(rel: str, text: str, parent_id: str) -> list[ObjectRow]:
    rows: list[ObjectRow] = []
    matches = list(DECISION_HEAD.finditer(text))
    for i, match in enumerate(matches):
        code, title = match.group(1), match.group(2).strip()
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        chunk = text[start:end].strip()
        slug = _slugify(title)
        object_id = schema.make_id("decision", slug)
        rows.append(
            ObjectRow(
                id=object_id,
                type="decision",
                title=f"{code} {title}",
                path=f"{rel}#{code}",
                slug=slug,
                status="locked",
                created=_field_after(chunk, "Locked"),
                updated=_field_after(chunk, "Locked"),
                valid_from=_field_after(chunk, "Locked"),
                valid_until="",
                body=chunk,
                links=tuple(_unique(WIKILINK.findall(chunk))),
            )
        )
    return rows


def _split_contradictions_page(rel: str, text: str, parent_id: str) -> list[ObjectRow]:
    rows: list[ObjectRow] = []
    matches = list(CONTRA_HEAD.finditer(text))
    for i, match in enumerate(matches):
        code, title = match.group(1), match.group(2).strip()
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        chunk = text[start:end].strip()
        slug = code.lower()
        rows.append(
            ObjectRow(
                id=schema.make_id("contradiction", slug),
                type="contradiction",
                title=f"{code} {title}",
                path=f"{rel}#{code}",
                slug=slug,
                status=_status_from_chunk(chunk),
                created="",
                updated="",
                valid_from="",
                valid_until="",
                body=chunk,
                links=tuple(_unique(WIKILINK.findall(chunk))),
            )
        )
    return rows


def _insert_claim(conn: sqlite3.Connection, claim: dict) -> None:
    claim_id = str(claim["id"])
    subject = str(claim.get("subject") or "")
    predicate = str(claim.get("predicate") or "")
    obj = str(claim.get("object") or "")
    body = f"{subject} {predicate} {obj}".strip()
    conn.execute(
        """
        INSERT INTO claims (
          id, subject, predicate, object, confidence, status,
          valid_from, valid_until, observed_at, superseded_by
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            claim_id,
            subject,
            predicate,
            obj,
            str(claim.get("confidence") or ""),
            str(claim.get("status") or ""),
            str(claim.get("valid_from") or "") or None,
            str(claim.get("valid_until") or "") or None,
            str(claim.get("observed_at") or "") or None,
            str(claim.get("superseded_by") or "") or None,
        ),
    )
    conn.execute(
        """
        INSERT INTO objects (
          id, type, title, path, slug, status, created, updated,
          valid_from, valid_until, body
        ) VALUES (?, 'claim', ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            claim_id,
            f"{subject} {predicate} {obj}".strip(),
            f"wiki/data/claims.yaml#{claim_id}",
            claim_id.split(":", 1)[-1],
            str(claim.get("status") or "supported"),
            str(claim.get("valid_from") or claim.get("observed_at") or ""),
            str(claim.get("observed_at") or claim.get("valid_from") or ""),
            str(claim.get("valid_from") or ""),
            str(claim.get("valid_until") or ""),
            body,
        ),
    )
    for source_id in _as_id_list(claim.get("sources")):
        conn.execute(
            "INSERT INTO claim_sources (claim_id, source_id) VALUES (?, ?)",
            (claim_id, source_id),
        )
        conn.execute(
            "INSERT INTO links (src_id, dst_slug) VALUES (?, ?)",
            (claim_id, source_id.split(":", 1)[-1]),
        )
    for concept_id in _as_id_list(claim.get("concepts")):
        conn.execute(
            "INSERT INTO claim_concepts (claim_id, concept_id) VALUES (?, ?)",
            (claim_id, concept_id),
        )
        conn.execute(
            "INSERT INTO links (src_id, dst_slug) VALUES (?, ?)",
            (claim_id, concept_id.split(":", 1)[-1]),
        )


def _insert_contradiction(conn: sqlite3.Connection, item: dict) -> None:
    contra_id = str(item["id"])
    conn.execute(
        """
        INSERT INTO contradictions (
          id, claim_a, claim_b, reason, status, severity,
          resolution, resolution_source, page
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            contra_id,
            str(item.get("claim_a") or ""),
            str(item.get("claim_b") or ""),
            str(item.get("reason") or ""),
            str(item.get("status") or ""),
            str(item.get("severity") or "medium"),
            str(item.get("resolution") or "") or None,
            str(item.get("resolution_source") or "") or None,
            str(item.get("page") or ""),
        ),
    )
    # objects row may already exist from contradictions.md split
    exists = conn.execute(
        "SELECT 1 FROM objects WHERE id = ?", (contra_id,)
    ).fetchone()
    if not exists:
        conn.execute(
            """
            INSERT INTO objects (
              id, type, title, path, slug, status, created, updated,
              valid_from, valid_until, body
            ) VALUES (?, 'contradiction', ?, ?, ?, ?, '', '', '', '', ?)
            """,
            (
                contra_id,
                str(item.get("reason") or contra_id),
                str(item.get("page") or f"wiki/data/contradictions.yaml#{contra_id}"),
                contra_id.split(":", 1)[-1],
                str(item.get("status") or ""),
                str(item.get("reason") or ""),
            ),
        )


def _resolve_link_ids(conn: sqlite3.Connection) -> None:
    """Map every link target to an object id in one pass.

    A target matches an object by slug, by full id, or by id minus a known
    prefix. The first object in insertion order wins, same as the old
    correlated subquery, but this is O(objects + links) instead of a scan
    of every object for every link.
    """
    first: dict[str, str] = {}
    for row in conn.execute("SELECT id, slug FROM objects ORDER BY rowid"):
        object_id, slug = row["id"], row["slug"]
        keys = [slug, object_id]
        for prefix in ID_PREFIXES:
            if object_id.startswith(prefix):
                keys.append(object_id[len(prefix):])
        for key in keys:
            first.setdefault(key, object_id)
    targets = [row["dst_slug"] for row in conn.execute("SELECT DISTINCT dst_slug FROM links")]
    conn.executemany(
        "UPDATE links SET dst_id = ? WHERE dst_slug = ?",
        ((first[slug], slug) for slug in targets if slug in first),
    )


def _load_yaml_list(path: Path, key: str) -> list[dict]:
    if not path.exists():
        return []
    from .yamlutil import loads as load_yaml

    data = load_yaml(path.read_text(encoding="utf-8"))
    if data is None:
        return []
    if isinstance(data, dict):
        items = data.get(key) or data.get("items") or []
    else:
        items = data
    return [item for item in items if isinstance(item, dict)]


def _as_id_list(value: object) -> list[str]:
    if not value:
        return []
    if isinstance(value, list):
        out = []
        for item in value:
            if isinstance(item, dict):
                if "id" in item:
                    out.append(str(item["id"]))
                elif item:
                    out.append(str(next(iter(item.values()))))
            else:
                out.append(str(item))
        return out
    return [str(value)]


def _unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        slug = item.strip()
        if slug and slug not in seen:
            seen.add(slug)
            out.append(slug)
    return out


def _slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug or "untitled"


def _field_after(chunk: str, label: str) -> str:
    match = re.search(rf"{label}:\s*(\d{{4}}-\d{{2}}-\d{{2}})", chunk)
    return match.group(1) if match else ""


def _status_from_chunk(chunk: str) -> str:
    lower = chunk.lower()
    if "resolution: unresolved" in lower or "unresolved." in lower:
        return "unresolved"
    if "`unverified`" in lower or "unverified" in lower:
        return "unverified"
    if "resolution:" in lower:
        return "resolved"
    return "open"


def today() -> date:
    return date.today()
