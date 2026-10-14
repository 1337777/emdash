#!/usr/bin/env python3
"""A dimension-three necessary test for the proposed double-lax Homd.

This is a finite semantic model, not a Lambdapi contradiction. The mapping
categories are interpreted as standard Gray-lax internal Homs. Tensor
orientations use d(a tensor b)=da tensor b+(-1)^dim(a) a tensor db.
See Ara--Guetta 2503.08832v1, paragraphs 17, 21 and 35--38, and
Steiner math/0403237v2, Example 3.10 and Proposition 7.2.
"""
from collections import Counter
import json
from mixed_family_profile_models import Finite2


def signed_tensor_boundary(left, left_dim, left_source, left_target,
                           right, right_source, right_target, names):
    out = Counter()
    for pair, sign in [((left_target, right), 1),
                       ((left_source, right), -1),
                       ((left, right_target), (-1) ** left_dim),
                       ((left, right_source), -((-1) ** left_dim))]:
        out[names[pair]] += sign
    return {name: value for name, value in out.items() if value}


def path_difference(target, source):
    out = Counter(target[1])
    out.subtract(source[1])
    return {name: value for name, value in out.items() if value}


def check():
    # Four objects F0,F1,G0,G1. Besides identities, the nonempty homs are:
    # C(F0,F1)=walking Ftheta, C(G0,G1)=walking Gtheta,
    # C(F0,G0)={e0}, C(F1,G1)={e1}, and C(F0,G1)=the hom below.
    # Its objects L_i=G(h_i)e0 and R_i=e1F(h_i) are arrows of C.
    # Its edges are 2-cells of C; kappa is its sole nonidentity 2-cell,
    # hence a 3-cell of C. There is no chain of three nonidentity arrows
    # between the four objects, so nonunit outer associativity is vacuous.
    t = ('L0', ('eps0', 'Ftheta'))
    s = ('L0', ('Gtheta', 'eps1'))
    hom = Finite2(('L0', 'L1', 'R0', 'R1'), {
        'Gtheta': ('L0', 'L1'), 'Ftheta': ('R0', 'R1'),
        'eps0': ('L0', 'R0'), 'eps1': ('L1', 'R1'),
    }, [(t, s)])
    assert t != s and (t, s) in hom.cells and (s, t) not in hom.cells

    # Outer whiskering embeds the two walking homs into this hom. A strict
    # functor from a walking arrow is determined by its image edge. The
    # chosen edges and their identity 2-cells exist, so these composition
    # functors preserve all inner composition and identities.
    assert ('R0', ('Ftheta',)) in hom.paths
    assert ('L0', ('Gtheta',)) in hom.paths
    for edge in ('Ftheta', 'Gtheta'):
        arrow = (hom.edges[edge][0], (edge,))
        assert (arrow, arrow) in hom.cells

    # A is the walking 2-cell theta:h0=>h1. An input lax transformation
    # epsilon:F=>G is classified by A tensor D1 -> C. Its two arrow
    # comparisons are eps_i:L_i=>R_i; its theta comparison is kappa:t=>s.
    input_boundary = signed_tensor_boundary(
        'theta', 2, 'h0', 'h1', 'alpha', 'F', 'G', {
            ('h0', 'alpha'): 'eps0', ('h1', 'alpha'): 'eps1',
            ('theta', 'F'): 'Ftheta', ('theta', 'G'): 'Gtheta',
        })
    assert input_boundary == path_difference(s, t)
    for i in (0, 1):
        choices = {p for p in hom.paths
                   if p[0] == f'L{i}' and hom.target(p) == f'R{i}'}
        assert choices == {(f'L{i}', (f'eps{i}',))}

    # Let K be the walking 2-cell f=>g and E send it to epsilon.
    # Evaluate Homd at y and v=G1. The prescribed u-action sends h_i to
    # H_i:P_1=>P_0 over T(I), I=Hom_K(x,y), with components pre_F(h_i)
    # and pre_G(h_i). Its index comparison at alpha^T is forced to eps_i.
    # A theta image would be a standard lax 2-transformation H0=>H1.
    # Its components are forced to Ftheta and Gtheta by the homs above.
    # A lax 2-transformation uses T(I) tensor D2; here its mixed boundary
    # is s=>t, opposite to the sole kappa provided by epsilon.
    requested_boundary = signed_tensor_boundary(
        'alphaT', 1, 'G', 'F', 'theta', 'h0', 'h1', {
            ('F', 'theta'): 'Ftheta', ('G', 'theta'): 'Gtheta',
            ('alphaT', 'h0'): 'eps0', ('alphaT', 'h1'): 'eps1',
        })
    assert requested_boundary == path_difference(t, s)
    assert all(requested_boundary[k] == -v for k, v in input_boundary.items())
    assert (s, t) not in hom.cells

    # If the input coherence is invertible, this particular obstruction
    # disappears. This is a control, not permission to strengthen E.
    invertible = Finite2(hom.objects, hom.edges, [(t, s), (s, t)])
    assert (s, t) in invertible.cells
    return {
        'input': 'strict E and strict E[f],E[g]; E[alpha] is a Gray-lax transformation; external FF=id',
        'retainedTwoDimensionalComparisons': ['L0 -> R0', 'L1 -> R1'],
        'inputThreeCell': 'kappa: (Ftheta o eps0) -> (eps1 o Gtheta)',
        'requestedThreeCell': '(eps1 o Gtheta) -> (Ftheta o eps0)',
        'requestedCellExists': False,
        'inputTensorBoundary': input_boundary,
        'requestedTensorBoundary': requested_boundary,
        'invertibleInputControl': True,
        'scope': 'Refutes the prescribed source-u functor into the unmodified double-Gray-lax target under standard higher-transform semantics; not a native Empty derivation or a no-go for corrected mixed mapping profiles.',
    }


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
