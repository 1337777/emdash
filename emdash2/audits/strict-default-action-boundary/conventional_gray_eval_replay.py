#!/usr/bin/env python3
"""Emit the Gray-evaluator owner candidate on the public total-duality pin.

NON-LIBRARY. This replaces the planned Eval signature in a staged prefix.
It does not yet migrate the donor's separate joint Cartesian composition.
"""
import hashlib
import json
from pathlib import Path
import runpy


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    evidence = audit / 'conventional_total_op_verification.json'
    donor = json.loads(evidence.read_text())
    for name, expected in donor['authoringInputs'].items():
        assert sha(root / name) == expected, name
    runpy.run_path(str(audit / 'conventional_total_op_replay.py'), run_name='__main__')
    source = root / 'tmp/probes/conventional_total_op/candidate.lp'
    assert sha(source) == donor['outputs']['candidate.lp']
    body = source.read_text()
    assert 'symbol Eval_func ' not in body
    assert 'symbol GrayTensor_R ' not in body
    files = ('conventional_gray_tensor.lpfragment', 'conventional_gray_eval.lpfragment',
             'conventional_gray_eval_hom_joins.lpfragment',
             'conventional_gray_eval_controls.lpfragment',
             'conventional_gray_paths.lpfragment', 'conventional_gray_path_controls.lpfragment',
             'conventional_gray_eval_path_readings.lpfragment')
    parts = {name: (audit / name).read_text() for name in files}
    tensor_owner = '// 5c. Product and uncurried composition action'
    eval_owner = '// Native one-leg controls.'
    for marker in (tensor_owner, eval_owner):
        assert body.count(marker) == 1, marker
    body = body.replace(tensor_owner, parts[files[0]] + '\n' + parts[files[4]] + '\n' + tensor_owner)
    out = root / 'tmp/probes/conventional_gray_eval'
    out.mkdir(parents=True, exist_ok=True)
    evaluator = parts[files[1]]
    joins = parts[files[2]]
    readings = parts[files[6]]
    coord_start = '// Evaluation along one coordinate retains the original generic action.'
    coord_end = '// Existing fixed-object evaluation section, now through the Gray coordinate.'
    identity = '// IDENTITY-PROJECTION:'
    right_reading = '// The other path evaluates to epsilon[y] o F[p], the selected middle.'
    fixed_fold = 'rule @comp_fapp0 Cat_cat _ _ _ (@Eval_func $A $B)'
    for marker in (coord_start, coord_end):
        assert evaluator.count(marker) == 1
    assert evaluator.count(fixed_fold) == 2
    assert joins.count(identity) == 1
    assert readings.count(right_reading) == 1
    variants = {
        'candidate.lp': (evaluator, joins, readings),
        'no_coordinates.lp': (evaluator[:evaluator.index(coord_start)]
            + evaluator[evaluator.index(coord_end):], joins, readings),
        'no_fixed_folds.lp': (evaluator[:evaluator.index(fixed_fold)], joins, readings),
        'no_hom_joins.lp': (evaluator, joins[joins.index(identity):], readings),
        'no_identity_join.lp': (evaluator, joins[:joins.index(identity)], readings),
        'no_path_readings.lp': (evaluator, joins, ''),
        'only_left_reading.lp': (evaluator, joins, readings[:readings.index(right_reading)]),
        'only_right_reading.lp': (evaluator, joins, readings[readings.index(right_reading):]),
        'wrong_path.lp': (evaluator, joins,
            readings.replace('gray_tensor_right_then_left', 'gray_tensor_left_then_right')),
    }
    outputs = {}
    for name, (ev, hj, pr) in variants.items():
        candidate = body.replace(eval_owner, ev + '\n' + hj + '\n' + pr + '\n' + eval_owner)
        candidate += '\n' + parts[files[3]]
        candidate += '\n' + parts[files[5]]
        target = out / name
        target.write_text(candidate)
        outputs[name] = sha(target)
    (out / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    authors = [Path(__file__)] + [audit / n for n in files]
    (out / 'manifest.json').write_text(json.dumps({
        'status': 'unqualified Gray evaluation owner candidate',
        'donorEvidence': str(evidence.relative_to(root)), 'donorEvidenceSha256': sha(evidence),
        'donorSource': str(source.relative_to(root)), 'donorSourceSha256': sha(source),
        'authoringInputs': {str(p.relative_to(root)): sha(p) for p in authors},
        'outputs': outputs,
        'scope': ['Object pairs do not identify tensor Homs with Cartesian-product Homs.',
                  'Fixed evaluations keep the ordinary generic action owners.',
                  'No supplied interchanger or laxity witness is introduced.',
                  'The donor still has legacy joint Cartesian composition; no global repair claimed.']
    }, indent=2)+'\n')
    print('Emitted public-universe Gray evaluation owner candidate.')


if __name__ == '__main__':
    main()
