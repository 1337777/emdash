"""Adapt original column Hom/diagram proofs to their existing native profiles.

No runtime or unification rules are introduced. Source hashes and exact
replacement counts bound this authoring transformation; emitted LP is checked
at its original module positions.
"""
import hashlib
import re
from production_diagram_observation_migration import _atom

SOURCES = {
    "emdash3_2_commutative_algebra_freyd_adjunction_homology_maps.lp": {
        "replacements": {
            "TotalOp_cat": 2
        },
        "sha256": "2d3a5fd8b8aefeea3df205097b084b8c6283c825bb10099c3abbe81f7f3b6209"
    },
    "emdash3_2_commutative_algebra_freyd_native_column_diagram_paths.lp": {
        "replacements": {
            "Functor_oplax_cat": 56,
            "hom": 2,
            "one_cat_oplax_diagram_map_path": 2
        },
        "sha256": "eaf8d751e3a6581920846001a95bb7c11d8318fde55c02469786143df6ef3622"
    },
    "emdash3_2_commutative_algebra_freyd_native_middle_column_comparisons.lp": {
        "replacements": {
            "Functor_oplax_cat": 4
        },
        "sha256": "4e834788888965d1cf8b98822f3b0c32944571fc0df13cfe3e5e647344fb65a6"
    },
    "emdash3_2_commutative_algebra_freyd_native_middle_column_inputs.lp": {
        "replacements": {
            "Functor_oplax_cat": 5
        },
        "sha256": "fe9f89df6f1fe535a135644e606404b723162e335df5ee29da745fa0255d9482"
    },
    "emdash3_2_commutative_algebra_freyd_native_middle_column_quotient_paths.lp": {
        "replacements": {
            "Functor_oplax_cat": 4,
            "diagram_oplax_evaluation_at_func": 1
        },
        "sha256": "bf14c86b037ce1728554e2455ee66a88d833ad69b2b96296b0a1d4e9359a8ac7"
    },
    "emdash3_2_homology_family_map_point_observations.lp": {
        "replacements": {
            "Functor_oplax_cat": 10,
            "TotalOp_cat": 2,
            "diagram_oplax_family_at_func": 4,
            "diagram_oplax_family_map_at": 1
        },
        "sha256": "7ccf93c4df72c4f44f8870f8fc084a4eaa4a36eaa0ce186684d280f067c67de8"
    },
    "emdash3_2_homology_native_comparison_cycle_paths.lp": {
        "replacements": {
            "Functor_oplax_cat": 47,
            "TotalOp_cat": 1,
            "diagram_oplax_family_at_func": 4,
            "diagram_oplax_family_map_at": 1,
            "hom": 3
        },
        "sha256": "da84775b4c7268d2fc26025207c3d08029615736cf09cf23128e5ef46c411634"
    },
    "emdash3_2_homology_native_map_comparison_paths.lp": {
        "replacements": {
            "Functor_oplax_cat": 6,
            "TotalOp_cat": 1,
            "diagram_oplax_family_at_func": 4,
            "diagram_oplax_family_map_at": 1
        },
        "sha256": "3fd4f1fc700a1ec62bf09ff08a3be64c3472d7c29a5f25964cde28ecbb2b81fd"
    },
    "emdash3_2_kernel_family_map_point_views.lp": {
        "replacements": {
            "Functor_oplax_cat": 15,
            "TotalOp_cat": 1
        },
        "sha256": "fcbe3a50b7fdcf54b59706a9e9eec612202fa1f5ebf7ee2adcc9b967a7f271a6"
    },
    "emdash3_2_one_cat_chain_pair_homology_maps.lp": {
        "replacements": {
            "TotalOp_cat": 2
        },
        "sha256": "860f32a2520a3c73070ed446887f90739b398b040b3b756ae665d6459ed025d2"
    },
    "emdash3_2_one_cat_cokernel_point_cancellation.lp": {
        "replacements": {
            "Functor_oplax_cat": 18,
            "TotalOp_cat": 3,
            "arrowEvaluation": 4,
            "diagram_oplax_evaluation_at_func": 2,
            "hom": 4,
            "object": 3,
            "objectEvaluation": 7,
            "one_cat_oplax_diagram_map_path": 1
        },
        "sha256": "ad3157c3a1c8394e8f0d328377a4e56e2f5beef5ecb469ec9309b776697e0382"
    },
    "emdash3_2_one_cat_middle_column_inputs.lp": {
        "replacements": {
            "Functor_oplax_cat": 3,
            "TotalOp_cat": 2
        },
        "sha256": "25c38b106aa7604743c37215e65892579c775cbd0388d5b3d5f506e3730d7af4"
    },
    "emdash3_2_one_cat_row_homology_maps.lp": {
        "replacements": {
            "Functor_oplax_cat": 2,
            "TotalOp_cat": 10,
            "diagram_oplax_family_map_at": 6
        },
        "sha256": "aa0e7e11fe8df306cf81ce2031d61857b81392e0acb691cda7b6cbdc004c5b35"
    },
    "examples/freyd_native_middle_column_comparisons.lp": {
        "replacements": {
            "Functor_oplax_cat": 5
        },
        "sha256": "2a77043ccba5b3d7a88a67d540e08140d162e4aaa33f48816c724f730a73d380"
    }
}


