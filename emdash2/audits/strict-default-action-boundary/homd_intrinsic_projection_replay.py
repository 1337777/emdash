#!/usr/bin/env python3
"""Replay one intrinsic-action consumer of the whole Homd candidate.

Non-library; replay after changing its declared action or projection owners.
The imported coefficient contracts remain conditional, as in the donor.
"""
import hashlib
import json
from pathlib import Path
import runpy


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    donor_path = audit / 'homd_transposed_target_verification.json'
    donor = json.loads(donor_path.read_text())
    for path, expected in donor['authoringInputs'].items():
        assert sha(root / path) == expected, path
    runpy.run_path(str(audit / 'homd_transposed_target_replay.py'), run_name='__main__')
    source = root / 'tmp/probes/homd_transposed_target/candidate.lp'
    assert sha(source) == donor['outputs']['candidate.lp']
    owner = audit / 'homd_intrinsic_projection.lpfragment'
    controls = audit / 'homd_intrinsic_projection_controls.lpfragment'
    marker = '// Native one-leg controls.'
    body = source.read_text()
    assert body.count(marker) == 1
    output = root / 'tmp/probes/homd_intrinsic_projection'
    output.mkdir(parents=True, exist_ok=True)
    target = output / 'candidate.lp'
    target.write_text(body.replace(marker, owner.read_text() + '\n' + marker)
                      + '\n' + controls.read_text())
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    (output / 'manifest.json').write_text(json.dumps({
        'status': 'non-library intrinsic-action projection candidate',
        'donorEvidence': str(donor_path.relative_to(root)),
        'donorEvidenceSha256': sha(donor_path),
        'authoringInputs': {str(p.relative_to(root)): sha(p)
                           for p in (Path(__file__), owner, controls)},
        'outputSha256': sha(target),
    }, indent=2) + '\n')
    print('Emitted one intrinsic-action projection candidate.')


if __name__ == '__main__':
    main()
