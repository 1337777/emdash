#!/usr/bin/env python3
"""Finite counit/lift-direction control, not a full omega/coend model.

A is terminal, B is the walking arrow, and F:A->B picks 0. The coend over A
is just a product, so the comparison can be computed without a quotient.
"""
import json


def hom(x, y):
    return {(x, y)} if x <= y else set()


def composite(first, second):
    assert first[1] == second[0]
    result = (first[0], second[1])
    assert result in hom(*result)
    return result


def main():
    rows = []
    naturality_checks = 0
    for b in (0, 1):
        for c in (0, 1):
            source = {(beta, gamma) for beta in hom(b, 0) for gamma in hom(0, c)}
            target = hom(b, c)
            image = {pair: composite(*pair) for pair in source}
            assert set(image.values()) <= target
            for b0 in (0, 1):
                for c1 in (0, 1):
                    for left in hom(b0, b):
                        for right in hom(c, c1):
                            for beta, gamma in source:
                                transported = (composite(left, beta), composite(gamma, right))
                                assert composite(*transported) == composite(composite(left, image[(beta, gamma)]), right)
                                naturality_checks += 1
            rows.append({'sourceObject': b, 'targetObject': c,
                         'tensorFibre': len(source), 'unitFibre': len(target),
                         'surjective': set(image.values()) == target})
    missing = next(r for r in rows if r['sourceObject'] == r['targetObject'] == 1)
    assert missing['tensorFibre'] == 0 and missing['unitFibre'] == 1
    assert not missing['surjective']

    # Realize the same counit as the q-comparison of a strict family map U:
    # E=(A --F--> B), D=(B --id--> B), U0=F, U1=id. The original square
    # commutes strictly. Its represented mate is iota(F) kappa(F) -> id_B.
    F = {'*': 0}
    E_q = F
    D_q = {0: 0, 1: 1}
    U0 = F
    U1 = {0: 0, 1: 1}
    assert {a: D_q[U0[a]] for a in F} == {a: U1[E_q[a]] for a in F}
    assert naturality_checks > 0
    print(json.dumps({
        'status': 'finite semantic control passed',
        'functor': 'Terminal -> walking arrow, selecting 0',
        'counit': 'iota(F) o kappa(F) -> Unit_B',
        'fibres': rows,
        'nonemptyNaturalityChecks': naturality_checks,
        'strictInputSquare': 'id_B o F = id_B o F',
        'liftComparisonAt11': 'Empty -> Terminal',
        'inverseExistsAt11': False,
        'scope': 'Demonstrates direction and noninvertibility; does not qualify the full omega coefficient.'
    }, indent=2))


if __name__ == '__main__':
    main()
