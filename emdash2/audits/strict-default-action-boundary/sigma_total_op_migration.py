#!/usr/bin/env python3
"""Correct Sigma-Hom through total duality, without a second Sigma theory.

NON-LIBRARY. Preserve the public Sigma constructor and arrow/projection
owners; all later Homd-dependent consumers remain visible in the full file.
"""
import hashlib
import json
from pathlib import Path
import re
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'total_op_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_total_op'
    prior = json.loads((audit / 'total_op_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']

    def replace(old, new):
        nonlocal source
        assert source.count(old) == 1, (old, source.count(old))
        source = source.replace(old, new)

    replace('''//     ↪ Op_cat(Σ (p : Hom_K(x,y)^op), homd_(id_E,x,u,y,v)[p]).
rule Hom_cat (@Sigma_cat $K $E) (Struct_sigma $x $u) (Struct_sigma $y $v)
  ↪ Op_cat
      (@Sigma_cat
        (Op_cat (Hom_cat $K $x $y))
        (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v));''', '''//     ↪ O(Σ (p : O(Hom_K(x,y))), O_fib(homd_(id_E,x,u,y,v))[p]).
// The fibre duality is essential: total O then restores the fibre direction.
rule Hom_cat (@Sigma_cat $K $E) (Struct_sigma $x $u) (Struct_sigma $y $v)
  ↪ TotalOp_cat
      (@Sigma_cat
        (TotalOp_cat (Hom_cat $K $x $y))
        (@TotalOp_catd (Op_cat (Hom_cat $K $x $y))
          (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v)));''')

    # Keep the existing first-Hom head and refine only its recursive action,
    # as before. Its negative total now uses total functor duality as well.
    start = source.index('// Keep the first Hom owner; refine its recursive next action.')
    end = source.index('// Capped next projection joins the whole route on a visible Sigma cell.', start)
    block = source[start:end]
    old = '''      (@Op_func
      (@Sigma_cat (Op_cat (Hom_cat $K $x $y))
        (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v))
      (Op_cat (Hom_cat $K $x $y))
      (@Sigma_proj1_func (Op_cat (Hom_cat $K $x $y))
        (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v)))'''
    assert block.count(old) == 1
    new = '''      (@TotalOp_func
      (@Sigma_cat (TotalOp_cat (Hom_cat $K $x $y))
        (@TotalOp_catd (Op_cat (Hom_cat $K $x $y))
          (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v)))
      (TotalOp_cat (Hom_cat $K $x $y))
      (@Sigma_proj1_func (TotalOp_cat (Hom_cat $K $x $y))
        (@TotalOp_catd (Op_cat (Hom_cat $K $x $y))
          (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v))))'''
    source = source[:start] + block.replace(old, new) + source[end:]

    # The old explicit second pair family had the wrong fibre direction.
    # Theta's reduced Sigma-Hom type now supplies its actual pair indices.
    m = re.search(r'(?m)^symbol sigma_proj1_hom_fapp1_fapp0\b[\s\S]*?;\n', source)
    assert m
    declaration = m[0].split('≔', 1)[0]
    replace(m[0], declaration + '≔ sigma_Fst theta;\n')

    anchor = '// Stable head for the computationally important projection pullback.'
    replace(anchor, (audit / 'sigma_total_op_controls.lpfragment').read_text() + '\n' + anchor)
    output = root / 'tmp/probes/strict_default_sigma_total_op'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'emdash3_2.lp').write_text(source)
    (output / 'owner_prefix.lp').write_text(source[:source.index(anchor)])
    end = '// 11. Representables and presheaf-family classifiers'
    (output / 'hom_prefix.lp').write_text(source[:source.index(end)])
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    files = ('sigma_total_op_migration.py', 'sigma_total_op_controls.lpfragment')
    manifest = {
        'status': 'non-library corrected Sigma-Hom candidate; complete Homd integration remains open',
        'totalOpInputSha256': prior['outputs']['emdash3_2.lp'],
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in files},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in ('emdash3_2.lp', 'owner_prefix.lp', 'hom_prefix.lp', 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted corrected Sigma-Hom and its existing projection owners.')


if __name__ == '__main__':
    main()
