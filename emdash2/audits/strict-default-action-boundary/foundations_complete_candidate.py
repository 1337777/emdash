"""Assemble the complete migration candidate from the retained pinned recipes.

This is an authoring/replay command, not a proof checker or production promotion.
It refuses an existing destination and preserves the qualified parent package.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess

import displayed_action_projection_candidate as displayed
import foundation_reviewer_followup as annotations
import foundation_family_reviewer_followup as families
import foundation_reviewer_annotation_finish as final_annotations
import foundation_final_reviewer_candidate as final_reviewers


def library_driver():
    registry = json.loads((displayed.ROOT / 'checks.json').read_text())
    names = [name for name in registry['core'] if name != 'emdash3_2_checks.lp']
    parent = json.loads((displayed.ROOT / displayed.parent.INPUTS['parentVerification']).read_text())
    expected = {name for name in parent['currentQualifiedSourceSha256']
        if name.endswith('.lp') and '/' not in name}
    assert set(names) == expected, 'Original library registry drift'
    return ('/* Complete original owner import scope; central diagnostic and reviewer gates remain separate. */\n'
        + ''.join('require emdash.' + name[:-3] + ';\n' for name in names))


def emit(out):
    assert not out.exists(), out
    displayed.emit(out, 'telescope')
    annotations.apply(out)
    families.apply(out)
    final_annotations.apply(out)
    pin = final_reviewers.INPUTS['sourcePin']
    # These original files were deliberately outside the qualified parent.
    # Validate all baseline bytes before installing the final reviewer batch.
    originals = {}
    for name, spec in final_reviewers.INPUTS['files'].items():
        body = subprocess.check_output(['git', 'show', pin + ':emdash2/' + name],
            cwd=displayed.ROOT)
        assert hashlib.sha256(body).hexdigest() == spec['sourceSha256'], name
        originals[out / name] = body
    for path, body in originals.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)
    final_reviewers.apply(out)
    (out / 'all_original_library_owners.lp').write_text(library_driver())
    return {str(p.relative_to(out)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(out.rglob('*.lp'))}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    outputs = emit(args.out.resolve())
    (args.out / 'complete_candidate_manifest.json').write_text(json.dumps({
        'status': 'complete source candidate; validation and adoption pending',
        'outputs': outputs,
        'authoringSha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'out': str(args.out), 'lpFiles': len(outputs),
        'status': 'emitted; not qualified'}, indent=2))
