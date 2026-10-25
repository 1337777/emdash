"""Migrate the final original reviewers to the already selected owner profiles.

No assertion is omitted. Two proof-time owner comparisons retain all supplied
data; no runtime rule or primitive is added. These are non-library candidates
until the complete reviewer and integration checks pass.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
from production_diagram_observation_migration import _atom, _point_readings

HERE = Path(__file__).resolve().parent
INPUTS = json.loads((HERE / 'foundation_final_reviewer_inputs.json').read_text())
REPLACEMENTS = (
    (r'\bFunctor_cat(?=\s+WalkingArrow_cat\s+C\b)', 'Functor_oplax_cat'),
    (r'\(Functor\s+WalkingArrow_cat\s+C\s*\)', '(Obj (Functor_oplax_cat WalkingArrow_cat C))'),
    (r'@Transf\s+WalkingArrow_cat\s+C\b', '@Hom (Functor_oplax_cat WalkingArrow_cat C)'),
    (r'\bOp_cat(?=\s+C\b)', 'TotalOp_cat'),
    (r'\bsym_fapp0_func\b', 'diagram_oplax_family_at_func'),
    (r'\bsym_transf_tapp0_transf\b', 'diagram_oplax_family_map_at'),
)


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def migrate(name, text):
    spec = INPUTS['files'][name]
    assert sha(text) == spec['sourceSha256'], name
    for (pattern, replacement), expected in zip(REPLACEMENTS, spec['counts']):
        text, count = re.subn(pattern, replacement, text)
        assert count == expected, (name, pattern, count)
    text = _point_readings(text, spec['pointReadings'])
    edits = []
    for match in re.finditer(r'@walking_arrow_func\b', text):
        cursor, args = match.end(), []
        for _ in range(4):
            value, cursor = _atom(text, cursor)
            args.append(value)
        assert args[0] == 'C', (name, args)
        edits.append((match.start(), cursor,
            '@OddDual_func WalkingArrow_cat C (' + text[match.start():cursor] + ')'))
    assert len(edits) == spec['walkingArrowViews'], name
    for start, end, body in reversed(edits):
        text = text[:start] + body + text[end:]
    if 'strictCompositionAssertion' in spec:
        assertions = list(re.finditer(r'(?m)^assert(?:not)?\b.*?;', text, re.S))
        assert len(assertions) == 9, name
        target = assertions[spec['strictCompositionAssertion'] - 1]
        assert target.group().startswith('assertnot')
        assert '@comp_fapp0 C' in target.group()
        text = text[:target.start()] + target.group().replace('assertnot', 'assert', 1) + text[target.end():]
        text = text.replace('// Normal identity, qualified composition and further Hom action on the native source.',
            '// Strict-default identity, composition and further Hom action on the native source.')
    if 'candidateSha256' in spec:
        assert sha(text) == spec['candidateSha256'], name
    return text


def apply(package):
    updates = {package / name: migrate(name, (package / name).read_text())
        for name in INPUTS['files']}
    for name, spec in INPUTS['owners'].items():
        path = package / name
        old = path.read_text()
        assert sha(old) == spec['sourceSha256'], name
        fragment = (HERE / spec['fragment']).read_text() + '\n'
        if 'anchor' in spec:
            assert old.count(spec['anchor']) == 1, name
            new = old.replace(spec['anchor'], fragment + spec['anchor'], 1)
        else:
            assert old.count(spec['before']) == 1, name
            new = old.replace(spec['before'], fragment, 1)
        assert sha(new) == spec['candidateSha256'], name
        updates[path] = new
    updates[package / 'tail_profile_inference_trace.lp'] = (
        HERE / 'foundation_final_reviewer_controls.lpfragment').read_text()
    updates[package / 'original_tail_reviewers.lp'] = (
        'require open emdash.examples.zero_arrow_family_action_paths;\n'
        'require open emdash.examples.zero_arrow_family_point_inputs;\n')
    updates[package / 'combined_tail_review.lp'] = (
        'require open emdash.tail_profile_inference_trace;\n'
        'require open emdash.original_tail_reviewers;\n')
    updates[package / 'original_final_reviewers.lp'] = ''.join(
        'require open emdash.' + name[:-3].replace('/', '.') + ';\n'
        for name in INPUTS['files'])
    # Validate the whole pinned input batch before mutating an idle candidate.
    for path, body in updates.items():
        path.write_text(body)
    return {str(p.relative_to(package)): sha(body) for p, body in updates.items()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps({'status': 'unadopted final reviewer candidate',
        'outputs': apply(args.package.resolve())}, indent=2))
