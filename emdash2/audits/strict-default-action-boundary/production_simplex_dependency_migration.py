"""Migrate existing simplex consumers of the selected Sigma/Hom owners.

This is source replay, not a new nerve construction or a proof checker.
The original complete reviewers qualify the emitted LP at its module owner.
"""
from pathlib import Path
import re

from production_strict_wrapper_finish import ALIASES, RENAMES, calls, remove_decl, rename_code


JOIN_ALIASES = {
    'strict_join_fst': 'join_fst_func',
    'strict_join_snd': 'join_snd_func',
    'strict_join_map': 'join_map_func',
}
RETIRED_JOIN_DECLARATIONS = list(JOIN_ALIASES) + [
    'join_fst_is_strict', 'join_snd_is_strict', 'join_map_is_strict',
]


def _replace(text, old, new, count=1):
    assert text.count(old) == count, (old, text.count(old), count)
    return text.replace(old, new)


def migrate_simplex_dependency(path, text):
    if path == 'emdash3_2_dependent_simplex_path_associator.lp':
        for old, new, count in (
            ('(@hom_int_precomp_func Z Z (@id_func Z) x1 x0 f)',
             '(@Rep_transport_func Z x0 x1 f)', 5),
            ('(@hom_int_precomp_func Z Z (@id_func Z) x2 x1 g)',
             '(@Rep_transport_func Z x1 x2 g)', 6),
        ):
            text = _replace(text, old, new, count)
        return text
    if path == 'emdash3_2_simplex_shapes.lp':
        for name in RETIRED_JOIN_DECLARATIONS:
            text, removed = remove_decl(text, name)
            assert removed, name
        text, _ = calls(text, 'strict_functor_underlying', 3, 1, lambda a, _: a[-1])
        text = rename_code(text, {**ALIASES, **JOIN_ALIASES})
        text = text.replace('// Supplied strictness of the existing left join inclusion.',
                            '// Join inclusions and maps use the public strict-functor default.')
        text = text.replace('// Supplied strictness of the existing right join inclusion.', '')
        text = text.replace('// Supplied strictness closure of the existing join map.', '')
        text = text.replace('strict-profile whole functor', 'default-strict whole functor')
        text = text.replace('strict-profile\n', 'default-strict\n')
        return re.sub(r'\n[ \t]*\n(?:[ \t]*\n)+', '\n\n', text).rstrip() + '\n'
    if path == 'emdash3_2_dependent_simplex_bridge.lp':
        text = text.replace('Op_cat', 'TotalOp_cat').replace('Op_func', 'TotalOp_func')
        text = _replace(text, '≔ @homd_ K E E (@id_funcd K E) x u y v;',
                        '≔ @TotalOp_catd (Op_cat (Hom_cat K x y))\n'
                        '    (@homd_ K E E (@id_funcd K E) x u y v);')
        start = text.index('≔ @homd_', text.index('symbol DependentTriangleImage_catd'))
        end = text.index(';', start)
        body = text[start + 2:end]
        text = (text[:start] + '≔ @TotalOp_catd (Op_cat (Hom_cat K x y))\n'
                + '    (' + body + ');' + text[end + 1:])
        start = text.index('≔ @TotalOp_func', text.index('symbol dependent_triangle_map'))
        end = text.index(';', start)
        text = text[:start] + '''≔ @fapp1_func (@Sigma_cat K E) (@Sigma_cat K D)
    (@sigma_map_func K E D FF)
    (@Struct_sigma (Obj K) (λ k : τ (Obj K), Obj (Fibre_cat E k)) x u)
    (@Struct_sigma (Obj K) (λ k : τ (Obj K), Obj (Fibre_cat E k)) y v)''' + text[end:]
        text = text.replace('First dependent-hom simplex family for fixed total endpoints.',
                            'Negative total-index family from the existing dependent Hom.\n'
                            '// Total fibre duality and the outer total dual restore the forward fillers.')
        text = text.replace('Whole first action. The displayed map is the active internal-action\n'
                            '// projection, not a separately postulated transformation.',
                            'Whole first action at the existing Sigma-map Hom owner. Its projection\n'
                            '// uses Homd_index_sigma_func and the actual internal-action presheaf arrow.')
        action = Path(__file__).with_name('production_triangle_family_action.lpfragment').read_text()
        return _replace(text, 'symbol DependentTriangleImage_cat\n',
                        action + '\n' + 'symbol DependentTriangleImage_cat\n')
    if path not in {
        'examples/dependent_simplex_bridge.lp',
        'examples/dependent_simplex_profiles.lp',
        'examples/dependent_simplex_represented_source.lp',
        'examples/simplex_shapes.lp',
    }:
        return None
    if path != 'examples/simplex_shapes.lp':
        text = text.replace('Op_cat (Hom_cat K', 'TotalOp_cat (Hom_cat K')
    if path in {'examples/dependent_simplex_profiles.lp', 'examples/simplex_shapes.lp'}:
        for name in ('strict_functor', 'strict_functor_underlying'):
            text, _ = calls(text, name, 3, 1, lambda a, _: a[-1])
        text = rename_code(text, {**ALIASES, **RENAMES})
    if path == 'examples/dependent_simplex_profiles.lp':
        text = _replace(text, 'assertnot [A B : Cat]', 'assert [A B : Cat]')
        text = text.replace('// General ambient functors retain distinct compositor endpoints, so the cell\n'
                            '// is not even homogeneously comparable with an identity.',
                            '// Default strict functors identify the existing compositor endpoints.')
        text = text.replace('// A classified strict object reconstructs canonical evidence about the\n'
                            '// same whole intrinsic compositor without projecting an admission witness.',
                            '// The public default reconstructs canonical evidence about the same\n'
                            '// whole intrinsic compositor, with no strict-object wrapper.')
        text = text.replace('General lax, selected strict, and Path readings',
                            'Default strict-functor and Path readings')
    if path in {'examples/dependent_simplex_bridge.lp',
                'examples/dependent_simplex_represented_source.lp'}:
        args = ('K E D FF x u y v' if path == 'examples/dependent_simplex_bridge.lp'
                else 'K E D FF x0 u0 x3 u3')
        text = _replace(text, '(@fdapp1_int_presheaf_arrow ' + args + ')',
                        '(@dependent_triangle_map_catd ' + args + ')')
    return text
