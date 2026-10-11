#!/usr/bin/env python3
"""Adapt existing displayed products and evaluation to the Cartesian Hom.

NON-LIBRARY. Preserve the product-family composite, raw FF/GG arguments,
component rules and universal-property owners. The two off-diagonal
projection functors use the corrected coefficient mapping profile; section
and transport evaluation retain their bodies through the existing inclusion.
"""
import hashlib
import json
from pathlib import Path
import re
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'displayed_op_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_displayed_op'
    prior = json.loads((audit / 'displayed_op_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']

    for side in ('L', 'R'):
        pattern = (r'(?m)^rule @tapp1_func\n[\s\S]*?'
                   + r'\(@Product_proj' + side + r'_funcd \$K \$B \$C\)\n'
                   + r'[\s\S]*?;\n')
        # Limit discovery to this owner, so a preceding unrelated rule can
        # never be swallowed by the multiline pattern.
        start = source.index('// Fixed-base fibrewise-product structural owners.')
        end = source.index('// 8c. Section categories and Pi action', start)
        block = source[start:end]
        rules = list(re.finditer(r'(?m)^rule\b[\s\S]*?;\n', block))
        matches = [m for m in rules if re.fullmatch(pattern.removeprefix('(?m)'), m[0])]
        assert len(matches) == 1, (side, len(matches))
        m = matches[0]
        changed = m[0].replace('Functor_cat', 'Functor_cart_cat')
        changed = changed.replace('@comp_cat_con_func', '@comp_cat_con_cart_func')
        assert changed != m[0]
        source = source[:start+m.start()] + changed + source[start+m.end():]

    anchor = '// 8c. Section categories and Pi action'
    assert source.count(anchor) == 1
    source = source.replace(anchor,
        (audit / 'displayed_product_controls.lpfragment').read_text() + '\n' + anchor)

    def replace(old, new):
        nonlocal source
        assert source.count(old) == 1, (old, source.count(old))
        source = source.replace(old, new)

    replace('''≔ comp_cat_fapp0
     (@fapp0_func Terminal_cat (Fibre_cat E k) Terminal_obj)
     (@tapp0_func K Cat_cat (@Const_catd K Terminal_cat) E k);''', '''≔ comp_cat_fapp0
     (@fapp0_func Terminal_cat (Fibre_cat E k) Terminal_obj)
     (comp_cat_fapp0
       (cart_functor_include Terminal_cat (Fibre_cat E k))
       (@tapp0_func K Cat_cat (@Const_catd K Terminal_cat) E k));''')
    replace('''≔ comp_cat_fapp0
     (@fapp0_func (Fibre_cat E x) (Fibre_cat E y) u)
     (@fapp1_func K Cat_cat E x y);''', '''≔ comp_cat_fapp0
     (@fapp0_func (Fibre_cat E x) (Fibre_cat E y) u)
     (comp_cat_fapp0
       (cart_functor_include (Fibre_cat E x) (Fibre_cat E y))
       (@fapp1_func K Cat_cat E x y));''')
    evaluation_end = '// General endpoint notation for dependent homs along a displayed functor.'
    replace(evaluation_end,
        (audit / 'displayed_evaluation_controls.lpfragment').read_text() + '\n' + evaluation_end)
    output = root / 'tmp/probes/strict_default_displayed_product'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'emdash3_2.lp').write_text(source)
    (output / 'owner_prefix.lp').write_text(source[:source.index(anchor)])
    (output / 'evaluation_prefix.lp').write_text(source[:source.index(evaluation_end)])
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    files = ('displayed_product_migration.py', 'displayed_product_controls.lpfragment',
             'displayed_evaluation_controls.lpfragment')
    manifest = {
        'status': 'non-library existing-consumer adaptation; full integration remains open',
        'displayedOpInputSha256': prior['outputs']['emdash3_2.lp'],
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in files},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in ('emdash3_2.lp', 'owner_prefix.lp', 'evaluation_prefix.lp', 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted displayed-product consumer adaptation.')


if __name__ == '__main__':
    main()
