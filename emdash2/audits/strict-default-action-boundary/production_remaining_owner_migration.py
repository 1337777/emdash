"""Original remaining owners at the strict-default/corrected-duality foundation.
Non-library migration: preserve existing assumptions and bounded claims.
"""
import hashlib
from production_strict_wrapper_finish import calls, rename_code, ALIASES, RENAMES

SOURCES = {'emdash3_2_dependent_simplex_ordinal_adequacy.lp': 'bdbc041ebd0638f3c6932033a13cc8adcc5e4eb20aeb95ef25c4cd66fcf49890',
 'emdash3_2_dependent_simplex_ordinal_dimension3.lp': 'aaab17087fb173ecdc9a816f495e9aa66da780250dd096be3b1d04e2d00a6a70',
 'emdash3_2_dependent_simplex_ordinal_dimension4.lp': '8a1b19adc3e03fcf93ffd9263c851345eb91ddc91be03e3b2a30ee77ed225db0',
 'emdash3_2_dependent_simplex_ordinal_filler.lp': '71bcfeb5cdc96dd2fe04f2c8b513f1fc689aecb864a61bab3d39e8696d665b47',
 'emdash3_2_dependent_simplex_ordinal_recursive.lp': '2affdcd9c6f5a2d053cdf9d67a467a4dd7b144c312fce5480381cf6522e8cca7',
 'emdash3_2_path_cubical_cube3_open_box.lp': '0d6230d017a50a1bd1ff9bdb04ee44cbf49c507e1a29a2b63eb7f9d3b591e9e2',
 'emdash3_2_path_cubical_face_naturality.lp': 'dbe304811c5a68a8a3c5fe9c8370fb9a089da2cce0dd5f5b7aa0af7fb2e515df',
 'emdash3_2_path_cubical_hcomp2.lp': '3a95cff6224c49bb93fbd0e2acd762cd2d423ece51763028b834dabac96dffec',
 'emdash3_2_path_cubical_open_box_addresses.lp': '6e0a4449bc973b0f644b4b5878d6527b08c29bee2457202d08027bc3c3fee6b6',
 'emdash3_2_path_cubical_open_square_actions.lp': '9c93a0a7ebe51eef2c13be9cbc1918477697c6304952d293d3e960049c8e659a',
 'emdash3_2_path_cubical_open_square_fillers.lp': '236d8dd645d5c44c07e0f8efff0e63c664e877a0f1b0474d67604a19b6810d29',
 'emdash3_2_path_cubical_open_square_frames.lp': 'a3f11bcf39f2d16c6fb8dbb3e232d311515f0efb8108ca17b5bf4d30a285261f',
 'emdash3_2_path_cubical_open_square_restrictions.lp': 'c4c4546a162956ba31820c7ec5ecb23a8622a0a0cd9d30fa0db0f6fe6c0db2ba',
 'emdash3_2_path_cubical_open_square_sections.lp': '3f118fdf7b072fc2106b39e9a6b537a6c7af0f47d8bd9591e45130d8c0b87d4b',
 'emdash3_2_path_cubical_open_square_sieve_realization.lp': '29f964daa30746802c27d6d1b7e7ea39025dc65d42b4df7acf2f10a564ecba58',
 'emdash3_2_path_cubical_square_elim.lp': 'c4fcd2d2fc4ea0a43fbd5ae8feaf36308670b7982675b4d366f4fa85ae8500f9',
 'emdash3_2_path_cubical_structured_native_low_dimensions.lp': 'd68ba61f0450ebc9f4ec2ace692ab374569832362a1d823143fd11fa3d5aed46',
 'emdash3_2_path_cubical_structured_operators.lp': '45abcfe6beebe66481487f9ad6053907c5d784b636e589bca42e7bc6eb9ca03a',
 'emdash3_2_path_cubical_structured_recursion.lp': '695b9bfd5db5ea1b600396653ac7877a386a8f563fbb7e5eb4ff51c8fa946e4a',
 'emdash3_2_prof_reindex_terminal_normalization.lp': '57d8b259b1b0b8406f0ab9d700ba7efe2ac1824409aea6335defe3806007e3b6',
 'examples/dependent_simplex_ordinal_adequacy.lp': 'e13945c66aa0fc03d39f0fab77e0c9b76f499ec128ca26c0af812328c876c5b6',
 'examples/dependent_simplex_ordinal_dimension3.lp': 'd8cb168f9d417c345eebe48691964bd14ad57be116d13f9815c090a9d69bb92d',
 'examples/dependent_simplex_ordinal_dimension4.lp': 'fef6bd3aae9cd78f574b4f6b526be01a39639811acd5252706bac68d0a775c34',
 'examples/dependent_simplex_ordinal_filler.lp': 'eca0a564382e17282608fa44ce6c8889d766ee1e812f1c2fb68110d73b7ea1c9',
 'examples/dependent_simplex_ordinal_recursive.lp': 'fea2544c15fd41753d31f7700f468962a36dcefdd6151d0671f5cd3068714e20',
 'examples/path_cubical_cube3_open_box.lp': '50b4f85cb33f5dc83aa1468c4b7ddd28f52f09cfaada87d8b2b62af9d9613713',
 'examples/path_cubical_face_naturality.lp': 'ae6db77d975b19460366a3d79a16faf9031fe8c14140e00d894b4b955f648aae',
 'examples/path_cubical_hcomp2.lp': '264de74be2f6ca84cf8417cede03b145869af7bc8157445281a162fd1fb3c735',
 'examples/path_cubical_open_box_addresses.lp': '49586bf8101a2e91784a5132c62e60f35a17ae9d6b7ee96df12a0174e4432ee7',
 'examples/path_cubical_open_square_fillers.lp': '6dcfb88ec6c5dfb8655961f6653d8361f367edce54574246a3db82f38742c2d6',
 'examples/path_cubical_open_square_sections.lp': '84f4a481aaad0a16a2adbf84b231bab5f0ecfc9890751ed2b2d1f484229a0a14',
 'examples/path_cubical_open_square_sieves.lp': '7739d17b5377621e30999a3a94dcfcf6ffc375f09fc00e8a0cf13816fa481d1d',
 'examples/path_cubical_structured_native_low_dimensions.lp': '2fff0bc60f15373b925216788af798320e4f198dbe4c9a67e7a4a48484c220a2',
 'examples/path_cubical_structured_operators.lp': 'f38d67eef6d2bcaddc242daf9cbb30a25d244cc7e9cee42657805ae55c68a552',
 'examples/path_cubical_structured_recursion.lp': 'c232100fc0e8af80f8ee00ce59d4a91a3005f8dfcd4bb955c2ab7a143764e3e0',
 'examples/prof_reindex_terminal_normalization.lp': '89a3af3d3f7d073a0e976a52bd30f4d2731d56f1d705138a470d4979032b25ec'}

