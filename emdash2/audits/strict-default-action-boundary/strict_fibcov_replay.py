#!/usr/bin/env python3
"""Emit the first whole-family consumer of the strict displayed-map comparison.

NON-LIBRARY. This does not qualify a Q coefficient or the outer Homd root.
"""
import hashlib
import json
from pathlib import Path
import runpy
import subprocess


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clause(source, marker):
    assert source.count(marker) == 1, marker
    start = source.index(marker)
    return source[start:source.index(';', start)+1]+'\n'


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    evidence = audit/'strict_displayed_maps_verification.json'
    donor = json.loads(evidence.read_text())
    for name, expected in donor['authoringInputs'].items():
        assert sha(root/name) == expected, name
    runpy.run_path(str(audit/'strict_displayed_maps_replay.py'), run_name='__main__')
    source = root/'tmp/probes/strict_displayed_maps/candidate.lp'
    assert sha(source) == donor['outputs']['candidate.lp']
    body = source.read_text()
    pin = donor['nativeDeclarationSourcePin']
    core = subprocess.check_output(['git','show',pin+':emdash2/emdash3_2.lp'],cwd=root,text=True)
    native = clause(core, 'symbol Fibre_cat [K : Cat]')
    native += clause(core, 'symbol fib_cov_tapp0_func [K : Cat]')
    native += clause(core, 'symbol comp_cat_cov_func [X Y Z : Cat]')
    files = ('strict_fibcov.lpfragment', 'strict_fibcov_controls.lpfragment',
             'strict_fibcov_readings.lpfragment')
    parts = {name:(audit/name).read_text() for name in files}
    owner = '// Native one-leg controls.'
    assert body.count(owner) == 1
    structure = parts[files[0]]
    no_component = structure.replace(clause(structure,'rule @tapp0_fapp0'), '')
    no_composition = structure.replace(clause(structure,'rule @comp_fapp0'), '')
    no_action = structure
    for marker in ('rule @tapp1_func', 'rule @tapp1_fapp0'):
        no_action = no_action.replace(clause(no_action,marker), '')
    readings = parts[files[2]]
    split = '// Component-first reading'
    assert readings.count(split) == 1
    leaf = '// Evaluated index-composition reading.'
    assert readings.count(leaf) == 1
    out = root/'tmp/probes/strict_fibcov'; out.mkdir(parents=True,exist_ok=True)
    outputs = {}
    for name, (fragment, readings) in {
            'candidate.lp':(structure,parts[files[2]]),
            'no_component.lp':(no_component,parts[files[2]]),
            'no_composition.lp':(no_composition,parts[files[2]]),
            'no_action.lp':(no_action,parts[files[2]]),
            'no_readings.lp':(structure,''),
            'no_whole_reading.lp':(structure,readings[readings.index(split):]),
            'no_leaf_reading.lp':(structure,readings[:readings.index(leaf)]),
            'no_component_reading.lp':(structure,readings[:readings.index(split)]
                +readings[readings.index(leaf):])}.items():
        candidate = body.replace(owner,native+'\n'+fragment+'\n'+readings+'\n'+owner)
        candidate += '\n'+parts[files[1]]
        target = out/name; target.write_text(candidate); outputs[name]=sha(target)
    (out/'lambdapi.pkg').write_bytes((root/'lambdapi.pkg').read_bytes())
    authors = [Path(__file__)]+[audit/n for n in files]
    (out/'manifest.json').write_text(json.dumps({
        'status':'unqualified strict canonical transport-map consumer',
        'donorEvidence':str(evidence.relative_to(root)), 'donorEvidenceSha256':sha(evidence),
        'nativeSourcePin':pin,'nativeExcerptSha256':hashlib.sha256(native.encode()).hexdigest(),
        'authoringInputs':{str(p.relative_to(root)):sha(p) for p in authors},
        'outputs':outputs,
    },indent=2)+'\n')
    print('Emitted strict canonical transport-map consumer.')


if __name__ == '__main__':
    main()
