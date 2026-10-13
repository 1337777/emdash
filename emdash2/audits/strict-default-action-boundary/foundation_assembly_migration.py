#!/usr/bin/env python3
"""Compose the identity Homd owner with the checked lift additions; no checker.

The lift successor changes its donor prefix only by insertion. Reapply those
same insertion blocks to the identity-owner successor, so its removed generic
FF reduction rules are not reintroduced. No semantic LP body is duplicated.
"""
import argparse
import difflib
import hashlib
import json
from pathlib import Path


def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    digest = lambda data: hashlib.sha256(data).hexdigest()
    cart_record = audit / 'cart_action_verification.json'
    identity_record = audit / 'homd_identity_verification.json'
    lift_record = root / 'tmp/probes/lift_action/manifest.json'
    cart = json.loads(cart_record.read_text())
    identity = json.loads(identity_record.read_text())
    lift = json.loads(lift_record.read_text())
    inputs = [Path(__file__), cart_record, identity_record, lift_record]

    def pinned(relative, expected):
        path = root / relative
        data = path.read_bytes()
        assert digest(data) == expected, (relative, 'source pin changed')
        inputs.append(path)
        return data.decode()

    base = pinned('tmp/probes/strict_default_cart_action/q_prefix.lp',
                  cart['outputs']['q_prefix.lp'])
    upgraded = pinned('tmp/probes/lift_action/paired_unit_owner_prefix.lp',
                      lift['outputs']['paired_unit_owner_prefix.lp'])
    current = pinned('tmp/probes/homd_identity/selected_prefix.lp',
                     identity['outputs']['selected_prefix.lp'])
    full_identity = pinned('tmp/probes/homd_identity/full_source.lp',
                           identity['outputs']['full_source.lp'])
    old_lines = base.splitlines(keepends=True)
    new_lines = upgraded.splitlines(keepends=True)
    changes = difflib.SequenceMatcher(None, old_lines, new_lines, autojunk=False).get_opcodes()
    insertions = []
    for tag, i, j, k, l in changes:
        if tag == 'equal':
            continue
        assert tag == 'insert' and i == j, ('non-additive lift change', tag, i, j)
        block = ''.join(new_lines[k:l])
        if i == len(old_lines):
            current += block
            anchor = '<end-of-prefix>'
        else:
            for width in range(3, 65):
                anchor = ''.join(old_lines[i:i + width])
                if anchor and base.count(anchor) == 1 and current.count(anchor) == 1:
                    break
            else:
                raise AssertionError(('no preserved unique owner anchor', i))
            current = current.replace(anchor, block + anchor, 1)
        insertions.append({'donorLine': i + 1, 'lineCount': l - k,
                           'anchorSha256': digest(anchor.encode()),
                           'insertedSha256': digest(block.encode())})
    assert len(insertions) == 7, ('lift insertion boundary changed', len(insertions))
    assert 'injective symbol homd_id_int' in current
    assert 'injective symbol homd_int :' not in current
    marker = '// 14. Section action over dependent homs'
    assert full_identity.count(marker) == 1
    tail = full_identity[full_identity.index(marker):]
    controls = []
    for name in ('lift_action_controls.lpfragment', 'lift_action_represented_controls.lpfragment'):
        path = audit / name
        inputs.append(path)
        controls.append(path.read_text())
    outputs = {
        'combined_prefix.lp': current,
        'combined_controls.lp': current + '\n' + '\n'.join(controls),
        'full_source.lp': current + '\n' + tail,
    }
    package = root / 'lambdapi.pkg'
    inputs.append(package)
    assert digest(package.read_bytes()) == identity['outputs']['lambdapi.pkg']
    manifest = {
        'status': 'non-library coordinated owner assembly; no checker invoked by builder',
        'sourceInputs': {str(p.relative_to(root)): digest(p.read_bytes()) for p in inputs},
        'insertions': insertions,
        'outputs': {name: digest(source.encode()) for name, source in outputs.items()},
        'qualification': 'Combines identity-only Homd and structural lift action; Q profile, triangle coherence and generic intrinsic-action integration remain unqualified.',
    }
    manifest['outputs']['lambdapi.pkg'] = digest(package.read_bytes())
    return root, outputs, package.read_bytes(), manifest


def check_evidence(root, manifest):
    """Verify recorded bytes/settings/results; never invoke the checker."""
    digest = lambda data: hashlib.sha256(data).hexdigest()
    record = json.loads((Path(__file__).parent / 'foundation_assembly_verification.json').read_text())
    for group in ('sourceInputs', 'outputs', 'insertions'):
        assert manifest[group] == record[group], group + ' changed; review before repinning'
    entries = list(record['checks'].items()) + list(record['baselines'].items())
    for name, evidence in entries:
        receipt_path = root / evidence['receipt']
        assert digest(receipt_path.read_bytes()) == evidence['receiptSha256'], name
        receipt = json.loads(receipt_path.read_text())
        assert receipt['inputs'][receipt['target']] == evidence['sourceSha256'], name
        if name in manifest['outputs']:
            assert evidence['sourceSha256'] == manifest['outputs'][name], name
        for path, expected in receipt['inputs'].items():
            assert digest((root / path).read_bytes()) == expected, path
        assert digest((root / receipt['log']).read_bytes()) == receipt['logSha256'] == evidence['logSha256'], name
        assert receipt['settings'] == evidence['settings'], name
        assert receipt['checkerExit'] == evidence['checkerExit'], name
        assert receipt['outcome'] == evidence['outcome'], name
    print(f"Verified {len(entries)} source/receipt/log identities; no checker run.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true', help='check recipe without writing')
    parser.add_argument('--check-evidence', action='store_true', help='verify existing saved execution evidence')
    args = parser.parse_args()
    root, outputs, package, manifest = build()
    if args.check_evidence:
        check_evidence(root, manifest)
    if not args.check_authoring:
        output = root / 'tmp/probes/foundation_assembly'
        output.mkdir(parents=True, exist_ok=True)
        for name, source in outputs.items():
            (output / name).write_text(source)
        (output / 'lambdapi.pkg').write_bytes(package)
        (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Prepared coordinated identity/lift source from seven pinned owner insertions; Lambdapi not run.')


if __name__ == '__main__':
    main()
