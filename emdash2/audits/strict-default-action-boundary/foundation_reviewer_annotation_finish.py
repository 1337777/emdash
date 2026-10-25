"""Replay source-pinned coefficient and duality annotations in complete reviewers.

This changes diagnostic interfaces, not semantic owners or assertion polarity.
The recursive Sigma normal-form negative uses the corrected total-dual Hom.
Qualification belongs to the emitted source receipts.
"""
from pathlib import Path
import argparse
import hashlib
import json

HERE = Path(__file__).resolve().parent
INPUTS = json.loads((HERE / 'foundation_reviewer_annotation_inputs.json').read_text())


def sha(data):
    return hashlib.sha256(data).hexdigest()


def apply(package):
    updates = {}
    for name, item in INPUTS['files'].items():
        path = package / 'examples' / (name + '.lp')
        old = path.read_bytes()
        assert sha(old) == item['sourceSha256'], name
        if 'occurrences' in item:
            assert old.count(b'Cat_cat') == item['occurrences'], name
            new = old.replace(b'Cat_cat', b'Cat_cart')
        else:
            before, after = item['before'].encode(), item['after'].encode()
            assert old.count(before) == 1, name
            new = old.replace(before, after, 1)
        assert sha(new) == item['candidateSha256'], name
        updates[path] = new
    # Validate the full small delta before changing an idle candidate.
    for path, data in updates.items():
        path.write_bytes(data)
    return {str(p.relative_to(package)): sha(data) for p, data in updates.items()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps({'status': 'unadopted reviewer annotations',
        'outputs': apply(args.package.resolve())}, indent=2))
