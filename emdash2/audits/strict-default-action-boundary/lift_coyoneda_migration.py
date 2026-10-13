#!/usr/bin/env python3
"""Emit a raw counit/generator owner experiment without invoking Lambdapi.

The checked raw-counit comparison variant supplies the exact canonical body.
Missing shaped-application/tensor-introduction/co-Yoneda-beta owners are
copied unchanged from its pinned production Git object. A separately marked
candidate tests the reindexed lambda/evaluation cut on actual generators.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess


FRAGMENTS = (
    'lift_coyoneda_reindexed_eval.lpfragment',
    'lift_coyoneda_reindexed_eval_guarded.lpfragment',
    'lift_coyoneda_existing_controls.lpfragment',
    'lift_coyoneda_general_controls.lpfragment',
    'lift_coyoneda_counit_controls.lpfragment',
    'lift_coyoneda_identity_middle_control.lpfragment',
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def insert_before(source, anchor, block):
    assert source.count(anchor) == 1, ('non-unique owner anchor', anchor)
    return source.replace(anchor, block + '\n' + anchor)


def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    pins_path = audit / 'lift_coyoneda_inputs.json'
    pins = json.loads(pins_path.read_text())
    for name, expected in pins['sourceInputs'].items():
        assert digest((root / name).read_bytes()) == expected, (name, 'source pin changed')
    prior_path = audit / 'raw_represented_counit_verification.json'
    prior = json.loads(prior_path.read_text())
    source_path = root / pins['donor']
    source = source_path.read_text()
    assert digest(source.encode()) == prior['outputs']['comparison_variant.lp']
    production_bytes = subprocess.check_output(
        ['git', 'show', pins['productionRevision'] + ':emdash2/emdash3_2.lp'], cwd=root)
    assert digest(production_bytes) == pins['productionSha256'], 'production Git-object pin changed'
    production = production_bytes.decode()
    blocks = []

    def block(label, start, end):
        text = production[start:end]
        blocks.append({'label': label, 'source': 'emdash3_2.lp',
                       'revision': pins['productionRevision'],
                       'startLine': production.count('\n', 0, start) + 1,
                       'endLine': production.count('\n', 0, end),
                       'sha256': digest(text.encode())})
        return text

    def symbol(name):
        pattern = r'(?m)^(?:(?:injective|constant) )?symbol ' + re.escape(name) + r'\b[\s\S]*?;\n'
        matches = list(re.finditer(pattern, production))
        assert len(matches) == 1, (name, len(matches))
        assert not re.search(r'(?m)^(?:(?:injective|constant) )?symbol ' + re.escape(name) + r'\b', source)
        return block(name, matches[0].start(), matches[0].end())

    def between(label, start, end):
        assert production.count(start) == production.count(end) == 1
        i = production.index(start)
        return block(label, i, production.index(end, i))

    nested = between('nested endpoint reindexing',
        '// Nested reindexing accumulates both endpoint functors.',
        '// Reindexing a constant profunctor remains constant.')
    declarations = '\n'.join(symbol(name) for name in
        ('Prof_cell_apply', 'Prof_tensor_hom_hom', 'Prof_func_hom'))
    beta = between('fixed right-unit co-Yoneda generator beta',
        '// Fixed right-unit co-Yoneda beta on tensor-introduced shaped elements.',
        '// Fixed right-unit co-Yoneda naturality fusion under shaped application.')
    owner = insert_before(source,
        '// Unchanged raw production owner: Hom_prof_along', nested)
    owner = insert_before(owner,
        '// Unchanged raw production owner: implication endpoint reindexing',
        '// Additional unchanged raw production owners for shaped generator consumption.\n'
        + declarations + '\n' + beta)
    assert '↪ @Functord_cat (Product_cat (Op_cat $A) $B) $P $Q;' in owner
    assert not re.search(r'(?m)^rule @Prof_imply_cov\b', owner)
    assert 'Prof_cov_universe' not in owner
    f = {name: (audit / name).read_text() for name in FRAGMENTS}
    candidate = f['lift_coyoneda_reindexed_eval.lpfragment']
    assert len(re.findall(r'(?m)^rule\b', candidate)) == 1
    assert not re.search(r'(?m)^(?:unif_rule|(?:injective |constant )?symbol)\b', candidate)
    for name, text in f.items():
        if name not in ('lift_coyoneda_reindexed_eval.lpfragment',
                        'lift_coyoneda_reindexed_eval_guarded.lpfragment'):
            assert not re.search(r'(?m)^(?:rule|unif_rule|(?:injective |constant )?symbol)\b', text), name
    candidate_owner = insert_before(owner,
        '// Unchanged raw production owner: reindexed map whole-fibre component', candidate)
    targets = {
        'owner_prefix.lp': owner,
        'existing_beta.lp': owner + '\n' + f['lift_coyoneda_existing_controls.lpfragment'],
        'general_boundary.lp': owner + '\n' + f['lift_coyoneda_general_controls.lpfragment'],
        'counit_boundary.lp': owner + '\n' + f['lift_coyoneda_counit_controls.lpfragment'],
        'candidate_owner.lp': candidate_owner,
        'candidate_generic.lp': candidate_owner + '\n' + f['lift_coyoneda_general_controls.lpfragment'],
        'candidate_counit_generator.lp': candidate_owner + '\n' + f['lift_coyoneda_counit_controls.lpfragment'],
    }
    assert targets['candidate_counit_generator.lp'].count(beta) == 1
    targets['no_coyoneda_beta.lp'] = targets['candidate_counit_generator.lp'].replace(beta, '')
    guarded = f['lift_coyoneda_reindexed_eval_guarded.lpfragment']
    assert len(re.findall(r'(?m)^rule\b', guarded)) == 1
    assert not re.search(r'(?m)^(?:unif_rule|(?:injective |constant )?symbol)\b', guarded)
    guarded_owner = insert_before(owner,
        '// Unchanged raw production owner: reindexed map whole-fibre component', guarded)
    targets['guarded_owner.lp'] = guarded_owner
    targets['guarded_generic.lp'] = guarded_owner + '\n' + f['lift_coyoneda_general_controls.lpfragment']
    targets['guarded_counit_generator.lp'] = guarded_owner + '\n' + f['lift_coyoneda_counit_controls.lpfragment']
    assert targets['guarded_counit_generator.lp'].count(beta) == 1
    targets['guarded_no_coyoneda_beta.lp'] = targets['guarded_counit_generator.lp'].replace(beta, '')
    targets['guarded_identity_middle.lp'] = guarded_owner + '\n' + f['lift_coyoneda_identity_middle_control.lpfragment']
    package = (root / 'lambdapi.pkg').read_bytes()
    inputs = [Path(__file__).resolve(), pins_path, prior_path, source_path, root / 'lambdapi.pkg']
    inputs += [audit / name for name in FRAGMENTS]
    manifest = {
        'status': 'unchecked non-library raw evaluation/generator experiment; no triangle qualification',
        'sourceInputs': {str(p.relative_to(root)): digest(p.read_bytes()) for p in inputs},
        'productionRevision': pins['productionRevision'],
        'productionSha256': pins['productionSha256'],
        'unchangedProductionBlocks': blocks,
        'outputs': {name: digest(text.encode()) for name, text in targets.items()},
        'outputControlCounts': {name: {
            'positive': len(re.findall(r'(?m)^assert\b', text)),
            'negative': len(re.findall(r'(?m)^assertnot\b', text)),
        } for name, text in targets.items()},
        'qualification': [
            'Raw public ProfMap and shaped-cell profiles remain unchanged; no map is retyped as Cartesian.',
            'Actual raw_represented_counit body is inherited unchanged: eval(reindex(lambda(co-Yoneda),id,F)).',
            'No implication-to-Conjoint identification is present.',
            'Existing beta controls use only unchanged production owners and map-level eval/lambda beta.',
            'The new candidate is a reindexed lambda/evaluation cut at Prof_cell_apply on a tensor introduction; it is not derivable from opaque map beta/eta alone.',
            'Unextended general/counit boundaries and the co-Yoneda-beta removal are positive obligations; failures are not passing negatives.',
            'Generator success would not establish balancing beyond this cut, whole map extensionality, Cartesian admission, a mate triangle or companion composition.',
        ],
        'checkerInvoked': False,
    }
    manifest['outputs']['lambdapi.pkg'] = digest(package)
    return root, targets, package, manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true', help='validate source pins and recipe without writing')
    args = parser.parse_args()
    root, targets, package, manifest = build()
    record = json.loads((Path(__file__).resolve().parent / 'lift_coyoneda_verification.json').read_text())
    for group in ('sourceInputs', 'outputs'):
        assert record[group] == manifest[group], (group, 'changed; review before refreshing evidence')
    if not args.check_authoring:
        output = root / 'tmp/probes/lift_coyoneda'
        output.mkdir(parents=True, exist_ok=True)
        for name, text in targets.items():
            (output / name).write_text(text)
        (output / 'lambdapi.pkg').write_bytes(package)
        (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'{len(targets)} raw co-Yoneda/evaluation targets prepared; Lambdapi not run.')


if __name__ == '__main__':
    main()
