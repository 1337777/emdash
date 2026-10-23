"""Source-pinned original target exactness and native public pair consumers.

Original maps, inverse data and complete reviewers retain qualification.
Existing whole inclusions and encoded proof views; no new formal rule.
"""
import hashlib
import re
from production_diagram_observation_migration import _atom, _point_readings, _body
from production_selected_presentation_migration import map_calls
from production_introduced_input_migration import enc_walk

SOURCES = {'emdash3_2_arrow_equivalence_observations.lp': {'counts': {'fapp0': 0,
                                                            'functorCarrier': 0,
                                                            'functorCategory': 0,
                                                            'initialOp': 0,
                                                            'shapeAction': 0,
                                                            'tapp0_fapp0': 0,
                                                            'transforCarrier': 0,
                                                            'walkingConstructor': 0},
                                                 'sha256': 'd747b90281c5974711f2ade16922a1b3e7c5e95191c20cb4cefeaf307b89441c',
                                                 'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                'diagram_evaluation_transf': 0,
                                                                'diagram_family_at_func': 0,
                                                                'diagram_family_transf': 0,
                                                                'one_cat_functor_category': 0,
                                                                'sym_transf_tapp0_transf': 0}},
 'emdash3_2_coimage_family_point_comparisons.lp': {'counts': {'fapp0': 0,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 20,
                                                              'initialOp': 2,
                                                              'shapeAction': 0,
                                                              'tapp0_fapp0': 0,
                                                              'transforCarrier': 0,
                                                              'walkingConstructor': 0},
                                                   'sha256': '3fa055fae8dcd8ca26bf7d848fd7809a69e08e9c6a9d00cc60d3af2fcd593546',
                                                   'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                  'diagram_evaluation_transf': 0,
                                                                  'diagram_family_at_func': 0,
                                                                  'diagram_family_transf': 0,
                                                                  'one_cat_functor_category': 0,
                                                                  'sym_transf_tapp0_transf': 0}},
 'emdash3_2_image_family_point_comparisons.lp': {'counts': {'fapp0': 0,
                                                            'functorCarrier': 0,
                                                            'functorCategory': 20,
                                                            'initialOp': 2,
                                                            'shapeAction': 0,
                                                            'tapp0_fapp0': 0,
                                                            'transforCarrier': 0,
                                                            'walkingConstructor': 0},
                                                 'sha256': '82e5fe3f3ab118139a12350f411e644ba7d746b283cee0a01486abedee25624c',
                                                 'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                'diagram_evaluation_transf': 0,
                                                                'diagram_family_at_func': 0,
                                                                'diagram_family_transf': 0,
                                                                'one_cat_functor_category': 0,
                                                                'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_categorical_exactness.lp': {'counts': {'fapp0': 0,
                                                           'functorCarrier': 0,
                                                           'functorCategory': 5,
                                                           'initialOp': 2,
                                                           'shapeAction': 0,
                                                           'tapp0_fapp0': 0,
                                                           'transforCarrier': 0,
                                                           'walkingConstructor': 0},
                                                'sha256': '8d02fde2b02c6cbb1219d9c549d4f67eeb3709211ec2d018856bf68e07dd7a8b',
                                                'wholeViews': {'diagram_evaluation_at_func': 0,
                                                               'diagram_evaluation_transf': 0,
                                                               'diagram_family_at_func': 0,
                                                               'diagram_family_transf': 0,
                                                               'one_cat_functor_category': 0,
                                                               'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_categorical_exactness_points.lp': {'counts': {'fapp0': 0,
                                                                  'functorCarrier': 0,
                                                                  'functorCategory': 13,
                                                                  'initialOp': 3,
                                                                  'shapeAction': 0,
                                                                  'tapp0_fapp0': 0,
                                                                  'transforCarrier': 0,
                                                                  'walkingConstructor': 0},
                                                       'sha256': '6190a6bbc0340041818ec77f045a8376f1365a9ed9f493c2d58ae2d86fa557aa',
                                                       'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                      'diagram_evaluation_transf': 0,
                                                                      'diagram_family_at_func': 0,
                                                                      'diagram_family_transf': 0,
                                                                      'one_cat_functor_category': 0,
                                                                      'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_connecting_target_exactness.lp': {'counts': {'fapp0': 0,
                                                                 'functorCarrier': 0,
                                                                 'functorCategory': 1,
                                                                 'initialOp': 6,
                                                                 'shapeAction': 0,
                                                                 'tapp0_fapp0': 0,
                                                                 'transforCarrier': 0,
                                                                 'walkingConstructor': 0},
                                                      'sha256': '15f23a8b846bc1a45de42daba3d6e11716a967fffa4d0bca4b6406bc081bf6bd',
                                                      'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                     'diagram_evaluation_transf': 0,
                                                                     'diagram_family_at_func': 0,
                                                                     'diagram_family_transf': 0,
                                                                     'one_cat_functor_category': 0,
                                                                     'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_connecting_target_lifts.lp': {'counts': {'fapp0': 0,
                                                             'functorCarrier': 0,
                                                             'functorCategory': 0,
                                                             'initialOp': 10,
                                                             'shapeAction': 0,
                                                             'tapp0_fapp0': 0,
                                                             'transforCarrier': 0,
                                                             'walkingConstructor': 0},
                                                  'sha256': '7127075bcb8a781b041bb9370e10f32ac550dd11628e73dd63f70ce2ab5d754c',
                                                  'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                 'diagram_evaluation_transf': 0,
                                                                 'diagram_family_at_func': 0,
                                                                 'diagram_family_transf': 1,
                                                                 'one_cat_functor_category': 0,
                                                                 'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_image_kernel_point_paths.lp': {'counts': {'fapp0': 0,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 157,
                                                              'initialOp': 5,
                                                              'shapeAction': 0,
                                                              'tapp0_fapp0': 0,
                                                              'transforCarrier': 0,
                                                              'walkingConstructor': 0},
                                                   'sha256': '4d9595b706cca16150914a1caabe2af355a7ad2f9a995cd503788c45abb8f16b',
                                                   'wholeViews': {'diagram_evaluation_at_func': 6,
                                                                  'diagram_evaluation_transf': 0,
                                                                  'diagram_family_at_func': 0,
                                                                  'diagram_family_transf': 0,
                                                                  'one_cat_functor_category': 0,
                                                                  'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_kernel_input_pair_observations.lp': {'counts': {'fapp0': 0,
                                                                    'functorCarrier': 0,
                                                                    'functorCategory': 4,
                                                                    'initialOp': 2,
                                                                    'shapeAction': 0,
                                                                    'tapp0_fapp0': 0,
                                                                    'transforCarrier': 0,
                                                                    'walkingConstructor': 0},
                                                         'sha256': '07e3e9d78f6065bd0b2087bf885f1153535334fc0ca9fecdfbce5b91d97eaf85',
                                                         'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                        'diagram_evaluation_transf': 0,
                                                                        'diagram_family_at_func': 1,
                                                                        'diagram_family_transf': 0,
                                                                        'one_cat_functor_category': 0,
                                                                        'sym_transf_tapp0_transf': 1}},
 'emdash3_2_one_cat_native_exact_arrow_pairs.lp': {'counts': {'fapp0': 0,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 13,
                                                              'initialOp': 7,
                                                              'shapeAction': 0,
                                                              'tapp0_fapp0': 0,
                                                              'transforCarrier': 0,
                                                              'walkingConstructor': 0},
                                                   'sha256': 'a699b3cdf88450b9b7569b4f31d159c8abe9a9e9c1654c4085124d407f826e11',
                                                   'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                  'diagram_evaluation_transf': 0,
                                                                  'diagram_family_at_func': 0,
                                                                  'diagram_family_transf': 0,
                                                                  'one_cat_functor_category': 0,
                                                                  'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_pair_comparisons.lp': {'counts': {'fapp0': 72,
                                                             'functorCarrier': 4,
                                                             'functorCategory': 38,
                                                             'initialOp': 0,
                                                             'shapeAction': 0,
                                                             'tapp0_fapp0': 2,
                                                             'transforCarrier': 10,
                                                             'walkingConstructor': 0},
                                                  'sha256': 'f386f4a22fe7bc8372f02d27c0ca850c49748389afa27929290333e73d36fb4a',
                                                  'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                 'diagram_evaluation_transf': 0,
                                                                 'diagram_family_at_func': 0,
                                                                 'diagram_family_transf': 0,
                                                                 'one_cat_functor_category': 0,
                                                                 'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_public_pair_exactness.lp': {'counts': {'fapp0': 41,
                                                                  'functorCarrier': 5,
                                                                  'functorCategory': 5,
                                                                  'initialOp': 1,
                                                                  'shapeAction': 0,
                                                                  'tapp0_fapp0': 0,
                                                                  'transforCarrier': 5,
                                                                  'walkingConstructor': 2},
                                                       'sha256': '0ce4ff31981642963c44436da1b148185d674fae58467fdb29f34bb076869fb7',
                                                       'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                      'diagram_evaluation_transf': 0,
                                                                      'diagram_family_at_func': 0,
                                                                      'diagram_family_transf': 0,
                                                                      'one_cat_functor_category': 0,
                                                                      'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_natural_equivalence_transport.lp': {'counts': {'fapp0': 0,
                                                                   'functorCarrier': 0,
                                                                   'functorCategory': 0,
                                                                   'initialOp': 0,
                                                                   'shapeAction': 0,
                                                                   'tapp0_fapp0': 0,
                                                                   'transforCarrier': 0,
                                                                   'walkingConstructor': 0},
                                                        'sha256': 'c45ee1e98d8a2219bd1204f9e285924752e835632e0dce10ba0869dc8eb2a617',
                                                        'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                       'diagram_evaluation_transf': 0,
                                                                       'diagram_family_at_func': 0,
                                                                       'diagram_family_transf': 0,
                                                                       'one_cat_functor_category': 0,
                                                                       'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_pair_comparison_zero.lp': {'counts': {'fapp0': 0,
                                                          'functorCarrier': 0,
                                                          'functorCategory': 0,
                                                          'initialOp': 0,
                                                          'shapeAction': 0,
                                                          'tapp0_fapp0': 0,
                                                          'transforCarrier': 0,
                                                          'walkingConstructor': 0},
                                               'sha256': '755ec59e744566cbcbb1e43668e96250e480674a446a804f87c0f8e608c8409b',
                                               'wholeViews': {'diagram_evaluation_at_func': 0,
                                                              'diagram_evaluation_transf': 0,
                                                              'diagram_family_at_func': 0,
                                                              'diagram_family_transf': 0,
                                                              'one_cat_functor_category': 0,
                                                              'sym_transf_tapp0_transf': 0}},
 'emdash3_2_zero_arrow_family_point_comparisons.lp': {'counts': {'fapp0': 6,
                                                                 'functorCarrier': 3,
                                                                 'functorCategory': 24,
                                                                 'initialOp': 0,
                                                                 'shapeAction': 0,
                                                                 'tapp0_fapp0': 0,
                                                                 'transforCarrier': 0,
                                                                 'walkingConstructor': 1},
                                                      'sha256': '1f16158400323dd68446ab846ce47647c6b96c222aa6bee7664925bc5132952a',
                                                      'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                     'diagram_evaluation_transf': 0,
                                                                     'diagram_family_at_func': 5,
                                                                     'diagram_family_transf': 0,
                                                                     'one_cat_functor_category': 0,
                                                                     'sym_transf_tapp0_transf': 0}},
 'emdash3_2_zero_arrow_family_point_diagrams.lp': {'counts': {'fapp0': 34,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 146,
                                                              'initialOp': 0,
                                                              'shapeAction': 18,
                                                              'tapp0_fapp0': 4,
                                                              'transforCarrier': 4,
                                                              'walkingConstructor': 6},
                                                   'sha256': 'db9d824e7af52f63b1d4b27071bef0065f14fc2390e2d637080a2e6dbf0e18fe',
                                                   'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                  'diagram_evaluation_transf': 0,
                                                                  'diagram_family_at_func': 0,
                                                                  'diagram_family_transf': 0,
                                                                  'one_cat_functor_category': 0,
                                                                  'sym_transf_tapp0_transf': 0}},
 'emdash3_2_zero_arrow_pair_observations.lp': {'counts': {'fapp0': 0,
                                                          'functorCarrier': 0,
                                                          'functorCategory': 3,
                                                          'initialOp': 0,
                                                          'shapeAction': 0,
                                                          'tapp0_fapp0': 0,
                                                          'transforCarrier': 0,
                                                          'walkingConstructor': 0},
                                               'sha256': '44e0574df6c324454fb783a60f8426b298bc477f6d490e3f0643bc97f495f291',
                                               'wholeViews': {'diagram_evaluation_at_func': 0,
                                                              'diagram_evaluation_transf': 0,
                                                              'diagram_family_at_func': 3,
                                                              'diagram_family_transf': 1,
                                                              'one_cat_functor_category': 0,
                                                              'sym_transf_tapp0_transf': 0}},
 'examples/arrow_equivalence_observations.lp': {'counts': {'fapp0': 0,
                                                           'functorCarrier': 0,
                                                           'functorCategory': 0,
                                                           'initialOp': 0,
                                                           'shapeAction': 0,
                                                           'tapp0_fapp0': 0,
                                                           'transforCarrier': 0,
                                                           'walkingConstructor': 0},
                                                'sha256': 'cdcb2f99ce2565d5a54dba55db7ad5cf71161d23ee465dbb4f5c6ad137b04677',
                                                'wholeViews': {'diagram_evaluation_at_func': 0,
                                                               'diagram_evaluation_transf': 0,
                                                               'diagram_family_at_func': 0,
                                                               'diagram_family_transf': 0,
                                                               'one_cat_functor_category': 0,
                                                               'sym_transf_tapp0_transf': 0}},
 'examples/image_family_point_comparisons.lp': {'counts': {'fapp0': 0,
                                                           'functorCarrier': 0,
                                                           'functorCategory': 46,
                                                           'initialOp': 2,
                                                           'shapeAction': 0,
                                                           'tapp0_fapp0': 0,
                                                           'transforCarrier': 0,
                                                           'walkingConstructor': 0},
                                                'sha256': '74061e3377265bd9fd759d82d0bf62b1324e9872f63b81ca1866694ec3084a16',
                                                'wholeViews': {'diagram_evaluation_at_func': 0,
                                                               'diagram_evaluation_transf': 0,
                                                               'diagram_family_at_func': 0,
                                                               'diagram_family_transf': 0,
                                                               'one_cat_functor_category': 0,
                                                               'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_categorical_exactness.lp': {'counts': {'fapp0': 0,
                                                          'functorCarrier': 0,
                                                          'functorCategory': 23,
                                                          'initialOp': 6,
                                                          'shapeAction': 0,
                                                          'tapp0_fapp0': 0,
                                                          'transforCarrier': 0,
                                                          'walkingConstructor': 0},
                                               'sha256': 'f2b9fed8d9cba3704c1483c80bf7e9c340ec990f870de384279cb262be0c735a',
                                               'wholeViews': {'diagram_evaluation_at_func': 0,
                                                              'diagram_evaluation_transf': 0,
                                                              'diagram_family_at_func': 0,
                                                              'diagram_family_transf': 0,
                                                              'one_cat_functor_category': 0,
                                                              'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_categorical_exactness_points.lp': {'counts': {'fapp0': 0,
                                                                 'functorCarrier': 0,
                                                                 'functorCategory': 0,
                                                                 'initialOp': 1,
                                                                 'shapeAction': 0,
                                                                 'tapp0_fapp0': 0,
                                                                 'transforCarrier': 0,
                                                                 'walkingConstructor': 0},
                                                      'sha256': '5d81f5f8c2af20eaddae7f4e0254092705175c3a888ddd9e3e7b6989a5c80acf',
                                                      'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                     'diagram_evaluation_transf': 0,
                                                                     'diagram_family_at_func': 0,
                                                                     'diagram_family_transf': 0,
                                                                     'one_cat_functor_category': 0,
                                                                     'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_connecting_target_exactness.lp': {'counts': {'fapp0': 0,
                                                                'functorCarrier': 0,
                                                                'functorCategory': 14,
                                                                'initialOp': 7,
                                                                'shapeAction': 0,
                                                                'tapp0_fapp0': 0,
                                                                'transforCarrier': 0,
                                                                'walkingConstructor': 0},
                                                     'sha256': '6523b4e773935e22fc30b9fb64707f4c7766986152f3d05c482958f9b1f7a307',
                                                     'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                    'diagram_evaluation_transf': 0,
                                                                    'diagram_family_at_func': 0,
                                                                    'diagram_family_transf': 0,
                                                                    'one_cat_functor_category': 0,
                                                                    'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_native_exact_arrow_pairs.lp': {'counts': {'fapp0': 0,
                                                             'functorCarrier': 0,
                                                             'functorCategory': 10,
                                                             'initialOp': 5,
                                                             'shapeAction': 0,
                                                             'tapp0_fapp0': 0,
                                                             'transforCarrier': 0,
                                                             'walkingConstructor': 0},
                                                  'sha256': '8d69ef170ac3b6e6a128f47320ecb77c45a5dcc7ed38642140f901bd78e5141e',
                                                  'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                 'diagram_evaluation_transf': 0,
                                                                 'diagram_family_at_func': 0,
                                                                 'diagram_family_transf': 0,
                                                                 'one_cat_functor_category': 0,
                                                                 'sym_transf_tapp0_transf': 0}},
 'examples/zero_arrow_family_point_diagrams.lp': {'counts': {'fapp0': 2,
                                                             'functorCarrier': 0,
                                                             'functorCategory': 22,
                                                             'initialOp': 0,
                                                             'shapeAction': 0,
                                                             'tapp0_fapp0': 4,
                                                             'transforCarrier': 0,
                                                             'walkingConstructor': 0},
                                                  'sha256': 'c945ce31b8a65308740a966b113d15568f67855741f0db2de4d4ba23da845c5b',
                                                  'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                 'diagram_evaluation_transf': 0,
                                                                 'diagram_family_at_func': 0,
                                                                 'diagram_family_transf': 0,
                                                                 'one_cat_functor_category': 0,
                                                                 'sym_transf_tapp0_transf': 0}},
 'examples/zero_arrow_pair_observations.lp': {'counts': {'fapp0': 0,
                                                         'functorCarrier': 0,
                                                         'functorCategory': 9,
                                                         'initialOp': 0,
                                                         'shapeAction': 0,
                                                         'tapp0_fapp0': 0,
                                                         'transforCarrier': 0,
                                                         'walkingConstructor': 0},
                                              'sha256': 'a3b9c974413bef371b3383d610a087eb80077e58ddd2a9fbdc54b18183ae5cf2',
                                              'wholeViews': {'diagram_evaluation_at_func': 0,
                                                             'diagram_evaluation_transf': 0,
                                                             'diagram_family_at_func': 6,
                                                             'diagram_family_transf': 1,
                                                             'one_cat_functor_category': 0,
                                                             'sym_transf_tapp0_transf': 0}}}

def native_pair_comparisons_view(text):
    B='(Functor_oplax_cat WalkingArrow_cat C)';W='(Functor_cat WalkingArrow_cat C)'
    d0='(@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d0)'
    d1='(@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d1)'
    inc='(@one_cat_diagram_oplax_include_func C C1)'
    m=re.search(r'(?m)^symbol native_pair_diagram_map\b.*?;',text,re.S);assert m
    raw=m.group().split('≔',1)[1].removesuffix(';').strip()
    assert raw.startswith('@one_cat_original_diagram_map C C1 d0 d1 c1 c2')
    raw='('+raw.replace('@one_cat_original_diagram_map C C1 d0 d1',f'@one_cat_original_diagram_map C C1 {d0} {d1}',1)+')'
    text=_body(text,'native_pair_diagram_map',f'@fapp1_fapp0 {W} {B} {inc} {d0} {d1} {raw}')
    assert text.count('@one_cat_diagram_map_path C C1')==1
    text=text.replace('@one_cat_diagram_map_path C C1','@one_cat_oplax_diagram_map_path C C1')
    matches=list(re.finditer(r'@one_cat_diagram_map_equiv\b',text));assert len(matches)==1
    m=matches[0];cursor=m.end();args=[]
    for _ in range(7):a,cursor=_atom(text,cursor);args.append(a)
    assert args[:4]==['C','C1','d0','d1'] and args[-2:]==['U1','U2']
    assert args[4].startswith('(@native_pair_diagram_map')
    equiv=f'(@one_cat_diagram_map_equiv C C1 {d0} {d1} {raw} U1 U2)'
    new=f'@one_cat_omega_equiv_fmap {W} {B} (@one_cat_oplax_functor_category WalkingArrow_cat C C1) {inc} {d0} {d1} {raw} {equiv}'
    text=text[:m.start()]+new+text[cursor:]
    return 'require open emdash.emdash3_2_one_cat_diagram_family_reflection;\n'+text


def native_point_diagrams(text):
    B='(Functor_oplax_cat WalkingArrow_cat C)'
    W='(Functor_cat WalkingArrow_cat C)'
    d=f'(@fapp0 K {B} (@zero_arrow_family_incoming_func K C t T A D h) x)'
    Z='(@ZeroArrowCone_cat C t T)'
    e=f'''(@fapp0 {Z} {B}
      (@zero_arrow_family_incoming_func {Z} C t T
        (@zero_arrow_cone_first_func C t T) (@zero_arrow_cone_diagram_func C t T)
        (@zero_arrow_cone_universal_transf C C1 t T))
      (@zero_arrow_family_point_input K C t T A D h x))'''
    decode=lambda a:f'(@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) {a})'
    u='(@fapp0 K C A x)'
    v=f'(@fapp0 {B} C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@fapp0 K {B} D x))'
    generator=lambda a:f'(@fapp1_fapp0 WalkingArrow_cat C {decode(a)} walking_arrow_src walking_arrow_tgt walking_arrow_generator)'
    gd,ge=generator(d),generator(e)
    q='(@zero_arrow_family_point_generator_path K C C1 t T A D h x)'
    r=f'(@eq_sym (Hom C {u} {v}) {gd} {ge} {q})'
    for name,source,target,p in [('zero_arrow_family_point_diagram_map',d,e,q),('zero_arrow_family_point_diagram_inverse',e,d,r)]:
        original=f'''(@one_cat_original_diagram_map C C1 {decode(source)} {decode(target)}
          (@id C {u}) (@id C {v})
          (@path_to_hom (Hom_cat C {u} {v}) {generator(source)} {generator(target)} {p}))'''
        body=f'''@fapp1_fapp0 {W} {B} (@one_cat_diagram_oplax_include_func C C1)
          {decode(source)} {decode(target)} {original}'''
        text=_body(text,name,body)
    assert text.count('@one_cat_diagram_map_path C C1')==2
    text=text.replace('@one_cat_diagram_map_path C C1','@one_cat_oplax_diagram_map_path C C1')
    text='require open emdash.emdash3_2_one_cat_diagram_map_equivalences;\nrequire open emdash.emdash3_2_one_cat_diagram_family_reflection;\n'+text
    return text


def kernel_pair_path_view(text):
    B='(Functor_oplax_cat WalkingArrow_cat C)'
    diagram='(@transf_arrow_diagram_func K C B D g)'
    inp=f'(@one_cat_kernel_family_input K C C1 t T T0 A {diagram} f z)'
    incoming=f'(@zero_arrow_family_incoming_transf K C t T A {diagram} {inp})'
    body=f'''@eq_ap (@Transf K C A B) (ArrowPairObservation C)
      (λ u : τ (@Transf K C A B), @transf_arrow_pair_at K C A B D u g x)
      {incoming} f
      (@one_cat_kernel_input_incoming_path K C C1 t T T0 A B D f g z)'''
    return _body(text,'one_cat_kernel_input_pair_path',body)


def point_comparison_view(text):
    B='(Functor_oplax_cat WalkingArrow_cat C)'
    Y=f'(@diagram_oplax_family_at_func K WalkingArrow_cat C D walking_arrow_src)'
    incoming='(@zero_arrow_family_incoming_transf K C t T A D h)'
    a='(@fapp0 K C A x)';b=f'(@fapp0 K C {Y} x)'
    cell=f'(@tapp0_fapp0 K C A {Y} x {incoming})'
    end=f'''(@terminal_arrow_test_incoming C t T {a} (@fapp0 K {B} D x)
       (@tapp0_fapp0 K {B} (@comp_cat_fapp0 K C {B} (@terminal_arrow_diagram_func C t T) A) D x h))'''
    raw=f'(@walking_arrow_func C {a} {b} {cell})'
    final=f'(@walking_arrow_func C {a} {b} {end})'
    encode=lambda f:f'(@OddDual_func WalkingArrow_cat C {f})'
    input=f'(@fapp0 K {B} (@zero_arrow_family_incoming_func K C t T A D h) x)'
    decoded=f'(@transf_arrow_diagram_at_func K C A {Y} {incoming} x)'
    body=f'''@eq_trans (Obj {B}) {input} {encode(raw)} {encode(final)}
      (@eq_ap (Functor WalkingArrow_cat C) (Obj {B})
        (λ d : τ (Functor WalkingArrow_cat C), @OddDual_func WalkingArrow_cat C d)
        {decoded} {raw}
        (@transf_arrow_diagram_point_path K C A {Y} {incoming} x))
      (@eq_ap (Hom C {a} {b}) (Obj {B})
        (λ f : τ (Hom C {a} {b}), @OddDual_func WalkingArrow_cat C (@walking_arrow_func C {a} {b} f))
        {cell} {end} (@zero_arrow_incoming_at_point_path K C C1 t T A D h x))'''
    return _body(text,'zero_arrow_incoming_point_diagram_path',body)


def image_kernel_point_view(text):
    # Endpoints of qualified one_cat_image_kernel_reconstruction_path.
    # Source SHA256: 6e4f2d26bd10cb479366ac8123e97b41277a518eb297ebeec3b05f316b18f68d
    whole = ['(@Transf K C (@comp_cat_fapp0 K (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0 P Q)\n    (@zero_arrow_family_incoming_func K C t T A D h)) (@kernel_adjunction_family_func K C S t T P D))', '(@comp_fapp0\n    (Functor_cat K C) (@comp_cat_fapp0 K (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0 P Q)\n    (@zero_arrow_family_incoming_func K C t T A D h)) (@comp_cat_fapp0 K (Functor_oplax_cat WalkingArrow_cat C) C\n    (@adjunction_image_func C S t T T0 P Q) (@zero_arrow_family_incoming_func K C t T A D h))\n    (@kernel_adjunction_family_func K C S t T P D) (@one_cat_image_to_kernel_transf K C S C1 t T T0 P Q A D h N)\n    (@fapp0 _ _ (@comp_cat_con_fapp1_func K (Functor_oplax_cat WalkingArrow_cat C) C (@zero_arrow_family_incoming_func K C t\n    T A D h) (@adjunction_coimage_func C S t T T0 P Q) (@adjunction_image_func C S t T T0 P Q))\n    (@one_cat_coimage_image_comparison C S C1 t T T0 P Q)))', '(@one_cat_coimage_to_kernel_transf K C S C1 t T T0 P Q A D\n    h)']
    start=text.index('symbol one_cat_image_kernel_point_reconstruction ')
    end=text.index('symbol one_cat_image_kernel_point_path ',start)
    part=text[start:end];matches=list(re.finditer(r'@eq_ap\b',part));assert len(matches)==1
    m=matches[0];cursor=m.end();args=[]
    for _ in range(6):a,cursor=_atom(part,cursor);args.append(a)
    assert args[3:5]==['_','_']
    assert args[5].startswith('(@one_cat_image_kernel_reconstruction_path K C S C1')
    args[3:5]=whole[1:]
    replacement='@eq_ap '+ '\n    '.join(args)
    part=part[:m.start()]+replacement+part[cursor:]
    return text[:start]+part+text[end:]


def migrate_native_target_exactness_consumer(name,original):
 if name not in SOURCES:return None
 spec=SOURCES[name];assert hashlib.sha256(original.encode()).hexdigest()==spec['sha256']
 text=original;B='(Functor_oplax_cat WalkingArrow_cat C)'
 for pattern,replacement,key in (
  (r'\bFunctor_cat(?=\s+WalkingArrow_cat\s+C\b)','Functor_oplax_cat','functorCategory'),
  (r'\(Functor\s+WalkingArrow_cat\s+C\s*\)','(Obj '+B+')','functorCarrier'),
  (r'@Transf\s+WalkingArrow_cat\s+C\b','@Hom '+B,'transforCarrier'),
  (r'\bOp_cat(?=\s+C\b)','TotalOp_cat','initialOp')):
  text,count=re.subn(pattern,replacement,text);assert count==spec['counts'][key],(name,key,count)
 text=_point_readings(text,(spec['counts']['fapp0'],spec['counts']['tapp0_fapp0']))
 for head,arity,corrected in (
  ('diagram_family_at_func',3,'diagram_oplax_family_at_func'),
  ('diagram_family_transf',3,'diagram_oplax_family_transf'),
  ('diagram_evaluation_at_func',2,'diagram_oplax_evaluation_at_func'),
  ('diagram_evaluation_transf',2,'diagram_oplax_evaluation_transf'),
  ('sym_transf_tapp0_transf',3,'diagram_oplax_family_map_at'),
  ('one_cat_functor_category',2,'one_cat_oplax_functor_category')):
  edits=[]
  for match in re.finditer(r'@'+head+r'\b',text):
   cursor,args=match.end(),[]
   for _ in range(arity):a,cursor=_atom(text,cursor);args.append(a)
   if args[-2:]!=['WalkingArrow_cat','C']:continue
   edits.append((match.start(),match.end()))
  assert len(edits)==spec['wholeViews'][head],(name,head)
  for lo,hi in reversed(edits):text=text[:lo]+'@'+corrected+text[hi:]
 def arrow(args):
  d,x,y,f=args
  return f'@tapp0_fapp0 {B} C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C {x}) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C {y}) {d} (@diagram_oplax_evaluation_transf WalkingArrow_cat C {x} {y} {f})'
 text,count=map_calls(text,'fapp1_fapp0',4,arrow);assert count==spec['counts']['shapeAction']
 text=enc_walk(text)
 if name == 'emdash3_2_one_cat_native_pair_comparisons.lp':
  text=native_pair_comparisons_view(text)
 if name == 'emdash3_2_zero_arrow_family_point_diagrams.lp':
  text=native_point_diagrams(text)
 if name == 'emdash3_2_one_cat_kernel_input_pair_observations.lp':
  text=kernel_pair_path_view(text)
 if name == 'emdash3_2_zero_arrow_family_point_comparisons.lp':
  text=point_comparison_view(text)
 if name == 'emdash3_2_one_cat_image_kernel_point_paths.lp':
  text=image_kernel_point_view(text)
 decl=r'(?m)^(?:(?:protected|injective|constant) )?symbol\s+(\w+)'
 assert re.findall(decl,original)==re.findall(decl,text),name
 assert re.findall(r'(?m)^(assert(?:not)?)\b',original)==re.findall(r'(?m)^(assert(?:not)?)\b',text),name
 return text
