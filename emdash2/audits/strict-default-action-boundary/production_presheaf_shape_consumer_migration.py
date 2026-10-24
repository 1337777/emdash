"""Pinned original presheaf/shape consumers at the Cartesian family coefficient.

Non-library migration recipe. Preserve whole actions, selected face comparisons,
all original assertions and the bounded application claims; no new nerve theorem.
The two parent inputs are hashed after the existing shape-consumer migration.
"""
import hashlib
import re
from production_strict_wrapper_finish import calls, rename_code, ALIASES, RENAMES

SOURCES = {'emdash3_2_coherent_nerve_levels.lp': '72518af925e32082eba399dcd34aba77a8cbcc826f3777f78a15ba13338cb728',
 'emdash3_2_cubical.lp': '78447a091fd06a01888586989833a688d8e771175ffffa594f0d20f79d4d4edb',
 'emdash3_2_cubical_face_addresses.lp': 'ecf08ecc22f91215b59bdbc47100f53b952f2b0163f2680bc17098686b86da65',
 'emdash3_2_cubical_open_box_sieves_recursive.lp': '3c9dd04009e4cc22fced011ed81a3f3ff128c8f437fa4fafb272bafdc2fa08d3',
 'emdash3_2_cubical_yoneda.lp': 'b23a0f750eca99eda2da332b95d2d97e34ca705237ec3083cf7e99aa1c610635',
 'emdash3_2_path_cubical_levels.lp': 'cc777cbc5d196b0ad0ac39305c6ef49cbb0ef070f658fbdde8132586509e1a94',
 'emdash3_2_path_cubical_nerve.lp': '0890ca57fd0462a7eafb72b4eabc1cc6b030bdc4a77ed470890cdaa19bcd815f',
 'emdash3_2_path_cubical_open_square_sieves.lp': '7d8d86aafe0b9f7eb75ef6c20869ccb7b9828e7f6b4f739576f17424b2c8c0cd',
 'emdash3_2_path_cubical_square_comparison.lp': 'ef72ed68bc949edeb07d84687283afa8403bab488513a7ff4cbbf9c927807997',
 'emdash3_2_path_cubical_square_readback.lp': '2df1673d0764dd105a3d206ebc2748adc02600ce46c6a09883b06cdd5c254869',
 'emdash3_2_path_cubical_successor_elim.lp': 'ac8cf1384ef11e0b91308d33260fee50042ceeee58e1fa79f16cbb81a702b207',
 'emdash3_2_path_groupoid_2horn_fillers.lp': '4012837783b172b01cf3ea248b5417c03cd87a5d9471d11a9650c7ec7bd1d963',
 'emdash3_2_semicubical_representables.lp': 'f20de426fd8341d9bc65e8b63fa62450084b8db0a62650a06077d80f74a7e539',
 'emdash3_2_semisimplicial_decalage.lp': '02c9db841fa82aba422ba5aeb7250f5fe34b3e2283df4ed65a0e3db24ebab1af',
 'emdash3_2_semisimplicial_diagrams.lp': 'e1bf722b5a02fd505c96cc235bef53133dc4d4c64bc12cdd157dd1969613bb8f',
 'emdash3_2_simplex2_sieves.lp': '275de07640bcf996d7c2418ba371401559ff0b288c01ccaedf9e504116ab95fe',
 'emdash3_2_tetrahedron_faces.lp': '6bd9b90532d92386c52b1985bc238cf2d63423acaede092ce378c664aa283491',
 'examples/coherent_nerve_levels.lp': 'ca8226769f6abb5e69fa4282f5cc8ba7715f013cc34c2d5c32808434e2ad8ed1',
 'examples/cubical_facade.lp': '393e716fe1c1e6472abb3dfec668133da0984f4cc68cda1ce7ef490224329ea1',
 'examples/cubical_face_addresses.lp': '14b517e895955f54a0c43fb33c5cea856a626ac0b1e1339e10a988218f59a7ac',
 'examples/cubical_open_box_sieves_recursive.lp': 'cfc16c2d6c46b9f12e34db2db8b28da338e7098414bb80b30302bd009b9bb8a4',
 'examples/cubical_yoneda.lp': '1a3da103b7e3cc4afb9610d8c6443ec34b6dc910160bfd86b7f2081a28edb5d5',
 'examples/face_realization.lp': 'bfac5ba70602efc851f19429c412ec0b9b519585c18b6f7b619e9d668ffd44b0',
 'examples/path_cubical_levels.lp': '7a4cb725df659c6fc1e1d5a8257462a5b286c87ded0ce89a780a4c4b9f6bd2e7',
 'examples/path_cubical_nerve.lp': 'd06756560a679b54c117e0417d25a7f779e43276dcfa1a34628b5bc8a82c503e',
 'examples/path_cubical_square_comparison.lp': 'a102584b55047dc62086a11acdee6fd755302baf9e81482bca217ef6d3f32d3c',
 'examples/path_cubical_square_readback.lp': '9abbb90c8a26731685ae9d13636a5a9e3cb829027b0aa642cd5f5ce38bc1c225',
 'examples/path_cubical_successor_elim.lp': '5212833c9029a92ea02cc6306cf805a19f4963c2aaa04b3a74f1e71737c5b6bd',
 'examples/path_groupoid_2horn_fillers.lp': '3e21b6eb034de3e5f6b60a0254340dea09ffa431fab9de6823e4226c51cd9ae9',
 'examples/semicubical_representables.lp': 'c7aed37bfbb63105d605baa0abbdc283d86aa6cbbf5c6799da306c3e9cee5028',
 'examples/semisimplicial_decalage.lp': 'a771fa566d132011bb01b00687e24d3f3c71cf484db5d9163d9d435f039a3dac',
 'examples/semisimplicial_diagrams.lp': '36e14f525cb7b9312c005a9d2efc3b711407ac195ec3c7084d79e1d808fa0c96',
 'examples/simplex2_boundary_horns.lp': 'a0ccc5da280b4a036f8ad1ece0d13d1230af40697318a07c1c366e4fb5599921',
 'examples/tetrahedron_faces.lp': '5abe419c361b60635bd130633b1cf425181b14ffea6bbfe0653978a7fe617f0d'}

