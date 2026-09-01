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


def rel_posix(path: Path, root: Path) -> str:
    """`path` relative to `root` as a posix string.

    Same lexical result as `path.relative_to(root).as_posix()`, but a string
    slice. pathlib.relative_to builds several Path objects per call and was
    28% of the validate gate on Python 3.12.
    """
    text = str(path)
    base = str(root)
    if text == base:
        return "."
    if not text.startswith(base) or text[len(base)] != os.sep:
        raise ValueError(f"{text!r} is not in the subpath of {base!r}")
    rel = text[len(base) + 1:]
    return rel.replace(os.sep, "/") if os.sep != "/" else rel
