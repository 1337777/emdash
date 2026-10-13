#!/usr/bin/env python3
"""Emit generic proof-time owners for the nested identity inverse; no checker.

Runtime composition, precomposition, and the checked product-swap inverse
rules remain unchanged. The actual runtime inverse remains a separate
positive boundary; it is not relabelled as a passing negative.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re


FRAGMENTS = (
    'inverse_nested_precomp_comparison.lpfragment',
    'inverse_nested_horizontal_comparison.lpfragment',
    'inverse_nested_precomp_controls.lpfragment',
    'inverse_nested_horizontal_controls.lpfragment',
    'inverse_nested_controls.lpfragment',
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def insert_before(source, anchor, body):
    assert source.count(anchor) == 1, ('non-unique owner anchor', anchor)
    return source.replace(anchor, body + '\n' + anchor)


def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    pin_path = audit / 'inverse_nested_inputs.json'
    pins = json.loads(pin_path.read_text())
    for name, expected in pins['sourceInputs'].items():
        assert digest((root / name).read_bytes()) == expected, (name, 'source pin changed')
    donor = root / pins['donor']
    source = donor.read_text()
    prior_path = audit / 'coefficient_assembly_verification.json'
    prior = json.loads(prior_path.read_text())
    assert digest(source.encode()) == prior['outputs'][donor.name]
    assert prior['checks'][donor.name]['outcome'] == 'passed-fresh'
    assert source.count('symbol local_inverse_swap_action ') == 1
    assert source.count('symbol local_inverse_perturbed_swap ') == 1
    f = {name: (audit / name).read_text() for name in FRAGMENTS}
    pre = f['inverse_nested_precomp_comparison.lpfragment']
    horizontal = f['inverse_nested_horizontal_comparison.lpfragment']
    for name, body in f.items():
        assert not re.search(r'(?m)^(?:rule|(?:injective |constant )?symbol)\b', body), name
        expected = 1 if name.endswith('_comparison.lpfragment') else 0
        assert len(re.findall(r'(?m)^unif_rule\b', body)) == expected, name
    pre_anchor = '/*\n  Propositional join for postcomposition outside stable precomposition:'
    horizontal_anchor = '// 6c. Constant/opposite transfors and Cat-valued composition projections'
    pre_source = insert_before(source, pre_anchor, pre)
    horizontal_source = insert_before(source, horizontal_anchor, horizontal)
    both = insert_before(pre_source, horizontal_anchor, horizontal)
    controls = f['inverse_nested_controls.lpfragment']
    runtime_path = audit / 'local_inverse_interaction_controls.lpfragment'
    old_controls = runtime_path.read_text()
    marker = '// Endpoint equal to a stable precomposition; use an actual identity map.'
    assert old_controls.count(marker) == 1
    runtime = old_controls[old_controls.index(marker):]
    body = runtime.split('⊢\n', 1)[1]
    left, right = body.split('\n  ≡ ', 1)
    right = right.strip().removesuffix(';')
    query_context = ('compute λ (A B C D : Cat) (H : τ (Functor (Product_cat A B) C))\n'
                     '  (F : τ (Functor C D)),\n  ')
    normal_forms = query_context + left.strip() + ';\n\n' + query_context + right + ';\n'
    targets = {
        'owner_prefix.lp': both,
        'precomp_baseline.lp': source + '\n' + f['inverse_nested_precomp_controls.lpfragment'],
        'precomp_candidate.lp': pre_source + '\n' + f['inverse_nested_precomp_controls.lpfragment'],
        'horizontal_baseline.lp': source + '\n' + f['inverse_nested_horizontal_controls.lpfragment'],
        'horizontal_candidate.lp': horizontal_source + '\n' + f['inverse_nested_horizontal_controls.lpfragment'],
        'nested_baseline.lp': source + '\n' + controls,
        'nested_comparison.lp': both + '\n' + controls,
        'without_precomp_comparison.lp': horizontal_source + '\n' + controls,
        'without_horizontal_comparison.lp': pre_source + '\n' + controls,
        'runtime_boundary.lp': both + '\n' + runtime,
        'normal_forms.lp': both + '\n' + normal_forms,
    }
    package = (root / 'lambdapi.pkg').read_bytes()
    paths = [Path(__file__).resolve(), pin_path, prior_path, donor, runtime_path, root / 'lambdapi.pkg']
    paths += [audit / name for name in FRAGMENTS]
    manifest = {
        'status': 'unchecked non-library proof-time nested inverse experiment; runtime boundary separate',
        'sourceInputs': {str(p.relative_to(root)): digest(p.read_bytes()) for p in paths},
        'donor': str(donor.relative_to(root)),
        'donorReceipt': prior['checks'][donor.name]['receipt'],
        'outputs': {name: digest(body.encode()) for name, body in targets.items()},
        'outputControlCounts': {name: {
            'positive': len(re.findall(r'(?m)^assert\b', body)),
            'negative': len(re.findall(r'(?m)^assertnot\b', body)),
        } for name, body in targets.items()},
        'qualification': [
            'Only two generic proof-time comparisons are added at existing precomposition/horizontal-identity owners.',
            'No runtime identity-pair rule is loosened; the two earlier subject-reduction failures stay in predecessor evidence.',
            'Both actual source and target endpoint pairs are constrained against the two identity-cell objects; a variable cell is not an identity.',
            'Actual nested inverse and perturbation use existing local_inverse_swap_action and local_inverse_perturbed_swap bodies.',
            'Runtime inverse is an independent positive boundary, not inferred from typed eq_refl success.',
            'Raw public Prof versus local Cartesian mapping-category profiles remain distinct; no new inverse witness or whole inverse postulate is supplied.',
        ],
        'checkerInvoked': False,
    }
    manifest['outputs']['lambdapi.pkg'] = digest(package)
    return root, targets, package, manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true', help='validate recipe/source pins without writing')
    args = parser.parse_args()
    root, targets, package, manifest = build()
    record = json.loads((Path(__file__).resolve().parent / 'inverse_nested_verification.json').read_text())
    for group in ('sourceInputs', 'outputs'):
        assert record[group] == manifest[group], (group, 'changed; review before refreshing evidence')
    if not args.check_authoring:
        output = root / 'tmp/probes/inverse_nested'
        output.mkdir(parents=True, exist_ok=True)
        for name, body in targets.items():
            (output / name).write_text(body)
        (output / 'lambdapi.pkg').write_bytes(package)
        (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'{len(targets)} nested inverse targets prepared; no checker run or runtime qualification.')


if __name__ == '__main__':
    main()
