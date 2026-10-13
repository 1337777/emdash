#!/usr/bin/env python3
"""Emit the bounded represented-lift action experiment; never run Lambdapi.

The donor is the exact checked named-middle-mate/component prefix. This adds
only the whole/capped action projections at their owner. Mate identity,
lift identity and lift composition remain independent positive obligations.
No native-extraction or full-lift coherence qualification is inferred.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re


FRAGMENTS = (
    'lift_action.lpfragment',
    'lift_action_controls.lpfragment',
    'lift_action_represented_controls.lpfragment',
    'lift_action_raw_composition_view.lpfragment',
    'lift_action_mate_identity_boundary.lpfragment',
    'lift_action_id_components.lpfragment',
    'lift_action_id_boundary.lpfragment',
    'lift_action_composition_components.lpfragment',
    'lift_action_composition_boundary.lpfragment',
    'lift_action_coefficient_units.lpfragment',
    'lift_action_coefficient_unit_controls.lpfragment',
    'lift_action_left_identity_endpoint.lpfragment',
    'lift_action_coefficient_left_unit.lpfragment',
    'lift_action_coefficient_left_unit_controls.lpfragment',
    'lift_action_mate_identity_normal_forms.lpfragment',
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    pins_path = audit / 'lift_action_inputs.json'
    pins = json.loads(pins_path.read_text())
    for name, expected in pins['sourceInputs'].items():
        assert digest((root / name).read_bytes()) == expected, (name, 'source pin changed; review required')
    donor = root / pins['donor']
    predecessor_path = audit / 'lift_middle_verification.json'
    predecessor = json.loads(predecessor_path.read_text())
    source = donor.read_text()
    assert digest(source.encode()) == predecessor['outputs'][donor.name]
    assert predecessor['checks'][donor.name]['outcome'] == 'passed-fresh'
    f = {name: (audit / name).read_text() for name in FRAGMENTS}
    action = f['lift_action.lpfragment']
    assert len(re.findall(r'(?m)^rule\b', action)) == 2
    assert not re.search(r'(?m)^unif_rule\b', action)
    for name, text in f.items():
        if name not in ('lift_action.lpfragment', 'lift_action_coefficient_units.lpfragment',
                        'lift_action_coefficient_left_unit.lpfragment'):
            assert not re.search(r'(?m)^(?:rule|unif_rule|(?:injective |constant )?symbol)\b', text), name
    anchor = '// The y-section is the existing transformation category in the coefficient.'
    assert source.count(anchor) == 1
    assert source.count('symbol Prof_cov_lift_comparison ') == 1
    assert source.count('symbol Prof_cov_lift_right_func ') == 1
    assert source.index('symbol Prof_cov_lift_comparison ') < source.index(anchor)
    prefix = source.replace(anchor, action + '\n' + anchor)
    targets = {'owner_prefix.lp': prefix}
    for target, fragment in (
            ('action_controls.lp', 'lift_action_controls.lpfragment'),
            ('represented_action.lp', 'lift_action_represented_controls.lpfragment'),
            ('raw_composition_view.lp', 'lift_action_raw_composition_view.lpfragment'),
            ('mate_identity_boundary.lp', 'lift_action_mate_identity_boundary.lpfragment'),
            ('lift_id_components.lp', 'lift_action_id_components.lpfragment'),
            ('lift_id_boundary.lp', 'lift_action_id_boundary.lpfragment'),
            ('lift_composition_components.lp', 'lift_action_composition_components.lpfragment'),
            ('lift_composition_boundary.lp', 'lift_action_composition_boundary.lpfragment')):
        targets[target] = prefix + '\n' + f[fragment]
    targets['no_action_controls.lp'] = source + '\n' + f['lift_action_controls.lpfragment']
    # Separate unit-projection candidate; old action/idq failure bytes stay
    # reproducible in the original targets above. Only the measured right
    # unit projection is added, not a precomposition or triangle law.
    unit_anchor = '// Read the derived unit through the actual product-prof/curried functor.'
    assert prefix.count(unit_anchor) == 1
    units = f['lift_action_coefficient_units.lpfragment']
    assert len(re.findall(r'(?m)^rule\b', units)) == 1
    assert not re.search(r'(?m)^unif_rule\b', units)
    unit_prefix = prefix.replace(unit_anchor, units + '\n' + unit_anchor)
    targets['unit_projection_owner_prefix.lp'] = unit_prefix
    for target, fragment in (
            ('unit_projection_action_controls.lp', 'lift_action_controls.lpfragment'),
            ('unit_projection_controls.lp', 'lift_action_coefficient_unit_controls.lpfragment'),
            ('left_identity_endpoint_boundary.lp', 'lift_action_left_identity_endpoint.lpfragment'),
            ('unit_projection_mate_identity_boundary.lp', 'lift_action_mate_identity_boundary.lpfragment')):
        targets[target] = unit_prefix + '\n' + f[fragment]
    # The independently measured L(id) failure motivates this separate
    # mirrored point-unit candidate. Preserve every right-only target above.
    left_unit = f['lift_action_coefficient_left_unit.lpfragment']
    assert len(re.findall(r'(?m)^rule\b', left_unit)) == 1
    assert not re.search(r'(?m)^unif_rule\b', left_unit)
    assert unit_prefix.count(unit_anchor) == 1
    paired_prefix = unit_prefix.replace(unit_anchor, left_unit + '\n' + unit_anchor)
    targets['paired_unit_owner_prefix.lp'] = paired_prefix
    targets['paired_unit_controls.lp'] = (
        paired_prefix + '\n' + f['lift_action_coefficient_unit_controls.lpfragment']
        + '\n' + f['lift_action_coefficient_left_unit_controls.lpfragment']
        + '\n' + f['lift_action_left_identity_endpoint.lpfragment'])
    for label, candidate_rule in (('right', units), ('left', left_unit)):
        assert targets['paired_unit_controls.lp'].count(candidate_rule) == 1
        targets['paired_unit_without_' + label + '_projection.lp'] = (
            targets['paired_unit_controls.lp'].replace(candidate_rule, ''))
    for target, fragment in (
            ('paired_unit_action_controls.lp', 'lift_action_controls.lpfragment'),
            ('paired_unit_mate_identity_boundary.lp', 'lift_action_mate_identity_boundary.lpfragment'),
            ('paired_unit_represented_action.lp', 'lift_action_represented_controls.lpfragment'),
            ('paired_unit_lift_id_components.lp', 'lift_action_id_components.lpfragment'),
            ('paired_unit_lift_composition_components.lp', 'lift_action_composition_components.lpfragment'),
            ('paired_unit_mate_identity_normal_forms.lp', 'lift_action_mate_identity_normal_forms.lpfragment')):
        targets[target] = paired_prefix + '\n' + f[fragment]
    package = (root / 'lambdapi.pkg').read_bytes()
    inputs = [Path(__file__).resolve(), pins_path, predecessor_path, donor, root / 'lambdapi.pkg']
    inputs += [audit / name for name in FRAGMENTS]
    manifest = {
        'status': 'non-library authoring manifest; qualifications are recorded in lift_action_verification.json',
        'donor': str(donor.relative_to(root)),
        'donorReceipt': predecessor['checks'][donor.name]['receipt'],
        'sourceInputs': {str(p.relative_to(root)): digest(p.read_bytes()) for p in inputs},
        'outputs': {name: digest(text.encode()) for name, text in targets.items()},
        'outputControlCounts': {name: {
            'positive': len(re.findall(r'(?m)^assert\b', text)),
            'negative': len(re.findall(r'(?m)^assertnot\b', text)),
        } for name, text in targets.items()},
        'qualification': [
            'The two new rules project the existing structural lift to its actual right-action body.',
            'Mate identity and whole lift identity/composition are positive obligations, not installed laws or successful negative tests.',
            'Check lift-id/composition component prerequisites before considering any whole law.',
            'Represented controls use the actual ProfRep_cov_int map and Cartesian representation action at arbitrary p.',
            'No standalone laxity owner is declared; later native extraction and full higher coherence remain outside this prefix.',
            'Raw FF retains its separate covariant diagram map and is not admitted as a strict lift input.',
        ],
        'checkerInvoked': False,
    }
    manifest['outputs']['lambdapi.pkg'] = digest(package)
    return root, targets, package, manifest


def check_pins(audit, manifest):
    record = json.loads((audit / 'lift_action_verification.json').read_text())
    for group in ('sourceInputs', 'outputs'):
        assert manifest[group] == record[group], (
            group, 'changed; review the authoring/evidence boundary, do not refresh automatically')
    return record


def check_evidence(root, record):
    """Read existing records only; do not run a checker or renew qualification."""
    for name, evidence in record['checks'].items():
        path = root / evidence['receipt']
        assert digest(path.read_bytes()) == evidence['receiptSha256'], name
        receipt = json.loads(path.read_text())
        assert receipt['inputs'] == evidence['inputs'], name
        assert receipt['inputs'][receipt['target']] == record['outputs'][name], name
        for source, expected in receipt['inputs'].items():
            assert digest((root / source).read_bytes()) == expected, source
        assert receipt['log'] == evidence['log'], name
        assert digest((root / receipt['log']).read_bytes()) == receipt['logSha256'] == evidence['logSha256'], name
        assert digest((root / evidence['output']).read_bytes()) == evidence['outputSha256'], name
        for field in ('outcome', 'checkerExit', 'settings', 'checker'):
            if field in evidence:
                assert receipt[field] == evidence[field], (name, field)
    for name, evidence in record.get('historicalChecks', {}).items():
        path = root / evidence['receipt']
        assert digest(path.read_bytes()) == evidence['receiptSha256'], name
        receipt = json.loads(path.read_text())
        assert receipt['inputs'][receipt['target']] == evidence['sourceSha256'], name
        for expected in receipt['inputs'].values():
            archived = root / receipt['inputStore'] / expected
            assert digest(archived.read_bytes()) == expected, str(archived)
        assert digest((root / receipt['log']).read_bytes()) == receipt['logSha256'] == evidence['logSha256'], name
        assert receipt['outcome'] == evidence['outcome'], name
        assert receipt['checkerExit'] == evidence['checkerExit'], name
    return len(record['checks']), len(record.get('historicalChecks', {}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true', help='validate pins/owner recipe without writing')
    parser.add_argument('--check-evidence', action='store_true',
                        help='also verify saved receipt/source/log identities; never invoke Lambdapi')
    args = parser.parse_args()
    root, targets, package, manifest = build()
    record = check_pins(Path(__file__).resolve().parent, manifest)
    if args.check_evidence:
        current, historical = check_evidence(root, record)
        print(f'Verified {current} current and {historical} historical receipt/source/log identities; no checker run.')
    if not args.check_authoring:
        output = root / 'tmp/probes/lift_action'
        output.mkdir(parents=True, exist_ok=True)
        for name, source in targets.items():
            (output / name).write_text(source)
        (output / 'lambdapi.pkg').write_bytes(package)
        (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'{len(targets)} bounded lift-action targets prepared; no Lambdapi run or coherence qualification.')


if __name__ == '__main__':
    main()
