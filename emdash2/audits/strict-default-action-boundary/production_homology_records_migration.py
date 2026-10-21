"""Native profile adaptation of original adjunction/H-map record consumers.

Source hashes and exact counts delimit the replay. Existing record fields,
chosen operations and hypotheses are retained; no formal rule is introduced.
"""
from pathlib import Path
import hashlib
import re
from production_diagram_observation_migration import _atom, _profile, _point_readings

AUDIT = Path(__file__).resolve().parent
SOURCES = {
    "emdash3_2_commutative_algebra_freyd_adjunction_homology.lp": {
        "generatorView": 0,
        "observations": [
            0,
            0
        ],
        "otherOpposites": 2,
        "outgoingDiagramViews": 0,
        "profile": [
            0,
            0,
            0,
            0
        ],
        "reflection": 0,
        "sha256": "c3ec52498871bf8c7f76aafdf227f340a9d9746fca27f443b825c8f7728e889d"
    },
    "emdash3_2_homology_adjunction_record_data.lp": {
        "generatorView": 0,
        "observations": [
            4,
            0
        ],
        "otherOpposites": 0,
        "outgoingDiagramViews": 0,
        "profile": [
            1,
            1,
            1,
            0
        ],
        "reflection": 0,
        "sha256": "a69da3525f2d88cdfa4f547d166d531346627cf69186d365cc4b2f5bad2b2f5c"
    },
    "emdash3_2_one_cat_adjunction_cancellation.lp": {
        "generatorView": 0,
        "observations": [
            32,
            0
        ],
        "otherOpposites": 0,
        "outgoingDiagramViews": 0,
        "profile": [
            36,
            2,
            4,
            1
        ],
        "reflection": 2,
        "sha256": "b7489080893ab29b628fbda59b321e493db95f038829e0e94e5f0e33118dcec3"
    },
    "emdash3_2_one_cat_adjunction_records.lp": {
        "generatorView": 0,
        "observations": [
            42,
            0
        ],
        "otherOpposites": 0,
        "outgoingDiagramViews": 0,
        "profile": [
            26,
            4,
            2,
            2
        ],
        "reflection": 0,
        "sha256": "fcce3cf2002c15e3719a5fc255c5ef88c5cb311b00443c218c40fa85d18f6001"
    },
    "emdash3_2_one_cat_chain_pair_homology_records.lp": {
        "generatorView": 0,
        "observations": [
            0,
            0
        ],
        "otherOpposites": 0,
        "outgoingDiagramViews": 4,
        "profile": [
            1,
            1,
            0,
            1
        ],
        "reflection": 0,
        "sha256": "67965aaa99c58e9f0ddb1675dfc868962093f8d59aecf848e449ec2cee3c6ba3"
    },
    "emdash3_2_one_cat_zero_diagram_inputs.lp": {
        "fragment": "production_zero_diagram_record_inputs.lpfragment",
        "sha256": "b0ee693567bfb371d1ddb1985b28b6f3f83123d0b4cc9aafbde0ebf86ac4d1fa"
    },
    "examples/freyd_adjunction_homology.lp": {
        "generatorView": 0,
        "observations": [
            0,
            0
        ],
        "otherOpposites": 2,
        "outgoingDiagramViews": 0,
        "profile": [
            0,
            0,
            0,
            0
        ],
        "reflection": 0,
        "sha256": "bf6ee301ff52199c66837d1947bfb793c474cacaec891d5ea53e3d11d85bff99"
    },
    "examples/freyd_adjunction_homology_maps.lp": {
        "generatorView": 0,
        "observations": [
            0,
            0
        ],
        "otherOpposites": 4,
        "outgoingDiagramViews": 0,
        "profile": [
            0,
            0,
            0,
            0
        ],
        "reflection": 0,
        "sha256": "bb40532548e74b951051433efcea542101f45ff4e388fbe32f4086e894ee3540"
    },
    "examples/one_cat_adjunction_records.lp": {
        "generatorView": 0,
        "observations": [
            72,
            0
        ],
        "otherOpposites": 0,
        "outgoingDiagramViews": 0,
        "profile": [
            16,
            10,
            0,
            5
        ],
        "reflection": 0,
        "sha256": "9d058efd01c39d553804450f54b118e241ce5aec42a7158bc01b5ab6ab5e170a"
    },
    "examples/one_cat_chain_pair_homology_maps.lp": {
        "generatorView": 0,
        "observations": [
            0,
            0
        ],
        "otherOpposites": 0,
        "outgoingDiagramViews": 0,
        "profile": [
            0,
            0,
            0,
            4
        ],
        "reflection": 0,
        "sha256": "8467a2c24221dab6e16ae51aef813d46382b7e0be2ec13856da665f68ad4b49a"
    },
    "examples/one_cat_chain_pair_homology_records.lp": {
        "generatorView": 0,
        "observations": [
            0,
            0
        ],
        "otherOpposites": 0,
        "outgoingDiagramViews": 3,
        "profile": [
            3,
            0,
            0,
            5
        ],
        "reflection": 0,
        "sha256": "c825b407746c6982d685a97de39378952a1f9173ed0526923d057f8baeeed4ed"
    },
    "examples/one_cat_zero_diagram_inputs.lp": {
        "generatorView": 2,
        "observations": [
            10,
            2
        ],
        "otherOpposites": 0,
        "outgoingDiagramViews": 0,
        "profile": [
            2,
            2,
            0,
            1
        ],
        "reflection": 0,
        "sha256": "d053ee2620a4f2d3c5998f322fa486a9ae711e610217742e82d46bd6e62d2876"
    }
}


def finish_homology_records(path, text):
    if path not in SOURCES:
        return None
    spec = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == spec['sha256'], path
    original = text
    if 'fragment' in spec:
        text = (AUDIT / spec['fragment']).read_text()
    else:
        text = _profile(text, spec['profile'])
        text = _point_readings(text, spec['observations'])
        text, count = re.subn(r'\bOp_cat\b', 'TotalOp_cat', text)
        assert count == spec['otherOpposites'], (path, count)
        text, count = re.subn(r'\bone_cat_diagram_map_path\b', 'one_cat_oplax_diagram_map_path', text)
        assert count == spec['reflection'], (path, count)
        if count:
            text = 'require open emdash.emdash3_2_one_cat_diagram_family_reflection;\n' + text
        if spec['generatorView']:
            pattern = r'@fapp1_fapp0\s+WalkingArrow_cat\s+C\s+d\s+walking_arrow_src\s+walking_arrow_tgt\s+walking_arrow_generator'
            text, count = re.subn(pattern, '@terminal_arrow_test_outgoing C d', text)
            assert count == spec['generatorView'], (path, count)
            text = 'require open emdash.emdash3_2_zero_arrow_diagram_observations;\n' + text
        edits = []
        for match in re.finditer(r'\(@chain_pair_outgoing_diagram\b', text):
            atom, end = _atom(text, match.start())
            edits.append((match.start(), end, f'(@OddDual_func WalkingArrow_cat C {atom})'))
        assert len(edits) == spec['outgoingDiagramViews'], (path, len(edits))
        for start, end, replacement in reversed(edits):
            text = text[:start] + replacement + text[end:]
    declaration = r'^(?:protected |constant |injective )?symbol\s+([^\s\[]+)'
    assert re.findall(declaration, text, re.M) == re.findall(declaration, original, re.M), path
    return text
