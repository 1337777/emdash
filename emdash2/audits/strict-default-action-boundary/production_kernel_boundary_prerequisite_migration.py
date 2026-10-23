"""Source-pinned migration of original connecting-kernel prerequisites.

Qualification belongs to the emitted original owners and complete reviewers.
No new formal rules: retain the two original product-adjunction clauses.
"""
import hashlib
import re

from production_diagram_observation_migration import _atom, _point_readings

SOURCES = {'emdash3_2_additive_shears.lp': {'counts': {'fapp0': 0,
                                             'functorCarrier': 0,
                                             'functorCategory': 0,
                                             'initialOp': 0,
                                             'tapp0_fapp0': 0,
                                             'transforCarrier': 0},
                                  'sha256': '12f99fc31ce7f840632515c87c7fa0b584ff9bb25a7773f323888561c314e36d',
                                  'wholeViews': {'diagram_evaluation_at_func': 0,
                                                 'diagram_evaluation_transf': 0,
                                                 'diagram_family_at_func': 0,
                                                 'diagram_family_transf': 0,
                                                 'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_adjunction_normality.lp': {'counts': {'fapp0': 0,
                                                          'functorCarrier': 0,
                                                          'functorCategory': 13,
                                                          'initialOp': 4,
                                                          'tapp0_fapp0': 0,
                                                          'transforCarrier': 0},
                                               'sha256': 'd852520e82fcb36cb680dc94a1a57b53e6990ef8a00af174c5515a84efa9ba33',
                                               'wholeViews': {'diagram_evaluation_at_func': 0,
                                                              'diagram_evaluation_transf': 0,
                                                              'diagram_family_at_func': 0,
                                                              'diagram_family_transf': 0,
                                                              'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_coimage_factor_paths.lp': {'counts': {'fapp0': 0,
                                                          'functorCarrier': 0,
                                                          'functorCategory': 77,
                                                          'initialOp': 5,
                                                          'tapp0_fapp0': 0,
                                                          'transforCarrier': 0},
                                               'sha256': '24a96a1b6cc3474d607c63f48cc91f64df124078198464cc8bb2eb14edf86cbc',
                                               'wholeViews': {'diagram_evaluation_at_func': 40,
                                                              'diagram_evaluation_transf': 2,
                                                              'diagram_family_at_func': 0,
                                                              'diagram_family_transf': 0,
                                                              'one_cat_functor_category': 3}},
 'emdash3_2_one_cat_cokernel_family_annihilation.lp': {'counts': {'fapp0': 0,
                                                                  'functorCarrier': 0,
                                                                  'functorCategory': 28,
                                                                  'initialOp': 2,
                                                                  'tapp0_fapp0': 0,
                                                                  'transforCarrier': 0},
                                                       'sha256': '48cadf01b4a62de0db6d4df953d0556d5774f3efbe359edbb977cce407292800',
                                                       'wholeViews': {'diagram_evaluation_at_func': 9,
                                                                      'diagram_evaluation_transf': 2,
                                                                      'diagram_family_at_func': 24,
                                                                      'diagram_family_transf': 7,
                                                                      'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_homology_covered_maps.lp': {'counts': {'fapp0': 0,
                                                           'functorCarrier': 0,
                                                           'functorCategory': 0,
                                                           'initialOp': 7,
                                                           'tapp0_fapp0': 0,
                                                           'transforCarrier': 0},
                                                'sha256': '05abb9b01b23e70ebf7cecc9cba4dd34ab653d64291f0f547555e5058a5f39a0',
                                                'wholeViews': {'diagram_evaluation_at_func': 0,
                                                               'diagram_evaluation_transf': 0,
                                                               'diagram_family_at_func': 0,
                                                               'diagram_family_transf': 0,
                                                               'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_image_coimage_comparison.lp': {'counts': {'fapp0': 0,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 576,
                                                              'initialOp': 8,
                                                              'tapp0_fapp0': 0,
                                                              'transforCarrier': 0},
                                                   'sha256': 'a0ea7f11ae5e52d048d62ecab9193a139dac529e79e70228523e4f27ba0af247',
                                                   'wholeViews': {'diagram_evaluation_at_func': 81,
                                                                  'diagram_evaluation_transf': 10,
                                                                  'diagram_family_at_func': 0,
                                                                  'diagram_family_transf': 16,
                                                                  'one_cat_functor_category': 24}},
 'emdash3_2_one_cat_kernel_input_boundaries.lp': {'counts': {'fapp0': 0,
                                                             'functorCarrier': 0,
                                                             'functorCategory': 1,
                                                             'initialOp': 1,
                                                             'tapp0_fapp0': 0,
                                                             'transforCarrier': 0},
                                                  'sha256': '02d46f1e21d6c62abf55bb18eece8d3215735776fe0b8082034dae164ad83edf',
                                                  'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                 'diagram_evaluation_transf': 0,
                                                                 'diagram_family_at_func': 7,
                                                                 'diagram_family_transf': 1,
                                                                 'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_product_adjunction.lp': {'counts': {'fapp0': 0,
                                                        'functorCarrier': 0,
                                                        'functorCategory': 0,
                                                        'initialOp': 0,
                                                        'tapp0_fapp0': 0,
                                                        'transforCarrier': 0},
                                             'sha256': '43144f1c5726524ad099d025c6077df1a99597d5a6da607d6afa0602bcea1cac',
                                             'wholeViews': {'diagram_evaluation_at_func': 0,
                                                            'diagram_evaluation_transf': 0,
                                                            'diagram_family_at_func': 0,
                                                            'diagram_family_transf': 0,
                                                            'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_product_families.lp': {'counts': {'fapp0': 0,
                                                      'functorCarrier': 0,
                                                      'functorCategory': 0,
                                                      'initialOp': 0,
                                                      'tapp0_fapp0': 0,
                                                      'transforCarrier': 0},
                                           'sha256': '8bb80b35581b8f2822c2f82523011fcbb2fa3954fc6058556bd78d92938e5ec3',
                                           'wholeViews': {'diagram_evaluation_at_func': 0,
                                                          'diagram_evaluation_transf': 0,
                                                          'diagram_family_at_func': 0,
                                                          'diagram_family_transf': 0,
                                                          'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_short_exact_family_lifts.lp': {'counts': {'fapp0': 0,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 27,
                                                              'initialOp': 5,
                                                              'tapp0_fapp0': 0,
                                                              'transforCarrier': 0},
                                                   'sha256': 'e5625230f7ec43363bb79eb631735d152ff670f9e23e259743018e1ec409f3f2',
                                                   'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                  'diagram_evaluation_transf': 0,
                                                                  'diagram_family_at_func': 45,
                                                                  'diagram_family_transf': 3,
                                                                  'one_cat_functor_category': 1}},
 'emdash3_2_one_cat_zero_kernel_families.lp': {'counts': {'fapp0': 0,
                                                          'functorCarrier': 0,
                                                          'functorCategory': 32,
                                                          'initialOp': 4,
                                                          'tapp0_fapp0': 0,
                                                          'transforCarrier': 0},
                                               'sha256': '81b59dad0763af44839bb09b84994038fb4f5d86d8ea6bb08b874e85fd829c49',
                                               'wholeViews': {'diagram_evaluation_at_func': 0,
                                                              'diagram_evaluation_transf': 0,
                                                              'diagram_family_at_func': 50,
                                                              'diagram_family_transf': 4,
                                                              'one_cat_functor_category': 0}},
 'emdash3_2_preadditive_zero_family_components.lp': {'counts': {'fapp0': 0,
                                                                'functorCarrier': 0,
                                                                'functorCategory': 5,
                                                                'initialOp': 1,
                                                                'tapp0_fapp0': 0,
                                                                'transforCarrier': 0},
                                                     'sha256': '83557c01bd19559dbd4128380d9588eb40a87def9870a7785bf34ddb4664a135',
                                                     'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                    'diagram_evaluation_transf': 0,
                                                                    'diagram_family_at_func': 0,
                                                                    'diagram_family_transf': 5,
                                                                    'one_cat_functor_category': 0}},
 'emdash3_2_product_composition_paths.lp': {'counts': {'fapp0': 0,
                                                       'functorCarrier': 0,
                                                       'functorCategory': 0,
                                                       'initialOp': 0,
                                                       'tapp0_fapp0': 0,
                                                       'transforCarrier': 0},
                                            'sha256': '48ca940dfe579b57b8b7be71d78a7ab176e4a81023c46d342ed1db4ccd6c9555',
                                            'wholeViews': {'diagram_evaluation_at_func': 0,
                                                           'diagram_evaluation_transf': 0,
                                                           'diagram_family_at_func': 0,
                                                           'diagram_family_transf': 0,
                                                           'one_cat_functor_category': 0}},
 'emdash3_2_product_family_maps.lp': {'counts': {'fapp0': 0,
                                                 'functorCarrier': 0,
                                                 'functorCategory': 0,
                                                 'initialOp': 0,
                                                 'tapp0_fapp0': 0,
                                                 'transforCarrier': 0},
                                      'sha256': '26a2becbdab305b1a6ade2a7c58e157674f8439f3c1e16013f114b320144dd8f',
                                      'wholeViews': {'diagram_evaluation_at_func': 0,
                                                     'diagram_evaluation_transf': 0,
                                                     'diagram_family_at_func': 0,
                                                     'diagram_family_transf': 0,
                                                     'one_cat_functor_category': 0}},
 'emdash3_2_product_family_tuple_paths.lp': {'counts': {'fapp0': 0,
                                                        'functorCarrier': 0,
                                                        'functorCategory': 0,
                                                        'initialOp': 0,
                                                        'tapp0_fapp0': 0,
                                                        'transforCarrier': 0},
                                             'sha256': '6d630e6937a1ca494e7ce1318ce71ada8e58c1ab20eb4ffaab96144b4835db0e',
                                             'wholeViews': {'diagram_evaluation_at_func': 0,
                                                            'diagram_evaluation_transf': 0,
                                                            'diagram_family_at_func': 0,
                                                            'diagram_family_transf': 0,
                                                            'one_cat_functor_category': 0}},
 'examples/one_cat_adjunction_normality.lp': {'counts': {'fapp0': 0,
                                                         'functorCarrier': 2,
                                                         'functorCategory': 83,
                                                         'initialOp': 12,
                                                         'tapp0_fapp0': 0,
                                                         'transforCarrier': 0},
                                              'sha256': 'b9aebe08e32cb8a41154a58043f191b5142068f119bf81b74203918886c41647',
                                              'wholeViews': {'diagram_evaluation_at_func': 0,
                                                             'diagram_evaluation_transf': 0,
                                                             'diagram_family_at_func': 0,
                                                             'diagram_family_transf': 0,
                                                             'one_cat_functor_category': 0}},
 'examples/one_cat_image_coimage_comparison.lp': {'counts': {'fapp0': 8,
                                                             'functorCarrier': 6,
                                                             'functorCategory': 206,
                                                             'initialOp': 14,
                                                             'tapp0_fapp0': 0,
                                                             'transforCarrier': 2},
                                                  'sha256': '119a5a78be520458961b8e8bc7fab59687fa4105599091355712730b387f0fd0',
                                                  'wholeViews': {'diagram_evaluation_at_func': 27,
                                                                 'diagram_evaluation_transf': 7,
                                                                 'diagram_family_at_func': 0,
                                                                 'diagram_family_transf': 0,
                                                                 'one_cat_functor_category': 3}},
 'examples/one_cat_product_families.lp': {'counts': {'fapp0': 0,
                                                     'functorCarrier': 0,
                                                     'functorCategory': 0,
                                                     'initialOp': 0,
                                                     'tapp0_fapp0': 0,
                                                     'transforCarrier': 0},
                                          'sha256': '66ad98c174b0a3a72c7286c88d90a7e4349c310f63bfd2c7a782f3110921347b',
                                          'wholeViews': {'diagram_evaluation_at_func': 0,
                                                         'diagram_evaluation_transf': 0,
                                                         'diagram_family_at_func': 0,
                                                         'diagram_family_transf': 0,
                                                         'one_cat_functor_category': 0}},
 'examples/one_cat_short_exact_family_lifts.lp': {'counts': {'fapp0': 0,
                                                             'functorCarrier': 0,
                                                             'functorCategory': 66,
                                                             'initialOp': 8,
                                                             'tapp0_fapp0': 0,
                                                             'transforCarrier': 0},
                                                  'sha256': '5210332de3c85db675893200b7639633b6e31de3a0ed59c8b145e9c0e7be85a8',
                                                  'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                 'diagram_evaluation_transf': 0,
                                                                 'diagram_family_at_func': 27,
                                                                 'diagram_family_transf': 5,
                                                                 'one_cat_functor_category': 0}}}

def migrate_kernel_boundary_prerequisite(name, original):
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
    if name == 'emdash3_2_one_cat_cokernel_family_annihilation.lp':
        pattern = (r'@one_cat_diagram_family_transf_whisker_path\s+B\s+WalkingArrow_cat\s+C\s+C1\s+D'
                   r'\s+walking_arrow_src\s+walking_arrow_tgt\s+walking_arrow_generator')
        replacement = '''@eq_refl
    (@Transf B C
      (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src)
      (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt))
    (@diagram_oplax_family_transf B WalkingArrow_cat C D
      walking_arrow_src walking_arrow_tgt walking_arrow_generator)'''
        text, count = re.subn(pattern, replacement, text)
        assert count == 1
    if name in ('emdash3_2_one_cat_image_coimage_comparison.lp',
                'examples/one_cat_image_coimage_comparison.lp'):
        expected = 24 if name.startswith('emdash3_2_') else 1
        edits = []
        for match in re.finditer(r'@sym_transf_tapp0_transf\b', text):
            cursor, args = match.end(), []
            for _ in range(3):
                value, cursor = _atom(text, cursor)
                args.append(value)
            assert args[1:] == ['WalkingArrow_cat', 'C']
            edits.append((match.start(), match.end()))
        assert len(edits) == expected
        for start, end in reversed(edits):
            text = text[:start] + '@diagram_oplax_family_map_at' + text[end:]
    if name == 'emdash3_2_one_cat_image_coimage_comparison.lp':
        # Terminal-diagram endpoint actions use the direct composition
        # presentation of the qualified mate-input/source-observation owners.
        # Retain the selected K/Q postcomposition heads used by native mates.
        edits = []
        for match in re.finditer(r'@fapp0\b', text):
            cursor, args = match.end(), []
            for _ in range(4):
                value, cursor = _atom(text, cursor)
                args.append(value)
            if not re.match(r'\(@comp_cat_cov_func\b', args[2]):
                continue
            owner = args[2]
            index = owner.index('comp_cat_cov_func') + len('comp_cat_cov_func')
            inner = []
            for _ in range(4):
                value, index = _atom(owner, index)
                inner.append(value)
            if ' '.join(inner[-1].split()) != '(@terminal_arrow_diagram_func C t T)':
                continue
            replacement = '@comp_cat_fapp0 ' + ' '.join(inner + [args[3]])
            edits.append((match.start(), cursor, replacement))
        assert len(edits) == 14
        for start, end, replacement in reversed(edits):
            text = text[:start] + replacement + text[end:]
    if name == 'emdash3_2_one_cat_coimage_factor_paths.lp':
        # The existing projection theorem uses raw Hom classifiers, while
        # native inverse mating retains literal Hom endpoints. Reuse their
        # already derived whole comparison before the source observation.
        pattern = r'\(@one_cat_source_to_image_projection_path\s+C\s+S\s+C1\s+t\s+T\s+T0\s+P\s+Q\)'
        replacement = '''(@eq_trans _ _ _ _
    (@eq_sym _ _ _ (@kernel_family_mate_projection_view
      (Functor_oplax_cat WalkingArrow_cat C) C S C1 t T P
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
      (@cokernel_adjunction_arrow_func C S t T0 Q)
      (@one_cat_adjunction_source_to_image C S C1 t T T0 P Q)))
    (@one_cat_source_to_image_projection_path C S C1 t T T0 P Q))'''
        text, count = re.subn(pattern, replacement, text)
        assert count == 1
    if name == 'emdash3_2_one_cat_homology_covered_maps.lp':
        start = text.index('symbol one_cat_native_cover_left_zero')
        end = text.index('symbol one_cat_native_cover_left_cycles', start)
        part = text[start:end]
        matches = []
        for match in re.finditer(r'@eq_ap\b', part):
            cursor, args = match.end(), []
            for _ in range(6):
                value, cursor = _atom(part, cursor)
                args.append(value)
            if args[-1] == 'z':
                matches.append((match.start(), cursor, args))
        assert len(matches) == 1
        lo, hi, args = matches[0]
        # Use the existing whole associativity witness before applying the
        # original chain-law z. No whole nested-associativity inference needed.
        assoc = '''(@comp_assoc (Functor_cat B C)
      (@kernel_precomposition_family_func B C Add t T P
        (@zero_cone_row_family_vertex_func B C t T R0 walking_arrow_src)
        (@zero_cone_right_column_outgoing_func B C t T R0 R1 m0)
        (@zero_cone_row_family_outgoing B C t T R0))
      (@zero_cone_row_family_vertex_func B C t T R0 walking_arrow_src)
      (@zero_cone_row_family_vertex_func B C t T R1 walking_arrow_src)
      (@zero_cone_row_family_vertex_func B C t T R2 walking_arrow_src)
      (@zero_cone_row_family_vertex_map B C t T R1 R2 m1 walking_arrow_src)
      (@zero_cone_row_family_vertex_map B C t T R0 R1 m0 walking_arrow_src)
      (@kernel_precomposition_first_transf B C Add t T P
        (@zero_cone_row_family_vertex_func B C t T R0 walking_arrow_src)
        (@zero_cone_right_column_outgoing_func B C t T R0 R1 m0)
        (@zero_cone_row_family_outgoing B C t T R0)))'''
        replacement = '@eq_trans ' + args[1] + ' _ _ _ ' + assoc + '\n      (' + part[lo:hi] + ')'
        part = part[:lo] + replacement + part[hi:]
        text = text[:start] + part + text[end:]
    declarations = r'(?m)^(?:(?:protected|injective|constant) )?symbol\s+(\w+)'
    assertions = r'(?m)^(assert(?:not)?)\b'
    assert re.findall(declarations, original) == re.findall(declarations, text), name
    assert re.findall(assertions, original) == re.findall(assertions, text), name
    return text
