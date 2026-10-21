"""Migrate original zero-arrow consumers through existing whole owners.

This is a scoped authoring adapter. Qualification belongs to its emitted LP,
not to these textual substitutions. No formal rewrite/unification rule is added.
"""
import re
from pathlib import Path

from production_diagram_observation_migration import (
    B, E0, E1, EPS, _atom, _body, _profile, _point_readings,
)


def _encode(functor):
    return f'(@OddDual_func WalkingArrow_cat C {functor})'


def _arrow_objects(text):
    pattern = r'\(@walking_arrow_func C [A-Za-z0-9_]+ [A-Za-z0-9_]+ [A-Za-z0-9_]+\)'
    return re.sub(pattern, lambda m: _encode(m.group()), text)


def _inputs(text):
    old = '   form actual diagram transformations before any universal operation.'
    assert text.count(old) == 1
    text = text.replace(old,
        '   reuse the existing Cartesian square action and its oplax inclusion\n'
        '   before any universal operation. The actual terminal/initial diagram\n'
        '   object is decoded for that action; no equality transport is supplied.')
    assert text.count('(Op_cat C)') == 1
    text = text.replace('(Op_cat C)', '(TotalOp_cat C)')
    for name, source, target in (
        ('terminal_zero_composite_transf',
         f'(@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) (@fapp0 C {B} (@terminal_arrow_diagram_func C t T) X))',
         '(@walking_arrow_func C A B d)'),
        ('initial_zero_composite_transf',
         '(@walking_arrow_func C A B d)',
         f'(@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) (@fapp0 C {B} (@initial_arrow_diagram_func C t T) X))'),
    ):
        match = re.search(r'(?m)^symbol ' + name + r'\b.*?;', text, re.S)
        assert match
        decl, body = match.group()[:-1].split('≔', 1)
        decl = decl.replace('@Transf WalkingArrow_cat C', '@Hom ' + B)
        decl = decl.replace('(Functor_cat WalkingArrow_cat C)', B)
        decl = _arrow_objects(decl)
        cursor = body.index('@one_cat_square_diagram_transf') + len('@one_cat_square_diagram_transf')
        args = []
        for _ in range(11):
            arg, cursor = _atom(body, cursor)
            args.append(arg)
        assert args[:2] == ['C', 'C1']
        x0, x1, y0, y1, u, v, a, b, alpha = args[2:]
        cart = '(@one_cat_arrow_cart_diagram_func C C1)'
        new_body = f'''≔ @fapp1_fapp0 (Functor_cart_cat WalkingArrow_cat C) {B}
    (Functor_cart_oplax_include WalkingArrow_cat C) {source} {target}
    (@fapp1_fapp0 (@LaxArrow_cat C) (Functor_cart_cat WalkingArrow_cat C)
      {cart} (@lax_edge C {x0} {y0} {u}) (@lax_edge C {x1} {y1} {v})
      (@lax_square C {x0} {x1} {y0} {y1} {u} {v} {a} {b} {alpha}));'''
        text = text[:match.start()] + decl + new_body + text[match.end():]
    # This constructor's argument is a diagram object in the new coefficient.
    a = text.index('symbol zero_composite_native_cone')
    text = text[:a] + _arrow_objects(text[a:])
    return text


def _input_reviewer(text):
    assert text.count('(Functor_cat WalkingArrow_cat C)') == 16
    assert text.count('(Op_cat C)') == 3
    assert len(re.findall(r'\(@walking_arrow_func C [A-Za-z0-9_]+ [A-Za-z0-9_]+ [A-Za-z0-9_]+\)', text)) == 26
    text = text.replace('(Functor_cat WalkingArrow_cat C)', B)
    text = text.replace('(Op_cat C)', '(TotalOp_cat C)')
    return _arrow_objects(text)


def _raw_input_reviewer(text):
    anchor = '// The kernel-side input retains its incoming arrow and zero tip.'
    first = text.index(anchor)
    prefix, tail = text[:first], text[first:]
    tail = _point_readings(_profile(tail, (2, 0, 1, 2)), (0, 4))
    tail = _arrow_objects(tail)
    old = '≡ @walking_arrow_func C A B d;'
    assert tail.count(old) == 1
    tail = tail.replace(old, '≡ @OddDual_func WalkingArrow_cat C (@walking_arrow_func C A B d);')
    return prefix + tail


def _inverse_profiles(text, counts, ordinary_targets):
    text = _profile(text, counts)
    old = '@one_cat_functor_category WalkingArrow_cat C C1'
    assert text.count(old) == ordinary_targets
    return text.replace(old, '@one_cat_oplax_functor_category WalkingArrow_cat C C1')


