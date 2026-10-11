#!/usr/bin/env python3
"""Emit the next coupled whole-opposite migration over the Cartesian slice.

NON-LIBRARY. Keep the checked Cartesian authoring stage reproducible. The
new head prefix is a bounded check, not a replacement for the full source.
"""
import hashlib
import json
from pathlib import Path
import re
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'cartesian_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_profiles'
    prior = json.loads((audit / 'cartesian_migration_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']

    def replace(old, new):
        nonlocal source
        assert source.count(old) == 1, (old, source.count(old))
        source = source.replace(old, new)

    anchor = '// Path categories internalize HoTT equality as a groupoidal category.'
    replace(anchor, (audit / 'co_at2_category.lpfragment').read_text() + '\n' + anchor)
    anchor = '// Terminal category and points-as-functors are needed to derive unary homs from'
    replace(anchor, (audit / 'co_at2_functor.lpfragment').read_text() + '\n' + anchor)
    replace('constant symbol op : τ (Functor Cat_cat Cat_cat);',
            'constant symbol op : τ (Functor (CoAt2_cat Cat_cat) Cat_cat);')
    replace('rule @fapp0 Cat_cat Cat_cat op $A ↪ Op_cat $A;',
            'rule @fapp0 (CoAt2_cat Cat_cat) Cat_cat op $A ↪ Op_cat $A;')
    replace('rule @fapp1_fapp0 Cat_cat Cat_cat op $A $B $F ↪ @Op_func $A $B $F;',
            '''rule @fapp1_func (CoAt2_cat Cat_cat) Cat_cat op $A $B
  ↪ Op_func_func $A $B;
rule @fapp1_fapp0 (CoAt2_cat Cat_cat) Cat_cat op $A $B $F
  ↪ @Op_func $A $B $F;''')
    anchor = '// 3f. Internalized universe-level constructor packages'
    replace(anchor, (audit / 'duality_head_controls.lpfragment').read_text() + '\n' + anchor)

    # The existing family operator receives the shifted base and an explicitly
    # Cartesian parameter category. Objects remain ordinary default functors.
    replace('injective symbol Op_catd_func (Z : Cat) : τ (Functor (Catd_cat Z) (Catd_cat Z));',
            '''injective symbol Op_catd_func (Z : Cat)
  : τ (Functor (CoAt2_cat (Functor_cart_cat Z Cat_cat))
      (Catd_cat (CoAt2_cat Z)));''')
    replace('''rule @fapp1_fapp0 Cat_cat Cat_cat
      (Functor_cat_fapp0_func $Z) Cat_cat Cat_cat op
  ↪ @Op_catd_func $Z;''', '''// Whole formation pipeline for the corrected opposite-family operator.
rule @comp_fapp0 Cat_cat _ _ _
      (@comp_fapp0 Cat_cat _ _ _
        (@fapp1_fapp0 Cat_cat Cat_cat
          (Functor_cat_fapp0_func (CoAt2_cat $K)) (CoAt2_cat Cat_cat) Cat_cat op)
        (cart_functor_include (CoAt2_cat $K) (CoAt2_cat Cat_cat)))
      (CoAt2_func_func $K Cat_cat)
  ↪ Op_catd_func $K;''')
    replace('injective symbol Op_catd [K : Cat] (E : τ (Catd K)) : τ (Catd K);',
            'injective symbol Op_catd [K : Cat] (E : τ (Catd K)) : τ (Catd (CoAt2_cat K));')
    replace('''rule @comp_fapp0 Cat_cat $K Cat_cat Cat_cat op $E
  ↪ @Op_catd $K $E;''', '''rule @comp_fapp0 Cat_cat _ _ _ op (@CoAt2_func $K Cat_cat $E)
  ↪ @Op_catd $K $E;''')
    replace('''rule @Pullback_catd $K Cat_cat op $E
  ↪ @Op_catd $K $E;''', '''rule @Pullback_catd _ (CoAt2_cat Cat_cat) op (@CoAt2_func $K Cat_cat $E)
  ↪ @Op_catd $K $E;''')
    replace('''  ≡ @Pullback_catd $A $B $Eop $F
  ↪ [ $Eop ≡ (@Op_catd $B $E) ];''', '''  ≡ @Pullback_catd (CoAt2_cat $A) (CoAt2_cat $B) $Eop (@CoAt2_func $A $B $F)
  ↪ [ $Eop ≡ (@Op_catd $B $E) ];''')
    replace('''  ≡ @Pullback_catd $A $C $Eop
      (@comp_fapp0 Cat_cat $A $B $C $F $G)
  ↪ [ $Eop ≡ @Op_catd $C $E ];''', '''  ≡ @Pullback_catd (CoAt2_cat $A) (CoAt2_cat $C) $Eop
      (@CoAt2_func $A $C (@comp_fapp0 Cat_cat $A $B $C $F $G))
  ↪ [ $Eop ≡ @Op_catd $C $E ];''')
    replace('rule @fapp0 $K Cat_cat (@Op_catd $K $E) $k',
            'rule @fapp0 _ Cat_cat (@Op_catd $K $E) $k')
    m = re.search(r'(?m)^rule @fapp1_func\n      \$K Cat_cat \(@Op_catd \$K \$E\)[\s\S]*?;\n', source)
    assert m
    source = source[:m.start()] + '''rule @fapp1_func
      _ Cat_cat (@Op_catd $K $E) $x $y
  ↪ @comp_cat_fapp0
      (Op_cat (Hom_cat $K $x $y))
      (Op_cat (Functor_cart_cat (Fibre_cat $E $x) (Fibre_cat $E $y)))
      (Functor_cart_cat (Op_cat (Fibre_cat $E $x)) (Op_cat (Fibre_cat $E $y)))
      (Op_func_func (Fibre_cat $E $x) (Fibre_cat $E $y))
      (@Op_func
        (Hom_cat $K $x $y)
        (Functor_cart_cat (Fibre_cat $E $x) (Fibre_cat $E $y))
        (@fapp1_func $K Cat_cat $E $x $y));
''' + source[m.end():]
    replace('''rule @fapp1_fapp0
      $K Cat_cat (@Op_catd $K $E) $x $y $p''', '''rule @fapp1_fapp0
      _ Cat_cat (@Op_catd $K $E) $x $y $p''')
    replace('rule @Op_catd $K (@Op_catd $K $E) ↪ $E;',
            'rule @Op_catd _ (@Op_catd $K $E) ↪ $E;')
    replace('rule @Op_catd $K (@Const_catd $K $A) ↪ @Const_catd $K (Op_cat $A);',
            'rule @Op_catd $K (@Const_catd $K $A) ↪ @Const_catd (CoAt2_cat $K) (Op_cat $A);')
    family_end = '// Fixed-base layer: pointwise opposite of a displayed functor.'
    replace(family_end, (audit / 'duality_family_controls.lpfragment').read_text() + '\n' + family_end)
    output = root / 'tmp/probes/strict_default_duality'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'emdash3_2.lp').write_text(source)
    (output / 'head_prefix.lp').write_text(source[:source.index(anchor)])
    (output / 'family_prefix.lp').write_text(source[:source.index(family_end)])
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    files = ('duality_migration.py', 'co_at2_category.lpfragment',
             'co_at2_functor.lpfragment', 'duality_head_controls.lpfragment',
             'duality_family_controls.lpfragment')
    manifest = {
        'status': 'non-library; full migration is incomplete',
        'cartesianInputSha256': prior['outputs']['emdash3_2.lp'],
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in files},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in ('emdash3_2.lp', 'head_prefix.lp', 'family_prefix.lp', 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted corrected-transpose head and full-file continuation.')


if __name__ == '__main__':
    main()
