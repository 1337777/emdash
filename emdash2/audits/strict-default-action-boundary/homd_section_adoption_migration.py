#!/usr/bin/env python3
"""Adopt checked section bodies in the public Homd ladder; no checker run."""
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
    pin_path = audit / 'homd_section_adoption_inputs.json'
    pins = json.loads(pin_path.read_text())
    for name, sha in pins['sourceInputs'].items():
        assert digest((root / name).read_bytes()) == sha, (name, 'pinned input changed')
    prior_path = audit / 'homd_native_section_assembly_verification.json'
    prior = json.loads(prior_path.read_text())
    donor = root / pins['donor']
    original = donor.read_text()
    assert digest(original.encode()) == prior['outputs'][donor.name]
    assert prior['checks'][donor.name]['outcome'] == 'passed-fresh'
    source = original
    changes = []

    def replace(label, old, new):
        nonlocal source
        assert source.count(old) == 1, (label, 'not a unique owner')
        source = source.replace(old, new, 1)
        changes.append({'label': label, 'oldSha256': digest(old.encode()),
                        'newSha256': digest(new.encode()), 'old': old, 'new': new})

    section = re.findall(r'(?ms)^symbol homd_id_src_sec\b.*?;', source)
    target = re.findall(r'(?ms)^symbol homd_id_tgt_func\b.*?;', source)
    assert len(section) == len(target) == 1
    assert '≔' not in section[0] and '≔' not in target[0]
    replace('define-public-source-section', section[0], section[0][:-1] +
            '\n≔ @fibcov_cart_section K E x u;')
    replace('define-public-y-component', target[0], target[0][:-1] +
            '\n≔ @Prof_cov_companion (Hom_cat K x y) (@Fibre_cat K E y)\n'
            '    (@fib_cov_tapp0_func K E x y u);')
    replace('remove-redundant-source-component-rule',
            'rule @tapp0_fapp0 _ _ _ _ $y (@homd_id_src_sec $K $E $x $u)\n'
            '  ↪ @homd_id_tgt_func $K $E $x $u $y;', '')
    replace('remove-redundant-target-object-rule',
            'rule fapp0 (@homd_id_tgt_func $K $E $x $u $y) $v\n'
            '  ↪ @homd_id_ $K $E $x $u $y $v;', '')
    # Preserve every inherited assertion byte and every other rule/definition.
    assert re.findall(r'(?ms)^assert(?:not)?\b.*?;', source) == re.findall(r'(?ms)^assert(?:not)?\b.*?;', original)
    assert len(re.findall(r'(?m)^assert\b', original)) == 340
    assert len(re.findall(r'(?m)^assertnot\b', original)) == 73
    controls_path = audit / 'homd_section_adoption_controls.lpfragment'
    controls = controls_path.read_text()
    assert not re.search(r'(?m)^(?:rule|unif_rule|(?:injective |constant )?symbol)\b', controls)
    combined = source + '\n' + controls
    targets = {'combined_controls.lp': combined}
    continuation_path = root / pins['continuationDonor']
    continuation = continuation_path.read_text()
    continuation_marker = '// 14. Section action over dependent homs'
    assert continuation.count(continuation_marker) == 1
    continuation_tail = continuation[continuation.index(continuation_marker):]
    targets['full_source.lp'] = combined + '\n' + continuation_tail
    removals = {}
    for name, change in zip(('without_srcsec_definition.lp', 'without_tgt_definition.lp'), changes[:2]):
        assert combined.count(change['new']) == 1
        variant = combined.replace(change['new'], change['old'], 1)
        # Restore only the original declaration, never the deleted rules.
        assert all(deletion['old'] not in variant for deletion in changes[2:])
        targets[name] = variant
        removals[name] = {'restoredDeclarationSha256': change['oldSha256'],
                          'removedDefinitionSha256': change['newSha256'],
                          'redundantProjectionRulesRestored': False}
    inputs = [Path(__file__).resolve(), pin_path, prior_path, donor, controls_path,
              root / 'lambdapi.pkg', audit / 'homd_section_adoption_source_closure.md',
              continuation_path, root / 'audits/strict-default-action-boundary/foundation_assembly_verification.json']
    manifest = {
        'status': 'public native-section body adoption authoring replay; execution status is recorded separately',
        'contextRevision': pins['contextRevision'],
        'sourceInputs': {str(path.relative_to(root)): digest(path.read_bytes()) for path in inputs},
        'donor': pins['donor'], 'donorReceipt': prior['checks'][donor.name]['receipt'],
        'exactReplacements': changes,
        'definitionRemovals': removals,
        'fullSourceContinuation': {'donor': pins['continuationDonor'],
                                   'marker': continuation_marker,
                                   'tailSha256': digest(continuation_tail.encode()),
                                   'qualification': 'Historical tail diagnostic only; generic intrinsic displayed-action profile remains under review.'},
        'outputs': {name: digest(body.encode()) for name, body in targets.items()},
        'inheritedAssertions': {'positive': 340, 'negative': 73},
        'newAssertions': {'positive': len(re.findall(r'(?m)^assert\b', controls)),
                          'negative': len(re.findall(r'(?m)^assertnot\b', controls))},
        'scope': [
            'Public src_sec and tgt_func become definitions of checked actual bodies; no equality between independent primitives is introduced.',
            'Only their two redundant object/component projection clauses are removed.',
            'Primitive source functor/root, source object projection, all u rungs/laws, and defined relative interface remain byte-identical.',
            'All inherited controls are retained in the original order.',
            'No whole F/FF strictification, new operational proof argument, new owner rule, or production change.',
            'Definition removals restore one old declaration each, without restoring either redundant projection rule; all controls remain present.',
            'Full-source continuation is a separate diagnostic, not general-FF intrinsic action qualification.',
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
        output = root / 'tmp/probes/homd_section_adoption'
        output.mkdir(parents=True, exist_ok=True)
        for name, body in targets.items():
            path = output / name
            if path.exists():
                assert path.read_text() == body, 'preserve emitted source'
            path.write_text(body)
        (output / 'lambdapi.pkg').write_bytes(package)
        (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'status': 'pins/replacements/inherited assertions verified; no checker run',
                      'targets': list(targets), 'newAssertions': manifest['newAssertions']}, indent=2))


if __name__ == '__main__':
    main()
