#!/usr/bin/env python3
"""NON-LIBRARY direct curried Prof owner migration; downstream work retained."""
import hashlib
import json
from pathlib import Path
import re
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'q_unit_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_q_unit/emdash3_2.lp'
    prior = json.loads((audit / 'q_unit_verification.json').read_text())
    assert hashlib.sha256(previous.read_bytes()).hexdigest() == prior['outputs']['emdash3_2.lp']
    source = previous.read_text()
    start = source.index('// Profunctor base: A^op × B.')
    op_start = source.index('// 18b. Opposite profunctors and fixed-endpoint duality', start)
    op_end = source.index('\nsymbol Prof_reindex [', op_start)
    tensor = source.index('\nsymbol Prof_tensor [', op_end)
    # Preserve ordinary product Hom as the upstream generic construction,
    # while Unit_prof now names the actual curried Prof unit.
    before = source[:start].replace('Unit_prof', 'Hom_prod_func')
    upstream = before
    action = (audit / 'curried_prof_precomp_action.lpfragment').read_text()
    anchor = '// Precomposing the identity at F[X] by h returns the functorial action F[h].'
    assert before.count(anchor) == 1
    comparison = (audit / 'curried_prof_whisker_comparison.lpfragment').read_text()
    before = before.replace(anchor, action + '\n' + comparison + '\n' + anchor)
    # Locate the exact old partial-evaluation rule; the new normalized view
    # must precede its strict-transfor/action consumers.
    anchor = 'rule @fapp0 _ _\n      (@hom_precomp_along_fapp0 _ _ (@id Cat_cat Cat_cat) _ _ _\n        (@Product_pair_tele_func (Op_cat $C) $C)'
    assert before.count(anchor) == 1
    before = before.replace(anchor, (audit / 'curried_prof_rep_projection.lpfragment').read_text() + '\n' + anchor)
    # Identity objects are determined by the typed pair endpoints. Keeping
    # duplicate literal objects here prevents the existing proof-time
    # stable-precomposition/raw-composition agreement from being usable.
    identity_pair = '(Struct_sigma\n        (@id (Functor_cart_cat $X $Y) $F)\n        (@id (Functor_cart_cat $Y $Z) $G))'
    assert before.count(identity_pair) == 1
    before = before.replace(identity_pair,
        '(Struct_sigma\n        (@id (Functor_cart_cat $X $Y) _)\n        (@id (Functor_cart_cat $Y $Z) _))')
    anchor = 'rule @tapp1_fapp0 $A $B $F $G $X $X $ϵ (@id $A $X)'
    assert before.count(anchor) == 1
    i = before.index(';', before.index(anchor)) + 1
    transpose_unit = (audit / 'curried_prof_transpose_identity.lpfragment').read_text()
    before = before[:i] + '\n' + transpose_unit + before[i:]
    owners = (audit / 'curried_prof.lpfragment').read_text()
    controls = (audit / 'curried_prof_controls.lpfragment').read_text()
    suffix = source[op_start:op_end] + source[tensor:]
    # The later declarations have moved, but their product-specific rules
    # remain in the full file as explicit next migration consumers.
    for name in ('Prof_reindex_func', 'Prof_reindex_transf'):
        pattern = r'(?m)^symbol ' + name + r'\b[\s\S]*?;\n'
        assert len(re.findall(pattern, suffix)) == 1, name
        suffix = re.sub(pattern, '// ' + name + ' migrated before opposite/tensor.\n', suffix)
    prefix = before + owners + '\n' + controls
    legacy = (root / 'tmp/probes/strict_default_q_unit/owner_prefix.lp').read_text().replace('Unit_prof', 'Hom_prod_func')
    assert legacy.startswith(upstream)
    legacy = before + legacy[len(upstream):]
    targets = {'owner_prefix.lp': prefix,
               'emdash3_2.lp': prefix + '\n' + suffix,
               'baseline_prefix.lp': source[:start],
               'legacy_interaction.lp': legacy,
               'map_boundary.lp': prefix + '\n' + (audit / 'curried_prof_map_boundary.lpfragment').read_text(),
               'no_precomp_action.lp': prefix.replace(action, ''),
               'no_whisker_comparison.lp': prefix.replace(comparison, ''),
               'no_rep_projection.lp': prefix.replace((audit / 'curried_prof_rep_projection.lpfragment').read_text(), '')}
    targets['no_transpose_identity.lp'] = targets['map_boundary.lp'].replace(transpose_unit, '')
    targets['no_transpose_guard.lp'] = targets['map_boundary.lp'].replace(
        'rule @tapp1_fapp0 (Op_cat $A) $B $F $G $x $x $eta (@id $A $x)',
        'rule @tapp1_fapp0 _ $B $F $G $x $x $eta (@id $A $x)')
    targets['whole_composition.lp'] = targets['map_boundary.lp'] + '\n' + (audit / 'curried_prof_composition_boundary.lpfragment').read_text()
    targets['no_identity_pair_minimization.lp'] = targets['map_boundary.lp'].replace(
        '(Struct_sigma\n        (@id (Functor_cart_cat $X $Y) _)\n        (@id (Functor_cart_cat $Y $Z) _))', identity_pair)
    output = root / 'tmp/probes/strict_default_curried_prof'
    output.mkdir(parents=True, exist_ok=True)
    for name, text in targets.items():
        (output / name).write_text(text)
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    inputs = ('curried_prof_migration.py', 'curried_prof.lpfragment', 'curried_prof_controls.lpfragment', 'curried_prof_precomp_action.lpfragment', 'curried_prof_rep_projection.lpfragment', 'curried_prof_whisker_comparison.lpfragment', 'curried_prof_map_boundary.lpfragment', 'curried_prof_transpose_identity.lpfragment', 'curried_prof_composition_boundary.lpfragment')
    manifest = {
        'status': 'non-library direct curried Prof; opposite/tensor and downstream integration pending',
        'inputSha256': prior['outputs']['emdash3_2.lp'],
        'authoringInputs': {str((audit / p).relative_to(root)): hashlib.sha256((audit / p).read_bytes()).hexdigest() for p in inputs},
        'outputs': {p: hashlib.sha256((output / p).read_bytes()).hexdigest() for p in (*targets, 'lambdapi.pkg')},
        'ordinaryHomRename': 'upstream Unit_prof -> Hom_prod_func; its existing action and consumers unchanged',
        'scope': 'new Prof(A,B) = old Prof(B,A) with curried argument order; no legacy Prof conversion in reindexing',
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted direct curried Prof owner copy and preserved downstream boundary.')


if __name__ == '__main__':
    main()
