"""Retain public computational inverse owners in ordinary terminal equivalence records."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {
    "emdash3_2_one_cat_terminal_adjunctions.lp": {
        "fragment": "production_terminal_equivalence_records.lpfragment",
        "inputBoundary": "existing staged owner after earlier migration steps",
        "sha256": "beb3db840898d483ce5064be364f9394eadc1a23237736aa2ee114d892880ab5"
    },
    "examples/one_cat_terminal_adjunctions.lp": {
        "fragment": "production_terminal_adjunctions_reviewer.lpfragment",
        "inputBoundary": "pinned original reviewer",
        "sha256": "2ac29393100e5b46de1fbcbededecb058a307a5dd11cb934c7cdb8f5bf12dddf"
    }
}


def finish_ordinary_reviewers(path, text):
    if path not in SOURCES:
        return None
    spec = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == spec['sha256'], (path, spec['inputBoundary'])
    return (AUDIT / spec['fragment']).read_text()
