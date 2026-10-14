#!/usr/bin/env python3
"""Emit owner-position conventional-lax default candidates and controls.

NON-LIBRARY. Prefixes test native ordinary action; the full-source variants
retain known legacy duality/Cartesian defects and test only the selected
intrinsic-cell owner. No output qualifies the whole migrated foundation.
"""
import hashlib
import json
from pathlib import Path
import subprocess


def digest(s):
    return hashlib.sha256(s.encode()).hexdigest()


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    pin = 'f8af1fca472657ff1598c639eb29c0566e7b2ec0'
    source = subprocess.check_output(
        ['git', 'show', pin + ':emdash2/emdash3_2.lp'], cwd=root, text=True)
    expected = '6a980df34be718a23a6be121d170153650830a49f54b7e0eca415705ffb2068a'
    assert digest(source) == expected
    fragments = {name: (audit / name).read_text() for name in (
        'composition_rule.lpfragment', 'whole_rules.lpfragment',
        'projected_rules.lpfragment', 'conventional_lax_rules.lpfragment',
        'conventional_lax_intrinsic.lpfragment', 'conventional_lax_controls.lpfragment')}

    capped_owner = '/*\n  The former capped composition cut and detached all-components law are\n'
    whole_owner = '/*\n  The former whole post/left and pre/right strict-functoriality accumulation\n'
    prefix_end = '// Cat instance of product-composition arrow action.'
    for anchor in (capped_owner, whole_owner, prefix_end):
        assert source.count(anchor) == 1
    strict = source.replace(capped_owner,
        fragments['composition_rule.lpfragment'] + '\n' + capped_owner)

    # Exact unchanged identity clauses move into the prefix after tapp1 exists.
    units = '''// Unchanged capped identity projections, relocated for this prefix.
rule @tapp1_fapp0 $A $B _ _ $X $Y (@id (Functor_cat $A $B) $F) $p
  ↪ @fapp1_fapp0 $A $B $F $X $Y $p;
rule @tapp1_fapp0 $A $B $F $G $X $X $ϵ (@id $A $X)
  ↪ @tapp0_fapp0 $A $B $F $G $X $ϵ;
'''
    for rule in units.split('rule ')[1:]:
        assert 'rule ' + rule.strip() in source

    prefix = strict[:strict.index(prefix_end)]
    op_start = prefix.index('// Internalized opposite as a functor in Cat.')
    op_end = prefix.index('constant symbol Functor_cat_func', op_start)
    removed_universe_op = prefix[op_start:op_end]
    prefix = prefix[:op_start] + prefix[op_end:]
    legacy_prefix = prefix
    start = prefix.index('/*\n  Opposite of an ordinary transfor.')
    end = prefix.index('// 6b. Internalized hom endpoint actions', start)
    removed_transfor = prefix[start:end]
    prefix = prefix[:start] + prefix[end:]
    start = prefix.index('// Opposite transfor off-diagonal action swaps the base endpoints.')
    removed_op_action = prefix[start:]
    prefix = prefix[:start]
    assert 'Op_transf' not in prefix

    whole = (fragments['whole_rules.lpfragment'] + '\n'
             + fragments['projected_rules.lpfragment'])
    ordinary = fragments['conventional_lax_rules.lpfragment']
    controls = fragments['conventional_lax_controls.lpfragment']
    baseline_controls = controls.replace('// PRE-POSITIVE\nassert ',
                                        '// PRE-POSITIVE\nassertnot ')
    assert controls.count('// PRE-POSITIVE\nassert ') == 4

    adverse = '''// ADVERSE: the old same-profile transpose turns pre strictness
// into a post equality. No supplied equality/naturality evidence is input.
symbol conventional_lax_pre_eq [A B : Cat] [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G)) [x y : τ (Obj A)] (p : τ (Hom A x y))
  : τ (@= (Hom B (fapp0 F x) (fapp0 G y))
      (@comp_fapp0 B _ _ _
        (@tapp0_fapp0 A B F G y epsilon) (@fapp1_fapp0 A B F x y p))
      (@tapp1_fapp0 A B F G x y epsilon p))
≔ @eq_refl (Hom B (fapp0 F x) (fapp0 G y))
    (@tapp1_fapp0 A B F G x y epsilon p);

symbol conventional_lax_legacy_post_eq [A B : Cat] [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G)) [x y : τ (Obj A)] (p : τ (Hom A x y))
  : τ (@= (Hom B (fapp0 F x) (fapp0 G y))
      (@comp_fapp0 B _ _ _
        (@fapp1_fapp0 A B G x y p) (@tapp0_fapp0 A B F G x epsilon))
      (@tapp1_fapp0 A B F G x y epsilon p))
≔ @eq_ap
    (Hom (Op_cat B) (@fapp0 A B G y) (@fapp0 A B F x))
    (Hom B (@fapp0 A B F x) (@fapp0 A B G y))
    (λ z : τ (Hom (Op_cat B) (@fapp0 A B G y) (@fapp0 A B F x)), z)
    _ _
    (@conventional_lax_pre_eq (Op_cat A) (Op_cat B)
      (@Op_func A B G) (@Op_func A B F)
      (@Op_transf A B F G epsilon) y x p);
'''

    intrinsic_controls = '''// The selected identity is the existing extracted whole pre cell.
assert [A B : Cat] [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G)) (Y : τ (Obj A))
  [W X : τ (Obj A)] (h : τ (Hom A W X)) ⊢
  @tapp1_pre_laxity_transf A B F G epsilon Y W X h
  ≡ @id
      (Functor_cat (Hom_cat A X Y) (Hom_cat B (fapp0 F W) (fapp0 G Y)))
      (@functord_transport_lhs_func (Op_cat A)
        (@hom_con A Y A (@id_func A))
        (@hom_con B (@fapp0 A B G Y) A F)
        (@tapp1_con_at_transf A B F G epsilon Y) X W h);

// The other whole comparison still comes from the native intrinsic owner.
assert [A B : Cat] [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G)) (X : τ (Obj A))
  [Y Z : τ (Obj A)] (g : τ (Hom A Y Z)) ⊢
  @tapp1_post_laxity_transf A B F G epsilon X Y Z g
  ≡ @fdapp1_comma_projection_transf A
      (@hom_ A A (@id_func A) X)
      (@hom_ B A G (@fapp0 A B F X))
      (@tapp1_at_transf A B F G X epsilon)
      (@fdapp1_int_transfd A
        (@hom_ A A (@id_func A) X)
        (@hom_ B A G (@fapp0 A B F X))
        (@tapp1_at_transf A B F G X epsilon)) Y Z g;

assertnot [A B : Cat] [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G)) (X : τ (Obj A))
  [Y Z : τ (Obj A)] (g : τ (Hom A Y Z)) ⊢
  @id
      (Functor_cat (Hom_cat A X Y) (Hom_cat B (fapp0 F X) (fapp0 G Z)))
      (@functord_transport_lhs_func A
        (@hom_ A A (@id_func A) X)
        (@hom_ B A G (@fapp0 A B F X))
        (@tapp1_at_transf A B F G X epsilon) Y Z g)
  : τ (@Transf (Hom_cat A X Y) (Hom_cat B (fapp0 F X) (fapp0 G Z))
      (@functord_transport_lhs_func A
        (@hom_ A A (@id_func A) X)
        (@hom_ B A G (@fapp0 A B F X))
        (@tapp1_at_transf A B F G X epsilon) Y Z g)
      (@functord_transport_rhs_func A
        (@hom_ A A (@id_func A) X)
        (@hom_ B A G (@fapp0 A B F X))
        (@tapp1_at_transf A B F G X epsilon) Y Z g));
'''
    full = strict.replace(whole_owner, whole + '\n' + ordinary + '\n' + whole_owner)
    intrinsic_owner = '// Whole post/left ordinary laxity.'
    assert full.count(intrinsic_owner) == 1
    with_intrinsic = full.replace(intrinsic_owner,
        fragments['conventional_lax_intrinsic.lpfragment'] + '\n' + intrinsic_owner)

    variants = {
        'baseline.lp': prefix + units + whole + '\n' + baseline_controls,
        'ordinary.lp': prefix + units + whole + '\n' + ordinary + '\n' + controls,
        'no_pre.lp': prefix + units + whole + '\n' + controls,
        'legacy_op_adverse.lp': legacy_prefix + units + whole + '\n' + ordinary + '\n' + adverse,
        'full_intrinsic.lp': with_intrinsic + '\n' + controls + '\n' + intrinsic_controls,
        'full_without_cell.lp': full + '\n' + controls + '\n' + intrinsic_controls,
    }
    output = root / 'tmp/probes/conventional_lax_default'
    output.mkdir(parents=True, exist_ok=True)
    for name, body in variants.items():
        (output / name).write_text(body)
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    manifest = {
        'status': 'unqualified native candidates; run probes and record outcomes',
        'sourcePin': pin, 'sourceSha256': expected,
        'authoringInputs': {name: digest(body) for name, body in fragments.items()},
        'builderSha256': digest(Path(__file__).read_text()),
        'removedFromOrdinaryPrefix': {
            'oldCovariantUniverseOp': removed_universe_op,
            'oldSameProfileTransposeTransfor': removed_transfor,
            'oldSameProfileTransposeAction': removed_op_action},
        'relocatedIdentityRules': units,
        'outputs': {name: digest(body) for name, body in variants.items()},
        'qualification': [
            'The prefix omits the invalid same-profile transpose; it is not a new implementation of its replacement.',
            'The full-source variants retain known legacy Op and Cartesian assumptions and qualify only the selected intrinsic-cell owner.',
            'No Cartesian public-universe substitution, profile input, or independent laxity witness is introduced.'],
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted conventional-lax ordinary and intrinsic owner candidates.')


if __name__ == '__main__':
    main()
