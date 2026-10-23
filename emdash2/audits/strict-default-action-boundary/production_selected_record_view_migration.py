"""Source-pinned original selected-record and mate-evaluation continuation.

No new formal rules or operational primitives. Qualification belongs to the
emitted original declarations and complete original reviewers.
"""
import hashlib
import re

from production_diagram_observation_migration import _profile, _point_readings

SOURCES = {'emdash3_2_one_cat_adjunction_selected_views.lp': {'sha256': 'ccfc24a1924b36f93fd8feda2c2d692b21121ab7f99713f931e4baf3e10590b7',
                                                    'counts': [2, 2, 0, 1, 40, 0]},
 'emdash3_2_one_cat_homology_adjunction_records.lp': {'sha256': '1106487872fee14e57dbdd99ac5689127f69187e88d8716de293a7418dae3e8c',
                                                      'counts': [12, 0, 0, 1, 4, 0]},
 'emdash3_2_one_cat_adjunction_evaluation_paths.lp': {'sha256': '30702eaada4aa03777f73a9ea02f10b555893b891726198e2fa5e89a54857265',
                                                      'counts': [0, 0, 0, 0, 0, 0]},
 'examples/one_cat_homology_adjunction_records.lp': {'sha256': '1062a7e3bec7777d65e30382c8f9308134f09f91d857b83bc792ad479b315022',
                                                     'counts': [36, 0, 0, 6, 16, 0]},
 'examples/one_cat_adjunction_evaluation_paths.lp': {'sha256': '776ebb203f5248d6124cb2230b49a534b2d4fcfedf2f2195c7a8e883c0bbc25e',
                                                     'counts': [0, 0, 0, 0, 0, 0]},
 'emdash3_2_one_cat_cokernel_family_point_paths.lp': {'sha256': '9298717ddbc20c0dd61d13fdca4f719f08758d48a35e4a5950c40aa6c9f37753',
                                                      'counts': [7, 0, 0, 1, 0, 0],
                                                      'wholeViewCounts': {'diagram_family_at_func': 5,
                                                                          'diagram_family_transf': 1,
                                                                          'one_cat_functor_category': 1}},
 'examples/one_cat_cokernel_family_point_paths.lp': {'sha256': '7299b407fe011fa43886468ff73e90c48d4c10c8a29b297f2f2f1a815c4b5ee8',
                                                     'counts': [15, 0, 0, 1, 0, 0],
                                                     'wholeViewCounts': {'diagram_family_at_func': 5,
                                                                         'diagram_family_transf': 1,
                                                                         'one_cat_functor_category': 0}}}

def migrate_selected_record_view(path, original):
    spec = SOURCES.get(path)
    if spec is None:
        return None
    assert hashlib.sha256(original.encode()).hexdigest() == spec['sha256'], path
    result = _profile(original, spec['counts'][:4])
    result = _point_readings(result, spec['counts'][4:])
    for head, expected in spec.get('wholeViewCounts', {}).items():
        corrected = {
            'diagram_family_at_func': 'diagram_oplax_family_at_func',
            'diagram_family_transf': 'diagram_oplax_family_transf',
            'one_cat_functor_category': 'one_cat_oplax_functor_category',
        }[head]
        result, actual = re.subn(r'@' + head + r'\b', '@' + corrected, result)
        assert actual == expected, (path, head, expected, actual)
    declarations = r'(?m)^(?:(?:protected|injective|constant) )?symbol\s+(\w+)'
    assert re.findall(declarations, original) == re.findall(declarations, result)
    assertions = r'(?m)^(assert(?:not)?)\b'
    assert re.findall(assertions, original) == re.findall(assertions, result)
    return result
