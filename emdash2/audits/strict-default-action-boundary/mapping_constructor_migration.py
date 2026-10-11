#!/usr/bin/env python3
"""Replace the invalid whole ambient mapping constructor by native Hom(Cat).

NON-LIBRARY. The valid fixed-source ambient constructor and fixed whiskering
remain. Variable-base family formation has Cartesian mapping fibres, and Pi
observes them through the existing inclusion.
"""
import hashlib
import json
from pathlib import Path
import re
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'precomposition_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_precomposition'
    prior = json.loads((audit / 'precomposition_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']

    def replace(old, new):
        nonlocal source
        assert source.count(old) == 1, (old, source.count(old))
        source = source.replace(old, new)

    replace('''// Internalized ordinary functor-category formation. The total package has no
// recoverable parameters; the partial stage is injective so equality of
// packages can recover the fixed source category.
//
// Surface/formula:
//   Functor_cat_func[A][B] = A ⊢ B.
constant symbol Functor_cat_func : τ (Functor (Op_cat Cat_cat) (Functor_cat Cat_cat Cat_cat));''', '''// Fixed-source ambient mapping-category formation remains valid. Its former
// whole contravariant source package had an unsupported higher profile.
// Cartesian whole formation uses the existing Hom(Cat) owner below.''')
    replace('''// First application of the binary constructor fixes the source category.
rule @fapp0 _ _ Functor_cat_func $A
  ↪ Functor_cat_fapp0_func $A;
// Second application yields the ordinary functor category `A ⊢ B`.''',
            '// Fixed-source application yields the ambient mapping category A ⊢ B.')

    start = source.index('// Internalized-x prerequisite: directed-family category formation as a')
    end = source.index('// Internalized pointwise opposite on directed families.', start)
    source = source[:start] + '// Variable-base family formation is declared after the native Hom owner.\n\n' + source[end:]
    formation = '''// Variable-base family formation uses Cartesian Hom(Cat). Its objects are
// the same default Cat-valued functors; its parameter transformations are strict.
symbol Catd_cat_func : τ (Functor (Op_cat Cat_cat) Cat_cat)
≔ @comp_cat_fapp0
     (Op_cat Cat_cat) (Catd_cat Cat_cat) Cat_cat
     (@fapp0_func Cat_cat Cat_cat Cat_cat)
     (@hom_int Cat_cat Cat_cat (@id_func Cat_cat));

// Contravariant family of these diagram classifiers, retaining all base cells.
symbol Catd_catd_con [L : Cat] (K : τ (Catd L)) : τ (Catd (Op_cat L))
≔ @comp_cat_fapp0 (Op_cat L) (Op_cat Cat_cat) Cat_cat
     Catd_cat_func (@Op_func L Cat_cat K);

'''
    anchor = '// Generic stable owner for the represented-object action of `hom_int`.'
    replace(anchor, formation + anchor)

    # The old comparison equated Cartesian Hom(Cat) precomposition with
    # ambient family reindexing. Its valid ambient counterpart is the actual
    # constant-section Hom action now used by comp_cat_con_func.
    replace('''unif_rule
  @hom_precomp_along_func Cat_cat Cat_cat (@id Cat_cat Cat_cat) Cat_cat $A $B $F
  ≡ @Pullback_catd_func $A $B $F
  ↪ [ tt ≡ tt ];''', '''unif_rule
  @fapp1_func _ _ (@Pullback_catd_func $A $B $F)
    (@Const_catd $B Terminal_cat) (@Const_catd $B Cat_cat)
  ≡ @Pullback_catd_func $A $B $F
  ↪ [ tt ≡ tt ];''')
    start = source.index('// Arrow action of the internalized Catd constructor. `Catd_cat_func` is a')
    end = source.index('// Pointwise projection for the hom-action of family pullback.', start)
    source = source[:start] + '// The Cartesian Catd constructor action now derives from Hom(Cat) evaluation.\n\n' + source[end:]

    # Preserve the existing Pi and section-reindexing operations. Their whole
    # variable-base package restricts its diagram argument via the inclusion.
    replace('''      Pi_int_funcd
  ↪ @Pi_func $K;''', '''      Pi_int_funcd
  ↪ @comp_cat_fapp0 (Functor_cart_cat $K Cat_cat) (Catd_cat $K) Cat_cat
      (@Pi_func $K) (cart_functor_include $K Cat_cat);''')
    replace('''      (@Pi_pullback_funcd $K $G)
  ↪ @Pi_func (@fapp0 $K (Op_cat Cat_cat) $G $x);''', '''      (@Pi_pullback_funcd $K $G)
  ↪ @comp_cat_fapp0
      (Functor_cart_cat (@fapp0 $K (Op_cat Cat_cat) $G $x) Cat_cat)
      (Catd_cat (@fapp0 $K (Op_cat Cat_cat) $G $x)) Cat_cat
      (@Pi_func (@fapp0 $K (Op_cat Cat_cat) $G $x))
      (cart_functor_include (@fapp0 $K (Op_cat Cat_cat) $G $x) Cat_cat);''')

    anchor = '// 8d. Fibre covariance and dependent-hom endpoint notation'
    replace(anchor, (audit / 'mapping_constructor_controls.lpfragment').read_text() + '\n' + anchor)
    output = root / 'tmp/probes/strict_default_mapping_constructor'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'emdash3_2.lp').write_text(source)
    (output / 'owner_prefix.lp').write_text(source[:source.index(anchor)])
    comparison = '''unif_rule
  @fapp1_func _ _ (@Pullback_catd_func $A $B $F)
    (@Const_catd $B Terminal_cat) (@Const_catd $B Cat_cat)
  ≡ @Pullback_catd_func $A $B $F
  ↪ [ tt ≡ tt ];'''
    assert source.count(comparison) == 1
    without_comparison = source.replace(comparison, '// Diagnostic: ambient whole comparison omitted.')
    (output / 'no_comparison.lp').write_text(without_comparison[:without_comparison.index(anchor)])
    end = '// Mixed-variance hom family for two sections of a displayed family.'
    (output / 'mixed_prefix.lp').write_text(source[:source.index(end)])
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    files = ('mapping_constructor_migration.py', 'mapping_constructor_controls.lpfragment')
    manifest = {
        'status': 'non-library whole Cartesian formation and ambient fixed-action repair',
        'precompositionInputSha256': prior['outputs']['emdash3_2.lp'],
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in files},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in ('emdash3_2.lp', 'owner_prefix.lp', 'no_comparison.lp',
                              'mixed_prefix.lp', 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    assert not re.search(r'(?m)^(?:constant )?symbol Functor_cat_func\b', source)
    print('Emitted native Hom(Cat) formation and restricted variable-base Pi views.')


if __name__ == '__main__':
    main()
