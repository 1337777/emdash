#!/usr/bin/env python3
"""Join represented Q laws at their native owner; retain semantic boundaries."""
import hashlib
import json
from pathlib import Path
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'q_homd_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_q_homd'
    prior = json.loads((audit / 'q_homd_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']
    anchor = '// Fixed postcomposition uses the existing ambient whiskering, so a general'
    assert source.count(anchor) == 1
    laws = (audit / 'q_represented_laws.lpfragment').read_text()
    derivations = (audit / 'q_represented_derivations.lpfragment').read_text()
    source = source.replace(anchor, derivations + '\n' + laws + '\n' + anchor)
    marker = '// 14. Section action over dependent homs'
    end = source.index(marker)
    boundaries = (audit / 'q_homd_coefficient_boundary.lpfragment').read_text()
    source = source[:end] + boundaries + '\n' + source[end:]
    controls = audit / 'q_represented_controls.lpfragment'
    source = source.replace(marker, controls.read_text() + '\n' + marker)
    output = root / 'tmp/probes/strict_default_q_represented'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'emdash3_2.lp').write_text(source)
    (output / 'owner_prefix.lp').write_text(source[:source.index(marker)])
    (output / 'no_laws.lp').write_text(source[:source.index(marker)].replace(laws, ''))
    unguarded = laws
    for left, right in (('$B', '$C'), ('$A', '$B')):
        old = f'{left} {right}\n        (Functor_cart_cat (Op_cat {right}) Cat_cat)'
        assert unguarded.count(old) == 1
        unguarded = unguarded.replace(old, f'{left} {right} _')
    (output / 'without_endpoint_guards.lp').write_text(
        source[:source.index(marker)].replace(laws, unguarded))
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    names = ['q_represented_migration.py', 'q_represented_laws.lpfragment',
             'q_represented_derivations.lpfragment', 'q_represented_controls.lpfragment']
    manifest = {
        'status': 'non-library represented coefficient law computation; complete coefficient/lift semantics remain open',
        'qHomdInputSha256': prior['outputs']['emdash3_2.lp'],
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in names},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in ('emdash3_2.lp', 'owner_prefix.lp', 'no_laws.lp',
                              'without_endpoint_guards.lp', 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted represented Q unit/composition candidate.')


if __name__ == '__main__':
    main()
