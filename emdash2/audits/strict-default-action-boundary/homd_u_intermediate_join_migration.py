#!/usr/bin/env python3
"""Replay exact intermediate u joins and individual removals; no checker."""
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
    pins_path = audit / 'homd_u_intermediate_join_inputs.json'
    pins = json.loads(pins_path.read_text())
    for name, sha in pins['sourceInputs'].items():
        assert digest((root / name).read_bytes()) == sha, (name, 'pinned source changed')
    donor = root / pins['donor']
    donor_record = json.loads((audit / 'homd_u_normalization_verification.json').read_text())
    source = donor.read_text()
    assert digest(source.encode()) == donor_record['outputs'][donor.name]
    assert donor_record['checks'][donor.name]['outcome'] == 'passed-fresh'
    names = ('controls', 'y_identity', 'v_identity', 'y_composition', 'v_composition')
    controls = '\n'.join((audit / ('homd_u_intermediate_' + name + '.lpfragment')).read_text()
                         for name in names)
    anchor = '// Existing public names remain available as defined projections of the\n'
    assert source.count(anchor) == 1
    targets = {}
    variants = {
        'joined_controls.lp': 'homd_u_intermediate_joins_unguarded.lpfragment',
        'guarded_controls.lp': 'homd_u_intermediate_joins_explicit_guard.lpfragment',
        'minimal_guard_controls.lp': 'homd_u_intermediate_joins.lpfragment',
    }
    for name, fragment in variants.items():
        body = (audit / fragment).read_text()
        targets[name] = source.replace(anchor, body + '\n' + anchor, 1) + '\n' + controls
        assert digest(targets[name].encode()) == pins['historicalOutputs'][name], (name, 'historical bytes changed')
    selected = targets['minimal_guard_controls.lp']
    joins = (audit / variants['minimal_guard_controls.lp']).read_text()
    blocks = re.findall(r'(?ms)^rule\b.*?;', joins)
    assert len(blocks) == 4
    groups = ('y_identity', 'v_identity', 'y_composition', 'v_composition')
    for name, block in zip(groups, blocks):
        assert selected.count(block) == 1
        targets['without_' + name + '.lp'] = selected.replace(block, '', 1)
    selected_receipt = json.loads((root / pins['selectedReceipt']).read_text())
    assert selected_receipt['outcome'] == 'passed-fresh'
    assert selected_receipt['inputs'][selected_receipt['target']] == digest(selected.encode())
    authoring = [Path(__file__).resolve(), pins_path, audit / 'homd_u_intermediate_join_source_closure.md']
    manifest = {
        'status': 'exact selected source and preserved guard/removal variants; authoring manifest only, execution status is recorded in homd_u_intermediate_join_verification.json',
        'contextRevision': pins['contextRevision'],
        'sourceInputs': pins['sourceInputs'],
        'authoringInputs': {str(path.relative_to(root)): digest(path.read_bytes()) for path in authoring},
        'donor': pins['donor'], 'donorReceipt': donor_record['checks'][donor.name]['receipt'],
        'selectedReceipt': pins['selectedReceipt'],
        'historicalOutputs': pins['historicalOutputs'],
        'outputs': {name: digest(body.encode()) for name, body in targets.items()},
        'ruleGroups': {name: digest(block.encode()) for name, block in zip(groups, blocks)},
        'newAssertions': {'positive': len(re.findall(r'(?m)^assert\b', controls)),
                          'negative': len(re.findall(r'(?m)^assertnot\b', controls))},
        'qualification': 'Four existing projection-order joins, with category constructor guard on each composition rule. No new root strictness, arbitrary raw-map admission, whole-family extensionality or production qualification.',
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
        output = root / 'tmp/probes/homd_u_intermediate'
        for name, body in targets.items():
            target = output / name
            if target.exists():
                assert target.read_text() == body, (name, 'preserve emitted source')
            target.write_text(body)
        (output / 'lambdapi.pkg').write_bytes(package)
        (output / 'join_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'status': 'exact source pins pass; Lambdapi not run', 'targets': list(targets)}, indent=2))


if __name__ == '__main__':
    main()
