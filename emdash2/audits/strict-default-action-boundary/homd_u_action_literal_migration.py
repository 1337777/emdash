#!/usr/bin/env python3
"""Preserve first u-action targets; expose literal Op in consumer annotations."""
import argparse
import hashlib
import json
from pathlib import Path


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true')
    args = parser.parse_args()
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    output = root / 'tmp/probes/homd_u_action'
    pins_path = audit / 'homd_u_action_literal_inputs.json'
    pins = json.loads(pins_path.read_text())
    for name, expected in pins['sourceInputs'].items():
        assert digest((root / name).read_bytes()) == expected, name
    prior_path = output / 'manifest.json'
    prior = json.loads(prior_path.read_text())
    old = {}
    for name, expected in prior['outputs'].items():
        data = (output / name).read_bytes()
        assert digest(data) == expected, ('historical target changed', name)
        if name.endswith('.lp'):
            old[name] = data.decode()
    marker = '// Derived observations of the actual source action. No extra semantic owner.\n'
    before = '(Fibre_cat (@Op_catd K E) x)'
    after = '(Op_cat (Fibre_cat E x))'
    targets = {}
    replacements = {}
    for name, source in old.items():
        if marker not in source:
            continue
        assert source.count(marker) == 1
        offset = source.index(marker)
        prefix, tail = source[:offset], source[offset:]
        replacements[name] = tail.count(before)
        assert replacements[name] >= 1
        targets['literal_' + name] = prefix + tail.replace(before, after)
    fragment = audit / 'homd_u_action_literal_source_controls.lpfragment'
    targets['literal_source_controls.lp'] = old['owner.lp'] + '\n' + fragment.read_text()
    manifest = {
        'status': 'unchecked separately labelled annotation successor; no new semantic rule',
        'sourceInputs': {**pins['sourceInputs'],
                         str(Path(__file__).relative_to(root)): digest(Path(__file__).read_bytes()),
                         str(fragment.relative_to(root)): digest(fragment.read_bytes())},
        'historicalOutputs': prior['outputs'],
        'replacementsByHistoricalTarget': replacements,
        'outputs': {name: digest(source.encode()) for name, source in targets.items()},
        'change': 'Only appended consumer annotations expose Op(E[x]) directly; native owner bytes and all original emitted targets are unchanged.',
        'hypothesis': 'The original y observation fails before leaf action; explicit reducible fibre annotation may trigger Hom endpoint inversion before exposing Op. Literal Op avoids that elaboration route.',
        'checkerInvoked': False,
    }
    if not args.check_authoring:
        for name, source in targets.items():
            target = output / name
            if target.exists():
                assert target.read_text() == source, (name, 'preserve emitted successor')
            target.write_text(source)
        (output / 'literal_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'status': 'authoring pins pass; Lambdapi not run', 'targets': list(targets)}, indent=2))


if __name__ == '__main__':
    main()
