#!/usr/bin/env python3
"""Finite direction/noninvertibility control for the represented unit.

A is the walking arrow, B is terminal, F:A->B is strict. The tensor over
B is a product, so no general coend implementation is assumed by this test.
"""
import json


def hom(a, b):
    return {(a, b)} if a <= b else set()


def compose(f, g):
    assert f[1] == g[0]
    return (f[0], g[1])


def image(f):
    assert f in hom(*f)
    return ('*', '*')


def unit(f):
    # The shaped tensor introduction may split at the source. Both factors
    # are the original F Hom action, including its identity component.
    return (image((f[0], f[0])), image(f))


def main():
    checks = 0
    fibres = []
    for a in (0, 1):
        for b in (0, 1):
            source = hom(a, b)
            target = {(('*', '*'), ('*', '*'))}
            values = {f: unit(f) for f in source}
            assert set(values.values()) <= target
            for a0 in (0, 1):
                for b1 in (0, 1):
                    for left in hom(a0, a):
                        for right in hom(b, b1):
                            for f in source:
                                transported = compose(compose(left, f), right)
                                assert image(transported) == compose(compose(image(left), image(f)), image(right))
                                actual = (compose(image(left), values[f][0]),
                                          compose(values[f][1], image(right)))
                                assert unit(transported) == actual
                                checks += 1
            fibres.append({'negativeEndpoint': a, 'positiveEndpoint': b,
                           'unitHomSize': len(source), 'representedTensorSize': len(target),
                           'surjective': set(values.values()) == target})
    missing = next(x for x in fibres if x['negativeEndpoint'] == 1 and x['positiveEndpoint'] == 0)
    assert missing['unitHomSize'] == 0 and missing['representedTensorSize'] == 1
    assert not missing['surjective'] and checks > 0
    print(json.dumps({'status': 'finite unit control passed',
                      'functor': 'walking arrow -> Terminal',
                      'unit': 'id_Q(A) -> kappa(F) o iota(F)',
                      'legacyFibre': 'Hom_A(a,b) -> Hom_B(F(a),F(b))',
                      'fibres': fibres, 'naturalityChecks': checks,
                      'inverseExistsAt10': False,
                      'scope': 'finite semantic direction/noncollapse; not omega coherence or native tensor evaluation'}, indent=2))


if __name__ == '__main__':
    main()
