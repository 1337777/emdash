#!/usr/bin/env python3
"""Emit native identity-Homd fibre-arrow projections; never run Lambdapi."""
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
    pins_path = audit / 'homd_u_action_inputs.json'
    pins = json.loads(pins_path.read_text())
    for path, expected in pins['sourceInputs'].items():
        assert digest((root / path).read_bytes()) == expected, (path, 'source pin changed')
    record_path = audit / 'foundation_assembly_verification.json'
    prior = json.loads(record_path.read_text())
    donor = root / pins['donor']
    source = donor.read_text()
    assert digest(source.encode()) == prior['outputs'][donor.name]
    assert prior['checks'][donor.name]['outcome'] == 'passed-fresh'
    names = ('owner', 'observations', 'controls', 'negative_controls',
             'law_controls', 'composition_leaf')
    paths = {name: audit / ('homd_u_action_' + name + '.lpfragment') for name in names}
    fragments = {name: path.read_text() for name, path in paths.items()}
    owner = fragments['owner']
    assert len(re.findall(r'(?m)^rule\b', owner)) == 8
    assert not re.search(r'(?m)^unif_rule\b', owner)
    assert not re.search(r'(?m)^(?:rule|unif_rule)\b', fragments['observations'])
    for name in names[2:]:
        assert not re.search(r'(?m)^(?:rule|unif_rule|(?:injective |constant )?symbol)\b', fragments[name])
    anchor = '// Existing public names remain available as defined projections of the\n'
    assert source.count(anchor) == 1
    inserted = source.replace(anchor, owner + '\n' + anchor, 1)
    observed = inserted + '\n' + fragments['observations']
    controls = observed + '\n' + fragments['controls'] + '\n' + fragments['negative_controls']
    laws = controls + '\n' + fragments['law_controls']
    targets = {
        'owner.lp': inserted,
        'observations.lp': observed,
        'controls.lp': controls,
        'law_controls.lp': laws,
        'composition_leaf.lp': laws + '\n' + fragments['composition_leaf'],
    }
    rule_blocks = re.findall(r'(?ms)^rule\b.*?;', owner)
    assert len(rule_blocks) == 8
    removals = {
        'source_projection': (0, 1, 2),
        'component_projection': (3, 4),
        'leaf_projection': (5,),
        'law_joins': (6, 7),
    }
    for name, indices in removals.items():
        variant = laws
        for index in indices:
            block = rule_blocks[index]
            assert variant.count(block) == 1
            variant = variant.replace(block, '', 1)
        targets['without_' + name + '.lp'] = variant
    inputs = [Path(__file__).resolve(), pins_path, record_path, donor,
              root / 'lambdapi.pkg', *paths.values(), audit / 'homd_u_action_source_closure.md']
    manifest = {
        'status': 'unchecked native Homd u-action owner-position prototype; no checker invoked',
        'donor': pins['donor'],
        'donorReceipt': prior['checks'][donor.name]['receipt'],
        'sourceInputs': {str(path.relative_to(root)): digest(path.read_bytes()) for path in inputs},
        'outputs': {name: digest(body.encode()) for name, body in targets.items()},
        'ownerPosition': 'Inside the identity Homd ladder, after object projections and before relative aliases.',
        'ruleGroups': {name: [digest(rule_blocks[index].encode()) for index in indices]
                       for name, indices in removals.items()},
        'newAssertions': {name: {
            'positive': len(re.findall(r'(?m)^assert\b', body)),
            'negative': len(re.findall(r'(?m)^assertnot\b', body)),
        } for name, body in fragments.items()},
        'scope': [
            'Four structural native projection rungs belong to the already declared whole identity Homd owner.',
            'The ordinary leaf is the existing precomposition functor along E[f](h), retaining higher beta action.',
            'Whole h-parameter observation is a defined composite with actual Cartesian inclusions; only its cap and higher-action formation are tested here.',
            'No claim that equality of object projections derives equality of the whole h-parameter functor.',
            'Source identity/composition joins project the laws already imposed by homd_id_src_func:Functor.',
            'The root homd_id_int and arbitrary public FF remain ambient transformations.',
            'No combined x/y dependent context, raw-map strictifier, operational path input, coend theory or production edit.',
            'The two-factor leaf composition comparison is separately measured; it introduces no runtime precomposition collapse.',
        ],
        'checkerInvoked': False,
    }
    package = (root / 'lambdapi.pkg').read_bytes()
    manifest['outputs']['lambdapi.pkg'] = digest(package)
    return root, targets, package, manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true')
    args = parser.parse_args()
    root, targets, package, manifest = build()
    if not args.check_authoring:
        output = root / 'tmp/probes/homd_u_action'
        output.mkdir(parents=True, exist_ok=True)
        for name, body in targets.items():
            target = output / name
            if target.exists():
                assert target.read_text() == body, (name, 'preserve emitted bytes; label a successor')
            target.write_text(body)
        (output / 'lambdapi.pkg').write_bytes(package)
        (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'status': 'pins and authoring checks pass; Lambdapi not run',
                      'targets': list(targets), 'newAssertions': manifest['newAssertions']}, indent=2))


if __name__ == '__main__':
    main()
