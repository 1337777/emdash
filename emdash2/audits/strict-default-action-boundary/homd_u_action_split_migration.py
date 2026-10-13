#!/usr/bin/env python3
"""Separate actual u-leaf qualification from whole-parameter family assembly."""
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
targets = {}
removed = {}
names = ['fullcap_controls.lp', 'fullcap_law_controls.lp', 'fullcap_composition_leaf.lp']
names += [name for name in prior['outputs'] if name.startswith('fullcap_without_')]
for name in names:
    data = (output / name).read_bytes()
    assert digest(data) == prior['outputs'][name], name
    source = data.decode()
    family = re.findall(r'(?ms)^symbol homd_u_action_leaf_family\b.*?;', source)
    assert len(family) == 1
    source = source.replace(family[0], '// Whole h-parameter family is measured in a separate successor.\n')
    assertions = re.findall(r'(?ms)^assert(?:not)?\b.*?;', source)
    family_assertions = [block for block in assertions if 'homd_u_action_leaf_family' in block]
    assert len(family_assertions) == 3
    for block in family_assertions:
        source = source.replace(block, '// Corresponding whole h-family observation is separately measured.\n')
    new_name = 'leaf_' + name.removeprefix('fullcap_')
    targets[new_name] = source
    removed[new_name] = {
        'declarationSha256': digest(family[0].encode()),
        'assertionSha256': [digest(block.encode()) for block in family_assertions],
        'positive': 2, 'negative': 1,
    }
for name, source in targets.items():
    target = output / name
    if target.exists():
        assert target.read_text() == source, ('preserve prior successor', name)
    target.write_text(source)
manifest = {
    'status': 'unchecked bounded actual u-leaf successor; no checker run',
    'sourceInputs': {str(p.relative_to(root)): digest(p.read_bytes()) for p in (Path(__file__), prior_path)},
    'historicalFullcapOutputs': prior['outputs'],
    'outputs': {name: digest(source.encode()) for name, source in targets.items()},
    'removedWholeFamily': removed,
    'qualification': 'Only the derived whole-h-family declaration and its two positive/one negative controls are removed. Actual nonidentity source action, y/v/ordinary leaf, higher beta action, source identity/composition and raw/root rejection remain. Whole h-family assembly is not counted as qualified.',
}
(output / 'leaf_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'status': 'emitted; Lambdapi not run', 'targets': list(targets)}, indent=2))
