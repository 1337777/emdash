#!/usr/bin/env python3
"""Emit observational precomposition-peak successors; never run Lambdapi."""
import hashlib
import json
from pathlib import Path
import re

audit = Path(__file__).resolve().parent
root = audit.parents[1]
digest = lambda data: hashlib.sha256(data).hexdigest()
prior_path = audit / 'homd_u_normalization_verification.json'
prior = json.loads(prior_path.read_text())
donor = root / 'tmp/probes/homd_u_normalization/combined_controls.lp'
source = donor.read_text()
assert digest(source.encode()) == prior['outputs'][donor.name]
assert prior['checks'][donor.name]['outcome'] == 'passed-fresh'
failed_path = root / 'logs/check-runs/20261013T182459Z-36201fe106644757be405bd611a56254.json'
failed = json.loads(failed_path.read_text())
assert failed['outcome'] == 'failed'
assert digest((root / failed['target']).read_bytes()) == failed['inputs'][failed['target']]
fragments = [audit / 'homd_u_peaks_precomp_observations.lpfragment',
             audit / 'homd_u_peaks_curry_observation.lpfragment']
for path in fragments:
    assert not re.search(r'(?m)^(?:rule|unif_rule|(?:injective |constant )?symbol)\b', path.read_text())
targets = {'precomp_observations.lp': source + '\n' + fragments[0].read_text(),
           'curry_observation.lp': source + '\n' + fragments[1].read_text()}
output = root / 'tmp/probes/homd_u_peaks'
output.mkdir(parents=True, exist_ok=True)
for name, body in targets.items():
    target = output / name
    if target.exists():
        assert target.read_text() == body, 'preserve previous successor'
    target.write_text(body)
(output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
inputs = [Path(__file__), prior_path, donor, failed_path, root / failed['target'],
          root / 'lambdapi.pkg', *fragments]
manifest = {
    'status': 'unchecked observational successors; no new semantic rule or operational proof argument',
    'sourceInputs': {str(path.relative_to(root)): digest(path.read_bytes()) for path in inputs},
    'donorReceipt': prior['checks'][donor.name]['receipt'],
    'preservedFailure': str(failed_path.relative_to(root)),
    'outputs': {name: digest(body.encode()) for name, body in targets.items()},
    'scope': 'Existing triple associativity observation retained; generic and Cat-valued identity-beta use eq_ap of ordinary identity-family precomposition comparison. Contextual curry(Eval) observation is independent.',
    'checkerInvoked': False,
}
(output / 'observations_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print('Emitted precomp_observations.lp and independent curry_observation.lp; no checker run.')
