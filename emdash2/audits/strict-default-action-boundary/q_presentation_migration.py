#!/usr/bin/env python3
"""NON-LIBRARY Cartesian inverse / product-prof presentation experiment."""
import hashlib
import json
from pathlib import Path
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'q_closed_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_q_closed'
    prior = json.loads((audit / 'q_closed_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']
    rules = (audit / 'cartesian_inverse_rules.lpfragment').read_text()
    controls = (audit / 'cartesian_inverse_controls.lpfragment').read_text()
    anchor = '// The transfor action of semantic uncurry depends on the higher arrow-action'
    assert source.count(anchor) == 1
    source = source.replace(anchor, rules + '\n' + controls + '\n' + anchor)
    anchor = '// The y-section is the existing transformation category in the coefficient.'
    assert source.count(anchor) == 1
    bridge = (audit / 'q_presentation_bridge.lpfragment').read_text()
    composition = (audit / 'q_presentation_composition.lpfragment').read_text()
    source = source.replace(anchor, bridge + '\n' + composition + '\n' + anchor)
    marker = '// 14. Section action over dependent homs'
    source = source.replace(marker, (audit / 'q_presentation_controls.lpfragment').read_text() + '\n' + marker)
    output = root / 'tmp/probes/strict_default_q_presentation'
    output.mkdir(parents=True, exist_ok=True)
    prefix = source[:source.index(marker)]
    targets = {
        'emdash3_2.lp': source,
        'owner_prefix.lp': prefix,
        'cartesian_prefix.lp': source[:source.index('// 7d. Adjunctions and opposite adjunctions')],
        'no_inverse.lp': prefix.replace(rules, ''),
        'no_swap_inverse.lp': prefix.replace(bridge, ''),
        'no_composition.lp': prefix.replace(composition, ''),
        'action_boundary.lp': prefix + '\n' + (audit / 'cartesian_inverse_action_boundary.lpfragment').read_text(),
    }
    represented = (audit / 'q_presentation_represented_boundaries.lpfragment').read_text()
    split = represented.index('// COMPANION INVERSE')
    targets['conjoint_boundary.lp'] = prefix + '\n' + represented[:split]
    targets['companion_boundary.lp'] = prefix + '\n' + represented[split:]
    unguarded = rules.replace('$B (Product_cat $A $B) $C', '_ _ _')
    assert unguarded != rules
    targets['without_endpoint_guards.lp'] = prefix.replace(rules, unguarded)
    for name in ('roundtrip_boundary.lp', 'composition_boundary.lp', 'counit_boundary.lp'):
        old = (previous / name).read_text()
        old_prefix = (previous / 'owner_prefix.lp').read_text()
        assert old.startswith(old_prefix)
        targets[name] = prefix + old[len(old_prefix):]
    for name, data in targets.items():
        (output / name).write_text(data)
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    names = ('q_presentation_migration.py', 'cartesian_inverse_rules.lpfragment',
             'cartesian_inverse_controls.lpfragment', 'cartesian_inverse_action_boundary.lpfragment',
             'q_presentation_bridge.lpfragment', 'q_presentation_controls.lpfragment',
             'q_presentation_composition.lpfragment', 'q_presentation_represented_boundaries.lpfragment')
    manifest = {
        'status': 'non-library Cartesian presentation computation candidate',
        'qClosedInputSha256': prior['outputs']['emdash3_2.lp'],
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in names},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in (*targets, 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted Cartesian presentation inverse candidate.')


if __name__ == '__main__':
    main()
