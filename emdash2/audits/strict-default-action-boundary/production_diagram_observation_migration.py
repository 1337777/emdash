"""Scoped source adaptation of existing diagram observations; no formal rules.

The emitted LP is qualified at the original module positions. This helper
only rewrites the recorded original declarations and is not a proof checker.
"""
import re


B = '(Functor_oplax_cat WalkingArrow_cat C)'
E0 = '(@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)'
E1 = '(@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)'
EPS = '(@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator)'
J = f'(@fapp0 C {B} (@terminal_arrow_diagram_func C t T) A)'
I = f'(@fapp0 C {B} (@initial_arrow_diagram_func C t T) A)'


def _profile(text, counts):
    replacements = (
        (r'Functor_cat(?=\s+WalkingArrow_cat\s+C\b)', 'Functor_oplax_cat'),
        (r'\(Functor WalkingArrow_cat C\)', f'(Obj {B})'),
        (r'@Transf\s+WalkingArrow_cat\s+C\b', f'@Hom {B}'),
        (r'\(Op_cat C\)', '(TotalOp_cat C)'),
    )
    for (pattern, replacement), count in zip(replacements, counts):
        text, actual = re.subn(pattern, replacement, text)
        assert actual == count, (pattern, actual, count)
    return text


def _atom(text, i):
    while text[i].isspace():
        i += 1
    start = i
    if text[i] == '(':
        depth = 1
        i += 1
        while depth:
            depth += (text[i] == '(') - (text[i] == ')')
            i += 1
    else:
        while i < len(text) and not text[i].isspace() and text[i] not in '();':
            i += 1
    return text[start:i], i


def _point_readings(text, counts):
    # Fixed evaluation of an arrow in the oplax mapping category is ordinary
    # functor action. Keep the actual whole evaluation as the owner.
    for (head, arity), expected in zip((('fapp0', 2), ('tapp0_fapp0', 4)), counts):
        pattern = r'@' + head + r'\s+WalkingArrow_cat\s+C\b'
        count = 0
        while matches := list(re.finditer(pattern, text)):
            match = matches[-1]
            cursor = match.end()
            args = []
            for _ in range(arity):
                value, cursor = _atom(text, cursor)
                args.append(value)
            if head == 'fapp0':
                functor, point = args
                replacement = f'@fapp0 {B} C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C {point}) {functor}'
            else:
                source, target, point, cell = args
                replacement = f'@fapp1_fapp0 {B} C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C {point}) {source} {target} {cell}'
            text = text[:match.start()] + replacement + text[cursor:]
            count += 1
        assert count == expected, (head, count, expected)
    return text


def _body(text, name, body):
    match = re.search(r'(?m)^symbol ' + name + r'\b.*?;', text, re.S)
    assert match and match.group().count('≔') == 1
    return (text[:match.start()] + match.group().split('≔', 1)[0]
            + '≔ ' + body + ';' + text[match.end():])


def _zero_observations(text):
    text = _profile(text, (9, 8, 7, 8))
    # These four raw component bodies are replaced below, so only their
    # point-object readings are changed by the shared scanner here.
    for point, evaluator, expected in (('walking_arrow_src', E0, 12),
                                       ('walking_arrow_tgt', E1, 13)):
        text, count = re.subn(r'@fapp0\s+WalkingArrow_cat\s+C\s+d\s+' + point,
                             f'@fapp0 {B} C {evaluator} d', text)
        assert count == expected
    for name, body in (
        ('terminal_arrow_test_incoming', f'@fapp1_fapp0 {B} C {E0} {J} d h'),
        ('terminal_arrow_test_tip', f'@fapp1_fapp0 {B} C {E1} {J} d h'),
        ('terminal_arrow_test_outgoing', f'@tapp0_fapp0 {B} C {E0} {E1} d {EPS}'),
        ('terminal_arrow_test_naturality_path',
         f'@eq_sym _ _ _\n    (@one_cat_component_naturality_path {B} C C1\n      {E0} {E1} {EPS} {J} d h)'),
        ('initial_arrow_test_outgoing', f'@fapp1_fapp0 {B} C {E1} d {I} h'),
        ('initial_arrow_test_tip', f'@fapp1_fapp0 {B} C {E0} d {I} h'),
    ):
        text = _body(text, name, body)
    start = text.index('symbol initial_arrow_test_chain_path')
    match = re.search(r'\(@eq_sym _ _ _ \(@one_cat_component_naturality_path\b', text[start:])
    assert match
    begin = start + match.start()
    _, end = _atom(text, begin)
    replacement = f'(@one_cat_component_naturality_path {B} C C1\n      {E0} {E1} {EPS} d {I} h)'
    text = text[:begin] + replacement + text[end:]
    text = text.replace('Hom(Op(C),t,t) versus Hom(C,t,t)',
                        'Hom(TotalOp(C),t,t) versus Hom(C,t,t)')
    old = '   Raw arrow observations keep their original unrestricted signatures.'
    assert text.count(old) == 1
    return text.replace(old,
        '   Raw projections keep unrestricted C; diagrams use the existing oplax coefficient.')


