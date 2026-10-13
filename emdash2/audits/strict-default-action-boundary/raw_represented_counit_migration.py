#!/usr/bin/env python3
"""Emit a bounded raw-counit owner/first-consumer replay; never run Lambdapi.

The upstream strict-default prefix is inherited from the pinned q_unit copy.
Every Prof declaration/rule below is copied unchanged from the pinned raw
production source. This is explicitly not a full-source continuation.
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
    pin_path = audit / 'raw_represented_counit_inputs.json'
    pins = json.loads(pin_path.read_text())
    inputs = {}
    for relative, expected in pins['sourceInputs'].items():
        if relative == 'emdash3_2.lp':
            data = subprocess.check_output(
                ['git', 'show', pins['productionRevision'] + ':emdash2/' + relative],
                cwd=root)
        else:
            data = (root / relative).read_bytes()
        actual = digest(data)
        assert actual == expected, (relative, 'source pin changed', expected, actual)
        inputs[relative] = data
    donor_path = 'tmp/probes/strict_default_q_unit/emdash3_2.lp'
    production_path = 'emdash3_2.lp'
    prior = json.loads(inputs['audits/strict-default-action-boundary/q_unit_verification.json'])
    assert digest(inputs[donor_path]) == prior['outputs']['emdash3_2.lp']
    assert digest(inputs['lambdapi.pkg']) == prior['outputs']['lambdapi.pkg']
    donor = inputs[donor_path].decode()
    production = inputs[production_path].decode()
    anchor = '// Profunctor base: A^op × B.'
    assert donor.count(anchor) == 1
    prefix = donor[:donor.index(anchor)]
    assert not re.search(r'(?m)^(?:injective |constant )?symbol Prof(?:_|\b)', prefix)
    assert 'injective symbol Functor_cart_cat' in prefix
    assert 'rule @fapp1_fapp0 $A $B $F $X $X (@id $A $X)' in prefix
    records = []

    def record(label, start, end):
        block = production[start:end]
        records.append({
            'label': label,
            'source': production_path,
            'startLine': production.count('\n', 0, start) + 1,
            'endLine': production.count('\n', 0, end),
            'sha256': digest(block.encode()),
        })
        return '// Unchanged raw production owner: ' + label + '\n' + block

    def between(label, start, end):
        assert production.count(start) == 1, start
        assert production.count(end) == 1, end
        i = production.index(start)
        j = production.index(end, i)
        return record(label, i, j)

    def symbol(name):
        matches = list(re.finditer(
            r'(?m)^(?:injective |constant )?symbol ' + re.escape(name) + r'\b[\s\S]*?;\n',
            production))
        assert len(matches) == 1, (name, len(matches))
        match = matches[0]
        return record(name, match.start(), match.end())

    blocks = [between('raw Prof classifiers', anchor,
        '// 18b. Opposite profunctors and fixed-endpoint duality')]
    blocks += [symbol('Prof_reindex')]
    blocks += [between('reindex fibre projection',
        '// Object/fibre projection of profunctor reindexing.',
        '// Full base-arrow action of reindexing.')]
    blocks += [between('identity endpoint reindexing',
        '// Reindexing along identity endpoint functors is neutral.',
        '// Nested reindexing accumulates both endpoint functors.')]
    blocks += [symbol(name) for name in (
        'Hom_prof_along', 'Hom_prof', 'Companion_prof', 'Conjoint_prof',
        'Prof_transf_cat', 'Prof_hom_cat', 'Prof_hom', 'Prof_tensor',
        'Prof_imply_cov', 'Prof_eval_cov_map', 'Prof_lambda_cov_map',
        'Prof_coyoneda_cov_map', 'Prof_reindex_transf')]
    blocks += [between('implication endpoint reindexing',
        '// Reindexing the implication result acts on the left endpoints of both inputs.',
        '/*\n  Mixed-variance covariant implication.')]
    blocks += [between('closed beta/eta',
        '// Covariant beta/eta: lambda(eval(t))',
        '/*\n  Contravariant profunctor implication.')]
    blocks += [between('reindexed map whole-fibre component',
        '// Component of the existing whole reindexed map: retain the entire fibre functor.',
        '// Capped hom-action: Prof_reindex_func(F,G)[r]')]
    blocks += [between('identity endpoint reindexing of maps',
        '// Identity endpoint reindexing leaves a vertical profunctor map unchanged.',
        '// Probe: stable arrow action of profunctor reindexing should not hide')]
    closure = '\n'.join(blocks)
    assert '↪ @Functord_cat (Product_cat (Op_cat $A) $B) $P $Q;' in closure
    assert 'symbol Unit_prof' not in closure  # The strict-default donor owns it.
    assert 'Functor_cart_cat' not in closure
    assert not re.search(r'(?m)^rule @Prof_imply_cov\b', closure)
    candidate_path = audit / 'raw_represented_counit.lpfragment'
    controls_path = audit / 'raw_represented_counit_controls.lpfragment'
    candidate = candidate_path.read_text()
    controls = controls_path.read_text()
    component_path = audit / 'raw_represented_counit_component_boundary.lpfragment'
    component = component_path.read_text().rstrip() + '\n\n'
    assert not re.search(r'(?m)^(?:rule|unif_rule)\b', candidate + controls)
    owner = prefix + '\n// BOUNDED RAW PROF OWNER CLOSURE; not a full kernel.\n' + closure
    constructor = owner + '\n' + candidate
    first_consumer = constructor + '\n' + controls
    targets = {
        'owner_prefix.lp': owner,
        'constructor_boundary.lp': constructor,
        'first_consumer.lp': first_consumer,
        'component_boundary.lp': first_consumer + '\n' + component,
    }
    # Separately labelled comparison experiment: preserve the runtime
    # reindexing head, while comparing its implication presentation at proof time.
    law_start = closure.index('// Reindexing the implication result acts')
    law_end = closure.index(';', law_start) + 1
    law = closure[law_start:law_end]
    # Match only rigid outer heads. The target's reindexed inputs may have
    # normalized already, so compare them in side conditions, not patterns.
    comparison = """
