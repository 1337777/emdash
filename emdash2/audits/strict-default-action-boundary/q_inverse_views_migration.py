#!/usr/bin/env python3
"""NON-LIBRARY represented presentation-inverse observation joins."""
import hashlib
import json
from pathlib import Path
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'q_presentation_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_q_presentation'
    prior = json.loads((audit / 'q_presentation_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']
    moved = []
    for start, end, destination in (
        ('// 17d. Generic ordinary functor hom-action',
         '// Stable pullback cut elimination and arrow projections.',
         '// Strict Grpd-valued action after function evaluation erases composition.'),
        ('// Reindexing along identity endpoint functors is neutral.',
         '// Nested reindexing accumulates both endpoint functors.',
         '// Whole opposite of the unit Hom, using dimension-one transpose.'),
    ):
        assert source.count(start) == source.count(end) == source.count(destination) == 1
        left = source.index(start)
        right = source.index(end, left)
        block = source[left:right]
        source = source[:left] + '// Existing computation moved to its earlier consumer owner.\n\n' + source[right:]
        source = source.replace(destination, block + '\n' + destination)
        moved.append({'owner': start, 'sha256': hashlib.sha256(block.encode()).hexdigest()})
    rules = (audit / 'q_inverse_views.lpfragment').read_text()
    anchor = '// NON-LIBRARY structural coefficient candidate.'
    assert source.count(anchor) == 1
    source = source.replace(anchor, rules + '\n' + anchor)
    marker = '// 14. Section action over dependent homs'
    controls = (audit / 'q_presentation_represented_boundaries.lpfragment').read_text()
    controls += '\n' + (audit / 'q_inverse_views_controls.lpfragment').read_text()
    source = source.replace(marker, controls + '\n' + marker)
    prefix = source[:source.index(marker)]
    output = root / 'tmp/probes/strict_default_q_inverse_views'
    output.mkdir(parents=True, exist_ok=True)
    targets = {
        'emdash3_2.lp': source,
        'owner_prefix.lp': prefix,
        'no_rules.lp': prefix.replace(rules, ''),
        'action_boundary.lp': prefix + '\n' + (audit / 'cartesian_inverse_action_boundary.lpfragment').read_text(),
    }
    unit_start = rules.index('// Reindexing by identities may reduce before')
    targets['no_unit_rule.lp'] = prefix.replace(rules[unit_start:], '')
    for name, data in targets.items():
        (output / name).write_text(data)
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    names = ('q_inverse_views_migration.py', 'q_inverse_views.lpfragment', 'q_inverse_views_controls.lpfragment',
             'q_presentation_represented_boundaries.lpfragment', 'cartesian_inverse_action_boundary.lpfragment')
    manifest = {
        'status': 'non-library represented inverse joins; higher action/full migration remain unqualified',
        'qPresentationInputSha256': prior['outputs']['emdash3_2.lp'],
        'movedOwners': moved,
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in names},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in (*targets, 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted represented inverse joins.')


if __name__ == '__main__':
    main()
