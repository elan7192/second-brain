#!/usr/bin/env python3
"""Shared parse/validate helpers for the claims + provenance memory layer."""

from __future__ import annotations

import csv
import io
import re
from dataclasses import dataclass, field
from pathlib import Path

CLAIM_FIELDS = [
    "claim_id",
    "kind",
    "status",
    "confidence",
    "text",
    "source",
    "raw",
    "url",
    "created_at",
    "updated_at",
    "created_by",
    "derived_from",
    "pages",
]
CONFLICT_FIELDS = [
    "conflict_id",
    "title",
    "status",
    "resolution",
    "pages",
]
KINDS = {"fact", "inference", "opinion"}
STATUSES = {"active", "deprecated", "disputed", "unknown"}
CONFLICT_STATUSES = {"unresolved", "resolved"}
CONFIDENCES = {"high", "medium", "low", "unverified"}
MEMORY_V1_REQUIRED = ("schema", "created", "updated", "created_by", "confidence")
INJECTION_RE = re.compile(
    r"(ignore\s+(all\s+)?(previous|prior|above)\s+instructions"
    r"|ignore\s+your\s+(system\s+)?prompt"
    r"|you\s+are\s+now\s+"
    r"|new\s+instructions\s*:"
    r"|disclose\s+(your\s+)?(system\s+prompt|hidden)"
    r"|from\s+now\s+on,?\s+you\s+will"
    r"|do\s+not\s+follow\s+(the\s+)?(previous|above|system))",
    re.I,
)
FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_CODE_RE = re.compile(r"`[^`]+`")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.S)
CLAIMS_SECTION_RE = re.compile(
    r"^## Claims kept[^\n]*\n(.*?)(?=^## |\Z)", re.M | re.S
)
PAGES_SECTION_RE = re.compile(
    r"^## Pages updated\n(.*?)(?=^## |\Z)", re.M | re.S
)
CONFLICT_RE = re.compile(r"^## (C\d+)\. (.+)$", re.M)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
RAW_PATH_RE = re.compile(r"`(raw/[^`]+)`")
URL_RE = re.compile(r"https?://[^\s)]+")
SEE_ONLY_RE = re.compile(r"^See \[\[[^\]]+\]\]\.?$", re.I)

TRUSTED_SCHEMA_FILES = ("AGENTS.md", "MEMORY.md", "decisions.md", "CLAUDE.md")


@dataclass
class Claim:
    claim_id: str
    kind: str
    status: str
    confidence: str
    text: str
    source: str
    raw: str = ""
    url: str = ""
    created_at: str = ""
    updated_at: str = ""
    created_by: str = ""
    derived_from: str = ""
    pages: str = ""

    def row(self) -> dict[str, str]:
        return {name: getattr(self, name) for name in CLAIM_FIELDS}


@dataclass
class Conflict:
    conflict_id: str
    title: str
    status: str
    resolution: str
    pages: str = ""

    def row(self) -> dict[str, str]:
        return {name: getattr(self, name) for name in CONFLICT_FIELDS}


@dataclass
class Frontmatter:
    raw: dict[str, object] = field(default_factory=dict)

    def get(self, key: str, default: str = "") -> str:
        value = self.raw.get(key, default)
        if isinstance(value, list):
            return ", ".join(str(item) for item in value)
        if value is None:
            return default
        return str(value)


