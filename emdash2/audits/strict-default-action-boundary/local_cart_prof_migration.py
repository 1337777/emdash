#!/usr/bin/env python3
"""Build a local Cartesian product-Prof replay; never invoke Lambdapi.

The checked cart_action prefix supplies ordinary Cartesian structure only.
The checked raw-counit closure supplies unchanged raw public Prof owners.
No global Cartesian Prof classifier, Q postulate or implication/conjoint
identification from the cart_action suffix is imported.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re


def digest(data):
    return hashlib.sha256(data).hexdigest()


def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    pins_path = audit / 'local_cart_prof_inputs.json'
    pins = json.loads(pins_path.read_text())
    for name, expected in pins['sourceInputs'].items():
        actual = digest((root / name).read_bytes())
        assert actual == expected, (name, 'source pin changed', expected, actual)
    cart_path = root / 'tmp/probes/strict_default_cart_action/emdash3_2.lp'
    cart = cart_path.read_text()
    cart_verified = json.loads((audit / 'cart_action_verification.json').read_text())
    assert digest(cart.encode()) == cart_verified['outputs']['emdash3_2.lp']
    marker = '// Profunctor base: A^op × B.'
    assert cart.count(marker) == 1
    prefix = cart[:cart.index(marker)]
    assert not re.search(r'(?m)^(?:injective |constant )?symbol Prof(?:_|\b)', prefix)

    spec = importlib.util.spec_from_file_location(
        'raw_represented_counit_local_dependency', audit / 'raw_represented_counit_migration.py')
    raw = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(raw)
    raw_root, raw_targets, package, raw_manifest = raw.build()
    assert raw_root == root
    raw_verified = json.loads((audit / 'raw_represented_counit_verification.json').read_text())
    for name in ('owner_prefix.lp', 'comparison_variant.lp'):
        assert digest(raw_targets[name].encode()) == raw_verified['outputs'][name]
    closure_marker = '// BOUNDED RAW PROF OWNER CLOSURE; not a full kernel.'
    assert raw_targets['owner_prefix.lp'].count(closure_marker) == 1
    closure = raw_targets['owner_prefix.lp'].split(closure_marker, 1)[1]
    assert '↪ @Functord_cat (Product_cat (Op_cat $A) $B) $P $Q;' in closure
    assert 'Functor_cart_cat' not in closure

    fragment_names = (
        'local_cart_prof.lpfragment', 'local_cart_prof_controls.lpfragment',
        'local_cart_prof_inverse_boundary.lpfragment', 'local_cart_prof_facade.lpfragment',
        'local_cart_prof_inclusion_controls.lpfragment', 'local_cart_prof_reindex_boundary.lpfragment',
        'local_cart_prof_precomp_projection.lpfragment', 'local_cart_prof_precomp_controls.lpfragment',
        'local_cart_prof_rep_projection.lpfragment', 'local_cart_prof_inclusion_typed_controls.lpfragment',
        'local_cart_prof_composition_facade.lpfragment', 'local_cart_prof_composition_controls.lpfragment')
    fragments = {name: (audit / name).read_text() for name in fragment_names}
    assert not re.search(r'(?m)^(?:rule|unif_rule)\b', '\n'.join(
        value for name, value in fragments.items()
        if name not in ('local_cart_prof_facade.lpfragment', 'local_cart_prof_precomp_projection.lpfragment',
                        'local_cart_prof_rep_projection.lpfragment', 'local_cart_prof_composition_facade.lpfragment')))
    facade = fragments['local_cart_prof_facade.lpfragment']
    assert len(re.findall(r'(?m)^unif_rule\b', facade)) == 1
    assert not re.search(r'(?m)^rule\b', facade)
    owner = prefix + '\n' + closure_marker + closure + '\n'
    local = fragments['local_cart_prof.lpfragment']
    candidate_marker = '/* NON-LIBRARY raw represented counit through the existing closed core.'
    comparison = raw_targets['comparison_variant.lp']
    assert comparison.count(closure_marker) == 1
    assert comparison.count(candidate_marker) == 1
    # Keep the separately checked head-preserving implication comparison
    # variant; it is explicitly not promoted here or rewritten by this builder.
    comparison = prefix + '\n' + closure_marker + comparison.split(closure_marker, 1)[1]
    candidate_start = comparison.index(candidate_marker)
    comparison_base = comparison[:candidate_start] + local + '\n' + comparison[candidate_start:]
    comparison = comparison[:candidate_start] + facade + '\n' + local + '\n' + comparison[candidate_start:]
    targets = {
        'owner_prefix.lp': owner,
        'local_view.lp': owner + local,
        'first_consumer.lp': comparison_base + '\n' + fragments['local_cart_prof_controls.lpfragment'],
        'inverse_boundary.lp': owner + local + '\n' + fragments['local_cart_prof_inverse_boundary.lpfragment'],
        'facade_view.lp': owner + facade + '\n' + local,
        'facade_first_consumer.lp': comparison + '\n' + fragments['local_cart_prof_controls.lpfragment'] + '\n' + fragments['local_cart_prof_inclusion_controls.lpfragment'],
        'facade_inverse_boundary.lp': owner + facade + '\n' + local + '\n' + fragments['local_cart_prof_inverse_boundary.lpfragment'],
        'facade_reindex_boundary.lp': owner + facade + '\n' + local + '\n' + fragments['local_cart_prof_reindex_boundary.lpfragment'],
        'no_facade_comparison.lp': owner + local,
    }
    projection = fragments['local_cart_prof_precomp_projection.lpfragment']
    assert len(re.findall(r'(?m)^rule\b', projection)) == 1
    assert not re.search(r'(?m)^unif_rule\b', projection)
    projection_anchor = '// Hom-action functoriality for precomposition.'
    assert prefix.count(projection_anchor) == 1
    point_prefix = prefix.replace(projection_anchor, projection + '\n' + projection_anchor)
    for old, new in (
            ('facade_view.lp', 'point_view.lp'),
            ('facade_first_consumer.lp', 'point_first_consumer.lp'),
            ('facade_inverse_boundary.lp', 'point_inverse_boundary.lp'),
            ('facade_reindex_boundary.lp', 'point_reindex_boundary.lp')):
        assert targets[old].startswith(prefix)
        targets[new] = point_prefix + targets[old][len(prefix):]
    targets['no_precomp_projection.lp'] = targets['facade_first_consumer.lp']
    targets['point_projection_controls.lp'] = targets['point_view.lp'] + '\n' + fragments['local_cart_prof_precomp_controls.lpfragment']
    representation_join = fragments['local_cart_prof_rep_projection.lpfragment']
    assert len(re.findall(r'(?m)^rule\b', representation_join)) == 1
    assert not re.search(r'(?m)^unif_rule\b', representation_join)
    representation_anchor = '// Canonical partial evaluation of the curried unit Hom.'
    assert point_prefix.count(representation_anchor) == 1
    joined_prefix = point_prefix.replace(representation_anchor,
                                         representation_join + '\n' + representation_anchor)
    for name in ('view', 'first_consumer', 'inverse_boundary', 'reindex_boundary', 'projection_controls'):
        old = targets['point_' + name + '.lp']
        assert old.startswith(point_prefix)
        targets['joined_' + name + '.lp'] = joined_prefix + old[len(point_prefix):]
    targets['no_representation_join.lp'] = targets['point_first_consumer.lp']
    runtime_inclusion = fragments['local_cart_prof_inclusion_controls.lpfragment']
    assert targets['joined_first_consumer.lp'].endswith(runtime_inclusion)
    targets['joined_profile_consumer.lp'] = targets['joined_first_consumer.lp'][:-len(runtime_inclusion)] + fragments['local_cart_prof_inclusion_typed_controls.lpfragment']
    targets['joined_inclusion_runtime_boundary.lp'] = targets['joined_view.lp'] + '\n' + runtime_inclusion
    composition_facade = fragments['local_cart_prof_composition_facade.lpfragment']
    assert len(re.findall(r'(?m)^unif_rule\b', composition_facade)) == 1
    assert not re.search(r'(?m)^rule\b', composition_facade)
    for name in ('profile_consumer', 'projection_controls', 'inverse_boundary', 'reindex_boundary'):
        old = targets['joined_' + name + '.lp']
        assert old.count(facade) == 1
        targets['composition_' + name + '.lp'] = old.replace(facade, facade + '\n' + composition_facade)
    targets['no_composition_facade.lp'] = targets['joined_profile_consumer.lp']
    targets['composition_profile_consumer.lp'] += '\n' + fragments['local_cart_prof_composition_controls.lpfragment']
    selected = targets['composition_profile_consumer.lp']
    for name, fragment in (
            ('without_raw_facade.lp', facade),
            ('without_precomp_projection.lp', projection),
            ('without_representation_projection.lp', representation_join),
            ('without_composition_congruence.lp', composition_facade)):
        assert selected.count(fragment) == 1
        targets[name] = selected.replace(fragment, '')
    authoring = [Path(__file__), pins_path, *(audit / n for n in fragment_names),
                 audit / 'local_cart_prof_source_closure.md']
    manifest = {
        'status': 'authoring replay only; no checker outcome recorded by this builder',
        'boundary': 'checked Cartesian prefix plus unchanged raw Prof owner closure and local view definitions',
        'fullSourceContinuation': False,
        'sourceInputs': pins['sourceInputs'],
        'cartesianPrefix': {'source': str(cart_path.relative_to(root)),
                            'excludedAnchor': marker, 'sha256': digest(prefix.encode())},
        'unchangedProductionBlocks': raw_manifest['unchangedProductionBlocks'],
        'rawCounitComparisonVariant': {
            'inheritedOutputSha256': raw_verified['outputs']['comparison_variant.lp'],
            'status': 'retained proof-time comparison experiment; no runtime equality/path input'},
        'qualification': {
            'rawPublicProfMap': 'unchanged Functord; no blanket strictification',
            'localView': 'definition by existing Cartesian mapping category',
            'facadeComparison': 'direct proof-time closure of existing raw Prof/Catd and Functor/Catd comparisons; Cart is never identified with raw Prof',
            'pointProjectionVariant': 'Cat-valued stable precomposition fapp0 projection, matching its existing postcomposition counterpart; whole reindex/action agreement remains separate',
            'representationJoinVariant': 'literal Unit_prof postcomposition with (Const_x,id) rejoins the existing whole hom_ partial-evaluation owner',
            'compositionFacadeVariant': 'sufficient proof-time congruence requires agreement of all endpoints and both actual raw arrows; no runtime composite fold or injectivity',
            'presentation': 'actual precomposition/swap/curry maps; inverse action is separately measured',
            'canonicalAdmission': 'not established; negative control preserves current boundary',
            'tensorClosedTheory': 'shared raw owners; no second local closed calculus',
            'QUniverse': 'not declared; local qhom is exactly the selected nested Hom type',
        },
        'authoringInputs': {str(path.relative_to(root)): digest(path.read_bytes()) for path in authoring},
        'outputs': {name: digest(value.encode()) for name, value in targets.items()},
        'newControls': {name: {
            'positive': len(re.findall(r'(?m)^assert\b', content)),
            'negative': len(re.findall(r'(?m)^assertnot\b', content))}
            for name, content in fragments.items()},
    }
    return root, targets, package, manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true')
    args = parser.parse_args()
    root, targets, package, manifest = build()
    if args.check_authoring:
        print(json.dumps({'status': 'source pins and authoring guards pass; Lambdapi not run',
                          'newControls': manifest['newControls']}, indent=2))
        return
    output = root / 'tmp/probes/local_cart_prof'
    output.mkdir(parents=True, exist_ok=True)
    for name, source in targets.items():
        (output / name).write_text(source)
    (output / 'lambdapi.pkg').write_bytes(package)
    manifest['outputs']['lambdapi.pkg'] = digest(package)
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted local Cartesian product-Prof replay; Lambdapi not run.')


if __name__ == '__main__':
    main()
