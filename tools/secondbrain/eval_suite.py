"""Eval suite for retrieval, citations, contradictions, and stale facts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from . import claims, index, retrieve
from .paths import EVAL_DIR, ROOT
from .yamlutil import loads


@dataclass
class Question:
    id: str
    question: str
    kind: str
    must_retrieve: tuple[str, ...]
    must_include: tuple[str, ...]
    must_not_include: tuple[str, ...]
    must_claims: tuple[str, ...]
    forbidden_claims: tuple[str, ...]
    k: int = 8


@dataclass
class Scores:
    retrieval_recall: float
    retrieval_precision: float
    citation_coverage: float
    unsupported_rate: float
    contradiction_handling: float
    stale_fact_detection: float
    n: int
    failures: tuple[str, ...]


def load_questions(eval_dir: Path | None = None) -> list[Question]:
    eval_dir = eval_dir or EVAL_DIR
    questions = _as_list(loads((eval_dir / "questions.yaml").read_text(encoding="utf-8")), "questions")
    sources = _as_map(eval_dir / "expected_sources.yaml")
    expected_claims = _as_map(eval_dir / "expected_claims.yaml")
    forbidden = _as_map(eval_dir / "forbidden_claims.yaml")
    out: list[Question] = []
    for item in questions:
        qid = str(item["id"])
        out.append(
            Question(
                id=qid,
                question=str(item["question"]),
                kind=str(item.get("kind") or "fact"),
                must_retrieve=tuple(_as_str_list(item.get("must_retrieve") or sources.get(qid))),
                must_include=tuple(_as_str_list(item.get("must_include"))),
                must_not_include=tuple(
                    _as_str_list(item.get("must_not_include") or forbidden.get(qid))
                ),
                must_claims=tuple(_as_str_list(item.get("must_claims") or expected_claims.get(qid))),
                forbidden_claims=tuple(_as_str_list(item.get("forbidden_claims"))),
                k=int(item.get("k") or 8),
            )
        )
    return out


def run_eval(
    *,
    root: Path | None = None,
    eval_dir: Path | None = None,
    db: Path | None = None,
) -> tuple[int, str, Scores]:
    root = root or ROOT
    eval_dir = eval_dir or EVAL_DIR
    index.rebuild(root, db)
    questions = load_questions(eval_dir)
    recalls: list[float] = []
    precisions: list[float] = []
    citations: list[float] = []
    unsupported_flags: list[int] = []
    contra_flags: list[int] = []
    failures: list[str] = []
    conn = index.connect(db)
    try:
        searched = [
            (q, retrieve.search_conn(conn, q.question, limit=q.k)) for q in questions
        ]
        # One search per question. The evidence text is formatted from the same hits.
        evidences = [retrieve.format_evidence(conn, q.question, hits) for q, hits in searched]
        blobs = [_evidence_blob(conn, hits, ev) for (_, hits), ev in zip(searched, evidences)]
    finally:
        conn.close()
    for (question, hits), blob in zip(searched, blobs):
        hit_ids = [h.id for h in hits]
        retrieved = set(hit_ids)
        must = set(question.must_retrieve)
        recall = (len(must & retrieved) / len(must)) if must else 1.0
        relevant = _expand_relevant(must, hit_ids)
        precision = (len(relevant) / len(retrieved)) if retrieved else 1.0
        cites = 1.0 if (not must or must <= retrieved) else recall
        recalls.append(recall)
        precisions.append(precision)
        citations.append(cites)
        bad = False
        for phrase in question.must_not_include:
            if phrase.lower() in blob:
                bad = True
        for claim_id in question.forbidden_claims:
            if claim_id.lower() in blob:
                bad = True
        unsupported_flags.append(1 if bad else 0)
        if question.must_include:
            for phrase in question.must_include:
                if phrase.lower() not in blob:
                    failures.append(f"{question.id} missing phrase {phrase!r}")
        if must - retrieved:
            failures.append(
                f"{question.id} miss {sorted(must - retrieved)} got {hit_ids[:5]}"
            )
        if question.must_claims:
            missing_claims = [c for c in question.must_claims if c not in blob]
            if missing_claims:
                failures.append(f"{question.id} missing claims {missing_claims}")
        if question.kind == "contradiction":
            ok = ("unresolved" in blob) or any(h.type == "contradiction" for h in hits)
            contra_flags.append(1 if ok else 0)
            if not ok:
                failures.append(f"{question.id} contradiction not surfaced")
    stale_ok = _stale_eval(eval_dir, db)
    scores = Scores(
        retrieval_recall=_mean(recalls),
        retrieval_precision=_mean(precisions),
        citation_coverage=_mean(citations),
        unsupported_rate=_mean([float(x) for x in unsupported_flags]),
        contradiction_handling=_mean([float(x) for x in contra_flags]) if contra_flags else 1.0,
        stale_fact_detection=1.0 if stale_ok else 0.0,
        n=len(questions),
        failures=tuple(failures),
    )
    lines = [
        f"Retrieval recall          {scores.retrieval_recall * 100:.0f}%",
        f"Retrieval precision       {scores.retrieval_precision * 100:.0f}%",
        f"Citation coverage         {scores.citation_coverage * 100:.0f}%",
        f"Unsupported claims        {scores.unsupported_rate * 100:.0f}%",
        f"Contradiction handling    {scores.contradiction_handling * 100:.0f}%",
        f"Stale-fact detection      {scores.stale_fact_detection * 100:.0f}%",
        f"questions                 {scores.n}",
    ]
    if failures:
        lines.append("")
        lines.append("failures")
        lines.extend(f"- {item}" for item in failures)
    code = 0 if _pass(scores) else 1
    lines.append("PASS" if code == 0 else "FAIL")
    return code, "\n".join(lines) + "\n", scores


def _pass(scores: Scores) -> bool:
    return (
        scores.retrieval_recall >= 0.8
        and scores.citation_coverage >= 0.8
        and scores.unsupported_rate <= 0.1
        and scores.contradiction_handling >= 0.8
        and scores.stale_fact_detection >= 1.0
        and scores.retrieval_precision >= 0.2
    )


def _stale_eval(eval_dir: Path, db: Path | None) -> bool:
    from datetime import date as date_cls

    conn = index.connect(db)
    try:
        cutoff = date_cls.today().isoformat()
        expected = [
            row["id"]
            for row in conn.execute(
                """
                SELECT id FROM objects
                WHERE valid_until IS NOT NULL AND valid_until != '' AND valid_until < ?
                """,
                (cutoff,),
            )
        ]
    finally:
        conn.close()
    report = claims.stale_report(db)
    return all(item in report for item in expected)


def _evidence_blob(conn, hits: list, evidence: str) -> str:
    parts = [evidence]
    for hit in hits:
        row = conn.execute(
            "SELECT id, title, body FROM objects WHERE id = ?", (hit.id,)
        ).fetchone()
        if row:
            parts.append(f"{row['id']}\n{row['title']}\n{row['body']}")
        for extra in conn.execute(
            """
            SELECT claims.id, claims.subject, claims.predicate, claims.object
            FROM claims
            LEFT JOIN claim_concepts ON claim_concepts.claim_id = claims.id
            LEFT JOIN claim_sources ON claim_sources.claim_id = claims.id
            WHERE claim_concepts.concept_id = ? OR claim_sources.source_id = ?
               OR claims.id = ?
            """,
            (hit.id, hit.id, hit.id),
        ):
            parts.append(
                f"{extra['id']} {extra['subject']} {extra['predicate']} {extra['object']}"
            )
    return "\n".join(parts).lower()


def _expand_relevant(must: set[str], hit_ids: list[str]) -> set[str]:
    relevant = set()
    for hit in hit_ids:
        if hit in must:
            relevant.add(hit)
            continue
        for gold in must:
            _, _, gold_slug = gold.partition(":")
            _, _, hit_slug = hit.partition(":")
            if gold_slug and gold_slug in hit_slug:
                relevant.add(hit)
                break
            if gold_slug and gold_slug in hit:
                relevant.add(hit)
                break
    return relevant


def _as_list(data: object, key: str) -> list[dict]:
    if data is None:
        return []
    if isinstance(data, dict):
        items = data.get(key) or data.get("items") or []
        return [item for item in items if isinstance(item, dict)]
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    return []


def _as_map(path: Path) -> dict[str, list[str]]:
    if not path.exists():
        return {}
    data = loads(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        return {}
    out: dict[str, list[str]] = {}
    for key, value in data.items():
        out[str(key)] = _as_str_list(value)
    return out


def _as_str_list(value: object) -> list[str]:
    if not value:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def _mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)