def _body(text, name, new):
    start = text.index('symbol ' + name)
    body = text.index('≔', start)
    end = text.index(';', body) + 1
    return text[:body] + '≔ ' + new + ';' + text[end:]


def migrate_remaining_owner(name, original):
    if name not in SOURCES:
        return None
    assert hashlib.sha256(original.encode()).hexdigest() == SOURCES[name], name
    text = original
    for symbol in ('strict_functor', 'strict_functor_underlying'):
        text, _ = calls(text, symbol, 3, 1, lambda args, explicit: args[-1])
    text = rename_code(text, {**ALIASES, **RENAMES})
    if name == 'emdash3_2_dependent_simplex_ordinal_adequacy.lp':
        old = '≔ @Const_func_func Terminal_cat C;'
        assert text.count(old) == 1
        text = text.replace(old, '≔ @comp_cat_fapp0 C\n'
            '    (Functor_cart_cat Terminal_cat C) (Functor_cat Terminal_cat C)\n'
            '    (Functor_cart_include Terminal_cat C) (@Const_func_func Terminal_cat C);')
    if name == 'emdash3_2_dependent_simplex_ordinal_dimension3.lp':
        start = text.index('symbol ordinal_simplex3_lhs_tele_func')
        end = text.index('symbol ordinal_simplex3_lhs_transport_path')
        text = text[:start] + text[start:end].replace('Functor_cat', 'Functor_cart_cat') + text[end:]
        # Compare the actual left route with its own capped presentation.
        # The former use of an unconditional left/middle equality is invalid
        # for the retained conventional lax action. No such equality is restored.
        text = _body(text, 'ordinal_simplex3_transport_at_second', 'ordinal_simplex3_top_lhs_func')
        proof = '@eq_refl\n' + (
            '    (Functor\n'
            '      (Hom_cat ordinal_simplex3_source_pathout_cat\n'
            '        ordinal_simplex3_raw_obj ordinal_simplex3_stable_obj)\n'
            '      (Hom_cat ordinal_simplex3_target_pathout_cat\n'
            '        ordinal_simplex3_e01 ordinal_simplex3_e03))\n'
            '    ordinal_simplex3_top_lhs_func')
        text = _body(text, 'ordinal_simplex3_lhs_tele_transport_path', proof)
        text = _body(text, 'ordinal_simplex3_lhs_transport_path', proof)
        old = '// Whole left transport telescope and its projection to the capped owner.'
        assert text.count(old) == 1
        text = text.replace(old, old + '\n'
            '// The retained left/post route is compared with itself, not with the strict\n'
            '// pre/right middle action of an arbitrary displayed transformation.')
    if name == 'emdash3_2_prof_reindex_terminal_normalization.lp':
        # Both original telescopes now land in Cartesian mapping categories.
        # Keep ordinary fixed evaluation by composing the existing inclusion.
        index = '(Hom_cat A W X)'
        terminal = '(Hom_cat Terminal_cat Terminal_obj Terminal_obj)'
        pair = f'(Product_cat {index} {terminal})'
        cart = f'(Functor_cart_cat {terminal} {pair})'
        ambient = f'(Functor_cat {terminal} {pair})'
        text = _body(text, 'prof_terminal_reversed_base_hom_func',
            f'@comp_cat_fapp0 {index} {cart} {pair}\n'
            f'    (@comp_cat_fapp0 {cart} {ambient} {pair}\n'
            f'      (@fapp0_func {terminal} {pair} Terminal_obj)\n'
            f'      (Functor_cart_include {terminal} {pair}))\n'
            f'    (@Product_pair_tele_func {index} {terminal})')
        source = '(Hom_cat B (@fapp0 A B F X) (@fapp0 Terminal_cat B G Terminal_obj))'
        target = '(Hom_cat B (@fapp0 A B F W) (@fapp0 Terminal_cat B G Terminal_obj))'
        cart = f'(Functor_cart_cat {source} {target})'
        ambient = f'(Functor_cat {source} {target})'
        text = _body(text, 'prof_terminal_expected_source_func',
            f'@comp_cat_fapp0 {index} {cart} {target}\n'
            f'    (@comp_cat_fapp0 {cart} {ambient} {target}\n'
            f'      (@fapp0_func {source} {target} g)\n'
            f'      (Functor_cart_include {source} {target}))\n'
            '    (@hom_precomp_along_tele_func A B F\n'
            '      (@fapp0 Terminal_cat B G Terminal_obj) W X)')
        old = '// lhs-audit: keep 1,2 -- exact hom source/codomain guard this component.\nrule @tapp0_fapp0\n      (Hom_cat $A $W $X)\n      (Hom_cat $B\n        (@fapp0 $A $B $F $W)\n        (@fapp0 Terminal_cat $B $G Terminal_obj))\n      _ _ $p'
        new = '// The constructor carries A,B,F,G,W,X; infer the component endpoints.\n// Compound endpoint guards lose this beta when Hom/identity projects first.\nrule @tapp0_fapp0\n      _ _\n      _ _ $p'
        assert text.count(old) == 1
        text = text.replace(old, new, 1)
    if name in ('emdash3_2_prof_reindex_terminal_normalization.lp',
                'examples/prof_reindex_terminal_normalization.lp'):
        # These occurrences are family-valued Hom/Pi action and their component
        # observations; no occurrence denotes an unrelated universe object.
        text = text.replace('Cat_cat', 'Cat_cart')
    return text