PARENT_INPUTS = {'emdash3_2_semicubical_nerve.lp': '06145945a97ee24ea558e9ebe02c93e54098a5344df2ccef0699652412a78396',
 'examples/semicubical_nerve.lp': '41c613e191579f69d33019ff771062c4a23aaef8a466ecec88097d2ee0ac9b0c'}

def _replace_once(text, old, new):
    assert text.count(old) == 1, old
    return text.replace(old, new, 1)


def migrate_presheaf_shape_consumer(name, original):
    if name not in SOURCES:
        return None
    assert hashlib.sha256(original.encode()).hexdigest() == SOURCES[name], name
    text = original
    if name in ('emdash3_2_semisimplicial_diagrams.lp', 'examples/semisimplicial_diagrams.lp'):
        text = re.sub(r'\bCat_cat\b', 'Cat_cart', text)
        text = re.sub(r'\bPath_cat_func\b', 'Path_cat_cart_func', text)
    if name in ('emdash3_2_tetrahedron_faces.lp', 'examples/tetrahedron_faces.lp'):
        text, count = calls(text, 'strict_functor_underlying', 3, 1, lambda args, explicit: args[-1])
        assert count == (4 if name.startswith('examples/') else 0)
        text = rename_code(text, {**ALIASES, **RENAMES,
            'strict_join_fst': 'join_fst_func', 'strict_join_map': 'join_map_func'})
    if name == 'emdash3_2_semicubical_representables.lp':
        text = _replace_once(text, '    Cat_cat\n    (@StandardSemicube n)',
            '    Cat_cart\n    (@StandardSemicube n)')
        start = text.index('≔ @fapp1_func', text.index('symbol standard_semicube_native_decode_func'))
        end = text.index(';', start) + 1
        text = text[:start] + '''≔ @comp_cat_fapp0
    (@standard_semicube_level n p)
    (Functor_cart_cat (@CubicalLevel_cat C n) (@CubicalLevel_cat C p))
    (Functor_cat (@CubicalLevel_cat C n) (@CubicalLevel_cat C p))
    (Functor_cart_include (@CubicalLevel_cat C n) (@CubicalLevel_cat C p))
    (@fapp1_func
      (Op_cat SemiCubePlus_cat) Cat_cart
      (@semicubical_nerve_func C) n p);''' + text[end:]
    if name == 'emdash3_2_cubical_yoneda.lp':
        start = text.index('≔ @fib_cov_transf')
        end = text.index(';', start) + 1
        text = text[:start] + '''≔ @strict_transfor _ _ _ _
    (@fib_cov_transf
      (Op_cat SemiCubePlus_cat)
      (@semicubical_nerve_func C) n X);''' + text[end:]
    if name in ('emdash3_2_cubical_yoneda.lp', 'emdash3_2_path_cubical_nerve.lp', 'examples/path_cubical_nerve.lp'):
        text = re.sub(r'(\(Op_cat SemiCubePlus_cat\)\s+)Cat_cat', r'\1Cat_cart', text)
    if name == 'examples/simplex2_boundary_horns.lp':
        start = text.index('// One next action')
        end = text.index('// Generic pullback', start)
        part = text[start:end]
        assert part.count('Cat_cat') == 1 and part.count('Functor_cat') == 1
        text = text[:start] + part.replace('Cat_cat', 'Cat_cart').replace('Functor_cat', 'Functor_cart_cat') + text[end:]
    return text


