#!/usr/bin/env python3
"""Rebuild the bounded lift-middle experiment without invoking Lambdapi.

The source donor is cart_action's pinned Q prefix. Existing LP fragments
remain the authoring inputs; the six original temporary control snippets
and the native normal-form queries are preserved below as literal text.
Historical comment spelling/blank lines are retained for receipt identity.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re


# These controls were originally authored in tmp/probes/lift_middle.
# Store their exact text here so regeneration does not read its own outputs.
CONTROLS = {
    'mapped_post': '''
assert [A B : Cat] (F : τ (Functor A B)) [x y z : τ (Obj A)] (g : τ (Hom A y z)) ⊢
 @eq_refl (Functor (Hom_cat A x y) (Hom_cat B (fapp0 F x) (fapp0 F z))) (@comp_cat_fapp0 _ _ _ (@hom_postcomp_func B B (@id_func B) (fapp0 F x) (fapp0 F y) (fapp0 F z) (@fapp1_fapp0 A B F y z g)) (@fapp1_func A B F x y))
 : τ (@= (Functor (Hom_cat A x y) (Hom_cat B (fapp0 F x) (fapp0 F z))) (@comp_cat_fapp0 _ _ _ (@hom_postcomp_func B B (@id_func B) (fapp0 F x) (fapp0 F y) (fapp0 F z) (@fapp1_fapp0 A B F y z g)) (@fapp1_func A B F x y)) (@comp_cat_fapp0 _ _ _ (@fapp1_func A B F x z) (@hom_postcomp_func A A (@id_func A) x y z g)));
''',
    'mapped_pre': '''
assert [A B : Cat] (F : τ (Functor A B)) [w x y : τ (Obj A)] (h : τ (Hom A w x)) ⊢
 @eq_refl (Functor (Hom_cat A x y) (Hom_cat B (fapp0 F w) (fapp0 F y))) (@comp_cat_fapp0 _ _ _ (@hom_precomp_along_func B B (@id_func B) (fapp0 F y) (fapp0 F w) (fapp0 F x) (@fapp1_fapp0 A B F w x h)) (@fapp1_func A B F x y))
 : τ (@= (Functor (Hom_cat A x y) (Hom_cat B (fapp0 F w) (fapp0 F y))) (@comp_cat_fapp0 _ _ _ (@hom_precomp_along_func B B (@id_func B) (fapp0 F y) (fapp0 F w) (fapp0 F x) (@fapp1_fapp0 A B F w x h)) (@fapp1_func A B F x y)) (@comp_cat_fapp0 _ _ _ (@fapp1_func A B F w y) (@hom_precomp_along_func A A (@id_func A) y w x h)));
''',
    'blended_post': '''
assert [A B : Cat] (F : τ (Functor A B)) [x y z : τ (Obj A)] (g : τ (Hom A y z)) ⊢
 @eq_refl (Functor (Hom_cat A x y) (Hom_cat B (fapp0 F x) (fapp0 F z))) (@comp_cat_fapp0 _ _ _ (@hom_postcomp_func B A F (fapp0 F x) y z g) (@fapp1_func A B F x y))
 : τ (@= (Functor (Hom_cat A x y) (Hom_cat B (fapp0 F x) (fapp0 F z))) (@comp_cat_fapp0 _ _ _ (@hom_postcomp_func B A F (fapp0 F x) y z g) (@fapp1_func A B F x y)) (@comp_cat_fapp0 _ _ _ (@fapp1_func A B F x z) (@hom_postcomp_func A A (@id_func A) x y z g)));
''',
    'mixed_order': '''
assert [C : Cat] [a b c d : τ (Obj C)] (f : τ (Hom C a b)) (g : τ (Hom C c d)) ⊢
 @eq_refl (Functor (Hom_cat C b c) (Hom_cat C a d)) (@comp_cat_fapp0 _ _ _ (@hom_postcomp_func C C (@id_func C) a c d g) (@hom_precomp_along_func C C (@id_func C) c a b f))
 : τ (@= (Functor (Hom_cat C b c) (Hom_cat C a d)) (@comp_cat_fapp0 _ _ _ (@hom_postcomp_func C C (@id_func C) a c d g) (@hom_precomp_along_func C C (@id_func C) c a b f)) (@comp_cat_fapp0 _ _ _ (@hom_precomp_along_func C C (@id_func C) d a b f) (@hom_postcomp_func C C (@id_func C) b c d g)));
''',
    'unit': '''
// Typed whole comparison, not an operational proof argument.
assert [K : Cat] [E D : τ (Catd K)]
 (U : τ (@StrictTransfor K Cat_cat E D)) (x y : τ (Obj K)) ⊢
 @eq_refl (Functor (Hom_cat K x y)
   (Hom_cat Prof_cov_universe (Fibre_cat D x) (Fibre_cat E y)))
   (@Prof_cov_lift_middle_func K E D U x y)
 : τ (@= (Functor (Hom_cat K x y)
   (Hom_cat Prof_cov_universe (Fibre_cat D x) (Fibre_cat E y)))
   (@Prof_cov_lift_middle_func K E D U x y)
   (@comp_cat_fapp0 _ _ _
        (@hom_postcomp_func Prof_cov_universe Prof_cov_universe
          (@id_func Prof_cov_universe) (Fibre_cat D x) (Fibre_cat E y) (Fibre_cat E y)
          (@comp_fapp0 Prof_cov_universe (Fibre_cat E y) (Fibre_cat D y) (Fibre_cat E y)
            (@Prof_cov_companion (Fibre_cat E y) (Fibre_cat D y)
              (@tapp0_fapp0 K Cat_cat E D y (@strict_transfor K Cat_cat E D U)))
            (@fapp1_fapp0 Cat_cat Prof_cov_universe Prof_cov_include (Fibre_cat E y) (Fibre_cat D y)
              (@tapp0_fapp0 K Cat_cat E D y (@strict_transfor K Cat_cat E D U)))))
        (@Prof_cov_lift_left_func K E D U x y)));
''',
    'counit': '''
// Typed whole comparison, not an operational proof argument.
assert [K : Cat] [E D : τ (Catd K)]
 (U : τ (@StrictTransfor K Cat_cat E D)) (x y : τ (Obj K)) ⊢
 @eq_refl (Functor (Hom_cat K x y)
   (Hom_cat Prof_cov_universe (Fibre_cat D x) (Fibre_cat E y)))
   (@Prof_cov_lift_middle_func K E D U x y)
 : τ (@= (Functor (Hom_cat K x y)
   (Hom_cat Prof_cov_universe (Fibre_cat D x) (Fibre_cat E y)))
   (@Prof_cov_lift_middle_func K E D U x y)
   (@comp_cat_fapp0 _ _ _
        (@hom_precomp_along_func Prof_cov_universe Prof_cov_universe
          (@id_func Prof_cov_universe) (Fibre_cat E y) (Fibre_cat D x) (Fibre_cat D x)
          (@comp_fapp0 Prof_cov_universe (Fibre_cat D x) (Fibre_cat E x) (Fibre_cat D x)
            (@fapp1_fapp0 Cat_cat Prof_cov_universe Prof_cov_include (Fibre_cat E x) (Fibre_cat D x)
              (@tapp0_fapp0 K Cat_cat E D x (@strict_transfor K Cat_cat E D U)))
            (@Prof_cov_companion (Fibre_cat E x) (Fibre_cat D x)
              (@tapp0_fapp0 K Cat_cat E D x (@strict_transfor K Cat_cat E D U)))))
        (@Prof_cov_lift_right_func K E D U x y)));
''',
}

NORMAL_FORM_QUERIES = '''


compute λ (K : Cat) (E D : τ (Catd K)) (U : τ (@StrictTransfor K Cat_cat E D)) (x y : τ (Obj K)), @Prof_cov_lift_middle_func K E D U x y;

compute λ (K : Cat) (E D : τ (Catd K)) (U : τ (@StrictTransfor K Cat_cat E D)) (x y : τ (Obj K)), (@comp_cat_fapp0 _ _ _
        (@hom_postcomp_func Prof_cov_universe Prof_cov_universe
          (@id_func Prof_cov_universe) (Fibre_cat D x) (Fibre_cat E y) (Fibre_cat E y)
          (@comp_fapp0 Prof_cov_universe (Fibre_cat E y) (Fibre_cat D y) (Fibre_cat E y)
            (@Prof_cov_companion (Fibre_cat E y) (Fibre_cat D y)
              (@tapp0_fapp0 K Cat_cat E D y (@strict_transfor K Cat_cat E D U)))
            (@fapp1_fapp0 Cat_cat Prof_cov_universe Prof_cov_include (Fibre_cat E y) (Fibre_cat D y)
              (@tapp0_fapp0 K Cat_cat E D y (@strict_transfor K Cat_cat E D U)))))
        (@Prof_cov_lift_left_func K E D U x y));

compute λ (K : Cat) (E D : τ (Catd K)) (U : τ (@StrictTransfor K Cat_cat E D)) (x y : τ (Obj K)), (@comp_cat_fapp0 _ _ _
        (@hom_precomp_along_func Prof_cov_universe Prof_cov_universe
          (@id_func Prof_cov_universe) (Fibre_cat E y) (Fibre_cat D x) (Fibre_cat D x)
          (@comp_fapp0 Prof_cov_universe (Fibre_cat D x) (Fibre_cat E x) (Fibre_cat D x)
            (@fapp1_fapp0 Cat_cat Prof_cov_universe Prof_cov_include (Fibre_cat E x) (Fibre_cat D x)
              (@tapp0_fapp0 K Cat_cat E D x (@strict_transfor K Cat_cat E D U)))
            (@Prof_cov_companion (Fibre_cat E x) (Fibre_cat D x)
              (@tapp0_fapp0 K Cat_cat E D x (@strict_transfor K Cat_cat E D U)))))
        (@Prof_cov_lift_right_func K E D U x y));
'''


FRAGMENTS = (
    'lift_middle.lpfragment',
    'lift_middle_whiskering.lpfragment',
    'lift_middle_whiskering_controls.lpfragment',
    'lift_middle_image_rules.lpfragment',
    'lift_middle_naturality_rules.lpfragment',
    'lift_middle_context_controls.lpfragment',
    'lift_middle_inclusion_image.lpfragment',
    'lift_middle_inclusion_controls.lpfragment',
    'lift_middle_contextual_factorizations.lpfragment',
    'lift_middle_contextual_controls.lpfragment',
    'lift_middle_contextual_explicit_domains.lpfragment',
    'lift_middle_contextual_shared_arrows.lpfragment',
    'lift_middle_fused_post_square.lpfragment',
    'lift_middle_fused_post_controls.lpfragment',
    'lift_middle_mate_component_controls.lpfragment',
    'q_lift_mate.lpfragment',
    'cart_action_q_controls.lpfragment',
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def insert_before(source, anchor, fragment):
    assert source.count(anchor) == 1, ('non-unique owner anchor', anchor)
    return source.replace(anchor, fragment + '\n' + anchor)


def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    prior_path = audit / 'cart_action_verification.json'
    prior = json.loads(prior_path.read_text())
    donor = root / 'tmp/probes/strict_default_cart_action/emdash3_2.lp'
    source = donor.read_text()
    assert digest(source.encode()) == prior['outputs']['emdash3_2.lp'], 'cart_action donor pin changed'
    marker = '// 14. Section action over dependent homs'
    assert source.count(marker) == 1, marker
    prefix = source[:source.index(marker)]
    assert digest(prefix.encode()) == prior['outputs']['q_prefix.lp'], 'cart_action prefix pin changed'
    f = {name: (audit / name).read_text() for name in FRAGMENTS}
    mate = f['q_lift_mate.lpfragment']
    assert mate.count('// WHOLE MATE:') == 1
    partial = mate[:mate.index('// WHOLE MATE:')]
    section_anchor = '// The y-section is the existing transformation category in the coefficient.'

    def constructor(base):
        return insert_before(base, section_anchor,
                             partial + '\n' + f['lift_middle.lpfragment'])

    whisker = f['lift_middle_whiskering.lpfragment']
    assert len(re.findall(r'(?m)^unif_rule\b', whisker)) == 3
    # The first checked whiskering variants predate the annotation-only edit
    # to numeric lhs-audit slots. Reproduce those comments explicitly instead
    # of attributing their old receipts to different emitted source bytes.
    old_whisker = whisker
    annotation = '// lhs-audit: keep 1 -- compares whole functor composition.'
    assert old_whisker.count(annotation) == 2
    for heads in ('hom_postcomp_func,hom_precomp_along_func',
                  'hom_precomp_along_func,hom_postcomp_func'):
        old_whisker = old_whisker.replace(annotation,
            '// lhs-audit: keep Cat_cat -- compares whole functor composition.\n'
            '// lhs-audit: keep ' + heads
            + ' -- identity-family endpoints determine the two Hom cuts.', 1)
    whisker_anchor = '// 7b. Evaluation and fixed-object evaluation'
    early = insert_before(prefix, whisker_anchor, old_whisker)
    image = insert_before(prefix, whisker_anchor, whisker)
    image = insert_before(image,
        '/* API-04V RULE-OFF CONTROL: these three raw folds can recover',
        f['lift_middle_naturality_rules.lpfragment'])
    image = insert_before(image,
        '/*\n  The former whole post/left and pre/right strict-functoriality accumulation',
        f['lift_middle_image_rules.lpfragment'])
    included = insert_before(image,
        '// Fixed postcomposition uses the existing ambient whiskering, so a general',
        f['lift_middle_inclusion_image.lpfragment'])
    controls = ('\n' + f['lift_middle_whiskering_controls.lpfragment'] + '\n'
                + '\n'.join(CONTROLS[name] for name in ('mapped_post', 'mapped_pre', 'blended_post')))
    targets = {
        'constructor.lp': constructor(prefix),
        'whiskering.lp': early + '\n' + f['lift_middle_whiskering_controls.lpfragment'],
        'image_rules.lp': image + controls,
        'context.lp': image + controls + '\n' + f['lift_middle_context_controls.lpfragment'],
        'inclusion_image.lp': included + controls + '\n' + f['lift_middle_inclusion_controls.lpfragment'],
        'mate_image.lp': insert_before(image, section_anchor, mate),
        'mate_included.lp': insert_before(included, section_anchor, mate),
        'middle_normal_forms.lp': constructor(image) + NORMAL_FORM_QUERIES,
    }
    for name in ('mapped_post', 'mapped_pre', 'blended_post', 'mixed_order'):
        targets[name + '.lp'] = prefix + '\n' + f['cart_action_q_controls.lpfragment'] + CONTROLS[name]
    for kind in ('unit', 'counit'):
        targets[kind + '_comparison.lp'] = constructor(prefix) + CONTROLS[kind]
        for name, base in (('whiskering', early), ('image', image), ('included', included)):
            targets[kind + '_' + name + '.lp'] = constructor(base) + '\n' + CONTROLS[kind]
    for label, fragment in (('image', 'lift_middle_image_rules.lpfragment'),
                            ('naturality', 'lift_middle_naturality_rules.lpfragment')):
        assert targets['context.lp'].count(f[fragment]) == 1
        targets['no_' + label + '_context.lp'] = targets['context.lp'].replace(f[fragment], '')
    # Removal evidence shows the contextual strict-naturality pair is not
    # required by the current controls. Also test removing the last two
    # contextual image clauses, retaining the first two mapped-image cuts.
    # Preserve historical targets; these are separate unqualified variants.
    image_fragment = f['lift_middle_image_rules.lpfragment']
    contextual_marker = '// Left association can hide the existing post/left strict-image redex'
    assert image_fragment.count(contextual_marker) == 1
    contextual_image = image_fragment[image_fragment.index(contextual_marker):]
    assert len(re.findall(r'(?m)^rule\b', contextual_image)) == 2
    def minimal(candidate):
        assert candidate.count(f['lift_middle_naturality_rules.lpfragment']) == 1
        assert candidate.count(contextual_image) == 1
        return candidate.replace(
            f['lift_middle_naturality_rules.lpfragment'], '').replace(contextual_image, '')
    for name in ('context.lp', 'inclusion_image.lp'):
        targets['minimal_' + name] = minimal(targets[name])
    contextual = f['lift_middle_contextual_factorizations.lpfragment']
    assert len(re.findall(r'(?m)^unif_rule\b', contextual)) == 2
    assert not re.search(r'(?m)^rule\b', contextual)
    contextual_controls = f['lift_middle_contextual_controls.lpfragment']
    targets['contextual_factorizations.lp'] = insert_before(
        targets['minimal_inclusion_image.lp'], whisker_anchor, contextual) + '\n' + contextual_controls
    targets['no_contextual_factorizations.lp'] = targets['minimal_inclusion_image.lp'] + '\n' + contextual_controls
    for name in ('unit_included.lp', 'counit_included.lp', 'mate_included.lp'):
        targets['contextual_' + name] = insert_before(minimal(targets[name]), whisker_anchor, contextual)
    # The first contextual factorization check exposes a new real consumer
    # of guarded naturality under an outer functor. Restore only that pair;
    # preserve the failed minimal sources and omit contextual image cuts.
    for output_name, input_name in (
            ('contextual_naturality.lp', 'contextual_factorizations.lp'),
            ('contextual_naturality_unit_included.lp', 'contextual_unit_included.lp'),
            ('contextual_naturality_counit_included.lp', 'contextual_counit_included.lp')):
        candidate = targets[input_name]
        assert f['lift_middle_naturality_rules.lpfragment'] not in candidate
        assert contextual_image not in candidate
        targets[output_name] = insert_before(candidate,
            '/* API-04V RULE-OFF CONTROL: these three raw folds can recover',
            f['lift_middle_naturality_rules.lpfragment'])
    explicit_domains = f['lift_middle_contextual_explicit_domains.lpfragment']
    assert len(re.findall(r'(?m)^unif_rule\b', explicit_domains)) == 2
    assert not re.search(r'(?m)^rule\b', explicit_domains)
    for suffix in ('', '_unit_included', '_counit_included'):
        candidate = targets['contextual_naturality' + suffix + '.lp']
        assert candidate.count(contextual) == 1
        targets['contextual_explicit_domains' + suffix + '.lp'] = candidate.replace(
            contextual, explicit_domains)
    # Retype the existing two steps against the already defined common M.
    # Their original bodies and the final composite remain byte-identical.
    named_mate = mate
    for symbol, source_name, target_name in (
            ('Prof_cov_lift_unit_step', 'Prof_cov_lift_left_func', 'Prof_cov_lift_middle_func'),
            ('Prof_cov_lift_counit_step', 'Prof_cov_lift_middle_func', 'Prof_cov_lift_right_func')):
        symbol_anchor = 'symbol ' + symbol + ' '
        assert named_mate.count(symbol_anchor) == 1
        start = named_mate.index(symbol_anchor)
        annotation = named_mate.index('  : τ (Transf', start)
        body_start = named_mate.index('≔', annotation)
        body_end = named_mate.index(';', body_start) + 1
        body = named_mate[body_start:body_end]
        named_mate = (named_mate[:annotation]
            + '  : τ (Transf (@' + source_name + ' K E D U x y)\n'
            + '      (@' + target_name + ' K E D U x y))\n'
            + named_mate[body_start:])
        assert named_mate.count(body) == 1
    named_mate = insert_before(named_mate,
        '// First whole step: whisker the canonical unit at U[y] by the left functor.',
        f['lift_middle.lpfragment'])
    named_source = targets['contextual_mate_included.lp']
    assert named_source.count(contextual) == named_source.count(mate) == 1
    named_source = named_source.replace(contextual, explicit_domains).replace(mate, named_mate)
    named_source = insert_before(named_source,
        '/* API-04V RULE-OFF CONTROL: these three raw folds can recover',
        f['lift_middle_naturality_rules.lpfragment'])
    targets['contextual_explicit_domains_named_middle_mate.lp'] = named_source
    shared_arrows = f['lift_middle_contextual_shared_arrows.lpfragment']
    fused_post = f['lift_middle_fused_post_square.lpfragment']
    assert len(re.findall(r'(?m)^unif_rule\b', shared_arrows)) == 2
    assert len(re.findall(r'(?m)^rule\b', fused_post)) == 1
    for suffix in ('', '_unit_included', '_counit_included', '_named_middle_mate'):
        candidate = targets['contextual_explicit_domains' + suffix + '.lp']
        assert candidate.count(explicit_domains) == 1
        candidate = candidate.replace(explicit_domains, shared_arrows)
        candidate = insert_before(candidate,
            '/* API-04V RULE-OFF CONTROL: these three raw folds can recover', fused_post)
        if not suffix:
            candidate += '\n' + f['lift_middle_fused_post_controls.lpfragment']
        targets['shared_arrows_fused_post' + suffix + '.lp'] = candidate
    selected_mate = targets['shared_arrows_fused_post_named_middle_mate.lp']
    for label, rules in (
            ('shared_context', shared_arrows), ('fused_post', fused_post),
            ('contextual_naturality', f['lift_middle_naturality_rules.lpfragment'])):
        assert selected_mate.count(rules) == 1
        targets['named_middle_mate_without_' + label + '.lp'] = selected_mate.replace(rules, '')
    targets['named_middle_mate_components.lp'] = (
        selected_mate + '\n' + f['lift_middle_mate_component_controls.lpfragment'])
    package = (root / 'lambdapi.pkg').read_bytes()
    assert digest(package) == prior['outputs']['lambdapi.pkg'], 'package pin changed'
    inputs = [Path(__file__).resolve(), prior_path, donor, root / 'lambdapi.pkg']
    inputs += [audit / name for name in FRAGMENTS]
    manifest = {
        'status': 'non-library; whole lift and Q qualification remain open',
        'donorVerification': str(prior_path.relative_to(root)),
        'sourceInputs': {str(p.relative_to(root)): digest(p.read_bytes()) for p in inputs},
        'prefixSha256': digest(prefix.encode()),
        'outputs': {name: digest(text.encode()) for name, text in targets.items()},
        'outputControlCounts': {name: {
            'positive': len(re.findall(r'(?m)^assert\b', text)),
            'negative': len(re.findall(r'(?m)^assertnot\b', text)),
        } for name, text in targets.items()},
        'checkerInvoked': False,
    }
    manifest['outputs']['lambdapi.pkg'] = digest(package)
    return root, targets, package, manifest


def check_pins(audit, manifest):
    record = json.loads((audit / 'lift_middle_verification.json').read_text())
    for group in ('sourceInputs', 'outputs'):
        assert manifest[group] == record[group], group + ' changed; review and requalify instead of updating pins automatically'
    return record


def check_evidence(root, record):
    # This reads existing receipts only. Passing old checks does not execute
    # the checker or qualify any changed source/profile.
    entries = list(record['checks'].items()) + list(record.get('externalProbeEvidence', {}).items())
    for name, evidence in entries:
        receipt_path = root / evidence['receipt']
        assert digest(receipt_path.read_bytes()) == evidence['receiptSha256'], name
        receipt = json.loads(receipt_path.read_text())
        expected_source = evidence.get('sourceSha256', record['outputs'].get(name))
        assert receipt['inputs'][receipt['target']] == expected_source, name
        for path, expected in receipt['inputs'].items():
            assert digest((root / path).read_bytes()) == expected, path
        log = root / receipt['log']
        assert digest(log.read_bytes()) == receipt['logSha256'] == evidence['logSha256'], name
        assert digest((root / evidence['output']).read_bytes()) == evidence['outputSha256'], name
        assert receipt['outcome'] == evidence['outcome'], name
        assert receipt['checkerExit'] == evidence['checkerExit'], name
    historical = record.get('historicalChecks', {})
    for name, evidence in historical.items():
        path = root / evidence['receipt']
        assert digest(path.read_bytes()) == evidence['receiptSha256'], name
        receipt = json.loads(path.read_text())
        assert receipt['inputs'][receipt['target']] == evidence['sourceSha256'], name
        for expected in receipt['inputs'].values():
            archive = root / receipt['inputStore'] / expected
            assert digest(archive.read_bytes()) == expected, str(archive)
        assert digest((root / receipt['log']).read_bytes()) == evidence['logSha256'], name
        assert receipt['outcome'] == evidence['outcome'], name
        assert receipt['checkerExit'] == evidence['checkerExit'], name
    return len(entries) + len(historical)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true',
                        help='verify pinned authoring and emitted hashes without writing')
    parser.add_argument('--check-evidence', action='store_true',
                        help='also verify saved receipts/logs and existing target bytes; never run Lambdapi')
    args = parser.parse_args()
    root, targets, package, manifest = build()
    record = check_pins(Path(__file__).resolve().parent, manifest)
    if args.check_evidence:
        print(f'Verified {check_evidence(root, record)} existing receipt/source/log identities; no checker run.')
    if not args.check_authoring:
        output = root / 'tmp/probes/lift_middle'
        output.mkdir(parents=True, exist_ok=True)
        for name, source in targets.items():
            (output / name).write_text(source)
        (output / 'lambdapi.pkg').write_bytes(package)
        (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'{len(targets)} lift-middle targets reproduce their pinned bytes; no Q/lift completion claimed.')


if __name__ == '__main__':
    main()
