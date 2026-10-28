#!/usr/bin/env python3
"""Build fixed-x intrinsic target parameter action from existing whole owners."""
import argparse
import hashlib
import json
from pathlib import Path
import re


def digest(b):
    return hashlib.sha256(b).hexdigest()


def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    donor = root / 'tmp/probes/homd_root_action_scope/combined_controls.lp'
    old = donor.read_text()
    assert digest(old.encode()) == '82b0d9881e730ccf3254b1f4927f31690a7e1ae45cb21db5e89aa7ef90b67148'
    owners_path = audit / 'homd_intrinsic_parameter.lpfragment'
    controls_path = audit / 'homd_intrinsic_parameter_controls.lpfragment'
    owners, controls = owners_path.read_text(), controls_path.read_text()
    assert not re.search(r'(?m)^(rule|unif_rule|injective symbol|constant symbol)\b', owners)
    assert len(re.findall(r'(?m)^symbol\b', owners)) == owners.count('≔')
    assert not re.search(r'(?m)^(rule|unif_rule|symbol|injective symbol|constant symbol)\b', controls)
    marker = '// NON-LIBRARY identity-core qualification at the actual whole package.'
    assert old.count(marker) == 1
    selected = old.replace(marker, owners + '\n' + marker, 1)
    assert re.findall(r'(?ms)^assert(?:not)?\b.*?;', selected) == re.findall(r'(?ms)^assert(?:not)?\b.*?;', old)
    targets = {'definitions.lp': selected, 'combined_controls.lp': selected + '\n' + controls}
    inputs = [Path(__file__).resolve(), donor, owners_path, controls_path, root / 'lambdapi.pkg']
    manifest = {
        'status': 'authoring only; execution status is recorded separately',
        'hypothesis': 'Fixed-x source/target parameter action is defined on ambient FF/GG using strict component transpose; the whole y-section is retained.',
        'sourceInputs': {str(p.relative_to(root)): digest(p.read_bytes()) for p in inputs},
        'outputs': {name: digest(s.encode()) for name, s in targets.items()},
        'inheritedAssertions': {'positive': 348, 'negative': 77},
        'newAssertions': {'positive': len(re.findall(r'(?m)^assert\b', controls)), 'negative': len(re.findall(r'(?m)^assertnot\b', controls))},
        'scope': ['Definitions through existing whole owners; no new rule, primitive, proof payload or strict-transfor input.',
                  'Parameter action only: not whole x-assembly or extracted intrinsic laxity.'],
    }
    return root, targets, manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true')
    parser.add_argument('--variant', default='initial')
    args = parser.parse_args()
    assert re.fullmatch(r'[a-z0-9_]+', args.variant)
    root, targets, manifest = build()
    if not args.check_authoring:
        out = root / 'tmp/probes/homd_intrinsic_parameter' / args.variant
        out.mkdir(parents=True, exist_ok=True)
        for name, source in targets.items():
            path = out / name
            assert not path.exists() or path.read_text() == source, 'preserve emitted source'
            path.write_text(source)
        (out / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
        (out / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'status': 'authoring checked; no checker run', 'targets': list(targets)}, indent=2))


if __name__ == '__main__':
    main()
