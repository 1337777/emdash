#!/usr/bin/env python3
"""Correct the fixed mixed-family Hom(Cat) owner over the pinned prototype.

NON-LIBRARY. Keep later parameter/Homd declarations present in the full file.
Their profiles are not qualified by this fixed-family prefix.
"""
import hashlib
import json
from pathlib import Path
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'displayed_product_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_displayed_product'
    prior = json.loads((audit / 'displayed_product_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']

    start = source.index('// Fibre projection: Functor_catd(A,B)[k]')
    end = source.index('// Coherent evaluation for a constant-domain displayed functor family.', start)
    block = source[start:end]
    assert block.count('rule ') == 3
    block = block.replace('Functor_cat (', 'Functor_cart_cat (')
    block = block.replace('(Functor_cat\n', '(Functor_cart_cat\n')
    block = block.replace('@Hom_tele_func', '@Hom_cart_tele_func')
    source = source[:start] + block + source[end:]

    def replace(old, new):
        nonlocal source
        assert source.count(old) == 1, (old, source.count(old))
        source = source.replace(old, new)

    # Contravariant family reindexing reverses the naturality square. The
    # ordinary-base countermodel rejects the former raw same-profile input.
    # Use the existing Cartesian classifier here; the covariant B-parameter
    # remains the ambient displayed transformation category.
    replace('''      (Op_cat (Catd_cat (Op_cat K)))
      (Functor_cat (Catd_cat K) (Catd_cat K)));''', '''      (Op_cat (Functor_cart_cat (Op_cat K) Cat_cat))
      (Functor_cat (Catd_cat K) (Catd_cat K)));''')
    replace('''            (Op_cat (Catd_cat (Op_cat $K)))
            (Functor_cat (Catd_cat $K) (Catd_cat $K))''', '''            (Op_cat (Functor_cart_cat (Op_cat $K) Cat_cat))
            (Functor_cat (Catd_cat $K) (Catd_cat $K))''')
    replace('''      (@tapp0_fapp0 (Op_cat $K) Cat_cat $A' $A $k $L);''', '''      (@tapp0_fapp0 (Op_cat $K) Cat_cat $A' $A $k
        (@strict_transfor (Op_cat $K) Cat_cat $A' $A $L));''')

    # Existing product and constant-middle composition components now use
    # the same Hom(Cat) fibre type as the corrected family owner.
    start = source.index('// Pointwise distribution of a pair of mixed functors into a product target.')
    end = source.index('// Mixed-variance hom family for two sections of a displayed family.', start)
    block = source[start:end]
    block = block.replace('Functor_cat (', 'Functor_cart_cat (')
    block = block.replace('(Functor_cat\n', '(Functor_cart_cat\n')
    block = block.replace('@comp_cat_con_func', '@comp_cat_con_cart_func')
    source = source[:start] + block + source[end:]

    anchor = '// Internalized constructor package for mixed-variance functor families.'
    assert source.count(anchor) == 1
    source = source.replace(anchor,
        (audit / 'mixed_family_controls.lpfragment').read_text() + '\n' + anchor)
    parameter_end = '// Mixed-variance hom family for two sections of a displayed family.'
    replace(parameter_end,
        (audit / 'mixed_family_parameter_controls.lpfragment').read_text() + '\n' + parameter_end)
    output = root / 'tmp/probes/strict_default_mixed_family'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'emdash3_2.lp').write_text(source)
    (output / 'owner_prefix.lp').write_text(source[:source.index(anchor)])
    (output / 'parameter_prefix.lp').write_text(source[:source.index(parameter_end)])
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    files = ('mixed_family_migration.py', 'mixed_family_controls.lpfragment',
             'mixed_family_parameter_controls.lpfragment',
             'mixed_family_profile_models.py')
    manifest = {
        'status': 'non-library fixed mixed-family candidate; whole parameter and Homd repair remain open',
        'familyInputSha256': prior['outputs']['emdash3_2.lp'],
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in files},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in ('emdash3_2.lp', 'owner_prefix.lp', 'parameter_prefix.lp', 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted fixed mixed-family Cartesian Hom adaptation.')


if __name__ == '__main__':
    main()
