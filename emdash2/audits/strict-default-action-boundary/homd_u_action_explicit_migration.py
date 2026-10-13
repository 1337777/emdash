#!/usr/bin/env python3
"""Expose intermediate whole-observation profiles without new semantic rules."""
import hashlib
import json
from pathlib import Path
import re

audit = Path(__file__).resolve().parent
root = audit.parents[1]
output = root / 'tmp/probes/homd_u_action'
digest = lambda data: hashlib.sha256(data).hexdigest()
prior_path = output / 'fullcap_manifest.json'
prior = json.loads(prior_path.read_text())
fragment = audit / 'homd_u_action_explicit_family.lpfragment'
body = fragment.read_text()
assert not re.search(r'(?m)^(?:rule|unif_rule)\b', body)
targets = {}
for name in ('fullcap_observations.lp', 'fullcap_controls.lp', 'fullcap_law_controls.lp', 'fullcap_composition_leaf.lp'):
    data = (output / name).read_bytes()
    assert digest(data) == prior['outputs'][name]
    source, count = re.subn(r'(?ms)^symbol homd_u_action_leaf_family\b.*?;', lambda _: body.rstrip(), data.decode())
    assert count == 1
    targets['explicit_' + name.removeprefix('fullcap_')] = source
for name, source in targets.items():
    target = output / name
    if target.exists():
        assert target.read_text() == source, ('preserve previous successor', name)
    target.write_text(source)
manifest = {
    'status': 'unchecked explicit-profile whole-family successor; no checker run',
    'sourceInputs': {str(p.relative_to(root)): digest(p.read_bytes()) for p in (Path(__file__), prior_path, fragment)},
    'historicalFullcapOutputs': prior['outputs'],
    'outputs': {name: digest(source.encode()) for name, source in targets.items()},
    'change': 'Same six generic functors composed in three named, explicitly typed stages. No primitive, rewrite, unification rule, endpoint change or objectwise-extensionality claim.',
}
(output / 'explicit_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'status': 'emitted; Lambdapi not run', 'targets': list(targets)}, indent=2))
