#!/usr/bin/env python3
"""Emit the explicit canonical seed profile proposal; never run Lambdapi.

The only new profile contract concerns co-Yoneda(Unit). The existing raw
chain, native generator action and derived reindex consumer are retained.
Lambda/evaluation admission is not postulated by this builder.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess


def digest(data):
    return hashlib.sha256(data).hexdigest()


def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    pins_path = audit / 'canonical_admission_inputs.json'
    pins = json.loads(pins_path.read_text())
    inputs = {}
    for name, expected in pins['sourceInputs'].items():
        data = (subprocess.check_output(
            ['git', 'show', pins['productionRevision'] + ':emdash2/' + name], cwd=root)
            if name == 'emdash3_2.lp' else (root / name).read_bytes())
        assert digest(data) == expected, (name, 'source pin changed')
        inputs[name] = data
    prior = json.loads(inputs['audits/strict-default-action-boundary/admission_next_verification.json'])
    donor_name = 'tmp/probes/admission_next/staged_full_bridge.lp'
    donor = inputs[donor_name].decode()
    assert digest(donor.encode()) == prior['outputs']['staged_full_bridge.lp']
    assert prior['checks']['staged_full_bridge.lp']['outcome'] == 'passed-fresh'
    production = inputs['emdash3_2.lp'].decode()
    records = []

    def record(label, start, end):
        block = production[start:end]
        records.append({'label': label, 'source': 'emdash3_2.lp',
                        'startLine': production.count('\n', 0, start) + 1,
                        'endLine': production.count('\n', 0, end),
                        'sha256': digest(block.encode())})
        return block

    def symbol(name):
        matches = list(re.finditer(r'(?m)^(?:injective |constant )?symbol ' +
                                  re.escape(name) + r'\b[\s\S]*?;\n', production))
        assert len(matches) == 1, (name, len(matches))
        assert not re.search(r'(?m)^(?:injective |constant )?symbol ' + re.escape(name) + r'\b', donor)
        match = matches[0]
        return record(name, match.start(), match.end())

    declarations = '\n'.join(symbol(name) for name in (
        'Prof_cell_apply', 'Prof_func_hom', 'Prof_tensor_hom_hom'))
    beta_start = '// Fixed right-unit co-Yoneda beta on tensor-introduced shaped elements.'
    beta_end = '// Fixed right-unit co-Yoneda naturality fusion under shaped application.'
    assert production.count(beta_start) == production.count(beta_end) == 1
    i = production.index(beta_start)
    beta = record('existing covariant co-Yoneda shaped beta', i, production.index(beta_end, i))
    native = '// Unchanged native shaped/co-Yoneda owner closure.\n' + declarations + '\n' + beta
    names = ('canonical_admission_seed.lpfragment',
             'canonical_admission_operations.lpfragment',
             'canonical_admission_generator.lpfragment',
             'canonical_admission_controls.lpfragment',
             'canonical_admission_native_controls.lpfragment')
    fragments = {name: (audit / name).read_text() for name in names}
    seed = fragments[names[0]]
    assert len(re.findall(r'(?m)^unif_rule\b', seed)) == 1
    assert len(re.findall(r'(?m)^symbol\b', seed)) == 1
    assert not re.search(r'(?m)^rule\b', seed)
    assert not re.search(r'(?m)^(?:rule|unif_rule)\b',
                         '\n'.join(fragments[name] for name in names[1:]))
    view = seed[seed.index('unif_rule'):]
    anchor = '// Unchanged raw production owner: Prof_reindex_transf\n'
    assert donor.count(anchor) == 1
    native_owner = donor.replace(anchor, native + '\n' + anchor)
    seed_owner = donor.replace(anchor, native + '\n' + seed + '\n' + anchor)
    operations = fragments[names[1]]
    generator = fragments[names[2]]
    controls = fragments[names[3]]
    native_controls = fragments[names[4]]
    targets = {
        'native_owners.lp': native_owner,
        'native_controls.lp': native_owner + '\n' + native_controls,
        'seed_owner.lp': seed_owner + '\n' + native_controls,
        'seed_operations.lp': seed_owner + '\n' + native_controls + '\n' + operations,
        'seed_consumers.lp': seed_owner + '\n' + native_controls + '\n' + operations +
                             '\n' + generator + '\n' + controls,
    }
    selected = targets['seed_consumers.lp']
    assert selected.count(view) == selected.count(beta) == 1
    targets['without_seed_view.lp'] = selected.replace(view, '')
    targets['without_native_coyoneda_beta.lp'] = selected.replace(beta, '')
    authoring = [Path(__file__), pins_path, *(audit / name for name in names),
                 audit / 'canonical_admission_source_closure.md']
    manifest = {
        'status': 'authoring candidate only; proposed canonical structural profile is not a derived strictness theorem or checked qualification',
        'productionRevision': pins['productionRevision'],
        'sourceInputs': pins['sourceInputs'],
        'donorReceipt': prior['checks']['staged_full_bridge.lp']['id'],
        'fullSourceContinuation': False,
        'unchangedProductionBlocks': records,
        'newProfileContract': 'Only co-Yoneda(Unit_B) receives a proposed canonical Cartesian view; no arbitrary raw map or independent evidence argument.',
        'derivedConsumers': 'Actual inclusion, existing raw lambda/reindex/eval chain with proof-time agreement to its original raw body, classified seed reindex, native shaped-generator observation.',
        'remainingQualification': {
            'seedMathematics': 'The profile is a structural refinement of the named canonical operation, not derived from current opaque tensor/beta declarations.',
            'lambdaAdmission': 'Both whole strictness cells or a justified canonical preservation body for lambda(co-Yoneda(Unit)) remain absent.',
            'evaluationAdmission': 'General F changes the tensor middle to A; composition on generators, A-balancing and both whole exposed-endpoint actions remain required.',
            'rawProfiles': 'Public ProfMap/Prof_hom and all raw constructor signatures remain unchanged.',
            'noDesiredCounitPostulate': True,
        },
        'authoringInputs': {str(path.relative_to(root)): digest(path.read_bytes()) for path in authoring},
        'outputs': {name: digest(text.encode()) for name, text in targets.items()},
        'newControls': {name: {'positive': len(re.findall(r'(?m)^assert\b', text)),
                              'negative': len(re.findall(r'(?m)^assertnot\b', text))}
                        for name, text in fragments.items()},
    }
    return root, targets, inputs['lambdapi.pkg'], manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true')
    args = parser.parse_args()
    root, targets, package, manifest = build()
    if args.check_authoring:
        print(json.dumps({'status': 'pins and authoring guards pass; Lambdapi not run',
                          'sourceBlocks': len(manifest['unchangedProductionBlocks']),
                          'newControls': manifest['newControls']}, indent=2))
        return
    output = root / 'tmp/probes/canonical_admission'
    output.mkdir(parents=True, exist_ok=True)
    for name, source in targets.items():
        (output / name).write_text(source)
    (output / 'lambdapi.pkg').write_bytes(package)
    manifest['outputs']['lambdapi.pkg'] = digest(package)
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted proposed canonical seed profile and actual consumers; Lambdapi not run.')


if __name__ == '__main__':
    main()
