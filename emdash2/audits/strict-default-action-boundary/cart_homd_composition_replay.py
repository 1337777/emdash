#!/usr/bin/env python3
"""Emit the represented-composition consumer of the extracted Homd square."""
import hashlib
import json
from pathlib import Path
import runpy


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    evidence = audit / 'cart_homd_ordinary_verification.json'
    donor = json.loads(evidence.read_text())
    for path, expected in donor['authoringInputs'].items():
        assert sha(root / path) == expected, path
    runpy.run_path(str(audit / 'cart_homd_ordinary_replay.py'), run_name='__main__')
    source = root / 'tmp/probes/cart_homd_ordinary/candidate.lp'
    assert sha(source) == donor['outputSha256']
    owner = audit / 'cart_homd_composition.lpfragment'
    controls = audit / 'cart_homd_composition_controls.lpfragment'
    functor = audit / 'cart_homd_composition_functor.lpfragment'
    body = source.read_text()
    functor_marker = '// Generic object projection for Cat-valued postcomposition:'
    assert body.count(functor_marker) == 1
    body = body.replace(functor_marker, functor.read_text() + '\n' + functor_marker)
    marker = '// Native one-leg controls.'
    assert body.count(marker) == 1
    out = root / 'tmp/probes/cart_homd_composition'
    out.mkdir(parents=True, exist_ok=True)
    target = out / 'candidate.lp'
    target.write_text(body.replace(marker, owner.read_text() + '\n' + marker)
                      + '\n' + controls.read_text())
    (out / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    (out / 'manifest.json').write_text(json.dumps({
        'status': 'non-library represented-composition beta for Homd',
        'donorEvidence': str(evidence.relative_to(root)),
        'donorEvidenceSha256': sha(evidence),
        'authoringInputs': {str(p.relative_to(root)): sha(p)
                           for p in (Path(__file__).resolve(), owner, controls, functor)},
        'outputSha256': sha(target),
    }, indent=2) + '\n')
    print('Emitted one represented-composition Homd candidate.')


if __name__ == '__main__':
    main()
