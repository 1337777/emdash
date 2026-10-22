"""Strict-default controls and a head-preserving conventional-pre comparison."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {
    "examples/action_profile_vertical_unit_controls.lp": {
        "fragment": "production_vertical_unit_default_controls.lpfragment",
        "sha256": "907c6073516a915c67eb22acd56cb22481e2f0b3cbc556b3b6eb7b2a067b4dc6"
    },
    "examples/action_profile_postcomp_profile_controls.lp": {
        "fragment": "production_postcomp_default_controls.lpfragment",
        "sha256": "3ebca2dd7b67bc1a92beea9819f929cf102d4c5172ef98098eba85384689fae9"
    },
    "examples/action_profile_vertical_profile_controls.lp": {
        "fragment": "production_vertical_default_controls.lpfragment",
        "sha256": "41545080418c911804cfdef7e143adf1e91ad170fc23d29185b72b6f4f404823"
    }
}
CORE_INPUT_SHA256 = '7ed6b2d06bded69965fc771d447dfb8b9faa26d114aa060b1e5389243ffe7789'


def finish_action_controls(path, text):
    if path not in SOURCES:
        return None
    spec = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == spec['sha256'], path
    return (AUDIT / spec['fragment']).read_text()


def add_default_vertical_comparison(text):
    assert hashlib.sha256(text.encode()).hexdigest() == CORE_INPUT_SHA256
    marker = '// Proof-time pre/right readings after ordinary action has already projected.'
    assert text.count(marker) == 1
    clause = (AUDIT / 'production_default_vertical_clause.lpfragment').read_text()
    return text.replace(marker, clause + '\n' + marker, 1)
