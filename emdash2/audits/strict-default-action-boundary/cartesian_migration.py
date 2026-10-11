#!/usr/bin/env python3
"""Emit the unfinished full-file Cartesian coefficient migration candidate.

NON-LIBRARY: the upstream evaluation/curry prefix is checked; the full-file
family migration remains incomplete. No rule is promoted by this authoring
helper. The historical source pin is deliberate.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess

root = Path(__file__).resolve().parents[2]
audit = Path(__file__).resolve().parent
out = root / 'tmp/probes/strict_default_profiles'
out.mkdir(parents=True, exist_ok=True)
base = 'f8af1fca472657ff1598c639eb29c0566e7b2ec0'
def historical(name, expected):
    data = subprocess.check_output(['git', 'show', base + ':emdash2/' + name], cwd=root)
    assert hashlib.sha256(data).hexdigest() == expected, name
    return data.decode()
s = historical('emdash3_2.lp', '6a980df34be718a23a6be121d170153650830a49f54b7e0eca415705ffb2068a')
p = historical('emdash3_2_gray_profiles.lp', 'f670814a83a508bd8a77a4000c7ab04690bbfc25978d106bb1d761ce6723a69c')
for marker, parts in (
    ('/*\n  The former capped composition cut and detached all-components law are\n', ['composition_rule']),
    ('/*\n  The former whole post/left and pre/right strict-functoriality accumulation\n', ['whole_rules', 'projected_rules']),
    ('// The public whole laxity candidate is now an object projection, not an\n', ['intrinsic_rule']),
    ('// Ordinary category identity cuts: g ∘ id ↪ g and id ∘ f ↪ f.', ['evaluation_rules']),
):
    assert s.count(marker) == 1, marker
    insertion = '\n'.join((audit / (part + '.lpfragment')).read_text() for part in parts)
    s = s.replace(marker, insertion + '\n' + marker)

def take_symbol(src, name):
    m = re.search(r'(?m)^(?:injective )?symbol ' + re.escape(name) + r'\b[\s\S]*?;\n', src)
    assert m, name
    return m[0], src[:m.start()] + src[m.end():]

def replace(old, new):
    global s
    assert s.count(old) == 1, (old, s.count(old))
    s = s.replace(old, new)

transf_cat, s = take_symbol(s, 'Transf_cat')
transf, s = take_symbol(s, 'Transf')
strict, p = take_symbol(p, 'StrictTransfor')
view, p = take_symbol(p, 'strict_transfor')
hom_rule = 'rule Hom_cat (Functor_cat _ _) $F $G ↪ Transf_cat $F $G;'
replace(hom_rule, '// Hom projection is at the early classifier owner.')
anchor = '// Full hom-category action `F_1[X,Y]` before capping at one arrow.'
intro = '''// Cartesian and lax mapping categories share strict functor objects.
injective symbol Functor_cart_cat (A B : Cat) : Cat;
rule Obj (Functor_cart_cat $A $B) ↪ Functor $A $B;

''' + transf_cat + transf + hom_rule + '\n' + strict + view + '''
rule Obj (Hom_cat (Functor_cart_cat $A $B) $F $G)
  ↪ @StrictTransfor $A $B $F $G;
injective symbol cart_functor_include (A B : Cat)
  : τ (Functor (Functor_cart_cat A B) (Functor_cat A B));
rule @fapp0 _ _ (cart_functor_include _ _) $F ↪ $F;

'''
replace(anchor, intro + anchor)
anchor = '// Projection beta: applying the full hom action yields capped arrow action.'
replace(anchor, '''rule @fapp1_fapp0 _ _ (cart_functor_include $A $B) $F $G $epsilon
  ↪ @strict_transfor $A $B $F $G $epsilon;
rule @strict_transfor $A $B $F $F (@id (Functor_cart_cat $A $B) $F)
  ↪ @id (Functor_cat $A $B) $F;
rule @strict_transfor $A $B $F $H
      (@comp_fapp0 (Functor_cart_cat $A $B) $F $G $H $eta $epsilon)
  ↪ @comp_fapp0 (Functor_cat $A $B) $F $G $H
      (@strict_transfor $A $B $G $H $eta)
      (@strict_transfor $A $B $F $G $epsilon);

''' + anchor)
replace('rule Hom_cat Cat_cat $X $Y ↪ Functor_cat $X $Y;',
        'rule Hom_cat Cat_cat $X $Y ↪ Functor_cart_cat $X $Y;')

for old in ('hom_postcomp_tele_func', 'hom_precomp_along_tele_func', 'hom_con_precomp_tele_func'):
    new = old.removesuffix('_func') + '_cart_func'
    m = re.search(r'(?m)^symbol ' + old + r'\b[\s\S]*?;\n', s)
    assert m, old
    decl = m[0].replace('symbol ' + old, 'injective symbol ' + new).replace('(Functor_cat', '(Functor_cart_cat')
    s = s[:m.start()] + decl + '\n' + s[m.start():]

replace('↪ @hom_postcomp_tele_func $A $B $F $W $X $Y;',
        '↪ @hom_postcomp_tele_cart_func $A $B $F $W $X $Y;')
replace('↪ @hom_con_precomp_tele_func $A $B $F $W $X $Y;',
        '↪ @hom_con_precomp_tele_cart_func $A $B $F $W $X $Y;')

for anchor, new, old, args, point, point_args in (
    ('// Direct capped arrow action of hom_(F,W) joins the telescope projection.',
     'hom_postcomp_tele_cart_func', 'hom_postcomp_tele_func', '$A $B $F $W $X $Y',
     'hom_postcomp_func', '$A $B $F $W $X $Y'),
    ('// Direct contravariant capped action joins the telescope projection.',
     'hom_con_precomp_tele_cart_func', 'hom_con_precomp_tele_func', '$A $B $F $W $X $Y',
     'hom_precomp_along_func', '$B $A $F $W $Y $X'),
    ('// Applying the telescope to h yields the capped precomposition functor.',
     'hom_precomp_along_tele_cart_func', 'hom_precomp_along_tele_func', '$A $B $F $Z $W $X',
     'hom_precomp_along_func', '$A $B $F $Z $W $X'),
):
    code = f'''rule fapp0 (@{new} {args}) $p
  ↪ @{point} {point_args} $p;
rule @comp_fapp0 Cat_cat _ _ _
      (cart_functor_include _ _) (@{new} {args})
  ↪ @{old} {args};

'''
    replace(anchor, code + anchor)

# Cat's joint composition has Cartesian transformation inputs.
m = re.search(r'(?m)^symbol Functor_comp_pair_func\b[\s\S]*?;\n', s)
assert m
s = s[:m.start()] + m[0].replace('Functor_cat', 'Functor_cart_cat') + s[m.end():]

# The path-universe's second action is Cartesian; expose its existing lax view.
m = re.search(r'(?m)^symbol path_map_transf\b[\s\S]*?;\n', s)
assert m
decl, body = m[0].split('≔', 1)
body = body.rstrip().removesuffix(';').replace('(Functor_cat', '(Functor_cart_cat')
s = s[:m.start()] + decl + '≔ strict_transfor (\n' + body.strip() + ');\n' + s[m.end():]

# Whole Cartesian view of two-endpoint Hom; retain the public lax observation.
m = re.search(r'(?m)^symbol Hom_tele_func\b[\s\S]*?;\n', s)
assert m
cart = m[0].replace('symbol Hom_tele_func', 'injective symbol Hom_cart_tele_func').replace('(Functor_cat', '(Functor_cart_cat')
s = s[:m.start()] + cart + '\n' + s[m.start():]
anchor = '// Applying the two-endpoint telescope to `(g,f)` yields `Hom_func(g,f)`.'
replace(anchor, '''rule fapp0 (@Hom_cart_tele_func $A $x $x' $y $y') (Struct_sigma $g $f)
  ↪ @Hom_func $A $x $x' $y $y' $g $f;
rule @comp_fapp0 Cat_cat _ _ _
      (cart_functor_include _ _) (@Hom_cart_tele_func $A $x $x' $y $y')
  ↪ @Hom_tele_func $A $x $x' $y $y';

''' + anchor)
for m in reversed(list(re.finditer(r'(?m)^rule @tapp1_func\b[\s\S]*?;\n', s))):
    if 'hom_int_precomp_func' in m[0] or 'hom_con_int_postcomp_func' in m[0]:
        changed = m[0].replace('@Hom_tele_func', '@Hom_cart_tele_func').replace('(Functor_cat', '(Functor_cart_cat')
        s = s[:m.start()] + changed + s[m.end():]

# Horizontal action in Cat has strict-transfor input and output carriers.
left = s.index('// Cat instance of product-composition arrow action.')
right = s.index('// 6c. Constant/opposite transfors', left)
block = s[left:right]
needle = "(@comp_prod_fapp1_fapp0 Cat_cat $X $Y $Z $FG $FG' $theta)"
assert block.count(needle) == 3
block = block.replace(needle, '(@strict_transfor $X $Z _ _ ' + needle + ')')
block = block.replace('(sigma_Snd $theta)', "(@strict_transfor $Y $Z (sigma_Snd $FG) (sigma_Snd $FG') (sigma_Snd $theta))")
block = block.replace('(sigma_Fst $theta)', "(@strict_transfor $X $Y (sigma_Fst $FG) (sigma_Fst $FG') (sigma_Fst $theta))")
block = block.replace('(Functor_cat $X $Y)', '(Functor_cart_cat $X $Y)').replace('(Functor_cat $Y $Z)', '(Functor_cart_cat $Y $Z)').replace('(Functor_cat $X $Z)', '(Functor_cart_cat $X $Z)')
s = s[:left] + block + s[right:]

# Fixed postcomposition belongs to the action of the lax mapping constructor,
# not to Hom(Cat), whose transformation profile is now Cartesian.
m = re.search(r'(?m)^symbol comp_cat_cov_func\b[\s\S]*?;\n', s)
assert m
decl = m[0].split('≔', 1)[0]
body = '''≔ @fapp1_fapp0 Cat_cat Cat_cat
    (Functor_cat_fapp0_func X) Y Z G;

// Object action of the mapping-category constructor's fixed postcomposition.
rule @fapp0 _ _
      (@fapp1_fapp0 Cat_cat Cat_cat (Functor_cat_fapp0_func $X) $Y $Z $G) $F
  ↪ @comp_cat_fapp0 $X $Y $Z $G $F;
'''
s = s[:m.start()] + decl + body + s[m.end():]

# Path's whole action now lands in the Cartesian mapping category. Its
# existing public lift remains the lax observation through the inclusion.
replace('''    (@fapp1_func
      Grpd_cat Cat_cat Path_cat_func
      A (Obj C));''', '''    (@comp_cat_fapp0
      (Path_cat (@Function_grpd A (Obj C)))
      (Functor_cart_cat (Path_cat A) (Core_cat C))
      (Functor_cat (Path_cat A) (Core_cat C))
      (cart_functor_include (Path_cat A) (Core_cat C))
      (@fapp1_func
        Grpd_cat Cat_cat Path_cat_func
        A (Obj C)));''')

# Preserve the old derived Cat-composition helpers with their actual
# Cartesian Hom inputs. Fixed whiskering on ambient transfors is a separate
# view of the existing internal mapping-category constructor, above/below.
for name in ('comp_cat_cov_func_func', 'comp_cat_con_func_func'):
    m = re.search(r'(?m)^symbol ' + name + r'\b[\s\S]*?;\n', s)
    assert m, name
    decl, body = m[0].split('≔', 1)
    # The target is the ambient functor category of the two Cartesian Homs;
    # the existing generic telescope already has precisely this type.
    outer = '(Functor_cat (Functor_cat '
    assert outer in decl
    decl = decl.replace('Functor_cat', 'Functor_cart_cat')
    decl = decl.replace('(Functor_cart_cat (Functor_cart_cat ',
                        '(Functor_cat (Functor_cart_cat ', 1)
    s = s[:m.start()] + decl + '≔' + body + s[m.end():]

# The fixed Cartesian companions retain the original semantic derivations;
# they are transparent aliases, not a duplicated composition calculus.
for variance, generic, args in (
    ('cov', 'hom_postcomp_func', 'X Y Z G'),
    ('con', 'hom_precomp_along_func', 'Z X Y F'),
):
    parameter = 'G' if variance == 'cov' else 'F'
    pdom, pcod = ('Y', 'Z') if variance == 'cov' else ('X', 'Y')
    dom = '(Functor_cart_cat X Y)' if variance == 'cov' else '(Functor_cart_cat Y Z)'
    marker = 'symbol comp_cat_' + variance + '_func_func [X Y Z : Cat]'
    code = f'''// Cartesian fixed-whiskering view of the existing Cat Hom action.
symbol comp_cat_{variance}_cart_func [X Y Z : Cat]
  ({parameter} : τ (Functor {pdom} {pcod}))
  : τ (Functor {dom} (Functor_cart_cat X Z))
≔ @{generic} Cat_cat Cat_cat (@id Cat_cat Cat_cat) {args};

'''
    replace(marker, code + marker)

# Fixed precomposition on the ambient mapping category is the object
# component of the existing binary mapping constructor's source action.
m = re.search(r'(?m)^symbol comp_cat_con_func\b[\s\S]*?;\n', s)
assert m
decl = m[0].split('≔', 1)[0]
body = '''≔ @tapp0_fapp0 Cat_cat Cat_cat
    (Functor_cat_fapp0_func Y) (Functor_cat_fapp0_func X) Z
    (@fapp1_fapp0 (Op_cat Cat_cat) (Functor_cat Cat_cat Cat_cat)
      Functor_cat_func Y X F);

// Applying the source action of the internal mapping constructor precomposes.
rule @fapp0 _ _
      (@tapp0_fapp0 _ _ _ _ $Z
        (@fapp1_fapp0 _ _ Functor_cat_func $Y $X $F)) $G
  ↪ @comp_cat_fapp0 $X $Y $Z $G $F;
'''
s = s[:m.start()] + decl + body + s[m.end():]

# Full action of fixed whiskering continues to accept ambient transfors.
for variance, args, endpoints in (('cov', 'G', 'F H'), ('con', 'F', 'G H')):
    name = 'comp_cat_' + variance + '_fapp1_func'
    m = re.search(r'(?m)^symbol ' + name + r'\b[\s\S]*?;\n', s)
    assert m, name
    decl = m[0].split('≔', 1)[0]
    body = f'''≔ @fapp1_func _ _
    (@comp_cat_{variance}_func X Y Z {args}) {endpoints};
'''
    s = s[:m.start()] + decl + body + s[m.end():]

# Pointwise opposite on an ambient family belongs to ambient post-whiskering,
# not to the Cartesian Hom(Cat) specialization. Whole duality retyping is a
# subsequent coupled edit; this step only keeps the existing owner/profile.
replace('''rule @hom_postcomp_func Cat_cat Cat_cat (@id Cat_cat Cat_cat) $Z Cat_cat Cat_cat op
  ↪ @Op_catd_func $Z;''', '''rule @fapp1_fapp0 Cat_cat Cat_cat
      (Functor_cat_fapp0_func $Z) Cat_cat Cat_cat op
  ↪ @Op_catd_func $Z;''')

# Hom(Cat)-specialized projection rules consume Cartesian transfors.
left = s.index('// Cat-valued capped postcomposition exposes ordinary transfor projections.')
right = s.index('// The old `comp_cat_cov_transf` compatibility name', left)
s = s[:left] + s[left:right].replace('Functor_cat', 'Functor_cart_cat') + s[right:]

m = re.search(r'(?m)^rule @hom_precomp_along_fapp1_fapp0\n      \$K\n      Cat_cat[\s\S]*?;\n', s)
assert m
s = s[:m.start()] + m[0].replace('Functor_cat', 'Functor_cart_cat') + s[m.end():]

# The parameterized helpers remain derived from generic Cat Hom telescopes.
# Their parameter arrows belong to Cartesian Homs. Their output remains the
# existing ambient transformation view; no generic naturality is restored.
for variance, first, last, pdom, pcod in (
    ('cov', 'G', 'H', 'Y', 'Z'), ('con', 'F', 'K', 'X', 'Y')):
    for suffix in ('_fapp1_func', '_transf'):
        name = 'comp_cat_' + variance + '_func_func' + suffix
        m = re.search(r'(?m)^symbol ' + name + r'\b[\s\S]*?;\n', s)
        assert m, name
        decl, body = m[0].split('≔', 1)
        if suffix == '_fapp1_func':
            decl = decl.replace(f'(@Transf_cat {pdom} {pcod} {first} {last})',
                                f'(Hom_cat (Functor_cart_cat {pdom} {pcod}) {first} {last})')
        else:
            decl = decl.replace(f'(Transf {first} {last})',
                                f'(Hom (Functor_cart_cat {pdom} {pcod}) {first} {last})')
        decl = decl.replace('(Functor_cat', '(Functor_cart_cat')
        decl = decl.replace('(@comp_cat_' + variance + '_func',
                            '(@comp_cat_' + variance + '_cart_func')
        s = s[:m.start()] + decl + '≔' + body + s[m.end():]

control_owner = '// 7a. Internalized product formation and product maps'
replace(control_owner, (audit / 'cartesian_whiskering_controls.lpfragment').read_text()
        + '\n' + control_owner)

# Product formation is still the same Cat-valued constructor. Its Hom(Cat)
# parameter actions now expose Cartesian mapping categories in their types.
for name in ('Product_cat_fapp1_func', 'Product_mapL_func_func'):
    m = re.search(r'(?m)^symbol ' + name + r'\b[\s\S]*?;\n', s)
    assert m, name
    s = s[:m.start()] + m[0].replace('Functor_cat', 'Functor_cart_cat') + s[m.end():]

# Cartesian currying uses the Cartesian whole composition telescopes. The
# existing raw transformation helper names remain their explicit lax views.
for variance, old, new in (
    ('cov', 'hom_postcomp_tele_func', 'hom_postcomp_tele_cart_func'),
    ('con', 'hom_precomp_along_tele_func', 'hom_precomp_along_tele_cart_func')):
    name = 'comp_cat_' + variance + '_func_func'
    m = re.search(r'(?m)^symbol ' + name + r'\b[\s\S]*?;\n', s)
    assert m, name
    s = s[:m.start()] + m[0].replace('Functor_cat', 'Functor_cart_cat').replace(old, new) + s[m.end():]

# The canonical pair telescope is strictly natural in the retained variable.
m = re.search(r'(?m)^symbol Product_pair_tele_func\b[\s\S]*?;\n', s)
assert m
s = s[:m.start()] + m[0].replace('Functor_cat', 'Functor_cart_cat') + s[m.end():]

# Evaluation keeps its existing ladder, now over the Cartesian mapping Hom.
left = s.index('// 7b. Evaluation and fixed-object evaluation')
right = s.index('// 7c. Ordinary curry and uncurry', left)
block = s[left:right].replace('Functor_cat', 'Functor_cart_cat')
block = block.replace('(Transf_cat F G)', '(Hom_cat (Functor_cart_cat A B) F G)')
block = block.replace('(@Transf_cat $A $B $F $G)',
                      '(Hom_cat (Functor_cart_cat $A $B) $F $G)')
assert block.count('↪ tapp1_fapp0 $eta $p;') == 2
block = block.replace('↪ tapp1_fapp0 $eta $p;',
                      '↪ tapp1_fapp0 (@strict_transfor $A $B $F $G $eta) $p;')
assert block.count('↪ fapp0_func $x;') == 1
block = block.replace('↪ fapp0_func $x;', '''↪ @comp_cat_fapp0
      (Functor_cart_cat $A $B) (Functor_cat $A $B) $B
      (@fapp0_func $A $B $x) (cart_functor_include $A $B);''')
s = s[:left] + block + s[right:]

# Preserve the actual Cartesian curry/uncurry composition bodies. Their
# source/target Homs and the inner functor classifier now have that profile.
for name in ('curry_func_func', 'curry_func', 'uncurry_func_func', 'uncurry_func'):
    m = re.search(r'(?m)^symbol ' + name + r'\b[\s\S]*?;\n', s)
    assert m, name
    body = m[0].replace('Functor_cat', 'Functor_cart_cat')
    body = body.replace('(@comp_cat_con_func\n', '(@comp_cat_con_cart_func\n')
    body = body.replace('(@comp_cat_cov_func\n', '(@comp_cat_cov_cart_func\n')
    s = s[:m.start()] + body + s[m.end():]

# Cartesian mapping into a product retains the existing paired-functor form.
anchor = '// Product homs compute componentwise.'
replace(anchor, '''// Cartesian internal Hom preserves products in its target.
rule Functor_cart_cat $X (Product_cat $A $B)
  ↪ Product_cat (Functor_cart_cat $X $A) (Functor_cart_cat $X $B);

''' + anchor)

# Product formation has canonical strict parameter naturality. Its Cartesian
# view shares the existing partial constructor and one whole inclusion fold.
anchor = '// Object projection ladder for the internalized product constructor.'
replace(anchor, '''// Cartesian parameter view of the same product constructor.
injective symbol Product_cat_cart_func
  : τ (Functor Cat_cat (Functor_cart_cat Cat_cat Cat_cat));
rule fapp0 Product_cat_cart_func $A ↪ Product_cat_fapp0_func $A;
rule @comp_fapp0 Cat_cat _ _ _
      (cart_functor_include Cat_cat Cat_cat) Product_cat_cart_func
  ↪ Product_cat_func;

''' + anchor)
needle = '@uncurry_func Cat_cat Cat_cat Cat_cat Product_cat_func'
assert s.count(needle) > 0
s = s.replace(needle, '@uncurry_func Cat_cat Cat_cat Cat_cat Product_cat_cart_func')

evaluation_end = '// 7d. Adjunctions and opposite adjunctions'
replace(evaluation_end, (audit / 'cartesian_evaluation_controls.lpfragment').read_text()
        + '\n' + evaluation_end)

# Constant-family transport is the identity in the corrected coefficient Hom.
replace('''rule @fapp1_func $K Cat_cat (@Const_catd $K $A) $x $y
  ↪ @Const_func
      (Hom_cat $K $x $y)
      (Functor_cat $A $A)
      (@id_func $A);''', '''rule @fapp1_func $K Cat_cat (@Const_catd $K $A) $x $y
  ↪ @Const_func
      (Hom_cat $K $x $y)
      (Functor_cart_cat $A $A)
      (@id_func $A);''')

(out / 'emdash3_2.lp').write_text(s)
(out / 'owner_prefix.lp').write_text(s[:s.index(evaluation_end)])
(out / 'emdash3_2_gray_profiles.lp').write_text(p)
(out / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
parts = ('composition_rule', 'whole_rules', 'projected_rules', 'intrinsic_rule',
         'evaluation_rules', 'cartesian_whiskering_controls', 'cartesian_evaluation_controls')
authoring = [Path(__file__)] + [audit / (part + '.lpfragment') for part in parts]
controls = '\n'.join((audit / (part + '.lpfragment')).read_text() for part in parts[-2:])
manifest = {
    'status': 'non-library; emitted source is not a qualification claim',
    'sourcePin': base,
    'authoringInputs': {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in authoring},
    'outputs': {name: hashlib.sha256((out / name).read_bytes()).hexdigest()
                for name in ('emdash3_2.lp', 'emdash3_2_gray_profiles.lp', 'owner_prefix.lp', 'lambdapi.pkg')},
    'ownerPrefixBoundary': evaluation_end,
    'controls': {'positive': len(re.findall(r'(?m)^assert\b', controls)),
                 'negative': len(re.findall(r'(?m)^assertnot\b', controls))},
}
(out / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print('Built full-file Cartesian-universe candidate with early carriers.')
