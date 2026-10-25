"""Replay the four complete family reviewers on the pinned, idle candidate.

This preserves the existing semantic owners and replaces one reducible
Op-reindexing comparison pattern. It does not promote production sources.
"""
from pathlib import Path
import argparse
import hashlib
import json

HERE = Path(__file__).resolve().parent
INPUTS = json.loads((HERE / 'foundation_family_reviewer_inputs.json').read_text())


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def replace_once(text, old, new):
    assert text.count(old) == 1, old
    return text.replace(old, new, 1)


def migrate(name, text):
    assert sha(text) == INPUTS['files'][name]['sourceSha256'], name
    if name == 'higher_sieve_classifier':
        text = text.replace('Cat_cat', 'Cat_cart')
        text = replace_once(text,
            '// Both presentations compare to one stable Catd category.',
            '// The varying classifier has Cartesian diagram maps; ordinary presheaves\n'
            '// retain their ambient lax-map category and the actual whole inclusion.')
        text = replace_once(text,
            '      (@HigherSieve_cat K U)\n      (@Catd_cat (@Into_restr_cat K U)));',
            '      (@HigherSieve_cat K U)\n      (Functor_cart_cat (@Into_restr_cat K U) Cat_cart));')
        text = replace_once(text,
            '// Lambdapi does not chain those two experimental unification steps.',
            '// These categories have different mapping profiles, despite sharing objects.')
        text += ('\n// The existing whole inclusion supplies the ordinary presheaf view.\n'
            'assert [K : Cat] (U : τ (Obj K)) ⊢\n'
            '  @higher_sieve_include_func K U\n'
            '  : τ (Functor (@HigherSieve_cat K U) (@Psh_cat (@Slice_cat K U)));\n')
    elif name == 'join_cross_computation':
        for old in ['@tapp1_fapp0 (Product_cat (Op_cat A) A) Cat_cat',
                    '@tapp1_fapp0 A Cat_cat',
                    '@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cat',
                    '@fapp0 (Product_cat (Op_cat B) C) Cat_cat R']:
            text = replace_once(text, old, old.replace('Cat_cat', 'Cat_cart'))
        assert text.count('@hom_int ') == 2
        text = text.replace('@hom_int ', '@hom_int_view ')
    elif name == 'sigma_section_projection_views':
        end = text.index('// Sufficient section congruence')
        first, rest = text[:end], text[end:]
        first = first.replace('(Catd A)', '(Catd (CoAt2_cat A))').replace('Cat_cat', 'Cat_cart')
        first = first.replace('@Pullback_catd A C', '@Pullback_catd (CoAt2_cat A) (CoAt2_cat C)')
        first = first.replace('(@comp_cat_fapp0 A B C F G)',
            '(@CoAt2_func A C (@comp_cat_fapp0 A B C F G))')
        text = first + rest
    elif name == 'sigma_total':
        assert text.count('K Cat_cat E D') == 2
        text = text.replace('K Cat_cat E D', 'K Cat_cart E D')
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
    old = INPUTS['oldComparison']
    replacement = (HERE / 'foundation_family_op_reindex.lpfragment').read_text() + '\n'
    updates[core] = replace_once(text, old, replacement)
    assert sha(updates[core]) == INPUTS['candidateCoreSha256']
    target = package / 'reviewer_family_continuation.lp'
    updates[target] = ''.join('require open emdash.examples.' + n + ';\n' for n in INPUTS['files'])
    # Validate all source pins before mutating this idle probe package.
    for path, body in updates.items():
        path.write_text(body)
    return {str(p.relative_to(package)): sha(body) for p, body in updates.items()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps({'status': 'unadopted family-reviewer candidate',
        'outputs': apply(args.package.resolve())}, indent=2))
