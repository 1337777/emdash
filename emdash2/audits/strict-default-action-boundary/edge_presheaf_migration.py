#!/usr/bin/env python3
"""Correct the whole Edge and presheaf packages using the derived Cart view.

NON-LIBRARY. The old Homd target is kept in the full file as the next coupled
consumer, not silently replaced by a pointwise or combined-context contract.
"""
import hashlib
import json
from pathlib import Path
import re
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'representation_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_representation'
    prior = json.loads((audit / 'representation_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']

    def replace(old, new):
        nonlocal source
        assert source.count(old) == 1, (old, source.count(old))
        source = source.replace(old, new)

    replace('rule CoAt2_cat (CoAt2_cat $A) ↪ $A;', '''rule CoAt2_cat (CoAt2_cat $A) ↪ $A;
// Independent reversals of dimensions one and two commute.
rule Op_cat (CoAt2_cat $A) ↪ CoAt2_cat (Op_cat $A);''')
    replace('''symbol Edge_catd_func [Z : Cat]
  : τ (Functor (Op_cat Z) (Catd_cat Z))
≔ comp_cat_fapp0
     (@Op_catd_func Z)
     (@hom_int Z Z (@id Cat_cat Z));''', '''symbol Edge_catd_func [Z : Cat]
  : τ (Functor (CoAt2_cat (Op_cat Z)) (Functor_cart_cat (CoAt2_cat Z) Cat_cat))
≔ @comp_cat_fapp0
    (CoAt2_cat (Op_cat Z)) (CoAt2_cat (Functor_cart_cat Z Cat_cat))
    (Functor_cart_cat (CoAt2_cat Z) Cat_cat)
    (@Op_catd_func Z)
    (@CoAt2_func (Op_cat Z) (Functor_cart_cat Z Cat_cat) (@Rep_cart_func Z));''')
    replace('''symbol Presheaf_catd_func (K : Cat)
  : τ (Functor
      (Op_cat (Catd_cat (Op_cat K)))
      (Catd_cat K))''', '''symbol Presheaf_catd_func (K : Cat)
  : τ (Functor
      (Op_cat (Functor_cart_cat (Op_cat K) Cat_cat))
      (Catd_cat K))''')
    replace('''symbol HomPresheaf_catd_func [Z : Cat]
  : τ (Functor Z (Catd_cat (Op_cat Z)))
≔ comp_cat_fapp0
     (@Presheaf_catd_func (Op_cat Z))
     (@Op_func (Op_cat Z) (Catd_cat Z) (@Edge_catd_func Z));''', '''symbol HomPresheaf_catd_func [Z : Cat]
  : τ (Functor (CoAt2_cat Z) (Catd_cat (Op_cat (CoAt2_cat Z))))
≔ @comp_cat_fapp0
    (CoAt2_cat Z) (Op_cat (Functor_cart_cat (CoAt2_cat Z) Cat_cat))
    (Catd_cat (Op_cat (CoAt2_cat Z)))
    (@Presheaf_catd_func (Op_cat (CoAt2_cat Z)))
    (@Op_func (CoAt2_cat (Op_cat Z)) (Functor_cart_cat (CoAt2_cat Z) Cat_cat)
      (@Edge_catd_func Z));''')

    anchor = '// 12. Directed homd target and internal homd functor'
    replace(anchor, (audit / 'edge_presheaf_controls.lpfragment').read_text() + '\n' + anchor)
    output = root / 'tmp/probes/strict_default_edge_presheaf'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'emdash3_2.lp').write_text(source)
    (output / 'owner_prefix.lp').write_text(source[:source.index(anchor)])
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    files = ('edge_presheaf_migration.py', 'edge_presheaf_controls.lpfragment')
    manifest = {
        'status': 'non-library whole Edge/presheaf correction; Q/Homd target remains open',
        'representationInputSha256': prior['outputs']['emdash3_2.lp'],
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in files},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in ('emdash3_2.lp', 'owner_prefix.lp', 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted corrected whole Edge and presheaf packages.')


if __name__ == '__main__':
    main()
