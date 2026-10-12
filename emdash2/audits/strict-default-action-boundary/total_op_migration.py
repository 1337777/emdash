#!/usr/bin/env python3
"""Qualify R/total duality and the existing negative Pi/Hom_catd interface.

NON-LIBRARY. The original whole Homd/Q and later action consumers remain in
the full source, so a prefix cannot be mistaken for completed integration.
"""
import hashlib
import json
from pathlib import Path
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'mapping_constructor_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_mapping_constructor'
    prior = json.loads((audit / 'mapping_constructor_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']

    def replace(old, new):
        nonlocal source
        assert source.count(old) == 1, (old, source.count(old))
        source = source.replace(old, new)

    anchor = '// Reverse dimension two only. The existing Op_cat is the dimension-one'
    replace(anchor, (audit / 'co_above2_category.lpfragment').read_text() + '\n' + anchor)
    anchor = '// Terminal category and points-as-functors are needed to derive unary homs from'
    replace(anchor, (audit / 'co_above2_functor.lpfragment').read_text() + '\n' + anchor)
    replace('rule Op_cat Terminal_cat ↪ Terminal_cat;',
            'rule Op_cat Terminal_cat ↪ Terminal_cat;\nrule CoAbove2_cat Terminal_cat ↪ Terminal_cat;')
    replace('''rule Op_cat (Product_cat $A $B)
  ↪ Product_cat (Op_cat $A) (Op_cat $B);''', '''rule Op_cat (Product_cat $A $B)
  ↪ Product_cat (Op_cat $A) (Op_cat $B);
rule CoAbove2_cat (Product_cat $A $B)
  ↪ Product_cat (CoAbove2_cat $A) (CoAbove2_cat $B);''')
    head_end = '// 3f. Internalized universe-level constructor packages'
    replace(head_end, (audit / 'total_op_head_controls.lpfragment').read_text() + '\n' + head_end)

    family_end = 'injective symbol Op_catd [K : Cat] (E : τ (Catd K))'
    replace(family_end,
        (audit / 'total_op_family.lpfragment').read_text() + '\n'
        + (audit / 'total_op_family_controls.lpfragment').read_text() + '\n' + family_end)

    # Keep the original Hom_catd/Transf_catd outline. Only their negative
    # section uses total fibre opposite; ordinary contravariance remains T.
    start = source.index('// Mixed-variance hom family for two sections of a displayed family.')
    end = source.index('// 11. Representables and presheaf-family classifiers', start)
    block = source[start:end].replace('Op_catd', 'TotalOp_catd')
    block = block.replace('@piapp0 $K (@TotalOp_catd',
                          '@piapp0 (CoAbove2_cat $K) (@TotalOp_catd')
    block = block.replace('(@Op_func $K (Op_cat Cat_cat) $X)',
                          '(@TotalOp_func (CoAbove2_cat $K) (TotalOp_cat Cat_cat) $X)')
    old = '  ↪ Transf_cat\n'
    assert block.count(old) == 1
    block = block.replace(old,
        '  ↪ Hom_cat\n      (Functor_cart_cat (Fibre_cat $A $k) (Fibre_cat $B $k))\n')
    block += (audit / 'total_op_hom_family_controls.lpfragment').read_text() + '\n'
    source = source[:start] + block + source[end:]

    output = root / 'tmp/probes/strict_default_total_op'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'emdash3_2.lp').write_text(source)
    (output / 'head_prefix.lp').write_text(source[:source.index(head_end)])
    assertion_start = '// The two Hom classifiers normalize identically.'
    assert source.count(assertion_start) == 1
    bare = source[:source.index(assertion_start)] + '''assert [A B : Cat] (F : τ (Functor A B))
  [x y : τ (Obj A)] (p : τ (Hom A x y)) ⊢
  @fapp1_fapp0 (TotalOp_cat A) (TotalOp_cat B) (@TotalOp_func A B F) y x p
  ≡ @fapp1_fapp0 A B F x y p;
'''
    (output / 'bare_action_assertion.lp').write_text(bare)
    (output / 'family_prefix.lp').write_text(source[:source.index(family_end)])
    (output / 'hom_prefix.lp').write_text(source[:source.index('// 11. Representables and presheaf-family classifiers')])
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    files = ('total_op_migration.py', 'total_op_section_model.py',
             'co_above2_category.lpfragment', 'co_above2_functor.lpfragment',
             'total_op_head_controls.lpfragment', 'total_op_family.lpfragment',
             'total_op_family_controls.lpfragment', 'total_op_hom_family_controls.lpfragment')
    manifest = {
        'status': 'non-library total-opposite/negative-section candidate; complete Homd integration remains open',
        'mappingInputSha256': prior['outputs']['emdash3_2.lp'],
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in files},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in ('emdash3_2.lp', 'head_prefix.lp', 'bare_action_assertion.lp', 'family_prefix.lp',
                              'hom_prefix.lp', 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted total fibre opposite and existing Pi/Hom_catd candidate.')


if __name__ == '__main__':
    main()
