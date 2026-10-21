"""Scoped native Freyd entry adaptation; qualification is on emitted LP."""
from pathlib import Path
import hashlib
import re

from production_diagram_observation_migration import B, _atom, _point_readings

AUDIT = Path(__file__).resolve().parent
FREYD = '(@CommRingFreydPresentation_cat R)'


def _alias_body(text, name, target, args):
    match = re.search(r'(?m)^\s*protected symbol ' + name + r'\b.*?;', text, re.S)
    assert match and '≔' in match.group()
    replacement = match.group().split('≔', 1)[0] + '≔ @' + target + ' ' + args + ';'
    return text[:match.start()] + replacement + text[match.end():]


def _native_review(text):
    text = re.sub(r'Functor_cat(?=\s+WalkingArrow_cat\s+C\b)', 'Functor_oplax_cat', text)
    text = re.sub(r'@Transf\s+WalkingArrow_cat\s+C\b', f'@Hom {B}', text)
    text = re.sub(r'@chain_pair_outgoing_diagram_map\b', '@chain_pair_native_diagram_map', text)
    while matches := list(re.finditer(r'\(@chain_pair_outgoing_diagram C\b', text)):
        match = matches[-1]
        cursor = match.end()
        for _ in range(5):
            _, cursor = _atom(text, cursor)
        assert text[cursor] == ')'
        term = text[match.start():cursor + 1].replace('@chain_pair_outgoing_diagram C', '@ORIGINAL_DIAGRAM C', 1)
        text = text[:match.start()] + f'(@OddDual_func WalkingArrow_cat C {term})' + text[cursor + 1:]
    text = text.replace('@ORIGINAL_DIAGRAM C', '@chain_pair_outgoing_diagram C')
    counts = tuple(len(re.findall(r'@' + h + r'\s+WalkingArrow_cat\s+C\b', text))
                   for h in ('fapp0', 'tapp0_fapp0'))
    return _point_readings(text, counts)


def _freyd_review(text):
    coeff = f'(Functor_oplax_cat WalkingArrow_cat {FREYD})'
    text = re.sub(r'Functor_cat(?=\s+WalkingArrow_cat\s+\(@CommRingFreydPresentation_cat R\))',
                  'Functor_oplax_cat', text)
    marker = '@tapp0_fapp0 WalkingArrow_cat ' + FREYD
    while marker in text:
        start = text.rfind(marker)
        cursor = start + len(marker)
        args = []
        for _ in range(4):
            value, cursor = _atom(text, cursor)
            args.append(value)
        d, e, i, h = args
        replacement = f'@fapp1_fapp0 {coeff} {FREYD} (@diagram_oplax_evaluation_at_func WalkingArrow_cat {FREYD} {i}) {d} {e} {h}'
        text = text[:start] + replacement + text[cursor:]
    marker = '@fapp1_fapp0 WalkingArrow_cat ' + FREYD
    while marker in text:
        start = text.rfind(marker)
        cursor = start + len(marker)
        args = []
        for _ in range(4):
            value, cursor = _atom(text, cursor)
            args.append(value)
        d, i, j, g = args
        assert (i, j, g) == ('walking_arrow_src', 'walking_arrow_tgt', 'walking_arrow_generator')
        text = text[:start] + f'@terminal_arrow_test_outgoing {FREYD} {d}' + text[cursor:]
    return text


def _row_constant(text):
    marker = '(@Const_transf_func'
    assert text.count(marker) == 1
    start = text.index(marker)
    cursor = start + len(marker)
    args = []
    for _ in range(4):
        value, cursor = _atom(text, cursor)
        args.append(value)
    assert text[cursor] == ')'
    K, A, x, y = args
    F, G = f'(@Const_func {K} {A} {x})', f'(@Const_func {K} {A} {y})'
    V, W = f'(Functor_cart_cat {K} {A})', f'(Functor_cat {K} {A})'
    original = text[start:cursor + 1]
    replacement = f'''(@comp_cat_fapp0 (Hom_cat {A} {x} {y})
      (Hom_cat {V} {F} {G}) (@Transf_cat {K} {A} {F} {G})
      (@fapp1_func {V} {W} (Functor_cart_include {K} {A}) {F} {G}) {original})'''
    return text[:start] + replacement + text[cursor + 1:]


