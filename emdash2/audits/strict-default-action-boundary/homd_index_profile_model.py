#!/usr/bin/env python3
"""Finite terminal-source obstruction to an all-Cartesian Homd index Hom.

K is the strict walking 2-cell: Hom_K(x,y) is I=(p -> q). F=id_K is a
strict functor, hence gives a permitted section between constant families.
The required first-Hom action is id_I, including its noninvertible arrow.
This is a necessary-profile check, not a model of the whole omega kernel.
"""
from itertools import product
import json


def main():
    objects = (0, 1)
    arrows = {(0, 0), (1, 1), (0, 1)}
    assert (1, 0) not in arrows

    # A constant-to-constant Cartesian transformation has equal components
    # at the ends of every index arrow. The intended components are p,q.
    strict = [pair for pair in product(objects, repeat=2) if pair[0] == pair[1]]

    # Default lax over T(I): delta : eta_q -> eta_p. This also excludes id_I.
    lax_over_transpose = [pair for pair in product(objects, repeat=2)
                          if (pair[1], pair[0]) in arrows]

    # A reversed transformation in Functor(I,T(Cart)) has the required
    # comparison eta_p -> eta_q, with both components still functors 1->H.
    derived_negative = [pair for pair in product(objects, repeat=2)
                        if (pair[0], pair[1]) in arrows]
    strict_functors_I_to_I = [pair for pair in product(objects, repeat=2)
                             if all((pair[a], pair[b]) in arrows for a, b in arrows)]

    identity = (0, 1)
    assert identity not in strict
    assert identity not in lax_over_transpose
    assert identity in derived_negative
    assert derived_negative == strict_functors_I_to_I
    assert (1, 0) not in derived_negative
    assert all(pair in derived_negative for pair in strict)

    # The same orientation is forced by the existing negative-Sigma arrows:
    # a -> H[kappa](b). Mapping a gives U_p(a) -> U_p(H[kappa](b));
    # the needed comparison is U_p H[kappa] -> H'[kappa] U_q.
    required_negative_total_comparison = ('U_p H[kappa]', "H'[kappa] U_q")
    default_lax_comparison = tuple(reversed(required_negative_total_comparison))
    assert required_negative_total_comparison != default_lax_comparison

    print(json.dumps({
        'base': 'strict walking 2-cell, Hom_K(x,y)=I=(p -> q)',
        'section': 'F=id_K, between constant strict families',
        'required_index_action': 'id_I, with noninvertible p -> q',
        'cartesian_components': strict,
        'default_lax_over_transpose_components': lax_over_transpose,
        'derived_negative_components': derived_negative,
        'strict_functors_I_to_I': strict_functors_I_to_I,
        'negative_total_required_direction': required_negative_total_comparison,
        'default_lax_direction': default_lax_comparison,
        'conclusion': 'The all-Cartesian index Hom cannot admit general intrinsic FF action; default lax over T(I) alone has the wrong direction.',
        'scope': 'finite necessary-profile result; the derived omega classifier and whole Q integration need separate qualification',
    }, indent=2))


if __name__ == '__main__':
    main()
