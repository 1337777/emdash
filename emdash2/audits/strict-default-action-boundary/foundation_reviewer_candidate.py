"""Unadopted foundational-reviewer candidate, replayed from pinned source.

This script does not modify production or qualify the generated package. It
keeps all original reviewer assertions and records the changed profiles. The
full displayed-evaluation Op cases and shared-core qualification remain open.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
from production_strict_wrapper_finish import calls, rename_code, ALIASES, RENAMES, code_mask, arg_end

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
INPUTS = json.loads((HERE / 'foundation_reviewer_candidate_inputs.json').read_text())

def once(text,name,arity,fn):
    positions=[m.start() for m in re.finditer(r'@'+name+r'\b',code_mask(text))]
    for s in reversed(positions):
        c=code_mask(text);end=s+len(name)+1;args=[]
        for _ in range(arity):
            a,b=arg_end(c,end);args.append(text[a:b]);end=b
        text=text[:s]+fn(args)+text[end:]
    return text


def contravariant(original):
    t=original
    t=t.replace('Cat_cat','Cat_cart')
    t,n=re.subn(r'@hom_int\s+\(Op_cat A\)\s+\(Op_cat A\)\s+\(@id_func \(Op_cat A\)\)',r'@hom_con_int_view A A (@id_func A)',t);assert n==10,n
    t,n=re.subn(r'@hom_int\s+\(Op_cat B\)\s+\(Op_cat A\)\s+\(@Op_func A B F\)',r'@hom_con_int_view B A F',t);assert n==10,n
    t=re.sub(r'\(@Op_func\s+\(Op_cat A\)\s+\(Op_cat B\)\s+\(@Op_func A B ([FG])\)\)',r'\1',t)
    for m in reversed(list(re.finditer(r'(?m)^assert(?:not)?\b.*?;',t,re.S))):
     b=m.group()
     if '@Op_transf' not in b:continue
     both='(epsilon other : τ (Transf F G))' in b
     if both:b=b.replace('(epsilon other : τ (Transf F G))','(U V : τ (@StrictTransfor A B F G))')
     else:
      assert b.count('(epsilon : τ (Transf F G))')==1
      b=b.replace('(epsilon : τ (Transf F G))','(U : τ (@StrictTransfor A B F G))')
     for old,new in [('epsilon','U')]+([('other','V')] if both else []):
      atom=f'(@Op_transf A B F G {old})';view=f'(@strict_transfor (Op_cat A) (Op_cat B) (@Op_func A B G) (@Op_func A B F) (@Op_transf A B F G {new}))';b=b.replace(atom,view);b=re.sub(r'\b'+old+r'\b',f'(@strict_transfor A B F G {new})',b)
     t=t[:m.start()]+b+t[m.end():]
    t=t.replace('// The direct opposite presentation compares proof-time in both orientations.', '// Direct ordinary-opposite comparison requires the classified strict transfor.\n// The native con owners above and below still admit arbitrary lax epsilon.')
    t=t.replace('Whole/component/identity computation, proof-time Op bridges, and retained\n   higher action; no opaque action-profile migration is imported.', 'Whole/component/identity computation, correctly profiled proof-time Op\n   bridges, and retained general lax native action.')
    return t

def evaluation(original):
    t=original
    t=once(t,'sym_transf_tapp0_transf',7,lambda a:f'''@fapp1_fapp0 (Functor_cat {a[0]} (Functor_cat {a[1]} {a[2]}))
        (Functor_cat {a[0]} {a[2]})
        (@diagram_family_evaluation_func {a[0]} {a[1]} {a[2]} {a[6]}) {a[3]} {a[4]} {a[5]}''')
    # Only the last three projection-order tests consume Cartesian exchange itself.
    s=t.index('// Compare evaluation before and after projecting its Hom owner.')
    t=t[:s]+t[s:].replace('Functor_cat I C','Functor_cart_cat I C')
    return t

def exchange(original):
    t=original
    t=original.replace('Functor_cat','Functor_cart_cat')
    t=re.sub(r'@Transf\s+A\s+\(Functor_cart_cat B C\)\s+H\s+K',r'@StrictTransfor A (Functor_cart_cat B C) H K',t)
    # These are Cartesian-classified transfors; their generic tapp views use the
    # existing ambient inclusion, without imposing strictness on ambient transfors.
    for name,arity in [('tapp0_fapp0',6),('tapp1_func',7)]:
     def wrap(a,name=name):
      if a[1]=='(Functor_cart_cat B C)':a[-1]=f'(@strict_transfor {a[0]} {a[1]} {a[2]} {a[3]} {a[-1]})'
      return '@'+name+' '+' '.join(a)
     t=once(t,name,arity,wrap)
    # The explicit ordinary-transpose observations are the strict-transfor profile.
    s=t.index('// Opposite action, direct');e=t.index('\n\nassertnot',s);b=t[s:e]
    b=b.replace('(eta : τ (@Transf A B F G))','(U : τ (@StrictTransfor A B F G))')
    b=b.replace('(@Op_transf A B F G eta)','(@strict_transfor (Op_cat A) (Op_cat B) (@Op_func A B G) (@Op_func A B F) (@Op_transf A B F G U))')
    b=re.sub(r'\beta\b',r'(@strict_transfor A B F G U)',b)
    b=b.replace('@probe_op_capped A B F G (@strict_transfor A B F G U)', '@probe_op_capped A B F G U')
    t=t[:s]+b+t[e:]
    t=t.replace('/* Double-exchange projection orders and the opposite mixed-action join. */','/* Cartesian double-exchange projection orders and the strict-transfor\n   ordinary-opposite join. General fixed evaluation is checked separately. */')
    return t

def migrate(name, original):
    assert hashlib.sha256(original.encode()).hexdigest() == INPUTS['files'][name]['sha256'], name
    if name == 'examples/contravariant_action_owners.lp':
        return contravariant(original)
    if name == 'examples/diagram_constant_evaluation.lp':
        return original.replace('Functor_cat', 'Functor_cart_cat')
    if name == 'examples/diagram_evaluation_usability.lp':
        text = evaluation(original)
        old = '@comp_cat_fapp0 A B C (@diagram_family_at_func B I C D i) F'
        assert text.count(old) == 2
        text = text.replace(old, '@hom_precomp_along_fapp0 Cat_cat Cat_cat (@id_func Cat_cat) C A B F\n        (@diagram_family_at_func B I C D i)')
        return text.replace('// Evaluation after precomposition retains the remaining whole functor.', '// Evaluation after precomposition retains the canonical whole precomposition\n// owner; the separate raw composition presentation is checked proof-time below.')
    if name == 'examples/diagram_exchange_computation.lp':
        return exchange(original)
    text = original
    if name in ('examples/displayed_evaluation.lp', 'examples/gray_right_closure.lp'):
        text, _ = calls(text, 'strict_functor', 3, 1, lambda args, explicit: args[-1])
        text = rename_code(text, {**ALIASES, **RENAMES})
    if name == 'examples/dependent_hom_laxity.lp':
        old = '    ≡ Op_cat\n        (@Sigma_cat\n          (Op_cat (Hom_cat Z x y))\n          (@homd_ Z E E (@id_funcd Z E) x u y v));'
        new = '    ≡ TotalOp_cat\n        (@Sigma_cat\n          (TotalOp_cat (Hom_cat Z x y))\n          (@TotalOp_catd (Op_cat (Hom_cat Z x y))\n            (@homd_ Z E E (@id_funcd Z E) x u y v)));'
        assert text.count(old) == 1
        text = text.replace(old, new)
        text = text.replace('// Composition preservation is the identity-transfor specialization of the\n// same post/left cell, yielding the normal-lax compositor surface.', '// Composition preservation is the identity-transfor specialization of the\n// same post/left cell; the public functor now has the strict default.')
    if name == 'examples/displayed_evaluation.lp':
        start = text.index('symbol eval_order_domain')
        end = text.index(';', start) + 1
        text = text[:start] + text[start:end].replace('Cat_cat', 'Cat_cart').replace('Product_cat_func', 'Product_cat_coeff_func') + text[end:]
        start = text.index('symbol eval_order_leading')
        end = text.index(';', start) + 1
        text = text[:start] + text[start:end].replace('(@Eval_funcd K I E)', '(@strict_transfor _ _ _ _ (@Eval_funcd K I E))') + text[end:]
    return text



def ordinary_displayed_slice(text):
    pending = []
    for number, match in reversed(list(enumerate(re.finditer(r'(?m)^assert(?:not)?\b.*?;', text, re.S), 1))):
        if '@Op_funcd' in match.group():
            pending.append(number)
            text = text[:match.start()] + '// Pending corrected shifted/profiled Op assertion ' + str(number) + '.' + text[match.end():]
    assert len(pending) == 12
    text = '/* DIAGNOSTIC SLICE ONLY: raw same-base Op obligations remain in the complete reviewer. */\n' + text
    text = text.replace('(@Eval_funcd K I E)', '(@strict_transfor _ _ _ _ (@Eval_funcd K I E))')
    text = text.replace('(@strict_transfor _ _ _ _ (@strict_transfor _ _ _ _ (@Eval_funcd K I E)))', '(@strict_transfor _ _ _ _ (@Eval_funcd K I E))')
    old = 'assertnot [A B : Cat] (F : τ (Functor A B)) [x y z : τ (Obj A)]\n  (f : τ (Hom A x y)) (g : τ (Hom A y z)) ⊢\n  @comp_fapp0 B _ _ _ (@fapp1_fapp0 A B F y z g) (@fapp1_fapp0 A B F x y f)\n  ≡ @fapp1_fapp0 A B F x z (@comp_fapp0 A x y z g f);'
    assert text.count(old) == 1
    text = text.replace(old, old.replace('assertnot ', 'assert ', 1))
    return text


def emit(out):
    source = ROOT / 'tmp/probes/production_owner_migration/package'
    parent_path = ROOT / INPUTS['parentVerification']
    assert hashlib.sha256(parent_path.read_bytes()).hexdigest() == INPUTS['parentVerificationSha256']
    parent = json.loads(parent_path.read_text())
    assert all(hashlib.sha256((source / n).read_bytes()).hexdigest() == h for n, h in parent['qualifiedInputSha256'].items()), 'Qualified source drift'
    assert not out.exists(), out
    shutil.copytree(source, out, ignore=shutil.ignore_patterns('*.lpo', '*.lpi', '*.lpj'))
    for name in INPUTS['order']:
        old = subprocess.check_output(['git', 'show', INPUTS['sourcePin'] + ':emdash2/' + name], cwd=ROOT, text=True)
        target = out / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(migrate(name, old))
    core = out / 'emdash3_2.lp'
    assert hashlib.sha256(core.read_bytes()).hexdigest() == INPUTS['coreSourceSha256']
    text = core.read_text()
    anchor = '// Cat_cat composition point/arrow actions of composed functors.'
    assert text.count(anchor) == 1
    core.write_text(text.replace(anchor, (HERE / 'foundation_reviewer_candidate_congruence.lpfragment').read_text() + '\n' + anchor, 1))
    (out / 'whole_contravariant_review.lp').write_text((HERE / 'foundation_reviewer_candidate_controls.lpfragment').read_text())
    driver = ''.join('require open emdash.' + name.removesuffix('.lp').replace('/', '.') + ';\n' for name in INPUTS['order'])
    (out / 'original_foundation_reviewers.lp').write_text(driver + 'require open emdash.whole_contravariant_review;\n')
    (out / 'ordinary_displayed_diagnostic.lp').write_text(ordinary_displayed_slice((out / 'examples/displayed_evaluation.lp').read_text()))
    (out / 'terminal_displayed_identity_compute.lp').write_text((HERE / 'foundation_reviewer_candidate_terminal_trace.lpfragment').read_text())
    hashes = {str(p.relative_to(out)): hashlib.sha256(p.read_bytes()).hexdigest() for p in out.rglob('*.lp')}
    (out.parent / (out.name + '_candidate_manifest.json')).write_text(json.dumps({'status': 'unadopted; emission is not qualification', 'sourcePin': INPUTS['sourcePin'], 'parentVerificationSha256': INPUTS['parentVerificationSha256'], 'outputs': hashes}, indent=2) + '\n')
    print(json.dumps({'out': str(out), 'reviewers': len(INPUTS['files']), 'status': 'unadopted'}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    emit(args.out.resolve())
