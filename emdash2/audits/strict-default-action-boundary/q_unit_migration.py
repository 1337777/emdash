#!/usr/bin/env python3
"""NON-LIBRARY canonical represented unit through existing shaped tensor."""
import hashlib
import json
from pathlib import Path
import re
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'q_inverse_views_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_q_inverse_views'
    prior = json.loads((audit / 'q_inverse_views_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']
    square_owner = '/* API-04V RULE-OFF CONTROL: these three raw folds can recover'
    assert source.count(square_owner) == 1
    source = source.replace(square_owner, (audit / 'q_unit_strict_squares.lpfragment').read_text()
                            + '\n' + square_owner)
    whisker_owner = '// Component of tele-postcomposition in an arbitrary ambient category.'
    assert source.count(whisker_owner) == 1
    source = source.replace(whisker_owner, (audit / 'q_unit_ambient_whiskering.lpfragment').read_text()
                            + '\n' + whisker_owner)
    section_owner = '// Constant-family section evaluation follows ordinary functor application.'
    assert source.count(section_owner) == 1
    source = source.replace(section_owner, (audit / 'q_unit_ambient_views.lpfragment').read_text()
                            + '\n' + section_owner)
    moved = []

    def symbol(name):
        nonlocal source
        matches = list(re.finditer(r'(?m)^(?:injective |constant )?symbol ' + re.escape(name) + r'\b[\s\S]*?;\n', source))
        assert len(matches) == 1, name
        m = matches[0]
        source = source[:m.start()] + '// ' + name + ' moved before Q/Homd.\n' + source[m.end():]
        moved.append(name)
        return m[0]

    def take(start, end):
        nonlocal source
        assert source.count(start) == source.count(end) == 1
        i = source.index(start)
        j = source.index(end, i)
        block = source[i:j]
        source = source[:i] + '// Existing owner moved before Q/Homd.\n\n' + source[j:]
        return block

    core = take('// Nested reindexing accumulates both endpoint functors.',
                '// Reindexing a constant profunctor remains constant.')
    shape = symbol('Prof_transf_cat')
    old = '≔ @Functord_cat\n    (Product_cat (Op_cat A\') B\')'
    new = '≔ Hom_cat (Prof_cat A\' B\')'
    assert shape.count(old) == 1
    core += '\n// Shaped coefficient cells use the same vertical Hom as Prof_cat.\n' + shape.replace(old, new)
    core += '\n' + symbol('Prof_hom_cat') + '\n' + symbol('Prof_hom')
    identity = symbol('Prof_id_hom')
    old = '''≔ @id_funcd
    (Product_cat (Op_cat B) B)
    (@Unit_prof B);'''
    new = '''≔ @id (Functor_cart_cat (Product_cat (Op_cat B) B) Cat_cat) (@Unit_prof B);'''
    assert identity.count(old) == 1
    core += '\n' + identity.replace(old, new)
    core += '\n' + symbol('Prof_func_hom')
    action = take('// Identity functor induces the canonical shaped identity of Unit_prof(A).',
                  '// 18h. Tensor, shaped introduction, and fixed-endpoint co-Yoneda maps')
    needle = '(@Prof_func_hom $A $B $F)'
    assert action.count(needle) == 2
    action = action.replace(needle, '(@strict_transfor _ _ _ _ ' + needle + ')')
    core += '\n' + action + '\n' + symbol('Prof_tensor_hom_hom')
    core += '\n' + (audit / 'q_unit.lpfragment').read_text()
    anchor = '// NON-LIBRARY structural coefficient candidate.'
    assert source.count(anchor) == 1
    source = source.replace(anchor, core + '\n' + anchor)
    old = 'aliases: `Functord_cat` and `Prof_reindex` are the semantic owners, while the'
    new = 'aliases: `Hom_cat(Prof_cat)` and `Prof_reindex` are the semantic owners, while the'
    assert source.count(old) == 1
    source = source.replace(old, new)
    anchor = '// The y-section is the existing transformation category in the coefficient.'
    assert source.count(anchor) == 1
    source = source.replace(anchor, (audit / 'q_unit_hom_units.lpfragment').read_text() + '\n'
                            + (audit / 'q_unit_bridge.lpfragment').read_text() + '\n' + anchor)
    marker = '// 14. Section action over dependent homs'
    source = source.replace(marker, (audit / 'q_unit_controls.lpfragment').read_text() + '\n'
                            + (audit / 'q_unit_ambient_whiskering_controls.lpfragment').read_text() + '\n' + marker)
    prefix = source[:source.index(marker)]
    output = root / 'tmp/probes/strict_default_q_unit'
    output.mkdir(parents=True, exist_ok=True)
    targets = {'emdash3_2.lp': source, 'owner_prefix.lp': prefix,
               'action_boundary.lp': prefix + '\n' + (audit / 'cartesian_inverse_action_boundary.lpfragment').read_text()}
    mate = (audit / 'q_lift_mate.lpfragment').read_text()
    anchor = '// The y-section is the existing transformation category in the coefficient.'
    mate_source = source.replace(anchor, mate + '\n' + anchor)
    targets['mate_source.lp'] = mate_source
    targets['mate_boundary.lp'] = mate_source[:mate_source.index(marker)]
    partial = mate[:mate.index('// WHOLE MATE:')]
    partial_source = source.replace(anchor, partial + '\n' + anchor)
    targets['mate_steps.lp'] = partial_source[:partial_source.index(marker)]
    projections = (audit / 'q_lift_mate_projections.lpfragment').read_text()
    split = projections.index('// COUNit PROJECTION:')
    targets['mate_unit_projection.lp'] = targets['mate_steps.lp'] + '\n' + projections[:split]
    targets['mate_counit_projection.lp'] = targets['mate_steps.lp'] + '\n' + projections[split:]
    squares = (audit / 'q_unit_strict_squares.lpfragment').read_text()
    hom_units = (audit / 'q_unit_hom_units.lpfragment').read_text()
    targets['no_strict_squares.lp'] = prefix.replace(squares, '')
    targets['no_hom_units.lp'] = prefix.replace(hom_units, '')
    inferred_rhs = hom_units.replace('(Op_cat $T)', '$B')
    targets['inferred_identity_object.lp'] = prefix.replace(hom_units, inferred_rhs)
    views = (audit / 'q_unit_ambient_views.lpfragment').read_text()
    comparisons = views[:views.index('// Typed reflexivity')]
    targets['no_ambient_views.lp'] = prefix.replace(comparisons, '')
    object_start = comparisons.index('// Obj is not an injective category decoder')
    targets['no_ambient_obj_view.lp'] = prefix.replace(comparisons[object_start:], '')
    whisker = (audit / 'q_unit_ambient_whiskering.lpfragment').read_text()
    targets['no_ambient_whiskering.lp'] = prefix.replace(whisker, '')
    for name, data in targets.items():
        (output / name).write_text(data)
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    names = ('q_unit_migration.py', 'q_unit.lpfragment', 'q_unit_bridge.lpfragment', 'q_unit_controls.lpfragment',
             'q_lift_mate.lpfragment', 'q_unit_hom_units.lpfragment', 'q_unit_strict_squares.lpfragment',
             'q_unit_model.py', 'q_lift_mate_projections.lpfragment', 'q_unit_ambient_whiskering.lpfragment',
             'q_unit_ambient_whiskering_controls.lpfragment', 'q_unit_ambient_views.lpfragment')
    manifest = {
        'status': 'non-library canonical unit construction; whole lift/coherence unqualified',
        'qInverseViewsInputSha256': prior['outputs']['emdash3_2.lp'],
        'movedSymbols': moved,
        'profileChange': 'Prof_transf_cat uses Hom(Prof_cat), matching its Cartesian vertical-map profile; raw displayed FF is unchanged.',
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in names},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in (*targets, 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted existing shaped-cell canonical unit construction.')


if __name__ == '__main__':
    main()
