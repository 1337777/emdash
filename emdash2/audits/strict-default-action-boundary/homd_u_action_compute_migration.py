#!/usr/bin/env python3
"""Emit u-action normal-form diagnostics from the unchanged checked owner."""
import hashlib
import json
from pathlib import Path

audit = Path(__file__).resolve().parent
root = audit.parents[1]
output = root / 'tmp/probes/homd_u_action'
digest = lambda data: hashlib.sha256(data).hexdigest()
manifest_path = output / 'manifest.json'
prior = json.loads(manifest_path.read_text())
owner = output / 'owner.lp'
assert digest(owner.read_bytes()) == prior['outputs']['owner.lp']
receipt_path = root / 'logs/check-runs/20261013T172401Z-a7ec7a93e0bf430cbdbff1ff323ee86e.json'
receipt = json.loads(receipt_path.read_text())
assert receipt['outcome'] == 'passed-fresh'
assert receipt['inputs'][receipt['target']] == digest(owner.read_bytes())
fragment = audit / 'homd_u_action_compute.lpfragment'
source = owner.read_text() + '\n' + fragment.read_text()
target = output / 'compute_source.lp'
if target.exists():
    assert target.read_text() == source, 'preserve previous diagnostic bytes'
target.write_text(source)
record = {
    'status': 'unchecked normalization diagnostic; no checker run',
    'sourceInputs': {str(p.relative_to(root)): digest(p.read_bytes())
                     for p in (Path(__file__), manifest_path, owner, receipt_path, fragment)},
    'outputs': {'compute_source.lp': digest(source.encode())},
    'queries': 'Five compute queries, followed by two type queries; no new declaration, rewrite or assertion.',
}
(output / 'compute_manifest.json').write_text(json.dumps(record, indent=2) + '\n')
print('Emitted compute_source.lp; original targets unchanged; Lambdapi not run.')
