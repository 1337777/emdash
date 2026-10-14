#!/usr/bin/env python3
"""Emit public-universe total duality candidates on the conventional-lax pin.

NON-LIBRARY. Declares the structural whole total-duality map and checks its
projections. This is not a Cartesian-universe replacement or full Homd proof.
"""
import hashlib
import json
from pathlib import Path
import runpy
import subprocess


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    donor = json.loads((audit / 'conventional_lax_projection_verification.json').read_text())
    for name, expected in donor['authoringInputs'].items():
        assert sha(root / name) == expected, name
    runpy.run_path(str(audit / 'conventional_lax_projection_replay.py'), run_name='__main__')
    old = root / 'tmp/probes/conventional_lax_projection/ordinary.lp'
    assert sha(old) == donor['outputs']['ordinary.lp']
    body = old.read_text()
    category = (audit / 'co_above2_category.lpfragment').read_text()
    actions = (audit / 'co_above2_functor.lpfragment').read_text()
    boundary = '// Whole action on Cartesian mapping categories.'
    assert actions.count(boundary) == 1
    actions = actions[:actions.index(boundary)]
    assert 'Functor_cart_cat' not in actions
    files = ('conventional_total_op_mapping.lpfragment',
             'conventional_total_op_transfors.lpfragment',
             'conventional_total_op_offdiagonal.lpfragment',
             'conventional_total_op_involution_reading.lpfragment',
             'conventional_total_op_composition_reading.lpfragment',
             'conventional_total_op_source_units.lpfragment',
             'conventional_total_op_whole_action.lpfragment',
             'conventional_total_op_controls.lpfragment',
             'conventional_total_op_interaction_controls.lpfragment')
    parts = {name: (audit / name).read_text() for name in files}
    pin = json.loads((audit / 'conventional_lax_verification.json').read_text())['sourcePin']
    full = subprocess.check_output(['git', 'show', pin + ':emdash2/emdash3_2.lp'], cwd=root, text=True)
    start = full.index('rule @fapp1_func $A $A (@id Cat_cat $A) $x $y')
    end = full.index('// Stable pullback cut elimination and arrow projections.', start)
    whole = parts['conventional_total_op_whole_action.lpfragment']
    assert whole[whole.index('rule @fapp1_func'):].rstrip() == full[start:end].rstrip()
    units = parts['conventional_total_op_source_units.lpfragment']
    total_unit = '// lhs-audit: keep 1 -- the total source has lost both R and T identity tags.'
    assert units.count(total_unit) == 1
    category_owner = '// Path categories internalize HoTT equality as a groupoidal category.'
    functor_owner = '// Terminal category and points-as-functors are needed to derive unary homs from'
    transfor_owner = "// Point component of Path_cat_func's second action."
    identity_owner = '/*\n   Typed equality view of the generic strict identity cut.'
    composition_owner = '// Ordinary category identity cuts: g ∘ id ↪ g and id ∘ f ↪ f.'
    for marker in (category_owner, functor_owner, transfor_owner, identity_owner, composition_owner):
        assert body.count(marker) == 1
    body = body.replace(category_owner, category + '\n' + category_owner)
    body = body.replace(functor_owner, actions + '\n'
        + parts['conventional_total_op_mapping.lpfragment'] + '\n'
        + '// TOTAL-OP-COMPOSITION-READING\n' + functor_owner)
    body = body.replace(transfor_owner,
        parts['conventional_total_op_transfors.lpfragment'] + '\n'
        + '// TOTAL-OP-OFFDIAGONAL\n'
        + '// TOTAL-OP-INVOLUTION-READING\n' + transfor_owner)
    assert 'rule Hom_cat Cat_cat $X $Y ↪ Functor_cat $X $Y;' in body
    assert 'Functor_cart_cat' not in body
    correct = parts['conventional_total_op_offdiagonal.lpfragment']
    wrong = '''// Deliberately wrong copied-middle projection; negative control.
rule @tapp1_func _ _ _ _ $y $x (@TotalOp_transf $A $B $F $G $epsilon)
  ↪ @TotalOp_func (Hom_cat $A $x $y)
      (Hom_cat $B (@fapp0 $A $B $F $x) (@fapp0 $A $B $G $y))
      (@tapp1_func $A $B $F $G $x $y $epsilon);
rule @tapp1_fapp0 _ _ _ _ $y $x (@TotalOp_transf $A $B $F $G $epsilon) $p
  ↪ @tapp1_fapp0 $A $B $F $G $x $y $epsilon $p;
'''
    out = root / 'tmp/probes/conventional_total_op'
    out.mkdir(parents=True, exist_ok=True)
    outputs = {}
    for name, rules in (('candidate.lp', correct), ('no_offdiagonal.lp', ''),
                        ('wrong_middle.lp', wrong), ('no_source_units.lp', correct),
                        ('no_whole_action.lp', correct), ('no_involution_reading.lp', correct),
                        ('no_composition_reading.lp', correct), ('no_total_source_unit.lp', correct)):
        text = body.replace('// TOTAL-OP-OFFDIAGONAL\n', rules + '\n')
        reading = '' if name == 'no_involution_reading.lp' else parts[
            'conventional_total_op_involution_reading.lpfragment']
        text = text.replace('// TOTAL-OP-INVOLUTION-READING\n', reading + '\n')
        composition = '' if name == 'no_composition_reading.lp' else parts[
            'conventional_total_op_composition_reading.lpfragment']
        text = text.replace('// TOTAL-OP-COMPOSITION-READING\n', composition + '\n')
        if name != 'no_source_units.lp':
            selected_units = units[:units.index(total_unit)] if name == 'no_total_source_unit.lp' else units
            text = text.replace(identity_owner,
                selected_units + '\n' + identity_owner)
        if name != 'no_whole_action.lp':
            text = text.replace(composition_owner, whole + '\n' + composition_owner)
        text += '\n' + parts['conventional_total_op_controls.lpfragment']
        text += '\n' + parts['conventional_total_op_interaction_controls.lpfragment']
        (out / name).write_text(text)
        outputs[name] = sha(out / name)
    (out / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    authors = [Path(__file__), audit / 'co_above2_category.lpfragment',
               audit / 'co_above2_functor.lpfragment'] + [audit / n for n in files]
    (out / 'manifest.json').write_text(json.dumps({
        'status': 'unqualified structural total-duality candidates',
        'donor': str(old.relative_to(root)), 'donorSha256': sha(old),
        'wholeActionSourcePin': pin,
        'authoringInputs': {str(p.relative_to(root)): sha(p) for p in authors},
        'outputs': outputs,
        'scope': ['Public Hom(Cat)=Functor_cat retained.',
                  'No whole R or T mapping action on arbitrary transformations is assumed.',
                  'Family formation is a composite; no same-profile action on family maps is declared.',
                  'No full corrected Homd or coherent whole inverse theorem is claimed.']}, indent=2)+'\n')
    print('Emitted public-universe conventional-lax total-duality candidates.')


if __name__ == '__main__':
    main()
