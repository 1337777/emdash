#!/usr/bin/env python3
"""Assemble native x/u controls with normalization before Hom-cat inversion.

The selected inference change removes only Hom_cat's eager injective flag.
Hom remains injective. Existing u-action fragments are consumed unchanged;
their appended fibre annotations are made explicit deterministically.
This script never invokes Lambdapi.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re

DELAYED = '''// Invert residual Hom heads only after native user-rule normalization.
unif_rule Hom_cat $A $x $y ≡ Hom_cat $B $u $v
  ↪ [ $A ≡ $B; $x ≡ $u; $y ≡ $v ];

'''


def digest(data):
    return hashlib.sha256(data).hexdigest()


def explicit_fibres(body):
    for old, new in (
        ('(Fibre_cat E x)', '(@Fibre_cat K E x)'),
        ('(Fibre_cat E y)', '(@Fibre_cat K E y)'),
        ('(Fibre_cat (@Op_catd K E) x)', '(@Fibre_cat (CoAt2_cat K) (@Op_catd K E) x)'),
    ):
        body = body.replace(old, new)
    assert not re.search(r'\(Fibre_cat (?:E|\(@Op_catd K E\)) ', body)
    return body


def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    pins_path = audit / 'homd_u_normalization_inputs.json'
    pins = json.loads(pins_path.read_text())
    for name, expected in pins['sourceInputs'].items():
        assert digest((root / name).read_bytes()) == expected, (name, 'pinned input changed')
    donor_path = root / pins['donor']
    prior_path = audit / 'homd_native_action_verification.json'
    prior = json.loads(prior_path.read_text())
    source = donor_path.read_text()
    assert digest(source.encode()) == prior['outputs'][donor_path.name]
    assert prior['checks'][donor_path.name]['outcome'] == 'passed-fresh'

    declaration = 'injective symbol Hom_cat : Π (A : Cat) (X_A Y_A : τ (Obj A)), Cat;'
    assert source.count(declaration) == 1
    source = source.replace(declaration, declaration.removeprefix('injective '), 1)
    inversion_anchor = '// Proof-time inversion for object classifiers of two rigid hom-category heads.\n'
    assert source.count(inversion_anchor) == 1
    source = source.replace(inversion_anchor, DELAYED + inversion_anchor, 1)
    assert 'injective symbol Hom (A : Cat)' in source
    precomp_old = (audit / 'homd_u_normalization_precomp_old.lpfragment').read_text()
    precomp_new = (audit / 'homd_u_normalization_precomp_new.lpfragment').read_text()
    assert source.count(precomp_old) == 1
    source = source.replace(precomp_old, precomp_new, 1)

    fragments = {}
    for name in ('owner', 'observations', 'controls', 'negative_controls',
                 'law_controls', 'composition_leaf'):
        fragments[name] = (audit / ('homd_u_action_' + name + '.lpfragment')).read_text()
    owner = fragments['owner']
    owner_anchor = '// Existing public names remain available as defined projections of the\n'
    assert source.count(owner_anchor) == 1
    source = source.replace(owner_anchor, owner + '\n' + owner_anchor, 1)

    ordinary_tail = '\n'.join(fragments[name] for name in
                              ('observations', 'controls', 'negative_controls', 'law_controls'))
    normalized_tail = explicit_fibres(ordinary_tail)
    # Carry forward the exact measured tail, not merely similarly named tests.
    measured_path = root / pins['measuredLaws']
    measured = measured_path.read_text()
    marker = '// Derived observations of the actual source action. No extra semantic owner.\n'
    assert measured.count(marker) == 1
    assert normalized_tail == measured[measured.index(marker):]
    measured_receipt = json.loads((root / pins['measuredLawsReceipt']).read_text())
    assert measured_receipt['outcome'] == 'passed-fresh'
    assert measured_receipt['inputs'][measured_receipt['target']] == digest(measured.encode())
    selected_measured = root / pins['measuredSelected']
    selected_receipt = json.loads((root / pins['measuredSelectedReceipt']).read_text())
    assert selected_receipt['outcome'] == 'passed-fresh'
    assert selected_receipt['inputs'][selected_receipt['target']] == digest(selected_measured.read_bytes())
    generic_path = audit / 'homd_u_inversion_controls.lpfragment'
    generic_original = generic_path.read_text()
    implicit_comp = '@comp_fapp0 _ _ _ _ eta epsilon'
    assert generic_original.count(implicit_comp) == 1
    generic_adapted = generic_original.replace(implicit_comp, '@comp_fapp0 (Functor_cat A B) F G H eta epsilon')
    generic_adapted = generic_adapted.replace(
        '// Reconstruct ambient composition from actual Transf inputs. All composition\n'
        '// classifier/endpoints are inferred here, exercising the mixed Hom facade.',
        '// Ordinary ambient composition retains actual Transf inputs and endpoints.\n'
        '// Its category is explicit; no mixed-facade inference bridge is assumed.')
    generic_adapted = generic_adapted.replace(
        '// The mixed facade bridge reconstructs the ambient category, never Cart.',
        '// Ambient transformation membership does not supply Cartesian membership.')
    generic = explicit_fibres(generic_adapted)
    composition = explicit_fibres(fragments['composition_leaf'])
    selected_tail = normalized_tail + '\n' + composition + '\n' + generic
    measured_selected_source = selected_measured.read_text()
    assert measured_selected_source.count(marker) == 1
    strip_comments = lambda body: re.sub(r'//[^\n]*', '', body).strip()
    assert strip_comments(selected_tail) == strip_comments(measured_selected_source[measured_selected_source.index(marker):])
    precomp_controls = (audit / 'homd_u_precomp_controls.lpfragment').read_text()
    assert not re.search(r'(?m)^(?:rule|unif_rule|symbol)\b', precomp_controls)
    combined = source + '\n' + selected_tail + '\n' + precomp_controls
    targets = {
        'combined_controls.lp': combined,
        'implicit_fibre_boundary.lp': source + '\n' + ordinary_tail + '\n' + fragments['composition_leaf'] + '\n' + generic_adapted + '\n' + precomp_controls,
        'restored_hom_cat_injectivity.lp': combined.replace(declaration.removeprefix('injective '), declaration, 1),
        'without_delayed_inversion.lp': combined.replace(DELAYED, '', 1),
        'without_default_precomposition.lp': combined.replace(precomp_new, precomp_old, 1),
    }
    blocks = re.findall(r'(?ms)^rule\b.*?;', owner)
    assert len(blocks) == 8
    groups = {'source_projection': (0, 1, 2), 'component_projection': (3, 4),
              'leaf_projection': (5,), 'law_joins': (6, 7)}
    for name, indices in groups.items():
        variant = combined
        for index in indices:
            assert variant.count(blocks[index]) == 1
            variant = variant.replace(blocks[index], '', 1)
        targets['without_' + name + '.lp'] = variant
    authoring = [Path(__file__).resolve(), pins_path, audit / 'homd_u_normalization_source_closure.md']
    manifest = {
        'status': 'non-library native x/u assembly; authoring manifest only, execution status is recorded in homd_u_normalization_verification.json',
        'contextRevision': pins['contextRevision'],
        'sourceInputs': pins['sourceInputs'],
        'authoringInputs': {str(path.relative_to(root)): digest(path.read_bytes()) for path in authoring},
        'donor': pins['donor'], 'donorReceipt': prior['checks'][donor_path.name]['receipt'],
        'measuredLaws': pins['measuredLaws'], 'measuredLawsReceipt': pins['measuredLawsReceipt'],
        'measuredSelected': pins['measuredSelected'], 'measuredSelectedReceipt': pins['measuredSelectedReceipt'],
        'measuredTailSha256': digest(normalized_tail.encode()),
        'normalizationPolicy': 'Only Hom_cat loses eager injectivity; residual same-head inversion is delayed. Hom alias stays injective. New consumer fibre bases are explicit.',
        'selectedCompositionScope': 'Existing precomposition accumulation owners restored for arbitrary default-strict F. Selected controls include the actual two-factor nested leaf comparison.',
        'genericAmbientComposition': 'Category and endpoints explicit; no mixed-facade inference bridge is added.',
        'defaultPrecomposition': {'oldSha256': digest(precomp_old.encode()), 'newSha256': digest(precomp_new.encode())},
        'ruleGroups': {name: [digest(blocks[index].encode()) for index in indices] for name, indices in groups.items()},
        'newAssertionCounts': {'uLawsTail': {'positive': len(re.findall(r'(?m)^assert\b', normalized_tail)),
                                           'negative': len(re.findall(r'(?m)^assertnot\b', normalized_tail))},
                               'twoFactorComposition': {'positive': len(re.findall(r'(?m)^assert\b', composition)), 'negative': 0},
                               'genericPrecomposition': {'positive': len(re.findall(r'(?m)^assert\b', precomp_controls)),
                                                        'negative': len(re.findall(r'(?m)^assertnot\b', precomp_controls))},
                               'generic': {'positive': len(re.findall(r'(?m)^assert\b', generic)),
                                           'negative': len(re.findall(r'(?m)^assertnot\b', generic))}},
        'outputs': {name: digest(body.encode()) for name, body in targets.items()},
        'checkerInvoked': False,
    }
    package = (root / 'lambdapi.pkg').read_bytes()
    manifest['outputs']['lambdapi.pkg'] = digest(package)
    return root, targets, package, manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true')
    args = parser.parse_args()
    root, targets, package, manifest = build()
    if not args.check_authoring:
        output = root / 'tmp/probes/homd_u_normalization'
        output.mkdir(parents=True, exist_ok=True)
        for name, body in targets.items():
            target = output / name
            if target.exists():
                assert target.read_text() == body, (name, 'preserve previously emitted bytes; label a successor')
            target.write_text(body)
        (output / 'lambdapi.pkg').write_bytes(package)
        (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'status': 'authoring pins pass; Lambdapi not run', 'targets': list(targets)}, indent=2))


if __name__ == '__main__':
    main()