def parse_frontmatter(text: str) -> tuple[Frontmatter, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return Frontmatter(), text
    data: dict[str, object] = {}
    key: str | None = None
    for line in match.group(1).splitlines():
        if line.startswith("  - ") and key:
            bucket = data.setdefault(key, [])
            if not isinstance(bucket, list):
                bucket = [str(bucket)]
                data[key] = bucket
            bucket.append(line[4:].strip())
            continue
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            data[key] = value if value else []
            continue
        key = None
    body = text[match.end() :]
    return Frontmatter(data), body


def strip_code(text: str) -> str:
    text = FENCE_RE.sub(" ", text)
    return INLINE_CODE_RE.sub(" ", text)


def injection_hits(text: str) -> list[str]:
    return [match.group(0) for match in INJECTION_RE.finditer(strip_code(text))]


def extract_raw_path(text: str) -> str:
    match = RAW_PATH_RE.search(text)
    return match.group(1) if match else ""


def extract_url(text: str) -> str:
    match = URL_RE.search(text)
    return match.group(0) if match else ""


def extract_pages(text: str) -> str:
    match = PAGES_SECTION_RE.search(text)
    if not match:
        return ""
    slugs = [item.strip() for item in WIKILINK_RE.findall(match.group(1))]
    slugs = [slug for slug in slugs if slug and slug.lower() != "none"]
    return "|".join(slugs)


def split_claim_chunks(section: str) -> list[str]:
    lines = [line.rstrip() for line in section.strip().splitlines()]
    bullets = [line[2:].strip() for line in lines if line.lstrip().startswith("- ")]
    if bullets:
        chunks = bullets
    else:
        chunks = [part.strip() for part in re.split(r"\n\s*\n", section) if part.strip()]
    cleaned: list[str] = []
    for chunk in chunks:
        text = re.sub(r"\s+", " ", chunk).strip()
        if not text or SEE_ONLY_RE.match(text):
            continue
        cleaned.append(text)
    return cleaned


def parse_source_claims(path: Path, root: Path) -> list[Claim]:
    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    section_match = CLAIMS_SECTION_RE.search(body)
    if not section_match:
        return []
    rel_source = path.relative_to(root).as_posix()
    created = meta.get("created")
    updated = meta.get("updated") or created
    raw = extract_raw_path(body)
    url = extract_url(body)
    pages = extract_pages(body)
    claims: list[Claim] = []
    for index, chunk in enumerate(split_claim_chunks(section_match.group(1)), start=1):
        confidence = "unverified" if re.search(r"\bunverified\b", chunk, re.I) else "medium"
        claims.append(
            Claim(
                claim_id=f"{path.stem}-{index:02d}",
                kind="fact",
                status="active",
                confidence=confidence,
                text=chunk,
                source=rel_source,
                raw=raw,
                url=url,
                created_at=created,
                updated_at=updated,
                created_by="compile-claims",
                derived_from=path.stem,
                pages=pages,
            )
        )
    return claims


def parse_curated_claims(path: Path, root: Path) -> list[Claim]:
    text = path.read_text(encoding="utf-8")
    _, body = parse_frontmatter(text)
    claims: list[Claim] = []
    parts = re.split(r"^## ", body, flags=re.M)
    rel = path.relative_to(root).as_posix()
    for part in parts[1:]:
        lines = part.strip().splitlines()
        if not lines:
            continue
        claim_id = lines[0].strip()
        if claim_id.startswith("c-") is False:
            continue
        fields: dict[str, str] = {}
        body_lines: list[str] = []
        in_body = False
        for line in lines[1:]:
            if not in_body and ":" in line and not line.startswith(" "):
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip()
                continue
            in_body = True
            body_lines.append(line)
        text_body = " ".join(item.strip() for item in body_lines if item.strip())
        text_body = re.sub(r"\s+", " ", text_body).strip()
        if not text_body:
            continue
        claims.append(
            Claim(
                claim_id=claim_id,
                kind=fields.get("kind", "fact"),
                status=fields.get("status", "active"),
                confidence=fields.get("confidence", "medium"),
                text=text_body,
                source=fields.get("source", rel),
                raw=fields.get("raw", ""),
                url=fields.get("url", ""),
                created_at=fields.get("created_at", ""),
                updated_at=fields.get("updated_at", fields.get("created_at", "")),
                created_by=fields.get("created_by", "agent"),
                derived_from=fields.get("derived_from", ""),
                pages=fields.get("pages", ""),
            )
        )
    return claims


def parse_conflicts(path: Path) -> list[Conflict]:
    text = path.read_text(encoding="utf-8")
    matches = list(CONFLICT_RE.finditer(text))
    conflicts: list[Conflict] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[start:end]
        resolution_match = re.search(r"^Resolution:\s*(.+)$", block, re.M)
        resolution = resolution_match.group(1).strip() if resolution_match else ""
        status = "unresolved" if re.search(r"unresolved", resolution, re.I) else "resolved"
        if not resolution:
            status = "unresolved"
        pages = "|".join(WIKILINK_RE.findall(block))
        conflicts.append(
            Conflict(
                conflict_id=match.group(1),
                title=match.group(2).strip(),
                status=status,
                resolution=resolution,
                pages=pages,
            )
        )
    return conflicts


def csv_text(fieldnames: list[str], rows: list[dict[str, str]]) -> str:
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({name: row.get(name, "") for name in fieldnames})
    return buf.getvalue()


def validate_claim(claim: Claim) -> list[str]:
    errors: list[str] = []
    if not claim.claim_id:
        errors.append("missing claim_id")
    if claim.kind not in KINDS:
        errors.append(f"{claim.claim_id} bad kind {claim.kind!r}")
    if claim.status not in STATUSES:
        errors.append(f"{claim.claim_id} bad status {claim.status!r}")
    if claim.confidence not in CONFIDENCES:
        errors.append(f"{claim.claim_id} bad confidence {claim.confidence!r}")
    if not claim.text:
        errors.append(f"{claim.claim_id} empty text")
    if not claim.source:
        errors.append(f"{claim.claim_id} missing source")
    if not claim.created_at:
        errors.append(f"{claim.claim_id} missing created_at")
    return errors


def validate_memory_v1(path: Path, text: str) -> list[str]:
    meta, body = parse_frontmatter(text)
    if meta.get("schema") != "memory-v1":
        return []
    errors: list[str] = []
    for key in MEMORY_V1_REQUIRED:
        if not meta.get(key):
            errors.append(f"{path.as_posix()} missing {key}")
    source = meta.get("source")
    derived = meta.get("derived_from")
    if not source and not derived:
        errors.append(f"{path.as_posix()} missing source or derived_from")
    if meta.get("confidence") and meta.get("confidence") not in CONFIDENCES:
        errors.append(f"{path.as_posix()} bad confidence {meta.get('confidence')!r}")
    headings = set(re.findall(r"^## (FACT|INFERENCE|OPINION)\s*$", body, re.M))
    if meta.get("type") == "concept" and not headings:
        errors.append(
            f"{path.as_posix()} memory-v1 concept missing ## FACT/INFERENCE/OPINION"
        )
    return errors


def gather_claims(root: Path) -> list[Claim]:
    claims: list[Claim] = []
    sources = sorted((root / "wiki" / "sources").glob("*.md"))
    for path in sources:
        claims.extend(parse_source_claims(path, root))
    curated = root / "wiki" / "claims" / "curated-claims.md"
    if curated.exists():
        claims.extend(parse_curated_claims(curated, root))
    claims.sort(key=lambda item: item.claim_id)
    return claims


def gather_conflicts(root: Path) -> list[Conflict]:
    path = root / "wiki" / "contradictions.md"
    if not path.exists():
        return []
    conflicts = parse_conflicts(path)
    conflicts.sort(key=lambda item: item.conflict_id)
    return conflicts


def compile_tables(root: Path) -> tuple[str, list[str]]:
    claims = gather_claims(root)
    errors: list[str] = []
    for claim in claims:
        errors.extend(validate_claim(claim))
    seen: set[str] = set()
    for claim in claims:
        if claim.claim_id in seen:
            errors.append(f"duplicate claim_id {claim.claim_id}")
        seen.add(claim.claim_id)
    claims_csv = csv_text(CLAIM_FIELDS, [claim.row() for claim in claims])
    return claims_csv, errors


def contradiction_ids(root: Path) -> set[str]:
    return {item.conflict_id for item in gather_conflicts(root)}
