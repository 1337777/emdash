#!/usr/bin/env python3
"""Scope the Cat source-action comparison to identity Homd; no checker run."""
import argparse
import hashlib
import json
from pathlib import Path
import re


def sha(data):
    return hashlib.sha256(data).hexdigest()


def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    donor = root / 'tmp/probes/homd_section_adoption/combined_controls.lp'
    original = donor.read_text()
    assert sha(original.encode()) == '7d27980170780fc1db23acdb74b040c6be4a0035979db4380b5768a13b222b66'
    matches = re.findall(r'(?ms)^// Existing native Cat-valued source-action convention,.*?^// 6c\.', original)
    assert len(matches) == 1
    removed = matches[0][:-len('// 6c.')]
    assert removed.count('unif_rule') == 1
    replacement = '// Intrinsic-profile audit: unqualified Cat action comparison removed.\n\n'
    without = original.replace(removed, replacement, 1)
    marker = '// NON-LIBRARY native u-arrow projections of the existing identity Homd owner.'
    assert without.count(marker) == 1
    owner_path = audit / 'homd_root_action_scope.lpfragment'
    owner = owner_path.read_text()
    controls_path = audit / 'homd_root_action_scope_controls.lpfragment'
    controls = controls_path.read_text()
    assert len(re.findall(r'(?m)^unif_rule\b', owner)) == 1
    assert not re.search(r'(?m)^(?:rule|unif_rule|(?:injective |constant )?symbol)\b', controls)
    selected = without.replace(marker, owner + '\n' + marker, 1)
    assert re.findall(r'(?ms)^assert(?:not)?\b.*?;', selected) == re.findall(r'(?ms)^assert(?:not)?\b.*?;', original)
    combined = selected + '\n' + controls
    restored = combined.replace(replacement, removed, 1)
    targets = {
        'combined_controls.lp': combined,
        'without_scoped_comparison.lp': without + '\n' + controls,
        'with_generic_comparison.lp': restored,
    }
    continuation = root / 'tmp/probes/homd_section_adoption/full_source.lp'
    full_source = continuation.read_text()
    assert sha(full_source.encode()) == '6856ea4aa0616ec921e8877bec44889cd9aabec3777b879771f5b9644f33020a'
    tail_marker = '// 14. Section action over dependent homs'
    assert full_source.count(tail_marker) == 1
    targets['full_source.lp'] = combined + '\n' + full_source[full_source.index(tail_marker):]
    inputs = [Path(__file__).resolve(), donor, owner_path, controls_path,
              continuation, root / 'lambdapi.pkg']
    manifest = {
        'status': 'authoring replay only; see separate verification for checked outcomes',
        'hypothesis': 'Canonical Homd x consumers need only their named source-action comparison; raw FF need not inherit it.',
        'sourceInputs': {str(p.relative_to(root)): sha(p.read_bytes()) for p in inputs},
        'removedGenericComparison': removed,
        'outputs': {name: sha(body.encode()) for name, body in targets.items()},
        'inheritedAssertions': {'positive': 348, 'negative': 75},
        'newAssertions': {'positive': 0, 'negative': 2},
        'scope': [
            'Preserves every inherited assertion byte and order.',
            'Replaces one generic proof-time comparison by its named identity-Homd instance at the owning position.',
            'No rule equates the two naturality routes, strictifies arbitrary FF, or supplies a laxity cell.',
            'No claimed general-FF intrinsic extraction, global coefficient coherence, or production qualification.',
        ],
    }
    return root, targets, manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true')
    args = parser.parse_args()
    root, targets, manifest = build()
    if not args.check_authoring:
        out = root / 'tmp/probes/homd_root_action_scope'
        out.mkdir(parents=True, exist_ok=True)
        for name, source in targets.items():
            path = out / name
            assert not path.exists() or path.read_text() == source, 'preserve emitted source'
            path.write_text(source)
        (out / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
        (out / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'status': 'authoring checks passed; no checker run',
                      'targets': list(targets)}, indent=2))


if __name__ == '__main__':
    main()
