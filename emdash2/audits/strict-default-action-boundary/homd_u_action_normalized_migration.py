#!/usr/bin/env python3
"""Make the measured remaining source-control classifier explicit."""
import hashlib
import json
from pathlib import Path

audit = Path(__file__).resolve().parent
root = audit.parents[1]
output = root / 'tmp/probes/homd_u_action'
digest = lambda data: hashlib.sha256(data).hexdigest()
prior_path = output / 'leaf_manifest.json'
prior = json.loads(prior_path.read_text())
old = output / 'leaf_law_controls.lp'
data = old.read_bytes()
assert digest(data) == prior['outputs'][old.name]
receipt_path = root / 'logs/check-runs/20261013T174505Z-9e1b191ec79144ffb96aa7a53adb9293.json'
receipt = json.loads(receipt_path.read_text())
assert receipt['outcome'] == 'failed'
assert receipt['inputs'][receipt['target']] == digest(data)
before = '@fapp1_func _ _ (@homd_id_src_func K E x) u1 u0'
after = ('@fapp1_func (Op_cat (Fibre_cat E x)) (@Homd_section_cat K E x) '
         '(@homd_id_src_func K E x) u1 u0')
source = data.decode()
assert source.count(before) == 1, 'only the first full-action comparison remains implicit'
source = source.replace(before, after, 1)
target = output / 'normalized_leaf_law_controls.lp'
if target.exists():
    assert target.read_text() == source, 'preserve prior normalized-control target'
target.write_text(source)
manifest = {
    'status': 'unchecked exact source-control annotation correction; no checker run',
    'sourceInputs': {str(p.relative_to(root)): digest(p.read_bytes())
                     for p in (Path(__file__), prior_path, old, receipt_path)},
    'outputs': {target.name: digest(source.encode())},
    'change': 'One source-control full-action application now has the same explicit Op fibre and section classifiers as the successful Q1 compute. No other declaration, rule, assertion or observation changes.',
}
(output / 'normalized_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(target.name + ' emitted; one annotation correction; Lambdapi not run.')
