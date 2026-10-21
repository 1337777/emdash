"""Migrate original factor/H reviewers at unchanged staged library owners.

Only recorded coefficient annotations and native observations change.
All original assertions and reviewer proof declarations are retained.
"""
import hashlib
import re
from production_diagram_observation_migration import _atom, _profile, _point_readings

SOURCES = {
    "examples/one_cat_chain_pair_inputs.lp": {
        "encodedDiagrams": 2,
        "evaluationHeads": 0,
        "generatorView": 0,
        "observations": [
            0,
            0
        ],
        "profile": [
            2,
            0,
            0,
            0
        ],
        "sha256": "d09ef28f3ce98ee768fcc92f2d57abe2378332323d1f8c9a5bee87fdf7fd3e31",
        "transforCategories": 0
    },
    "examples/one_cat_image_coimage_factor_reconstruction.lp": {
        "encodedDiagrams": 0,
        "evaluationHeads": 0,
        "generatorView": 2,
        "observations": [
            8,
            1
        ],
        "profile": [
            6,
            3,
            1,
            3
        ],
        "sha256": "a41da5b0c858318d27950f17c5f97e412dc1ebcaf1e9114b4a2db3c7b795115f",
        "transforCategories": 2
    },
    "examples/one_cat_image_coimage_factors.lp": {
        "encodedDiagrams": 0,
        "evaluationHeads": 8,
        "generatorView": 2,
        "observations": [
            4,
            8
        ],
        "profile": [
            28,
            10,
            2,
            10
        ],
        "sha256": "b8027ad859c11d6895a458c99dac07cda907094d124f06092b2598eba7722d66",
        "transforCategories": 2
    },
    "examples/zero_arrow_cone_adjunction_homology.lp": {
        "encodedDiagrams": 0,
        "evaluationHeads": 0,
        "generatorView": 0,
        "observations": [
            0,
            0
        ],
        "profile": [
            11,
            4,
            4,
            4
        ],
        "sha256": "f8c621227aea0d334ca40a9d81c5d66550281b1de29a93a7e08e9881720220db",
        "transforCategories": 0
    },
    "examples/zero_composite_adjunction_homology.lp": {
        "encodedDiagrams": 2,
        "evaluationHeads": 0,
        "generatorView": 0,
        "observations": [
            0,
            0
        ],
        "profile": [
            16,
            0,
            0,
            3
        ],
        "sha256": "7125bf0e8fb22add18345d00f08bbe8625e18aa0af2b5d5ce402c3f96767fccd",
        "transforCategories": 0
    }
}


def finish_factor_h_reviewers(path, text):
    if path not in SOURCES:
        return None
    spec = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == spec['sha256'], path
    original = text
    text = _point_readings(_profile(text, spec['profile']), spec['observations'])
    text, count = re.subn(r'@Transf_cat\s+WalkingArrow_cat\s+C\b',
                         '@Hom_cat (Functor_oplax_cat WalkingArrow_cat C)', text)
    assert count == spec['transforCategories'], (path, count)
    text, count = re.subn(r'\bdiagram_evaluation_at_func\b', 'diagram_oplax_evaluation_at_func', text)
    assert count == spec['evaluationHeads'], (path, count)
    pattern = r'@fapp1_fapp0\s+WalkingArrow_cat\s+C\s+d\s+walking_arrow_src\s+walking_arrow_tgt\s+walking_arrow_generator'
    text, count = re.subn(pattern, '@terminal_arrow_test_outgoing C d', text)
    assert count == spec['generatorView'], (path, count)
    if count:
        text = 'require open emdash.emdash3_2_zero_arrow_diagram_observations;\n' + text
    if spec['encodedDiagrams']:
        # The final chain-pair assertion intentionally remains an ordinary
        # generator observation; only its earlier native consumer slots change.
        if path == 'examples/one_cat_chain_pair_inputs.lp':
            marker = '// The outgoing diagram generator is the original d.'
            assert text.count(marker) == 1
            prefix, suffix = text.split(marker, 1)
            suffix = marker + suffix
            pattern = r'\(@chain_pair_outgoing_diagram\b'
        else:
            assert path == 'examples/zero_composite_adjunction_homology.lp', path
            prefix, suffix = text, ''
            pattern = r'\(@walking_arrow_func\b'
        edits = []
        for match in re.finditer(pattern, prefix):
            atom, end = _atom(prefix, match.start())
            edits.append((match.start(), end, f'(@OddDual_func WalkingArrow_cat C {atom})'))
        assert len(edits) == spec['encodedDiagrams'], (path, len(edits))
        for start, end, replacement in reversed(edits):
            prefix = prefix[:start] + replacement + prefix[end:]
        text = prefix + suffix
    declaration = r'^(?:protected |constant |injective )?symbol\s+([^\s\[]+)'
    assert re.findall(declaration, text, re.M) == re.findall(declaration, original, re.M), path
    assert re.findall(r'^assert(?:not)?\b', text, re.M) == re.findall(r'^assert(?:not)?\b', original, re.M), path
    return text