unif_rule
  @Prof_reindex $A $A' $B $B'
    (@Prof_imply_cov $A $B $X $O $Q) $F $M
  ≡ @Prof_imply_cov $A0 $B0 $X0 $O0 $Q0
  ↪ [ $A' ≡ $A0; $B' ≡ $B0; $X ≡ $X0;
      $O0 ≡ @Prof_reindex $A $A' $X $X $O $F (@id_func $X);
      $Q0 ≡ @Prof_reindex $B $B' $X $X $Q $M (@id_func $X) ];
"""
    variant_candidate = candidate.replace(
        '(@Prof_imply_cov B A B\n        (@Unit_prof B) (@Companion_prof A B F)))',
        '(@Prof_reindex B B B A\n        (@Prof_imply_cov B B B (@Unit_prof B) (@Unit_prof B)) (@id_func B) F))', 1)
    assert variant_candidate != candidate
    c_start = controls.index('// The target is computed')
    c_end = controls.index('assert [A B : Cat] (F : τ (Functor A B)) ⊢', c_start)
    c_end = controls.index(';', c_end) + 1
    comparison_control = """// Whole canonical target remains available at proof time.
assert [A B : Cat] (F : τ (Functor A B)) ⊢
  @eq_refl (Prof B A)
    (@Prof_reindex B B B A
      (@Prof_imply_cov B B B (@Unit_prof B) (@Unit_prof B)) (@id_func B) F)
  : τ (@= (Prof B A)
    (@Prof_reindex B B B A
      (@Prof_imply_cov B B B (@Unit_prof B) (@Unit_prof B)) (@id_func B) F)
    (@Prof_imply_cov B A B (@Unit_prof B) (@Companion_prof A B F)));
"""
    comparison_control += """
// The general whole law is also tested before identity reindexing specializes it.
assert [A A' B B' X : Cat] (O : τ (Prof A X)) (Q : τ (Prof B X))
  (F : τ (Functor A' A)) (M : τ (Functor B' B)) ⊢
  @eq_refl (Prof A' B') (@Prof_reindex A A' B B' (@Prof_imply_cov A B X O Q) F M)
  : τ (@= (Prof A' B')
      (@Prof_reindex A A' B B' (@Prof_imply_cov A B X O Q) F M)
      (@Prof_imply_cov A' B' X
        (@Prof_reindex A A' X X O F (@id_func X))
        (@Prof_reindex B B' X X Q M (@id_func X))));
"""
    variant_controls = controls[:c_start] + comparison_control + controls[c_end:]
    variant_component = component.replace(
        '(@Prof_imply_cov B A B (@Unit_prof B) (@Companion_prof A B F)) ba',
        '(@Prof_reindex B B B A\n      (@Prof_imply_cov B B B (@Unit_prof B) (@Unit_prof B)) (@id_func B) F) ba')
    targets['comparison_variant.lp'] = (owner.replace(law, comparison) + '\n' +
        variant_candidate + '\n' + variant_controls + '\n' + variant_component)
    fibre_path = audit / 'raw_represented_counit_fibre_view.lpfragment'
    fibre_view = fibre_path.read_text()
    targets['fibre_view_variant.lp'] = owner + '\n' + fibre_view + '\n' + candidate + '\n' + controls + '\n' + component
    targets['no_implication_reindex.lp'] = first_consumer.replace(law, '')
    targets['no_comparison_instance.lp'] = targets['comparison_variant.lp'].replace(
        comparison, '')
    beta_start = owner.index('// Covariant beta/eta: lambda(eval(t))')
    beta_end = owner.index('// Unchanged raw production owner:', beta_start)
    targets['no_closed_beta.lp'] = first_consumer.replace(owner[beta_start:beta_end], '')
    authoring = (Path(__file__), pin_path, candidate_path, controls_path, component_path, fibre_path,
                 audit / 'raw_represented_counit_source_closure.md')
    manifest = {
        'status': 'authoring replay only; no checker result recorded by this builder',
        'boundary': 'strict-default prefix plus unchanged raw Prof owners and first consumers',
        'fullSourceContinuation': False,
        'fibreViewVariant': 'Original runtime law and operational annotations remain unchanged; add only its normalized represented fibre comparison.',
        'comparisonVariant': 'Implication reindexing changes from runtime to proof-time with normalized target inputs compared in side conditions; j_F return annotation and component observation retain the reindex head. All operational bodies unchanged.',
        'qualification': {
            'rawPublicProfMap': 'preserved as Functord; no global Cartesian retyping',
            'candidate': 'derived lambda(co-Yoneda), endpoint reindexing, evaluation',
            'cartesianAdmission': 'not established',
            'generatorComputation': 'not established',
            'triangleCoherence': 'not established',
            'QCompositionAndLift': 'outside this bounded replay',
        },
        'sourceInputs': pins['sourceInputs'],
        'productionRevision': pins['productionRevision'],
        'strictDefaultPrefix': {
            'source': donor_path,
            'excludedAnchor': anchor,
            'sha256': digest(prefix.encode()),
        },
        'unchangedProductionBlocks': records,
        'authoringInputs': {str(path.relative_to(root)): digest(path.read_bytes()) for path in authoring},
        'outputs': {name: digest(value.encode()) for name, value in targets.items()},
        'newControls': {
            'positive': len(re.findall(r'(?m)^assert\b', controls)),
            'negative': len(re.findall(r'(?m)^assertnot\b', controls)),
        },
    }
    return root, targets, inputs['lambdapi.pkg'], manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true',
                        help='validate source pins and extraction in memory; write nothing')
    args = parser.parse_args()
    root, targets, package, manifest = build()
    if args.check_authoring:
        print(json.dumps({'status': 'authoring guards pass; Lambdapi not run',
                          'blocks': len(manifest['unchangedProductionBlocks']),
                          'newControls': manifest['newControls']}, indent=2))
        return
    output = root / 'tmp/probes/raw_represented_counit'
    output.mkdir(parents=True, exist_ok=True)
    for name, source in targets.items():
        (output / name).write_text(source)
    (output / 'lambdapi.pkg').write_bytes(package)
    manifest['outputs']['lambdapi.pkg'] = digest(package)
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted bounded raw represented-counit replay; Lambdapi not run.')


if __name__ == '__main__':
    main()
