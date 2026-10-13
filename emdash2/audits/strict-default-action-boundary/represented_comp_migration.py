#!/usr/bin/env python3
"""Construct one raw represented-composition comparison; no checker run."""
import hashlib
import json
from pathlib import Path
import re
import subprocess


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    digest = lambda data: hashlib.sha256(data).hexdigest()
    prior_path = audit / 'coefficient_assembly_verification.json'
    prior = json.loads(prior_path.read_text())
    source_path = root / 'tmp/probes/coefficient_assembly/with_nested_reindex.lp'
    source = source_path.read_text()
    assert digest(source.encode()) == prior['outputs']['with_nested_reindex.lp']
    assert prior['checks']['with_nested_reindex.lp']['outcome'] == 'passed-fresh'
    pins_path = audit / 'lift_coyoneda_inputs.json'
    pins = json.loads(pins_path.read_text())
    production = subprocess.check_output(['git', 'show', pins['productionRevision']+':emdash2/emdash3_2.lp'], cwd=root)
    assert digest(production) == pins['productionSha256']
    text = production.decode()
    start = '// Tensor reindexing acts only at its two exposed endpoints.'
    assert text.count(start) == 1 and start not in source
    i = text.index(start)
    tensor_reindex = text[i:text.index('\n/*', i)]
    matches = list(re.finditer(r'(?m)^symbol Prof_tensor_map\b[\s\S]*?;\n', text))
    assert len(matches) == 1 and 'symbol Prof_tensor_map' not in source
    tensor_map = matches[0].group(0)
    anchor = '// Unchanged raw production owner: Prof_imply_cov\n'
    assert source.count(anchor) == 1
    source = source.replace(anchor, tensor_reindex+'\n'+tensor_map+'\n'+anchor)
    body_path = audit / 'represented_comp_forward.lpfragment'
    controls_path = audit / 'represented_comp_controls.lpfragment'
    owner = source + '\n' + body_path.read_text()
    outputs = {'owner.lp': owner, 'controls.lp': owner+'\n'+controls_path.read_text()}
    view_path = audit / 'represented_comp_tensor_view.lpfragment'
    assert owner.count(tensor_reindex) == 1
    comparison = owner.replace(tensor_reindex, view_path.read_text())
    outputs['comparison_owner.lp'] = comparison
    outputs['comparison_controls.lp'] = comparison+'\n'+controls_path.read_text()
    general_path = audit / 'represented_comp_tensor_controls.lpfragment'
    outputs['general_controls.lp'] = outputs['comparison_controls.lp']+'\n'+general_path.read_text()
    outputs['without_tensor_view.lp'] = outputs['general_controls.lp'].replace(view_path.read_text(), '')
    integrated = outputs['general_controls.lp']
    integrated_paths = []
    for target_anchor, name in (
        ('/*\n  Propositional join for postcomposition outside stable precomposition:', 'inverse_nested_precomp_comparison.lpfragment'),
        ('// 6c. Constant/opposite transfors and Cat-valued composition projections', 'inverse_nested_horizontal_comparison.lpfragment'),
        ('// Unchanged raw production owner: Prof_coyoneda_cov_map\n', 'canonical_lambda_profile.lpfragment'),
        ('// Unchanged raw production owner: Prof_lambda_cov_map\n', 'canonical_eval_profile.lpfragment')):
        path = audit/name
        integrated_paths.append(path)
        assert integrated.count(target_anchor) == 1
        integrated = integrated.replace(target_anchor, path.read_text()+'\n'+target_anchor)
    for name in (
        'inverse_nested_controls.lpfragment',
        'canonical_lambda_mapping_controls.lpfragment', 'canonical_lambda_operations.lpfragment',
        'canonical_lambda_generator.lpfragment', 'canonical_lambda_consumers.lpfragment',
        'canonical_eval_mapping_controls.lpfragment', 'canonical_eval_operations.lpfragment',
        'canonical_eval_generator.lpfragment', 'canonical_eval_consumers.lpfragment',
        'canonical_eval_curried.lpfragment'):
        path = audit/name
        integrated_paths.append(path)
        integrated += '\n'+path.read_text()
    outputs['integrated_controls.lp'] = integrated
    out = root / 'tmp/probes/represented_comp'
    out.mkdir(parents=True, exist_ok=True)
    for name, value in outputs.items(): (out/name).write_text(value)
    package = root/'lambdapi.pkg'
    (out/'lambdapi.pkg').write_bytes(package.read_bytes())
    inputs = [Path(__file__), prior_path, source_path, pins_path, body_path, controls_path, view_path, general_path, package]
    inputs += integrated_paths
    manifest = {'status': 'non-library derived raw forward map and coupled fixed-parameter profile replay; the forward map has no inverse, Cartesian admission or Q composition law',
      'sourceInputs': {str(p.relative_to(root)):digest(p.read_bytes()) for p in inputs},
      'productionRevision': pins['productionRevision'], 'productionSha256': digest(production),
      'existingOwnerBlocks': {'tensorReindex': digest(tensor_reindex.encode()), 'tensorMap':digest(tensor_map.encode())},
      'outputs': {name:digest(value.encode()) for name,value in outputs.items()}}
    manifest['outputs']['lambdapi.pkg'] = digest(package.read_bytes())
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print('Prepared actual raw companion-composition map; no checker run.')


if __name__ == '__main__': main()
