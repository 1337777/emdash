"""Original diagram/mate reviewer migration at unchanged library owners."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {
    "examples/arrow_diagram_point_usability.lp": {
        "fragment": "production_arrow_point_usability_reviewer.lpfragment",
        "sha256": "07c2150092be6b2cc26c3f540159eafd5e587cc1cd0f5093c8c99bfc7d3d420c"
    },
    "examples/one_cat_adjunction_family_zero_inputs.lp": {
        "fragment": "production_adjunction_zero_inputs_reviewer.lpfragment",
        "sha256": "0471047296fc0e3cd45465f3bb82199d12224fca82aee1e69e692c05781c344c"
    },
    "examples/walking_arrow_diagram_evaluation.lp": {
        "fragment": "production_walking_evaluation_reviewer.lpfragment",
        "sha256": "c06eda4c2ec524e9aaf3c353c4b9cbb67dc2b9faa9eb43cdc79ab342712aa2c0"
    }
}


def finish_diagram_mate_reviewers(path, text):
    if path not in SOURCES:
        return None
    spec = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == spec['sha256'], path
    return (AUDIT / spec['fragment']).read_text()
