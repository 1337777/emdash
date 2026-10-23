"""Source-pinned original product/coimage/additive-family continuation.

The emitted source and complete original reviewers own qualification.
Retain the original structural biproduct adjunction and its two clauses.
"""
import hashlib
import re

from production_diagram_observation_migration import _atom, _point_readings

SOURCES = {'emdash3_2_one_cat_additive_families.lp': {'counts': {'fapp0': 0,
                                                       'functorCarrier': 0,
                                                       'functorCategory': 0,
                                                       'initialOp': 2,
                                                       'tapp0_fapp0': 0,
                                                       'transforCarrier': 0},
                                            'sha256': 'a22fab7560b045801a435bc154277c9dea14986f6c1e6c8fd51bf8152a92803e',
                                            'wholeViews': {'diagram_evaluation_at_func': 0,
                                                           'diagram_evaluation_transf': 0,
                                                           'diagram_family_at_func': 0,
                                                           'diagram_family_transf': 0,
                                                           'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_additive_family_paths.lp': {'counts': {'fapp0': 0,
                                                           'functorCarrier': 0,
                                                           'functorCategory': 0,
                                                           'initialOp': 2,
                                                           'tapp0_fapp0': 0,
                                                           'transforCarrier': 0},
                                                'sha256': '41a27cc01e344a82f07e8b9af96da9bf9d54d8d0e8f3a054793ab742b55e0ab1',
                                                'wholeViews': {'diagram_evaluation_at_func': 0,
                                                               'diagram_evaluation_transf': 0,
                                                               'diagram_family_at_func': 0,
                                                               'diagram_family_transf': 0,
                                                               'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_biproduct_adjunction.lp': {'counts': {'fapp0': 0,
                                                          'functorCarrier': 0,
                                                          'functorCategory': 0,
                                                          'initialOp': 1,
                                                          'tapp0_fapp0': 0,
                                                          'transforCarrier': 0},
                                               'sha256': '3965bbe8787f6825bfc3e576c08ac7f6cd854f870a8aad9f9f0c36e4303fb4c1',
                                               'wholeViews': {'diagram_evaluation_at_func': 0,
                                                              'diagram_evaluation_transf': 0,
                                                              'diagram_family_at_func': 0,
                                                              'diagram_family_transf': 0,
                                                              'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_biproduct_injections.lp': {'counts': {'fapp0': 0,
                                                          'functorCarrier': 0,
                                                          'functorCategory': 0,
                                                          'initialOp': 2,
                                                          'tapp0_fapp0': 0,
                                                          'transforCarrier': 0},
                                               'sha256': '148df5e17e6102ffedcb267911c1184e88018a783c1bf2aeb44c989cfe48548b',
                                               'wholeViews': {'diagram_evaluation_at_func': 0,
                                                              'diagram_evaluation_transf': 0,
                                                              'diagram_family_at_func': 0,
                                                              'diagram_family_transf': 0,
                                                              'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_coimage_cover_descent.lp': {'counts': {'fapp0': 0,
                                                           'functorCarrier': 0,
                                                           'functorCategory': 176,
                                                           'initialOp': 9,
                                                           'tapp0_fapp0': 0,
                                                           'transforCarrier': 0},
                                                'sha256': 'd6dd63e26874bdd22e09540d4e97fa1ca09b867f2f96d24f87e85e8b714cc4a0',
                                                'wholeViews': {'diagram_evaluation_at_func': 37,
                                                               'diagram_evaluation_transf': 1,
                                                               'diagram_family_at_func': 113,
                                                               'diagram_family_transf': 16,
                                                               'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_copair_families.lp': {'counts': {'fapp0': 0,
                                                     'functorCarrier': 0,
                                                     'functorCategory': 0,
                                                     'initialOp': 4,
                                                     'tapp0_fapp0': 0,
                                                     'transforCarrier': 0},
                                          'sha256': '97312ad0a5b5d08204947bb96776d71680ecc36f333740ac6c7e0ccc2e30dd1e',
                                          'wholeViews': {'diagram_evaluation_at_func': 0,
                                                         'diagram_evaluation_transf': 0,
                                                         'diagram_family_at_func': 0,
                                                         'diagram_family_transf': 0,
                                                         'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_copair_family_paths.lp': {'counts': {'fapp0': 0,
                                                         'functorCarrier': 0,
                                                         'functorCategory': 0,
                                                         'initialOp': 2,
                                                         'tapp0_fapp0': 0,
                                                         'transforCarrier': 0},
                                              'sha256': 'cf62d8f8d827aaff51c8dc4bb8985a3d51b1d09ee05d6f8257cdd387593f6e1e',
                                              'wholeViews': {'diagram_evaluation_at_func': 0,
                                                             'diagram_evaluation_transf': 0,
                                                             'diagram_family_at_func': 0,
                                                             'diagram_family_transf': 0,
                                                             'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_native_homology_window_maps.lp': {'counts': {'fapp0': 0,
                                                                 'functorCarrier': 0,
                                                                 'functorCategory': 4,
                                                                 'initialOp': 6,
                                                                 'tapp0_fapp0': 0,
                                                                 'transforCarrier': 0},
                                                      'sha256': 'bb26ab2b4a21b47bc79d0ef806b35d1837d0d48e1b336fdafc7ca6848e679ee5',
                                                      'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                     'diagram_evaluation_transf': 0,
                                                                     'diagram_family_at_func': 0,
                                                                     'diagram_family_transf': 0,
                                                                     'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_product_family_inverse_components.lp': {'counts': {'fapp0': 0,
                                                                       'functorCarrier': 0,
                                                                       'functorCategory': 0,
                                                                       'initialOp': 0,
                                                                       'tapp0_fapp0': 0,
                                                                       'transforCarrier': 0},
                                                            'sha256': '384fbe2d68f53c98f4458cda398841d0e79524bec6501a8e3faf9c1e3be22906',
                                                            'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                           'diagram_evaluation_transf': 0,
                                                                           'diagram_family_at_func': 0,
                                                                           'diagram_family_transf': 0,
                                                                           'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_product_family_projection_paths.lp': {'counts': {'fapp0': 0,
                                                                     'functorCarrier': 0,
                                                                     'functorCategory': 0,
                                                                     'initialOp': 0,
                                                                     'tapp0_fapp0': 0,
                                                                     'transforCarrier': 0},
                                                          'sha256': '3df9d3eb9f17704a0cb871747ad570d2d0295dc58782097ca5166f3b51ca8449',
                                                          'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                         'diagram_evaluation_transf': 0,
                                                                         'diagram_family_at_func': 0,
                                                                         'diagram_family_transf': 0,
                                                                         'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_zero_cokernel_covers.lp': {'counts': {'fapp0': 0,
                                                          'functorCarrier': 0,
                                                          'functorCategory': 104,
                                                          'initialOp': 5,
                                                          'tapp0_fapp0': 0,
                                                          'transforCarrier': 0},
                                               'sha256': '98b37e3857228aa757bd7497ee96e43173dfc0467ffad9663cd8814d7d4350d2',
                                               'wholeViews': {'diagram_evaluation_at_func': 15,
                                                              'diagram_evaluation_transf': 0,
                                                              'diagram_family_at_func': 37,
                                                              'diagram_family_transf': 9,
                                                              'one_cat_functor_category': 0}},
 'examples/one_cat_additive_families.lp': {'counts': {'fapp0': 0,
                                                      'functorCarrier': 0,
                                                      'functorCategory': 0,
                                                      'initialOp': 5,
                                                      'tapp0_fapp0': 0,
                                                      'transforCarrier': 0},
                                           'sha256': 'c75591e95ca37b6aecbadfcfd4a39afccdd8174108b605e880fe2a95e5fb6f5c',
                                           'wholeViews': {'diagram_evaluation_at_func': 0,
                                                          'diagram_evaluation_transf': 0,
                                                          'diagram_family_at_func': 0,
                                                          'diagram_family_transf': 0,
                                                          'one_cat_functor_category': 0}},
 'examples/one_cat_biproduct_adjunction.lp': {'counts': {'fapp0': 0,
                                                         'functorCarrier': 0,
                                                         'functorCategory': 0,
                                                         'initialOp': 4,
                                                         'tapp0_fapp0': 0,
                                                         'transforCarrier': 0},
                                              'sha256': '95ec9557ec30a9b1e018d474e02d1b07c53dbc260115bbeca222b9f5f12e1842',
                                              'wholeViews': {'diagram_evaluation_at_func': 0,
                                                             'diagram_evaluation_transf': 0,
                                                             'diagram_family_at_func': 0,
                                                             'diagram_family_transf': 0,
                                                             'one_cat_functor_category': 0}},
 'examples/one_cat_coimage_cover_descent.lp': {'counts': {'fapp0': 0,
                                                          'functorCarrier': 0,
                                                          'functorCategory': 29,
                                                          'initialOp': 5,
                                                          'tapp0_fapp0': 0,
                                                          'transforCarrier': 0},
                                               'sha256': '1e43439cc5eaac5095664d31775c31ee4e3b804f7a508f132158eadf7aa00b65',
                                               'wholeViews': {'diagram_evaluation_at_func': 6,
                                                              'diagram_evaluation_transf': 0,
                                                              'diagram_family_at_func': 36,
                                                              'diagram_family_transf': 6,
                                                              'one_cat_functor_category': 0}},
 'examples/one_cat_copair_families.lp': {'counts': {'fapp0': 0,
                                                    'functorCarrier': 0,
                                                    'functorCategory': 0,
                                                    'initialOp': 17,
                                                    'tapp0_fapp0': 0,
                                                    'transforCarrier': 0},
                                         'sha256': '7fef7be05453ba07509647cdec8ea08131c58d6ffeb10f3c0a9b8b6464a7a93f',
                                         'wholeViews': {'diagram_evaluation_at_func': 0,
                                                        'diagram_evaluation_transf': 0,
                                                        'diagram_family_at_func': 0,
                                                        'diagram_family_transf': 0,
                                                        'one_cat_functor_category': 0}},
 'examples/one_cat_native_homology_window_maps.lp': {'counts': {'fapp0': 0,
                                                                'functorCarrier': 0,
                                                                'functorCategory': 0,
                                                                'initialOp': 11,
                                                                'tapp0_fapp0': 0,
                                                                'transforCarrier': 0},
                                                     'sha256': 'b9c81e8aa824fa9b123e6d2ac565b5e987968be5a8ca939ec1e3d26923021ddb',
                                                     'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                    'diagram_evaluation_transf': 0,
                                                                    'diagram_family_at_func': 0,
                                                                    'diagram_family_transf': 0,
                                                                    'one_cat_functor_category': 0}},
 'examples/one_cat_product_family_inverse_components.lp': {'counts': {'fapp0': 0,
                                                                      'functorCarrier': 0,
                                                                      'functorCategory': 0,
                                                                      'initialOp': 0,
                                                                      'tapp0_fapp0': 0,
                                                                      'transforCarrier': 0},
                                                           'sha256': '5494bcf15fc60a0254fd25f5344410ca95db9f73be5ddb2e2177aa7836567bdb',
                                                           'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                          'diagram_evaluation_transf': 0,
                                                                          'diagram_family_at_func': 0,
                                                                          'diagram_family_transf': 0,
                                                                          'one_cat_functor_category': 0}},
 'examples/one_cat_zero_cokernel_covers.lp': {'counts': {'fapp0': 0,
                                                         'functorCarrier': 0,
                                                         'functorCategory': 53,
                                                         'initialOp': 8,
                                                         'tapp0_fapp0': 0,
                                                         'transforCarrier': 0},
                                              'sha256': 'cda0fd1de7433884525104eeba666351316271cee01a429009dcb7e820c916d7',
                                              'wholeViews': {'diagram_evaluation_at_func': 9,
                                                             'diagram_evaluation_transf': 0,
                                                             'diagram_family_at_func': 48,
                                                             'diagram_family_transf': 3,
                                                             'one_cat_functor_category': 0}}}

def migrate_kernel_additive_prerequisite(name, original):
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
    if name == 'emdash3_2_one_cat_product_family_projection_paths.lp':
        # Expose diagonal endpoint pairs through direct composition, while
        # retaining the selected product functor's postcomposition owners.
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
            if ' '.join(inner[-1].split()) != '(@product_diagonal_func C)':
                continue
            edits.append((match.start(), cursor, '@comp_cat_fapp0 ' + ' '.join(inner + [args[3]])))
        assert len(edits) == 50
        assert all(a[1] <= b[0] for a,b in zip(edits, edits[1:]))
        for start, end, replacement in reversed(edits):
            text = text[:start] + replacement + text[end:]
    if name == 'emdash3_2_one_cat_coimage_cover_descent.lp':
        # Oplax diagram families have ordinary whole shape action. Use its
        # native computation at the original quotient/factor proof steps.
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
        marker = 'symbol one_cat_coimage_family_quotient_path'
        start = text.index(marker)
        end = text.index(';', start)
        declaration = text[start:end]
        signature, old_body = declaration.split('≔', 1)
        assert old_body.strip().startswith('@one_cat_diagram_family_transf_reindex_path')
        body = '''@eq_refl
    (@Transf B C
      (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src)
      (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C
        (@adjunction_coimage_func C S t T T0 P Q) D))
    (@cokernel_adjunction_family_projection_transf B C S t T0 Q
      (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C)
        (Functor_oplax_cat WalkingArrow_cat C)
        (@kernel_adjunction_arrow_func C S t T P) D))'''
        text = text[:start] + signature + '≔ ' + body + text[end:]
    declarations = r'(?m)^(?:(?:protected|injective|constant) )?symbol\s+(\w+)'
    assertions = r'(?m)^(assert(?:not)?)\b'
    assert re.findall(declarations, original) == re.findall(declarations, text), name
    assert re.findall(assertions, original) == re.findall(assertions, text), name
    return text
