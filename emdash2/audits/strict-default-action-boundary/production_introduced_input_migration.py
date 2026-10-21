"""Scoped migration of the original introduced-terminal-input comparison.

The emitted Lambdapi retains the original maps, inverses and OneCat inputs.
Its whole reflection uses existing comparison owners; no rule is added here.
"""
from pathlib import Path
import re
from production_diagram_observation_migration import B, _atom, _body, _point_readings

M = '(Functor_cat WalkingArrow_cat C)'
x = '(@fapp0 K C F x)'
y = '(@fapp0 K C G x)'
u = '(@tapp0_fapp0 K C F G x u)'
d0 = f'(@fapp0 K {B} (@transf_arrow_diagram_func K C F G u) x)'
dec = f'(@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) {d0})'
raw = f'(@walking_arrow_func C {x} {y} {u})'
inc = '(@introduced_input_diagram_coefficient_func C C1)'
eps = '(@introduced_input_diagram_original_map K C C1 F G u x)'

def enc_walk(s):
    while matches := list(re.finditer(r'\(@walking_arrow_func C\b',s)):
        m = matches[-1]
        cursor = m.end()
        for _ in range(3):
            _, cursor = _atom(s, cursor)
        assert s[cursor] == ')'
        term = s[m.start():cursor+1].replace('@walking_arrow_func C','@WALKING C',1)
        s = s[:m.start()]+f'(@OddDual_func WalkingArrow_cat C {term})'+s[cursor+1:]
    return s.replace('@WALKING C','@walking_arrow_func C')
def profile(s, expected):
    patterns = [r'Functor_cat(?=\s+WalkingArrow_cat\s+C\b)',r'@Transf\s+WalkingArrow_cat\s+C\b',r'\(@walking_arrow_func C\b',r'@fapp0\s+WalkingArrow_cat\s+C\b',r'@tapp0_fapp0\s+WalkingArrow_cat\s+C\b']
    actual = tuple(len(re.findall(p,s)) for p in patterns)
    assert actual == expected, (actual, expected)
    s = re.sub(r'Functor_cat(?=\s+WalkingArrow_cat\s+C\b)','Functor_oplax_cat',s)
    s = re.sub(r'@Transf\s+WalkingArrow_cat\s+C\b',f'@Hom {B}',s)
    s = enc_walk(s)
    counts = tuple(len(re.findall(r'@'+h+r'\s+WalkingArrow_cat\s+C\b',s)) for h in ('fapp0','tapp0_fapp0'))
    return _point_readings(s,counts)


def _consumer(s):
    s = _body(s,'introduced_input_diagram_map','MAP_BODY')
    s = _body(s,'introduced_input_diagram_equiv','EQUIV_BODY')
    s = profile(s, (40, 7, 13, 0, 2))
    s = s.replace('@one_cat_diagram_map_path C C1','@introduced_input_oplax_map_path C C1')
    s = s.replace('MAP_BODY',f'@fapp1_fapp0 {M} {B} {inc} {dec} {raw} {eps}')
    s = s.replace('EQUIV_BODY',f'''@one_cat_omega_equiv_fmap {M} {B}
                    (@one_cat_oplax_functor_category WalkingArrow_cat C C1) {inc}
                    {dec} {raw} {eps}
                    (@one_cat_diagram_map_equiv C C1 {dec} {raw} {eps}
                            (@omega_equiv_along_refl C {x}) (@omega_equiv_along_refl C {y}))''')
    helper = f'''require open emdash.emdash3_2_one_cat_diagram_family_reflection;
{"    "}
    // Retain the original ordinary shape map before its actual coefficient image.
    protected symbol introduced_input_diagram_original_map [K C : Cat]
            (C1 : τ (IsNCat (cat_succ cat_zero) C))
            [F G : τ (Functor K C)] (u : τ (@Transf K C F G)) (x : τ (Obj K))
            : τ (@Transf WalkingArrow_cat C {dec} {raw})
    ≔ @one_cat_original_diagram_map C C1 {dec} {raw}
                    (@id C {x}) (@id C {y})
                    (@path_to_hom (Hom_cat C {x} {y})
                            (@fapp1_fapp0 WalkingArrow_cat C {dec}
                                    walking_arrow_src walking_arrow_tgt walking_arrow_generator)
                            {u} (@eq_refl (Hom C {x} {y}) {u}));
{"    "}
    // Whole inclusion through the existing OneCat mapping comparison.
    protected symbol introduced_input_diagram_coefficient_func [C : Cat]
            (C1 : τ (IsNCat (cat_succ cat_zero) C))
            : τ (Functor {M} {B})
    ≔ @comp_cat_fapp0 {M} (Functor_cart_cat WalkingArrow_cat C) {B}
                    (Functor_cart_oplax_include WalkingArrow_cat C)
                    (@one_cat_mapping_to_cart_func WalkingArrow_cat C C1);
{"    "}
    '''
    anchor = '// Reconstruct the evaluated diagram as its introduced generator, retaining actual endpoints.'
    assert s.count(anchor) == 1
    reflection = Path(__file__).with_name('production_introduced_input_reflection.lpfragment').read_text()
    s = s.replace(anchor,helper+reflection+'\n'+anchor)
    return s

def migrate_introduced_input(path, text):
    if path == 'emdash3_2_one_cat_introduced_terminal_input_comparisons.lp':
        return _consumer(text)
    if path == 'examples/introduced_terminal_input_comparisons.lp':
        return profile(text, (59, 10, 4, 0, 2))
    return None
