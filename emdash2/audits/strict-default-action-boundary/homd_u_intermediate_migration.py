#!/usr/bin/env python3
"""Emit independent intermediate Homd u-action baselines; no checker run."""
import argparse
import hashlib
import json
from pathlib import Path
import re


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true')
    args = parser.parse_args()
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    pins_path = audit / 'homd_u_intermediate_inputs.json'
    pins = json.loads(pins_path.read_text())
    for name, sha in pins['sourceInputs'].items():
        assert digest((root / name).read_bytes()) == sha, (name, 'pinned input changed')
    prior_path = audit / 'homd_u_normalization_verification.json'
    prior = json.loads(prior_path.read_text())
    donor = root / pins['donor']
    source = donor.read_text()
    assert digest(source.encode()) == prior['outputs'][donor.name]
    assert prior['checks'][donor.name]['outcome'] == 'passed-fresh'
    names = ('controls', 'y_identity', 'v_identity', 'y_composition', 'v_composition')
    paths = {name: audit / ('homd_u_intermediate_' + name + '.lpfragment') for name in names}
    bodies = {name: path.read_text() for name, path in paths.items()}
    for name, body in bodies.items():
        assert not re.search(r'(?m)^(?:rule|unif_rule|(?:injective |constant )?symbol)\b', body), name
        assert '(Fibre_cat E ' not in body, name
    targets = {name + '.lp': source + '\n' + bodies['controls'] + '\n' + bodies[name]
               for name in names[1:]}
    inputs = [Path(__file__).resolve(), pins_path, prior_path, donor, root / 'lambdapi.pkg', *paths.values()]
    manifest = {
        'status': 'unchecked independent intermediate y/v identity/composition baselines; no new semantic rule',
        'contextRevision': pins['contextRevision'],
        'sourceInputs': {str(path.relative_to(root)): digest(path.read_bytes()) for path in inputs},
        'donor': pins['donor'], 'donorReceipt': prior['checks'][donor.name]['receipt'],
        'outputs': {name: digest(body.encode()) for name, body in targets.items()},
        'newAssertionCounts': {'eachTarget': {'positive': 2, 'negative': 4}},
        'scope': [
            'Actual generic component routes are compared with native intermediate projection heads.',
            'All y/v identities and compositions use their existing Cartesian mapping categories.',
            'Two same-endpoint h perturbations and root/FF ambient negatives run before each positive boundary.',
            'No new primitive, rule, unification equation, operational witness, or strict root/section classification.',
            'Each target isolates one boundary; passing a generic route does not establish the native rung comparison.',
        ],
        'checkerInvoked': False,
    }
    package = (root / 'lambdapi.pkg').read_bytes()
    manifest['outputs']['lambdapi.pkg'] = digest(package)
    if not args.check_authoring:
        output = root / 'tmp/probes/homd_u_intermediate'
        output.mkdir(parents=True, exist_ok=True)
        for name, body in targets.items():
            target = output / name
            if target.exists():
                assert target.read_text() == body, (name, 'preserve previous baseline')
            target.write_text(body)
        (output / 'lambdapi.pkg').write_bytes(package)
        (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'status': 'pins and authoring guards pass; Lambdapi not run', 'targets': list(targets)}, indent=2))


if __name__ == '__main__':
    main()
