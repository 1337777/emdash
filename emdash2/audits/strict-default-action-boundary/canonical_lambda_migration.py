#!/usr/bin/env python3
"""Emit the exact Unit/Unit/Unit Cartesian lambda restriction; no checker.

The new whole mapping owner is an explicitly structural contract. All
canonical j_B/j_F/raw evaluation operations and comparison theorems have
actual bodies, and no operational symbol accepts an equality witness.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re


def digest(data):
    return hashlib.sha256(data).hexdigest()


def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    pins_path = audit / 'canonical_lambda_inputs.json'
    pins = json.loads(pins_path.read_text())
    inputs = {}
    for name, expected in pins['sourceInputs'].items():
        data = (root / name).read_bytes()
        assert digest(data) == expected, (name, 'source pin changed')
        inputs[name] = data
    prior = json.loads(inputs['audits/strict-default-action-boundary/coefficient_assembly_verification.json'])
    donor_name = 'tmp/probes/coefficient_assembly/with_nested_reindex.lp'
    donor = inputs[donor_name].decode()
    assert digest(donor.encode()) == prior['outputs']['with_nested_reindex.lp']
    assert prior['checks']['with_nested_reindex.lp']['outcome'] == 'passed-fresh'
    names = ('canonical_lambda_profile.lpfragment',
             'canonical_lambda_mapping_controls.lpfragment',
             'canonical_lambda_operations.lpfragment',
             'canonical_lambda_generator.lpfragment',
             'canonical_lambda_consumers.lpfragment')
    fragments = {name: (audit / name).read_text() for name in names}
    profile = fragments[names[0]]
    assert len(re.findall(r'(?m)^unif_rule\b', profile)) == 1
    assert not re.search(r'(?m)^rule\b', profile)
    assert not re.search(r'(?m)^(?:rule|unif_rule)\b',
                         '\n'.join(fragments[name] for name in names[1:]))
    anchor = '// Unchanged raw production owner: Prof_coyoneda_cov_map\n'
    assert donor.count(anchor) == 1
    owner = donor.replace(anchor, profile + '\n' + anchor)
    mapping = fragments[names[1]]
    operations = fragments[names[2]]
    generator = fragments[names[3]]
    consumers = fragments[names[4]]
    targets = {
        'owner.lp': owner,
        'restriction_controls.lp': owner + '\n' + mapping,
        'operations.lp': owner + '\n' + mapping + '\n' + operations,
        'consumers.lp': owner + '\n' + mapping + '\n' + operations + '\n' +
                        generator + '\n' + consumers,
    }
    raw_view = profile[profile.index('unif_rule'):]
    assert targets['consumers.lp'].count(raw_view) == 1
    targets['without_raw_view.lp'] = targets['consumers.lp'].replace(raw_view, '')
    authoring = [Path(__file__), pins_path, *(audit / name for name in names),
                 audit / 'canonical_lambda_source_closure.md']
    manifest = {
        'status': 'authoring only; explicit structural lambda-profile restriction, not strictness derived from raw beta/eta',
        'sourceInputs': pins['sourceInputs'],
        'contextRevision': pins['contextRevision'],
        'donorReceipt': prior['checks']['with_nested_reindex.lp']['receipt'],
        'fullSourceContinuation': False,
        'ownerPosition': 'Immediately after the unchanged Prof_lambda_cov_map declaration and before raw co-Yoneda.',
        'newStructuralContract': {
            'owner': 'canonical_lambda_unit_func',
            'scope': 'Whole functor Hom_S(B,B)(U tensor U,U) -> Hom_S(B,B)(U,imply(U,U)), only the Unit/Unit/Unit instance.',
            'higherAction': 'Retained by the whole functor and its composed raw inclusion, but supplied by the explicit restriction contract; no native raw directed lambda action was available to derive it.',
            'rawObjectView': 'Guarded comparison with the original Prof_lambda_cov_map on the included classified input.',
        },
        'derivedBodies': ['whole raw-image functor', 'j_B from admitted seed',
                          'j_F by existing Cartesian reindexing', 'actual raw evaluation',
                          'raw agreement theorems', 'native generator observation',
                          'proof-time identity evaluation'],
        'preservedBoundaries': ['Public raw ProfMap/Prof_hom and old lambda/eval signatures are unchanged.',
                                'No arbitrary raw-map strictifier or independently supplied proof/equality input.',
                                'No classified general evaluator/counit, global Cartesian closed Prof theory or new runtime beta.',
                                'Existing inverse interactions, balancing and coefficient/production obligations remain.'],
        'authoringInputs': {str(path.relative_to(root)): digest(path.read_bytes()) for path in authoring},
        'outputs': {name: digest(source.encode()) for name, source in targets.items()},
        'newControls': {name: {'positive': len(re.findall(r'(?m)^assert\b', source)),
                              'negative': len(re.findall(r'(?m)^assertnot\b', source))}
                        for name, source in fragments.items()},
    }
    return root, targets, inputs['lambdapi.pkg'], manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true')
    args = parser.parse_args()
    root, targets, package, manifest = build()
    if args.check_authoring:
        print(json.dumps({'status': 'pins and authoring guards pass; Lambdapi not run',
                          'newControls': manifest['newControls']}, indent=2))
        return
    output = root / 'tmp/probes/canonical_lambda'
    output.mkdir(parents=True, exist_ok=True)
    for name, source in targets.items():
        (output / name).write_text(source)
    (output / 'lambdapi.pkg').write_bytes(package)
    manifest['outputs']['lambdapi.pkg'] = digest(package)
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted exact Cartesian lambda restriction and actual canonical consumers; no checker run.')


if __name__ == '__main__':
    main()
