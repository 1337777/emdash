"""Apply the measured four-reviewer continuation to an unadopted candidate.

The package must be an unchanged telescope candidate at the recorded owner
positions. This changes no qualified production-emitter package. Generation
is not qualification; use the owning source checks and complete reviewers.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
INPUTS = json.loads((HERE / 'foundation_reviewer_followup_inputs.json').read_text())


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def migrate(name, text):
    assert sha(text) == INPUTS['files'][name]['sourceSha256'], name
    if name == 'displayed_identity_presentations':
        text = text.replace('Cat_cat', 'Cat_cart')
    elif name == 'prof_curry_hom_views':
        text = text.replace('Cat_cat', 'Cat_cart')
        text = text.replace('(@Catd_cat B)', '(Functor_cart_cat B Cat_cart)')
        text = text.replace('(@Catd_cat A)', '(Functor_cart_cat A Cat_cart)')
        text = text.replace('// catalog-area: Native Hom profunctor curry comparisons',
            '// catalog-area: Native Hom profunctor curry comparisons\n'
            '// Native Cartesian curry and Hom are compared before their ordinary inclusions.')
    elif name == 'products_eval_curry':
        text = text.replace('Functor_cat', 'Functor_cart_cat').replace('Cat_cat', 'Cat_cart')
        old = '  ≡ @fapp0_func A B x;'
        assert text.count(old) == 1
        text = text.replace(old,
            '  ≡ @comp_cat_fapp0 (Functor_cart_cat A B) (Functor_cat A B) B\n'
            '      (@fapp0_func A B x) (Functor_cart_include A B);')
        text = text.replace('ordinary functional-programming layer', 'Cartesian functional-programming layer')
    elif name == 'action_profile_telescope_profile_controls':
        matches = list(re.finditer(r'(?m)^assert(?:not)?\b.*?;', text, re.S))
        assert len(matches) == 14
        for index in reversed([2, 3, 8, 9]):
            match = matches[index - 1]
            assert match.group().startswith('assertnot') and '@eq_refl' in match.group()
            text = text[:match.start()] + match.group().replace('assertnot', 'assert', 1) + text[match.end():]
        text = text.replace('/* Legacy/modern distinction, named identity computation and explicit\n'
            '   telescope admission. These controls introduce no computation rule. */',
            '/* Default strict telescope composition, named identity computation, and\n'
            '   exact profile typing. The four former noncomputation checks are positive\n'
            '   under strict defaults; neither wrong-profile negative is removed. */')
    else:
        raise ValueError(name)
    assert sha(text) == INPUTS['files'][name]['candidateSha256'], name
    return text


def apply(package):
    core = package / 'emdash3_2.lp'
    text = core.read_text()
    assert sha(text) == INPUTS['parentCoreSha256'], 'Candidate core drift'
    updates = {}
    for name in INPUTS['files']:
        path = package / 'examples' / (name + '.lp')
        updates[path] = migrate(name, path.read_text())
    start = text.index("// Proof-time comparison of curry's semantic telescope with the native Hom family.")
    end = text.index('// Right-representable hom profunctor', start)
    assert sha(text[start:end]) == INPUTS['oldCurryBlockSha256']
    updates[core] = text[:start] + (HERE / 'foundation_reviewer_curry_comparison.lpfragment').read_text() + '\n' + text[end:]
    # Validate every input before the first mutation; apply only to an idle probe.
    for path, body in updates.items():
        path.write_text(body)
    target = package / 'reviewer_annotation_continuation.lp'
    target.write_text('require open emdash.examples.action_profile_telescope_profile_controls;\n'
        'require open emdash.examples.displayed_identity_presentations;\n'
        'require open emdash.examples.products_eval_curry;\n'
        'require open emdash.examples.prof_curry_hom_views;\n')
    return {str(p.relative_to(package)): sha(p.read_text()) for p in [*updates, target]}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps({'status': 'unadopted candidate', 'outputs': apply(args.package.resolve())}, indent=2))
