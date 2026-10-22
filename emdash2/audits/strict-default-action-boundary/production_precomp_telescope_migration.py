"""Migrate original precomposition/telescope observations at their actual classifiers."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {
    "examples/action_profile_precomp_minimal_all_orders.lp": {
        "fragment": "production_action_profile_precomp_minimal_all_orders.lpfragment",
        "sha256": "79f2d8f006701a06bf645212450f44abdb268b4c783a2a984c7053a2a4cbb88e"
    },
    "examples/action_profile_precomp_minimal_mixed_controls.lp": {
        "fragment": "production_action_profile_precomp_minimal_mixed_controls.lpfragment",
        "sha256": "9e453dd943364887c4cf772e34cc77ede103117fd3e4fc9cbbcc54534937c7d7"
    },
    "examples/action_profile_telescope_profile_paths.lp": {
        "fragment": "production_action_profile_telescope_profile_paths.lpfragment",
        "suffix": "\n",
        "sha256": "fbf1c010b23a32d5750535c812a4582a004f31901538b7d0b1879db506f5bb85"
    },
    "examples/action_profile_telescope_profile_controls.lp": {
        "fragment": "production_action_profile_telescope_profile_controls.lpfragment",
        "sha256": "c8ed627a0219bf6d33373547a2ae01b908b4f1e3164a53ba0b2c15fe1cb0620f"
    },
    "examples/action_profile_telescope_projection_controls.lp": {
        "fragment": "production_action_profile_telescope_projection_controls.lpfragment",
        "sha256": "cd7a5e9775d931c0a2d7fe28bafac87b8997b63f425adaf984511d145e8490a3"
    },
    "examples/action_profile_relative_transfor_profile_instances.lp": {
        "fragment": "production_action_profile_relative_transfor_profile_instances.lpfragment",
        "sha256": "af41ae70919430d75d4c685f0f6e08ec2444d06a377ae1cecce7b30f327a7ea9"
    },
    "examples/action_profile_relative_transfor_profile.lp": {
        "fragment": "production_action_profile_relative_transfor_profile.lpfragment",
        "sha256": "b8955e2398f14169a93417207fe8b96e0e72e1e85545314f9e00f16f2b3ad961"
    },
    "examples/action_profile_telescope_unit_overlap_controls.lp": {
        "fragment": "production_action_profile_telescope_unit_overlap_controls.lpfragment",
        "sha256": "91eb92e32b9dc36421997c6e8f9e6562bb6d292fbf6612c52f71466d8c5f1eaa"
    }
}
CORE_INPUT_SHA256 = '2a89475099b13e16c449488368d0b3315c5a35a8b47aded2f41ed62e9ef465f5'


def finish_precomp_telescope_reviewers(path, text):
    if path not in SOURCES:
        return None
    spec = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == spec['sha256'], path
    return (AUDIT / spec['fragment']).read_text() + spec.get('suffix', '')


def add_ordinary_telescope_identities(text):
    assert hashlib.sha256(text.encode()).hexdigest() == CORE_INPUT_SHA256
    marker = '// Defined ordinary diagram views of the same canonical whole Hom packages.'
    assert text.count(marker) == 1
    rules = (AUDIT / 'production_precomp_telescope_identity.lpfragment').read_text()
    return text.replace(marker, rules + '\n' + marker, 1)