def _map_paths(text):
    text = _inverse_profiles(text, (100, 5, 18, 0), 1)
    m = re.search(r'(?m)^symbol one_cat_zero_cone_map_rebuild_path\b.*?;', text, re.S)
    assert m
    body = m.group().split('≔', 1)[1]
    start = body.index('@sigma_ind _ _') + len('@sigma_ind _ _')
    motive, _ = _atom(body, start)
    start = body.index('(λ v : τ _, λ alpha : τ _,')
    lam, _ = _atom(body, start)
    inner = lam[len('(λ v : τ _, λ alpha : τ _,'): -1].strip()
    # Preserve the original constructor branch and its filler. Type each map
    # through the existing native owner before specializing the Sigma proof.
    inner, count = re.subn(r'\(Struct_sigma\s+u\s+\(Struct_sigma\s+v\s+alpha\)\)',
        '(@zero_cone_native_map C t T a0 a1 d0 d1 h0 h1 u v alpha)', inner)
    assert count == 3
    j0 = f'(@fapp0 C {B} (@terminal_arrow_diagram_func C t T) a0)'
    j1 = f'(@fapp0 C {B} (@terminal_arrow_diagram_func C t T) a1)'
    ja = f'(@fapp1_fapp0 C {B} (@terminal_arrow_diagram_func C t T) a0 a1 u)'
    alpha = f'(Hom (Hom_cat {B} {j0} d1) (@comp_fapp0 {B} {j0} d0 d1 v h0) (@comp_fapp0 {B} {j0} {j1} d1 h1 {ja}))'
    new = f'''@represented_comma_map_ind C {B} (@terminal_arrow_diagram_func C t T)
        a0 a1 d0 d1 h0 h1 {motive}
        (λ u : τ (Hom C a0 a1), λ v : τ (Hom {B} d0 d1),
          λ alpha : τ {alpha}, {inner}) m'''
    return _body(text, 'one_cat_zero_cone_map_rebuild_path', new)


def _chain(text):
    text = _point_readings(_profile(text, (72, 0, 0, 0)), (19, 6))
    old = '@one_cat_functor_category WalkingArrow_cat C C1'
    assert text.count(old) == 1
    text = text.replace(old, '@one_cat_oplax_functor_category WalkingArrow_cat C C1')
    z = '(@ZeroArrowCone_cat C t T)'
    d = '(@zero_arrow_cone_diagram_func C t T)'
    d0 = f'(@fapp0 {z} {B} {d} z0)'
    d1 = f'(@fapp0 {z} {B} {d} z1)'
    h = f'(@fapp1_fapp0 {z} {B} {d} z0 z1 m)'
    return _body(text, 'zero_arrow_cone_map_lower_path',
                 f'@one_cat_component_naturality_path {B} C C1\n'
                 f'    {E0} {E1} {EPS} {d0} {d1} {h}')


def _universal(text):
    return _point_readings(_profile(text, (2, 2, 2, 1)), (12, 0))


def _chain_reviewer(text):
    text = _point_readings(_profile(text, (14, 3, 9, 0)), (12, 2))
    family = f'(@represented_comma_prof C {B} (@terminal_arrow_diagram_func C t T))'
    assert text.count(family) == 3
    raw_view = f'''(@comp_cat_fapp0 (Op_cat C) (Functor_cart_cat {B} Cat_cart)
      (Catd_cat {B}) (Functor_cart_include {B} Cat_cart) {family})'''
    text = text.replace(family, raw_view)
    old = '(Struct_sigma a (Struct_sigma b theta))'
    assert text.count(old) == 3
    text = text.replace(old, f'(@reviewer_represented_homdc_map C {B} (@terminal_arrow_diagram_func C t T) A0 A1 d0 d1 h0 h1 a b theta)')
    anchor = 'require open emdash.emdash3_2_zero_arrow_cone_chain_pairs;'
    assert text.count(anchor) == 1
    helper = Path(__file__).with_name('production_zero_arrow_frame_reviewer.lpfragment').read_text()
    return text.replace(anchor, anchor + '\nrequire open emdash.emdash3_2_zero_arrow_cone_maps;\n' + helper)


def share_arrow_cart_owner(text):
    """Name the already present Cartesian body; keep one semantic definition."""
    anchor = 'symbol one_cat_arrow_diagram_func\n'
    assert text.count(anchor) == 1
    start = text.index('(@sym_func WalkingArrow_cat (@LaxArrow_cat C) C', text.index(anchor))
    cart, _ = _atom(text, start)
    assert text.count(cart) == 1
    text = text.replace(cart, '(@one_cat_arrow_cart_diagram_func C C1)', 1)
    shared = ('// The existing Cartesian construction, shared by its ordinary and oplax views.\n// This is a semantic definition; it adds no new action or computation rule.\nsymbol one_cat_arrow_cart_diagram_func\n  [C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))\n  : τ (Functor (@LaxArrow_cat C) (Functor_cart_cat WalkingArrow_cat C))\n≔ ' + cart[1:-1] + ';\n\n')
    return text.replace(anchor, shared + anchor, 1)


def migrate_zero_arrow_input(path, text):
    adapters = {
        'emdash3_2_one_cat_zero_arrow_inputs.lp': _inputs,
        'examples/kernel_cokernel_adjunction_observations.lp': _input_reviewer,
        'examples/one_cat_zero_arrow_inputs.lp': _raw_input_reviewer,
        'emdash3_2_zero_arrow_cone_chain_pairs.lp': _chain,
        'emdash3_2_zero_arrow_universal_tests.lp': _universal,
        'examples/one_cat_zero_cone_maps.lp': _chain_reviewer,
        'emdash3_2_one_cat_zero_cone_map_paths.lp': _map_paths,
        'emdash3_2_one_cat_zero_cone_map_equivalences.lp': lambda t: _inverse_profiles(t, (31, 4, 10, 0), 3),
        'examples/one_cat_zero_cone_map_equivalences.lp': lambda t: _inverse_profiles(t, (30, 6, 12, 0), 0),
    }
    return adapters[path](text) if path in adapters else None