def _point_terms():
    total = '(@ZeroArrowCone_cat C t T)'
    global_boundary = '(@kernel_adjunction_family_boundary_diagram_func K C S t T P A D h)'
    universal_boundary = f'(@kernel_adjunction_family_boundary_diagram_func {total} C S t T P (@zero_arrow_cone_first_func C t T) (@zero_arrow_cone_diagram_func C t T) (@zero_arrow_cone_universal_transf C C1 t T))'
    point = '(@zero_arrow_family_point_input K C t T A D h x)'
    decode = lambda term: '(@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) ' + term + ')'
    d0 = decode(f'(@fapp0 K {B} {global_boundary} x)')
    d1 = decode(f'(@fapp0 {total} {B} {universal_boundary} {point})')
    forward = '(@homology_family_global_boundary_point_map K C S C1 t T P A D h x)'
    return d0, d1, forward


def _point_diagrams(text):
    d0, d1, forward = _point_terms()
    names = ('homology_family_global_boundary_point_map',
             'homology_family_global_boundary_point_equiv')
    edits = []
    for name in names:
        match = re.search(r'(?m)^symbol ' + name + r'\b.*?;', text, re.S)
        assert match
        params = match.group().split('\n : τ', 1)[0]
        assert params.endswith('(x : τ (Obj K))')
        params = re.sub(r'Functor_cat(?=\s+WalkingArrow_cat\s+C\b)', 'Functor_oplax_cat', params)
        intro = f'''≔ let d0 : τ (Functor WalkingArrow_cat C) ≔ {d0} in
  let d1 : τ (Functor WalkingArrow_cat C) ≔ {d1} in
  '''
        if name == names[0]:
            typ = f' : τ (@Transf WalkingArrow_cat C {d0} {d1})\n'
            body = '''@one_cat_original_diagram_map C C1 d0 d1
    (@id C (@fapp0 WalkingArrow_cat C d0 walking_arrow_src))
    (@id C (@fapp0 WalkingArrow_cat C d0 walking_arrow_tgt))
    (@path_to_hom
      (Hom_cat C (@fapp0 WalkingArrow_cat C d0 walking_arrow_src)
        (@fapp0 WalkingArrow_cat C d0 walking_arrow_tgt))
      (@fapp1_fapp0 WalkingArrow_cat C d0 walking_arrow_src walking_arrow_tgt walking_arrow_generator)
      (@fapp1_fapp0 WalkingArrow_cat C d1 walking_arrow_src walking_arrow_tgt walking_arrow_generator)
      (@eq_refl (Hom C (@fapp0 WalkingArrow_cat C d0 walking_arrow_src)
          (@fapp0 WalkingArrow_cat C d0 walking_arrow_tgt))
        (@fapp1_fapp0 WalkingArrow_cat C d0 walking_arrow_src walking_arrow_tgt walking_arrow_generator)));'''
        else:
            typ = f' : τ (@OmegaEquivAlong (Functor_cat WalkingArrow_cat C) {d0} {d1} {forward})\n'
            body = f'''@one_cat_diagram_map_equiv C C1 d0 d1 {forward}
    (@omega_equiv_along_refl C (@fapp0 WalkingArrow_cat C d0 walking_arrow_src))
    (@omega_equiv_along_refl C (@fapp0 WalkingArrow_cat C d0 walking_arrow_tgt));'''
        edits.append((match.start(), match.end(), params + '\n' + typ + intro + body))
    for start, end, replacement in reversed(edits):
        text = text[:start] + replacement + text[end:]
    return text.replace('/* Categorical comparison of the same original H-boundary diagrams. */',
        '/* Categorical comparison of the same original H-boundary diagrams.\n'
        '   Their oplax-profile objects are read as ordinary strict functors through\n'
        '   the existing involutive OddDual_func decoder. No category equality or\n'
        '   new inverse data are supplied by this point observation. */')


def _point_reviewer(text):
    d0, d1, forward = _point_terms()
    matches = list(re.finditer(r'(?m)^assert\b.*?;', text, re.S))
    assert len(matches) == 2
    edits = []
    for match, point in zip(matches, ('walking_arrow_src', 'walking_arrow_tgt')):
        context = match.group().split('\n ⊢', 1)[0]
        assert context.endswith('(x : τ (Obj K))')
        context = re.sub(r'Functor_cat(?=\s+WalkingArrow_cat\s+C\b)', 'Functor_oplax_cat', context)
        replacement = f'''{context}
 ⊢ (@tapp0_fapp0 WalkingArrow_cat C {d0} {d1}
      {point} {forward})
   ≡ (@id C (@fapp0 WalkingArrow_cat C {d0} {point}));'''
        edits.append((match.start(), match.end(), replacement))
    for start, end, replacement in reversed(edits):
        text = text[:start] + replacement + text[end:]
    return text


def migrate_diagram_observation(path, text):
    if path == 'emdash3_2_zero_arrow_cone_adjunction_homology.lp':
        assert text.count('(Op_cat C)') == 1
        return text.replace('(Op_cat C)', '(TotalOp_cat C)')
    if path == 'emdash3_2_zero_arrow_diagram_observations.lp':
        return _zero_observations(text)
    if path == 'emdash3_2_kernel_cokernel_adjunction_observations.lp':
        return _point_readings(_profile(text, (32, 6, 2, 3)), (16, 2))
    if path == 'emdash3_2_homology_adjunction_input_data.lp':
        return _point_readings(_profile(text, (29, 2, 2, 0)), (9, 0))
    if path == 'emdash3_2_homology_family_point_diagrams.lp':
        return _point_diagrams(text)
    if path == 'examples/homology_family_point_diagrams.lp':
        return _point_reviewer(text)
    return None
