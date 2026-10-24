"""Source-pinned original native Freyd matching and whole-window consumers.

Retain supplied model/normality, actual inverse data and whole base action.
Only existing constant inclusion and walking-arrow profiles change views.
"""
import hashlib
import re
from production_diagram_observation_migration import _atom

SOURCES = {'emdash3_2_commutative_algebra_freyd_adjunction_model_arrows.lp': {'ambientConstantTransf': 0,
                                                                    'sha256': 'ffce300b55084c127bd440b220dec68feba2e3e9878908cf4bcc7afe881cee50',
                                                                    'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_adjunction_model_connecting.lp': {'ambientConstantTransf': 0,
                                                                        'sha256': 'fa09e83cbe13c5527669b6a118d22494ce4ac69ab588ce15cedd97eff4a62d59',
                                                                        'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_adjunction_model_connecting_observation.lp': {'ambientConstantTransf': 0,
                                                                                    'sha256': '478725d601ff91d6d14f776a81607c883e009bf3baf8a2ef1302c663a14ba2d5',
                                                                                    'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_adjunction_model_exactness.lp': {'ambientConstantTransf': 0,
                                                                       'sha256': '0d6ae2fc482ad0f27bf145141099402d7499c56f8bd6463266cd036f16bb2d17',
                                                                       'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_adjunction_model_exactness_observations.lp': {'ambientConstantTransf': 0,
                                                                                    'sha256': 'e2f93d44e2f77633172cd04dfd287edbc63982dc3aa4e507d854af538f21c7cb',
                                                                                    'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_adjunction_model_row_context.lp': {'ambientConstantTransf': 0,
                                                                         'sha256': 'be0a848fea277636626c11a49f558f205ba404da6b09748b92814bc6d016ab9d',
                                                                         'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_native_exactness_observations.lp': {'ambientConstantTransf': 0,
                                                                          'sha256': '142ae4acc01d4342948adfb77e48482765ddd314c773c902bdfe2e564b683794',
                                                                          'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_native_snake_matching.lp': {'ambientConstantTransf': 6,
                                                                  'sha256': 'f516db79a4d211c14022247e37e96b4b1fea2cb16e07c6a6da3bfd43534f3824',
                                                                  'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_raw_window_connecting.lp': {'ambientConstantTransf': 0,
                                                                  'sha256': 'f1e05a56b69a42a17016801c454a8e862f274fa95346fa4fec30cc31c31de57d',
                                                                  'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_raw_window_connecting_observation.lp': {'ambientConstantTransf': 0,
                                                                              'sha256': '0aefff86826b7e9c63835a4a60d92a641f37c18a0c1595ac3b218ed811c688e2',
                                                                              'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_raw_window_exactness.lp': {'ambientConstantTransf': 0,
                                                                 'sha256': 'ebd454ca82d51622fa47c0bd6878db9e5a46a9b10833184cb1ad0b84e1336c13',
                                                                 'walkingArrowOplax': 0},
 'examples/freyd_adjunction_model_arrows.lp': {'ambientConstantTransf': 0,
                                               'sha256': '58efe12f9e5833254dafa31e42524caf132ef2fd199498d137cf11f0bb6f6afa',
                                               'walkingArrowOplax': 0},
 'examples/freyd_adjunction_model_connecting_observation.lp': {'ambientConstantTransf': 0,
                                                               'sha256': '1141f135aa419858e686b59deee948fed2efcbdd7e8bd90d4a3c82fd62d0a95f',
                                                               'walkingArrowOplax': 0},
 'examples/freyd_adjunction_model_whole_exactness.lp': {'ambientConstantTransf': 0,
                                                        'sha256': 'bc6ba424e12562645604cd00c15066486f354e20c4f1c1db1917ad530ec3dcda',
                                                        'walkingArrowOplax': 0},
 'examples/freyd_adjunction_model_window.lp': {'ambientConstantTransf': 0,
                                               'sha256': '3463f2ce51f5a69d1c3fc15059b45d704d9bee10db6f8ba4374433596b9fe55b',
                                               'walkingArrowOplax': 6},
 'examples/freyd_diagram_observations.lp': {'ambientConstantTransf': 0,
                                            'sha256': '19dff423f1ad86bf2f58075b13dc97f75b95a7dd31b28812d97a612f3ec14556',
                                            'walkingArrowOplax': 0},
 'examples/freyd_native_connecting_endpoints.lp': {'ambientConstantTransf': 0,
                                                   'sha256': 'ae48f434eea6551d8778984378fd8e86637537cf2bc3612e3de9eb9d117adb2e',
                                                   'walkingArrowOplax': 0},
 'examples/freyd_native_whole_exactness.lp': {'ambientConstantTransf': 0,
                                              'sha256': 'b82ac6b7ef88a3e10af4a0951f881195a9f43defe45d084762be9d0ba022353f',
                                              'walkingArrowOplax': 0},
 'examples/freyd_observation_coherence.lp': {'ambientConstantTransf': 0,
                                             'sha256': 'dec717ccd2f5ec1d58197789327007e78ce72df330ff0faf412ca707203cba38',
                                             'walkingArrowOplax': 0},
 'examples/freyd_raw_native_window.lp': {'ambientConstantTransf': 0,
                                         'sha256': 'ad83e462dd7ffbf7f6746c9cbe5711b9b3303b02793da5b1c0cf2a9c9c724ff0',
                                         'walkingArrowOplax': 0}}

def migrate_freyd_native_window_consumer(name, original):
    if name not in SOURCES:
        return None
    spec = SOURCES[name]
    assert hashlib.sha256(original.encode()).hexdigest() == spec['sha256'], name
    text, count = re.subn(r'\bFunctor_cat(?=\s+WalkingArrow_cat\s+\(@CommRingFreydPresentation_cat\s+R\))', 'Functor_oplax_cat', original)
    assert count == spec['walkingArrowOplax'], name
    count = 0
    while hits := list(re.finditer(r'@Const_transf\b', text)):
        m = hits[-1]
        i = m.end()
        args = []
        for _ in range(5):
            a, i = _atom(text, i)
            args.append(a)
        K, C, x, y, p = args
        assert K == 'Terminal_cat' and ' '.join(C.split()) == '(@CommRingFreydPresentation_cat R)', (name, args)
        body = '(@CONST_TRANSF_ORIGINAL ' + ' '.join(args) + ')'
        new = f'@strict_transfor {K} {C} (@Const_func {K} {C} {x}) (@Const_func {K} {C} {y}) {body}'
        text = text[:m.start()] + new + text[i:]
        count += 1
    assert count == spec['ambientConstantTransf'], name
    return text.replace('@CONST_TRANSF_ORIGINAL', '@Const_transf')
