#!/usr/bin/env python3
"""Finite semantic control; not a Lambdapi proof or a library implementation.

K is the walking arrow. E is constant at the terminal category and D is
constant at the walking arrow. A normal-lax FF chooses 0,1 and the cell
0->1. All families and component/transport functors here are strict.
"""
import json


def main():
    objects = (0, 1)
    arrows = {(0, 0), (0, 1), (1, 1)}
    opposite = {(y, x) for x, y in arrows}
    for x in objects:
        assert (x, x) in arrows and (x, x) in opposite
    for relation in (arrows, opposite):
        for x, y in relation:
            for y1, z in relation:
                if y == y1:
                    assert (x, z) in relation

    # A component functor from the terminal category is just a chosen object;
    # its only arrow is sent to that object's identity, hence it is strict.
    components = {0: 0, 1: 1}
    assert all((v, v) in arrows for v in components.values())
    required_square = (components[0], components[1])
    assert required_square in arrows
    assert required_square not in opposite
    assert tuple(reversed(required_square)) in opposite
    print(json.dumps({
        'inputLaxComparison': list(required_square),
        'inputExists': True,
        'sameProfileTransposeExists': False,
        'oppositeSquareExists': True,
        'scope': 'ordinary walking-arrow obstruction only; no uniform omega oplax construction claimed',
    }, indent=2))


if __name__ == '__main__':
    main()
