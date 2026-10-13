#!/usr/bin/env python3
"""Reuse the existing product-prof closed core before the whole Homd owner.

NON-LIBRARY. Product and curried carriers stay distinct. This stage selects
Cartesian module transformations for the coefficient's closed core.
"""
import hashlib
import json
from pathlib import Path
import re
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'q_represented_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_q_represented'
    prior = json.loads((audit / 'q_represented_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']
    moved = []

    def take(start, end):
        nonlocal source
        assert source.count(start) == 1, start
        i = source.index(start)
        j = source.index(end, i)
        result = source[i:j]
        source = source[:i] + '// Existing owner moved before Q/Homd.\n\n' + source[j:]
        return result

    def symbol(name):
        nonlocal source
        ms = list(re.finditer(r'(?m)^(?:injective |constant )?symbol ' + re.escape(name) + r'\b[\s\S]*?;\n', source))
        assert len(ms) == 1, (name, len(ms))
        m = ms[0]
        source = source[:m.start()] + '// ' + name + ' moved before Q/Homd.\n' + source[m.end():]
        moved.append(name)
        return m[0]

    classifiers = take('// Profunctor base: A^op × B.', '// 18b. Opposite profunctors and fixed-endpoint duality')
    moved.extend(('Prof_base', 'Prof_cat', 'Prof', 'Prof_reindex_base_func', 'ProfMap'))
    classifiers = classifiers.replace('Obj (Catd_cat (Product_cat (Op_cat $A) $B))',
                                       'Obj (Functor_cart_cat (Product_cat (Op_cat $A) $B) Cat_cat)')
    classifiers = classifiers.replace('↪ @Functord_cat (Product_cat (Op_cat $A) $B) $P $Q;',
                                       '↪ Hom_cat (Functor_cart_cat (Product_cat (Op_cat $A) $B) Cat_cat) $P $Q;')
    classifiers = classifiers.replace('≡ Catd_cat (Product_cat $A0 $B0)',
                                       '≡ Functor_cart_cat (Product_cat $A0 $B0) Cat_cat')
    classifiers = classifiers.replace('Vertical hom projection: profunctor maps are natural family morphisms.',
                                       'Vertical hom projection: coefficient module maps use Cartesian naturality.')
    classifiers = classifiers.replace('// identities and composition remain owned by `id_funcd` and\n// `comp_catd_fapp0`.',
                                       '// identities and composition remain native in Prof_cat; its module\n// transformations now use the Cartesian profile.')
    opposite = take('// 18b. Opposite profunctors and fixed-endpoint duality',
                    '// 18c. Endpoint reindexing and product-base action')
    moved.extend(('Op_prof', 'Op_prof_func', 'Op_prof_map'))
    assert opposite.count('(Functor_cat\n') == 1
    opposite = opposite.replace('(Functor_cat\n', '(Functor_cart_cat\n')
    old = '''@Pullback_catd_func
      (Product_cat $B (Op_cat $A))
      (Product_cat (Op_cat $A) $B)
      (@Product_swap_func $B (Op_cat $A))'''
    new = '''@comp_cat_con_cart_func
      (Product_cat $B (Op_cat $A))
      (Product_cat (Op_cat $A) $B) Cat_cat
      (@Product_swap_func $B (Op_cat $A))'''
    assert opposite.count(old) == 1
    opposite = opposite.replace(old, new)
    core = classifiers + '\n' + opposite + '\n' + symbol('Prof_reindex')
    core += '\n' + take('// Object/fibre projection of profunctor reindexing.',
                         '// Full base-arrow action of reindexing.')
    for name in ('Hom_prof_along', 'Hom_prof', 'Companion_prof', 'Conjoint_prof', 'Prof_tensor'):
        core += '\n' + symbol(name)
    core += '\n' + take('/*\n  Fixed-endpoint tensor map action.',
                         '// Compose shaped elements through a common middle probe M.')
    moved.extend(('Prof_tensor_map', 'Prof_tensor_func'))
    for name in ('Prof_imply_cov', 'Prof_eval_cov_map', 'Prof_lambda_cov_map'):
        core += '\n' + symbol(name)
    core += '\n' + take('// Covariant beta/eta: lambda(eval(t))',
                         '/*\n  Contravariant profunctor implication.')
    core += '\n' + (audit / 'q_closed_representable.lpfragment').read_text()
    anchor = '// NON-LIBRARY structural coefficient candidate.'
    assert source.count(anchor) == 1
    source = source.replace(anchor, core + '\n' + anchor)
    anchor = '// The y-section is the existing transformation category in the coefficient.'
    assert source.count(anchor) == 1
    source = source.replace(anchor, (audit / 'q_closed_bridge.lpfragment').read_text() + '\n' + anchor)
    marker = '// 14. Section action over dependent homs'
    source = source.replace(marker, (audit / 'q_closed_controls.lpfragment').read_text() + '\n' + marker)
    output = root / 'tmp/probes/strict_default_q_closed'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'emdash3_2.lp').write_text(source)
    (output / 'owner_prefix.lp').write_text(source[:source.index(marker)])
    boundary = (audit / 'q_closed_boundaries.lpfragment').read_text()
    starts = ('// PRESENTATION ROUNDTRIP', '// COMPOSITION BODY', '// COUNit SOURCE')
    targets = ('roundtrip_boundary.lp', 'composition_boundary.lp', 'counit_boundary.lp')
    for i, (start, target) in enumerate(zip(starts, targets)):
        begin = boundary.index(start)
        end = boundary.index(starts[i + 1]) if i + 1 < len(starts) else len(boundary)
        (output / target).write_text(source[:source.index(marker)] + '\n' + boundary[begin:end])
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    names = ('q_closed_migration.py', 'q_closed_representable.lpfragment',
             'q_closed_bridge.lpfragment', 'q_closed_controls.lpfragment',
             'q_closed_boundaries.lpfragment', 'q_closed_counit_model.py')
    manifest = {
        'status': 'non-library reuse of Cartesian product-prof closed core; Q comparison/lift still require qualification',
        'qRepresentedInputSha256': prior['outputs']['emdash3_2.lp'],
        'movedSymbols': moved,
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in names},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in ('emdash3_2.lp', 'owner_prefix.lp', 'lambdapi.pkg', *targets)},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted existing Cartesian product-prof closed core before Homd.')


if __name__ == '__main__':
    main()
