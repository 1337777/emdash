#!/usr/bin/env python3
"""Stage required upstream owners in a full copy of the pre-goal kernel.

This is an in-progress production migration, not another foundation model.
No original downstream section is truncated. Legacy family/Op consumers
are intentionally retained for their subsequent coupled adaptation.

Check imports with scripts/run_lambdapi.py --package-root pointing to the
emitted package. The outer probe wrapper checks the source but inventories
imports relative to the outer package, which is not this staged dependency
snapshot.
"""
import hashlib
import json
import difflib
from pathlib import Path
import re
import subprocess


PIN = 'f8af1fca472657ff1598c639eb29c0566e7b2ec0'
CORE_SHA = '6a980df34be718a23a6be121d170153650830a49f54b7e0eca415705ffb2068a'


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    original = subprocess.check_output(
        ['git', 'show', PIN + ':emdash2/emdash3_2.lp'], cwd=root, text=True)
    profiles = subprocess.check_output(
        ['git', 'show', PIN + ':emdash2/emdash3_2_gray_profiles.lp'], cwd=root, text=True)
    original_profiles = profiles
    assert sha(original) == CORE_SHA
    body = original
    inputs = {}
    changes = []

    def fragment(name):
        path = audit / name
        text = path.read_text()
        inputs[str(path.relative_to(root))] = sha(text)
        return text

    def insert(marker, text, reason):
        nonlocal body
        assert body.count(marker) == 1, marker
        body = body.replace(marker, text + '\n' + marker, 1)
        changes.append({'anchor': marker, 'reason': reason,
                        'insertedSha256': sha(text)})

    def replace_once(old, new, owner, reason):
        nonlocal body
        assert body.count(old) == 1, owner
        body = body.replace(old, new, 1)
        changes.append({'owner': owner, 'reason': reason,
                        'oldSha256': sha(old), 'newSha256': sha(new)})

    insert('/*\n  The former capped composition cut and detached all-components law are\n',
           fragment('composition_rule.lpfragment'), 'Strict default: existing capped functor action owner')
    insert('/*\n  The former whole post/left and pre/right strict-functoriality accumulation\n',
           fragment('whole_rules.lpfragment') + '\n' + fragment('projected_rules.lpfragment')
           + '\n' + fragment('conventional_lax_projection_readings.lpfragment')
           + '\n' + fragment('production_conventional_pre_reading.lpfragment')
           + '\n' + fragment('conventional_lax_rules.lpfragment'),
           'Strict functor action and conventional-lax pre/right action at the existing whole/projection owners')
    insert('// The public whole laxity candidate is now an object projection, not an\n',
           fragment('intrinsic_rule.lpfragment'),
           'Strict default: normalize the existing extracted functor compositor, without a new witness')
    insert('// Whole post/left ordinary laxity.',
           fragment('conventional_lax_intrinsic.lpfragment'),
           'Conventional lax default: the existing extracted pre/right cell is identity, without a wrapper or supplied comparison')

    insert('// Path categories internalize HoTT equality as a groupoidal category.',
           fragment('co_above2_category.lpfragment') + '\n' + fragment('co_at2_category.lpfragment'),
           'Corrected duality: required category-level R, O and dimension-two action')
    above = fragment('co_above2_functor.lpfragment')
    cart_dualities = above[above.index('// Whole action on Cartesian mapping categories.'):]
    cart_dualities = (cart_dualities.replace('TotalOp_func_func', 'TotalOp_cart_func_func')
                     .replace('total_op', 'total_op_cart').replace('Cat_cat', 'Cat_cart'))
    above = above[:above.index('// Whole action on Cartesian mapping categories.')]
    at = fragment('co_at2_functor.lpfragment')
    public_total = fragment('conventional_total_op_mapping.lpfragment')
    public_total = public_total[:public_total.index('// Whole formation for any strict family')]
    insert('// Terminal category and points-as-functors are needed to derive unary homs from',
           above + '\n' + at + '\n' + cart_dualities + '\n' + public_total,
           'Corrected whole dualities: Cartesian transpose and total reversal, plus the distinct public conventional-lax total reversal')

    profile = fragment('cartesian_profile.lpfragment')
    early = profile[profile.index('injective symbol sf_cart_functor_cat'):profile.index('// Only the object classifier')]
    start = profile.index('constant symbol sf_cart_cat')
    early += profile[start:profile.index('// One whole inclusion', start)]
    early += '''
// Whole inclusion of the selected coefficient; category/functor objects agree.
injective symbol Cat_cart_include : τ (Functor Cat_cart Cat_cat);
rule fapp0 Cat_cart_include $A ↪ $A;
rule @fapp1_fapp0 _ _ Cat_cart_include _ _ $F ↪ $F;
rule @id Cat_cart $A ↪ @id Cat_cat $A;
// lhs-audit: keep 1 -- only composition inside the Cartesian coefficient.
rule @comp_fapp0 Cat_cart $A $B $C $G $F
  ↪ @comp_fapp0 Cat_cat $A $B $C $G $F;
'''
    names = {'sf_cart_functor_cat': 'Functor_cart_cat', 'sf_cart_cat': 'Cat_cart',
             'sf_cart_functor_include': 'Functor_cart_include'}

    def public(text):
        for old, new in names.items():
            text = text.replace(old, new)
        return text

    insert('/*\n  Internal path-category action.',
           '// Cartesian coefficient required by the selected Homd family type.\n' + public(early),
           'Homd coefficient: share strict functor objects while retaining public lax Hom(Cat)')

    carriers = ''
    relocated = []
    for marker in ('injective symbol StrictTransfor\n', 'injective symbol strict_transfor\n'):
        assert profiles.count(marker) == 1
        a = profiles.index(marker)
        b = profiles.index(';', a) + 1
        declaration = profiles[a:b]
        carriers += declaration + '\n\n'
        relocated.append({'symbol': marker.strip(), 'declarationSha256': sha(declaration)})
        profiles = profiles[:a] + '// Carrier/view relocated to the core owner.\n' + profiles[b:]
    post_start = '// Whole post/left strict naturality guarded by the evidence-bearing view.'
    post_end = '// Whole pre/right strict naturality guarded by the same full profile.'
    assert profiles.count(post_start) == profiles.count(post_end) == 1
    a, b = profiles.index(post_start), profiles.index(post_end)
    strict_post = profiles[a:b]
    profiles = profiles[:a] + '// Core-independent strict post action is owned by the nucleus.\n\n' + profiles[b:]
    insert('/*\n  The former whole post/left and pre/right strict-functoriality accumulation\n',
           strict_post + '''
// Identity specialization after the strict component has already projected.
rule @comp_fapp0 $B _ _ _
      (@fapp1_fapp0 $A $B $G $x $y $p)
      (@tapp0_fapp0 $A $B $F $G $x (@strict_transfor $A $B $F $G $U))
  ↪ @tapp1_fapp0 $A $B $F $G $x $y (@strict_transfor $A $B $F $G $U) $p;
''', 'Move existing strict-transfor post computation to the core Cartesian consumer; retain the later admission/property machinery')
    relocated.append({'owner': 'strict-transfor ordinary post action', 'bodySha256': sha(strict_post)})
    late = profile[profile.index('// Only the object classifier'):profile.index('// The corresponding strict coefficient universe')]
    start = profile.index('// One whole inclusion')
    late += profile[start:profile.index('// A Cartesian evaluator', start)]
    late += '''
// The whole first Hom of coefficient inclusion retains the strict profile.
rule @fapp1_func _ _ Cat_cart_include $A $B
  ↪ Functor_cart_include $A $B;

// Existing ordinary transfor observations of canonical Cartesian Hom action.
rule @strict_transfor _ _ _ _
      (@hom_postcomp_tele_fapp1_fapp0 $A $B $F $W $X $Y $f $g $alpha)
  ↪ @hom_postcomp_tele_transf $A $B $F $W $X $Y $f $g $alpha;
rule @strict_transfor _ _ _ _
      (@hom_precomp_along_tele_fapp1_fapp0 $A $B $F $Z $W $X $h $k $alpha)
  ↪ @hom_precomp_along_tele_transf $A $B $F $Z $W $X $h $k $alpha;

// Defined ordinary diagram views of the same canonical whole Hom packages.
// These admit general lax internal-action components without changing Hom.
symbol hom_int_view [A B : Cat] (F : τ (Functor B A))
  : τ (Functor (Op_cat A) (Catd_cat B))
≔ @comp_cat_fapp0 (Op_cat A) (Functor_cart_cat B Cat_cart)
    (Catd_cat B) (Functor_cart_include B Cat_cart) (@hom_int A B F);
symbol hom_con_int_view [A B : Cat] (F : τ (Functor B A))
  : τ (Functor A (Catd_cat (Op_cat B)))
≔ @comp_cat_fapp0 A (Functor_cart_cat (Op_cat B) Cat_cart)
    (Catd_cat (Op_cat B)) (Functor_cart_include (Op_cat B) Cat_cart)
    (@hom_con_int A B F);
'''
    insert('// Controlled Obj-inversion for transformation categories.',
           carriers, 'Relocate the existing strict-transfor carriers unchanged')
    hom_owner = 'rule Hom_cat (Functor_cat _ _) $F $G ↪ Transf_cat $F $G;'
    assert body.count(hom_owner) == 1
    body = body.replace(hom_owner, hom_owner + '\n\n' + public(late), 1)
    changes.append({'after': hom_owner,
                    'reason': 'Cartesian inclusion uses the original ordinary next-Hom projection',
                    'insertedSha256': sha(public(late))})

    replace_once('rule Obj (@Catd_cat $K)\n  ↪ Obj (Functor_cat $K Cat_cat);',
                 'rule Obj (@Catd_cat $K)\n  ↪ Obj (Functor_cat $K Cat_cart);',
                 'Catd_cat object classifier',
                 'Selected admitted families land in the Cartesian coefficient; Functord remains lax across the base')
    replace_once("unif_rule Functor_cat $K Cat_cat ≡ @Catd_cat $K'",
                 "unif_rule Functor_cat $K Cat_cart ≡ @Catd_cat $K'",
                 'Catd_cat whole classifier comparison',
                 'Match the selected coefficient at the existing displayed facade')
    replace_once('''symbol Catd_cat_func : τ (Functor (Op_cat Cat_cat) Cat_cat)
≔ @comp_cat_fapp0
     (Op_cat Cat_cat)
     (Functor_cat Cat_cat Cat_cat)
     Cat_cat
     (@fapp0_func Cat_cat Cat_cat Cat_cat)
     Functor_cat_func;''', '''symbol Catd_cat_func : τ (Functor (Op_cat Cat_cat) Cat_cat)
≔ @comp_cat_fapp0
     (Op_cat Cat_cat)
     (Functor_cat Cat_cat Cat_cat)
     Cat_cat
     (@fapp0_func Cat_cat Cat_cat Cat_cart)
     Functor_cat_func;''',
                 'Catd_cat_func',
                 'The original internal constructor now evaluates its coefficient slot at Cat_cart')
    replace_once('''symbol Catd_catd_con [L : Cat] (K : τ (Catd L)) : τ (Catd (Op_cat L))
≔ @comp_cat_fapp0
     (Op_cat L)
     (Op_cat Cat_cat)
     Cat_cat
     Catd_cat_func
     (@Op_func L Cat_cat K);''', '''symbol Catd_catd_con [L : Cat] (K : τ (Catd L))
  : τ (Functor (Op_cat L) Cat_cat)
≔ @comp_cat_fapp0
     (Op_cat L)
     (Op_cat Cat_cat)
     Cat_cat
     Catd_cat_func
     (@Op_func L Cat_cat
       (@comp_cat_fapp0 L Cat_cart Cat_cat Cat_cart_include K));''',
                 'Catd_catd_con',
                 'The existing constructor lands in the public universe; expose that raw result instead of assuming a Cartesian lift of its whole higher action')

    # Canonical Hom actions of strict categories have the Cartesian profile.
    # Keep every original covariant/contravariant owner and change its mapping
    # classifiers together, rather than introducing a parallel action API.
    section_start = '// 4. Ordinary internal hom and hom actions'
    section_end = '// 5. Ordinary binary products of categories'
    assert body.count(section_start) == body.count(section_end) == 1
    a, b = body.index(section_start), body.index(section_end)
    old_hom = body[a:b]
    new_hom = old_hom.replace('Functor_cat', 'Functor_cart_cat')
    new_hom = new_hom.replace(': τ (Functor B Cat_cat);', ': τ (Functor B Cat_cart);')
    new_hom = new_hom.replace(': τ (Functor (Op_cat B) Cat_cat);',
                              ': τ (Functor (Op_cat B) Cat_cart);')
    new_hom = re.sub(r'Cat_cat(\s+\(@hom_(?:con\b|\s))', r'Cat_cart\1', new_hom)
    for owner in ('hom_postcomp_tele', 'hom_precomp_along_tele'):
        marker = 'symbol ' + owner + '_transf '
        assert new_hom.count(marker) == 1
        start = new_hom.index(marker)
        end = new_hom.index(';', start) + 1
        ordinary_view = new_hom[start:end].replace('Functor_cart_cat', 'Functor_cat')
        new_hom = new_hom[:start] + ordinary_view + new_hom[end:]
        new_hom = new_hom.replace('↪ @' + owner + '_transf ',
                                   '↪ @' + owner + '_fapp1_fapp0 ')
    for old, new in (
            ('(Catd_cat B)', '(Functor_cart_cat B Cat_cart)'),
            ('(@Catd_cat B)', '(Functor_cart_cat B Cat_cart)'),
            ('(@Catd_cat $B)', '(Functor_cart_cat $B Cat_cart)'),
            ('(@Catd_cat (Op_cat B))', '(Functor_cart_cat (Op_cat B) Cat_cart)'),
            ('(Catd_cat (Op_cat B))', '(Functor_cart_cat (Op_cat B) Cat_cart)')):
        new_hom = new_hom.replace(old, new)
    replace_once(old_hom, new_hom, 'ordinary Hom owner block',
                 'Selected whole Cartesian Hom profile with the original public names and blended strict F argument')
    a = body.index('symbol Hom_tele_func ')
    b = body.index(';', a) + 1
    old_two_endpoint = body[a:b]
    replace_once(old_two_endpoint, old_two_endpoint.replace('Functor_cat', 'Functor_cart_cat'),
                 'Hom_tele_func',
                 'The original two-endpoint Hom action has the same Cartesian higher mapping profile as its curried observations')

    facade_start = '// Proof-time comparison only: ordinary Cat-valued transfors and displayed'
    facade_end = '// Product-valued transfors project componentwise.'
    assert body.count(facade_start) == body.count(facade_end) == 1
    a, b = body.index(facade_start), body.index(facade_end)
    old_facade = body[a:b]
    new_facade = re.sub(r'(\$K\s+)Cat_cat', r'\1Cat_cart', old_facade)
    replace_once(old_facade, new_facade, 'Functord and Transfd facade projections',
                 'Default lax transformations between the newly admitted Cartesian-coefficient families')

    observation_start = '// Component of a postcomposition-telescope action.'
    assert body.count(observation_start) == 1
    a = body.index(observation_start)
    old_observations = body[a:]
    new_observations = old_observations
    for owner in ('hom_postcomp_tele', 'hom_precomp_along_tele'):
        rule_start = 'rule @' + owner + '_fapp1_fapp0\n'
        assert new_observations.count(rule_start) == 1, owner
        start = new_observations.index(rule_start)
        end = new_observations.index(';', start) + 1
        old_rule = new_observations[start:end]
        new_observations = (new_observations[:start]
            + '// The former raw-to-ordinary telescope fold is replaced by\n'
              '// the Cartesian inclusion projection at the classifier owner.\n'
            + new_observations[end:])
        changes.append({'owner': owner + '_fapp1_fapp0 Cat specialization',
                        'reason': 'A Cartesian Hom arrow is not an ambient transfor until inclusion; the existing ordinary observation head is retained',
                        'retiredRuleSha256': sha(old_rule)})
        new_observations = new_observations.replace('@' + owner + '_fapp1_fapp0',
                                                    '@' + owner + '_transf')
    replace_once(old_observations, new_observations, 'ordinary observations of canonical Hom transfors',
                 'Retain existing tapp observations through their original ordinary-view heads after canonical action acquires the Cartesian profile')
    replace_once('''rule @tapp0_fapp0 $K Cat_cat _ _ $Y (@id (@Catd_cat $K) $E)
  ↪ @id Cat_cat (@fapp0 $K Cat_cat $E $Y);''',
                 '''rule @tapp0_fapp0 $K Cat_cart _ _ $Y (@id (@Catd_cat $K) $E)
  ↪ @id Cat_cart (@fapp0 $K Cat_cart $E $Y);''',
                 'displayed identity component',
                 'The original displayed identity now has Cartesian-coefficient components')

    a = body.index('// 6b. Internalized hom endpoint actions and rigid two-sided projections')
    b = body.index('// Product-valued off-diagonal components project componentwise.', a)
    old_root_views = body[a:b]
    new_root_views = old_root_views
    replacements = []
    for match in re.finditer(r'(?m)^rule\b', old_root_views):
        end = old_root_views.index(';', match.start()) + 1
        old_rule = old_root_views[match.start():end]
        lhs, rhs = old_rule.split('↪', 1)
        if not any(name in lhs for name in ('@hom_int_precomp_func ', '@hom_con_int_postcomp_func ', '@hom_int $')):
            continue
        lhs = lhs.replace('Cat_cat', 'Cat_cart')
        lhs = re.sub(r'(\(@hom_(?:int_precomp|con_int_postcomp)_func[^\n)]+\))',
                     r'(@strict_transfor _ _ _ _ \1)', lhs)
        generic = '''(@fapp1_fapp0 (Op_cat $A) (@Catd_cat $B)
        (@hom_int $A $B $F) $Y $X $f)'''
        if generic in lhs:
            lhs = lhs.replace(generic, '''(@strict_transfor _ _ _ _
        (@fapp1_fapp0 (Op_cat $A) (Functor_cart_cat $B Cat_cart)
          (@hom_int $A $B $F) $Y $X $f))''')
        replacements.append((old_rule, lhs + '↪' + rhs.replace('Functor_cat', 'Functor_cart_cat')))
    assert len(replacements) == 7, len(replacements)
    for old, new in replacements:
        assert new_root_views.count(old) == 1
        new_root_views = new_root_views.replace(old, new, 1)
    replace_once(old_root_views, new_root_views, 'ordinary component observations of whole Hom',
                 'Project canonical Cartesian family maps through the existing strict-transfor inclusion before ordinary tapp observations')

    # The two-parameter Cartesian packages have Cartesian parameter Homs.
    # Fixed ordinary whiskering above still acts on general lax transfors.
    for variance, args, parameter, left, right, first, second in (
            ('cov', 'X Y Z', '(Functor_cart_cat Y Z)', '(Functor_cart_cat X Y)', '(Functor_cart_cat X Z)', 'G', 'H'),
            ('con', 'Z X Y', '(Functor_cart_cat X Y)', '(Functor_cart_cat Y Z)', '(Functor_cart_cat X Z)', 'F', 'K')):
        generic = 'hom_postcomp_tele' if variance == 'cov' else 'hom_precomp_along_tele'
        base = 'comp_cat_' + variance + '_func_func'
        start = body.index('symbol ' + base + ' ')
        end = body.index(';', start) + 1
        replace_once(body[start:end], f'''symbol {base} [X Y Z : Cat]
  : τ (Functor {parameter} (Functor_cart_cat {left} {right}))
≔ @{generic}_func Cat_cart Cat_cart (@id_func Cat_cart) {args};''',
                     base + ' Cartesian profile',
                     'A parameterized Cartesian composition package must not silently make arbitrary lax squares commute')
        fixed = 'comp_cat_' + variance + '_cart_func'
        low = f'(@{fixed} X Y Z {first})'
        high = f'(@{fixed} X Y Z {second})'
        # Express the endpoints through the already-declared generic owner;
        # fixed Cart aliases are introduced later with closure, not forward references.
        if variance == 'cov':
            low = f'(@hom_postcomp_func Cat_cart Cat_cart (@id_func Cat_cart) X Y Z {first})'
            high = f'(@hom_postcomp_func Cat_cart Cat_cart (@id_func Cat_cart) X Y Z {second})'
            binders = '[G H : τ (Functor Y Z)]'
        else:
            low = f'(@hom_precomp_along_func Cat_cart Cat_cart (@id_func Cat_cart) Z X Y {first})'
            high = f'(@hom_precomp_along_func Cat_cart Cat_cart (@id_func Cat_cart) Z X Y {second})'
            binders = '[F K : τ (Functor X Y)]'
        owner = base + '_fapp1_func'
        start = body.index('symbol ' + owner + ' ')
        end = body.index(';', start) + 1
        replace_once(body[start:end], f'''symbol {owner} [X Y Z : Cat] {binders}
  : τ (Functor (Hom_cat {parameter} {first} {second})
      (Hom_cat (Functor_cart_cat {left} {right}) {low} {high}))
≔ @{generic}_fapp1_func Cat_cart Cat_cart (@id_func Cat_cart) {args} {first} {second};''',
                     owner + ' Cartesian profile', 'The whole first Hom retains the actual Cartesian parameter profile')
        owner = base + '_transf'
        start = body.index('symbol ' + owner + ' ')
        end = body.index(';', start) + 1
        replace_once(body[start:end], f'''symbol {owner} [X Y Z : Cat] {binders}
  (eta : τ (Hom {parameter} {first} {second}))
  : τ (Transf {low} {high})
≔ @{generic}_transf Cat_cart Cat_cart (@id_func Cat_cart) {args} {first} {second} eta;''',
                     owner + ' ordinary view', 'Observe the Cartesian parameter action as an ordinary transfor, without admitting a raw parameter')

    replace_once('constant symbol op : τ (Functor Cat_cat Cat_cat);',
                 'constant symbol op : τ (Functor (CoAt2_cat Cat_cart) Cat_cart);',
                 'op', 'Dimension-one transpose is whole on the Cartesian coefficient, with the required dimension-two shift')
    replace_once('rule @fapp0 Cat_cat Cat_cat op $A ↪ Op_cat $A;',
                 'rule @fapp0 (CoAt2_cat Cat_cart) Cat_cart op $A ↪ Op_cat $A;',
                 'op object action', 'Same category-level transpose with its corrected coefficient source')
    replace_once('rule @fapp1_fapp0 Cat_cat Cat_cat op $A $B $F ↪ @Op_func $A $B $F;',
                 '''rule @fapp1_func (CoAt2_cat Cat_cart) Cat_cart op $A $B
  ↪ Op_func_func $A $B;
rule @fapp1_fapp0 (CoAt2_cat Cat_cart) Cat_cart op $A $B $F ↪ @Op_func $A $B $F;''',
                 'op whole first Hom', 'Use the actual Cartesian mapping-category action, not a same-profile map on arbitrary lax transformations')
    replace_once('injective symbol Op_catd_func (Z : Cat) : τ (Functor (Catd_cat Z) (Catd_cat Z));',
                 '''injective symbol Op_catd_func (Z : Cat)
  : τ (Functor (CoAt2_cat (Functor_cart_cat Z Cat_cart))
      (Functor_cart_cat (CoAt2_cat Z) Cat_cart));''',
                 'Op_catd_func', 'The shifted-family operator acts on Cartesian diagram maps; ordinary FF is not silently admitted')
    replace_once('''rule @hom_postcomp_func Cat_cat Cat_cat (@id Cat_cat Cat_cat) $Z Cat_cat Cat_cat op
  ↪ @Op_catd_func $Z;''', '''// Formation of the shifted family uses the original postcomposition owner.
rule @comp_fapp0 Cat_cat _ _ _
      (@hom_postcomp_func Cat_cart Cat_cart (@id Cat_cat Cat_cart)
        (CoAt2_cat $K) (CoAt2_cat Cat_cart) Cat_cart op)
      (CoAt2_func_func $K Cat_cart)
  ↪ Op_catd_func $K;''',
                 'Op_catd_func formation', 'Preserve the semantic composite of dimension-two functor action and coefficient postcomposition')

    a = body.index('injective symbol Op_transf\n')
    b = body.index('// 6b. Internalized hom endpoint actions', a)
    old_transpose = body[a:b]
    old_decl_end = old_transpose.index(';') + 1
    new_transpose = '''injective symbol Op_transf
  [A B : Cat] [F G : τ (Functor A B)]
  (eta : τ (Hom (Functor_cart_cat A B) F G))
  : τ (Hom (Functor_cart_cat (Op_cat A) (Op_cat B))
      (@Op_func A B G) (@Op_func A B F));

// First arrow projection of the whole Cartesian transpose.
rule @fapp1_fapp0 _ _ (Op_func_func $A $B) $G $F $eta
  ↪ @Op_transf $A $B $F $G $eta;
''' + old_transpose[old_decl_end:].replace('Functor_cat', 'Functor_cart_cat')
    new_transpose = new_transpose.replace('''      (@Op_transf $A $B $F $G $eta)
  ↪ @tapp0_fapp0 $A $B $F $G $x $eta;''', '''      (@strict_transfor _ _ _ _ (@Op_transf $A $B $F $G $eta))
  ↪ @tapp0_fapp0 $A $B $F $G $x (@strict_transfor $A $B $F $G $eta);''')
    replace_once(old_transpose, new_transpose, 'Op_transf Cartesian mapping action',
                 'Dimension-one transpose of strict transfors is the Cartesian whole-map projection; the public lax total-opposite operation is distinct')
    replace_once('''rule @tapp1_func
      _ _
      _ _
      $x $y
      (@Op_transf $A $B $F $G $eta)
  ↪ @tapp1_func $A $B $F $G $y $x $eta;''',
                 '''rule @tapp1_func
      _ _
      _ _
      $x $y
      (@strict_transfor _ _ _ _ (@Op_transf $A $B $F $G $eta))
  ↪ @tapp1_func $A $B $F $G $y $x (@strict_transfor $A $B $F $G $eta);''',
                 'Op_transf whole ordinary observation',
                 'Observe the Cartesian transpose through the existing inclusion, retaining its ordinary action')
    replace_once('''rule @tapp1_fapp0 _ _ _ _ $x $y
      (@Op_transf $A $B $F $G $eta) $p
  ↪ @tapp1_fapp0 $A $B $F $G $y $x $eta $p;''',
                 '''rule @tapp1_fapp0 _ _ _ _ $x $y
      (@strict_transfor _ _ _ _ (@Op_transf $A $B $F $G $eta)) $p
  ↪ @tapp1_fapp0 $A $B $F $G $y $x (@strict_transfor $A $B $F $G $eta) $p;''',
                 'Op_transf capped ordinary observation',
                 'The same Cartesian-profile correction after capping')
    insert("// Point component of Path_cat_func's second action.",
           fragment('conventional_total_op_transfors.lpfragment') + '\n'
           + fragment('conventional_total_op_offdiagonal.lpfragment'),
           'Retain the qualified total reversal of arbitrary conventional-lax transfors and its correct post-boundary off-diagonal action')

    for owner, old_type, new_type in (
            ('Product_cat_fapp1_func', '(Functord_cat\n', '(@Transf_cat Cat_cat Cat_cat\n'),
            ('Product_cat_fapp1_fapp0_functord', '(Functord\n', '(@Transf Cat_cat Cat_cat\n')):
        start = body.index('symbol ' + owner + ' ')
        end = body.index(';', start) + 1
        old = body[start:end]
        assert old.count(old_type) == 1, owner
        replace_once(old, old.replace(old_type, new_type), owner,
                     'This original product-constructor parameter action is an ordinary public-Cat transformation, not a map between admitted Cartesian families')
    start = body.index('symbol Product_mapL_func_func ')
    end = body.index(';', start) + 1
    old = body[start:end]
    replace_once(old, old.replace('(@Functord_cat Cat_cat\n', '(@Transf_cat Cat_cat Cat_cat\n'),
                 'Product_mapL_func_func',
                 'Keep the same component-evaluation composition through the corrected ordinary product-constructor transformation classifier')

    a = body.index('/*\n  Opposite adjunction.')
    b = body.index('// 7e. Internal ordinary hom-action packages', a)
    old_adjunction = body[a:b]
    new_adjunction = (old_adjunction.replace('Op_cat', 'TotalOp_cat')
                      .replace('@Op_func', '@TotalOp_func')
                      .replace('Op_transf', 'TotalOp_transf'))
    new_adjunction = new_adjunction.replace('  Opposite adjunction.',
        '  Total-opposite adjunction (legacy public spelling Op_adjunction).')
    replace_once(old_adjunction, new_adjunction, 'Op_adjunction',
                 'Preserve general lax unit/counit transformations by using the qualified total-duality profile; do not silently require strict units')

    a = body.index('// 7e. Internal ordinary hom-action packages')
    b = body.index('// 8. Directed Cat-valued family constructors', a)
    old_internal = body[a:b]
    new_internal = re.sub(r'@hom_int\b', '@hom_int_view', old_internal)
    # Fixed-source/target components still land in the admitted coefficient.
    new_internal = re.sub(r'(\$A\s+)Cat_cat', r'\1Cat_cart', new_internal)
    new_internal = new_internal.replace('_ Cat_cat _ _', '_ Cat_cart _ _')
    for owner, varying in (('tapp1_con_int_fapp0_transf', 'G'), ('fapp1_con_int_transf', 'F')):
        start = new_internal.index('injective symbol ' + owner + '\n')
        begin = new_internal.index('  : τ (Transf\n', start)
        end = new_internal.index(';', begin) + 1
        new_internal = new_internal[:begin] + f'''  : τ (Transf
      (@hom_con_int_view A A (@id_func A))
      (@comp_cat_fapp0 A B (@Catd_cat (Op_cat A))
        (@hom_con_int_view B A F) {varying}));''' + new_internal[end:]
    for owner in ('tapp1_con_int_fapp0_transf', 'tapp1_con_at_transf'):
        pattern = (r'(?m)^unif_rule\n  @tapp1_(?:int_fapp0_transf|at_transf)\n'
                   r'[\s\S]*?≡ @' + owner + r'[\s\S]*?\];')
        matches = list(re.finditer(pattern, new_internal))
        assert len(matches) == 1, owner
        old = matches[0][0]
        new = old.replace('$epsilon2\n', '(@strict_transfor $A $B $F $G $U)\n')
        new = new.replace('$epsilon2 $Y\n', '(@strict_transfor $A $B $F $G $U) $Y\n')
        new = new.replace('(@Op_transf $A $B $F $G $epsilon2)',
                          '''(@strict_transfor (Op_cat $A) (Op_cat $B)
      (@Op_func $A $B $G) (@Op_func $A $B $F) (@Op_transf $A $B $F $G $U))''')
        assert '$epsilon2' not in new, owner
        new_internal = new_internal.replace(old, new, 1)
    replace_once(old_internal, new_internal, 'ordinary internal-action ladders',
                 'Keep general lax epsilon through ordinary whole-Hom inclusion views and direct contravariant roots; use transpose comparisons only for actual Cartesian inputs')

    insert('// Product homs compute componentwise.',
           '''// Cartesian mapping categories preserve target products.
rule Functor_cart_cat $X (Product_cat $A $B)
  ↪ Product_cat (Functor_cart_cat $X $A) (Functor_cart_cat $X $B);
''', 'The existing paired-functor computation also applies to the Cartesian mapping profile')
    start = body.index('symbol Product_pair_tele_func ')
    end = body.index(';', start) + 1
    old_pair = body[start:end]
    replace_once(old_pair, old_pair.replace('Functor_cat', 'Functor_cart_cat'),
                 'Product_pair_tele_func', 'Canonical pairing has strict naturality in its retained argument')
    insert('// Object projection ladder for the internalized product constructor.',
           '''// Cartesian parameter view of the original product constructor.
injective symbol Product_cat_cart_func
  : τ (Functor Cat_cat (Functor_cart_cat Cat_cat Cat_cat));
rule fapp0 Product_cat_cart_func $A ↪ Product_cat_fapp0_func $A;
// lhs-audit: keep 1 -- ordinary composition with the Cartesian mapping inclusion.
rule @comp_fapp0 Cat_cat _ _ _
      (Functor_cart_include Cat_cat Cat_cat) Product_cat_cart_func
  ↪ Product_cat_func;
''', 'Retain the original product constructor and partial actions while providing its required Cartesian parameter profile')
    insert('// 7b. Evaluation and fixed-object evaluation',
           fragment('production_cartesian_closure.lpfragment'),
           'Cartesian closure consumes canonical strict whiskering and product parameter actions')
    a = body.index('// 7b. Evaluation and fixed-object evaluation')
    b = body.index('// 7c. Ordinary curry and uncurry', a)
    old_eval = body[a:b]
    new_eval = old_eval.replace('Functor_cat', 'Functor_cart_cat')
    new_eval = new_eval.replace('(Transf_cat F G)', '(Hom_cat (Functor_cart_cat A B) F G)')
    new_eval = new_eval.replace('(@Transf_cat $A $B $F $G)',
                                '(Hom_cat (Functor_cart_cat $A $B) $F $G)')
    assert new_eval.count('↪ tapp1_fapp0 $eta $p;') == 2
    new_eval = new_eval.replace('↪ tapp1_fapp0 $eta $p;',
                               '↪ tapp1_fapp0 (@strict_transfor $A $B $F $G $eta) $p;')
    assert new_eval.count('↪ fapp0_func $x;') == 1
    new_eval = new_eval.replace('↪ fapp0_func $x;', '''↪ @comp_cat_fapp0
      (Functor_cart_cat $A $B) (Functor_cat $A $B) $B
      (@fapp0_func $A $B $x) (Functor_cart_include $A $B);''')
    replace_once(old_eval, new_eval, 'Cartesian evaluation ladder',
                 'Joint strict Cartesian evaluation accepts strict transfors; fixed ordinary evaluation remains available through inclusion')
    for owner in ('curry_func_func', 'curry_func', 'uncurry_func_func', 'uncurry_func'):
        start = body.index('symbol ' + owner + ' ')
        end = body.index(';', start) + 1
        old = body[start:end]
        new = old.replace('Functor_cat', 'Functor_cart_cat')
        new = re.sub(r'@comp_cat_(cov|con)_func\b', r'@comp_cat_\1_cart_func', new)
        new = new.replace('@Product_mapL_func_func', '@Product_mapL_cart_func_func')
        replace_once(old, new, owner,
                     'Keep the original Cartesian curry/uncurry composition body with its actual mapping profiles')
    product_uncurry = '@uncurry_func Cat_cat Cat_cat Cat_cat Product_cat_func'
    count = body.count(product_uncurry)
    assert count > 0
    body = body.replace(product_uncurry,
                        '@uncurry_func Cat_cat Cat_cat Cat_cat Product_cat_cart_func')
    changes.append({'owner': 'existing uncurried product-formation consumers',
                    'reason': 'Use the canonical Cartesian parameter view required by the corrected uncurry signature',
                    'count': count})

    a = body.index('// 8a. Fibre notation, pullback, and base-arrow transport')
    b = body.index('// 8b. Constant, terminal, opposite, and displayed composition', a)
    old_fibres = body[a:b]
    new_fibres = re.sub(r'((?:\$?[ABK])\s+)Cat_cat', r'\1Cat_cart', old_fibres)
    new_fibres = new_fibres.replace('@fapp0 _ Cat_cat (@Pullback_catd',
                                    '@fapp0 _ Cat_cart (@Pullback_catd')
    new_fibres = new_fibres.replace('id Cat_cat Cat_cat) Cat_cat $A $B $F',
                                    'id Cat_cat Cat_cat) Cat_cart $A $B $F')
    new_fibres = new_fibres.replace('(@fapp0_func Cat_cat Cat_cat Cat_cat)',
                                    '(@fapp0_func Cat_cat Cat_cat Cat_cart)')
    # Retain the still-valid public-Cat projected strict action as well.
    start = old_fibres.index('rule fapp0\n')
    end = old_fibres.index(';', start) + 1
    public_transport = old_fibres[start:end]
    cart_transport = re.sub(r'((?:\$?[ABK])\s+)Cat_cat', r'\1Cat_cart', public_transport)
    assert new_fibres.count(cart_transport) == 1
    new_fibres = new_fibres.replace(cart_transport, cart_transport + '\n\n'
        + '// The same valid strict-functor point action in the public universe.\n' + public_transport, 1)
    new_fibres = new_fibres.replace('''      (@Pullback_catd_func $B $D $G)
      (@hom_int $C $D $H)''', '''      (@hom_precomp_along_func Cat_cart Cat_cart (@id Cat_cat Cat_cart)
        Cat_cart $B $D $G)
      (@hom_int $C $D $H)''')
    replace_once(old_fibres, new_fibres, 'family fibres, transport and pullback',
                 'Apply the selected coefficient to actual family observations; retain ordinary raw-Cat action and the canonical whole Cartesian Hom reindexing')

    a = body.index('// 8b. Constant, terminal, opposite, and displayed composition')
    b = body.index('// Fixed-base layer: pointwise opposite of a directed family.', a)
    old_constants = body[a:b]
    new_constants = re.sub(r'(\$[ABK]\s+)Cat_cat', r'\1Cat_cart', old_constants)
    new_constants = new_constants.replace('(Functor_cat $A $A)', '(Functor_cart_cat $A $A)')
    replace_once(old_constants, new_constants, 'constant and terminal admitted families',
                 'Keep the existing object/transport computations with the Cartesian coefficient; constant Pi still uses default lax transformations')
    a = body.index('// Fixed-base layer: pointwise opposite of a directed family.')
    b = body.index('// Pointwise projection of displayed composition.', a)
    replace_once(body[a:b], fragment('production_cartesian_family_duality.lpfragment') + '\n',
                 'Op_catd and Op_funcd',
                 'The original family transpose uses the shifted base and Cartesian map profile; general lax FF is retained for the separate Homd-relative construction')

    a = body.index('// Pointwise projection of displayed composition.')
    b = body.index('// Fixed-base fibrewise-product structural owners.', a)
    old = body[a:b]
    new = re.sub(r'(\$K\s+)Cat_cat', r'\1Cat_cart', old)
    new = new.replace('↪ @comp_fapp0\n      Cat_cat', '↪ @comp_fapp0\n      Cat_cart')
    replace_once(old, new,
                 'displayed composition components',
                 'Vertical composition remains the original componentwise operation in the admitted coefficient')

    whole = fragment('conventional_total_op_whole_action.lpfragment')
    whole_rules = whole[whole.index('rule @fapp1_func'):].rstrip()
    assert body.count(whole_rules) == 1
    body = body.replace(whole_rules,
        '// Generic whole identity/composition action moved to the earlier composition owner.\n', 1)
    insert('// Ordinary category identity cuts: g ∘ id ↪ g and id ∘ f ↪ f.',
           whole, 'Relocate the unchanged original whole first-Hom action before the derived duality/family consumers')
    insert('/*\n   Typed equality view of the generic strict identity cut.',
           fragment('conventional_total_op_source_units.lpfragment') + '''
// The shifted family source likewise loses its dimension-two identity tag.
// lhs-audit: keep 1 -- CoAt2 is the erased-identity source discriminator.
rule @fapp1_fapp0 (CoAt2_cat $K) $D $F $x $x (@id $K $x)
  ↪ @id $D (@fapp0 (CoAt2_cat $K) $D $F $x);
''', 'Strict identity observations after duality has erased the original source tag')

    a = body.index('// Fixed-base fibrewise-product structural owners.')
    b = body.index('// 8c. Section categories and Pi action', a)
    old_products = body[a:b]
    new_products = old_products.replace('Cat_cat', 'Cat_cart').replace('Functor_cat', 'Functor_cart_cat')
    new_products = new_products.replace('Product_cat_cart_func', 'Product_cat_coeff_func')
    new_products = re.sub(r'@comp_cat_(cov|con)_func\b', r'@comp_cat_\1_cart_func', new_products)
    replace_once(old_products, fragment('production_cartesian_product.lpfragment') + '\n' + new_products,
                 'fibrewise products',
                 'Retain the original uncurry/product/pair construction and displayed owners with the admitted coefficient and its actual Cartesian fibre Homs')

    # The original Homd/Pi/Sigma tail remains for coupled adaptation. The
    # separately emitted prefix qualifies the preceding source only; passing
    # that target must not be reported as a passing complete kernel.
    out = root / 'tmp/probes/production_owner_migration'
    package = out / 'package'
    package.mkdir(parents=True, exist_ok=True)
    baseline_package = out / 'baseline_package'
    baseline_package.mkdir(exist_ok=True)
    assert not list(package.rglob('*.lpo')), 'Source-only candidate contains compiled objects'
    assert not list(baseline_package.rglob('*.lpo')), 'Source-only baseline contains compiled objects'
    (baseline_package / 'emdash3_2.lp').write_text(original)
    (baseline_package / 'emdash3_2_gray_profiles.lp').write_text(original_profiles)
    (baseline_package / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    (out / 'baseline.lp').write_text(original)
    (out / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    (package / 'emdash3_2.lp').write_text(body)
    (package / 'emdash3_2_gray_profiles.lp').write_text(profiles)
    (package / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    controls = (fragment('production_owner_controls.lpfragment') + '\n'
                + fragment('whole_controls.lpfragment') + '\n'
                + fragment('intrinsic_controls.lpfragment').replace('assertnot ', 'assert ')
                + '\n' + fragment('conventional_lax_controls.lpfragment')
                + '\n' + fragment('conventional_lax_projection_controls.lpfragment'))
    (package / 'owner_controls.lp').write_text('require open emdash.emdash3_2;\n\n' + controls)
    foundation_boundary = '// 8c. Section categories and Pi action'
    assert body.count(foundation_boundary) == 1
    (package / 'foundations_prefix.lp').write_text(body[:body.index(foundation_boundary)]
        + '\n' + fragment('production_foundations_controls.lpfragment'))
    # Stage the pre-goal reviewer and exactly its imported source closure.
    # Only the explicit strict-default proof/control adaptations below and
    # the upstream core/profile owners override those original inputs.
    dependencies = {}
    visited = set()

    def stage(path):
        if path in visited:
            return
        visited.add(path)
        if path == 'emdash3_2.lp':
            text = body
        elif path == 'emdash3_2_gray_profiles.lp':
            text = profiles
        else:
            text = subprocess.check_output(
                ['git', 'show', PIN + ':emdash2/' + path], cwd=root, text=True)
            dependencies[path] = sha(text)
            baseline_target = baseline_package / path
            baseline_target.parent.mkdir(parents=True, exist_ok=True)
            baseline_target.write_text(text)
            if path == 'emdash3_2_one_cat_action_paths.lp':
                marker = 'symbol one_cat_composition_path '
                assert text.count(marker) == 1
                start = text.index(marker)
                begin = text.index('≔', start)
                end = text.index(';', begin) + 1
                old = text[begin:end]
                replacement = '''≔ @eq_refl (Hom B (@fapp0 A B F x) (@fapp0 A B F z))
    (@fapp1_fapp0 A B F x z (@comp_fapp0 A x y z g f));'''
                text = text[:begin] + replacement + text[end:]
                changes.append({'source': path, 'owner': 'one_cat_composition_path',
                                'reason': 'Existing lax-cell proof no longer joins after strict-default compositor normalization; preserve its statement and use strict computation',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(replacement)})
            if path == 'emdash3_2_represented_comma_families.lp':
                marker = 'protected symbol comma_basechange_sigma_map_composition '
                assert text.count(marker) == 1
                addition = fragment('production_comma_equivalence.lpfragment')
                text = text.replace(marker, addition + '\n' + marker, 1)
                changes.append({'source': path, 'before': marker,
                                'reason': 'Map the actual identity-compositor inverse evidence through original whiskering instead of imposing additional runtime projection laws',
                                'insertedSha256': sha(addition)})
                marker = 'protected symbol comma_basechange_observation_pre_points '
                assert text.count(marker) == 1
                start = text.index(marker)
                begin = text.index('≔', start)
                end = text.index(';', begin) + 1
                old = text[begin:end]
                post_points = text[start:end].replace('comma_basechange_observation_pre',
                                                      'comma_basechange_observation_post')
                post_points = post_points.replace('comma_basechange_observation_inner',
                                                  'comma_basechange_observation_outer')
                replacement = '''≔ λ z : τ (Obj (@Sigma_cat A (@Pullback_catd A K E F))),
  let pre : τ (@OmegaEquivAlong
      (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
      (@comma_basechange_observation_inner A K C F E P)
      (@comma_basechange_observation_middle A K C F E P)
      (@comma_basechange_observation_pre A K C F E P))
    ≔ @comma_strict_omega_map
      (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) (Product_cat K C))
      (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
      (@comp_cat_cov_func (@Sigma_cat A (@Pullback_catd A K E F))
        (Product_cat K C) C (@Product_projR_func K C))
      (@comma_basechange_sigma_basechange_right A K F E (@Const_catd K C) P)
      (@comma_basechange_sigma_basechange_middle A K F E (@Const_catd K C) P)
      (@comma_basechange_sigma_basechange_pre A K F E (@Const_catd K C) P)
      (@comma_pre_cell_omega (@Catd_cat K) Cat_cat
        (@comma_basechange_sigma_basechange_source A K F) (@Sigma_func K)
        (@sigma_pullback_total_transf A K F)
        E (@Const_catd K C) (@Const_catd K C) P (@id (@Catd_cat K) (@Const_catd K C))) in
  @comma_strict_omega_map
    (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C) C
    (@fapp0_func (@Sigma_cat A (@Pullback_catd A K E F)) C z)
    (@comma_basechange_observation_inner A K C F E P)
    (@comma_basechange_observation_middle A K C F E P)
    (@comma_basechange_observation_pre A K C F E P) pre;'''
                text = text[:begin] + replacement + '\n\n' + post_points + text[end:]
                changes.append({'source': path, 'owner': 'comma_basechange_observation_pre_points',
                                'reason': 'Map inverse evidence of the extracted default pre cell through the original projection, then evaluate at an arbitrary total object',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(replacement),
                                'postPointsSha256': sha(post_points)})
                marker = 'protected symbol comma_basechange_observation_pre_equiv '
                assert text.count(marker) == 1
                start = text.index(marker)
                end = text.index(';', text.index('≔', start)) + 1
                post_equiv = text[start:end].replace('comma_basechange_observation_pre',
                                                     'comma_basechange_observation_post')
                post_equiv = post_equiv.replace('comma_basechange_observation_inner',
                                                'comma_basechange_observation_outer')
                text = text[:end] + '\n\n' + post_equiv + text[end:]
                marker = 'protected symbol comma_basechange_observation_basechange_component '
                assert text.count(marker) == 1
                addition = fragment('production_comma_basechange_equivalence.lpfragment')
                text = text.replace(marker, addition + '\n' + marker, 1)
                changes.append({'source': path, 'owner': 'comma_basechange_observation_basechange_equiv',
                                'reason': 'The old second-step reflexivity no longer follows the newly mapped pre inverse; retain both comparison maps and compose their inverse evidence',
                                'postEquivSha256': sha(post_equiv), 'insertedSha256': sha(addition)})
                marker = 'protected symbol comma_basechange_gamma_target_link_equiv '
                assert text.count(marker) == 1
                start = text.index(marker)
                begin = text.index('≔', start)
                end = text.index(';', begin) + 1
                old = text[begin:end]
                replacement = '''≔ @one_cat_transf_pointwise_omega_along K Y Y1
    (@comma_section_gamma_target_observed_op K X Y J A D h)
    (@represented_comma_hom_action_target_func K X Y J A D h)
    (@comma_basechange_gamma_target_link K X Y J A D h Y1)
    (λ x : τ (Obj K), @comma_op_omega_along Y
      (@fapp0 (Op_cat K) (Op_cat Y) (@comma_basechange_gamma_target_raw0 K X Y J A D h) x)
      (@fapp0 (Op_cat K) (Op_cat Y) (@comma_basechange_gamma_target_raw2 K X Y J A D h) x)
      (@tapp0_fapp0 (Op_cat K) (Op_cat Y)
        (@comma_basechange_gamma_target_raw0 K X Y J A D h)
        (@comma_basechange_gamma_target_raw2 K X Y J A D h) x
        (@comma_basechange_gamma_target_raw_link K X Y J A D h Y1))
      (@comma_strict_omega_map (Functor_cat (Op_cat K) (Op_cat Y)) (Op_cat Y)
        (@fapp0_func (Op_cat K) (Op_cat Y) x)
        (@comma_basechange_gamma_target_raw0 K X Y J A D h)
        (@comma_basechange_gamma_target_raw2 K X Y J A D h)
        (@comma_basechange_gamma_target_raw_link K X Y J A D h Y1)
        (@comma_basechange_gamma_target_raw_link_equiv K X Y J A D h Y1)));'''
                text = text[:begin] + replacement + text[end:]
                addition = fragment('production_comma_target_equivalence.lpfragment')
                text = text.replace(marker, addition + '\n' + marker, 1)
                changes.append({'source': path, 'owner': 'comma_basechange_gamma_target_link_equiv',
                                'reason': 'Preserve the original comparison and construct its inverse evidence before evaluating components',
                                'insertedSha256': sha(addition),
                                'oldBodySha256': sha(old), 'newBodySha256': sha(replacement)})
            if path == 'examples/gray_profiles.lp':
                old = '''assertnot [A B : Cat]
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y)) ⊢
  @strict_functor_compositor_lhs
    A B (@example_unprofiled_functor A B) X Y Z g f
  ≡ @strict_functor_compositor_rhs
      A B (@example_unprofiled_functor A B) X Y Z g f;'''
                assert text.count(old) == 1
                replacement = old.replace('assertnot ', 'assert ', 1)
                text = text.replace(old, replacement, 1)
                text = text.replace('// Rigid ambient negative control, deliberately outside StrictFunctor.',
                                    '// Ambient functor: the strict default no longer requires a wrapper.')
                text = text.replace('// Composition is selected only by the stable evidence-bearing view.',
                                    '// The legacy stable view still computes during wrapper migration.')
                changes.append({'source': path, 'owner': 'unprofiled compositor endpoint comparison',
                                'reason': 'The default functor now preserves composition; retain all unrelated negative controls',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(replacement)})
            target = package / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)
        for command in re.findall(r'(?m)^\s*require(?:\s+open)?\s+([^;]+);', text):
            for module in command.split():
                assert re.fullmatch(r'emdash(?:\.[A-Za-z0-9_]+)+', module), module
                stage(module.removeprefix('emdash.').replace('.', '/') + '.lp')

    stage('examples/gray_profiles.lp')
    delta = difflib.SequenceMatcher(None, original.splitlines(keepends=True),
                                   body.splitlines(keepends=True), autojunk=False).get_opcodes()
    original_lines_retained = all(kind in ('equal', 'insert') for kind, *_ in delta)
    declaration = r'(?m)^(?:(?:constant|injective|protected|private)\s+)?symbol\s+([A-Za-z0-9_]+)\b'
    original_names = re.findall(declaration, original)
    candidate_names = iter(re.findall(declaration, body))
    assert all(any(candidate == name for candidate in candidate_names)
               for name in original_names), 'An original declaration was dropped or reordered'
    inputs[str(Path(__file__).resolve().relative_to(root))] = sha(Path(__file__).read_text())
    manifest = {
        'status': 'in-progress full-source upstream migration; not final foundation qualification',
        'sourcePin': PIN, 'originalCoreSha256': CORE_SHA,
        'originalCoreLines': len(original.splitlines()), 'candidateCoreLines': len(body.splitlines()),
        'originalDownstreamSectionsRetained': True,
        'originalCoreLineOrderVerified': original_lines_retained,
        'originalNamedDeclarationSequenceVerified': True,
        'originalDependencyInputs': dependencies,
        'changes': changes, 'relocatedDeclarations': relocated,
        'authoringInputs': inputs,
        'outputs': {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in [out / 'baseline.lp', package / 'emdash3_2.lp',
                              package / 'emdash3_2_gray_profiles.lp', package / 'owner_controls.lp',
                              package / 'foundations_prefix.lp',
                              baseline_package / 'emdash3_2.lp', baseline_package / 'emdash3_2_gray_profiles.lp']
                    + [package / path for path in dependencies]},
        'stillRequired': ['Whole varying-base Pi and admitted meta-family interfaces',
                          'Selected Q/Homd/Sigma integration with general lax FF',
                          'Whole duality/adjunction and closure-consumer qualification',
                          'Downstream qualification and retirement of redundant strict wrappers'],
        'excluded': ['Auxiliary Sigma fibre-composition audit owner',
                     'Unrestricted Cartesian evaluation on lax transformations',
                     'Optional normalization redesign'],
    }
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted full pre-goal baseline and upstream owner migration; no original tail omitted.')


if __name__ == '__main__':
    main()
