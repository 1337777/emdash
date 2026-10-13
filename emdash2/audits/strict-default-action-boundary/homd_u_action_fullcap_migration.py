#!/usr/bin/env python3
"""Use the measured valid full-then-cap source action; no new semantic rule."""
import hashlib
import json
from pathlib import Path
import re

audit = Path(__file__).resolve().parent
root = audit.parents[1]
output = root / 'tmp/probes/homd_u_action'
digest = lambda data: hashlib.sha256(data).hexdigest()
prior_path = output / 'literal_manifest.json'
prior = json.loads(prior_path.read_text())
historical_path = output / 'manifest.json'
historical = json.loads(historical_path.read_text())
owner = output / 'owner.lp'
assert digest(owner.read_bytes()) == historical['outputs']['owner.lp']
receipt_path = root / 'logs/check-runs/20261013T173855Z-64c1bd83204a49288ddfe13e5b3187ba.json'
receipt = json.loads(receipt_path.read_text())
assert receipt['outcome'] == 'failed'
assert receipt['target'] == 'tmp/probes/homd_u_action/compute_source.lp'
assert receipt['inputs'][receipt['target']] == digest((root / receipt['target']).read_bytes())
pattern = (r'@fapp1_fapp0 \(Op_cat \(Fibre_cat E x\)\) '
           r'\(@Homd_section_cat K E x\)\s+'
           r'\(@homd_id_src_func K E x\) u1 u0 h')
replacement = ('fapp0 (@fapp1_func (Op_cat (Fibre_cat E x)) (@Homd_section_cat K E x) '
               '(@homd_id_src_func K E x) u1 u0) h')
targets = {}
counts = {}
for name, expected in prior['outputs'].items():
    path = output / name
    assert digest(path.read_bytes()) == expected, ('historical literal target changed', name)
    source = path.read_text()
    # All matching terms are appended consumers, not owner clauses.
    changed, count = re.subn(pattern, replacement, source)
    assert count >= 1, name
    new_name = 'fullcap_' + name.removeprefix('literal_')
    # Keep the first source normalization observation substantive after the
    # two source paths have deliberately become the same valid full/cap route.
    same = replacement + ')\n  ≡ fapp0 (@fapp1_func _ _ (@homd_id_src_func K E x) u1 u0) h;'
    if same in changed:
        changed = changed.replace(same, replacement + ')\n  ≡ @homd_id_u_map K E x u0 u1 h;', 1)
    targets[new_name] = changed
    counts[new_name] = count

diagnostic = '''// The direct capped declaration has its ordinary signature.
// This diagnostic spells h's classifier in the exact opposite source form.
flag "print_implicits" on;
compute λ (K : Cat) (E : τ (Catd K)) (x : τ (Obj K))
  (u0 u1 : τ (Obj (Fibre_cat E x)))
  (h : τ (Hom (Op_cat (Fibre_cat E x)) u1 u0)),
  @fapp1_fapp0 (Op_cat (Fibre_cat E x)) (@Homd_section_cat K E x)
    (@homd_id_src_func K E x) u1 u0 h;
'''
targets['op_typed_cap_diagnostic.lp'] = owner.read_text() + '\n' + diagnostic
generic = '''// Independent generic opposite-source capped action, with no Homd head.
// This measures whether the same elaboration issue already exists generically.
flag "print_implicits" on;
compute λ (A B : Cat) (F : τ (Functor (Op_cat A) B))
  (u0 u1 : τ (Obj A)) (h : τ (Hom A u0 u1)),
  @fapp1_fapp0 (Op_cat A) B F u1 u0 h;
'''
targets['generic_op_cap_diagnostic.lp'] = owner.read_text() + '\n' + generic
for name, source in targets.items():
    target = output / name
    if target.exists():
        assert target.read_text() == source, (name, 'preserve prior successor')
    target.write_text(source)
manifest = {
    'status': 'unchecked full-then-cap consumer successor; no checker run',
    'sourceInputs': {str(p.relative_to(root)): digest(p.read_bytes())
                     for p in (Path(__file__), prior_path, historical_path, owner, receipt_path)},
    'historicalLiteralOutputs': prior['outputs'],
    'outputs': {name: digest(source.encode()) for name, source in targets.items()},
    'replacementCounts': counts,
    'change': 'Only direct source-action applications in consumer terms become fapp0(fapp1_func(...)); no rule, endpoint or full-action contract changes.',
    'qualification': 'Successful normalization of full and cap-after-full in the failed diagnostic is partial trace evidence. New targets still require fresh checks. Direct capped elaboration remains separately failed until diagnosed.',
    'signatureReview': 'fapp1_fapp0 has the ordinary A,B,F,[X,Y],h:Hom(A,X,Y) signature with output Hom(B,F[X],F[Y]); there is no special opposite-source signature.',
}
(output / 'fullcap_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'status': 'emitted; Lambdapi not run', 'targets': list(targets)}, indent=2))
