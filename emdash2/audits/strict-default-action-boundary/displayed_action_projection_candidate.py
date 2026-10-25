"""Replay unadopted displayed-action repairs and separately recorded alternatives.

The default candidate keeps only the terminal-action and Eval-transport repairs.
The profiles/fold/vertical variants are experiments, not production choices.
Generation is not qualification; full original reviewer migration remains open.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import foundation_reviewer_candidate as parent

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def fragment(name, blank=False):
    return (HERE / name).read_text().rstrip() + ('\n\n' if blank else '\n')


def eval_transport(text):
    spec = json.loads((HERE / 'displayed_action_eval_transport.json').read_text())
    start = text.index("/* Evaluation's projected hom action, in both ordinary and pointwise-opposite")
    end = text.index('/* Product pairing exposes its two displayed hom actions', start)
    block = text[start:end]
    assert block.count(spec['old']) == 2
    block = block.replace(spec['old'], spec['new'])
    block = block.replace('   presentations. The whole result remains the existing mixed Eval action. */',
        '   presentations. Constant-domain transport retains the actual Cartesian Hom\n'
        '   action at id_I, matching the generic strict-transfor projection order. */')
    return text[:start] + block + text[end:]


def eval_reviewer(text):
    start = text.index('// Eval itself retains the whole mixed action')
    end = text.index('// The two new structural whole joins', start)
    block = text[start:end]
    old = '(@comp_cat_fapp0 I (Fibre_cat E x) (Fibre_cat E y)\n        (@catd_transport_func K E x y p) U)'
    new = '(@Hom_fapp0 Cat_cart I I (Fibre_cat E x) (Fibre_cat E y)\n        (@id_func I) (@catd_transport_func K E x y p) U)'
    assert block.count(old) == 2
    block = block.replace(old, new)
    block = block.replace('(eta : τ (Transf (@comp_cat_fapp0 I (Fibre_cat E x) (Fibre_cat E y)\n      (@catd_transport_func K E x y p) U) V))',
        '(eta : τ (@StrictTransfor I (Fibre_cat E y)\n'
        '      (@Hom_fapp0 Cat_cart I I (Fibre_cat E x) (Fibre_cat E y)\n'
        '        (@id_func I) (@catd_transport_func K E x y p) U) V))')
    block = block.replace('V i j eta q;', 'V i j (@strict_transfor _ _ _ _ eta) q;')
    return text[:start] + block + text[end:]


def terminal_normality_reviewer(text):
    count = 0
    for match in reversed(list(re.finditer(r'(?m)^assertnot\b.*?;', text, re.S))):
        if 'prof_terminal_test_wrong_normal' in match.group():
            text = text[:match.start()] + match.group().replace('assertnot', 'assert', 1) + text[match.end():]
            count += 1
    assert count == 2
    text = text.replace('// A reflexive path at the unnormalized terminal action cannot inhabit the\n// normality slot of the explicit whole displayed normalizer.',
        '// Default strict functors compute the canonical terminal identity action.\n'
        '// Its reflexive witness therefore inhabits the existing normality slot.\n'
        '// The independently supplied whole comparison and chosen path data remain.')
    return text + '\n' + fragment('displayed_action_normality_negative.lpfragment')


def emit(out, variant):
    requested_variant = variant
    refined = variant in ("terminal-owner", "classified-intrinsic", "classified-vertical", "telescope")
    if refined:
        variant = "constant-fold"
    parent.emit(out)
    core = out / 'emdash3_2.lp'
    prior = core.read_text()
    evidence = json.loads((HERE / 'foundation_reviewer_candidate_evidence.json').read_text())
    assert hashlib.sha256(prior.encode()).hexdigest() == evidence['candidateCoreSha256']
    text = prior
    anchor = '// Fixed-base layer: functorial section-category constructor at a fixed base.'
    assert text.count(anchor) == 1
    text = text.replace(anchor, fragment('displayed_action_terminal_identity.lpfragment', True) + anchor, 1)
    text = eval_transport(text)
    for name in ('ordinary_displayed_diagnostic.lp', 'examples/displayed_evaluation.lp'):
        path = out / name
        path.write_text(eval_reviewer(path.read_text()))
    controls = {
        'terminal_identity_action_review.lp': 'displayed_action_identity_controls.lpfragment',
        'corrected_op_eval_review.lp': 'displayed_action_op_eval_controls.lpfragment',
    }
    if variant in ('terminal-source', 'terminal-literal', 'constant-source', 'constant-fold'):
        anchor = '// Terminal composition is the unique terminal object/arrow.'
        assert text.count(anchor) == 1
        text = text.replace(anchor, fragment('displayed_action_source_terminal_literal.lpfragment' if variant == 'terminal-literal' else 'displayed_action_source_terminal_identity.lpfragment', True) + anchor, 1)
        controls['terminal_source_identity_review.lp'] = ('displayed_action_source_literal_controls.lpfragment' if variant == 'terminal-literal' else 'displayed_action_source_identity_controls.lpfragment')
        path = out / 'examples/prof_reindex_terminal_normalization.lp'
        path.write_text(terminal_normality_reviewer(path.read_text()))
        (out / 'strict_terminal_normality_review.lp').write_text('require open emdash.terminal_source_identity_review;\nrequire open emdash.examples.prof_reindex_terminal_normalization;\n')
    if variant in ('profiles', 'fold', 'vertical', 'constant-source', 'constant-fold'):
        for name, source in [('Product_pair_funcd', 'displayed_action_pair_cart_profile.lpfragment'),
                             ('Terminal_funcd', 'displayed_action_terminal_cart_profile.lpfragment')]:
            start = text.index('injective symbol ' + name)
            end = text.index(';', start) + 1
            text = text[:end] + '\n\n' + fragment(source, True) + text[end:]
        anchor = '// Fixed-base layer: functorial section-category constructor at a fixed base.'
        text = text.replace(anchor, fragment('displayed_action_constant_section_actions.lpfragment', True) + anchor, 1)
        controls.update({
            'structural_cart_profiles_review.lp': 'displayed_action_profile_controls.lpfragment',
            'structural_op_profiles_review.lp': 'displayed_action_op_profile_controls.lpfragment',
            'structural_op_more_review.lp': 'displayed_action_op_more_controls.lpfragment',
            'op_cart_comp_path_review.lp': 'displayed_action_op_comp_path.lpfragment',
        })
    if variant in ('constant-source', 'constant-fold'):
        anchor = '// Canonical coefficient-family view of an ordinary constant functor.'
        assert text.count(anchor) == 1
        text = text.replace(anchor, fragment('displayed_action_constant_source.lpfragment', True) + anchor, 1)
        controls['constant_source_projection_review.lp'] = 'displayed_action_constant_source_controls.lpfragment'
    if variant in ('fold', 'vertical', 'constant-fold'):
        start = text.index('rule @strict_transfor $A $B $F $H\n')
        end = text.index(';', start) + 1
        text = text[:start] + fragment('displayed_action_strict_composite_fold.lpfragment').rstrip() + text[end:]
        anchor = '// Vertical composite components compose pointwise.'
        assert text.count(anchor) == 1
        text = text.replace(anchor, fragment('displayed_action_strict_composite_component.lpfragment', True) + anchor, 1)
    if variant == 'vertical':
        anchor = '/* API-04V RULE-OFF CONTROL:'
        assert text.count(anchor) == 1
        text = text.replace(anchor, fragment('displayed_action_cart_vertical.lpfragment', True) + anchor, 1)
    if refined:
        start = text.index('injective symbol Terminal_cart_funcd')
        end = text.index(';', start) + 1
        text = text[:end] + '\n\n' + fragment('displayed_action_terminal_cart_identity.lpfragment') + text[end:]
    if requested_variant in ('classified-intrinsic', 'classified-vertical', 'telescope'):
        anchor = '// Unit at the existing projection heads'
        assert text.count(anchor) == 1
        text = text.replace(anchor, fragment('displayed_action_classified_intrinsic.lpfragment', True) + anchor, 1)
        (out / 'examples/displayed_evaluation.lp').write_text(fragment('displayed_action_complete_reviewer.lpfragment'))
        controls['classified_intrinsic_overlap_review.lp'] = 'displayed_action_classified_overlap_controls.lpfragment'
    if requested_variant in ('classified-vertical', 'telescope'):
        anchor = '/* API-04V RULE-OFF CONTROL:'
        assert text.count(anchor) == 1
        text = text.replace(anchor, fragment('displayed_action_cart_vertical.lpfragment') + '\n' + anchor, 1)
    if requested_variant == 'telescope':
        retired = list(re.finditer(r'/\* API-04T:.*?\*/', text, re.S))
        assert len(retired) == 2
        for match in reversed(retired):
            rule = re.search(r'(?m)^rule @comp_fapp0.*?;', match.group(), re.S).group()
            start = text.index('// Named identity-family telescope composition remains intrinsic.', match.end())
            end = text.index(';', start) + 1
            assert not text[match.end():start].strip()
            replacement = '// Default strict functors restore composition for this actual telescope.\n// This general instance subsumes the former identity-functor-only clause.\n' + rule + '\n'
            text = text[:match.start()] + replacement + text[end:]
        anchor = '// Identity of the ordinary telescope observation.'
        assert text.count(anchor) == 1
        text = text.replace(anchor, fragment('displayed_action_telescope_ordinary.lpfragment', True) + anchor, 1)
        controls['terminal_hom_warning_review.lp'] = 'displayed_action_terminal_hom_controls.lpfragment'
        (out / 'telescope_and_displayed_review.lp').write_text('require open emdash.examples.action_profile_telescope_profile_paths;\nrequire open emdash.classified_intrinsic_overlap_review;\n')
        (out / 'displayed_actions_complete_review.lp').write_text('require open emdash.telescope_and_displayed_review;\nrequire open emdash.terminal_hom_warning_review;\nrequire open emdash.examples.prof_reindex_terminal_normalization;\nrequire open emdash.terminal_source_identity_review;\n')
    core.write_text(text)
    for target, source in controls.items():
        (out / target).write_text(fragment(source))
    (out / 'minimal_displayed_actions_review.lp').write_text('require open emdash.terminal_identity_action_review;\nrequire open emdash.corrected_op_eval_review;\nrequire open emdash.whole_contravariant_review;\n')
    manifest = out.parent / (out.name + '_candidate_manifest.json')
    old_manifest = json.loads(manifest.read_text())
    manifest.write_text(json.dumps({
        'status': 'unadopted; generation is not qualification', 'variant': requested_variant,
        'sourcePin': parent.INPUTS['sourcePin'],
        'parentVerificationSha256': parent.INPUTS['parentVerificationSha256'],
        'parentCandidateCoreSha256': evidence['candidateCoreSha256'],
        'parentEmittedCoreSha256': old_manifest['outputs']['emdash3_2.lp'],
        'outputs': {str(p.relative_to(out)): hashlib.sha256(p.read_bytes()).hexdigest() for p in out.rglob('*.lp')},
    }, indent=2) + '\n')
    print(json.dumps({'out': str(out), 'variant': requested_variant, 'status': 'unadopted'}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--variant', choices=['minimal', 'terminal-source', 'terminal-literal', 'profiles', 'fold', 'vertical', 'constant-source', 'constant-fold', 'terminal-owner', 'classified-intrinsic', 'classified-vertical', 'telescope'], default='minimal')
    args = parser.parse_args()
    emit(args.out.resolve(), args.variant)
