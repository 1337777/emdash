#!/usr/bin/env python3
"""Emit the whole-u Cartesian covariance consumer at its owning position.

Non-library. Reuses the exact separate-coefficient candidate and adds only
its u-parameter/component ladder and focused controls.
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
    evidence = audit / 'cart_family_verification.json'
    donor = json.loads(evidence.read_text())
    for path, expected in donor['authoringInputs'].items():
        assert sha(root / path) == expected, path
    runpy.run_path(str(audit / 'cart_family_replay.py'), run_name='__main__')
    source = root / 'tmp/probes/cart_family/candidate.lp'
    assert sha(source) == donor['outputSha256']
    owner = audit / 'cart_family_u.lpfragment'
    controls = audit / 'cart_family_u_controls.lpfragment'
    marker = '// Native one-leg controls.'
    body = source.read_text()
    assert body.count(marker) == 1
    out = root / 'tmp/probes/cart_family_u'
    out.mkdir(parents=True, exist_ok=True)
    target = out / 'candidate.lp'
    target.write_text(body.replace(marker, owner.read_text() + '\n' + marker)
                      + '\n' + controls.read_text())
    (out / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    (out / 'manifest.json').write_text(json.dumps({
        'status': 'non-library whole-u Cartesian covariance comparison',
        'donorEvidence': str(evidence.relative_to(root)), 'donorEvidenceSha256': sha(evidence),
        'authoringInputs': {str(p.relative_to(root)): sha(p) for p in (Path(__file__).resolve(), owner, controls)},
        'outputSha256': sha(target),
    }, indent=2) + '\n')
    print('Emitted one whole-u Cartesian covariance candidate.')


if __name__ == '__main__':
    main()
