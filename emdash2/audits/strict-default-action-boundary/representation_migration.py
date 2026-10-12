#!/usr/bin/env python3
"""Recover a Cartesian representation view from existing ordinary Hom/curry.

NON-LIBRARY. Keep the public ambient hom_int and represented transport
owners. This is not currying a combined dependent-Hom context.
"""
import hashlib
import json
from pathlib import Path
import re
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'sigma_total_op_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_sigma_total_op'
    prior = json.loads((audit / 'sigma_total_op_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']

    def replace(old, new):
        nonlocal source
        assert source.count(old) == 1, (old, source.count(old))
        source = source.replace(old, new)

    start = source.index('// Identity/unit hom profunctor, the uncurried/product form of hom_int(id_X).')
    end = source.index('/*\n  Stable generic action of a displayed hom-family.', start)
    unit = source[start:end]
    assert unit.count(': τ (Prof X X);') == 1
    unit = unit.replace(': τ (Prof X X);',
                        ': τ (Functor (Product_cat (Op_cat X) X) Cat_cat);')
    unit = unit.replace('@Hom_tele_func', '@Hom_cart_tele_func')
    source = source[:start] + '// Unit_prof and its ordinary Hom actions are declared before Cartesian curry.\n\n' + source[end:]
    anchor = '// Semantic curry package through the product-pair telescope.'
    replace(anchor, unit + (audit / 'representation_unit_controls.lpfragment').read_text() + '\n' + anchor)

    # This object projection does not depend on the later constant-section
    # owners used by the telescope's other component views.
    old = '''// Object projection: Product_pair_tele_func[x] ↪ (const_B(x),id_B).
rule @fapp0 _ _
      (@Product_pair_tele_func $A $B) $x
  ↪ Struct_sigma (@Const_func $B $A $x) (@id_func $B);
'''
    replace(old, '// Product-pair object projection moved before Cartesian curry.\n')
    replace(anchor, old + '\n' + anchor)

    anchor = '// 11a. Representables'
    representation = '''// Derived Cartesian representation view. Ambient hom_int and its existing
// displayed transport owner remain available for non-strict transfor consumers.
symbol Rep_cart_func [Z : Cat]
  : τ (Functor (Op_cat Z) (Functor_cart_cat Z Cat_cat))
≔ @curry_func (Op_cat Z) Z Cat_cat (@Unit_prof Z);

'''
    typed = (audit / 'representation_type_controls.lpfragment').read_text()
    computations = (audit / 'representation_computation_controls.lpfragment').read_text()
    replace(anchor, (audit / 'representation_projection.lpfragment').read_text() + '\n'
            + representation + typed + '\n' + computations + '\n' + anchor)
    output = root / 'tmp/probes/strict_default_representation'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'emdash3_2.lp').write_text(source)
    (output / 'unit_prefix.lp').write_text(source[:source.index('// Semantic curry package through the product-pair telescope.')])
    (output / 'typing_prefix.lp').write_text(source[:source.index(computations)])
    (output / 'computation_prefix.lp').write_text(source[:source.index(anchor)])
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    files = ('representation_migration.py', 'representation_unit_controls.lpfragment',
             'representation_projection.lpfragment',
             'representation_type_controls.lpfragment', 'representation_computation_controls.lpfragment')
    manifest = {
        'status': 'non-library derived Cartesian representation; computation/whole comparison require checks',
        'sigmaInputSha256': prior['outputs']['emdash3_2.lp'],
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in files},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in ('emdash3_2.lp', 'unit_prefix.lp', 'typing_prefix.lp',
                              'computation_prefix.lp', 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted ordinary unit Hom and derived Cartesian representation.')


if __name__ == '__main__':
    main()
