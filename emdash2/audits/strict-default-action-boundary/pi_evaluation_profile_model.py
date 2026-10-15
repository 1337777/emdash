#!/usr/bin/env python3
"""Finite strict 2-category test of the old k-first Pi evaluator.

The nonidentity 1-cells form a square. Its two length-two paths have one
noninvertible 2-cell L => R. This is a semantic counterexample for an
extra evaluation profile, not a model or consistency certificate of Q.
"""
from itertools import product
import json


def main():
    vertices = (0, 1, 2, 3)
    edges = ((0, 1), (0, 2), (1, 3), (2, 3))
    left, right = (0, 2, 3), (0, 1, 3)
    paths = tuple((v,) for v in vertices) + edges + (left, right)

    def compose(g, f):
        assert f[-1] == g[0]
        return f + g[1:]

    def cell(f, g):
        return f == g or (f, g) == (left, right)

    # Validate identities, composition, associativity, and the locally
    # posetal 2-cell order, including horizontal functoriality.
    for f in paths:
        assert compose((f[-1],), f) == f == compose(f, (f[0],))
    for f, g in product(paths, repeat=2):
        if f[-1] == g[0]:
            assert compose(g, f) in paths
    for f, g, h in product(paths, repeat=3):
        if f[-1] == g[0] and g[-1] == h[0]:
            assert compose(h, compose(g, f)) == compose(compose(h, g), f)
        if cell(f, g) and cell(g, h):
            assert cell(f, h)
    cells = [(f, g) for f, g in product(paths, repeat=2) if cell(f, g)]
    for (f, f1), (g, g1) in product(cells, repeat=2):
        assert f[0] == f1[0] and f[-1] == f1[-1]
        if f[-1] == g[0]:
            assert cell(compose(g, f), compose(g1, f1))

    # K is 0->1. F[p]:0->1, G[p]:2->3; eta[0]:0->2,
    # eta[1]:1->3. Its conventional lax cell is G[p] eta[0]
    # => eta[1] F[p], hence L=>R.
    fp, gp, eta0, eta1 = (0, 1), (2, 3), (0, 2), (1, 3)
    assert compose(gp, eta0) == left
    assert compose(eta1, fp) == right
    assert cell(left, right)
    assert left != right and not cell(right, left)

    # A Cartesian evaluation comparison would require L=R.
    # A default lax comparison ev_0=>ev_1, evaluated on eta,
    # would instead require eta[1] F[p] => G[p] eta[0], i.e. R=>L.
    print(json.dumps({
        'model': 'finite locally posetal strict 2-category, one directed square',
        'family': 'constant at this 2-category; transports are identities',
        'retainedLaxSectionCell': [left, right],
        'cartesianEvaluationSquare': left == right,
        'sameDefaultLaxEvaluationSquare': cell(right, left),
        'oppositeEvaluationSquare': cell(left, right),
        'sectionFirstEvaluation': 'identity on the full section category retains eta and its L=>R cell',
        'scope': 'refutes the old k-first profile; does not exclude an explicit opposite-profile or tensor evaluator',
    }, indent=2))


if __name__ == '__main__':
    main()
