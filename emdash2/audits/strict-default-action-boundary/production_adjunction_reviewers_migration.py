"""Original adjunction reviewers with general and Cartesian exchange and total duality."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {
    "examples/adjunction_exchange_computation.lp": {
        "fragment": "production_adjunction_exchange_reviewer.lpfragment",
        "sha256": "1e454d2a34d7c7dbd90a4933e5d563daaa3a1aa068b7ecf6e7090408eac56bc2"
    },
    "examples/adjunction_exchange_op_identity.lp": {
        "fragment": "production_adjunction_op_identity_reviewer.lpfragment",
        "sha256": "be0587775bdfbc428374e1dbf6527a1444d41713e3383b47535357ea5b0f7504"
    },
    "examples/adjunction_triangles.lp": {
        "fragment": "production_adjunction_triangles_reviewer.lpfragment",
        "sha256": "5d78949b53fdeff2e08172f7c0140794d202f0869ea134bb064de37e803ae4ec"
    }
}


def finish_adjunction_reviewers(path, text):
    if path not in SOURCES:
        return None
    spec = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == spec['sha256'], path
    return (AUDIT / spec['fragment']).read_text()