def finish_column_homology_paths(path, text):
    if path not in SOURCES:
        return None
    spec = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == spec['sha256'], path
    original = text
    counts = {}
    for pattern, replacement in (
        (r'Functor_cat(?=\s+WalkingArrow_cat\b)', 'Functor_oplax_cat'),
        (r'\bdiagram_family_at_func\b', 'diagram_oplax_family_at_func'),
        (r'\bdiagram_family_transf\b', 'diagram_oplax_family_transf'),
        (r'\bsym_transf_tapp0_transf\b', 'diagram_oplax_family_map_at'),
        (r'\bdiagram_evaluation_at_func\b', 'diagram_oplax_evaluation_at_func'),
        (r'\bone_cat_diagram_map_path\b', 'one_cat_oplax_diagram_map_path'),
        (r'\bOp_cat\b', 'TotalOp_cat'),
    ):
        text, counts[replacement] = re.subn(pattern, replacement, text)

    # Native diagram objects and Hom carriers preserve both endpoints.
    for pattern, kind in (
        (r'(?<!\w)Functor\s+WalkingArrow_cat\b', 'object'),
        (r'@Transf\s+WalkingArrow_cat\b', 'hom'),
    ):
        marker = re.compile(pattern)
        count = 0
        while hits := list(marker.finditer(text)):
            match = hits[-1]
            coefficient, end = _atom(text, match.end())
            native = f'(Functor_oplax_cat WalkingArrow_cat {coefficient})'
            replacement = f'Obj {native}' if kind == 'object' else f'@Hom {native}'
            text = text[:match.start()] + replacement + text[end:]
            count += 1
        counts[kind] = count

    # Observe through the existing whole fixed-evaluation functor.
    for pattern, arity, kind in (
        (r'@fapp0\s+WalkingArrow_cat\b', 3, 'objectEvaluation'),
        (r'@tapp0_fapp0\s+WalkingArrow_cat\b', 5, 'arrowEvaluation'),
    ):
        marker = re.compile(pattern)
        count = 0
        while hits := list(marker.finditer(text)):
            match = hits[-1]
            cursor, arguments = match.end(), []
            for _ in range(arity):
                argument, cursor = _atom(text, cursor)
                arguments.append(argument)
            coefficient = arguments[0]
            native = f'(Functor_oplax_cat WalkingArrow_cat {coefficient})'
            if kind == 'objectEvaluation':
                _, diagram, point = arguments
                evaluation = f'(@diagram_oplax_evaluation_at_func WalkingArrow_cat {coefficient} {point})'
                replacement = f'@fapp0 {native} {coefficient} {evaluation} {diagram}'
            else:
                _, source, target, point, cell = arguments
                evaluation = f'(@diagram_oplax_evaluation_at_func WalkingArrow_cat {coefficient} {point})'
                replacement = f'@fapp1_fapp0 {native} {coefficient} {evaluation} {source} {target} {cell}'
            text = text[:match.start()] + replacement + text[cursor:]
            count += 1
        counts[kind] = count

    if counts['one_cat_oplax_diagram_map_path']:
        text = 'require open emdash.emdash3_2_one_cat_diagram_family_reflection;\n' + text
    assert {key: value for key, value in counts.items() if value} == spec['replacements'], (path, counts)
    declaration = r'^(?:protected |constant |injective )?symbol\s+([^\s\[]+)'
    assert re.findall(declaration, text, re.M) == re.findall(declaration, original, re.M), path
    return text
