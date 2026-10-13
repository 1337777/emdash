#!/usr/bin/env python3
"""Replay expanded local presentation inverses; no checker invocation."""
import hashlib
import json
from pathlib import Path


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    prior_path = audit / 'admission_next_verification.json'
    prior = json.loads(prior_path.read_text())
    source_path = root / 'tmp/probes/admission_next/staged_full_bridge.lp'
    source = source_path.read_text()
    digest = lambda data: hashlib.sha256(data).hexdigest()
    assert digest(source.encode()) == prior['outputs']['staged_full_bridge.lp']
    assert prior['checks']['staged_full_bridge.lp']['outcome'] == 'passed-fresh'
    swap_path = audit / 'local_inverse_swap_controls.lpfragment'
    controls_path = audit / 'local_cart_prof_inverse_boundary.lpfragment'
    swap = swap_path.read_text()
    term = swap[swap.index('  @fapp1_fapp0'):swap.index('\n  ≡ alpha;')].strip()
    nf = ('compute λ (A B C : Cat) (F G : τ (Functor (Product_cat A B) C))\n'
          '  (alpha : τ (@StrictTransfor (Product_cat A B) C F G)),\n  ' + term + ';\n')
    targets = {'baseline.lp': source + '\n' + controls_path.read_text(),
               'swap_boundary.lp': source + '\n' + swap,
               'swap_normal_form.lp': source + '\n' + nf}
    join_path = audit / 'local_inverse_swap_join.lpfragment'
    anchor = '// Whole operations, followed by both separately projected application orders.'
    assert source.count(anchor) == 1
    joined = source.replace(anchor, join_path.read_text() + '\n' + anchor)
    targets['joined_swap.lp'] = joined + '\n' + swap
    targets['joined_inverse.lp'] = joined + '\n' + swap + '\n' + controls_path.read_text()
    guarded_path = audit / 'local_inverse_swap_guarded.lpfragment'
    guarded = source.replace(anchor, guarded_path.read_text() + '\n' + anchor)
    targets['guarded_swap.lp'] = guarded + '\n' + swap
    targets['guarded_inverse.lp'] = guarded + '\n' + swap + '\n' + controls_path.read_text()
    extra_path = audit / 'local_inverse_controls.lpfragment'
    targets['selected_controls.lp'] = targets['guarded_inverse.lp'] + '\n' + extra_path.read_text()
    targets['without_swap_join.lp'] = targets['selected_controls.lp'].replace(guarded_path.read_text(), '')
    extra = extra_path.read_text()
    identity_term = extra[extra.index('  @fapp1_fapp0'):extra.index('\n  ≡ @id')].strip()
    targets['identity_normal_form.lp'] = guarded + '\ncompute λ (A B : Cat) (P : τ (Prof B A)),\n  ' + identity_term + ';\n'
    identity_join_path = audit / 'local_inverse_swap_identity.lpfragment'
    joined_identity = guarded.replace(anchor, identity_join_path.read_text() + '\n' + anchor)
    targets['identity_join_controls.lp'] = joined_identity + '\n' + swap + '\n' + controls_path.read_text() + '\n' + extra
    perturb_path = audit / 'local_inverse_perturbed_controls.lpfragment'
    typed_identity_path = audit / 'local_inverse_swap_identity_guarded.lpfragment'
    typed_identity = joined_identity.replace(identity_join_path.read_text(), typed_identity_path.read_text())
    targets['final_controls.lp'] = typed_identity + '\n' + swap + '\n' + controls_path.read_text() + '\n' + extra + '\n' + perturb_path.read_text()
    targets['final_without_swap.lp'] = targets['final_controls.lp'].replace(guarded_path.read_text(), '')
    targets['final_without_identity.lp'] = targets['final_controls.lp'].replace(typed_identity_path.read_text(), '')
    object_join_path = audit / 'local_inverse_swap_object.lpfragment'
    object_anchor = '// Opposite of product swap is swap between the opposite factors.'
    assert targets['final_controls.lp'].count(object_anchor) == 1
    targets['object_join_controls.lp'] = targets['final_controls.lp'].replace(object_anchor, object_join_path.read_text() + '\n' + object_anchor)
    # The historical arbitrary-H comparison has different dependent endpoint
    # types, so assertnot cannot express it. Keep its failed source, and use
    # the separately typed same-endpoint variable-theta control instead.
    invalid_control = extra[extra.index('// One arbitrary reindex map'):]
    assert targets['object_join_controls.lp'].count(invalid_control) == 1
    targets['qualified_controls.lp'] = targets['object_join_controls.lp'].replace(invalid_control, '')
    for name, fragment in [('swap', guarded_path), ('identity', typed_identity_path), ('object', object_join_path)]:
        assert targets['qualified_controls.lp'].count(fragment.read_text()) == 1
        targets['qualified_without_' + name + '.lp'] = targets['qualified_controls.lp'].replace(fragment.read_text(), '')
    horizontal_path = audit / 'local_inverse_horizontal_identity.lpfragment'
    identity_anchor = '// Identity pair of transfors collapses to the identity on the composite functor.'
    identity_end = '// 6c. Constant/opposite transfors and Cat-valued composition projections'
    assert guarded.count(identity_anchor) == guarded.count(identity_end) == 1
    start = guarded.index(identity_anchor)
    end = guarded.index(identity_end, start)
    old_horizontal = guarded[start:end]
    minimal = guarded[:start] + horizontal_path.read_text() + '\n' + guarded[end:]
    valid_controls = swap + '\n' + controls_path.read_text() + '\n' + extra.replace(invalid_control, '') + '\n' + perturb_path.read_text()
    targets['minimal_controls.lp'] = minimal + '\n' + valid_controls
    targets['minimal_without_identity_change.lp'] = guarded + '\n' + valid_controls
    targets['minimal_without_swap.lp'] = targets['minimal_controls.lp'].replace(guarded_path.read_text(), '')
    pair_identity_path = audit / 'local_inverse_horizontal_identity_pairs.lpfragment'
    targets['pair_identity_controls.lp'] = targets['minimal_controls.lp'].replace(horizontal_path.read_text(), pair_identity_path.read_text())
    interaction_path = audit / 'local_inverse_interaction_controls.lpfragment'
    targets['interaction_controls.lp'] = targets['qualified_controls.lp'] + '\n' + interaction_path.read_text()
    interaction = interaction_path.read_text()
    marker = '// Endpoint equal to a stable precomposition; use an actual identity map.'
    early, last = interaction.split(marker)
    targets['interaction_prefix.lp'] = targets['qualified_controls.lp'] + '\n' + early
    header, body = last.split('⊢\n', 1)
    lhs, rhs = body.split('\n  ≡ ', 1)
    rhs = rhs.strip().removesuffix(';')
    typ = '''(@StrictTransfor (Product_cat A B) D
      (fapp0 (@comp_cat_con_cart_func (Product_cat A B) C D H) F)
      (fapp0 (@comp_cat_con_cart_func (Product_cat A B) C D H) F))'''
    comparison = header + '⊢\n  @eq_refl ' + typ + '\n    (' + lhs.strip() + ')\n  : τ (@= ' + typ + '\n    (' + lhs.strip() + ')\n    (' + rhs + '));\n'
    targets['interaction_comparison.lp'] = targets['interaction_prefix.lp'] + '\n' + comparison
    output = root / 'tmp/probes/local_inverse'
    output.mkdir(parents=True, exist_ok=True)
    for name, text in targets.items():
        (output / name).write_text(text)
    package = (root / 'lambdapi.pkg').read_bytes()
    (output / 'lambdapi.pkg').write_bytes(package)
    inputs = [Path(__file__), prior_path, source_path, swap_path, controls_path, join_path, guarded_path, extra_path, identity_join_path, typed_identity_path, perturb_path, object_join_path, horizontal_path, pair_identity_path, interaction_path, root / 'lambdapi.pkg']
    manifest = {'status': 'non-library authoring replay; qualification separate',
                'sourceInputs': {str(p.relative_to(root)): digest(p.read_bytes()) for p in inputs},
                'outputs': {name: digest(text.encode()) for name, text in targets.items()}}
    manifest['outputs']['lambdapi.pkg'] = digest(package)
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print('Prepared expanded local inverse and independent swap boundaries; no checker run.')


if __name__ == '__main__':
    main()
