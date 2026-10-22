"""Remaining original action-profile reviewers and encoded evaluation comparison."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {
    "examples/action_profile_canonical_sigma_basechange_controls.lp": {
        "fragment": "production_action_profile_canonical_sigma_basechange_controls.lpfragment",
        "sha256": "83d381164d7e691fb7c9c855781727c4507a3cbbe3d5c72b7f17f19e199989f2"
    },
    "examples/action_profile_native_component_agreement_review.lp": {
        "fragment": "production_action_profile_native_component_agreement_review.lpfragment",
        "sha256": "2c8b55e70eecf7b818e9db7b18a2405bbd1a8d99447b186bf0c9e88a2005ac5b"
    },
    "examples/action_profile_native_residual_view_controls.lp": {
        "fragment": "production_action_profile_native_residual_view_controls.lpfragment",
        "sha256": "e08d61affda4e0dc63c4d413d79878b31c6bee641f20fa7217ca48109c67364a"
    },
    "examples/action_profile_sheaf_baseline_helper_controls.lp": {
        "fragment": "production_action_profile_sheaf_baseline_helper_controls.lpfragment",
        "sha256": "146b4b70fbe7013786b19ef71d45cd2bf25d96d2719d36a84e5101336153fb46"
    },
    "examples/action_profile_walking_cross_category_controls.lp": {
        "fragment": "production_action_profile_walking_cross_category_controls.lpfragment",
        "sha256": "4c2d86cfb588b949969b77639c371f459732be69fdf27f58fe7be60c5aa15bfc"
    }
}
NATIVE_OWNER_SHA256 = '17557f65653465a4c3cead2d8e42a925ce35b158dc20ae8ddb662af30af190eb'


def finish_remaining_action_reviewers(path, text):
    if path in SOURCES:
        spec = SOURCES[path]
        assert hashlib.sha256(text.encode()).hexdigest() == spec['sha256'], path
        return (AUDIT / spec['fragment']).read_text()
    if path != 'emdash3_2_walking_arrow_native_observation.lp':
        return None
    assert hashlib.sha256(text.encode()).hexdigest() == NATIVE_OWNER_SHA256
    marker = '// The existing ordinary-target guard selects ordinary evaluation.'
    assert text.count(marker) == 1
    clause = (AUDIT / 'production_encoded_evaluation_comparison.lpfragment').read_text()
    return text.replace(marker, clause + '\n' + marker, 1)