def refine_presheaf_shape_parent(name, previous):
    if name not in PARENT_INPUTS:
        return None
    assert hashlib.sha256(previous.encode()).hexdigest() == PARENT_INPUTS[name], name
    if name.startswith('examples/'):
        return re.sub(r'(\(Op_cat SemiCubePlus_cat\)\s+)Cat_cat', r'\1Cat_cart', previous)
    text = re.sub(r'\bCat_cat\b', 'Cat_cart', previous)
    # These equality classifiers still have the original ordinary functor objects.
    text = text.replace('Hom Cat_cart', 'Hom Cat_cat')
    text = text.replace('(@semicubical_nerve_func Cat_cart)', '(@semicubical_nerve_func Cat_cat)')
    text = _replace_once(text, 'rule @fapp0\n      (Op_cat SemiCubePlus_cat) Cat_cart', 'rule @fapp0\n      _ _')
    text = _replace_once(text, '  ambient normal-lax identity path and named composition component,',
        '  default identity path and composition law,')
    text = _replace_once(text,
        '  This module adds the nerve object beta; composition uses the strict default. It adds no runtime face-action beta, face-specific equation, broad',
        '''  The coefficient is Cat_cart, as required for the existing presheaf and
  Yoneda consumers. The base Homs are path categories of set-valued face
  codes; their higher actions come from equality, so this does not require
  strict naturality for arbitrary base transformations.

  This module adds the nerve object beta; composition uses the strict default.
  It adds no runtime face-action beta, face-specific equation, broad''')
    anchor = 'require open emdash.emdash3_2_semicubical_face_action;'
    text = _replace_once(text, anchor, anchor + '\nrequire open emdash.emdash3_2_strict_functor_actions;')
    start = text.index('symbol semicubical_nerve_composition_path')
    body = text.index('≔', start)
    end = text.index(';', body) + 1
    text = text[:body] + '''≔ @functor_composition_path
    (Op_cat SemiCubePlus_cat) Cat_cart
    (@semicubical_nerve_func C) X Y Z g f;''' + text[end:]
    return text
