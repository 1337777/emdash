#!/usr/bin/env python3
"""NON-LIBRARY Cartesian action projection qualification, retaining product Prof."""
import hashlib
import json
from pathlib import Path
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'q_unit_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_q_unit/emdash3_2.lp'
    prior = json.loads((audit / 'q_unit_verification.json').read_text())
    source = previous.read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']
    for anchor, name in (
        ('// Runtime functoriality of the tele-level postcomposition stable head.', 'cart_action_tele.lpfragment'),
        ('// General two-sided product map.', 'cart_action_product.lpfragment'),
        ('// Vertical action of profunctor duality, inherited from `Op_prof_func`.', 'cart_action_prof_swap.lpfragment'),
        ('// Readable second Path action: a function equality induces a path-valued', 'cart_action_product_view.lpfragment'),
    ):
        assert source.count(anchor) == 1, anchor
        source = source.replace(anchor, (audit / name).read_text() + '\n' + anchor)
    identity_categories = '(@id (Functor_cart_cat $X $Y) $F)\n        (@id (Functor_cart_cat $Y $Z) $G)'
    assert source.count(identity_categories) == 1
    source = source.replace(identity_categories, '(@id _ $F)\n        (@id _ $G)')
    strict_identity = 'rule @strict_transfor $A $B $F $F (@id (Functor_cart_cat $A $B) $F)'
    assert source.count(strict_identity) == 1
    source = source.replace(strict_identity, 'rule @strict_transfor $A $B $F $F (@id _ $F)')
    ambient_identities = (
        'rule @tapp0_fapp0 $A $B _ _ $Y (@id (Functor_cat $A $B) $F)',
        'rule @tapp1_func $A $B _ _ $X $Y (@id (Functor_cat $A $B) $F)',
        'rule @tapp1_fapp0 $A $B _ _ $X $Y (@id (Functor_cat $A $B) $F) $p',
    )
    for old in ambient_identities:
        assert source.count(old) == 1, old
        source = source.replace(old, old.replace('(Functor_cat $A $B)', '_').replace('$A $B _ _', '$A $B $F $F'))
    marker = '// 7d. Adjunctions and opposite adjunctions'
    raw_views = (audit / 'cart_action_raw_views.lpfragment').read_text()
    inverse_rules = (audit / 'cart_action_inverse.lpfragment').read_text()
    reverse_rules = (audit / 'cart_action_inverse_reverse.lpfragment').read_text()
    anchor = '// Whole operations, followed by both separately projected application orders.'
    assert source.count(anchor) == 1
    source = source.replace(anchor, raw_views + '\n' + inverse_rules + '\n' + reverse_rules + '\n' + anchor)
    anchor = 'rule @tapp1_fapp0 $A $B $F $G $X $X $ϵ (@id $A $X)'
    assert source.count(anchor) == 1
    i = source.index(';', source.index(anchor)) + 1
    source = source[:i] + '\n' + (audit / 'cart_action_pair_projection.lpfragment').read_text() + source[i:]
    controls = (audit / 'cart_action_controls.lpfragment').read_text()
    inverse_controls = (audit / 'cart_action_inverse_controls.lpfragment').read_text()
    source = source.replace(marker, controls + '\n' + inverse_controls + '\n' + marker)
    prefix = source[:source.index(marker)]
    inverse = (audit / 'cartesian_inverse_action_boundary.lpfragment').read_text()
    output = root / 'tmp/probes/strict_default_cart_action'
    output.mkdir(parents=True, exist_ok=True)
    targets = {
        'emdash3_2.lp': source,
        'owner_prefix.lp': prefix,
        'inverse_boundary.lp': prefix + '\n' + inverse,
        'q_prefix.lp': source[:source.index('// 14. Section action over dependent homs')],
    }
    reverse = '''
// Positive obligation: the independently expanded reverse transformation action.
assert [A B C : Cat] [F G : τ (Functor A (Functor_cart_cat B C))]
  (alpha : τ (Hom (Functor_cart_cat A (Functor_cart_cat B C)) F G)) ⊢
  @fapp1_fapp0 _ _ (@curry_func_func A B C)
    (@uncurry_func A B C F) (@uncurry_func A B C G)
    (@fapp1_fapp0 _ _ (@uncurry_func_func A B C) F G alpha)
  ≡ alpha;
'''
    targets['reverse_boundary.lp'] = prefix + '\n' + reverse
    q_controls = (audit / 'cart_action_q_controls.lpfragment').read_text()
    targets['q_bridge_actions.lp'] = targets['q_prefix.lp'] + '\n' + q_controls
    targets['no_prof_swap.lp'] = targets['q_bridge_actions.lp'].replace((audit / 'cart_action_prof_swap.lpfragment').read_text(), '')
    targets['no_reverse_inverse.lp'] = (prefix + '\n' + reverse).replace(reverse_rules, '')
    for name in ('tele', 'product', 'product_view', 'pair_projection'):
        targets['no_' + name + '.lp'] = prefix.replace((audit / ('cart_action_' + name + '.lpfragment')).read_text(), '')
    split = inverse_rules.index('// Completion of the measured higher-action')
    targets['no_inverse_action.lp'] = prefix.replace(inverse_rules[split:], '')
    targets['no_raw_beta.lp'] = prefix.replace(raw_views, '')
    targets['literal_strict_identity.lp'] = prefix.replace('rule @strict_transfor $A $B $F $F (@id _ $F)', strict_identity)
    literal_ambient = prefix
    for old in ambient_identities:
        literal_ambient = literal_ambient.replace(old.replace('(Functor_cat $A $B)', '_').replace('$A $B _ _', '$A $B $F $F'), old)
    targets['literal_ambient_identity.lp'] = literal_ambient
    targets['literal_identity_categories.lp'] = prefix.replace('(@id _ $F)\n        (@id _ $G)', identity_categories)
    # Measured inferred-slot control: remove only the outer data endpoints
    # of the forward action join, retaining its actual identity/data pattern.
    head = 'rule @comp_prod_fapp1_fapp0 Cat_cat _ _ _'
    h = inverse_rules.index(head) + len(head)
    start = h
    for _ in range(2):
        while inverse_rules[h].isspace(): h += 1
        assert inverse_rules[h] == '('
        depth = 0
        while True:
            depth += (inverse_rules[h] == '(') - (inverse_rules[h] == ')')
            h += 1
            if depth == 0: break
    inferred = inverse_rules[:start] + ' _ _' + inverse_rules[h:]
    targets['without_inverse_endpoint_data.lp'] = prefix.replace(inverse_rules, inferred)
    mate = (audit / 'q_lift_mate.lpfragment').read_text()
    a = '// The y-section is the existing transformation category in the coefficient.'
    assert source.count(a) == 1
    mate_source = source.replace(a, mate + '\n' + a)
    targets['mate_boundary.lp'] = mate_source[:mate_source.index('// 14. Section action over dependent homs')]
    for name, text in targets.items():
        (output / name).write_text(text)
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    names = ('cart_action_migration.py', 'cart_action_tele.lpfragment', 'cart_action_product.lpfragment', 'cart_action_controls.lpfragment', 'cart_action_product_view.lpfragment', 'cart_action_pair_projection.lpfragment', 'cart_action_inverse.lpfragment', 'cart_action_inverse_controls.lpfragment', 'cart_action_inverse_reverse.lpfragment', 'cart_action_prof_swap.lpfragment', 'cart_action_q_controls.lpfragment', 'cart_action_raw_views.lpfragment')
    manifest = {
        'status': 'non-library Cartesian action and presentation inverse candidate; Q/lift and production integration unqualified',
        'inputSha256': prior['outputs']['emdash3_2.lp'],
        'authoringInputs': {str((audit / p).relative_to(root)): hashlib.sha256((audit / p).read_bytes()).hexdigest() for p in names},
        'outputs': {p: hashlib.sha256((output / p).read_bytes()).hexdigest() for p in (*targets, 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted Cartesian projection-owner copy; product Prof preserved.')


if __name__ == '__main__':
    main()
