#!/usr/bin/env python3
"""Owner-position Q/Homd candidate; whole coherence remains to be qualified."""
import hashlib
import json
from pathlib import Path
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'edge_presheaf_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_edge_presheaf'
    prior = json.loads((audit / 'edge_presheaf_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']

    def replace(old, new):
        nonlocal source
        assert source.count(old) == 1, (old, source.count(old))
        source = source.replace(old, new)

    action_anchor = '''rule @fapp0 _ _ (@hom_int_precomp_tele_func $A $B $F $Y $X) $p
  ↪ @hom_int_precomp_func $A $B $F $Y $X $p;'''
    joins = (audit / 'q_homd_action_joins.lpfragment').read_text()
    replace(action_anchor, action_anchor + '\n\n' + joins)
    start = source.index('/*\n  Homd target architecture note:')
    end = source.index('// `homd_int` is a syntactic constructor package:', start)
    source = source[:start] + (audit / 'q_homd_interface.lpfragment').read_text() + '\n\n' + source[end:]
    # Preserve the existing root constructor and its FF argument. Its base is
    # inferred from the two corrected whole families.
    begin = source.index('symbol homd_src_func [Z : Cat]')
    end = source.index('// 14. Section action over dependent homs', begin)
    block = source[begin:end]
    block = block.replace('(Pi_cat (@Homd_target_section_catd Z D x))',
                          '(@Homd_section_cat Z D x)')
    block = block.replace('(Pi_cat (@Homd_target_section_catd $Z $D $x))',
                          '(@Homd_section_cat $Z $D $x)')
    block = block.replace('rule @tapp0_fapp0\n      $Z\n      Cat_cat',
                          'rule @tapp0_fapp0\n      _\n      Cat_cat')
    block = block.replace('(Functor_cat (Op_cat (Hom_cat Z x y)) Cat_cat)',
                          '(Functor_cart_cat (Op_cat (Hom_cat Z x y)) Cat_cat)')
    old = '''rule @tapp0_fapp0
      _
      Cat_cat
      _
      _
      $y
      (@homd_src_sec $Z $D $E $FF $x $u)
  ↪ @Obj_func
      (Fibre_cat (@Homd_target_section_catd $Z $D $x) $y)
      (@homd_tgt_func $Z $D $E $FF $x $u $y);'''
    new = '''rule @tapp0_fapp0 _ _ _ _ $y
      (@homd_src_sec $Z $D $E $FF $x $u)
  ↪ @homd_tgt_func $Z $D $E $FF $x $u $y;'''
    assert block.count(old) == 1
    block = block.replace(old, new)
    block = block.replace('E[x]^op ⊢ Π y :^n Z^op, ...',
                          'T(E[x]) ⊢ Transf(Z,Q,iota(D),iota(Rep(x)))')
    old_comment = '''// Third projection fold. In v3.2 `piapp0` is a definition through ordinary
// terminal-source component evaluation, so this rule lives one layer down at
// the `tapp0_fapp0` component. The inferred source/target family arguments are
// deliberately `_` for the same stable-head hygiene as the other homd folds.'''
    new_comment = '''// Third projection: the whole y-section is a Q-valued transformation.
// Its ordinary component is directly the v/f functor. There is no terminal
// component wrapper, auxiliary context, currying step or primitive Pi.'''
    assert block.count(old_comment) == 1
    block = block.replace(old_comment, new_comment)
    source = source[:begin] + block + source[end:]

    anchor = '// 14. Section action over dependent homs'
    controls = audit / 'q_homd_controls.lpfragment'
    replace(anchor, controls.read_text() + '\n\n' + anchor)
    output = root / 'tmp/probes/strict_default_q_homd'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'emdash3_2.lp').write_text(source)
    (output / 'interface_prefix.lp').write_text(source[:source.index('// `homd_int` is a syntactic constructor package:')])
    (output / 'ladder_prefix.lp').write_text(source[:source.index(anchor)])
    (output / 'no_action_joins.lp').write_text(source[:source.index(anchor)].replace(joins, ''))
    coefficient = (audit / 'q_homd_coefficient_boundary.lpfragment').read_text()
    unit, composition = coefficient.split('// COMPOSITION BOUNDARY\n')
    (output / 'coefficient_unit.lp').write_text(source[:source.index(anchor)] + '\n' + unit)
    (output / 'coefficient_composition.lp').write_text(source[:source.index(anchor)] + '\n' + composition)
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    files = ['q_homd_migration.py', 'q_homd_interface.lpfragment',
             'q_homd_controls.lpfragment', 'q_homd_action_joins.lpfragment',
             'q_homd_coefficient_boundary.lpfragment', 'ff_source_image_profile.py']
    manifest = {
        'status': 'non-library structural Q/Homd candidate; whole coefficient/lift coherence not established',
        'edgeInputSha256': prior['outputs']['emdash3_2.lp'],
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in files},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in ('emdash3_2.lp', 'interface_prefix.lp', 'ladder_prefix.lp',
                              'no_action_joins.lp', 'coefficient_unit.lp',
                              'coefficient_composition.lp', 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted whole Q/Homd target and direct ladder candidate.')


if __name__ == '__main__':
    main()
