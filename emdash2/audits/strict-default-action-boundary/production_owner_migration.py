#!/usr/bin/env python3
"""Stage required upstream owners in a full copy of the pre-goal kernel.

This is an in-progress production migration, not another foundation model.
No original downstream section is truncated. Owner checks and consumer
migration determine qualification; successful emission does not.

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
    insert('// Hom-action functoriality for precomposition. The composition orientation is',
           fragment('production_cat_precomposition_actions.lpfragment'),
           'Cat-valued precomposition evaluator: same composed-functor projection outline as postcomposition, retaining the whole precomposition owner and its next Hom action')
    insert('/*\n  The former whole post/left and pre/right strict-functoriality accumulation\n',
           fragment('whole_rules.lpfragment') + '\n' + fragment('projected_rules.lpfragment')
           + '\n' + fragment('conventional_lax_projection_readings.lpfragment')
           + '\n' + fragment('production_conventional_pre_reading.lpfragment')
           + '\n' + fragment('conventional_lax_rules.lpfragment'),
           'Strict functor action and conventional-lax pre/right action at the existing whole/projection owners')
    replace_once('''rule @hom_postcomp_fapp0
      $A $A (@id Cat_cat $A) $W $Y $Z $q
      (@hom_postcomp_fapp0 $A $A (@id Cat_cat $A) $W $X $Y $p $g)
  ↪ @hom_postcomp_fapp0
      $A $A (@id Cat_cat $A) $W $X $Z
      (@comp_fapp0 $A $X $Y $Z $q $p)
      $g;
''', fragment('production_postcomposition_inverse.lpfragment'),
                 'identity-family postcomposition on a composite',
                 'Keep consecutive represented cuts visible so the existing computational-inverse rules survive composition; reverse only this capped equation, retaining its whole functor owner')
    replace_once('''with @hom_postcomp_fapp0 $A $A (@id Cat_cat $A) $X $X $Y $f (@id $A $X) ↪ $f;''',
                 '''// The identity's inferred category may reduce through a duality first.
with @hom_postcomp_fapp0 $A $A (@id Cat_cat $A) $X $X $Y $f (@id _ $X) ↪ $f;''',
                 'identity input of represented postcomposition',
                 'Let the typed represented owner determine the identity category after duality normalization; do not discriminate on the erased category annotation')
    precomp_identity = '''rule @hom_precomp_along_fapp0
      $A
      $B
      $F
      _
      $W
      $X
      $h
      (@id $B _)
  ↪ @fapp1_fapp0 $A $B $F $W $X $h;'''
    replace_once(precomp_identity,
                 '// The identity category can normalize through duality before this cut.\n'
                 + precomp_identity.replace('(@id $B _)', '(@id _ _)'),
                 'identity input of represented precomposition',
                 'The typed precomposition owner determines the identity endpoints; allow its inferred category annotation to normalize through total duality')
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
    profile_tail = '// Profile-guarded whole target/right reading.'
    assert profiles.count(profile_tail) == 1
    begin = profiles.index(profile_tail)
    old = profiles[begin:]
    replacement = fragment('production_profile_readings.lpfragment')
    profiles = profiles[:begin] + replacement
    changes.append({'source': 'emdash3_2_gray_profiles.lp',
                    'owner': 'strict_functord_transport_rhs_tele_path / strict_functord_transport_rhs_path',
                    'reason': 'Use the admitted Cartesian family coefficient and derive the existing compatibility paths from the default pre/right comparison; retire its two redundant profile-only unifiers',
                    'oldBodySha256': sha(old), 'newBodySha256': sha(replacement)})
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
    a = body.index('// Internalized-x prerequisite: directed-family category formation as a')
    b = body.index('// Internalized pointwise opposite on directed families.', a)
    old_classifier = body[a:b]
    replace_once(old_classifier,
                 '// Varying-base family formation is defined after its canonical Hom owner.\n\n',
                 'Catd_cat_func / Catd_catd_con relocation',
                 'The whole Cartesian parameter family is derived from Hom(Cat_cart), not a lift of lax diagram categories')
    relocated.append({'symbols': ['Catd_cat_func', 'Catd_catd_con'],
                      'originalBlockSha256': sha(old_classifier),
                      'reason': 'Dependency-forced semantic definition after canonical Hom'})

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
    insert('// Applying the telescope at p yields the capped represented-object action.',
           '''// Unit after the canonical Hom source action has projected to its
// stable head. This is the identity law of the same strict Hom functor.
rule @hom_int_precomp_func $A $B $F $X $X (@id _ $X)
  ↪ @id (Functor_cart_cat $B Cat_cart) (@hom_ $A $B $F $X);
''', 'The actual Homd target-map identity consumes the stable native Hom projection')
    insert(section_end, fragment('production_family_classifier.lpfragment'),
           'Define the original varying-base family names by the actual Cartesian Hom owner')
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
    # TotalOp_cat is now a reducible alias. The inner Op_adjunction already
    # determines these inferred category/functor arguments; matching the alias
    # here breaks the canonical involution and unit/counit projections.
    old_adjunction_slots = '      (TotalOp_cat $B) (TotalOp_cat $A)\n      _\n      _\n'
    assert new_adjunction.count(old_adjunction_slots) == 3
    new_adjunction = new_adjunction.replace(old_adjunction_slots, '      _ _ _ _\n')
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
    insert('// 7f. Target-internalized ordinary hom-action mirror',
           fragment('production_internal_x_profile.lpfragment'),
           'Canonical strict-x refinement of the pre/right-normal internal action, retaining its whole ordinary view and lax inner y-action')

    insert('// Product homs compute componentwise.',
           '''// Cartesian mapping categories preserve target products.
rule Functor_cart_cat $X (Product_cat $A $B)
  ↪ Product_cat (Functor_cart_cat $X $A) (Functor_cart_cat $X $B);
''', 'The existing paired-functor computation also applies to the Cartesian mapping profile')
    insert('// Generic projections of an arbitrary object of a Sigma total.',
           '''// Sufficient object-carrier congruence for the same Sigma constructor.
// Obj is not injective: this only compares the actual bases and whole families
// to propagate an already justified proof-time endpoint comparison.
unif_rule Obj (@Sigma_cat $K $E) ≡ Obj (@Sigma_cat $K0 $E0)
  ↪ [ $K0 ≡ $K; $E0 ≡ $E ];
''', 'Propagate proved family comparisons through the Sigma object facade without making Obj injective')
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
    old_eval_point = 'rule fapp0 (@Eval_func $A $B) (Struct_sigma $F $x)\n  ↪ fapp0 $F $x;'
    assert new_eval.count(old_eval_point) == 1
    new_eval = new_eval.replace(old_eval_point,
        '// Evaluate the actual pair projections even when the argument is neutral.\n'
        '// This is local to Eval, not a global product/Sigma eta rule.\n'
        'rule fapp0 (@Eval_func $A $B) $z\n'
        '  ↪ @fapp0 $A $B (sigma_Fst $z) (sigma_Snd $z);')
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
    a = body.index('// Arrow action of the internalized Catd constructor. `Catd_cat_func` is a')
    b = body.index('// Pointwise projection for the hom-action of family pullback.', a)
    replace_once(body[a:b],
                 '// The Cartesian varying-base constructor computes through hom_con;\n'
                 '// fixed lax-family pullback retains its separate existing owner.\n\n',
                 'Catd_cat_func legacy raw action fold',
                 'Do not equate Cartesian parameter reindexing with the larger lax diagram-map functor')
    insert('// The Cartesian varying-base constructor computes through hom_con;',
           '''// Direct proof-time reading of represented-family reindexing.
// The semantic comp/Pullback comparison and Pullback(hom_) accumulation
// already express this law; the checker does not chain those comparisons.
unif_rule @comp_fapp0 Cat_cat $K $C Cat_cart
      (@hom_ $C $C (@id Cat_cat $C) $w) $F
  ≡ @hom_ $C0 $K0 $F0 $w0
  ↪ [ $C ≡ $C0; $K ≡ $K0; $F ≡ $F0; $w ≡ $w0 ];
''', 'The actual Homd target index consumes both existing represented-family reindexing presentations')

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
    for projection in ('fapp0', 'fapp1_fapp0', 'fapp1_func'):
        original_lhs = f'rule @{projection} $A $C (@comp_fapp0 Cat_cat $A $B $C $F $G)'
        replace_once(original_lhs,
            '// The typed composite supplies its own source and target; caller\n'
            '// annotations may be a proof-time category facade.\n'
            + original_lhs.replace(f'@{projection} $A $C', f'@{projection} _ _', 1),
            projection + ' composite inferred annotations',
            'The ordinary Yoneda view is applied through Psh_cat rather than the literal Catd_cat target; recover inferred annotations from the visible composite')
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

    insert('// Semantic uncurry package through fixed-right product action and evaluation.',
           fragment('production_lax_curry.lpfragment'),
           'One-way lax currying for the original raw ProfMap consumer; object action reuses Cartesian curry and inclusion, without claiming an ambient Cartesian inverse')

    a = body.index('// 8c. Section categories and Pi action')
    b = body.index('// 8d. Fibre covariance and dependent-hom endpoint notation', a)
    old_sections = body[a:b]
    new_sections = old_sections.replace("@Transf_cat $K' Cat_cat", "@Transf_cat $K' Cat_cart")
    new_sections = new_sections.replace('(Op_cat Cat_cat)', '(Op_cat Cat_cart)')
    new_sections = new_sections.replace('//   Pi_int_funcd[K] = Pi_func(K)',
        '//   Pi_int_funcd[K] = Pi_func(K) after the Cartesian-diagram inclusion')
    new_sections = new_sections.replace('// The base is Op(Cat) because section categories pull back contravariantly\n// along functors.',
        '// The base is T(Cat_cart). The parameter fibres use Cartesian diagram\n'
        '// maps; their inclusion retains the existing lax section operation.')
    new_sections = new_sections.replace('// Base component of internal Pi: Pi_int_funcd[K] ↪ Pi_func(K).',
        '// Base component: restrict the existing Pi along its actual diagram inclusion.')
    new_sections = new_sections.replace('//   for G : K ⊢ Cat^op,',
        '//   for G : K ⊢ T(Cat_cart),')
    new_sections = new_sections.replace('//   Pi_pullback_funcd(G)[x] = Pi_func(G[x])',
        '//   Pi_pullback_funcd(G)[x] = Pi_func(G[x]) after Cartesian-diagram inclusion')
    new_sections = new_sections.replace('// Pointwise projection: Pi_pullback_funcd(G)[x] ↪ Pi_func(G[x]).',
        '// Component after base pullback, retaining the same inclusion before Pi.')
    new_sections = new_sections.replace('''      (Op_cat Cat_cart)
      Cat_cat
      _
      _
      $K
      Pi_int_funcd
  ↪ @Pi_func $K;''', '''      (Op_cat Cat_cart)
      Cat_cart
      _
      _
      $K
      Pi_int_funcd
  ↪ @comp_cat_fapp0 (Functor_cart_cat $K Cat_cart) (Catd_cat $K) Cat_cat
      (@Pi_func $K) (Functor_cart_include $K Cat_cart);''')
    new_sections = new_sections.replace('''      $K
      Cat_cat
      _
      _
      $x
      (@Pi_pullback_funcd $K $G)
  ↪ @Pi_func (@fapp0 $K (Op_cat Cat_cart) $G $x);''', '''      $K
      Cat_cart
      _
      _
      $x
      (@Pi_pullback_funcd $K $G)
  ↪ @comp_cat_fapp0
      (Functor_cart_cat (@fapp0 $K (Op_cat Cat_cart) $G $x) Cat_cart)
      (Catd_cat (@fapp0 $K (Op_cat Cat_cart) $G $x)) Cat_cat
      (@Pi_func (@fapp0 $K (Op_cat Cat_cart) $G $x))
      (Functor_cart_include (@fapp0 $K (Op_cat Cat_cart) $G $x) Cat_cart);''')
    new_sections = new_sections.replace('''≔ comp_cat_fapp0
     (@fapp0_func Terminal_cat (Fibre_cat E k) Terminal_obj)
     (@tapp0_func K Cat_cat (@Const_catd K Terminal_cat) E k);''', '''≔ @comp_cat_fapp0 (Pi_cat E)
    (Functor_cart_cat Terminal_cat (Fibre_cat E k)) (Fibre_cat E k)
    (@comp_cat_fapp0
      (Functor_cart_cat Terminal_cat (Fibre_cat E k))
      (Functor_cat Terminal_cat (Fibre_cat E k)) (Fibre_cat E k)
      (@fapp0_func Terminal_cat (Fibre_cat E k) Terminal_obj)
      (Functor_cart_include Terminal_cat (Fibre_cat E k)))
    (@tapp0_func K Cat_cart (@Const_catd K Terminal_cat) E k);''')
    # Pi is the terminal-source Hom of Catd(K), so its canonical formation
    # has the same Cartesian target as represented Hom. Its input maps and
    # section objects remain the ordinary lax displayed ones.
    new_sections = new_sections.replace('Cat_cat', 'Cat_cart')
    new_sections = new_sections.replace('injective symbol Pi_func (K : Cat)',
        '// The terminal-source Hom profile changes the formation target,\n'
        '// not the existing lax section or displayed-map classifiers.\n'
        'injective symbol Pi_func (K : Cat)')
    replace_once(old_sections, new_sections, 'Pi and varying-base section interface',
                 'Retain lax sections and fixed-base maps; use the canonical represented-Hom formation target and the existing Cartesian parameter inclusion')

    a = body.index('// 8d. Fibre covariance and dependent-hom endpoint notation')
    b = body.index('// 9. Directed Sigma categories and maps between totals', a)
    old_transport_leaf = body[a:b]
    new_transport_leaf = old_transport_leaf.replace('''≔ comp_cat_fapp0
     (@fapp0_func (Fibre_cat E x) (Fibre_cat E y) u)
     (@fapp1_func K Cat_cat E x y);''', '''≔ @comp_cat_fapp0 (Hom_cat K x y)
    (Functor_cart_cat (Fibre_cat E x) (Fibre_cat E y)) (Fibre_cat E y)
    (@comp_cat_fapp0
      (Functor_cart_cat (Fibre_cat E x) (Fibre_cat E y))
      (Functor_cat (Fibre_cat E x) (Fibre_cat E y)) (Fibre_cat E y)
      (@fapp0_func (Fibre_cat E x) (Fibre_cat E y) u)
      (Functor_cart_include (Fibre_cat E x) (Fibre_cat E y)))
    (@fapp1_func K Cat_cart E x y);''')
    new_transport_leaf = new_transport_leaf.replace(
        ': τ (Functor (Op_cat (Hom_cat Z x y)) Cat_cat)',
        ': τ (Functor (Op_cat (Hom_cat Z x y)) Cat_cart)')
    new_transport_leaf = new_transport_leaf.replace('@tapp0_fapp0 Z Cat_cat D E y FF',
                                                    '@tapp0_fapp0 Z Cat_cart D E y FF')
    replace_once(old_transport_leaf, new_transport_leaf, 'fibre transport and defined Homd leaf',
                 'Keep the existing evaluation/composition bodies through Cartesian coefficient inclusion; the defined relative leaf retains arbitrary lax FF')

    replace_once('rule Op_cat Terminal_cat ↪ Terminal_cat;',
                 'rule Op_cat Terminal_cat ↪ Terminal_cat;\nrule CoAbove2_cat Terminal_cat ↪ Terminal_cat;',
                 'total duality terminal category', 'The corrected negative Sigma also uses total reversal')
    replace_once('''rule Op_cat (Product_cat $A $B)
  ↪ Product_cat (Op_cat $A) (Op_cat $B);''', '''rule Op_cat (Product_cat $A $B)
  ↪ Product_cat (Op_cat $A) (Op_cat $B);
rule CoAbove2_cat (Product_cat $A $B)
  ↪ Product_cat (CoAbove2_cat $A) (CoAbove2_cat $B);''',
                 'total duality product', 'Retain product normal forms in the explicit constant-family Sigma-Hom')
    total_family = (fragment('total_op_family.lpfragment')
                    .replace('TotalOp_func_func', 'TotalOp_cart_func_func')
                    .replace('total_op', 'total_op_cart').replace('Cat_cat', 'Cat_cart'))
    total_family = (total_family.replace('@comp_fapp0 Cat_cart', '@comp_fapp0 Cat_cat')
                    .replace('@id Cat_cart Cat_cart', '@id Cat_cat Cat_cart'))
    total_family += '''
// The same total-fibre object formation through ordinary fixed
// postcomposition. Its parameter profile remains distinct from Cart.
// lhs-audit: keep 1,2,3 -- named coefficient duality at its ordinary Hom owner.
rule @hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) _ _ _ total_op_cart
      (@CoAbove2_func $K Cat_cart $E)
  ↪ @TotalOp_catd $K $E;
'''
    insert('// Fibrewise dimension-one transpose changes the base by CoAt2.',
           total_family, 'Adapt the qualified total-fibre duality to the selected Cartesian coefficient')

    replace_once('''//     ↪ Op_cat(Σ (p : Hom_K(x,y)^op), homd_(id_E,x,u,y,v)[p]).
rule Hom_cat (@Sigma_cat $K $E) (Struct_sigma $x $u) (Struct_sigma $y $v)
  ↪ Op_cat
      (@Sigma_cat
        (Op_cat (Hom_cat $K $x $y))
        (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v));''', '''//     ↪ O(Σ (p : O(Hom_K(x,y))), O_fib(homd_(id_E,x,u,y,v))[p]).
// Total fibre duality followed by the outer total dual restores fibre directions.
rule Hom_cat (@Sigma_cat $K $E) (Struct_sigma $x $u) (Struct_sigma $y $v)
  ↪ TotalOp_cat
      (@Sigma_cat
        (TotalOp_cat (Hom_cat $K $x $y))
        (@TotalOp_catd (Op_cat (Hom_cat $K $x $y))
          (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v)));''',
                 'Sigma Hom', 'Use the qualified total-dual negative Sigma while retaining the original total and Homd leaf owners')
    a = body.index('// Keep the first Hom owner; refine its recursive next action.')
    b = body.index('// Capped next projection joins the whole route on a visible Sigma cell.', a)
    old_projection = body[a:b]
    old_body = '''      (@Op_func
      (@Sigma_cat (Op_cat (Hom_cat $K $x $y))
        (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v))
      (Op_cat (Hom_cat $K $x $y))
      (@Sigma_proj1_func (Op_cat (Hom_cat $K $x $y))
        (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v)))'''
    assert old_projection.count(old_body) == 1
    new_body = '''      (@TotalOp_func
      (@Sigma_cat (TotalOp_cat (Hom_cat $K $x $y))
        (@TotalOp_catd (Op_cat (Hom_cat $K $x $y))
          (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v)))
      (TotalOp_cat (Hom_cat $K $x $y))
      (@Sigma_proj1_func (TotalOp_cat (Hom_cat $K $x $y))
        (@TotalOp_catd (Op_cat (Hom_cat $K $x $y))
          (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v))))'''
    replace_once(old_projection, old_projection.replace(old_body, new_body),
                 'Sigma recursive first projection', 'Retain the first-Hom owner and refine its next action through the corrected negative total')
    start = body.index('symbol sigma_proj1_hom_fapp1_fapp0\n')
    end = body.index(';', start) + 1
    old_projection = body[start:end]
    replace_once(old_projection, old_projection.split('≔', 1)[0] + '≔ sigma_Fst theta;',
                 'Sigma second-cell projection facade', 'Infer the actual corrected nested Sigma carrier instead of spelling the former reversed fibre')

    a = body.index('// Stable head for the computationally important projection pullback.')
    b = body.index('// 9c. Families over Sigma totals and displayed-transfor uncurrying', a)
    old_sigma_families = body[a:b]
    new_sigma_families = re.sub(r'(\$?K\s+)Cat_cat', r'\1Cat_cart', old_sigma_families)
    new_sigma_families = new_sigma_families.replace(
        'Cat_cat\n      (@Sigma_proj1_pullback_catd',
        'Cat_cart\n      (@Sigma_proj1_pullback_catd')
    new_sigma_families = new_sigma_families.replace(
        '(@Sigma_cat $K $R)\n      Cat_cat',
        '(@Sigma_cat $K $R)\n      Cat_cart')
    new_sigma_families = new_sigma_families.replace(
        '(@Sigma_cat $K $R)\n        Cat_cat',
        '(@Sigma_cat $K $R)\n        Cat_cart')
    # The original total constructor consumes the ordinary diagram category;
    # the canonical Cartesian Hom enters it through its existing whole view.
    start = new_sigma_families.index('// Whole represented-Sigma base change accumulates')
    new_sigma_families = (new_sigma_families[:start]
        + re.sub(r'@hom_int\b', '@hom_int_view', new_sigma_families[start:]))
    replace_once(old_sigma_families, new_sigma_families, 'Sigma family observations and base change',
                 'Change only the admitted family coefficient and the existing whole Hom inclusion at the original total-map consumers')

    a = body.index('// 9c. Families over Sigma totals and displayed-transfor uncurrying')
    b = body.index('// 10. Mixed-variance family functor', a)
    old_sigma_uncurry = body[a:b]
    replace_once(old_sigma_uncurry, old_sigma_uncurry.replace('Cat_cat', 'Cat_cart'),
                 'families over Sigma totals',
                 'An admitted family over a total has the selected Cartesian coefficient in both its displayed input and its output')

    start = body.index('symbol Functor_comp_pair_func ')
    end = body.index(';', start) + 1
    old_pair_composition = body[start:end]
    replace_once(old_pair_composition,
                 old_pair_composition.replace('Functor_cat', 'Functor_cart_cat')
                     .replace('@comp_prod_func Cat_cat', '@comp_prod_func Cat_cart'),
                 'Cartesian pair composition',
                 'The original joint composition consumer now uses genuine Cartesian mapping inputs, while fixed ordinary whiskering remains lax')

    a = body.index('// 10. Mixed-variance family functor')
    b = body.index('// Mixed-variance hom family for two sections of a displayed family.', a)
    old_mixed = body[a:b]
    new_mixed = old_mixed.replace('Cat_cat', 'Cat_cart')
    new_mixed = new_mixed.replace('// Internalized constructor package for mixed-variance functor families.',
        '// Internalized mixed-family constructor. The negative parameter uses\n'
        '// Cartesian diagram maps; the positive parameter still admits lax FF.')
    new_mixed = (new_mixed.replace('@id Cat_cart Cat_cart', '@id Cat_cat Cat_cart')
                 .replace('Product_cat_cart_func', 'Product_cat_coeff_func'))
    fixed_end = new_mixed.index('// Coherent evaluation for a constant-domain displayed functor family.')
    new_mixed = (new_mixed[:fixed_end].replace('Functor_cat (', 'Functor_cart_cat (')
                  .replace('(Functor_cat\n', '(Functor_cart_cat\n') + new_mixed[fixed_end:])
    for variable in ('K', '$K'):
        old = f'(Op_cat (Catd_cat (Op_cat {variable})))'
        new = f'(Op_cat (Functor_cart_cat (Op_cat {variable}) Cat_cart))'
        assert new_mixed.count(old) == 1, variable
        new_mixed = new_mixed.replace(old, new)
    new_mixed = new_mixed.replace(
        "(@tapp0_fapp0 (Op_cat $K) Cat_cart $A' $A $k $L);",
        "(@tapp0_fapp0 (Op_cat $K) Cat_cart $A' $A $k\n"
        "        (@strict_transfor (Op_cat $K) Cat_cart $A' $A $L));")
    products_start = new_mixed.index('// Pointwise distribution of a pair of mixed functors into a product target.')
    new_mixed = (new_mixed[:products_start]
        + new_mixed[products_start:].replace('Functor_cat (', 'Functor_cart_cat (')
            .replace('(Functor_cat\n', '(Functor_cart_cat\n')
            .replace('@comp_cat_con_func', '@comp_cat_con_cart_func'))
    replace_once(old_mixed, new_mixed, 'mixed Functor_catd and its parameter action',
                 'Use Hom(Cat_cart) fibres; retain lax positive parameter maps and require the actual Cartesian negative parameter profile')

    a = body.index('// Mixed-variance hom family for two sections of a displayed family.')
    b = body.index('// 11. Representables and presheaf-family classifiers', a)
    old_mixed_hom = body[a:b]
    new_mixed_hom = old_mixed_hom.replace('Cat_cat', 'Cat_cart').replace('Op_catd', 'TotalOp_catd')
    new_mixed_hom = new_mixed_hom.replace('// Mixed-variance hom family for two sections of a displayed family.',
        '// Mixed-variance hom family. The negative section is over R(K), in\n'
        '// the total fibre dual O(E); the positive section is over K in E.')
    new_mixed_hom = new_mixed_hom.replace('@piapp0 $K (@TotalOp_catd',
                                         '@piapp0 (CoAbove2_cat $K) (@TotalOp_catd')
    new_mixed_hom = new_mixed_hom.replace('(@Op_func $K (Op_cat Cat_cart) $X)',
        '(@TotalOp_func (CoAbove2_cat $K) (TotalOp_cat Cat_cart) $X)')
    assert new_mixed_hom.count('  ↪ Transf_cat\n') == 1
    new_mixed_hom = new_mixed_hom.replace('  ↪ Transf_cat\n',
        '  ↪ Hom_cat\n      (Functor_cart_cat (Fibre_cat $A $k) (Fibre_cat $B $k))\n')
    replace_once(old_mixed_hom, new_mixed_hom, 'Hom_catd and Transf_catd negative sections',
                 'Retain the existing mixed section architecture with total fibre duality and the correct shifted negative-section base')

    a = body.index('// Constant-family section evaluation follows ordinary functor application.')
    b = body.index(';', a) + 1
    constant_section = body[a:b]
    replace_once(constant_section,
                 '// Constant-section evaluation is owned earlier with Pi and section evaluation.',
                 'constant-section evaluation relocation',
                 'The original computation is needed by constant negative sections before the Homd ladder')
    constant_section = constant_section.replace('      Cat_cat\n', '      Cat_cart\n')
    insert('// 8d. Fibre covariance and dependent-hom endpoint notation',
           constant_section, 'Keep the existing constant-section computation with its section owner')
    relocated.append({'owner': 'constant-section component', 'bodySha256': sha(constant_section)})

    replace_once('''symbol Rep_catd_func [Z : Cat]
  : τ (Functor (Op_cat Z) (Catd_cat Z))
≔ @hom_int Z Z (@id Cat_cat Z);''', '''symbol Rep_catd_func [Z : Cat]
  : τ (Functor (Op_cat Z) (Catd_cat Z))
≔ @hom_int_view Z Z (@id Cat_cat Z);''',
                 'Rep_catd_func', 'Retain the existing lax diagram view of the canonical Cartesian representable root')
    replace_once('''≔ @hom_int_precomp_func Z Z (@id Cat_cat Z) y x p;''',
                 '''≔ @strict_transfor Z Cat_cart (@Rep_catd Z y) (@Rep_catd Z x)
    (@hom_int_precomp_func Z Z (@id Cat_cat Z) y x p);''',
                 'Rep_transport_func', 'Use the existing inclusion to observe canonical strict precomposition as a lax displayed map')

    replace_once('rule CoAt2_cat (CoAt2_cat $A) ↪ $A;',
                 'rule CoAt2_cat (CoAt2_cat $A) ↪ $A;\n'
                 'rule Op_cat (CoAt2_cat $A) ↪ CoAt2_cat (Op_cat $A);',
                 'transpose / dimension-two commutation',
                 'The existing shifted Edge/presheaf construction consumes this category-level duality comparison')
    a = body.index('symbol Edge_catd_func [Z : Cat]')
    b = body.index(';', a) + 1
    replace_once(body[a:b], '''symbol Edge_catd_func [Z : Cat]
  : τ (Functor (CoAt2_cat (Op_cat Z))
      (Functor_cart_cat (CoAt2_cat Z) Cat_cart))
≔ @comp_cat_fapp0 (CoAt2_cat (Op_cat Z))
    (CoAt2_cat (Functor_cart_cat Z Cat_cart))
    (Functor_cart_cat (CoAt2_cat Z) Cat_cart)
    (@Op_catd_func Z)
    (@CoAt2_func (Op_cat Z) (Functor_cart_cat Z Cat_cart)
      (@hom_int Z Z (@id_func Z)));''',
                 'Edge_catd_func', 'The actual fibre transpose shifts the base and the whole represented parameter; no same-base coercion')
    a = body.index('symbol Presheaf_catd_func (K : Cat)')
    b = body.index(';', a) + 1
    replace_once(body[a:b], '''symbol Presheaf_catd_func (K : Cat)
  : τ (Functor (Op_cat (Functor_cart_cat (Op_cat K) Cat_cart)) (Catd_cat K))
≔ comp_cat_fapp0
    (@fapp0_func (Catd_cat K) (Catd_cat K) (@Const_catd K Cat_cart))
    (@Functor_catd_func K);''',
                 'Presheaf_catd_func', 'Use the actual Cartesian negative parameter of the existing mixed-family constructor')
    a = body.index('symbol HomPresheaf_catd_func [Z : Cat]')
    b = body.index(';', a) + 1
    replace_once(body[a:b], '''symbol HomPresheaf_catd_func [Z : Cat]
  : τ (Functor (CoAt2_cat Z) (Catd_cat (Op_cat (CoAt2_cat Z))))
≔ comp_cat_fapp0
    (@Presheaf_catd_func (Op_cat (CoAt2_cat Z)))
    (@Op_func (CoAt2_cat (Op_cat Z)) (Functor_cart_cat (CoAt2_cat Z) Cat_cart)
      (@Edge_catd_func Z));''',
                 'HomPresheaf_catd_func', 'Preserve the compositional presheaf construction at its actual shifted variance; Homd will use its Q-valued whole section')

    a = body.index('// 12. Directed homd target and internal homd functor')
    b = body.index('// 14. Section action over dependent homs', a)
    old_homd_core = body[a:b]
    replacement = ('// 12. Directed homd target and internal homd functor\n\n'
        + fragment('production_homd_index.lpfragment')
        + '\n' + fragment('production_homd_core.lpfragment')
        + '\n\n// 13. Dependent-hom projections and covariant fibre transport\n'
          '// The original names above now project the identity core and the\n'
          '// defined general-FF composition; no second primitive Homd theory.\n\n')
    replace_once(old_homd_core, replacement, 'native Q Homd and direct projection ladder',
                 'Replace the invalid ordinary-Pi target by the selected Q-valued transformation; reuse native Hom and original fibre-covariance owners')
    relocated.append({'symbols': ['FibCov_target_catd', 'FibCov_source_catd', 'fib_cov_int',
                                  'fib_cov_src_func', 'fib_cov_transf', 'homd_src_func',
                                  'homd_src_sec', 'homd_tgt_func'],
                      'originalBlockSha256': sha(old_homd_core),
                      'reason': 'Canonical covariance is required before the Q section and its root'})
    for name in ('homd_id_src_sec', 'homd_id_tgt_func'):
        matches = list(re.finditer(r'(?m)^symbol ' + name + r'\b[\s\S]*?;', body))
        assert len(matches) == 2, (name, len(matches))
        original_declaration = matches[-1][0]
        replace_once(original_declaration, '// ' + name + ' is now owned by the native identity Homd core.',
                     name + ' relocation', 'Reuse the original identity projection name in the corrected core')
        relocated.append({'symbol': name, 'originalDeclarationSha256': sha(original_declaration)})
    old_section = '(Pi_cat (Homd_target_section_catd E x))'
    occurrences = body.count(old_section)
    assert occurrences == 2, occurrences
    body = body.replace(old_section, '(@Homd_target_section_cat K E x)')
    changes.append({'owner': 'relative intrinsic section classifier views', 'count': occurrences,
                    'reason': 'The actual Q-valued section category replaces the defective former Pi target'})

    a = body.index('// 15. Internal displayed hom-action heads')
    b = body.index('// 16. Displayed components, displayed hom-action, and laxity extraction', a)
    old_intrinsic = body[a:b]
    new_intrinsic, count = re.subn(
        r'\((Transfd(?:_cat)?)\s+\(homd_int \(@id_funcd K E\)\)\s+'
        r'\(comp_catd_fapp0\s+\(homd_int (GG|FF)\)\s+\(Op_funcd FF\)\)\)',
        lambda m: '(' + m[1] + '\n        (comp_catd_fapp0 (homd_int ' + m[2] + ') FF)'
            + '\n        (homd_int (@id_funcd K E)))', old_intrinsic)
    assert count == 4, count
    new_intrinsic = new_intrinsic.replace('(homd_int (@id_funcd K E))',
        '(@strict_transfor K Cat_cart E (fapp0 (Homd_target_index_func K) (@Homd_coeff_diagram K E)) (@homd_id_int K E))')
    new_intrinsic = new_intrinsic.replace('(@Transf_cat $K Cat_cat $E $D)',
                                          '(@Transf_cat $K Cat_cart $E $D)')
    comment_a = new_intrinsic.index('/*')
    comment_b = new_intrinsic.index('*/', comment_a) + 2
    new_intrinsic = new_intrinsic[:comment_a] + '/*\n  The corrected root target is transposed. Accordingly the intrinsic arrow\n  runs from homd_int(GG) o FF to homd_int(id_E), without transposing raw FF.\n  Its source-u component reverses again in T(S_E(x)), exposing the forward\n  dependent-Hom action. The weaker inner P index retains its directed cells.\n\n  Original ownership is preserved:\n    internal hom-action -> extracted laxity -> Sigma action consumes laxity.\n  No separate comparison argument is introduced, and Sigma is not used to\n  define the intrinsic action which its maps later consume.\n*/' + new_intrinsic[comment_b:]
    replace_once(old_intrinsic, new_intrinsic, 'corrected intrinsic Homd direction',
                 'Retarget the existing internal-action owners; retain lax FF and derive their projections through the directed Q index')

    # Constant transformations are canonically Cartesian. Strengthen these
    # existing owners, rather than introduce a parallel constant-map calculus.
    a = body.index('symbol Const_transf_func [K A : Cat]')
    b = body.index('/*\n  Pure Cat/Catd convenience helpers.', a)
    old_constants = body[a:b]
    new_constants = old_constants.replace(
        '(@Transf_cat K A (@Const_func K A x) (@Const_func K A y))',
        '(Hom_cat (Functor_cart_cat K A) (@Const_func K A x) (@Const_func K A y))')
    new_constants = new_constants.replace(
        ': τ (Transf (@Const_func K A x) (@Const_func K A y));',
        ': τ (@StrictTransfor K A (@Const_func K A x) (@Const_func K A y));')
    new_constants = new_constants.replace(
        '$k (@Const_transf $K $A $x $y $p)',
        '$k (@strict_transfor _ _ _ _ (@Const_transf $K $A $x $y $p))')
    new_constants = new_constants.replace(
        "$k $k' (@Const_transf $K $A $x $y $p)",
        "$k $k' (@strict_transfor _ _ _ _ (@Const_transf $K $A $x $y $p))")
    replace_once(old_constants, new_constants, 'canonical constant transformation profile',
                 'The original constant-map owners have Cartesian naturality; ordinary observations use the existing inclusion')

    a = body.index('// 16a. Fibre-level displayed components')
    b = body.index('// 16b. Identity-specialized displayed hom action and Sigma-map action', a)
    old_components = body[a:b]
    new_components = old_components.replace('Cat_cat', 'Cat_cart').replace('Functor_cat', 'Functor_cart_cat')
    # Generic composition of functors still belongs to the public Cat owner.
    new_components = new_components.replace('@comp_fapp0 Cat_cart', '@comp_fapp0 Cat_cat')
    new_components = new_components.replace('@comp_cat_con_func', '@comp_cat_con_cart_func')
    new_components = new_components.replace('@comp_cat_cov_func', '@comp_cat_cov_cart_func')
    new_components = new_components.replace(
        '(Transf_cat (Fibre_func FF z) (Fibre_func GG z))',
        '(Hom_cat (Functor_cart_cat (Fibre_cat E z) (Fibre_cat D z)) (Fibre_func FF z) (Fibre_func GG z))')
    begin = new_components.index('symbol tdapp0_fapp0')
    end = new_components.index(';', begin) + 1
    old_component_type = new_components[begin:end]
    new_components = new_components[:begin] + old_component_type.replace(
        ': τ (Transf (Fibre_func FF z) (Fibre_func GG z));',
        ': τ (@StrictTransfor (Fibre_cat E z) (Fibre_cat D z) (Fibre_func FF z) (Fibre_func GG z));') + new_components[end:]
    # The two horizontal component Homs have the actual Cartesian profile.
    new_components = re.sub(
        r'\(@Transf_cat\s+(\(Fibre_cat \$[A-Z] \$k\))\s+(\(Fibre_cat \$[A-Z] \$k\))',
        r'(Hom_cat (Functor_cart_cat \1 \2)', new_components)
    # Evaluation accepts the ordinary view of these classified components.
    new_components = re.sub(
        r'(\$r|\$u)\s+\(@tdapp0_fapp0 ([^;]*?)\)\)',
        r'\1\n        (@strict_transfor _ _ _ _ (@tdapp0_fapp0 \2)))',new_components)
    c = new_components.index('// Object-component projection for generic Sigma-total uncurrying.')
    d = new_components.index('// Point component of the totalized displayed transfor', c)
    observed = new_components[c:d]
    assert observed.count('(@tdapp0_fapp0') == 1
    observed = observed.replace('(@tdapp0_fapp0', '(@strict_transfor _ _ _ _ (@tdapp0_fapp0').replace('$eta);', '$eta));')
    new_components = new_components[:c] + observed + new_components[d:]
    new_components = new_components.replace(
        '≔ @tdapp0_fapp0 K E D FF GG z ϵ;',
        '≔ @strict_transfor _ _ _ _ (@tdapp0_fapp0 K E D FF GG z ϵ);')
    new_components = new_components.replace(
        '≔ tapp0_fapp0 Terminal_obj (tdapp0_fapp0 k eta);',
        '≔ tapp0_fapp0 Terminal_obj (strict_transfor (tdapp0_fapp0 k eta));')
    # Retire the false unconditional left/middle equation. The conventional
    # pre/right leg, not the post/left comparison, is strict.
    c = new_components.index('/*\n  Ambient lax source-action reading:')
    d = new_components.index('// First-class whole path', c)
    new_components = new_components[:c] + '// Conventional pre/right action: the selected middle is FF[y] o E[p].\n// The left/post route retains its directed comparison.\nunif_rule @tapp1_func $K Cat_cart $E $D $x $y $FF\n  ≡ @comp_fapp0 Cat_cat _ _ _\n      (@hom_postcomp_func Cat_cart Cat_cart (@id Cat_cat Cat_cart) _ _ _\n        (@tapp0_fapp0 $K Cat_cart $E $D $y $FF))\n      (@fapp1_func $K Cat_cart $E $x $y)\n  ↪ [ tt ≡ tt ];\n\n' + new_components[d:]
    new_components = new_components.replace('functord_transport_lhs_tele_agrees', 'functord_transport_rhs_tele_agrees')
    new_components = new_components.replace('functord_transport_lhs_agrees', 'functord_transport_rhs_agrees')
    for name in ('functord_transport_rhs_tele_agrees', 'functord_transport_rhs_agrees'):
        c = new_components.index('symbol ' + name)
        d = new_components.index(';', c) + 1
        new_components = new_components[:c] + new_components[c:d].replace(
            'functord_transport_lhs_', 'functord_transport_rhs_') + new_components[d:]
    new_components = new_components.replace('Full left strict-naturality route', 'Full left/post transport route')
    new_components = new_components.replace('Full right strict-naturality route', 'Full selected pre/right transport route')
    new_components = new_components.replace(
        '// The former generic target/right equality and derived strict-naturality path\n// are retired. Ambient code consumes `functord_laxity_transf`; strict code uses\n// the evidence-bearing paths in `emdash3_2_gray_profiles.lp`.',
        '// Only the pre/right route is the strict middle action. The post/left\n// route retains the comparison extracted by functord_laxity_transf; no\n// equality between the two routes is imposed for arbitrary FF.')
    new_components = new_components.replace('First-class whole path for the ambient left/source presentation.',
                                            'First-class whole path for the selected pre/right presentation.')
    new_components = new_components.replace('Evaluate the whole ambient left/source path at p.',
                                            'Evaluate the selected pre/right path at p.')
    new_components += '''
// The displayed specialization erases tapp0_hom_fapp0 before the existing
// canonical covariance cut can fire. Keep the same projection normal form.
rule @tdapp0_fapp0 $K _ $E _ _ $y
      (@fapp1_fapp0 _ _
        (@fapp1_func _ _ (Functor_cart_include $K Cat_cart) _ $E)
        _ _ (@fapp1_fapp0 _ _ (@fib_cov_src_func $K $E $x) $u $v $h))
  ↪ @fib_cov_tapp0_u_map $K $E $x $y $u $v $h;

'''
    replace_once(old_components, new_components, 'displayed component and transport profiles',
                 'Use actual Cartesian fibre Homs, retaining lax base action; replace the false left/middle comparison by the selected right/middle comparison')

    a = body.index('// 16b. Identity-specialized displayed hom action and Sigma-map action')
    b = body.index('// 16c. Section action and displayed laxity cells', a)
    replace_once(body[a:b], fragment('production_intrinsic_projection.lpfragment') + '\n',
                 'intrinsic identity projection ladder',
                 'Retain the existing projection names through the actual Q section, Cartesian fibre Hom and directed index; total Hom uses the derived negative Sigma')

    a = body.index('symbol piapp1_func [K : Cat]')
    b = body.index(';', a) + 1
    replace_once(body[a:b], 'symbol piapp1_func [K : Cat] (E : τ (Catd K))\n  (s : τ (Obj (Pi_cat E))) (x y : τ (Obj K))\n  : τ (Obj (@Pi_cat (TotalOp_cat (Hom_cat K x y))\n      (@TotalOp_catd (Op_cat (Hom_cat K x y))\n        (@homd_ K E E (@id_funcd K E)\n          x (@piapp0 K E s x) y (@piapp0 K E s y)))))\n≔ @fapp1_fapp0 (CoAbove2_cat (Homd_index_cat (Hom_cat K x y)))\n    (Catd_cat (TotalOp_cat (Hom_cat K x y)))\n    (Homd_index_total_family_func (Hom_cat K x y))\n    (fapp0 (@homd_id_tgt_func K (@Const_catd K Terminal_cat) x Terminal_obj y) Terminal_obj)\n    (fapp0 (@homd_ff_tgt_func K (@Const_catd K Terminal_cat) E s x Terminal_obj y) Terminal_obj)\n    (@fdapp1_int_presheaf_arrow K (@Const_catd K Terminal_cat) E s\n      x Terminal_obj y Terminal_obj);',
                 'negative-index section action',
                 'Use the existing positive Pi over the actual total-dual index family; derive the section from the existing intrinsic P-arrow')

    a = body.index('// Totalizing the native Hom section retains the entire next action.')
    b = body.index('// Raw canonical-triangle cell extracted from the internal displayed hom-action.', a)
    replace_once(body[a:b], '// Totalizing the native Hom section retains its negative index presentation.\nrule @fapp1_func _ _ (@section_total_func $K $E $s) $x $y\n  ↪ @TotalOp_func\n      (TotalOp_cat (Hom_cat $K $x $y))\n      (@Sigma_cat (TotalOp_cat (Hom_cat $K $x $y))\n        (@TotalOp_catd (Op_cat (Hom_cat $K $x $y))\n          (@homd_ $K $E $E (@id_funcd $K $E)\n            $x (@piapp0 $K $E $s $x) $y (@piapp0 $K $E $s $y))))\n      (@section_total_func (TotalOp_cat (Hom_cat $K $x $y))\n        (@TotalOp_catd (Op_cat (Hom_cat $K $x $y))\n          (@homd_ $K $E $E (@id_funcd $K $E)\n            $x (@piapp0 $K $E $s $x) $y (@piapp0 $K $E $s $y)))\n        (@piapp1_func $K $E $s $x $y));\n\n', 'negative section totalization',
                 'The existing recursive totalization uses total reversal, matching the corrected Sigma Hom and Pi index')

    a = body.index('// 16c. Section action and displayed laxity cells')
    b = body.index('// 16d. Arbitrary displayed-transfor hom-action projections', a)
    old_section_action = body[a:b]
    new_section_action = old_section_action.replace('@fapp0 $K.[] Cat_cat $E.[]', '@fapp0 $K.[] Cat_cart $E.[]')
    new_section_action = new_section_action.replace('@tapp0_fapp0 _ Cat_cat _ _ $k', '@tapp0_fapp0 _ Cat_cart _ _ $k')
    new_section_action = new_section_action.replace('$K Cat_cat\n      (@Const_catd $K Terminal_cat)',
                                                    '$K Cat_cart\n      (@Const_catd $K Terminal_cat)')
    replace_once(old_section_action, new_section_action, 'section and Sigma family coefficient observations',
                 'Change only the admitted-family coefficient tags in existing section/base-change projections')

    a = body.index('// 16d. Arbitrary displayed-transfor hom-action projections')
    b = body.index('// 16e. Strict/cartesian and terminal-source specializations', a)
    replace_once(body[a:b], fragment('production_intrinsic_modification.lpfragment') + '\n\n',
                 'general displayed-transfor intrinsic projections',
                 'Use the same Q section, Cartesian fibre Hom and directed inner index as the identity specialization; retain epsilon and all original projection names')

    a = body.index('// 16e. Strict/cartesian and terminal-source specializations')
    b = body.index('// 17. Generic Sigma/Pi weakening, ordinary structural logic, and delayed projection helpers', a)
    old_specializations = body[a:b]
    represented = '(@hom_int_precomp_func $Z $Z (@id Cat_cat $Z) $y $x $p)'
    assert old_specializations.count(represented) == 2
    replace_once(old_specializations, old_specializations.replace(represented,
        '(@strict_transfor _ _ _ _ ' + represented + ')'),
        'canonical represented displayed specialization',
        'Use the ordinary displayed view of the existing Cartesian Hom source action; do not pass the classified strict transfor as a raw FF')

    constant_coherence = fragment('production_index_constant_coherence.lpfragment')
    marker2 = '// Part 2: constant coefficient formation, at Const_catd.'
    marker3 = '// Part 3: coefficient duality inverse, after TotalOp_catd.'
    postwhiskering, constant_tail = constant_coherence.split(marker2)
    constant_views, coefficient_inverse = constant_tail.split(marker3)
    insert('// 6c. Constant/opposite transfors and Cat-valued composition projections',
           postwhiskering, 'Fixed postwhiskering composition and unit, with both other legs identity; no unrestricted lax-square interchange')
    insert('// A represented family along a constant diagram is pointwise Hom(w,u).',
           constant_views, 'Whole constant-family/strict-functor duality views needed by the actual constant-index constructor')
    insert('// Fibrewise dimension-one transpose changes the base by CoAt2.',
           coefficient_inverse, 'Cartesian coefficient double duality, including its already-formed family head')

    insert('// Consumed object action of canonical total base change, preserving the whole tapp1 heads.',
           fragment('production_constant_section_index.lpfragment'),
           'Whole constant-family intrinsic action uses the ordinary strict functor Hom action through the actual constant-index constructor')
    a = body.index('// Proof-time comparison only: terminal-source displayed laxity agrees with')
    b = body.index('// Transparent theorem exposing the terminal-source proof-time comparison.', a)
    replace_once(body[a:b], '''// Constant-family section action now computes through the whole index
// constructor above. The former point-only proof-time rule is redundant.

''', 'constant section point comparison',
                 'The retained theorem follows the whole constant-index computation instead of an independent point agreement')

    body = body.replace(
        '// Transparent theorem exposing the terminal-source proof-time comparison.\n// Its reflexive body exercises the unification rule; this is not runtime beta.',
        '// Retained theorem for the terminal-source comparison. Its reflexive\n// body now follows the whole constant-index computation.')
    body = body.replace(
        '// Constant-section arrow action agrees propositionally with ordinary functor\n// action. The section projection computes to `fdapp1_int_cell`; the preceding\n// proof-time comparison supplies the final ordinary view.',
        '// The existing theorem records the constant section arrow computation.\n// The whole index specialization and its lower projections now retain the\n// ordinary functor action directly.')

    a = body.index('// 17a. Generic Sigma/Pi introduction and evaluation')
    b = body.index('// 17b. Constant sections and delayed product-pair telescope rules', a)
    replace_once(body[a:b], fragment('production_evaluation.lpfragment') + '\n\n',
                 'Sigma introduction and section-first Pi evaluation',
                 'Retain all lax sections through the actual Pi-to-Functord identity view; do not impose the invalid k-first Cartesian evaluation comparison')
    body = body.replace('    pi_eval_transf(E)                 : const(ΠE) ⊢ E\n'
                        '    pi_eval_transf(E)[k]              = piapp0_func(E,k) : ΠE ⊢ E[k]',
                        '    pi_eval_transf(E)                 : ΠE ⊢ (const(1) ⊢ E)\n'
                        '    pi_eval_transf(E)[s][k](*)        = s[k]')

    insert('// A canonical represented mate of a Cartesian whole map has a lax y-square.',
           fragment('production_q_reindex.lpfragment'),
           'Qualify whole right-represented composition by actual Cartesian source reindexing; retain the weaker inner index maps')

    a = body.index('// Stable weakening owner for ordinary functor categories.')
    b = body.index('// Direct displayed weakening for a mixed functor source slot.', a)
    old_weakening = body[a:b]
    new_weakening = old_weakening.replace('Functor_cat', 'Functor_cart_cat')
    replace_once(old_weakening,
                 '// The canonical Const_func_func owner is declared in 17b,\n'
                 '// before its product-pair telescope consumer.\n\n',
                 'constant functor owner relocation',
                 'The existing constant transformation is Cartesian; retain one owner and make it available at the first actual product consumer')
    insert('// Pairing telescope for products.\n//\n', new_weakening,
           'Canonical constant functors have Cartesian parameter action; ordinary lax sections remain separate')
    a = body.index('// Pairing telescope for products.\n//\n')
    b = body.index('// 17c. Ordinary functor structural logic', a)
    old_pairing = body[a:b]
    new_pairing = old_pairing.replace('@const_section_func $B $A', '@Const_func_func $B $A')
    new_pairing = new_pairing.replace('Functor_cat', 'Functor_cart_cat')
    new_pairing = new_pairing.replace('(@Transf_cat $B $B (@id_func $B) (@id_func $B))',
                                    '(Hom_cat (Functor_cart_cat $B $B) (@id_func $B) (@id_func $B))')
    replace_once(old_pairing, new_pairing, 'Cartesian product-pair telescope projections',
                 'Use the actual Cartesian constant-functor and constant-transfor owners instead of the larger lax Pi classifier')

    a = body.index('// 17c. Ordinary functor structural logic')
    b = body.index('// 17d. Generic ordinary functor hom-action', a)
    replace_once(body[a:b], fragment('production_ordinary_structural.lpfragment') + '\n\n\n',
                 'Cartesian ordinary structural logic and displayed weakening',
                 'Preserve the original exchange/diagonal ladders with the mapping profiles required by their interchange laws; default Transf and Functord remain lax')
    a = body.index('// 17d. Generic ordinary functor hom-action')
    b = body.index('// 17e. Section pullback and internal Pi action', a)
    replace_once(body[a:b], fragment('production_pullback_structural.lpfragment') + '\n\n\n',
                 'Pullback action and recursive negative-total base change',
                 'Keep the original first-Hom owner and next-Hom rules, with total-dual index/fibres and actual Cartesian structural consumers')
    insert('// The same total-fibre object formation through ordinary fixed',
           fragment('production_total_op_pullback.lpfragment'),
           'Commute total fibre duality with reindexing along the actual R-dual base functor, for recursive Sigma base change')
    a = body.index('// 17e. Section pullback and internal Pi action')
    b = body.index('// 18. Cat-valued profunctors', a)
    replace_once(body[a:b], fragment('production_section_pullback.lpfragment') + '\n\n'
                 + fragment('production_cartesian_intrinsic.lpfragment') + '\n\n',
                 'Section pullback and classified intrinsic action',
                 'Retain general lax section/evaluation computations; replace invalid raw same-base Op mirrors by actual Cartesian intrinsic observations on the corrected profile')
    insert('// The primitive Unit_prof projection keeps the Hom action rigid at runtime.',
           fragment('production_cartesian_hom_action.lpfragment'),
           'The actual Cartesian displayed evaluator consumes the rigid Hom action at an object, with the same shared strict-functor interpretation')
    insert('/*\n  Contravariant represented-family reindexing is runtime accumulation:',
           fragment('production_cartesian_reindex_view.lpfragment'),
           'Internal Pi consumes the existing represented precomposition and admitted pullback as the same whole family')
    insert('// Identity specialization after the strict component has already projected.',
           fragment('production_cartesian_naturality.lpfragment'),
           'Reuse the existing default pre/right and actual strict-view post/left consumed-object computations at Cat_cart')
    a = body.index('injective symbol Eval_funcd [K A : Cat]')
    b = body.index(';', a) + 1
    old_eval_map = body[a:b]
    replace_once(old_eval_map,
                 old_eval_map.replace(': τ (Functord\n', ': τ (Hom (Functor_cart_cat K Cat_cart)\n'),
                 'Canonical displayed evaluation profile',
                 'The existing Cartesian evaluator is strictly natural for admitted families; retain one constructor and its ordinary inclusion view')
    replace_once('rule @tapp0_fapp0 _ Cat_cart _ _ $k (@Eval_funcd _ $A $B)',
                 'rule @tapp0_fapp0 _ Cat_cart _ _ $k\n'
                 '      (@strict_transfor _ _ _ _ (@Eval_funcd _ $A $B))',
                 'Ordinary component of classified displayed evaluation',
                 'The same fibre Eval_func is observed through the actual Cartesian mapping inclusion')
    insert('// Target-internalized mirror of hom_int.',
           fragment('production_hom_source_composition.lpfragment'),
           'The target-map composition consumer needs strict Hom source action after its generic first-Hom projection has become a named transformation')
    insert('// 6c. Constant/opposite transfors and Cat-valued composition projections',
           fragment('production_fixed_postcomposition.lpfragment') + '\n'
           + fragment('production_fixed_precomposition.lpfragment'),
           'Fixed pre/postcomposition preserve vertical composition with the other legs identity; these are the consumed Homd target-map and corrected arrow-diagram projection joins')
    insert('// 6c. Constant/opposite transfors and Cat-valued composition projections',
           fragment('production_hom_next_action.lpfragment'),
           'The actual intrinsic-composite consumer requires the next Hom of two-sided whiskering and its existing component observations')
    insert('// 5d. Rigid two-endpoint Hom action',
           fragment('production_composition_identity_pair.lpfragment'),
           'The literal identity pair restores normality after displayed composition has projected to its first-Hom owner')
    insert('// 6c. Constant/opposite transfors and Cat-valued composition projections',
           fragment('production_displayed_unit_coherence.lpfragment'),
           'Whole intrinsic units require identity and associativity comparisons across the existing displayed/ordinary diagram facades; preserve actual operands and runtime Hom heads')
    insert('// 14. Section action over dependent homs',
           fragment('production_intrinsic_composite_views.lpfragment'),
           'Actual Homd target contravariance and associativity supply the whole whiskering endpoints without operational equality arguments')
    insert('// 16. Displayed components, displayed hom-action, and laxity extraction',
           fragment('production_intrinsic_composite.lpfragment'),
           'Compute the existing intrinsic action of a displayed composite by the checked whole modification, preserving both lax inputs')
    insert('// 18. Cat-valued profunctors',
           fragment('production_intrinsic_composite_projection.lpfragment'),
           'Join root-first and component-first observations of the same intrinsic composite; retain the actual first extracted cell inside the second intrinsic action')
    insert('// 18. Cat-valued profunctors',
           fragment('production_intrinsic_unit_projection.lpfragment'),
           'Join the intrinsic whole identity with the same existing section, y and index identity projections')

    # Canonical object-of-Hom result types avoid premature decomposition of
    # the injective Hom alias at the actual Cat_cart/total-opposite consumers.
    # These are definitionally the same types, not new component operations.
    for marker in ('symbol tapp0_fapp0 :', 'symbol fdapp1_int_cell ['):
        a = body.index(marker)
        b = body.index(';', a)
        old = body[a:b]
        start = old.rfind('τ (Hom')
        assert start >= 0, marker
        new = old[:start] + old[start:].replace('τ (Hom', 'τ (Obj (Hom_cat', 1) + ')'
        replace_once(old, new, marker,
                     'Expose the existing Obj(Hom_cat) result for coefficient inclusion and negative-section arrow typing; no type or computation is added')

    a = body.index('// 18b. Opposite profunctors and fixed-endpoint duality')
    b = body.index('// 18d. Unit hom profunctor and readable representables', a)
    old = body[a:b]
    replace_once(old, old.replace('Cat_cat', 'Cat_cart').replace('Functor_cat', 'Functor_cart_cat'),
                 'Opposite profunctor and reindexing base action',
                 'Keep product-swap and product-map owners with the admitted family coefficient and its actual first Hom')
    a = body.index('// 18d. Unit hom profunctor and readable representables')
    b = body.index('/*\n  Stable generic action of a displayed hom-family.', a)
    old = body[a:b]
    replace_once(old, old.replace('Cat_cat', 'Cat_cart'), 'Unit profunctor projections',
                 'The existing rigid Hom action lands in the admitted Cartesian coefficient')
    a = body.index('/*\n  Stable generic action of a displayed hom-family.')
    b = body.index('// Binary representable hom profunctor as endpoint reindexing of Unit_prof.', a)
    replace_once(body[a:b], fragment('production_hom_catd_action.lpfragment') + '\n',
                 'Existing Hom_catd action and semantic point comparison',
                 'Use the R-base total-dual negative section; retain both actual section cells and the transported positive source under the conventional-lax direction')
    a = body.index("// Proof-time comparison of curry's semantic telescope with the native Hom family.")
    b = body.index('// Right-representable hom profunctor,', a)
    old = body[a:b]
    replace_once(old, old.replace('(@id Cat_cat Cat_cat)', '(@id Cat_cat Cat_cart)')
                 .replace('$B _ Cat_cat $R', '$B _ Cat_cart $R'),
                 'Represented profunctor curry comparisons',
                 'Retain both actual endpoint functors and compare against the corrected Cartesian Hom package')
    a = body.index('// Component of the existing whole reindexed map:')
    b = body.index(';', a) + 1
    old = body[a:b]
    replace_once(old, old.replace('Cat_cat', 'Cat_cart'), 'Reindexed profunctor-map component',
                 'General lax ProfMap components remain ordinary strict fibre functors at the admitted coefficient')
    a = body.index('// Component of a functor-induced shaped unit is the ordinary hom-action.')
    b = body.index('// 18h. Tensor, shaped introduction, and fixed-endpoint co-Yoneda maps', a)
    old = body[a:b]
    replace_once(old, old.replace('Cat_cat', 'Cat_cart').replace('@hom_int ', '@hom_int_view '),
                 'Functor-induced shaped unit action',
                 'Use the existing ordinary view of Cartesian Hom in the retained internal-action projection')
    a = body.index('// Ordinary whole hom action of a recursor on the generating cross functor.')
    b = body.index('// 18z. Late cross-section normalization bridges', a)
    old = body[a:b]
    replace_once(old, old.replace(') Cat_cat', ') Cat_cart'), 'Join cross component computations',
                 'Keep the original whole/point cross rules; canonical tapp0 result typing supplies the coefficient boundary without extra LHS guards')
    old = '''      $A
      $B
      Cat_cat
      (@Pullback_catd $B $C $E $F)'''
    replace_once(old, old.replace('Cat_cat', 'Cat_cart'), 'Late family pullback accumulation',
                 'Only the family codomain changes; ambient functor composition remains Cat_cat')

    insert('// Object action of a Sigma map:', fragment('production_sigma_coefficient.lpfragment')
           + '\n' + fragment('production_sigma_parameter_profile.lpfragment'),
           'The actual comma family needs the Cartesian restriction of existing totalization, with the same total categories and strict-map action')
    insert('// Fibrewise dimension-one transpose changes the base by CoAt2.',
           fragment('production_total_op_parameter.lpfragment'),
           'Expose total-dual strict family-map components at the existing whole TotalOp_catd_func owner')
    insert('// Whole represented-Sigma base change accumulates before a retained outer',
           fragment('production_sigma_basechange_coefficient.lpfragment'),
           'Canonical Cartesian parameter view of original total base change, with unchanged components and actual ordinary restriction')
    insert('// Whole represented-Sigma base change accumulates before a retained outer',
           fragment('production_sigma_constant_projection.lpfragment'),
           'Canonical second-projection owner and measured projection-order joins for constant-target Sigma maps; preserve the original whole and first-Hom views and the conventional pre/right base-change action')
    sigma_composition = '''// Stable Sigma-map / represented-composition proof-time join.
unif_rule @sigma_map_func $K _ _
    (@hom_postcomp_fapp0 (@Catd_cat $K) (@Catd_cat $K)
      (@id Cat_cat (@Catd_cat $K)) $E $M $D $GG $FF)
  ≡ @comp_fapp0 Cat_cat (@Sigma_cat $K $E) (@Sigma_cat $K $M) (@Sigma_cat $K $D)
      (@sigma_map_func $K $M $D $GG) (@sigma_map_func $K $E $M $FF)
  ↪ [ tt ≡ tt ];'''
    replace_once(sigma_composition, sigma_composition.replace(
        '// Stable Sigma-map / represented-composition proof-time join.',
        '// Stable Sigma-map / represented-composition proof-time join.\n'
        '// Composite endpoint tags are inferred from the actual Sigma maps;\n'
        '// they can carry proof-time-equal total-dual family presentations.').replace(
        '≡ @comp_fapp0 Cat_cat (@Sigma_cat $K $E) (@Sigma_cat $K $M) (@Sigma_cat $K $D)',
        '≡ @comp_fapp0 Cat_cat _ _ _'),
        'Sigma represented-composition comparison',
        'Remove measured inferred endpoint discrimination while preserving the actual base, all three families and both displayed maps')
    insert('rule @fapp0 _ _ (@section_total_func $K $E $s) $k',
           fragment('production_total_dual_projection_views.lpfragment'),
           'Total-dual instances of the existing Sigma projection comparisons, retaining section/map/base-change heads and all data')
    insert('// Direct proof-time reading of represented-family reindexing.',
           fragment('production_pullback_composite_view.lpfragment'),
           'Direct existing reindexing/associativity comparison at the whole family, preserving actual bases and maps under total duality')
    a = body.index('// 18zz. Whole comma projection and displayed laxity extraction')
    b = body.index('// 19. Applications:', a)
    replace_once(body[a:b], fragment('production_comma_projection.lpfragment') + '\n',
                 'Original comma identity sections and whole laxity projection',
                 'Use negative totals, the actual E-to-transposed-target Homd roots, and the existing Q/P projection ladder; keep arbitrary eta and general lax FF')
    insert('// The public whole laxity candidate is now an object projection, not an\n',
           fragment('intrinsic_rule.lpfragment'),
           'Strict default: retain the existing extracted functor-compositor rule at its migrated comma owner')
    insert('// Whole post/left ordinary laxity.', fragment('conventional_lax_intrinsic.lpfragment'),
           'Retain the conventional pre/right extracted identity at the same migrated owner; post/left laxity remains directed')
    old = 'rule @tapp0_fapp0 $A $B $F $H $Y (@comp_fapp0 (Functor_cat $A $B) $F $G $H $η $ϵ)'
    replace_once(old, old.replace('$A $B $F $H $Y', '_ _ _ _ $Y', 1),
                 'Ordinary composite component inference slots',
                 'Recover endpoints from the actual composite; repeated inferred presentations prevented the arbitrary Homd-action projection')
    old = '''rule @tapp0_fapp0
      $K Cat_cart $E $C $x
      (@comp_fapp0 (@Catd_cat $K) $E $D $C $FF $GG)'''
    replace_once(old, old.replace('$K Cat_cart $E $C $x', '_ _ _ _ $x', 1),
                 'Displayed composite component inference slots',
                 'The displayed constructor supplies the same endpoints; preserve component composition across equivalent target presentations')
    insert('injective symbol Catd_cat (K : Cat) : Cat;',
           fragment('production_cartesian_path_identity.lpfragment') + '\n',
           'The original J/structured-transport comparison needs the existing literal path-reflexivity identity view at Cat_cart')
    insert('// 5d. Rigid two-endpoint Hom action',
           fragment('production_identity_whiskering.lpfragment'),
           'The original EH unit consumers require identity whiskering after the composition Hom action has projected; guard both identity dimensions by their actual category')
    a = body.index('// 19. Applications:')
    b = body.index('// 19g. Eckmann-Hilton first computation slice', a)
    replace_once(body[a:b], fragment('production_pathout.lpfragment') + '\n',
                 'Original moving PathOut, path-induction and nested telescope interfaces',
                 'Use Cartesian PathOut formation, the actual motive pullback, restricted moving components of the retained lax fixed-source theorem, and total-dual negative sections')
    # Preserve the complete original tail. A separately emitted prefix
    # qualifies only its preceding source; full-core qualification requires
    # the complete target and its actual consumers.
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
    section_boundary = '// 8d. Fibre covariance and dependent-hom endpoint notation'
    assert body.count(section_boundary) == 1
    (package / 'sections_prefix.lp').write_text(body[:body.index(section_boundary)]
        + '\n' + fragment('production_foundations_controls.lpfragment')
        + '\n' + fragment('production_sections_controls.lpfragment'))
    sigma_boundary = '// 10. Mixed-variance family functor'
    assert body.count(sigma_boundary) == 1
    sigma_controls = fragment('sigma_total_op_controls.lpfragment').replace(
        '(Op_cat (Hom_cat K x y)) Cat_cat', '(Op_cat (Hom_cat K x y)) Cat_cart')
    (package / 'sigma_prefix.lp').write_text(body[:body.index(sigma_boundary)]
        + '\n' + fragment('production_foundations_controls.lpfragment')
        + '\n' + fragment('production_sections_controls.lpfragment')
        + '\n' + sigma_controls)
    mixed_boundary = '// 11. Representables and presheaf-family classifiers'
    assert body.count(mixed_boundary) == 1
    mixed_controls = fragment('mixed_family_controls.lpfragment').replace('Cat_cat', 'Cat_cart')
    mixed_controls = mixed_controls.replace('(@Eval_funcd K A B)',
        '(@strict_transfor _ _ _ _ (@Eval_funcd K A B))')
    mixed_parameters = fragment('mixed_family_parameter_controls.lpfragment')
    mixed_parameters = mixed_parameters.split('// Dependency-complete recovery candidate for ambient fixed precomposition.', 1)[0]
    mixed_parameters = (mixed_parameters.replace('Cat_cat', 'Cat_cart')
                        .replace('@id Cat_cart Cat_cart', '@id Cat_cat Cat_cart'))
    negative_sections = fragment('total_op_hom_family_controls.lpfragment').replace('Cat_cat', 'Cat_cart')
    (package / 'mixed_prefix.lp').write_text(body[:body.index(mixed_boundary)]
        + '\n' + fragment('production_foundations_controls.lpfragment')
        + '\n' + fragment('production_sections_controls.lpfragment')
        + '\n' + sigma_controls + '\n' + mixed_controls
        + '\n' + mixed_parameters + '\n' + negative_sections)
    homd_boundary = '// 14. Section action over dependent homs'
    assert body.count(homd_boundary) == 1
    homd_controls = (fragment('production_foundations_controls.lpfragment')
        + '\n' + fragment('production_sections_controls.lpfragment')
        + '\n' + sigma_controls + '\n' + mixed_controls
        + '\n' + mixed_parameters + '\n' + negative_sections
        + '\n' + fragment('production_homd_controls.lpfragment')
        + '\n' + fragment('production_q_reindex_controls.lpfragment'))
    (package / 'homd_prefix.lp').write_text(body[:body.index(homd_boundary)]
        + '\n' + homd_controls)
    index_boundary = '// 15. Internal displayed hom-action heads'
    assert body.count(index_boundary) == 1
    index_controls = fragment('production_homd_index_controls.lpfragment')
    (package / 'index_profile.lp').write_text(body[:body.index(index_boundary)]
        + '\n' + index_controls)
    intrinsic_boundary = '// 16c. Section action and displayed laxity cells'
    assert body.count(intrinsic_boundary) == 1
    (package / 'intrinsic_identity_prefix.lp').write_text(body[:body.index(intrinsic_boundary)]
        + '\n' + homd_controls + '\n' + index_controls
        + '\n' + fragment('production_intrinsic_controls.lpfragment'))
    section_boundary = '// 17. Generic Sigma/Pi weakening, ordinary structural logic, and delayed projection helpers'
    assert body.count(section_boundary) == 1
    (package / 'section_action_prefix.lp').write_text(body[:body.index(section_boundary)]
        + '\n' + homd_controls + '\n' + index_controls
        + '\n' + fragment('production_intrinsic_controls.lpfragment')
        + '\n' + fragment('production_section_action_controls.lpfragment'))
    evaluation_boundary = '// 17b. Constant sections and delayed product-pair telescope rules'
    assert body.count(evaluation_boundary) == 1
    (package / 'evaluation_prefix.lp').write_text(body[:body.index(evaluation_boundary)]
        + '\n' + homd_controls + '\n' + index_controls
        + '\n' + fragment('production_intrinsic_controls.lpfragment')
        + '\n' + fragment('production_section_action_controls.lpfragment')
        + '\n' + fragment('production_evaluation_controls.lpfragment'))
    structural_boundary = '// 17c. Ordinary functor structural logic'
    assert body.count(structural_boundary) == 1
    (package / 'structural_prefix.lp').write_text(body[:body.index(structural_boundary)]
        + '\n' + homd_controls + '\n' + index_controls
        + '\n' + fragment('production_intrinsic_controls.lpfragment')
        + '\n' + fragment('production_section_action_controls.lpfragment')
        + '\n' + fragment('production_evaluation_controls.lpfragment')
        + '\n' + fragment('production_constant_map_controls.lpfragment'))
    ordinary_boundary = '// 17d. Generic ordinary functor hom-action'
    assert body.count(ordinary_boundary) == 1
    (package / 'ordinary_structural_prefix.lp').write_text(body[:body.index(ordinary_boundary)]
        + '\n' + homd_controls + '\n' + index_controls
        + '\n' + fragment('production_intrinsic_controls.lpfragment')
        + '\n' + fragment('production_section_action_controls.lpfragment')
        + '\n' + fragment('production_evaluation_controls.lpfragment')
        + '\n' + fragment('production_constant_map_controls.lpfragment')
        + '\n' + fragment('production_ordinary_structural_controls.lpfragment'))
    pullback_boundary = '// 17e. Section pullback and internal Pi action'
    assert body.count(pullback_boundary) == 1
    (package / 'pullback_structural_prefix.lp').write_text(body[:body.index(pullback_boundary)]
        + '\n' + homd_controls + '\n' + index_controls
        + '\n' + fragment('production_intrinsic_controls.lpfragment')
        + '\n' + fragment('production_section_action_controls.lpfragment')
        + '\n' + fragment('production_evaluation_controls.lpfragment')
        + '\n' + fragment('production_constant_map_controls.lpfragment')
        + '\n' + fragment('production_ordinary_structural_controls.lpfragment')
        + '\n' + fragment('production_pullback_structural_controls.lpfragment'))
    section_pullback_boundary = '// 18. Cat-valued profunctors'
    assert body.count(section_pullback_boundary) == 1
    (package / 'section_pullback_prefix.lp').write_text(body[:body.index(section_pullback_boundary)]
        + '\n' + homd_controls + '\n' + index_controls
        + '\n' + fragment('production_intrinsic_controls.lpfragment')
        + '\n' + fragment('production_section_action_controls.lpfragment')
        + '\n' + fragment('production_evaluation_controls.lpfragment')
        + '\n' + fragment('production_constant_map_controls.lpfragment')
        + '\n' + fragment('production_ordinary_structural_controls.lpfragment')
        + '\n' + fragment('production_pullback_structural_controls.lpfragment')
        + '\n' + fragment('production_section_pullback_controls.lpfragment'))
    (package / 'intrinsic_composite_prefix.lp').write_text(
        (package / 'section_pullback_prefix.lp').read_text()
        + '\n' + fragment('production_intrinsic_composite_controls.lpfragment'))
    (package / 'intrinsic_unit_prefix.lp').write_text(
        (package / 'intrinsic_composite_prefix.lp').read_text()
        + '\n' + fragment('production_intrinsic_unit_controls.lpfragment'))
    profunctor_boundary = '// 18zz. Whole comma projection and displayed laxity extraction'
    assert body.count(profunctor_boundary) == 1
    inherited_controls = (package / 'intrinsic_unit_prefix.lp').read_text()[
        len(body[:body.index(section_pullback_boundary)]):]
    (package / 'profunctor_prefix.lp').write_text(body[:body.index(profunctor_boundary)]
        + inherited_controls + '\n' + fragment('production_profunctor_controls.lpfragment'))
    comma_boundary = '// 19. Applications:'
    assert body.count(comma_boundary) == 1
    comma_inherited = (package / 'profunctor_prefix.lp').read_text()[len(body[:body.index(profunctor_boundary)]):]
    (package / 'comma_prefix.lp').write_text(body[:body.index(comma_boundary)]
        + comma_inherited + '\n' + fragment('production_comma_controls.lpfragment'))
    pathout_inherited = (package / 'comma_prefix.lp').read_text()[len(body[:body.index(comma_boundary)]):]
    (package / 'pathout_controls.lp').write_text(body + '\n' + pathout_inherited
        + '\n' + fragment('production_pathout_controls.lpfragment'))
    (package / 'rule_hygiene_full_controls.lp').write_text(
        (package / 'pathout_controls.lp').read_text() + '\n'
        + fragment('production_adjunction_guard_controls.lpfragment'))
    (package / 'inverse_core_controls.lp').write_text(
        (package / 'rule_hygiene_full_controls.lp').read_text() + '\n'
        + fragment('production_inverse_cut_controls.lpfragment'))
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
            comma_profiles = {
                'emdash3_2_zero_arrow_cones.lp': (2, 6, 1, 1),
                'emdash3_2_zero_arrow_cone_maps.lp': (0, 10, 1, 3),
                'examples/zero_arrow_cone_maps.lp': (0, 21, 2, 6),
            }
            if path in comma_profiles:
                old = text
                counts = tuple(text.count(s) for s in ('(@Catd_cat B)',
                    'Functor_cat WalkingArrow_cat C', 'Functor WalkingArrow_cat C',
                    '@Transf WalkingArrow_cat C'))
                assert counts == comma_profiles[path], (path, counts)
                # The original whole two-sided total consumes this Cartesian
                # Hom family; keep its actual profile instead of forgetting it.
                text = text.replace('(@Catd_cat B)', '(Functor_cart_cat B Cat_cart)')
                text = text.replace('Functor_cat WalkingArrow_cat C', 'Functor_oplax_cat WalkingArrow_cat C')
                text = text.replace('Functor WalkingArrow_cat C', 'Obj (Functor_oplax_cat WalkingArrow_cat C)')
                text = text.replace('@Transf WalkingArrow_cat C', '@Hom (Functor_oplax_cat WalkingArrow_cat C)')
                text = text.replace('@diagram_family_at_func', '@diagram_oplax_family_at_func')
                text = text.replace('@diagram_family_transf', '@diagram_oplax_family_transf')
                if path == 'emdash3_2_zero_arrow_cones.lp':
                    text = text.replace('// Hom_B(F[-],-), with the first coordinate contravariant as required by homdc.',
                        '// Hom_B(F[-],-), retaining the Cartesian inner family required by\n'
                        '// the corrected two-sided total. No ordinary-family coercion is needed.')
                    marker = '// The zero-cone\'s datum is an actual transformation J(A)⇒d of arrow diagrams.'
                    assert text.count(marker) == 1
                    text = text.replace(marker, fragment('production_represented_comma_map.lpfragment') + '\n' + marker, 1)
                if path == 'emdash3_2_zero_arrow_cone_maps.lp':
                    map_body = '≔ Struct_sigma u (Struct_sigma v alpha);'
                    assert text.count(map_body) == 1
                    text = text.replace(map_body, '≔ @represented_comma_map C (Functor_oplax_cat WalkingArrow_cat C)\n'
                        '    (@terminal_arrow_diagram_func C t T) a0 a1 d0 d1 h0 h1 u v alpha;', 1)
                changes.append({'source': path, 'owner': 'represented comma and zero-cone total/maps',
                                'reason': 'Keep the canonical Cartesian Hom family consumed by the existing two-sided total, and use the actual oplax arrow coefficient of the terminal embedding; preserve the original nested-Sigma and map bodies',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_adjunction_mates.lp':
                old = text
                dependency = 'require open emdash.emdash3_2_defiso_evaluation_points;'
                assert text.count(dependency) == 1
                text = text.replace(dependency,
                    'require open emdash.emdash3_2_strict_functor_actions;\n' + dependency, 1)
                old_unif = 'unif_rule @Prof_cat $A $B ≡ @Functor_cat $Base Cat_cat'
                assert text.count(old_unif) == 1
                text = text.replace(old_unif, old_unif.replace('Cat_cat', 'Cat_cart'), 1)
                component = '''≔ @defiso_at (Product_cat (Op_cat R) L) Cat_cat
    (@Hom_prof_along R L L F (@id_func L))
    (@Hom_prof_along R L R (@id_func R) G)
    (@Adjunction_hom_prof_comparison R L F G J)
    (@Product_pair (Op_cat R) L X Y);'''
                assert text.count(component) == 1
                text = text.replace(component, '''≔ @defiso_fmap Cat_cart Cat_cat Cat_cart_include
    (Hom_cat L (@fapp0 R L F X) Y) (Hom_cat R X (@fapp0 L R G Y))
    (@defiso_at (Product_cat (Op_cat R) L) Cat_cart
      (@Hom_prof_along R L L F (@id_func L))
      (@Hom_prof_along R L R (@id_func R) G)
      (@Adjunction_hom_prof_comparison R L F G J)
      (@Product_pair (Op_cat R) L X Y));''', 1)
                observation = 'symbol adjunction_transpose_semantic_path'
                assert text.count(observation) == 1
                text = text.replace(observation, fragment('production_cartesian_defiso_component.lpfragment') + '\n' + observation, 1)
                changes.append({'source': path, 'owner': 'adjunction_hom_component_iso',
                                'reason': 'Evaluate the original Hom comparison in its actual Cat_cart coefficient, then apply the existing whole Cat_cart inclusion to retain the public Cat_cat inverse package and its chosen maps',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('emdash3_2_prof_defiso_evaluation_paths.lp',
                        'examples/action_profile_prof_defiso_controls.lp'):
                old = text
                expected = 104 if path.startswith('emdash3_2_') else 38
                assert text.count('Cat_cat') == expected, (path, text.count('Cat_cat'))
                text = text.replace('Cat_cat', 'Cat_cart')
                if path.startswith('emdash3_2_'):
                    text = text.replace('The stable owner is unchanged; these are proof-time category views only.',
                        'The actual profunctor coefficient is Cat_cart. The stable owner and\n'
                        '   the original selected inverse data are unchanged; these remain proof-time views.')
                changes.append({'source': path, 'owner': 'profunctor selected inverse evaluation',
                                'reason': 'Evaluate the original forward and inverse maps in the actual Cat_cart coefficient, preserving every selected comparison and original observation',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_defiso_evaluation_points.lp':
                marker = 'symbol defiso_at_to_path '
                assert text.count(marker) == 1
                addition = fragment('production_cartesian_defiso_point_cuts.lpfragment')
                text = text.replace(marker, addition + '\n' + marker, 1)
                changes.append({'source': path, 'owner': 'evaluated inverse point cancellation',
                                'reason': 'Instance the existing two functor-valued point cuts at Cat_cart, retaining the actual chosen inverse package and evaluation point',
                                'insertedSha256': sha(addition)})
            if path == 'emdash3_2_discrete_functor_paths.lp':
                anchor = '// Core reflection, set-valued pointwise assembly, then the original core law.'
                assert text.count(anchor) == 1
                addition = fragment('production_discrete_functord_closure.lpfragment')
                text = text.replace(anchor, addition + '\n' + anchor, 1)
                changes.append({'source': path, 'owner': 'discrete displayed mapping category',
                                'reason': 'Structural fibrewise-discrete closure required for the original ordinary-target Hom-action admission; no global strictness or new caller data',
                                'insertedSha256': sha(addition)})
            if path == 'emdash3_2_presheaves.lp':
                old = text
                yoneda = '≔ @hom_con_int K K (@id_func K);'
                assert text.count(yoneda) == 1
                text = text.replace(yoneda, '≔ @hom_con_int_view K K (@id_func K);', 1)
                arrow_family = '''symbol arrow_into_catd (K : Cat) : τ (Catd K)
≔ @comp_cat_fapp0
    K
    (@Catd_cat (Op_cat K))
    Cat_cat
    (@Sigma_func (Op_cat K))
    (@yoneda_psh_func K);'''
                assert text.count(arrow_family) == 1
                text = text.replace(arrow_family, '''symbol arrow_into_catd (K : Cat) : τ (Catd K)
≔ @comp_cat_fapp0 K (Functor_cart_cat (Op_cat K) Cat_cart) Cat_cart
    (@Sigma_coeff_func (Op_cat K)) (@hom_con_int K K (@id_func K));''', 1)
                pullback_coefficient = '(Op_cat K)\n    Cat_cat\n    (@HigherSieveClassifier K)'
                assert text.count(pullback_coefficient) == 1
                text = text.replace(pullback_coefficient, pullback_coefficient.replace('Cat_cat', 'Cat_cart'), 1)
                postcompose_coefficient = '@fapp1_fapp0 K Cat_cat (@arrow_into_catd K)'
                assert text.count(postcompose_coefficient) == 1
                text = text.replace(postcompose_coefficient, postcompose_coefficient.replace('Cat_cat', 'Cat_cart'), 1)
                old_comment = '''  The comparison with `Psh_cat(Slice_cat(U))` goes through the stable shared
  presentation `Catd_cat(Into_restr_cat(U))`; no direct conversion rule is
  installed merely to make unification transitive.'''
                assert text.count(old_comment) == 1
                text = text.replace(old_comment, '''  The varying-base classifier uses Cartesian diagram maps. Its objects
  are the same Cat-valued families as Psh_cat(Slice_cat(U)), while their
  mapping profiles differ. No category equality with the ordinary lax-map
  presheaf category is asserted.''', 1)
                inclusion_anchor = 'symbol HigherSieve\n'
                assert text.count(inclusion_anchor) == 1
                text = text.replace(inclusion_anchor, '''// Whole ordinary view through the existing fixed-base family facade.
// The target annotation supplies the established one-step Psh comparison.
symbol higher_sieve_include_func [K : Cat] (U : τ (Obj K))
  : τ (Functor (@HigherSieve_cat K U) (@Catd_cat (@Into_restr_cat K U)))
≔ Functor_cart_include (@Into_restr_cat K U) Cat_cart;

''' + inclusion_anchor, 1)
                changes.append({'source': path, 'owner': 'presheaf Yoneda and canonical Sigma family',
                                'reason': 'Use the ordinary Hom inclusion for the unchanged raw presheaf category, and the canonical Cartesian Hom/Sigma coefficient for the whole arrow family; retain the existing slice presentation pending its actual controls',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_sieves.lp':
                old = text
                family_action = '@fapp1_fapp0 K Cat_cat (@arrow_into_catd K)'
                assert text.count(family_action) == 1
                text = text.replace(family_action,
                    '@fapp1_fapp0 K Cat_cart (@arrow_into_catd K)', 1)
                changes.append({'source': path, 'owner': 'ordinary sieve pullback evidence',
                                'reason': 'Use the actual coefficient of the canonical arrow family; retain pointwise subterminal evidence and the original pullback body',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_one_cat_hom_comparison_data.lp':
                old = text
                assert text.count('Cat_cat') == 82
                assert text.count('@hom_int ') == 12
                assert text.count('@Product_pair_tele_func') == 43
                # Preserve the two generic ordinary-functor inverse helpers.
                # The live profunctor paths below use their own coefficient
                # evaluations; these helpers do not consume those packages.
                ordinary_start = text.index('protected symbol hom_comparison_defiso_point_left')
                ordinary_end = text.index('// Evaluate the supplied whole DefIso', ordinary_start)
                ordinary_helpers = text[ordinary_start:ordinary_end]
                assert ordinary_helpers.count('Cat_cat') == 14
                text = (text[:ordinary_start].replace('Cat_cat', 'Cat_cart')
                        + ordinary_helpers
                        + text[ordinary_end:].replace('Cat_cat', 'Cat_cart'))
                text = text.replace('@hom_int ', '@hom_int_view ')
                text = text.replace('@Product_pair_tele_func', '@hom_comparison_pair_tele_func')
                anchor = '// Reconstruct F⇒G from its whole internal Hom action using the shared graph.'
                assert text.count(anchor) == 1
                addition = fragment('production_one_cat_hom_action_admission.lpfragment')
                text = text.replace(anchor, addition + '\n' + anchor, 1)
                view_anchor = '// Curry the supplied whole represented map at its original hom_int owners.'
                assert text.count(view_anchor) == 1
                text = text.replace(view_anchor,
                    fragment('production_lax_curry_hom_views.lpfragment') + '\n' + view_anchor, 1)
                start = text.index('symbol one_cat_transf_from_hom_action')
                end = text.index('// The original forward comparison', start)
                original = text[start:end]
                replacement = original.replace('@hom_int ', '@hom_int_view ')
                signature, definition = replacement.split('≔', 1)
                definition = re.sub(r'\balpha\b', '(@one_cat_hom_action_cart B C C1 F G alpha)', definition)
                text = text[:start] + signature + '≔' + definition + text[end:]
                start = text.index('symbol profmap_internal_hom_action')
                end = text.index('// η:id_A⇒GF', start)
                original_curry = text[start:end]
                replacement_curry = original_curry.replace('@hom_int ', '@hom_int_view ')
                replacement_curry = replacement_curry.replace('Cat_cat', 'Cat_cart')
                replacement_curry = replacement_curry.replace('@curry_func_func', '@curry_lax_func_func')
                text = text[:start] + replacement_curry + text[end:]
                pair_path, component_path = fragment('production_hom_comparison_curry_paths.lpfragment').split('// COMPONENT PATH\n', 1)
                start = text.index('protected symbol hom_comparison_pair_tele_identity_path')
                end = text.index('// Stage transfor identity evaluation', start)
                text = text[:start] + pair_path + '\n' + text[end:]
                start = text.index('protected symbol hom_comparison_prof_hom_action_component_path')
                end = text.index('symbol one_cat_hom_comparison_unit_component_path', start)
                text = text[:start] + component_path + '\n' + fragment('production_hom_comparison_admitted_path.lpfragment') + '\n' + text[end:]
                for owner, next_owner, idx, cod, ordinary, ff, gg, rr in (
                    ('symbol one_cat_hom_comparison_unit_component_path', 'symbol one_cat_hom_comparison_counit_component_path',
                     'A', 'A', 'A1', '(@id_func A)', '(@comp_cat_fapp0 A B A G F)', '(@hom_comparison_unit_profmap A B F G i)'),
                    ('symbol one_cat_hom_comparison_counit_component_path', 'protected symbol hom_comparison_prof_cov_cell',
                     'B', 'B', 'B1', '(@comp_cat_fapp0 B A B F G)', '(@id_func B)', '(@hom_comparison_counit_profmap A B F G i)'),
                    ('protected symbol hom_comparison_reconstruction_component_path', 'symbol one_cat_profmap_reconstruction_action_path',
                     'A', 'C', 'C1', 'F', 'G', 'r')):
                    start = text.index(owner)
                    end = text.index(next_owner, start)
                    signature, definition = text[start:end].split('≔', 1)
                    action = f'(@profmap_internal_hom_action {idx} {cod} {ff} {gg} {rr})'
                    assert definition.count(action) == 1, owner
                    admitted = f'''(@strict_transfor (Op_cat {idx}) (Catd_cat {idx})
        (one_cat_hom_action_source {idx}) (@one_cat_hom_action_target {idx} {cod} {ff} {gg})
        (@one_cat_hom_action_cart {idx} {cod} {ordinary} {ff} {gg} {action}))'''
                    definition = definition.replace(action, admitted, 1)
                    assert definition.count('@hom_comparison_prof_hom_action_component_path') == 1, owner
                    definition = definition.replace('@hom_comparison_prof_hom_action_component_path',
                        '@hom_comparison_admitted_hom_action_component_path', 1)
                    text = text[:start] + signature + '≔' + definition + text[end:]
                changes.append({'source': path, 'owner': 'ordinary-target supplied Hom-action reconstruction',
                                'reason': 'Retag 68 coefficient uses, retaining the two generic ordinary inverse helpers; adapt 12 ordinary Hom views and 43 pair-telescope views, derive admission from original OneCat(C), and use one-way lax curry with the shared graph and actual selected maps',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_one_cat_modifications.lp':
                old = text
                specialization = '(@one_cat_modification _ Cat_cat _ _ _ _ _ $m)'
                assert text.count(specialization) == 1
                text = text.replace(specialization,
                    '(@one_cat_modification _ Cat_cart _ _ _ _ _ $m)', 1)
                changes.append({'source': path, 'owner': 'ordinary modification displayed component',
                                'reason': 'Retag the existing displayed specialization at its actual Cat_cart coefficient; preserve the general modification, original OneCat premise and supplied components',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/one_cat_hom_comparison_data.lp':
                old = text
                assert text.count('Cat_cat') == 4
                text = text.replace('Cat_cat', 'Cat_cart')
                changes.append({'source': path, 'owner': 'original Hom-comparison reviewer',
                                'reason': 'Retag the four original profunctor component observations with their actual coefficient; preserve all selected comparisons and inverse controls',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            adjunction_intro_coefficients = {
                'emdash3_2_one_cat_adjunction_introduction.lp': 20,
                'examples/one_cat_adjunction_introduction.lp': 6,
            }
            if path in adjunction_intro_coefficients:
                old = text
                expected = adjunction_intro_coefficients[path]
                pattern = r'(\(Product_cat \(Op_cat A\) [AB]\)\s+)Cat_cat'
                assert text.count('Cat_cat') == expected, path
                assert len(re.findall(pattern, text)) == expected, path
                text = re.sub(pattern, r'\1Cat_cart', text)
                if path == 'emdash3_2_one_cat_adjunction_introduction.lp':
                    base = '(Product_cat (Op_cat A) B)'
                    left = '(@Hom_prof_along A B B F (@id_func B))'
                    right = '(@Hom_prof_along A B A (@id_func A) G)'
                    adj = '(@one_cat_adjunction_from_hom_comparison A B A1 B1 F G i)'
                    comparison = f'(@Adjunction_hom_prof_comparison A B F G {adj})'
                    point = '(@Product_pair (Op_cat A) B x y)'
                    evaluated = f'(@defiso_at {base} Cat_cart {left} {right} {comparison} {point})'
                    for direction, projection in [('transpose', 'to'), ('untranspose', 'from')]:
                        marker = f'symbol one_cat_adjunction_from_hom_comparison_{direction}_path'
                        assert text.count(marker) == 1
                        start = text.index(marker)
                        end = text.index(';', start) + 1
                        signature, definition = text[start:end].split('≔', 1)
                        mate = f'(@adjunction_{direction}_func A B F G {adj} x y)'
                        assert definition.count(mate) == 1
                        raw = f'(@defiso_at_{projection} {base} Cat_cart {left} {right} {comparison} {point})'
                        original_proof = definition[:-1].strip().replace(mate, raw, 1)
                        included_view = f'''@defiso_fmap_{projection}_path Cat_cart Cat_cat Cat_cart_include
      (Hom_cat B (@fapp0 A B F x) y) (Hom_cat A x (@fapp0 B A G y))
      {evaluated}'''
                        definition = f'''≔ @eq_trans _ _ _ _
    ({included_view})
    ({original_proof});'''
                        text = text[:start] + signature + definition + text[end:]
                changes.append({'source': path, 'owner': 'ordinary Hom-comparison adjunction introduction',
                                'reason': 'Retag the original coefficient positions and observe the actual Cat_cart_include mapped inverse before the existing input agreement; preserve the constructor, seven scoped comparisons, whole unit/counit agreement and reviewer controls',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_one_cat_arrow_diagrams.lp':
                old = text
                dep = 'require open emdash.emdash3_2_arrow_diagram_families;'
                assert text.count(dep) == 1
                text = text.replace(dep, dep + '\nrequire open emdash.emdash3_2_one_cat_transfor_profiles;', 1)
                identity = 'rule @tapp1_fapp0 (Op_cat $K) _ _ _'
                assert text.count(identity) == 1
                text = text.replace(identity, 'rule @tapp1_fapp0 (CoAbove2_cat (Op_cat $K)) _ _ _', 1)
                text = text.replace('after its opposite identity normalizes.', 'after its total-dual identity normalizes.')
                original_body = '''≔ @transf_arrow_diagram_func (@LaxArrow_cat C) C
    (@cubical_src_func C) (@cubical_tgt_func C)
    (@one_cat_arrow_universal_transf C C1);'''
                assert text.count(original_body) == 1
                replacement = '''// OneCat(C) supplies the existing strict-transfor admission. Cartesian
// exchange then constructs the same ordinary diagram interface, through its
// actual inclusion; the default ambient transformations remain lax.
≔ @comp_cat_fapp0 (@LaxArrow_cat C) (Functor_cart_cat WalkingArrow_cat C)
    (Functor_cat WalkingArrow_cat C) (Functor_cart_include WalkingArrow_cat C)
    (@sym_func WalkingArrow_cat (@LaxArrow_cat C) C
      (@walking_arrow_func (Functor_cart_cat (@LaxArrow_cat C) C)
        (@cubical_src_func C) (@cubical_tgt_func C)
        (@one_cat_strict_transfor (@LaxArrow_cat C) C C1
          (@cubical_src_func C) (@cubical_tgt_func C)
          (@one_cat_arrow_universal_transf C C1))));'''
                text = text.replace(original_body, replacement, 1)
                anchor = 'symbol one_cat_arrow_diagram_func\n'
                assert text.count(anchor) == 1
                text = text.replace(anchor, fragment('production_cartesian_arrow_point.lpfragment') + '\n' + anchor, 1)
                changes.append({'source': path, 'owner': 'ordinary-target arrow diagrams',
                                'reason': 'Correct the total-dual identity guard and reuse existing OneCat strict-transfor admission with Cartesian exchange; preserve the public ordinary diagram target and original square data',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/one_cat_arrow_diagrams.lp':
                old = text
                assert text.count('@hom_int ') == 2
                text = text.replace('@hom_int ', '@hom_int_view ')
                changes.append({'source': path, 'owner': 'ordinary arrow reviewer coefficient',
                                'reason': 'Pass the existing ordinary Hom-family view to the local square-fibre interface; preserve all original observations',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/adjunction_mates.lp':
                old = text
                carrier = '@Transf (Product_cat (Op_cat R) L) Cat_cat'
                assert text.count(carrier) == 1
                text = text.replace(carrier, carrier.replace('Cat_cat', 'Cat_cart'), 1)
                changes.append({'source': path, 'owner': 'adjunction mate negative control',
                                'reason': 'Keep the constant-source rejection well typed in the actual displayed-family coefficient Cat_cart',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('emdash3_2_one_cat_adjunction_families.lp',
                        'examples/one_cat_adjunction_families.lp'):
                old = text
                count = 2 if path.startswith('emdash3_2_') else 4
                assert text.count('@comp_cat_cov_func_func_transf') == count
                text = text.replace('@comp_cat_cov_func_func_transf',
                    '@hom_postcomp_tele_transf Cat_cat Cat_cat (@id_func Cat_cat)')
                if path.startswith('emdash3_2_'):
                    text = text.replace('// Whole unit/counit observations through existing tele-postcomposition.',
                        '// Whole unit/counit observations through existing ordinary tele-postcomposition.\n'
                        '// The short comp_cat_cov_func_func_transf alias now selects Cartesian\n'
                        '// mapping categories; these original endpoints are ordinary Functor_cat.')
                changes.append({'source': path, 'owner': 'ordinary-target postcomposition adjunction unit/counit',
                                'reason': 'Use the existing generic Cat_cat telescope directly at the original ordinary mapping endpoints; preserve the supplied J, existing OneCat hypotheses and every reviewer statement',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_strict_pointwise_equivalences.lp':
                old = text
                marker = '// Displayed fixed-forward pointwise evidence over one whole transformation.'
                assert text.count(marker) == 1
                start = text.index(marker)
                displayed = text[start:]
                assert displayed.count('@Functor_cat') == 3
                text = text[:start] + displayed.replace('@Functor_cat', '@Functor_cart_cat')
                text = text.replace(marker, marker + '\n'
                    '// The actual Cat_cart fibre Hom is Cartesian: retain the forward cell\n'
                    '// and both chosen inverse components in that same coefficient.\n'
                    '// Whole assembly remains the inherited primitive assumption above.')
                changes.append({'source': path, 'owner': 'displayed pointwise-equivalence coefficient',
                                'reason': 'Use the actual Cartesian coefficient of tdapp0_fapp0 for all selected pointwise inverse data; preserve ordinary assembly and the original whole declared inverse/law owners',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_represented_comma_families.lp':
                old = text
                start_marker = '// Source, middle, and target families for a transformation graph.'
                end_marker = '// Fibrewise Sigma of the existing whole internal action.'
                assert text.count(start_marker) == text.count(end_marker) == 1
                start, end = text.index(start_marker), text.index(end_marker)
                tail = text[end:]
                assert tail.count('@hom_int ') == 107
                tail = tail.replace('@hom_int ', '@hom_int_view ')
                # The single inner-total formation still consumes Cart,
                # unlike the surrounding ordinary internal-action inputs.
                canonical = '(@homdc_edge_catd C C (@hom_int_view C C (@id_func C)))'
                assert tail.count(canonical) == 1
                tail = tail.replace(canonical, canonical.replace('@hom_int_view ', '@hom_int '), 1)
                sigma_end = '// Pointwise opposite turns that whole transformation into the displayed map'
                assert tail.count(sigma_end) == 1
                tail = end_marker + '\n' + fragment('production_comma_graph_sigma.lpfragment') + '\n' + tail[tail.index(sigma_end):]
                admission_end = '// The represented C-family at the varying source F[x].'
                assert tail.count(admission_end) == 1
                begin, end_admission = tail.index(sigma_end), tail.index(admission_end)
                tail = tail[:begin] + sigma_end + '\n' + fragment('production_comma_graph_admitted.lpfragment') + '\n' + tail[end_admission:]
                basechange_end = 'protected symbol comma_graph_target_sec\n'
                assert tail.count(basechange_end) == 1
                begin, end_basechange = tail.index(admission_end), tail.index(basechange_end)
                tail = tail[:begin] + admission_end + '\n' + fragment('production_comma_graph_basechange.lpfragment') + '\n' + tail[end_basechange:]
                total_end = '// The actual whole input classifier.'
                assert tail.count(total_end) == 1
                begin, end_total = tail.index(basechange_end), tail.index(total_end)
                tail = tail[:begin] + fragment('production_comma_graph_total.lpfragment') + '\n' + tail[end_total:]
                constructor_end = '// Whole source projection with its original inverse data.'
                assert tail.count(constructor_end) == 1
                begin, end_constructor = tail.index(total_end), tail.index(constructor_end)
                tail = tail[:begin] + total_end + '\n\n' + fragment('production_represented_comma_constructor.lpfragment') + '\n' + tail[end_constructor:]
                # Original source-comparison proof, with its actual selected
                # inverse data. Only total/section duals become O here; protect
                # the nine internal-Hom T(K) classifiers before that change.
                source_end = '// Extract the actual target section before taking the outer opposite.'
                assert tail.count(source_end) == 1
                begin, end_source = tail.index(constructor_end), tail.index(source_end)
                source = tail[begin:end_source]
                theta_type = '''(@Transf (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))'''
                assert source.count(theta_type) == 9
                source = source.replace(theta_type, 'COMMA_SOURCE_THETA_TYPE')
                assert source.count('Op_cat') == 396 and source.count('Op_func') == 80
                source = source.replace('Op_cat', 'TotalOp_cat').replace('Op_func', 'TotalOp_func')
                source = source.replace('COMMA_SOURCE_THETA_TYPE', theta_type.replace('@Transf', '@StrictTransfor', 1))
                source = source.replace(constructor_end, constructor_end + '\n'
                    '// Total/section duality is O; the admitted internal Hom remains over T(K).')
                step1 = 'protected symbol comma_source_gamma_step1 '
                step2 = 'protected symbol comma_source_gamma_step2 '
                assert source.count(step1) == source.count(step2) == 1
                s1, s2 = source.index(step1), source.index(step2)
                source = source[:s1] + fragment('production_comma_source_reframe.lpfragment') + '\n' + source[s2:]
                tail = tail[:begin] + source + tail[end_source:]
                # Expose the unchanged ordinary-lax public source interface
                # at its dependency-ready position. Only its canonical
                # internal-action admission changes; eta gains no premise.
                ordinary_start = 'symbol represented_comma_family_func '
                ordinary_end = 'symbol represented_comma_family_target_func '
                assert tail.count(ordinary_start) == tail.count(ordinary_end) == 1
                o1, o2 = tail.index(ordinary_start), tail.index(ordinary_end)
                ordinary = tail[o1:o2]
                assert ordinary.count('@tapp1_int_fapp0_transf') == 4
                ordinary = ordinary.replace('@tapp1_int_fapp0_transf', '@tapp1_int_cart')
                tail = tail[:o1] + tail[o2:]
                tail = tail.replace(source_end, '// Original ordinary-lax constructor and source comparison.\n'
                    + ordinary + '\n' + source_end, 1)
                # Target section uses the same corrected total base and the
                # existing canonical projection's ordinary displayed view.
                target_start = 'protected symbol comma_section_gamma_target_family_map '
                target_end = '// Link that section to the original total base change.'
                assert tail.count(target_start) == tail.count(target_end) == 1
                t1, t2 = tail.index(target_start), tail.index(target_end)
                target_section = tail[t1:t2]
                assert target_section.count(theta_type) == 6
                target_section = target_section.replace(theta_type, 'COMMA_TARGET_THETA_TYPE')
                assert (target_section.count('Op_cat'), target_section.count('Op_func'), target_section.count('Op_transf')) == (35, 3, 1)
                target_section = (target_section.replace('Op_cat', 'TotalOp_cat')
                                  .replace('Op_func', 'TotalOp_func').replace('Op_transf', 'TotalOp_transf'))
                target_section = target_section.replace('COMMA_TARGET_THETA_TYPE', theta_type.replace('@Transf', '@StrictTransfor', 1))
                target_projection = '(@homdc_total_target_funcd X Y (@represented_comma_prof X Y J))'
                assert target_section.count(target_projection) == 1
                target_section = target_section.replace(target_projection, '(@strict_transfor _ _ _ _ ' + target_projection + ')')
                tail = tail[:t1] + target_section + tail[t2:]
                text = text[:start] + fragment('production_comma_graph_families.lpfragment') + '\n' + tail
                changes.append({'source': path, 'owner': 'represented-comma graph family profiles',
                                'reason': 'Retain canonical strict-x admission, total-dual sections, corrected base change, derived graph and original source inverse data; the coupled target adaptation is recorded below',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/action_profile_inherited_assembly_controls.lp':
                old = text
                assert text.count('Functor_cat (@Fibre_cat') == 2
                text = text.replace('Functor_cat (@Fibre_cat', 'Functor_cart_cat (@Fibre_cat')
                old_negative = 'assertnot [A B : Cat] (F : τ (Functor A B)) [x y z : τ (Obj A)]'
                assert text.count(old_negative) == 1
                text = text.replace(old_negative, old_negative.replace('assertnot', 'assert'), 1)
                text = text.replace('// The inherited primitive does not install these generic reflexivity cuts.',
                    '// Default functors now preserve composition; ordinary transfors remain lax.')
                changes.append({'source': path, 'owner': 'inherited assembly controls',
                                'reason': 'Observe the selected displayed inverse in its actual Cartesian coefficient, and update only the former lax-functor negative to the strict-default positive',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            zero_profiles = {
                'emdash3_2_zero_arrow_diagrams.lp': (2, 10, 0),
                'emdash3_2_kernel_cokernel_adjunctions.lp': (38, 5, 0),
                'emdash3_2_kernel_cokernel_adjunction_mates.lp': (16, 2, 4),
                'examples/kernel_cokernel_adjunctions.lp': (100, 9, 14),
            }
            if path in zero_profiles:
                old = text
                counts = (text.count('Functor_cat WalkingArrow_cat C'), text.count('(Op_cat C)'),
                          text.count('τ (Functor WalkingArrow_cat C)'))
                assert counts == zero_profiles[path], (path, counts)
                text = text.replace('Functor_cat WalkingArrow_cat C', 'Functor_oplax_cat WalkingArrow_cat C')
                text = text.replace('(Op_cat C)', '(TotalOp_cat C)')
                text = text.replace('τ (Functor WalkingArrow_cat C)', 'τ (Obj (Functor_oplax_cat WalkingArrow_cat C))')
                text = text.replace('τ (Transf d0 d1)', 'τ (Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1)')
                if path == 'emdash3_2_zero_arrow_diagrams.lp':
                    assert text.count('@Op_transf ') == 1
                    text = text.replace('@Op_transf ', '@TotalOp_transf ')
                    text = text.replace('TerminalObject(Op(C),t)', 'TerminalObject(TotalOp(C),t)')
                    text = text.replace('  Op_transf.', '  TotalOp_transf.')
                    text = text.replace('transparently via Op.', 'through total duality, which retains the default lax profile.')
                    text = text.replace('C→Arr(C)', 'C→Arr_oplax(C)')
                elif path == 'emdash3_2_kernel_cokernel_adjunctions.lp':
                    text = text.replace('diagram_evaluation_at_func', 'diagram_oplax_evaluation_at_func')
                    text = text.replace('/* Whole kernel/cokernel adjunction structures for the preadditive setting.',
                        '/* Whole kernel/cokernel adjunction structures for the preadditive setting.\n'
                        '   The corrected whole zero-arrow embeddings land in oplax diagrams;\n'
                        '   the supplied adjunctions and their actual unit/counit data use that profile.')
                if path == 'examples/kernel_cokernel_adjunctions.lp':
                    component = '@tapp0_fapp0 WalkingArrow_cat C _ _'
                    assert text.count(component) == 2
                    text = text.replace(component,
                        '@tapp0_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) _ _')
                    assert [len(re.findall(r'(?m)^' + k + r'\b', text)) for k in ('assert','assertnot')] == [16,2]
                changes.append({'source': path, 'owner': 'whole terminal/initial embeddings and supplied kernel/cokernel adjunctions',
                                'reason': 'Retain the existing general terminal transformation; use the corrected oplax arrow-diagram profile and total duality for the initial transformation, with its dual hypothesis explicit',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/zero_arrow_diagrams.lp':
                old = text
                text = fragment('production_zero_arrow_reviewer.lpfragment')
                assert [len(re.findall(r'(?m)^' + k + r'\b', old)) for k in ('assert','assertnot')] == [18,2]
                assert [len(re.findall(r'(?m)^' + k + r'\b', text)) for k in ('assert','assertnot')] == [18,2]
                changes.append({'source': path, 'owner': 'zero-arrow reviewer',
                                'reason': 'Retain all original observations using the actual oplax coefficient, decoded point functors and the explicit total-dual terminal hypothesis',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_arrow_diagram_families.lp':
                old = text
                text = fragment('production_arrow_diagram_families.lpfragment')
                for name in ('transf_arrow_diagram_func', 'transf_arrow_diagram_point_path'):
                    assert old.count('symbol ' + name + '\n') == text.count('symbol ' + name + '\n') == 1
                changes.append({'source': path, 'owner': 'transf_arrow_diagram_func',
                                'reason': 'Introduce the same walking diagram through the corrected two-profile exchange; preserve the whole eta and decode its point observation through actual duality',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/arrow_diagram_families.lp':
                old = text
                text = fragment('production_arrow_diagram_reviewer.lpfragment')
                assert [len(re.findall(r'(?m)^' + k + r'\b', old)) for k in ('assert', 'assertnot')] == [22, 2]
                assert [len(re.findall(r'(?m)^' + k + r'\b', text)) for k in ('assert', 'assertnot')] == [22, 2]
                changes.append({'source': path, 'owner': 'arrow diagram reviewer',
                                'reason': 'Retain the original whole observations with oplax diagram coefficients, decoded point functors and the corresponding opposite-profile evaluation',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_diagram_evaluation.lp':
                old = text
                first = '// Whole evaluation after precomposition:'
                last = '// Existing generic composition evidence at the ordinary family target.'
                assert text.count(first) == text.count(last) == 1
                start = text.index(first)
                end = text.index(last)
                text = (fragment('production_diagram_evaluation_profile.lpfragment') + '\n'
                        + fragment('production_diagram_evaluation_naturality.lpfragment') + '\n'
                        + 'require open emdash.emdash3_2_one_cat_action_paths;\n'
                        + 'require open emdash.emdash3_2_one_cat_functor_closure;\n\n'
                        + text[start:end]
                        + fragment('production_diagram_evaluation_helpers.lpfragment') + '\n'
                        + fragment('production_oplax_diagram_evaluation.lpfragment'))
                declaration = r'(?m)^(?:(?:constant|injective|protected|private)\s+)?symbol\s+([A-Za-z0-9_]+)\b'
                old_names, new_names = re.findall(declaration, old), re.findall(declaration, text)
                assert len(old_names) == 9
                assert all(new_names.count(name) == 1 for name in old_names)
                changes.append({'source': path, 'owner': 'diagram evaluation',
                                'reason': 'Preserve general fixed evaluation by postcomposition; correct whole shape evaluation to its alternating-dual oplax profile and reindex that actual profile',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/diagram_evaluation.lp':
                old = text
                text = fragment('production_diagram_evaluation_reviewer.lpfragment')
                assert [len(re.findall(r'(?m)^' + kind + r'\b', old))
                        for kind in ('assert', 'assertnot')] == [10, 3]
                assert [len(re.findall(r'(?m)^' + kind + r'\b', text))
                        for kind in ('assert', 'assertnot')] == [10, 3]
                changes.append({'source': path, 'owner': 'diagram evaluation reviewer',
                                'reason': 'Retain every original observation with the corrected opposite transformation profile and existing postcomposition action',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('emdash3_2_eq1_hom_action.lp', 'examples/groupoidal_structured_j_eq1.lp'):
                old = text
                facade = 'Fibre_cat (@strict_functor C Cat_cat D)'
                expected = 2 if path == 'emdash3_2_eq1_hom_action.lp' else 4
                assert text.count(facade) == expected, path
                text = text.replace(facade, '@fapp0 C Cat_cat (@strict_functor C Cat_cat D)')
                if path == 'emdash3_2_eq1_hom_action.lp':
                    text = text.replace(
                        '  The displayed family is supplied as one classified `StrictFunctor`, so its',
                        '  The ordinary Cat-valued diagram retains its legacy `StrictFunctor` input.\n'
                        '  Use its actual object action, without imposing Cat_cart-family admission. Its')
                else:
                    observation = '  ≡ @fib_cov_transf C D x u;'
                    assert text.count(observation) == 1
                    text = text.replace(observation,
                        '  ≡ @strict_transfor C Cat_cart (@FibCov_source_catd C x) D\n'
                        '      (@fib_cov_transf C D x u);')
                    text = text.replace(
                        '// Structured groupoidal J is the existing directed-family action.',
                        '// Structured groupoidal J observes the ambient view of canonical fibre covariance.')
                    action = '(Path_cat A) Cat_cat D x x (@eq_refl A x)'
                    assert text.count(action) == 2
                    text = text.replace(action, '(Path_cat A) Cat_cart D x x (@eq_refl A x)')
                    carrier = '(Hom Cat_cat (Fibre_cat D x) (Fibre_cat D x))'
                    assert text.count(carrier) == 2
                    text = text.replace(carrier, '(Functor (Fibre_cat D x) (Fibre_cat D x))')
                changes.append({'source': path, 'owner': 'groupoidal_fibre_transport_equiv',
                                'reason': 'Evaluate the existing general Cat-valued diagram directly instead of using the now-specialised admitted-family facade; keep its input, arrow action, chosen inverse and proof body',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_shaped_pathout.lp':
                old = text
                cart_pair = '(Functor_cat I (Product_cat (Op_cat I) I))'
                component = '(Product_cat (Op_cat I) I)\n    Cat_cat\n    (@Unit_prof I)'
                assert text.count(cart_pair) == text.count(component) == 1
                text = text.replace(cart_pair,
                    '(Functor_cart_cat I (Product_cat (Op_cat I) I))', 1)
                text = text.replace(component,
                    '(Product_cat (Op_cat I) I)\n    Cat_cart\n    (@Unit_prof I)', 1)
                changes.append({'source': path,
                                'owner': 'shaped_fixed_source_pair_func / shaped_pathout_component',
                                'reason': 'Follow the Cartesian product-pair and profunctor coefficient annotations; retain the original fixed-source, totalization and higher-action bodies',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_pathout_transformation_reframing.lp':
                old = text
                start = text.index('symbol pathout_lhs_tele\n')
                end = text.index('symbol pathout_lhs_tele_source\n', start)
                telescope = text[start:end]
                assert telescope.count('Functor_cat') == 2
                text = text[:start] + telescope.replace('Functor_cat', 'Functor_cart_cat') + text[end:]
                proofs = fragment('production_pathout_reframing.lpfragment')
                for name in ('pathout_general_pre_lhs_tele_path',
                             'pathout_lhs_tele_transport_path',
                             'pathout_top_lhs_transport_path'):
                    marker = 'symbol ' + name + '\n'
                    assert text.count(marker) == proofs.count(marker) == 1
                    start = text.index(marker)
                    end = text.index(';', text.index('≔', start)) + 1
                    begin = proofs.index(marker)
                    finish = proofs.index(';', proofs.index('≔', begin)) + 1
                    text = text[:start] + proofs[begin:finish] + text[end:]
                text = text.replace(
                    '// The cold whole Cat-precomposition comparison identifies the stable\n// precomposition component with the same telescope source.',
                    '// Cartesian precomposition now computes the telescope source directly.\n// The fixed-target action uses the selected pre/right convention.')
                text = text.replace('symbol pathout_lhs_tele_transport_path\n',
                    '// Fixed-target internalization has strict pre/right action for any epsilon.\n// Compare through the core right-leg path, not a general left-leg equality.\n'
                    'symbol pathout_lhs_tele_transport_path\n', 1)
                changes.append({'source': path, 'owner': 'PathOut pre/right source reframing',
                                'reason': 'Keep the original statements and arbitrary lax epsilon; derive the two transport paths from the conventional pre action and existing right-leg comparison instead of the retired general left-leg equality',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_cubical_dependent_hom.lp':
                old = text
                marker = 'symbol homdc_target_func\n'
                assert text.count(marker) == 1
                start = text.index(marker)
                end = text.index(';', text.index('≔', start)) + 1
                text = text[:start] + fragment('production_cubical_hom_evaluation.lpfragment').rstrip() + text[end:]
                assert text.count('(@hom_con_int\n') == 1
                assert text.count('(@hom_int C C') == 2
                # Keep the actual Cartesian result of hom_con_int: its next
                # totalization consumes that whole profile, not just objects.
                text = text.replace('(Catd_cat (Op_cat (Hom_cat K2 x2 y2)))',
                    '(Functor_cart_cat (Op_cat (Hom_cat K2 x2 y2)) Cat_cart)')
                text = text.replace('(Catd_cat (Op_cat (Hom_cat C x2 y2)))',
                    '(Functor_cart_cat (Op_cat (Hom_cat C x2 y2)) Cat_cart)')
                text = text.replace('(@hom_int C C', '(@hom_int_view C C')
                text = text.replace(': Hom_K1(x1,y1) -> Catd(Hom_K2(x2,y2)^op).',
                    ': Hom_K1(x1,y1) -> Cart(T(Hom_K2(x2,y2)),Cat_cart).')
                changes.append({'source': path, 'owner': 'fixed-endpoint cubical Hom evaluation',
                                'reason': 'Use existing whole Cartesian component evaluation, preserve the original broad E input, and expose the actual Cartesian Hom result needed by totalization',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/cubical_dependent_hom.lp':
                old = text
                start = text.index('// The outer and inner hom actions')
                end = text.index('// A direct unit-profunctor', start)
                observations = text[start:end]
                assert observations.count('Cat_cat') == 2
                text = text[:start] + observations.replace('Cat_cat', 'Cat_cart') + text[end:]
                text = text.replace('(Catd_cat (Op_cat (Hom_cat K2 x2 y2)))',
                    '(Functor_cart_cat (Op_cat (Hom_cat K2 x2 y2)) Cat_cart)')
                text = text.replace('(Catd_cat (Op_cat (Hom_cat C x2 y2)))',
                    '(Functor_cart_cat (Op_cat (Hom_cat C x2 y2)) Cat_cart)')
                changes.append({'source': path, 'owner': 'inner cubical Hom action',
                                'reason': 'Observe the actual admitted family coefficient; retain original leaf, both higher actions and twisted-boundary negative control',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_cubical_square_total.lp':
                old = text
                start = text.index('// Whole family of first projections')
                opposite = text.index('// Pointwise opposite retains', start)
                end = text.index('// At a, totalize the b-indexed filler family.', opposite)
                legacy = text[opposite:end]
                assert len(re.findall(r'(?m)^rule ', legacy)) == 3
                assert len(re.findall(r'(?m)^unif_rule ', legacy)) == 4
                inactive = '''/*
  Migration boundary: the following legacy same-base Op clauses are inactive.
  Op_catd now changes the base, and Op_funcd accepts Cartesian maps. Their
  corrected whole projection counterparts above use the actual TotalOp
  profiles. The old point-action clauses remain inactive audit candidates;
  none is silently asserted with the old types.

''' + legacy + '\n*/\n\n'
                text = (text[:start] + fragment('production_cubical_sigma_projection.lpfragment')
                        + '\n' + fragment('production_cubical_projection_views.lpfragment') + '\n' + inactive + text[end:])
                text = text.replace('(Functor (Hom_cat K1 x1 y1) Cat_cat)',
                                    '(Functor (Hom_cat K1 x1 y1) Cat_cart)')
                source = '''    (Catd_cat (Op_cat (Hom_cat K2 x2 y2)))
    Cat_cat
    (@Sigma_func (Op_cat (Hom_cat K2 x2 y2)))'''
                assert text.count(source) == 1
                text = text.replace(source, '''    (Functor_cart_cat (Op_cat (Hom_cat K2 x2 y2)) Cat_cart)
    Cat_cart
    (@Sigma_coeff_func (Op_cat (Hom_cat K2 x2 y2)))''', 1)
                projection = '''    (@sigma_proj1_family_funcd
      (Hom_cat K1 x1 y1)
      (Op_cat (Hom_cat K2 x2 y2))
      (@homdc_ K1 K2 E x1 y1 x2 y2 u v));'''
                assert text.count(projection) == 1
                text = text.replace(projection, '''    (@strict_transfor _ _ _ _
      (@sigma_proj1_family_funcd
        (Hom_cat K1 x1 y1)
        (Op_cat (Hom_cat K2 x2 y2))
        (@homdc_ K1 K2 E x1 y1 x2 y2 u v)));''', 1)
                text = text.replace('by applying the existing `homd_int` to the pointwise\n  opposite inner edge total;',
                    'by applying the existing `homd_int` to the total-dual\n  inner edge family over its shifted outer base;')
                changes.append({'source': path, 'owner': 'varying Sigma projection and fixed-boundary total',
                                'reason': 'Use canonical Cartesian projection/formation and inherited strict-map action; preserve the broader fixed-endpoint E input',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text),
                                'redundantDirectIntrinsicRuleRemoved': 1,
                                'pendingLegacyOppositeRules': 3,
                                'pendingLegacyOppositeUnifiers': 0,
                                'correctedWholeProjectionViews': 4,
                                'pendingLegacyBlockSha256': sha(legacy)})
            if path == 'emdash3_2_cubical_internalization.lp':
                old = text
                text = fragment('production_cubical_total_duality.lpfragment')
                changes.append({'source': path, 'owner': 'two-sided Homd/Sigma total and endpoint projections',
                                'reason': 'Admit the nested Cartesian family, shift the total-dual family base to O(K1), and derive the existing total and projections with O rather than the invalid same-base fibre opposite',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_gray_interchanger_orientation.lp':
                old = text
                readings = fragment('production_interchanger_source_reading.lpfragment')
                for name in ('gray_interchanger_common_func',
                             'gray_interchanger_source_common_path',
                             'gray_interchanger_lhs_tele_common_func_path',
                             'gray_interchanger_lhs_tele_post_composite_path'):
                    marker = 'protected symbol ' + name + '\n'
                    assert text.count(marker) == readings.count(marker) == 1
                    start = text.index(marker)
                    end = text.index(';', text.index('≔', start)) + 1
                    begin = readings.index(marker)
                    finish = readings.index(';', readings.index('≔', begin)) + 1
                    text = text[:start] + readings[begin:finish] + text[end:]
                start = text.index('protected symbol gray_interchanger_lhs_tele_func\n')
                end = text.index('protected symbol gray_interchanger_lhs_tele_value\n', start)
                telescope = text[start:end]
                assert telescope.count('Functor_cat GrayInterchangerDomain_cat GrayInterchangerCodomain_cat') == 2
                text = text[:start] + telescope.replace(
                    'Functor_cat GrayInterchangerDomain_cat GrayInterchangerCodomain_cat',
                    'Functor_cart_cat GrayInterchangerDomain_cat GrayInterchangerCodomain_cat') + text[end:]
                text = text.replace('// Common fixed-generator internal action selected by both whole strict paths.',
                    '// Shared left-hand presentation of the source endpoint and its telescope.\n'
                    '// It is not the pre/right middle action or a common value of both endpoints.')
                text = text.replace('// The two formal endpoints meet at the common internal action by the existing\n// whole displayed strict-naturality paths.',
                    '// The source endpoint and this left-hand presentation are the same value.\n'
                    '// The target retains its separate pre/right reading below.')
                text = text.replace('  The `lax_transfor` head makes the selected pre/right target judgmental; no\n  evidence-derived endpoint adapter, inverse, or independent interchanger is\n  added.',
                    '  The default conventional-lax action fixes the pre/right leg. No supplied\n'
                    '  comparison, inverse, or independent interchanger is added.')
                changes.append({'source': path, 'owner': 'interchanger source endpoint reading',
                                'reason': 'Use the actual post/left source and Cartesian telescope instead of the retired general left-leg equality; retain every public endpoint, cell and coordinate-swapped square',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_strict_functor_actions.lp':
                old = text
                begin = text.index('// Classified strict functors preserve ordinary isomorphism evidence.')
                end = text.index('/*\n  Selected named strict packages', begin)
                text = text[:begin] + fragment('production_default_inverse_action.lpfragment') + text[end:]
                marker = '/*\n  Left adjoints preserve weighted colimits.'
                assert text.count(marker) == 1
                text = text[:text.index(marker)] + fragment('production_weighted_colimit.lpfragment')
                text = text.replace(
                    '  selected inverses remain computational, and the ambient lax carrier gains\n  no equality.',
                    '  selected inverses remain computational. This legacy classified API now\n'
                    '  coexists with strict default functors; its wrappers await consumer migration\n'
                    '  and retirement. No strictness of arbitrary transformations is added.')
                changes.append({'source': path, 'owner': 'left-adjoint weighted-colimit preservation',
                                'reason': 'Default inverse action takes the ordinary strict functor directly, with legacy names as defined views; transpose the existing Hom comparison and retain the original three-step T-weighted proof without a second adjunction or supplied strictness evidence',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/cubical_square_total.lp':
                text += '\n' + fragment('production_cubical_sigma_projection_controls.lpfragment')
            if path == 'examples/cubical_internalization.lp':
                old = text
                text = text.replace('are derived from ordinary Sigma, pointwise opposite, and homd_int.',
                    'are derived from ordinary Sigma, shifted total fibre duality, and homd_int.')
                text = text.replace('// The internal owner is literally the existing homd_int of the pointwise\n// opposite inner edge family.',
                    '// The internal owner is the existing homd_int of the total-dual inner\n// edge family over O(K1).')
                text = text.replace('(Catd_cat K2)', '(Functor_cart_cat K2 Cat_cart)')
                start = text.index('assert [K1 K2')
                end = text.index('// At a fixed', start)
                text = text[:start] + text[start:end].replace(
                    '      (Op_cat K1)', '      (TotalOp_cat K1)') + text[end:]
                controls = fragment('production_cubical_total_controls.lpfragment')
                split = controls.index('// The corrected total rejects')
                start = text.index('// At a fixed first side arrow')
                end = text.index('// The selected ordinary', start)
                text = text[:start] + controls[:split] + text[end:]
                text += '\n' + controls[split:]
                changes.append({'source': path, 'owner': 'corrected total-dual Hom reading and retained endpoints',
                                'reason': 'Replace the invalid ordinary-opposite-total comparison by the actual inner Hom; retain square/endpoint observations and reject reversed or erased fillers',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
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
                # The original target comparison and its selected inverses
                # run in O(K), O(Y). Internal-Hom inputs remain over T(K).
                target_before = text
                raw_start = 'protected symbol comma_basechange_gamma_target_raw0 '
                raw_end = '// Group the original mapped graph section.'
                assert text.count(raw_start) == text.count(raw_end) == 1
                r1, r2 = text.index(raw_start), text.index(raw_end)
                raw = text[r1:r2]
                assert raw.count(theta_type) == 11
                assert raw.count(theta_type.replace('@hom_int_view ', '@hom_int ')) == 3
                raw = raw.replace(theta_type.replace('@hom_int_view ', '@hom_int '), theta_type)
                raw = raw.replace(theta_type, 'COMMA_RAW_THETA_TYPE')
                assert (raw.count('Op_cat'), raw.count('Op_func'), raw.count('Op_transf')) == (151, 8, 1)
                raw = (raw.replace('Op_cat', 'TotalOp_cat').replace('Op_func', 'TotalOp_func')
                       .replace('Op_transf', 'TotalOp_transf').replace('@one_cat_op ', '@one_cat_total_op ')
                       .replace('@comma_op_omega_along ', '@comma_total_op_omega_along '))
                raw = raw.replace('COMMA_RAW_THETA_TYPE', theta_type.replace('@Transf', '@StrictTransfor', 1))
                assert raw.count(target_projection) == 6
                raw = raw.replace(target_projection, '(@strict_transfor _ _ _ _ ' + target_projection + ')')
                link = 'protected symbol comma_basechange_gamma_target_link '
                assert raw.count(link) == 1
                raw = raw.replace(link, fragment('production_comma_target_reframe_view.lpfragment') + '\n' + link, 1)
                text = text[:r1] + raw + text[r2:]
                op_evidence = 'protected symbol comma_op_omega_along '
                oe = text.index(op_evidence); oe_end = text.index(';', text.index('≔', oe)) + 1
                old = text[oe:oe_end]
                text = text[:oe] + old.replace('comma_op_omega_along', 'comma_total_op_omega_along').replace('Op_cat', 'TotalOp_cat') + text[oe_end:]
                grouped_start = '// Group the original mapped graph section.'
                classify_start = '// Classify the target section and retain the whole target inverse.'
                ordinary_target = '// Original Γ interface, specialized to the native Hom action of h.'
                g1, g2 = text.index(grouped_start), text.index(classify_start)
                grouped = text[g1:g2]
                assert grouped.count(theta_type) == 2
                grouped = grouped.replace(theta_type, 'COMMA_GROUPED_THETA_TYPE')
                assert grouped.count('Op_cat') == 19 and grouped.count('Op_func') == 0
                grouped = grouped.replace('Op_cat', 'TotalOp_cat')
                grouped = grouped.replace('COMMA_GROUPED_THETA_TYPE', theta_type.replace('@Transf', '@StrictTransfor', 1))
                text = text[:g1] + grouped + text[g2:]
                c1, c2 = text.index(classify_start), text.index(ordinary_target)
                classification = text[c1:c2]
                projections = fragment('production_comma_target_projections.lpfragment')
                projection_names = ('comma_classification_target_projection',
                                    'comma_classification_middle_projection',
                                    'comma_classification_identity_section_projected')
                for name in projection_names:
                    marker = 'protected symbol ' + name
                    assert classification.count(marker) == projections.count(marker) == 1
                    p1 = classification.index(marker); p2 = classification.index(';', classification.index('≔', p1)) + 1
                    classification = classification[:p1] + name.upper() + classification[p2:]
                assert classification.count(theta_type) == 14
                classification = classification.replace(theta_type, 'COMMA_CLASSIFICATION_THETA_TYPE')
                assert (classification.count('Op_cat'), classification.count('Op_func'), classification.count('Op_transf')) == (53, 7, 1)
                classification = (classification.replace('Op_cat', 'TotalOp_cat')
                                  .replace('Op_func', 'TotalOp_func').replace('Op_transf', 'TotalOp_transf'))
                classification = classification.replace('COMMA_CLASSIFICATION_THETA_TYPE', theta_type.replace('@Transf', '@StrictTransfor', 1))
                for name in projection_names:
                    p1 = projections.index('protected symbol ' + name); p2 = projections.index(';', projections.index('≔', p1)) + 1
                    classification = classification.replace(name.upper(), projections[p1:p2])
                text = text[:c1] + classification + text[c2:]
                ordinary = text[text.index(ordinary_target):]
                assert ordinary.count('@tapp1_int_fapp0_transf') == 3
                text = text[:text.index(ordinary_target)] + ordinary.replace('@tapp1_int_fapp0_transf', '@tapp1_int_cart')
                changes.append({'source': path, 'owner': 'whole represented-comma target comparison and classification',
                                'reason': 'Preserve the original selected inverse data and OneCat target premise, correct the total-dual bases and coefficient views, and retain the ordinary-lax public wrappers through canonical admission',
                                'oldBodySha256': sha(target_before), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_one_cat_op.lp':
                addition = fragment('production_one_cat_total_dual.lpfragment')
                text += '\n' + addition
                changes.append({'source': path, 'owner': 'one_cat_total_op',
                                'reason': 'Ordinary-target comparison now uses total duality; retain the original ordinary-category premise through explicit discrete-profile closure',
                                'declaredBoundary': 'Discrete classifier closure under total duality; no operational chosen inverse or caller proof added',
                                'insertedSha256': sha(addition)})
            if path == 'examples/represented_comma_families.lp':
                old = text
                # The original arbitrary-section rejection observes the O
                # total projection; the seven Theta inputs still use T(K).
                pre, post = text.split('assert [A K : Cat]', 1)
                assert pre.count('Op_cat') == 11 and pre.count('Op_func') == 4
                pre = pre.replace('Op_cat', 'TotalOp_cat').replace('Op_func', 'TotalOp_func')
                text = pre + 'assert [A K : Cat]' + post
                assert text.count('(theta : τ (@Transf (Op_cat K)') == 7
                text = text.replace('(theta : τ (@Transf (Op_cat K)', '(theta : τ (@StrictTransfor (Op_cat K)')
                assert text.count('@hom_int ') == 16
                text = text.replace('@hom_int ', '@hom_int_view ')
                assert text.count('@tapp0_fapp0 K Cat_cat') == 1
                text = text.replace('@tapp0_fapp0 K Cat_cat', '@tapp0_fapp0 K Cat_cart', 1)
                assert text.count(' x theta)) (@id K x)') == 1
                text = text.replace(' x theta)) (@id K x)', ' x (@strict_transfor _ _ _ _ theta))) (@id K x)', 1)
                fibre = '(@homdc_fibre X Y (@represented_comma_prof X Y J)'
                assert text.count(fibre) == 1
                text = text.replace(fibre, '(@homdc_fibre X Y\n'
                    '  (@comp_cat_fapp0 (Op_cat X) (Functor_cart_cat Y Cat_cart) (Catd_cat Y)\n'
                    '    (Functor_cart_include Y Cat_cart) (@represented_comma_prof X Y J))', 1)
                text = text.replace('// Whole internal-Hom input: it need not be presented as the action of h.',
                    '// Whole internal-Hom input with the admitted strict x-profile;\n'
                    '// its displayed y-components remain lax. It need not be presented\n'
                    '// as the canonical action of an ordinary transformation h.')
                changes.append({'source': path, 'owner': 'original represented-comma reviewer',
                                'reason': 'Retain all original observations with corrected total duality, valid Theta profile and actual coefficient views; ordinary eta inputs remain lax',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
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
                old = text
                text = text.replace('K Cat_cat E D', 'K Cat_cart E D')
                marker = '// The target/right reading is available only through the strict profile.'
                assert text.count(marker) == 1
                start = text.index(marker)
                end = text.index('// Every opaque classified object', start)
                section = text[start:end].replace(
                    '(Functor_cat (Fibre_cat E x) (Fibre_cat D y))',
                    '(Functor_cart_cat (Fibre_cat E x) (Fibre_cat D y))', 1)
                section = section.replace(marker,
                    '// The legacy strict-profile observation agrees with the default pre/right action.')
                text = text[:start] + section + text[end:]
                text = text.replace(
                    '// An ambient compositor is typed between its two retained endpoints; those\n// endpoints are no longer convertible, so a literal identity comparison is\n// not even the appropriate judgment.',
                    '// An ambient compositor has the same endpoints under the strict default.\n// Its native intrinsic extraction is retained.')
                changes.append({'source': path, 'owner': 'displayed-profile observations',
                                'reason': 'Retain the original assertions with the actual family coefficient and whole Hom target; ordinary extracted-cell properties keep Functor_cat',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            target = package / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)
        for command in re.findall(r'(?m)^\s*require(?:\s+open)?\s+([^;]+);', text):
            for module in command.split():
                assert re.fullmatch(r'emdash(?:\.[A-Za-z0-9_]+)+', module), module
                stage(module.removeprefix('emdash.').replace('.', '/') + '.lp')

    stage('examples/gray_profiles.lp')
    stage('examples/cubical_dependent_hom.lp')
    stage('examples/cubical_square_total.lp')
    stage('examples/cubical_internalization.lp')
    stage('examples/cubical_internalization_composition.lp')
    stage('examples/gray_interchanger.lp')
    stage('examples/gray_interchanger_orientation.lp')
    stage('examples/profunctor_weighted_limits.lp')
    stage('examples/groupoidal_structured_j_eq1.lp')
    stage('examples/diagram_evaluation.lp')
    stage('examples/arrow_diagram_families.lp')
    stage('examples/zero_arrow_diagrams.lp')
    stage('examples/zero_arrow_cone_maps.lp')
    stage('examples/kernel_cokernel_adjunctions.lp')
    stage('examples/adjunction_mates.lp')
    stage('examples/one_cat_adjunction_families.lp')
    stage('examples/action_profile_inherited_assembly_controls.lp')
    stage('examples/represented_comma_families.lp')
    stage('examples/action_profile_prof_defiso_controls.lp')
    stage('examples/one_cat_arrow_diagrams.lp')
    stage('examples/one_cat_modifications.lp')
    (package / 'one_cat_arrow_profile_controls.lp').write_text(
        'require open emdash.examples.one_cat_arrow_diagrams;\n'
        + fragment('production_one_cat_arrow_controls.lpfragment'))
    stage('emdash3_2_one_cat_hom_comparison_data.lp')
    stage('examples/one_cat_hom_comparison_data.lp')
    stage('examples/one_cat_adjunction_introduction.lp')
    original_checks = subprocess.check_output(
        ['git', 'show', PIN + ':emdash2/emdash3_2_checks.lp'], cwd=root, text=True)
    psss_start = '// catalog-area: Cat-valued presheaf facade and restriction'
    psss_end = '/* End of the PSSS-02 higher-sieve diagnostics. */'
    assert original_checks.count(psss_start) == original_checks.count(psss_end) == 1
    psss = original_checks[original_checks.index(psss_start):original_checks.index(psss_end)+len(psss_end)]
    original_psss = psss
    psss = psss.replace('Cat_cat', 'Cat_cart')
    postcomp = '@hom_con_int_postcomp_func K K (@id_func K) V U p'
    assert psss.count(postcomp) == 2
    psss = psss.replace(postcomp, '@strict_transfor _ _ _ _ (' + postcomp + ')')
    higher_sieve_comparison = '''(@HigherSieve_cat K U)
      (@Catd_cat (@Into_restr_cat K U))'''
    assert psss.count(higher_sieve_comparison) == 1
    psss = psss.replace(higher_sieve_comparison, '''(@HigherSieve_cat K U)
      (Functor_cart_cat (@Into_restr_cat K U) Cat_cart)''', 1)
    psss = psss.replace('// Both higher-sieve presentations compare to this stable Catd intermediary.',
        '// The varying-base classifier has Cartesian diagram maps; the ordinary\n// presheaf facade retains its separate lax-map category.')
    psss = psss.replace('// Experimental unifiers are not transitively chained at runtime.',
        '// These categories have different mapping profiles, while their objects agree.')
    psss = psss.replace('// Restriction of higher sieves reuses Catd pullback along the arrow-total map.',
        '// Restriction of higher sieves is Cartesian precomposition along the arrow-total map.')
    pullback = '''@Pullback_catd_func
      (@Into_restr_cat K V)
      (@Into_restr_cat K U)
      (@fapp1_fapp0 K Cat_cart (@arrow_into_catd K) V U p)'''
    assert psss.count(pullback) == 1
    psss = psss.replace(pullback, '''@comp_cat_con_cart_func
      (@Into_restr_cat K V) (@Into_restr_cat K U) Cat_cart
      (@fapp1_fapp0 K Cat_cart (@arrow_into_catd K) V U p)''', 1)
    (package / 'presheaf_profile_controls.lp').write_text(
        'require open emdash.emdash3_2_presheaves;\n' + psss + '\n'
        + fragment('production_presheaf_profile_controls.lpfragment'))
    changes.append({'source': 'emdash3_2_checks.lp/PSSS-01/PSSS-02',
                    'owner': 'original presheaf and higher-sieve diagnostics',
                    'reason': 'Preserve the raw presheaf facade; use actual Cartesian inclusion for Yoneda and the selected Cartesian higher-sieve classifier/restriction, with explicit ordinary inclusion and directed-filler controls',
                    'oldBodySha256': sha(original_psss), 'newBodySha256': sha(psss)})
    sieve_start = '// catalog-area: Ordinary subterminal sieves and pullback'
    sieve_end = '/* End of the PSSS-03a ordinary-sieve diagnostics. */'
    assert original_checks.count(sieve_start) == original_checks.count(sieve_end) == 1
    sieve_controls = original_checks[original_checks.index(sieve_start):original_checks.index(sieve_end)+len(sieve_end)]
    assert sieve_controls.count('Cat_cat') == 1
    sieve_controls = sieve_controls.replace('Cat_cat', 'Cat_cart')
    (package / 'sieve_profile_controls.lp').write_text(
        'require open emdash.emdash3_2_sieves;\n' + psss + '\n' + sieve_controls + '\n'
        + fragment('production_presheaf_profile_controls.lpfragment'))
    introduction_source = (package / 'emdash3_2_one_cat_adjunction_introduction.lp').read_text()
    prefix_end = 'protected symbol intro_unit_original_identity_path'
    assert introduction_source.count(prefix_end) == 1
    introduction_prefix = introduction_source[:introduction_source.index(prefix_end)]
    dependency = 'require open emdash.emdash3_2_one_cat_hom_comparison_data;'
    assert introduction_prefix.count(dependency) == 1
    (package / 'adjunction_introduction_views_prefix.lp').write_text(
        introduction_prefix.replace(dependency,
            'require open emdash.emdash3_2_prof_defiso_evaluation_paths;', 1))
    (package / 'hom_action_admission_controls.lp').write_text(
        'require open emdash.emdash3_2_one_cat_transfor_profiles;\n'
        + fragment('production_one_cat_hom_action_admission.lpfragment') + '\n'
        + fragment('production_one_cat_hom_action_controls.lpfragment'))
    (package / 'lax_curry_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + fragment('production_lax_curry_hom_views.lpfragment') + '\n'
        + fragment('production_lax_curry_controls.lpfragment'))
    hom_comparison_source = (package / 'emdash3_2_one_cat_hom_comparison_data.lp').read_text()
    def source_slice(start, end):
        assert hom_comparison_source.count(start) == 1, start
        assert hom_comparison_source.count(end) == 1, end
        a = hom_comparison_source.index(start)
        return hom_comparison_source[a:hom_comparison_source.index(end, a)]
    (package / 'hom_comparison_curry_path_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + fragment('production_lax_curry_hom_views.lpfragment') + '\n'
        + source_slice('protected symbol hom_comparison_pair_tele_func', 'protected symbol one_cat_hom_action_source')
        + source_slice('symbol profmap_internal_hom_action', '// η:id_A⇒GF')
        + source_slice('protected symbol hom_comparison_pair_tele_identity_path', 'protected symbol hom_comparison_admitted_hom_action_component_path'))
    (package / 'hom_comparison_admitted_path_controls.lp').write_text(
        'require open emdash.emdash3_2_one_cat_transfor_profiles;\n'
        + fragment('production_one_cat_hom_action_admission.lpfragment') + '\n'
        + fragment('production_lax_curry_hom_views.lpfragment') + '\n'
        + source_slice('symbol profmap_internal_hom_action', '// η:id_A⇒GF')
        + source_slice('protected symbol hom_comparison_pair_tele_identity_path', 'symbol one_cat_hom_comparison_unit_component_path'))
    graph_source = (package / 'emdash3_2_represented_comma_families.lp').read_text()
    graph_boundary = '// Fibrewise Sigma of the existing whole internal action.'
    assert graph_source.count(graph_boundary) == 1
    (package / 'comma_graph_family_prefix.lp').write_text(graph_source[:graph_source.index(graph_boundary)])
    sigma_boundary = '// Pointwise opposite turns that whole transformation into the displayed map'
    assert graph_source.count(sigma_boundary) == 1
    (package / 'comma_graph_sigma_prefix.lp').write_text(graph_source[:graph_source.index(sigma_boundary)]
        + '\n' + fragment('production_comma_graph_sigma_control.lpfragment'))
    middle_boundary = '// The represented C-family at the varying source F[x].'
    assert graph_source.count(middle_boundary) == 1
    (package / 'comma_graph_middle_prefix.lp').write_text(graph_source[:graph_source.index(middle_boundary)]
        + '\n' + fragment('production_comma_graph_middle_controls.lpfragment'))
    basechange_boundary = 'protected symbol comma_graph_target_sec [B C : Cat]'
    assert graph_source.count(basechange_boundary) == 1
    (package / 'comma_graph_basechange_prefix.lp').write_text(graph_source[:graph_source.index(basechange_boundary)])
    total_boundary = '// The actual whole input classifier.'
    assert graph_source.count(total_boundary) == 1
    (package / 'comma_graph_total_prefix.lp').write_text(graph_source[:graph_source.index(total_boundary)]
        + '\n' + fragment('production_comma_graph_total_controls.lpfragment'))
    constructor_boundary = '// Whole source projection with its original inverse data.'
    assert graph_source.count(constructor_boundary) == 1
    (package / 'represented_comma_constructor_prefix.lp').write_text(graph_source[:graph_source.index(constructor_boundary)]
        + '\n' + fragment('production_represented_comma_constructor_controls.lpfragment'))
    source_boundary = '// Extract the actual target section before taking the outer opposite.'
    assert graph_source.count(source_boundary) == 1
    source_controls = (baseline_package / 'examples/represented_comma_families.lp').read_text()
    source_controls = source_controls.split('assert [A K : Cat]', 1)[0]
    source_controls = source_controls.replace('require open emdash.emdash3_2_represented_comma_families;', '')
    assert source_controls.count('Op_cat') == 11 and source_controls.count('Op_func') == 4
    # Only the original arbitrary-section negative has Op here: its total
    # projection is now O. All seven positive observations are unchanged.
    source_controls = source_controls.replace('Op_cat', 'TotalOp_cat').replace('Op_func', 'TotalOp_func')
    (package / 'represented_comma_source_prefix.lp').write_text(graph_source[:graph_source.index(source_boundary)]
        + '\n' + source_controls + '\n' + fragment('production_total_dual_projection_controls.lpfragment'))
    target_section_boundary = '// Link that section to the original total base change.'
    assert graph_source.count(target_section_boundary) == 1
    (package / 'represented_comma_target_section_prefix.lp').write_text(graph_source[:graph_source.index(target_section_boundary)])
    target_inverse_boundary = '// Group the original mapped graph section.'
    assert graph_source.count(target_inverse_boundary) == 1
    (package / 'represented_comma_target_inverse_prefix.lp').write_text(graph_source[:graph_source.index(target_inverse_boundary)])
    # These original assertions exercise the assembly owner itself. Keep the
    # full original downstream import closure staged as a separate obligation.
    assembly_controls = (package / 'examples/action_profile_inherited_assembly_controls.lp').read_text()
    imports = 'require open emdash.emdash3_2_direct_cover_completion_locality;\nrequire open emdash.emdash3_2_gray_profiles;'
    assert assembly_controls.count(imports) == 1
    (package / 'pointwise_assembly_controls.lp').write_text(assembly_controls.replace(
        imports, 'require open emdash.emdash3_2_strict_pointwise_equivalences;', 1)
        + '\n' + fragment('production_pointwise_coefficient_control.lpfragment'))
    (package / 'internal_x_profile_controls.lp').write_text(
        'require open emdash.emdash3_2_gray_profiles;\n'
        + fragment('production_internal_x_profile_controls.lpfragment'))
    (package / 'sigma_parameter_profile_controls.lp').write_text(
        'require open emdash.emdash3_2_gray_profiles;\n'
        + fragment('production_sigma_parameter_profile_controls.lpfragment'))
    (package / 'sigma_basechange_coefficient_controls.lp').write_text(
        'require open emdash.emdash3_2_gray_profiles;\n'
        + fragment('production_sigma_basechange_coefficient_controls.lpfragment'))
    (package / 'sigma_constant_projection_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + fragment('production_sigma_constant_projection_controls.lpfragment'))
    (package / 'sigma_projection_regression_controls.lp').write_text(
        (package / 'inverse_core_controls.lp').read_text() + '\n'
        + fragment('production_sigma_constant_projection_controls.lpfragment'))
    (package / 'lax_curry_regression_controls.lp').write_text(
        (package / 'sigma_projection_regression_controls.lp').read_text() + '\n'
        + fragment('production_lax_curry_hom_views.lpfragment') + '\n'
        + fragment('production_lax_curry_controls.lpfragment'))
    (package / 'comma_target_guard_controls.lp').write_text(
        'require open emdash.emdash3_2_represented_comma_families;\n'
        'require emdash.examples.represented_comma_families;\n'
        + fragment('production_comma_target_guard_controls.lpfragment'))
    (package / 'prof_defiso_coefficient_controls.lp').write_text(
        'require open emdash.emdash3_2_prof_defiso_evaluation_paths;\n'
        'require emdash.examples.action_profile_prof_defiso_controls;\n'
        + fragment('production_cartesian_defiso_point_controls.lpfragment'))
    (package / 'diagram_evaluation_profile_controls.lp').write_text(
        'require open emdash.emdash3_2_diagram_evaluation;\n'
        'require emdash.examples.diagram_evaluation;\n'
        + fragment('production_diagram_evaluation_controls.lpfragment'))
    (package / 'diagram_evaluation_naturality_controls.lp').write_text(
        (package / 'emdash3_2_diagram_evaluation.lp').read_text() + '\n'
        + fragment('production_diagram_evaluation_naturality_controls.lpfragment'))
    (package / 'arrow_diagram_migration_controls.lp').write_text(
        'require open emdash.emdash3_2_arrow_diagram_families;\n'
        + fragment('production_arrow_diagram_controls.lpfragment'))
    (package / 'zero_arrow_migration_controls.lp').write_text(
        'require open emdash.emdash3_2_zero_arrow_diagrams;\n'
        'require open emdash.emdash3_2_strict_functor_actions;\n'
        + fragment('production_zero_arrow_controls.lpfragment'))
    (package / 'cubical_migration_controls.lp').write_text(''.join(
        'require open emdash.examples.' + name + ';\n' for name in (
            'cubical_dependent_hom', 'cubical_square_total',
            'cubical_internalization', 'cubical_internalization_composition')))
    (package / 'interchanger_controls.lp').write_text(
        'require open emdash.examples.gray_interchanger;\n'
        'require open emdash.examples.gray_interchanger_orientation;\n')
    # Use the actual byte-identical reviewer module. The former flattened
    # driver did not explain the runtime variability and is no longer needed.
    (package / 'weighted_migration_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        'require open emdash.emdash3_2_strict_functor_actions;\n'
        'require emdash.examples.profunctor_weighted_limits;\n\n'
        + fragment('production_weighted_colimit_controls.lpfragment') + '\n'
        + fragment('production_default_inverse_legacy_controls.lpfragment') + '\n'
        + fragment('production_default_inverse_controls.lpfragment'))
    # Same original reviewer assertions, isolated at their actual profile
    # owner. The original broader import closure remains staged and required.
    profile_controls = (package / 'examples/gray_profiles.lp').read_text()
    assert profile_controls.count('require open emdash.emdash3_2_represented_comma_families;') == 1
    (package / 'profile_controls.lp').write_text(profile_controls.replace(
        'require open emdash.emdash3_2_represented_comma_families;',
        'require open emdash.emdash3_2_gray_profiles;', 1))
    delta = difflib.SequenceMatcher(None, original.splitlines(keepends=True),
                                   body.splitlines(keepends=True), autojunk=False).get_opcodes()
    original_lines_retained = all(kind in ('equal', 'insert') for kind, *_ in delta)
    declaration = r'(?m)^(?:(?:constant|injective|protected|private)\s+)?symbol\s+([A-Za-z0-9_]+)\b'
    original_names = re.findall(declaration, original)
    relocated_names = {'Catd_cat_func', 'Catd_catd_con', 'FibCov_target_catd',
                       'FibCov_source_catd', 'fib_cov_int', 'fib_cov_src_func',
                       'fib_cov_transf', 'homd_src_func', 'homd_src_sec', 'homd_tgt_func',
                       'homd_id_src_sec', 'homd_id_tgt_func', 'Const_func_func'}
    retired_names = {'Homd_target_section_catd': 'Homd_target_section_cat',
                     'functord_transport_lhs_tele_agrees': 'functord_transport_rhs_tele_agrees',
                     'functord_transport_lhs_agrees': 'functord_transport_rhs_agrees'}
    for name in relocated_names:
        assert re.findall(declaration, body).count(name) == 1, name
    for name, replacement in retired_names.items():
        assert not re.findall(r'(?m)^(?:injective |constant )?symbol ' + name + r'\b', body)
        assert re.findall(declaration, body).count(replacement) == 1
    original_names = [name for name in original_names if name not in relocated_names and name not in retired_names]
    candidate_names = iter(re.findall(declaration, body))
    assert all(any(candidate == name for candidate in candidate_names)
               for name in original_names), 'An original declaration was dropped or reordered'
    inputs[str(Path(__file__).resolve().relative_to(root))] = sha(Path(__file__).read_text())
    manifest = {
        'status': 'staged full-source migration; generation does not establish qualification',
        'sourcePin': PIN, 'originalCoreSha256': CORE_SHA,
        'originalCoreLines': len(original.splitlines()), 'candidateCoreLines': len(body.splitlines()),
        'originalDownstreamSectionsRetained': True,
        'originalCoreLineOrderVerified': original_lines_retained,
        'originalNamedDeclarationsRetained': not retired_names,
        'unretiredNamedDeclarationsRetained': True,
        'retiredNamesWithReplacements': retired_names,
        'originalNamedDeclarationSequenceVerified': not relocated_names,
        'unrelocatedNamedDeclarationSequenceVerified': True,
        'namedDeclarationSequenceExceptions': sorted(relocated_names),
        'originalDependencyInputs': dependencies,
        'changes': changes, 'relocatedDeclarations': relocated,
        'authoringInputs': inputs,
        'outputs': {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in [out / 'baseline.lp', package / 'emdash3_2.lp',
                              package / 'emdash3_2_gray_profiles.lp', package / 'owner_controls.lp',
                              package / 'foundations_prefix.lp',
                              package / 'sections_prefix.lp',
                              package / 'sigma_prefix.lp',
                              package / 'mixed_prefix.lp',
                              package / 'homd_prefix.lp',
                              package / 'index_profile.lp',
                              package / 'intrinsic_identity_prefix.lp',
                              package / 'section_action_prefix.lp',
                              package / 'evaluation_prefix.lp',
                              package / 'structural_prefix.lp',
                              package / 'ordinary_structural_prefix.lp',
                              package / 'pullback_structural_prefix.lp',
                              package / 'section_pullback_prefix.lp',
                              package / 'intrinsic_composite_prefix.lp',
                              package / 'intrinsic_unit_prefix.lp',
                              package / 'profunctor_prefix.lp',
                              package / 'comma_prefix.lp',
                              package / 'pathout_controls.lp',
                              package / 'rule_hygiene_full_controls.lp',
                              package / 'inverse_core_controls.lp',
                              package / 'profile_controls.lp',
                              package / 'cubical_migration_controls.lp',
                              package / 'interchanger_controls.lp',
                              package / 'weighted_migration_controls.lp',
                              package / 'diagram_evaluation_profile_controls.lp',
                              package / 'diagram_evaluation_naturality_controls.lp',
                              package / 'arrow_diagram_migration_controls.lp',
                              package / 'zero_arrow_migration_controls.lp',
                              package / 'pointwise_assembly_controls.lp',
                              package / 'comma_graph_family_prefix.lp',
                              package / 'comma_graph_sigma_prefix.lp',
                              package / 'internal_x_profile_controls.lp',
                              package / 'sigma_parameter_profile_controls.lp',
                              package / 'comma_graph_middle_prefix.lp',
                              package / 'sigma_basechange_coefficient_controls.lp',
                              package / 'comma_graph_basechange_prefix.lp',
                              package / 'comma_graph_total_prefix.lp',
                              package / 'represented_comma_constructor_prefix.lp',
                              package / 'represented_comma_source_prefix.lp',
                              package / 'represented_comma_target_section_prefix.lp',
                              package / 'represented_comma_target_inverse_prefix.lp',
                              package / 'sigma_constant_projection_controls.lp',
                              package / 'sigma_projection_regression_controls.lp',
                              package / 'hom_action_admission_controls.lp',
                              package / 'lax_curry_controls.lp',
                              package / 'hom_comparison_curry_path_controls.lp',
                              package / 'hom_comparison_admitted_path_controls.lp',
                              package / 'lax_curry_regression_controls.lp',
                              package / 'adjunction_introduction_views_prefix.lp',
                              package / 'presheaf_profile_controls.lp',
                              package / 'sieve_profile_controls.lp',
                              package / 'comma_target_guard_controls.lp',
                              package / 'prof_defiso_coefficient_controls.lp',
                              baseline_package / 'emdash3_2.lp', baseline_package / 'emdash3_2_gray_profiles.lp']
                    + [package / path for path in dependencies]},
        'stillRequired': ['Coefficient/mixed-parameter compatibility at installed-rule overlaps and actual consumers, without requiring a general Q model',
                          'Profile-extension and original diagnostic/import-closure migration',
                          'Whole duality/adjunction and closure-consumer qualification',
                          'Downstream qualification and retirement of redundant strict-functor wrappers',
                          'Public promotion with catalog, health, CI and source-pin review'],
        'excluded': ['Auxiliary Sigma fibre-composition audit owner',
                     'Unrestricted Cartesian evaluation on lax transformations',
                     'Optional normalization redesign'],
    }
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted full pre-goal baseline and upstream owner migration; no original tail omitted.')


if __name__ == '__main__':
    main()
