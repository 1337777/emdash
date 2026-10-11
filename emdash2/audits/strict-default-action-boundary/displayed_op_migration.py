#!/usr/bin/env python3
"""Owner-position Cartesian displayed transpose over the pinned duality stage.

NON-LIBRARY. This qualifies the Cartesian part only. The unchanged general
FF consumers remain in the full file and must receive their coupled Homd
repair; a passing prefix is not their replacement or a narrowed milestone.
"""
import hashlib
import json
from pathlib import Path
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'duality_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_duality'
    prior = json.loads((audit / 'duality_migration_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']

    def replace(old, new):
        nonlocal source
        assert source.count(old) == 1, (old, source.count(old))
        source = source.replace(old, new)

    replace('''injective symbol Op_catd_func (Z : Cat)
  : τ (Functor (CoAt2_cat (Functor_cart_cat Z Cat_cat))
      (Catd_cat (CoAt2_cat Z)));''', '''injective symbol Op_catd_func (Z : Cat)
  : τ (Functor (CoAt2_cat (Functor_cart_cat Z Cat_cat))
      (Functor_cart_cat (CoAt2_cat Z) Cat_cat));''')

    replace('''// Whole formation pipeline for the corrected opposite-family operator.
rule @comp_fapp0 Cat_cat _ _ _
      (@comp_fapp0 Cat_cat _ _ _
        (@fapp1_fapp0 Cat_cat Cat_cat
          (Functor_cat_fapp0_func (CoAt2_cat $K)) (CoAt2_cat Cat_cat) Cat_cat op)
        (cart_functor_include (CoAt2_cat $K) (CoAt2_cat Cat_cat)))
      (CoAt2_func_func $K Cat_cat)
  ↪ Op_catd_func $K;''', '''// Whole formation uses the original Cat-Hom postcomposition derivation.
// Both parameter categories now retain their Cartesian transformation profile.
rule @comp_fapp0 Cat_cat _ _ _
      (@hom_postcomp_func Cat_cat Cat_cat (@id Cat_cat Cat_cat)
        (CoAt2_cat $K) (CoAt2_cat Cat_cat) Cat_cat op)
      (CoAt2_func_func $K Cat_cat)
  ↪ Op_catd_func $K;''')

    # Retain the earlier controls while correcting the explicitly strengthened
    # E-parameter target. The family objects and their base action are unchanged.
    controls = (audit / 'duality_family_controls.lpfragment').read_text()
    prefix = controls.index('assert (K : Cat)')
    formation = '''// NON-LIBRARY: Cartesian formation of the same shifted family.
symbol sf_op_family_formation (K : Cat)
  : τ (Functor (CoAt2_cat (Functor_cart_cat K Cat_cat))
      (Functor_cart_cat (CoAt2_cat K) Cat_cat))
≔ @comp_cat_fapp0
    (CoAt2_cat (Functor_cart_cat K Cat_cat))
    (Functor_cart_cat (CoAt2_cat K) (CoAt2_cat Cat_cat))
    (Functor_cart_cat (CoAt2_cat K) Cat_cat)
    (@comp_cat_cov_cart_func (CoAt2_cat K) (CoAt2_cat Cat_cat) Cat_cat op)
    (CoAt2_func_func K Cat_cat);
'''
    revised = formation + controls[prefix:]
    revised = revised.replace('(Catd_cat (CoAt2_cat K))',
                              '(Functor_cart_cat (CoAt2_cat K) Cat_cat)')
    replace(controls, revised)

    # The old same-profile action is not meaningful on an arbitrary FF.
    # Keep the scope limitation explicit in the emitted source; later generic
    # users are deliberately retained, not deleted to make a prefix look green.
    start = source.index('// Fixed-base layer: pointwise opposite of a displayed functor.')
    end = source.index('// Pointwise projection of displayed composition.', start)
    action = (audit / 'displayed_op_cartesian.lpfragment').read_text() + '\n'
    controls = (audit / 'displayed_op_cartesian_controls.lpfragment').read_text() + '\n'
    no_join = source[:start] + action + controls + source[end:]
    source = (source[:start] + action
              + (audit / 'displayed_op_projection_joins.lpfragment').read_text() + '\n'
              + controls + source[end:])

    output = root / 'tmp/probes/strict_default_displayed_op'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'emdash3_2.lp').write_text(source)
    (output / 'owner_prefix.lp').write_text(
        source[:source.index('// Pointwise projection of displayed composition.')])
    (output / 'no_projection_join.lp').write_text(
        no_join[:no_join.index('// Pointwise projection of displayed composition.')])
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    files = ('displayed_op_migration.py', 'displayed_op_cartesian.lpfragment',
             'displayed_op_projection_joins.lpfragment',
             'displayed_op_cartesian_controls.lpfragment', 'op_funcd_profile_model.py')
    manifest = {
        'status': 'non-library Cartesian action; general-FF and Homd integration remain open',
        'dualityInputSha256': prior['outputs']['emdash3_2.lp'],
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in files},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in ('emdash3_2.lp', 'owner_prefix.lp', 'no_projection_join.lp', 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted Cartesian displayed-transpose owner and full-file continuation.')


if __name__ == '__main__':
    main()
