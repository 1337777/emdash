#!/usr/bin/env python3
"""Finite semantic control for the general-FF source-transpose boundary.

Not a Lambdapi checker or a full omega/coefficient model. The base is [1],
both families are constant, their transports are identities, and FF has
strict component functors. Its single naturality comparison is nonidentity.
"""
from dataclasses import dataclass
import json


@dataclass(frozen=True)
class FinitePoset:
    objects: tuple
    relation: frozenset

    def hom(self, x, y):
        return frozenset({(x, y)}) if (x, y) in self.relation else frozenset()

    def opposite(self):
        return FinitePoset(self.objects, frozenset((y, x) for x, y in self.relation))

    def check(self):
        assert all((x, x) in self.relation for x in self.objects)
        assert all((x, z) in self.relation
                   for x, y in self.relation for y0, z in self.relation if y == y0)
        assert all(x == y for x, y in self.relation if (y, x) in self.relation)


def functor(A, B, F):
    return (set(F) == set(A.objects)
            and all(F[x] in B.objects for x in A.objects)
            and all((F[x], F[y]) in B.relation for x, y in A.relation))


def transformation(A, B, F, G):
    # In posets there is at most one arrow, so components imply naturality.
    return functor(A, B, F) and functor(A, B, G) and all(B.hom(F[x], G[x]) for x in A.objects)


def map_exists(source, target):
    # These Hom sets are viewed as discrete categories (empty or terminal).
    return not source or bool(target)


def main():
    K = FinitePoset((0, 1), frozenset({(0, 0), (0, 1), (1, 1)}))
    A = FinitePoset(('u', 'v'), frozenset({('u', 'u'), ('v', 'v')}))
    B = K
    for C in (K, A, B, A.opposite(), B.opposite()):
        C.check()
    F0 = {'u': 0, 'v': 0}
    F1 = {'u': 1, 'v': 0}
    assert transformation(A, B, F0, F1)
    assert not transformation(A, B, F1, F0)
    assert F0 != F1

    # T_fib(FF) still has F0,F1 as object maps. In T(B), the normal-lax
    # direction is absent; the oplax direction is supplied by the same cell.
    assert functor(A.opposite(), B.opposite(), F0)
    assert functor(A.opposite(), B.opposite(), F1)
    assert not transformation(A.opposite(), B.opposite(), F0, F1)
    assert transformation(A.opposite(), B.opposite(), F1, F0)

    # The old internal-action target uses H_FF[x](F_x(u)). At y=1, v='v',
    # both represented index categories are terminal, and the represented
    # x transport is their identity. Its two local values are therefore:
    H0 = B.hom(F0['u'], F1['v'])
    H1 = B.hom(F1['u'], F1['v'])
    assert len(K.hom(0, 1)) == len(K.hom(1, 1)) == 1
    assert len(H0) == 1 and len(H1) == 0
    assert not map_exists(H0, H1)  # required by a normal-lax root
    assert map_exists(H1, H0)      # actual oplax direction

    print(json.dumps({
        'status': 'finite semantic control passed; not native omega qualification',
        'base': '[1]', 'families': 'constant discrete{u,v} and [1]',
        'strictTransports': True, 'strictComponentFunctors': True,
        'FF0': F0, 'FF1': F1,
        'noninvertibleNaturalityComponent': '0 -> 1 at u',
        'fibreTransposeNormalLax': False, 'fibreTransposeOplax': True,
        'oldSourceImageValuesAtY1V': [len(H0), len(H1)],
        'oldSourceImageNormalLax': False, 'oldSourceImageOplax': True,
        'conclusion': 'Retain general FF, but repair the old same-profile Op_funcd/source-image internal-action signature.'
    }, indent=2))


if __name__ == '__main__':
    main()
