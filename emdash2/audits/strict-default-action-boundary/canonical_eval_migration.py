#!/usr/bin/env python3
"""Emit exact companion-weight Cartesian evaluation; never run Lambdapi.

One whole restricted mapping owner is structural. Its canonical value at
the actual j_F, raw-image functor, raw agreement, generator observation and
curried image are definitions. No classified inverse/triangle rule is added.
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
    pins_path = audit / 'canonical_eval_inputs.json'
    pins = json.loads(pins_path.read_text())
    inputs = {}
    for name, expected in pins['sourceInputs'].items():
        data = (root / name).read_bytes()
        assert digest(data) == expected, (name, 'source pin changed')
        inputs[name] = data
    prior = json.loads(inputs['audits/strict-default-action-boundary/canonical_lambda_verification.json'])
    donor_name = 'tmp/probes/canonical_lambda/consumers.lp'
    donor = inputs[donor_name].decode()
    assert digest(donor.encode()) == prior['outputs']['consumers.lp']
    assert prior['checks']['consumers.lp']['outcome'] == 'passed-fresh'
    names = ('canonical_eval_profile.lpfragment',
             'canonical_eval_mapping_controls.lpfragment',
             'canonical_eval_operations.lpfragment',
             'canonical_eval_generator.lpfragment',
             'canonical_eval_consumers.lpfragment',
             'canonical_eval_curried.lpfragment')
    fragments = {name: (audit / name).read_text() for name in names}
    profile = fragments[names[0]]
    assert len(re.findall(r'(?m)^unif_rule\b', profile)) == 1
    assert not re.search(r'(?m)^rule\b', profile)
    assert not re.search(r'(?m)^(?:rule|unif_rule)\b',
                         '\n'.join(fragments[name] for name in names[1:]))
    anchor = '// Unchanged raw production owner: Prof_lambda_cov_map\n'
    assert donor.count(anchor) == 1
    owner = donor.replace(anchor, profile + '\n' + anchor)
    mapping = fragments[names[1]]
    operations = fragments[names[2]]
    generator = fragments[names[3]]
    consumers = fragments[names[4]]
    curried = fragments[names[5]]
    targets = {
        'owner.lp': owner,
        'restriction_controls.lp': owner + '\n' + mapping,
        'operations.lp': owner + '\n' + mapping + '\n' + operations,
        'raw_consumers.lp': owner + '\n' + mapping + '\n' + operations + '\n' +
                            generator + '\n' + consumers,
    }
    targets['consumers.lp'] = targets['raw_consumers.lp'] + '\n' + curried
    raw_view = profile[profile.index('unif_rule'):]
    assert targets['consumers.lp'].count(raw_view) == 1
    targets['without_raw_view.lp'] = targets['consumers.lp'].replace(raw_view, '')
    authoring = [Path(__file__), pins_path, *(audit / name for name in names),
                 audit / 'canonical_eval_source_closure.md']
    manifest = {
        'status': 'authoring only; explicit structural companion-weight evaluation restriction, not strictness derived from raw beta or faithful forgetting',
        'sourceInputs': pins['sourceInputs'],
        'contextRevision': pins['contextRevision'],
        'donorReceipt': prior['checks']['consumers.lp']['id'],
        'fullSourceContinuation': False,
        'ownerPosition': 'Immediately after the unchanged Prof_eval_cov_map declaration and before raw lambda.',
        'newStructuralContract': {
            'owner': 'canonical_eval_companion_func',
            'scope': 'Fixed F:A->B; classified Conjoint(F)->reindex(imply(U_B,U_B),id,F) maps to classified tensor(Conjoint(F),Companion(F))->U_B.',
            'higherAction': 'Supplied as part of the restricted whole functor, retained by its composed raw inclusion; not compared to a nonexistent full raw-eval mapping owner.',
            'parameterScope': 'Whole action is only on the classified input-map category at fixed F and fixed A/B. A whole varying-F or varying-A/B family and its coherent action remain a separate represented-lift assembly obligation.',
            'rawObjectView': 'Guarded by all original eval categories, P/Q/O and the actual included classified input.',
        },
        'derivedBodies': ['whole raw-image functor', 'counit as fapp0 at actual j_F',
                          'actual raw inclusion', 'raw original counit agreement',
                          'native canonical generator observation',
                          'actual image under existing Cartesian curry with full/capped action'],
        'preservedBoundaries': ['Public raw ProfMap/Prof_hom and original closed-operation signatures are unchanged.',
                                'No arbitrary raw-map admission or separately supplied proof/witness input.',
                                'No classified beta/eta, triangle, faithfulness inference or new runtime reduction.',
                                'No Q-composition/unit endpoint identification or new Q primitive.',
                                'No whole directed family/coherence as F or A/B vary; this parameter assembly is required for complete represented-lift coherence.',
                                'No arbitrary two-leg balancing or production qualification.'],
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
    output = root / 'tmp/probes/canonical_eval'
    output.mkdir(parents=True, exist_ok=True)
    for name, source in targets.items():
        (output / name).write_text(source)
    (output / 'lambdapi.pkg').write_bytes(package)
    manifest['outputs']['lambdapi.pkg'] = digest(package)
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted companion-weight Cartesian evaluation and constructed counit consumers; no checker run.')


if __name__ == '__main__':
    main()
