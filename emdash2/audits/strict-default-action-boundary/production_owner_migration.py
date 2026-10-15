#!/usr/bin/env python3
"""Stage required upstream owners in a full copy of the pre-goal kernel.

This is an in-progress production migration, not another foundation model.
No original downstream section is truncated. Legacy family/Op consumers
are intentionally retained for their subsequent coupled adaptation.

Check imports with scripts/run_lambdapi.py --package-root pointing to the
emitted package. The outer probe wrapper checks the source but inventories
imports relative to the outer package, which is not this staged dependency
snapshot.
"""
import hashlib
import json
import difflib
from pathlib import Path
import re
import subprocess


PIN = 'f8af1fca472657ff1598c639eb29c0566e7b2ec0'
CORE_SHA = '6a980df34be718a23a6be121d170153650830a49f54b7e0eca415705ffb2068a'


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    original = subprocess.check_output(
        ['git', 'show', PIN + ':emdash2/emdash3_2.lp'], cwd=root, text=True)
    profiles = subprocess.check_output(
        ['git', 'show', PIN + ':emdash2/emdash3_2_gray_profiles.lp'], cwd=root, text=True)
    original_profiles = profiles
    assert sha(original) == CORE_SHA
    body = original
    inputs = {}
    changes = []

    def fragment(name):
        path = audit / name
        text = path.read_text()
        inputs[str(path.relative_to(root))] = sha(text)
        return text

    def insert(marker, text, reason):
        nonlocal body
        assert body.count(marker) == 1, marker
        body = body.replace(marker, text + '\n' + marker, 1)
        changes.append({'anchor': marker, 'reason': reason,
                        'insertedSha256': sha(text)})

    insert('/*\n  The former capped composition cut and detached all-components law are\n',
           fragment('composition_rule.lpfragment'), 'Strict default: existing capped functor action owner')
    insert('/*\n  The former whole post/left and pre/right strict-functoriality accumulation\n',
           fragment('whole_rules.lpfragment') + '\n' + fragment('projected_rules.lpfragment')
           + '\n' + fragment('conventional_lax_projection_readings.lpfragment')
           + '\n' + fragment('production_conventional_pre_reading.lpfragment')
           + '\n' + fragment('conventional_lax_rules.lpfragment'),
           'Strict functor action and conventional-lax pre/right action at the existing whole/projection owners')
    insert('// The public whole laxity candidate is now an object projection, not an\n',
           fragment('intrinsic_rule.lpfragment'),
           'Strict default: normalize the existing extracted functor compositor, without a new witness')
    insert('// Whole post/left ordinary laxity.',
           fragment('conventional_lax_intrinsic.lpfragment'),
           'Conventional lax default: the existing extracted pre/right cell is identity, without a wrapper or supplied comparison')

    insert('// Path categories internalize HoTT equality as a groupoidal category.',
           fragment('co_above2_category.lpfragment') + '\n' + fragment('co_at2_category.lpfragment'),
           'Corrected duality: required category-level R, O and dimension-two action')
    above = fragment('co_above2_functor.lpfragment')
    above = above[:above.index('// Whole action on Cartesian mapping categories.')]
    at = fragment('co_at2_functor.lpfragment')
    at = at[:at.index('// Whole Cartesian mapping-category action of dimension-one transpose.')]
    insert('// Terminal category and points-as-functors are needed to derive unary homs from',
           above + '\n' + at, 'Corrected duality: strict functor action, without unsupported transfor action')

    profile = fragment('cartesian_profile.lpfragment')
    early = profile[profile.index('injective symbol sf_cart_functor_cat'):profile.index('// Only the object classifier')]
    start = profile.index('constant symbol sf_cart_cat')
    early += profile[start:profile.index('// One whole inclusion', start)]
    names = {'sf_cart_functor_cat': 'Functor_cart_cat', 'sf_cart_cat': 'Cat_cart',
             'sf_cart_functor_include': 'Functor_cart_include'}

    def public(text):
        for old, new in names.items():
            text = text.replace(old, new)
        return text

    insert('/*\n  Internal path-category action.',
           '// Cartesian coefficient required by the selected Homd family type.\n' + public(early),
           'Homd coefficient: share strict functor objects while retaining public lax Hom(Cat)')

    carriers = ''
    relocated = []
    for marker in ('injective symbol StrictTransfor\n', 'injective symbol strict_transfor\n'):
        assert profiles.count(marker) == 1
        a = profiles.index(marker)
        b = profiles.index(';', a) + 1
        declaration = profiles[a:b]
        carriers += declaration + '\n\n'
        relocated.append({'symbol': marker.strip(), 'declarationSha256': sha(declaration)})
        profiles = profiles[:a] + '// Carrier/view relocated to the core owner.\n' + profiles[b:]
    late = profile[profile.index('// Only the object classifier'):profile.index('// The corresponding strict coefficient universe')]
    start = profile.index('// One whole inclusion')
    late += profile[start:profile.index('// A Cartesian evaluator', start)]
    insert('// Controlled Obj-inversion for transformation categories.',
           carriers, 'Relocate the existing strict-transfor carriers unchanged')
    hom_owner = 'rule Hom_cat (Functor_cat _ _) $F $G ↪ Transf_cat $F $G;'
    assert body.count(hom_owner) == 1
    body = body.replace(hom_owner, hom_owner + '\n\n' + public(late), 1)
    changes.append({'after': hom_owner,
                    'reason': 'Cartesian inclusion uses the original ordinary next-Hom projection',
                    'insertedSha256': sha(public(late))})

    # This initial full-source slice does not replace original Homd/Pi/Sigma
    # or reinterpret the old op/Op_transf. Those coupled consumers remain in
    # this file so source adaptation cannot pass by omitting them.
    out = root / 'tmp/probes/production_owner_migration'
    package = out / 'package'
    package.mkdir(parents=True, exist_ok=True)
    baseline_package = out / 'baseline_package'
    baseline_package.mkdir(exist_ok=True)
    assert not list(package.rglob('*.lpo')), 'Source-only candidate contains compiled objects'
    assert not list(baseline_package.rglob('*.lpo')), 'Source-only baseline contains compiled objects'
    (baseline_package / 'emdash3_2.lp').write_text(original)
    (baseline_package / 'emdash3_2_gray_profiles.lp').write_text(original_profiles)
    (baseline_package / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    (out / 'baseline.lp').write_text(original)
    (out / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    (package / 'emdash3_2.lp').write_text(body)
    (package / 'emdash3_2_gray_profiles.lp').write_text(profiles)
    (package / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    controls = (fragment('production_owner_controls.lpfragment') + '\n'
                + fragment('whole_controls.lpfragment') + '\n'
                + fragment('intrinsic_controls.lpfragment').replace('assertnot ', 'assert ')
                + '\n' + fragment('conventional_lax_controls.lpfragment')
                + '\n' + fragment('conventional_lax_projection_controls.lpfragment'))
    (package / 'owner_controls.lp').write_text('require open emdash.emdash3_2;\n\n' + controls)
    # Stage the pre-goal reviewer and exactly its imported source closure.
    # Only the explicit strict-default proof/control adaptations below and
    # the upstream core/profile owners override those original inputs.
    dependencies = {}
    visited = set()

    def stage(path):
        if path in visited:
            return
        visited.add(path)
        if path == 'emdash3_2.lp':
            text = body
        elif path == 'emdash3_2_gray_profiles.lp':
            text = profiles
        else:
            text = subprocess.check_output(
                ['git', 'show', PIN + ':emdash2/' + path], cwd=root, text=True)
            dependencies[path] = sha(text)
            baseline_target = baseline_package / path
            baseline_target.parent.mkdir(parents=True, exist_ok=True)
            baseline_target.write_text(text)
            if path == 'emdash3_2_one_cat_action_paths.lp':
                marker = 'symbol one_cat_composition_path '
                assert text.count(marker) == 1
                start = text.index(marker)
                begin = text.index('≔', start)
                end = text.index(';', begin) + 1
                old = text[begin:end]
                replacement = '''≔ @eq_refl (Hom B (@fapp0 A B F x) (@fapp0 A B F z))
    (@fapp1_fapp0 A B F x z (@comp_fapp0 A x y z g f));'''
                text = text[:begin] + replacement + text[end:]
                changes.append({'source': path, 'owner': 'one_cat_composition_path',
                                'reason': 'Existing lax-cell proof no longer joins after strict-default compositor normalization; preserve its statement and use strict computation',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(replacement)})
            if path == 'emdash3_2_represented_comma_families.lp':
                marker = 'protected symbol comma_basechange_sigma_map_composition '
                assert text.count(marker) == 1
                addition = fragment('production_comma_equivalence.lpfragment')
                text = text.replace(marker, addition + '\n' + marker, 1)
                changes.append({'source': path, 'before': marker,
                                'reason': 'Map the actual identity-compositor inverse evidence through original whiskering instead of imposing additional runtime projection laws',
                                'insertedSha256': sha(addition)})
                marker = 'protected symbol comma_basechange_observation_pre_points '
                assert text.count(marker) == 1
                start = text.index(marker)
                begin = text.index('≔', start)
                end = text.index(';', begin) + 1
                old = text[begin:end]
                post_points = text[start:end].replace('comma_basechange_observation_pre',
                                                      'comma_basechange_observation_post')
                post_points = post_points.replace('comma_basechange_observation_inner',
                                                  'comma_basechange_observation_outer')
                replacement = '''≔ λ z : τ (Obj (@Sigma_cat A (@Pullback_catd A K E F))),
  let pre : τ (@OmegaEquivAlong
      (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
      (@comma_basechange_observation_inner A K C F E P)
      (@comma_basechange_observation_middle A K C F E P)
      (@comma_basechange_observation_pre A K C F E P))
    ≔ @comma_strict_omega_map
      (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) (Product_cat K C))
      (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
      (@comp_cat_cov_func (@Sigma_cat A (@Pullback_catd A K E F))
        (Product_cat K C) C (@Product_projR_func K C))
      (@comma_basechange_sigma_basechange_right A K F E (@Const_catd K C) P)
      (@comma_basechange_sigma_basechange_middle A K F E (@Const_catd K C) P)
      (@comma_basechange_sigma_basechange_pre A K F E (@Const_catd K C) P)
      (@comma_pre_cell_omega (@Catd_cat K) Cat_cat
        (@comma_basechange_sigma_basechange_source A K F) (@Sigma_func K)
        (@sigma_pullback_total_transf A K F)
        E (@Const_catd K C) (@Const_catd K C) P (@id (@Catd_cat K) (@Const_catd K C))) in
  @comma_strict_omega_map
    (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C) C
    (@fapp0_func (@Sigma_cat A (@Pullback_catd A K E F)) C z)
    (@comma_basechange_observation_inner A K C F E P)
    (@comma_basechange_observation_middle A K C F E P)
    (@comma_basechange_observation_pre A K C F E P) pre;'''
                text = text[:begin] + replacement + '\n\n' + post_points + text[end:]
                changes.append({'source': path, 'owner': 'comma_basechange_observation_pre_points',
                                'reason': 'Map inverse evidence of the extracted default pre cell through the original projection, then evaluate at an arbitrary total object',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(replacement),
                                'postPointsSha256': sha(post_points)})
                marker = 'protected symbol comma_basechange_observation_pre_equiv '
                assert text.count(marker) == 1
                start = text.index(marker)
                end = text.index(';', text.index('≔', start)) + 1
                post_equiv = text[start:end].replace('comma_basechange_observation_pre',
                                                     'comma_basechange_observation_post')
                post_equiv = post_equiv.replace('comma_basechange_observation_inner',
                                                'comma_basechange_observation_outer')
                text = text[:end] + '\n\n' + post_equiv + text[end:]
                marker = 'protected symbol comma_basechange_observation_basechange_component '
                assert text.count(marker) == 1
                addition = fragment('production_comma_basechange_equivalence.lpfragment')
                text = text.replace(marker, addition + '\n' + marker, 1)
                changes.append({'source': path, 'owner': 'comma_basechange_observation_basechange_equiv',
                                'reason': 'The old second-step reflexivity no longer follows the newly mapped pre inverse; retain both comparison maps and compose their inverse evidence',
                                'postEquivSha256': sha(post_equiv), 'insertedSha256': sha(addition)})
                marker = 'protected symbol comma_basechange_gamma_target_link_equiv '
                assert text.count(marker) == 1
                start = text.index(marker)
                begin = text.index('≔', start)
                end = text.index(';', begin) + 1
                old = text[begin:end]
                replacement = '''≔ @one_cat_transf_pointwise_omega_along K Y Y1
    (@comma_section_gamma_target_observed_op K X Y J A D h)
    (@represented_comma_hom_action_target_func K X Y J A D h)
    (@comma_basechange_gamma_target_link K X Y J A D h Y1)
    (λ x : τ (Obj K), @comma_op_omega_along Y
      (@fapp0 (Op_cat K) (Op_cat Y) (@comma_basechange_gamma_target_raw0 K X Y J A D h) x)
      (@fapp0 (Op_cat K) (Op_cat Y) (@comma_basechange_gamma_target_raw2 K X Y J A D h) x)
      (@tapp0_fapp0 (Op_cat K) (Op_cat Y)
        (@comma_basechange_gamma_target_raw0 K X Y J A D h)
        (@comma_basechange_gamma_target_raw2 K X Y J A D h) x
        (@comma_basechange_gamma_target_raw_link K X Y J A D h Y1))
      (@comma_strict_omega_map (Functor_cat (Op_cat K) (Op_cat Y)) (Op_cat Y)
        (@fapp0_func (Op_cat K) (Op_cat Y) x)
        (@comma_basechange_gamma_target_raw0 K X Y J A D h)
        (@comma_basechange_gamma_target_raw2 K X Y J A D h)
        (@comma_basechange_gamma_target_raw_link K X Y J A D h Y1)
        (@comma_basechange_gamma_target_raw_link_equiv K X Y J A D h Y1)));'''
                text = text[:begin] + replacement + text[end:]
                addition = fragment('production_comma_target_equivalence.lpfragment')
                text = text.replace(marker, addition + '\n' + marker, 1)
                changes.append({'source': path, 'owner': 'comma_basechange_gamma_target_link_equiv',
                                'reason': 'Preserve the original comparison and construct its inverse evidence before evaluating components',
                                'insertedSha256': sha(addition),
                                'oldBodySha256': sha(old), 'newBodySha256': sha(replacement)})
            if path == 'examples/gray_profiles.lp':
                old = '''assertnot [A B : Cat]
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y)) ⊢
  @strict_functor_compositor_lhs
    A B (@example_unprofiled_functor A B) X Y Z g f
  ≡ @strict_functor_compositor_rhs
      A B (@example_unprofiled_functor A B) X Y Z g f;'''
                assert text.count(old) == 1
                replacement = old.replace('assertnot ', 'assert ', 1)
                text = text.replace(old, replacement, 1)
                text = text.replace('// Rigid ambient negative control, deliberately outside StrictFunctor.',
                                    '// Ambient functor: the strict default no longer requires a wrapper.')
                text = text.replace('// Composition is selected only by the stable evidence-bearing view.',
                                    '// The legacy stable view still computes during wrapper migration.')
                changes.append({'source': path, 'owner': 'unprofiled compositor endpoint comparison',
                                'reason': 'The default functor now preserves composition; retain all unrelated negative controls',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(replacement)})
            target = package / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)
        for command in re.findall(r'(?m)^\s*require(?:\s+open)?\s+([^;]+);', text):
            for module in command.split():
                assert re.fullmatch(r'emdash(?:\.[A-Za-z0-9_]+)+', module), module
                stage(module.removeprefix('emdash.').replace('.', '/') + '.lp')

    stage('examples/gray_profiles.lp')
    delta = difflib.SequenceMatcher(None, original.splitlines(keepends=True),
                                   body.splitlines(keepends=True), autojunk=False).get_opcodes()
    assert all(kind in ('equal', 'insert') for kind, *_ in delta)
    inputs[str(Path(__file__).resolve().relative_to(root))] = sha(Path(__file__).read_text())
    manifest = {
        'status': 'in-progress full-source upstream migration; not final foundation qualification',
        'sourcePin': PIN, 'originalCoreSha256': CORE_SHA,
        'originalCoreLines': len(original.splitlines()), 'candidateCoreLines': len(body.splitlines()),
        'originalDownstreamSectionsRetained': True,
        'originalCoreLineOrderVerified': True,
        'originalDependencyInputs': dependencies,
        'changes': changes, 'relocatedDeclarations': relocated,
        'authoringInputs': inputs,
        'outputs': {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in [out / 'baseline.lp', package / 'emdash3_2.lp',
                              package / 'emdash3_2_gray_profiles.lp', package / 'owner_controls.lp',
                              baseline_package / 'emdash3_2.lp', baseline_package / 'emdash3_2_gray_profiles.lp']
                    + [package / path for path in dependencies]},
        'stillRequired': ['Coupled original op/Op_transf correction for the conventional-lax default',
                          'Original family classifiers and Q/Homd/Sigma/Pi adaptation',
                          'Existing evaluation/closure consumers under their required profiles',
                          'Downstream qualification and retirement of redundant strict wrappers'],
        'excluded': ['Auxiliary Sigma fibre-composition audit owner',
                     'New joint Cartesian evaluator', 'Optional normalization redesign'],
    }
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted full pre-goal baseline and upstream owner migration; no original tail omitted.')


if __name__ == '__main__':
    main()
