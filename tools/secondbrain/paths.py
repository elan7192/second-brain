"""Repo paths. The database lives in .cache and is rebuildable."""

from __future__ import annotations

import os
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent.parent
ROOT = TOOLS_DIR.parent
WIKI = ROOT / "wiki"
DATA = WIKI / "data"
CACHE = ROOT / ".cache"
DEFAULT_DB = CACHE / "secondbrain.sqlite"
CLAIMS_PATH = DATA / "claims.yaml"
CONTRADICTIONS_PATH = DATA / "contradictions.yaml"
EVAL_DIR = ROOT / "eval"


def db_path() -> Path:
    override = os.environ.get("SECOND_BRAIN_DB")
    return Path(override) if override else DEFAULT_DB
