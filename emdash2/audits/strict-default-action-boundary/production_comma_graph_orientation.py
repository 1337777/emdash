#!/usr/bin/env python3
"""Finite orientation diagnostic for the old arbitrary-Theta graph input.

This models a strict two-category fragment, not the entire emdash kernel.
K is 0->1. C has one object and the join-monoidal Boolean square as its
Hom category. F and G are constant at that object, with identity transport.
Theta's entries h[x,y] are defined when Hom_K(x,y) is inhabited. Inner lax
naturality requires h[x,y]<=h[x,z]; outer lax naturality requires
h[x',y]<=h[x,y] for x<=x'. A graph with the prescribed F/G side arrows
would require h[0,0]<=h[1,1].
Both nested transformations are conventional-lax; the two displayed
comparisons belong to their separate x and y variable directions.
"""
import itertools
import json


def run():
    poset = range(4)
    leq = lambda a, b: a | b == b
    join = lambda a, b: a | b
    for a in poset:
        assert join(0, a) == join(a, 0) == a
    for a, b, c in itertools.product(poset, repeat=3):
        assert join(join(a, b), c) == join(a, join(b, c))
        if leq(a, b) and leq(b, c):
            assert leq(a, c)
    for a, b, c, d in itertools.product(poset, repeat=4):
        if leq(a, b) and leq(c, d):
            assert leq(join(a, c), join(b, d))

    # 0 is the unit; a=1 and b=2 are incomparable, with common upper bound m=3.
    objects = (0, 1)
    def verify_theta(h):
        for x, y, z in itertools.product(objects, repeat=3):
            if x <= y <= z:
                assert leq(h[x, y], h[x, z])
        for x, xp, y in itertools.product(objects, repeat=3):
            if x <= xp <= y:
                assert leq(h[xp, y], h[x, y])
        # Every inhabited modification square commutes because P is thin.
        # The mixed corner (0,1,0,1) has empty source Hom_K(1,0).
        for x, xp, y, yp in itertools.product(objects, repeat=4):
            if x <= xp <= y <= yp:
                assert leq(h[xp, y], h[x, y]) and leq(h[x, y], h[x, yp])
                assert leq(h[xp, y], h[xp, yp]) and leq(h[xp, yp], h[x, yp])

    h = {(0, 0): 1, (0, 1): 3, (1, 1): 2}
    verify_theta(h)
    assert not leq(h[0, 0], h[1, 1])
    assert not leq(h[1, 1], h[0, 0])
    # Canonical pre/right-normal control: the outer comparison is identity,
    # but the retained inner naturality and graph comparison are noninvertible.
    canonical = {(0, 0): 1, (0, 1): 3, (1, 1): 3}
    verify_theta(canonical)
    assert canonical[0, 1] == canonical[1, 1]
    assert leq(canonical[0, 0], canonical[1, 1])
    assert not leq(canonical[1, 1], canonical[0, 0])
    return {
        "model": "strict one-object two-category; Hom is the Boolean-square join poset",
        "base": "walking arrow",
        "theta": {"h00": "a", "h01": "m", "h11": "b"},
        "innerLaxComparison": "a -> m",
        "outerLaxComparison": "b -> m",
        "requiredGraphComparison": "a -> b",
        "requiredGraphComparisonExists": False,
        "scope": "rejects unrestricted nested conventional-lax Theta with the prescribed F/G projections; does not reject a graph of an actual conventional lax eta",
        "canonicalCase": "the pre/right convention identifies h[x,y](p) with eta[y] F[p], making the outer x comparison strict",
        "canonicalControl": "outer comparison identity; inner and graph comparison a -> m still noninvertible",
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
