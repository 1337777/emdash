"""Source-pinned original homology-window and exactness continuation.

Original whole owners and complete reviewers own qualification. Two derived
ordinary proof views align a zero proof; no new rule or operational primitive.
"""
import hashlib
import re
from pathlib import Path

from production_diagram_observation_migration import _atom, _point_readings

AUDIT = Path(__file__).resolve().parent
ADDED_PROOF_VIEWS = {
    'emdash3_2_one_cat_quotient_cokernel_zero.lp': ['one_cat_quotient_cokernel_zero_native_path'],
    'emdash3_2_one_cat_boundary_representatives.lp': ['one_cat_boundary_quotient_zero_path'],
}

SOURCES = {'emdash3_2_one_cat_additive_family_units.lp': {'counts': {'fapp0': 0,
                                                           'functorCarrier': 0,
                                                           'functorCategory': 0,
                                                           'initialOp': 5,
                                                           'tapp0_fapp0': 0,
                                                           'transforCarrier': 0},
                                                'sha256': 'f9c3dcec3ab6fb8dc5d8fc249f5077d3902751684f3337cd082bbfffbeece385',
                                                'wholeViews': {'diagram_evaluation_at_func': 0,
                                                               'diagram_evaluation_transf': 0,
                                                               'diagram_family_at_func': 0,
                                                               'diagram_family_transf': 0,
                                                               'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_biproduct_injection_reindex.lp': {'counts': {'fapp0': 0,
                                                                 'functorCarrier': 0,
                                                                 'functorCategory': 8,
                                                                 'initialOp': 7,
                                                                 'tapp0_fapp0': 0,
                                                                 'transforCarrier': 0},
                                                      'sha256': 'bf4291be3ea04e27da2aa91c7ec44c4494a64802a535f69b63d86059d7c554f8',
                                                      'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                     'diagram_evaluation_transf': 0,
                                                                     'diagram_family_at_func': 0,
                                                                     'diagram_family_transf': 8,
                                                                     'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_boundary_representatives.lp': {'counts': {'fapp0': 0,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 263,
                                                              'initialOp': 11,
                                                              'tapp0_fapp0': 0,
                                                              'transforCarrier': 0},
                                                   'sha256': '29716a94c4b287e787aa0abd2eb2a12e543fd61ce0b898e4291886d555c122ae',
                                                   'wholeViews': {'diagram_evaluation_at_func': 11,
                                                                  'diagram_evaluation_transf': 0,
                                                                  'diagram_family_at_func': 9,
                                                                  'diagram_family_transf': 5,
                                                                  'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_connecting_source_cycles.lp': {'counts': {'fapp0': 0,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 0,
                                                              'initialOp': 12,
                                                              'tapp0_fapp0': 0,
                                                              'transforCarrier': 0},
                                                   'sha256': '8d93087d3e4e88281dc1954ed097adbd9835512f3342f1964f22713a92b83392',
                                                   'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                  'diagram_evaluation_transf': 0,
                                                                  'diagram_family_at_func': 0,
                                                                  'diagram_family_transf': 0,
                                                                  'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_connecting_source_exactness.lp': {'counts': {'fapp0': 0,
                                                                 'functorCarrier': 0,
                                                                 'functorCategory': 1,
                                                                 'initialOp': 10,
                                                                 'tapp0_fapp0': 0,
                                                                 'transforCarrier': 0},
                                                      'sha256': '73c9efde6fe9383afcf3c5c1a351fe7b7c425798c52cda8d318bc1987b1969fb',
                                                      'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                     'diagram_evaluation_transf': 0,
                                                                     'diagram_family_at_func': 0,
                                                                     'diagram_family_transf': 0,
                                                                     'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_connecting_source_representatives.lp': {'counts': {'fapp0': 0,
                                                                       'functorCarrier': 0,
                                                                       'functorCategory': 0,
                                                                       'initialOp': 12,
                                                                       'tapp0_fapp0': 0,
                                                                       'transforCarrier': 0},
                                                            'sha256': 'a42f2757c0b9c903403f0609ad082db3b674ce060bfef3e3bc5cacf644944515',
                                                            'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                           'diagram_evaluation_transf': 0,
                                                                           'diagram_family_at_func': 0,
                                                                           'diagram_family_transf': 0,
                                                                           'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_connecting_target_representatives.lp': {'counts': {'fapp0': 0,
                                                                       'functorCarrier': 0,
                                                                       'functorCategory': 0,
                                                                       'initialOp': 11,
                                                                       'tapp0_fapp0': 0,
                                                                       'transforCarrier': 0},
                                                            'sha256': '20d0af1f75eef8b5514c7d595a99dccd67c5e7ebb2774f118cdf16dd70d87bc7',
                                                            'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                           'diagram_evaluation_transf': 0,
                                                                           'diagram_family_at_func': 0,
                                                                           'diagram_family_transf': 0,
                                                                           'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_copair_injection_paths.lp': {'counts': {'fapp0': 0,
                                                            'functorCarrier': 0,
                                                            'functorCategory': 0,
                                                            'initialOp': 5,
                                                            'tapp0_fapp0': 0,
                                                            'transforCarrier': 0},
                                                 'sha256': '649ef835d5fd6cbec5372cbf4cf3c8a3eb5935429956806818f6da6a544a54cf',
                                                 'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                'diagram_evaluation_transf': 0,
                                                                'diagram_family_at_func': 0,
                                                                'diagram_family_transf': 0,
                                                                'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_cospan_kernel_covers.lp': {'counts': {'fapp0': 0,
                                                          'functorCarrier': 0,
                                                          'functorCategory': 2,
                                                          'initialOp': 12,
                                                          'tapp0_fapp0': 0,
                                                          'transforCarrier': 0},
                                               'sha256': '5fb89f9ced3addfb10df5f9e4bd5bbe61d4768644a21ed73db7574862a8f9c80',
                                               'wholeViews': {'diagram_evaluation_at_func': 1,
                                                              'diagram_evaluation_transf': 0,
                                                              'diagram_family_at_func': 0,
                                                              'diagram_family_transf': 0,
                                                              'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_homology_representatives.lp': {'counts': {'fapp0': 0,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 20,
                                                              'initialOp': 6,
                                                              'tapp0_fapp0': 0,
                                                              'transforCarrier': 0},
                                                   'sha256': '7b889ba2447c72e7c7086cacad7300628d9ec5504e6fd95fec15dff0c4fcecd7',
                                                   'wholeViews': {'diagram_evaluation_at_func': 1,
                                                                  'diagram_evaluation_transf': 0,
                                                                  'diagram_family_at_func': 0,
                                                                  'diagram_family_transf': 0,
                                                                  'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_image_kernel_exactness.lp': {'counts': {'fapp0': 0,
                                                            'functorCarrier': 0,
                                                            'functorCategory': 86,
                                                            'initialOp': 4,
                                                            'tapp0_fapp0': 0,
                                                            'transforCarrier': 0},
                                                 'sha256': '754babfc019efb99b8c422678b8745796630b4aa74d560556450e5b27ca91177',
                                                 'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                'diagram_evaluation_transf': 0,
                                                                'diagram_family_at_func': 0,
                                                                'diagram_family_transf': 0,
                                                                'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_image_kernel_inclusion_paths.lp': {'counts': {'fapp0': 0,
                                                                  'functorCarrier': 0,
                                                                  'functorCategory': 130,
                                                                  'initialOp': 4,
                                                                  'tapp0_fapp0': 0,
                                                                  'transforCarrier': 0},
                                                       'sha256': 'abca38b0edef2cecab3cbcb65e38b1bad5369484ca0f3da0308715d70af005bc',
                                                       'wholeViews': {'diagram_evaluation_at_func': 5,
                                                                      'diagram_evaluation_transf': 0,
                                                                      'diagram_family_at_func': 37,
                                                                      'diagram_family_transf': 0,
                                                                      'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_inverse_from_universal_zeros.lp': {'counts': {'fapp0': 0,
                                                                  'functorCarrier': 0,
                                                                  'functorCategory': 60,
                                                                  'initialOp': 2,
                                                                  'tapp0_fapp0': 0,
                                                                  'transforCarrier': 0},
                                                       'sha256': 'd37962a332c207cb718c96a30f8573bb5e2a5a1dd73333f5cef88ed9b03b65d3',
                                                       'wholeViews': {'diagram_evaluation_at_func': 2,
                                                                      'diagram_evaluation_transf': 0,
                                                                      'diagram_family_at_func': 38,
                                                                      'diagram_family_transf': 11,
                                                                      'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_middle_homology_cycles.lp': {'counts': {'fapp0': 0,
                                                            'functorCarrier': 0,
                                                            'functorCategory': 0,
                                                            'initialOp': 10,
                                                            'tapp0_fapp0': 0,
                                                            'transforCarrier': 0},
                                                 'sha256': '65012e49ca3ab2c3d9db8c1408f7cc1da6b7003da88ff86a67b519c1d7c613a5',
                                                 'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                'diagram_evaluation_transf': 0,
                                                                'diagram_family_at_func': 0,
                                                                'diagram_family_transf': 0,
                                                                'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_middle_homology_exactness.lp': {'counts': {'fapp0': 0,
                                                               'functorCarrier': 0,
                                                               'functorCategory': 1,
                                                               'initialOp': 10,
                                                               'tapp0_fapp0': 0,
                                                               'transforCarrier': 0},
                                                    'sha256': 'af19b7ee4f10723bc5c799f365f14d2cbed4f938b200a912094d531ae878a259',
                                                    'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                   'diagram_evaluation_transf': 0,
                                                                   'diagram_family_at_func': 0,
                                                                   'diagram_family_transf': 0,
                                                                   'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_middle_homology_representatives.lp': {'counts': {'fapp0': 0,
                                                                     'functorCarrier': 0,
                                                                     'functorCategory': 0,
                                                                     'initialOp': 16,
                                                                     'tapp0_fapp0': 0,
                                                                     'transforCarrier': 0},
                                                          'sha256': 'dcf7acd9d24bb6f45167be40b1b0a9c3e673f6fc89a89729ae17ea7bd729916d',
                                                          'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                         'diagram_evaluation_transf': 0,
                                                                         'diagram_family_at_func': 0,
                                                                         'diagram_family_transf': 0,
                                                                         'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_native_connecting_inclusion_zero.lp': {'counts': {'fapp0': 0,
                                                                      'functorCarrier': 0,
                                                                      'functorCategory': 0,
                                                                      'initialOp': 3,
                                                                      'tapp0_fapp0': 0,
                                                                      'transforCarrier': 0},
                                                           'sha256': '76ca5d7d1d4b217382aed18774e657295578ff882f7bd81809d66472f43ed2f3',
                                                           'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                          'diagram_evaluation_transf': 0,
                                                                          'diagram_family_at_func': 0,
                                                                          'diagram_family_transf': 0,
                                                                          'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_native_exact_comparison_kernels.lp': {'counts': {'fapp0': 0,
                                                                     'functorCarrier': 0,
                                                                     'functorCategory': 15,
                                                                     'initialOp': 3,
                                                                     'tapp0_fapp0': 0,
                                                                     'transforCarrier': 0},
                                                          'sha256': '495019ec30407d59b7c031d5060139be1ff0ec9bcafa1244203dcfe697f54ba2',
                                                          'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                         'diagram_evaluation_transf': 0,
                                                                         'diagram_family_at_func': 0,
                                                                         'diagram_family_transf': 0,
                                                                         'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_native_homology_window_connecting.lp': {'counts': {'fapp0': 0,
                                                                       'functorCarrier': 0,
                                                                       'functorCategory': 0,
                                                                       'initialOp': 5,
                                                                       'tapp0_fapp0': 0,
                                                                       'transforCarrier': 0},
                                                            'sha256': '8967aaaf9e91ce2ece3f46d39b4393ddd2b319ddbecec11762aab60603e96129',
                                                            'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                           'diagram_evaluation_transf': 0,
                                                                           'diagram_family_at_func': 0,
                                                                           'diagram_family_transf': 0,
                                                                           'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_native_homology_window_exact_inputs.lp': {'counts': {'fapp0': 0,
                                                                         'functorCarrier': 0,
                                                                         'functorCategory': 7,
                                                                         'initialOp': 11,
                                                                         'tapp0_fapp0': 0,
                                                                         'transforCarrier': 0},
                                                              'sha256': 'd601c74c3911d7b42fb283c09614cc5cb4ab3e7c521d904cda9c131acb89fe31',
                                                              'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                             'diagram_evaluation_transf': 0,
                                                                             'diagram_family_at_func': 0,
                                                                             'diagram_family_transf': 0,
                                                                             'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_native_middle_homology_exactness.lp': {'counts': {'fapp0': 0,
                                                                      'functorCarrier': 0,
                                                                      'functorCategory': 1,
                                                                      'initialOp': 1,
                                                                      'tapp0_fapp0': 0,
                                                                      'transforCarrier': 0},
                                                           'sha256': 'd62055b3bf42c9073c47db942b96f0210779518f050e3d729a3f065ad2aa4332',
                                                           'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                          'diagram_evaluation_transf': 0,
                                                                          'diagram_family_at_func': 0,
                                                                          'diagram_family_transf': 0,
                                                                          'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_quotient_cokernel_zero.lp': {'counts': {'fapp0': 0,
                                                            'functorCarrier': 0,
                                                            'functorCategory': 1,
                                                            'initialOp': 1,
                                                            'tapp0_fapp0': 0,
                                                            'transforCarrier': 0},
                                                 'sha256': 'faf7c64ac9793b05bcdbf78e1ce12bf7ca5230f549af661e0b2dd020f1d55e52',
                                                 'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                'diagram_evaluation_transf': 0,
                                                                'diagram_family_at_func': 9,
                                                                'diagram_family_transf': 0,
                                                                'one_cat_functor_category': 0}},
 'emdash3_2_one_cat_zero_cokernel_families.lp': {'counts': {'fapp0': 0,
                                                            'functorCarrier': 0,
                                                            'functorCategory': 4,
                                                            'initialOp': 4,
                                                            'tapp0_fapp0': 0,
                                                            'transforCarrier': 0},
                                                 'sha256': '77c293e38ad3e230f6dcb416fd2bfd3fc45367f41abe6a958573bb8f3b7c2f9c',
                                                 'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                'diagram_evaluation_transf': 0,
                                                                'diagram_family_at_func': 42,
                                                                'diagram_family_transf': 4,
                                                                'one_cat_functor_category': 0}},
 'examples/one_cat_additive_family_units.lp': {'counts': {'fapp0': 0,
                                                          'functorCarrier': 0,
                                                          'functorCategory': 0,
                                                          'initialOp': 5,
                                                          'tapp0_fapp0': 0,
                                                          'transforCarrier': 0},
                                               'sha256': 'a34fedd6c674451bd841a6b8d4fe004c6b5bc861ac18fb75a7002bce0593aeec',
                                               'wholeViews': {'diagram_evaluation_at_func': 0,
                                                              'diagram_evaluation_transf': 0,
                                                              'diagram_family_at_func': 0,
                                                              'diagram_family_transf': 0,
                                                              'one_cat_functor_category': 0}},
 'examples/one_cat_connecting_source_exactness.lp': {'counts': {'fapp0': 0,
                                                                'functorCarrier': 0,
                                                                'functorCategory': 14,
                                                                'initialOp': 7,
                                                                'tapp0_fapp0': 0,
                                                                'transforCarrier': 0},
                                                     'sha256': 'ad0f1f04f04b8085e3ecc2338568049c42703e2df84aaaa898e2dc0812cc8a0b',
                                                     'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                    'diagram_evaluation_transf': 0,
                                                                    'diagram_family_at_func': 0,
                                                                    'diagram_family_transf': 0,
                                                                    'one_cat_functor_category': 0}},
 'examples/one_cat_cospan_kernel_covers.lp': {'counts': {'fapp0': 0,
                                                         'functorCarrier': 0,
                                                         'functorCategory': 6,
                                                         'initialOp': 4,
                                                         'tapp0_fapp0': 0,
                                                         'transforCarrier': 0},
                                              'sha256': '41ede9485cb33ec012355f27c33be4ce209cac6f73aa1479600e97cceb962bd3',
                                              'wholeViews': {'diagram_evaluation_at_func': 2,
                                                             'diagram_evaluation_transf': 0,
                                                             'diagram_family_at_func': 0,
                                                             'diagram_family_transf': 0,
                                                             'one_cat_functor_category': 0}},
 'examples/one_cat_homology_representatives.lp': {'counts': {'fapp0': 0,
                                                             'functorCarrier': 0,
                                                             'functorCategory': 46,
                                                             'initialOp': 5,
                                                             'tapp0_fapp0': 0,
                                                             'transforCarrier': 0},
                                                  'sha256': '2f2ba892c4a77d32cb3b64cb390f8e1aeff85f2f2f1162be6f1efffb4c405845',
                                                  'wholeViews': {'diagram_evaluation_at_func': 2,
                                                                 'diagram_evaluation_transf': 0,
                                                                 'diagram_family_at_func': 0,
                                                                 'diagram_family_transf': 0,
                                                                 'one_cat_functor_category': 0}},
 'examples/one_cat_image_kernel_exactness.lp': {'counts': {'fapp0': 0,
                                                           'functorCarrier': 0,
                                                           'functorCategory': 31,
                                                           'initialOp': 5,
                                                           'tapp0_fapp0': 0,
                                                           'transforCarrier': 0},
                                                'sha256': '6351670101d72d89a05afc09fecdbffd55bb00d02e07b5a2effe9f6e468c470b',
                                                'wholeViews': {'diagram_evaluation_at_func': 0,
                                                               'diagram_evaluation_transf': 0,
                                                               'diagram_family_at_func': 0,
                                                               'diagram_family_transf': 0,
                                                               'one_cat_functor_category': 0}},
 'examples/one_cat_middle_homology_cycles.lp': {'counts': {'fapp0': 0,
                                                           'functorCarrier': 0,
                                                           'functorCategory': 0,
                                                           'initialOp': 6,
                                                           'tapp0_fapp0': 0,
                                                           'transforCarrier': 0},
                                                'sha256': 'b01e79101974a697952638eb16ea762a6bf70e3d8a7beceddd7b274fb000c32c',
                                                'wholeViews': {'diagram_evaluation_at_func': 0,
                                                               'diagram_evaluation_transf': 0,
                                                               'diagram_family_at_func': 0,
                                                               'diagram_family_transf': 0,
                                                               'one_cat_functor_category': 0}},
 'examples/one_cat_middle_homology_exactness.lp': {'counts': {'fapp0': 0,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 16,
                                                              'initialOp': 6,
                                                              'tapp0_fapp0': 0,
                                                              'transforCarrier': 0},
                                                   'sha256': '1b1d1e61fc7f7b306d67848540bc22ec9f47421d011e6fc8542b8440a63bb49d',
                                                   'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                  'diagram_evaluation_transf': 0,
                                                                  'diagram_family_at_func': 0,
                                                                  'diagram_family_transf': 0,
                                                                  'one_cat_functor_category': 0}},
 'examples/one_cat_native_exact_comparison_kernels.lp': {'counts': {'fapp0': 0,
                                                                    'functorCarrier': 0,
                                                                    'functorCategory': 60,
                                                                    'initialOp': 3,
                                                                    'tapp0_fapp0': 0,
                                                                    'transforCarrier': 0},
                                                         'sha256': '6da86d33e8e01888a5302c1a394d1987aa3c25ec67dc8f0e6a9f74b6757f3434',
                                                         'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                        'diagram_evaluation_transf': 0,
                                                                        'diagram_family_at_func': 0,
                                                                        'diagram_family_transf': 0,
                                                                        'one_cat_functor_category': 0}},
 'examples/one_cat_native_homology_window_connecting.lp': {'counts': {'fapp0': 0,
                                                                      'functorCarrier': 0,
                                                                      'functorCategory': 0,
                                                                      'initialOp': 6,
                                                                      'tapp0_fapp0': 0,
                                                                      'transforCarrier': 0},
                                                           'sha256': 'c405cb183324eac3e33b672d6e89d1ebf2f62087f4b7da8c9f35543349450739',
                                                           'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                          'diagram_evaluation_transf': 0,
                                                                          'diagram_family_at_func': 0,
                                                                          'diagram_family_transf': 0,
                                                                          'one_cat_functor_category': 0}},
 'examples/one_cat_native_homology_window_exact_inputs.lp': {'counts': {'fapp0': 0,
                                                                        'functorCarrier': 0,
                                                                        'functorCategory': 0,
                                                                        'initialOp': 4,
                                                                        'tapp0_fapp0': 0,
                                                                        'transforCarrier': 0},
                                                             'sha256': '694419f05facba41502cceba256c7884acc9ef02ce707f66f8cae3888256f212',
                                                             'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                            'diagram_evaluation_transf': 0,
                                                                            'diagram_family_at_func': 0,
                                                                            'diagram_family_transf': 0,
                                                                            'one_cat_functor_category': 0}},
 'examples/one_cat_zero_cokernel_families.lp': {'counts': {'fapp0': 0,
                                                           'functorCarrier': 0,
                                                           'functorCategory': 4,
                                                           'initialOp': 4,
                                                           'tapp0_fapp0': 0,
                                                           'transforCarrier': 0},
                                                'sha256': 'db9d1a9111dda3d02d5571375af898cf6686db29bbae0eb239936012f46c0aa0',
                                                'wholeViews': {'diagram_evaluation_at_func': 0,
                                                               'diagram_evaluation_transf': 0,
                                                               'diagram_family_at_func': 25,
                                                               'diagram_family_transf': 4,
                                                               'one_cat_functor_category': 0}}}

def _biproduct_reindex_view(text):
    marker = 'symbol one_cat_biproduct_inj1_reindex_path'
    assert text.count(marker) == 1
    start = text.index(marker)
    part = text[start:]
    matches = list(re.finditer(r'@eq_refl\b', part))
    assert len(matches) == 1
    match = matches[0]
    carrier, cursor = _atom(part, match.end())
    value, finish = _atom(part, cursor)
    assert value.startswith('(@fapp0 ')
    args=[];cursor=len('(@fapp0')
    for _ in range(4):
        arg,cursor = _atom(value,cursor);args.append(arg)
    source,target,local_mate,point=args
    assert local_mate.startswith('(@one_cat_adjunction_family_transpose_func ')
    args=[];cursor=len('(@one_cat_adjunction_family_transpose_func')
    for _ in range(10):
        arg,cursor = _atom(local_mate,cursor);args.append(arg)
    assert args[:3] == ['B','C','(Product_cat C C)']
    assert args[-2] == 'X'
    pair=args[-1]
    projected=f'(@comp_cat_fapp0 B (Product_cat C C) C (@Product_projL_func C C) {pair})'
    native_mate='(@one_cat_adjunction_family_transpose_func ' + ' '.join(args[:-2]+[projected,pair]) + ')'
    replacement=f'''@eq_ap (Functor {source} {target}) (Obj {target})
      (λ M : τ (Functor {source} {target}), @fapp0 {source} {target} M {point})
      {native_mate} {local_mate}
      (@eq_refl (Functor {source} {target}) {native_mate})'''
    return text[:start]+part[:match.start()]+replacement+part[finish:]


def migrate_native_exactness_consumer(name, original):
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
    if name == 'emdash3_2_one_cat_quotient_cokernel_zero.lp':
        text += '\n' + (AUDIT / 'production_quotient_zero_native_view.lpfragment').read_text()
    if name == 'emdash3_2_one_cat_boundary_representatives.lp':
        marker = '// The original quotient derives the boundary-representative cover without a supplied cover premise.'
        assert text.count(marker) == 1
        text = text.replace(marker, (AUDIT / 'production_boundary_quotient_zero_native_view.lpfragment').read_text() + '\n' + marker)
        matches = list(re.finditer(r'@one_cat_quotient_cokernel_zero\b', text))
        assert len(matches) == 2
        edits = []
        for match in matches:
            cursor, args = match.end(), []
            for _ in range(9):
                arg, cursor = _atom(text, cursor)
                args.append(arg)
            assert args[:2] == ['B','C'] and args[3:5] == ['C1','t']
            assert args[6:8] == ['T0','Q']
            assert ' '.join(args[2].split()) == '(@additive_preadditive C Prod t A)'
            assert ' '.join(args[5].split()) == '(@additive_terminal_object C Prod t A)'
            assert 'kernel_adjunction_family_boundary_diagram_func' in args[8]
            replacement = '@one_cat_boundary_quotient_zero_path B C ' + args[2] + ' C1 t ' + args[5] + ' T0 P Q U D h'
            edits.append((match.start(), cursor, replacement))
        for lo,hi,replacement in reversed(edits):
            text = text[:lo] + replacement + text[hi:]
    if name == 'emdash3_2_one_cat_biproduct_injection_reindex.lp':
        text = _biproduct_reindex_view(text)
    declarations = r'(?m)^(?:(?:protected|injective|constant) )?symbol\s+(\w+)'
    assertions = r'(?m)^(assert(?:not)?)\b'
    added = ADDED_PROOF_VIEWS.get(name, [])
    assert [n for n in re.findall(declarations, text) if n not in added] == re.findall(declarations, original), name
    assert all(re.findall(declarations, text).count(n) == 1 for n in added)
    assert re.findall(assertions, original) == re.findall(assertions, text), name
    return text