def finish_freyd_entry(path, text):
    replacements = {
        'emdash3_2_hom_action_factorization_views.lp': (
            'b417366ad8909c5b5fa70a93afddb5352d298588ec48d7c74c44cbfecf478162',
            'production_hom_action_factorization_views.lpfragment'),
        'emdash3_2_one_cat_family_naturality_paths.lp': (
            'b6b7824fd788ef2506f7ce317085e5524354bc9e66c1ed44b3ed198ff4d445a5',
            'production_one_cat_family_naturality_paths.lpfragment'),
    }
    if path in replacements:
        digest, fragment = replacements[path]
        assert hashlib.sha256(text.encode()).hexdigest() == digest
        return (AUDIT / fragment).read_text()
    if path == 'emdash3_2_one_cat_diagram_family_reflection.lp':
        assert 'symbol one_cat_oplax_diagram_map_path' not in text
        return text + '\n// Shared ordinary-target views consumed by native input comparisons.\n' + (AUDIT / 'production_one_cat_oplax_reflection.lpfragment').read_text()
    if path == 'emdash3_2_one_cat_introduced_terminal_input_comparisons.lp':
        for name, target, args in (
            ('introduced_input_cart_family_func', 'one_cat_oplax_family_cart_func', 'K I C C1 D'),
            ('introduced_input_cart_family_roundtrip', 'one_cat_oplax_family_roundtrip', 'K I C C1 D'),
            ('introduced_input_oplax_map_path', 'one_cat_oplax_diagram_map_path', 'C C1 d e h k p q'),
            ('introduced_input_diagram_coefficient_func', 'one_cat_diagram_oplax_include_func', 'C C1'),
        ):
            text = _alias_body(text, name, target, args)
        return text
    if path == 'emdash3_2_one_cat_chain_pair_native_maps.lp':
        assert hashlib.sha256(text.encode()).hexdigest() == '01332ae832b9f966ee68c1342328bacb6c3b057e5ebfa73102c31544cc86105c'
        return (AUDIT / 'production_native_chain_pair_maps.lpfragment').read_text()
    if path == 'examples/one_cat_chain_pair_native_maps.lp':
        assert hashlib.sha256(text.encode()).hexdigest() == '474fd2f626121018a656740b0614258a6dc0f64fc0ae48679b1f44e9bc0a888f'
        return _native_review(text)
    if path == 'emdash3_2_one_cat_chain_pair_inputs.lp':
        assert text.count('@Transf WalkingArrow_cat C') == 1
        text = text.replace('@Transf WalkingArrow_cat C', f'@Hom {B}')
        assert text.count('Functor_cat WalkingArrow_cat C') == 1
        text = text.replace('Functor_cat WalkingArrow_cat C', 'Functor_oplax_cat WalkingArrow_cat C')
        term = '(@chain_pair_outgoing_diagram C S A B D pair)'
        assert text.count(term) == 1
        return text.replace(term, '(@OddDual_func WalkingArrow_cat C ' + term + ')')
    if path == 'emdash3_2_commutative_algebra_freyd_zero_cones.lp':
        text, count = re.subn(r'Functor_cat(?=\s+WalkingArrow_cat\s+\(@CommRingFreydPresentation_cat R\))', 'Functor_oplax_cat', text)
        assert count == 2
        return text
    if path == 'emdash3_2_commutative_algebra_freyd_adjunction_models.lp':
        assert text.count('Op_cat') == 3
        return text.replace('Op_cat', 'TotalOp_cat')
    if path == 'emdash3_2_commutative_algebra_freyd_native_row_families.lp':
        return _row_constant(text)
    if path in ('examples/freyd_native_inputs.lp', 'examples/freyd_native_maps.lp', 'examples/freyd_native_row_families.lp'):
        return _freyd_review(text)
    return None
