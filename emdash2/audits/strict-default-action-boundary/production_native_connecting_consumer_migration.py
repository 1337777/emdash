"""Source-pinned migration of original native connecting consumers.

Whole original owners and reviewers own qualification. Preserve selected
maps/inverses and hypotheses; no new formal rule or operational primitive.
"""
import hashlib
import re

from production_diagram_observation_migration import _atom, _point_readings

SOURCES = {'emdash3_2_one_cat_covered_middle_cycles.lp': {'counts': {'fapp0': 0,
                                                           'functorCarrier': 0,
                                                           'functorCategory': 0,
                                                           'initialOp': 3,
                                                           'tapp0_fapp0': 0,
                                                           'transforCarrier': 0},
                                                'sha256': '58bf9a9b1c714099750e21491d3fe8f0514b78f30506e953e37114dfa1fb32b2',
                                                'wholeViews': {'diagram_evaluation_at_func': 0,
                                                               'diagram_evaluation_transf': 0,
                                                               'diagram_family_at_func': 0,
                                                               'diagram_family_transf': 0,
                                                               'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_image_kernel_comparison.lp': {'counts': {'fapp0': 0,
                                                             'functorCarrier': 0,
                                                             'functorCategory': 219,
                                                             'initialOp': 6,
                                                             'tapp0_fapp0': 0,
                                                             'transforCarrier': 0},
                                                  'sha256': 'd0a099b7efe9e9b13e57b06d9c568648fa2b9359ea0345a54bad65ff0f9f4782',
                                                  'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                 'diagram_evaluation_transf': 0,
                                                                 'diagram_family_at_func': 0,
                                                                 'diagram_family_transf': 0,
                                                                 'one_cat_functor_category': 5}},
 'emdash3_2_one_cat_native_connecting.lp': {'counts': {'fapp0': 0,
                                                       'functorCarrier': 0,
                                                       'functorCategory': 0,
                                                       'initialOp': 6,
                                                       'tapp0_fapp0': 0,
                                                       'transforCarrier': 0},
                                            'sha256': 'b412788007bbb5498e1606d41c79b4c696fac42f127e1cffc938aab7ba4b73d6',
                                            'wholeViews': {'diagram_evaluation_at_func': 0,
                                                           'diagram_evaluation_transf': 0,
                                                           'diagram_family_at_func': 0,
                                                           'diagram_family_transf': 0,
                                                           'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_native_connecting_projection_zero.lp': {'counts': {'fapp0': 0,
                                                                       'functorCarrier': 0,
                                                                       'functorCategory': 0,
                                                                       'initialOp': 7,
                                                                       'tapp0_fapp0': 0,
                                                                       'transforCarrier': 0},
                                                            'sha256': '14e793ad0bb5cda9744e0a508b3838bd894f94bd1494a6275620d155897cddfd',
                                                            'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                           'diagram_evaluation_transf': 0,
                                                                           'diagram_family_at_func': 0,
                                                                           'diagram_family_transf': 1,
                                                                           'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_native_connecting_upper_lifts.lp': {'counts': {'fapp0': 0,
                                                                   'functorCarrier': 0,
                                                                   'functorCategory': 0,
                                                                   'initialOp': 7,
                                                                   'tapp0_fapp0': 0,
                                                                   'transforCarrier': 0},
                                                        'sha256': 'bab0e59780ec3c35c541e52ab952150714b50d530ea9ca4b5846b57b6250152a',
                                                        'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                       'diagram_evaluation_transf': 0,
                                                                       'diagram_family_at_func': 0,
                                                                       'diagram_family_transf': 1,
                                                                       'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_native_cycles_connecting.lp': {'counts': {'fapp0': 0,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 0,
                                                              'initialOp': 3,
                                                              'tapp0_fapp0': 0,
                                                              'transforCarrier': 0},
                                                   'sha256': '66a586f864ab6e211078e50a7b318c88092b8d1252b97903447f8ecb2b0dedb4',
                                                   'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                  'diagram_evaluation_transf': 0,
                                                                  'diagram_family_at_func': 0,
                                                                  'diagram_family_transf': 0,
                                                                  'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_row_homology_zero_pairs.lp': {'counts': {'fapp0': 0,
                                                             'functorCarrier': 0,
                                                             'functorCategory': 3,
                                                             'initialOp': 4,
                                                             'tapp0_fapp0': 0,
                                                             'transforCarrier': 0},
                                                  'sha256': '49200c0e2e3b642419c33b4aad93b0f82de820fe745eaffa6f8a211024c2bf9d',
                                                  'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                 'diagram_evaluation_transf': 0,
                                                                 'diagram_family_at_func': 0,
                                                                 'diagram_family_transf': 0,
                                                                 'one_cat_functor_category': 0}},
 'examples/one_cat_image_kernel_comparison.lp': {'counts': {'fapp0': 0,
                                                            'functorCarrier': 0,
                                                            'functorCategory': 142,
                                                            'initialOp': 10,
                                                            'tapp0_fapp0': 0,
                                                            'transforCarrier': 0},
                                                 'sha256': 'd1509545c6fa6a6b9b39eb8ea249f391ec58d9e1dc10e0331db0ce201f6103d8',
                                                 'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                'diagram_evaluation_transf': 0,
                                                                'diagram_family_at_func': 0,
                                                                'diagram_family_transf': 0,
                                                                'one_cat_functor_category': 3}},
 'examples/one_cat_native_connecting.lp': {'counts': {'fapp0': 0,
                                                      'functorCarrier': 0,
                                                      'functorCategory': 0,
                                                      'initialOp': 5,
                                                      'tapp0_fapp0': 0,
                                                      'transforCarrier': 0},
                                           'sha256': 'b16b63d3d82c04f775d4294dabe4164773e5ed0dad58b3d8a9aa702070e04aaa',
                                           'wholeViews': {'diagram_evaluation_at_func': 0,
                                                          'diagram_evaluation_transf': 0,
                                                          'diagram_family_at_func': 0,
                                                          'diagram_family_transf': 0,
                                                          'one_cat_functor_category': 0}}}

def migrate_native_connecting_consumer(name, original):
    if name not in SOURCES:
        return None
    spec = SOURCES[name]
    assert hashlib.sha256(original.encode()).hexdigest() == spec['sha256']
    text = original
    for pattern, replacement, key in (
        (r'\bFunctor_cat(?=\s+WalkingArrow_cat\s+C\b)', 'Functor_oplax_cat', 'functorCategory'),
        (r'\(Functor\s+WalkingArrow_cat\s+C\s*\)', '(Obj (Functor_oplax_cat WalkingArrow_cat C))', 'functorCarrier'),
        (r'@Transf\s+WalkingArrow_cat\s+C\b', '@Hom (Functor_oplax_cat WalkingArrow_cat C)', 'transforCarrier'),
        (r'\bOp_cat(?=\s+C\b)', 'TotalOp_cat', 'initialOp'),
    ):
        text, count = re.subn(pattern, replacement, text)
        assert count == spec['counts'][key], (name, key, count)
    text = _point_readings(text, (spec['counts']['fapp0'], spec['counts']['tapp0_fapp0']))
    for head, arity, corrected in (
        ('diagram_family_at_func', 3, 'diagram_oplax_family_at_func'),
        ('diagram_family_transf', 3, 'diagram_oplax_family_transf'),
        ('diagram_evaluation_at_func', 2, 'diagram_oplax_evaluation_at_func'),
        ('diagram_evaluation_transf', 2, 'diagram_oplax_evaluation_transf'),
        ('one_cat_functor_category', 2, 'one_cat_oplax_functor_category'),
    ):
        edits = []
        for match in re.finditer(r'@' + head + r'\b', text):
            cursor, args = match.end(), []
            for _ in range(arity):
                value, cursor = _atom(text, cursor)
                args.append(value)
            if head == 'one_cat_functor_category' and args != ['WalkingArrow_cat', 'C']:
                continue
            assert args[-2:] == ['WalkingArrow_cat', 'C'], (name, head, args)
            edits.append((match.start(), match.end()))
        assert len(edits) == spec['wholeViews'][head], (name, head)
        for start, end in reversed(edits):
            text = text[:start] + '@' + corrected + text[end:]
    if name in ('emdash3_2_one_cat_image_kernel_comparison.lp',
                'examples/one_cat_image_kernel_comparison.lp'):
        reviewer = name.startswith('examples/')
        if reviewer:
            body = text
            head, arity, skip = 'one_cat_cokernel_family_input', 10, 6
        else:
            start = text.index('symbol one_cat_coimage_to_kernel_transf')
            end = text.index(';', start)
            body = text[start:end].split('≔', 1)[1]
            head, arity, skip = 'one_cat_cokernel_family_descent', 12, 8
        match = re.search(r'@' + head + r'\b', body)
        assert match
        cursor, args = match.end(), []
        for _ in range(arity):
            value, cursor = _atom(body, cursor)
            args.append(value)
        expected = ['B','C','C1','t','T','T0'] if reviewer else ['B','C','S','C1','t','T','T0','Q']
        assert args[:skip] == expected
        diagram, target, boundary, proof = args[skip:]
        assert proof.startswith('(@one_cat_boundary_kills_incoming_kernel_path ')
        source = '(@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P) (@zero_arrow_family_incoming_func B C t T A D h))'
        native_source = f'(@diagram_oplax_family_at_func B WalkingArrow_cat C {diagram} walking_arrow_src)'
        native_middle = f'(@diagram_oplax_family_at_func B WalkingArrow_cat C {diagram} walking_arrow_tgt)'
        kappa = f'(@diagram_oplax_family_transf B WalkingArrow_cat C {diagram} walking_arrow_src walking_arrow_tgt walking_arrow_generator)'
        lhs = f'(@comp_fapp0 (Functor_cat B C) {native_source} {native_middle} {target} {boundary} {kappa})'
        zero = f'(@zero_arrow_family_zero_transf B C t T T0 {native_source} {target})'
        original_lhs = f'(@comp_fapp0 (Functor_cat B C) {source} A {target} {boundary} {kappa})'
        original_zero = f'(@zero_arrow_family_zero_transf B C t T T0 {source} {target})'
        point = f'(Hom C (@fapp0 B C {source} b) (@fapp0 B C {target} b))'
        replacement = f'''(@hom_to_path (@Transf_cat B C {native_source} {target})
          ((@one_cat_functor_category B C C1) {native_source} {target})
          {lhs} {zero}
          (@one_cat_modification B C C1 {native_source} {target} {lhs} {zero}
            (λ b : τ (Obj B),
              @path_to_hom (Hom_cat C (@fapp0 B C {native_source} b) (@fapp0 B C {target} b))
                (@tapp0_fapp0 B C {native_source} {target} b {lhs})
                (@tapp0_fapp0 B C {native_source} {target} b {zero})
                (@eq_ap (@Transf B C {source} {target}) {point}
                  (λ a : τ (@Transf B C {source} {target}), @tapp0_fapp0 B C {source} {target} b a)
                  {original_lhs} {original_zero} {proof}))))'''
        # The same derived zero proof must feed descent and reconstruction.
        pattern = (r'\(@one_cat_boundary_kills_incoming_kernel_path\s+B\s+C\s+S\s+C1'
                   r'\s+t\s+T\s+T0\s+P\s+A\s+D\s+h\)')
        text, count = re.subn(pattern, lambda _: replacement, text)
        assert count == (1 if reviewer else 2)
        edits = []
        for match in re.finditer(r'@sym_transf_tapp0_transf\b', text):
            cursor, args = match.end(), []
            for _ in range(3):
                value, cursor = _atom(text, cursor)
                args.append(value)
            assert args == ['B', 'WalkingArrow_cat', 'C']
            edits.append((match.start(), match.end()))
        assert len(edits) == (1 if reviewer else 5)
        for lo, hi in reversed(edits):
            text = text[:lo] + '@diagram_oplax_family_map_at' + text[hi:]
    declarations = r'(?m)^(?:(?:protected|injective|constant) )?symbol\s+(\w+)'
    assertions = r'(?m)^(assert(?:not)?)\b'
    assert re.findall(declarations, original) == re.findall(declarations, text), name
    assert re.findall(assertions, original) == re.findall(assertions, text), name
    return text
