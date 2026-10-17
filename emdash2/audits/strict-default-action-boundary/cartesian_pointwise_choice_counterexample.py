"""Finite strict 2-category obstruction to arbitrary Cartesian inverse choices.

There is one object. Its Hom is the codiscrete groupoid on Z/2: exactly one
invertible 2-cell between every pair of 1-cells. Horizontal composition is
addition modulo two. This checks the stated strict-2-category example, not
a model of the entire native kernel or its object-path comparison rules.
"""

import itertools
import json


def compose(g: int, f: int) -> int:
    return g ^ f


def main() -> None:
    arrows = (0, 1)
    for a in arrows:
        assert compose(0, a) == compose(a, 0) == a
    for a, b, c in itertools.product(arrows, repeat=3):
        assert compose(c, compose(b, a)) == compose(compose(c, b), a)

    # Over the walking arrow, F=G is the constant strict diagram and eta=id.
    transport = 0
    eta = (0, 0)
    assert compose(transport, eta[0]) == compose(eta[1], transport)

    # Each choice is a quasi-inverse of eta's component, since the Hom
    # groupoid supplies invertible unit/counit 2-cells for either choice.
    selected_inverses = (0, 1)
    for forward, inverse in zip(eta, selected_inverses):
        assert compose(inverse, forward) in arrows
        assert compose(forward, inverse) in arrows

    lhs = compose(transport, selected_inverses[0])
    rhs = compose(selected_inverses[1], transport)
    assert lhs != rhs
    print(json.dumps({
        "strict_forward_naturality": True,
        "component_quasi_inverses": list(selected_inverses),
        "required_inverse_square": [lhs, rhs],
        "strict_inverse_naturality": False,
        "conclusion": "Cannot retain arbitrary pointwise quasi-inverse choices as a strict natural inverse",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
