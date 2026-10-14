#!/usr/bin/env python3
"""Emit one Cartesian-coefficient family/canonical-Hom comparison.

Non-library. Public Hom(Cat)=Functor_cat is retained; the donor's separate
joint Cartesian composition boundary is not claimed to be resolved.
"""
import hashlib
import json
from pathlib import Path
import runpy
import subprocess


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    evidence = audit / 'strict_displayed_maps_verification.json'
    donor = json.loads(evidence.read_text())
    for path, expected in donor['authoringInputs'].items():
        assert sha(root / path) == expected, path
    runpy.run_path(str(audit / 'strict_displayed_maps_replay.py'), run_name='__main__')
    source = root / 'tmp/probes/strict_displayed_maps/candidate.lp'
    assert sha(source) == donor['outputs']['candidate.lp']
    body = source.read_text()
    profile_path = audit / 'cartesian_profile.lpfragment'
    profile = profile_path.read_text()
    profile = profile[profile.index('// NON-LIBRARY'):profile.index('assert [A B : Cat]')]
    pin = 'f8af1fca472657ff1598c639eb29c0566e7b2ec0'
    native = subprocess.check_output(['git', 'show', pin + ':emdash2/emdash3_2.lp'], cwd=root, text=True)
    marker = '// Component of tele-postcomposition in an arbitrary ambient category.'
    assert native.count(marker) == 1 and marker not in body
    start = native.index(marker)
    component = native[start:native.index(';', start) + 1] + '\n'
    unit_owner = '/*\n  Proof-time projection-order comparison for the capped precomposition hom'
    owner = '// Native one-leg controls.'
    assert body.count(unit_owner) == 1 and body.count(owner) == 1
    files = [audit / name for name in ('cart_family_core.lpfragment',
             'cart_family_controls.lpfragment', 'cart_family_unit.lpfragment',
             'cart_family_precomp_reading.lpfragment')]
    reading = 'unif_rule\n  @hom_precomp_along_fapp1_fapp0\n'
    assert body.count(reading) == 1
    start = body.index(reading)
    stop = body.index('];', start) + 2
    old_reading = body[start:stop]
    body = body[:start] + files[3].read_text() + body[stop:]
    body = body.replace(unit_owner, files[2].read_text() + '\n' + unit_owner)
    body = body.replace(owner, component + '\n' + profile + '\n' + files[0].read_text() + '\n' + owner)
    body += '\n' + files[1].read_text()
    out = root / 'tmp/probes/cart_family'
    out.mkdir(parents=True, exist_ok=True)
    target = out / 'candidate.lp'
    target.write_text(body)
    (out / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    (out / 'manifest.json').write_text(json.dumps({
        'status': 'non-library separate Cartesian coefficient comparison',
        'donorEvidence': str(evidence.relative_to(root)), 'donorEvidenceSha256': sha(evidence),
        'nativeSourcePin': pin,
        'nativeComponentSha256': hashlib.sha256(component.encode()).hexdigest(),
        'cartProfileExcerptSha256': hashlib.sha256(profile.encode()).hexdigest(),
        'originalPrecompositionReadingSha256': hashlib.sha256(old_reading.encode()).hexdigest(),
        'authoringInputs': {str(p.relative_to(root)): sha(p) for p in [Path(__file__), profile_path] + files},
        'outputSha256': sha(target),
    }, indent=2) + '\n')
    print('Emitted one Cartesian-coefficient family candidate.')


if __name__ == '__main__':
    main()
