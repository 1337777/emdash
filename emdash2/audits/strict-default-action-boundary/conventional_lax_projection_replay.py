#!/usr/bin/env python3
"""Emit retained-head projection comparisons after the conventional-lax pilot.

NON-LIBRARY. Exact donor and owner insertion are checked; no confluence or
full corrected foundation is claimed from these typed comparisons.
"""
import hashlib
import json
from pathlib import Path
import runpy


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    evidence = json.loads((audit / 'conventional_lax_verification.json').read_text())
    for name, expected in evidence['authoringInputs'].items():
        assert sha(root / name) == expected, name
    runpy.run_path(str(audit / 'conventional_lax_replay.py'), run_name='__main__')
    old = root / 'tmp/probes/conventional_lax_default'
    reading = (audit / 'conventional_lax_projection_readings.lpfragment').read_text().rstrip() + '\n\n'
    controls = (audit / 'conventional_lax_projection_controls.lpfragment').read_text()
    out = root / 'tmp/probes/conventional_lax_projection'
    out.mkdir(parents=True, exist_ok=True)
    outputs = {}
    ordinary_start = reading.index('// Proof-time pre/right readings')
    for name, source_name, selected_reading in (
            ('no_reading.lp', 'ordinary.lp', ''),
            ('only_ordinary.lp', 'ordinary.lp', reading[ordinary_start:]),
            ('only_opposite.lp', 'ordinary.lp', reading[:ordinary_start]),
            ('ordinary.lp', 'ordinary.lp', reading),
            ('full_intrinsic.lp', 'full_intrinsic.lp', reading),
            ('legacy_op_adverse.lp', 'legacy_op_adverse.lp', reading)):
        p = old / source_name
        assert sha(p) == evidence['outputs'][source_name], source_name
        body = p.read_text()
        anchor = '// NON-LIBRARY candidate: conventional lax is the default Transf profile.'
        assert body.count(anchor) == 1
        if selected_reading:
            body = body.replace(anchor, selected_reading + '\n' + anchor)
        (out / name).write_text(body + '\n' + controls)
        outputs[name] = sha(out / name)
    (out / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    (out / 'manifest.json').write_text(json.dumps({
        'status': 'unqualified typed projection-order candidates',
        'donorOutputs': evidence['outputs'],
        'authoringInputs': {p.name: sha(p) for p in (Path(__file__),
            audit / 'conventional_lax_projection_controls.lpfragment',
            audit / 'conventional_lax_projection_readings.lpfragment')},
        'outputs': outputs}, indent=2) + '\n')
    print('Emitted conventional-lax projection-order candidates.')


if __name__ == '__main__':
    main()
