#!/usr/bin/env python3
"""Combine the raw coefficient prerequisites, retaining their qualifications."""
import hashlib
import json
import subprocess
from pathlib import Path


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    digest = lambda data: hashlib.sha256(data).hexdigest()
    record_path = audit / 'canonical_admission_verification.json'
    record = json.loads(record_path.read_text())
    source_path = root / 'tmp/probes/canonical_admission/seed_consumers.lp'
    source = source_path.read_text()
    assert digest(source.encode()) == record['outputs']['seed_consumers.lp']
    assert record['checks']['seed_consumers.lp']['outcome'] == 'passed-fresh'
    inputs = [Path(__file__), record_path, source_path]
    insertions = []

    def fragment(name):
        p = audit / name
        inputs.append(p)
        return p.read_text()

    for anchor, names in (
        ('// Opposite of product swap is swap between the opposite factors.',
         ['local_inverse_swap_object.lpfragment']),
        ('// Whole operations, followed by both separately projected application orders.',
         ['local_inverse_swap_guarded.lpfragment', 'local_inverse_swap_identity_guarded.lpfragment']),
        ('// Unchanged raw production owner: reindexed map whole-fibre component\n',
         ['lift_coyoneda_reindexed_eval_guarded.lpfragment'])):
        assert source.count(anchor) == 1
        body = '\n'.join(fragment(name) for name in names)
        source = source.replace(anchor, body + '\n' + anchor)
        insertions.append({'anchor': anchor.strip(), 'fragments': names, 'sha256': digest(body.encode())})
    for name in ('local_inverse_swap_controls.lpfragment',
                 'local_cart_prof_inverse_boundary.lpfragment'):
        source += '\n' + fragment(name)
    extra = fragment('local_inverse_controls.lpfragment')
    source += '\n' + extra[:extra.index('// One arbitrary reindex map')]
    source += '\n' + fragment('local_inverse_perturbed_controls.lpfragment')
    interaction = fragment('local_inverse_interaction_controls.lpfragment')
    source += '\n' + interaction[:interaction.index('// Endpoint equal to a stable precomposition')]
    for name in ('lift_coyoneda_general_controls.lpfragment',
                 'lift_coyoneda_counit_controls.lpfragment',
                 'lift_coyoneda_identity_middle_control.lpfragment'):
        source += '\n' + fragment(name)
    out = root / 'tmp/probes/coefficient_assembly'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'combined_controls.lp').write_text(source)
    lift_pins_path = audit / 'lift_coyoneda_inputs.json'
    lift_pins = json.loads(lift_pins_path.read_text())
    production = subprocess.check_output(['git', 'show', lift_pins['productionRevision'] + ':emdash2/emdash3_2.lp'], cwd=root)
    assert digest(production) == lift_pins['productionSha256']
    production_text = production.decode()
    start = '// Nested reindexing accumulates both endpoint functors.'
    end = '// Reindexing a constant profunctor remains constant.'
    assert production_text.count(start) == production_text.count(end) == 1
    nested = production_text[production_text.index(start):production_text.index(end, production_text.index(start))]
    owner = '// Unchanged raw production owner: Hom_prof_along'
    assert source.count(owner) == 1 and start not in source
    with_nested = source.replace(owner, nested + '\n' + owner)
    (out / 'with_nested_reindex.lp').write_text(with_nested)
    inputs.append(lift_pins_path)
    package = root / 'lambdapi.pkg'
    inputs.append(package)
    (out / 'lambdapi.pkg').write_bytes(package.read_bytes())
    manifest = {
        'status': 'non-library raw-preserving coefficient assembly; seed profile is an explicit structural proposal',
        'sourceInputs': {str(p.relative_to(root)): digest(p.read_bytes()) for p in inputs},
        'insertions': insertions,
        'outputs': {'combined_controls.lp': digest(source.encode()), 'with_nested_reindex.lp': digest(with_nested.encode()), 'lambdapi.pkg': digest(package.read_bytes())},
        'importedNestedReindex': {'revision': lift_pins['productionRevision'], 'sourceSha256': digest(production), 'blockSha256': digest(nested.encode()), 'status': 'byte-identical existing production owner; missing from canonical seed donor'},
        'limits': ['No Q category or lift coherence qualification.',
                   'No Cartesian lambda or general counit admission.',
                   'Nested reindexed identity inverse remains a separate failed interaction.',
                   'No production source changes.'],
    }
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print('Prepared raw-preserving coefficient assembly; no checker run.')


if __name__ == '__main__':
    main()
