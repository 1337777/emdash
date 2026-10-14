#!/usr/bin/env python3
"""Isolate external strict FF from E's higher action and compare the two Qs.

Finite strict 2-category observation only. It does not construct a whole
omega-category Q or certify the native prototype's remaining legacy owners.
"""
import json
from mixed_family_profile_models import Finite2


def main():
    # E is indexed by the walking 2-cell p=>q. Its two transports H,J
    # have walking-arrow source and the following free lax square as target.
    # No composition of nonidentity base arrows is needed. The external
    # displayed map can be id_E, so it is strictly natural throughout.
    left = ('H0', ('e0', 'k'))       # J[h] o epsilon[0]
    right = ('H0', ('h', 'e1'))      # epsilon[1] o H[h]
    b = Finite2(('H0', 'H1', 'J0', 'J1'),
        {'h': ('H0', 'H1'), 'k': ('J0', 'J1'),
         'e0': ('H0', 'J0'), 'e1': ('H1', 'J1')}, [(left, right)])
    assert left != right
    assert (left, right) in b.cells and (right, left) not in b.cells

    # Moving u through f |-> E[f](u) gives an oplax, not a default-lax,
    # transformation between the two transport functors. This precludes
    # naively promoting this parameter to an ordinary default Functor.
    transport_u_default_lax = (right, left) in b.cells
    transport_u_oplax = (left, right) in b.cells
    assert not transport_u_default_lax and transport_u_oplax

    # In the Homd u-action, after taking Hom(-,v) and reversing the index,
    # default lax naturality has the original left=>right orientation.
    # Evaluate at v=J1 and id_v. The distinction is an actual distinction
    # of objects in Hom_B(H0,J1), not just different syntactic words.
    id_v = ('J1', ())
    homd_left = b.compose(id_v, left)
    homd_right = b.compose(id_v, right)
    assert (homd_left, homd_right) in b.cells
    assert homd_left != homd_right
    assert (homd_right, homd_left) not in b.cells

    # The old whole root first forms T_fib(E):C2(K)->Cat. Reversing
    # the base 2-cell reverses its endpoints, but the fibre transpose
    # T(epsilon):T(J)=>T(H) needs right=>left as its default lax square.
    # T reverses 1-cells only; it cannot supply that missing 2-cell.
    transpose_same_lax = (right, left) in b.cells
    # Total O reverses that 2-cell too; its local transformation exists.
    total_op_same_lax = (left, right) in b.cells
    assert not transpose_same_lax and total_op_same_lax

    # Positive stricter control: the ordinary commuting diamond, regarded
    # as a locally discrete 2-category. The transformation components are
    # nonidentity; it is their naturality comparison which is identity.
    objects = ('H0', 'H1', 'J0', 'J1')
    order = {(a,a) for a in objects} | {
        ('H0','H1'), ('J0','J1'), ('H0','J0'), ('H1','J1')}
    while True:
        more = {(a,c) for a,b0 in order for b1,c in order if b0==b1}
        if more <= order:
            break
        order |= more
    assert all(a==b0 or (b0,a) not in order for a,b0 in order)

    def compose(after, before):
        assert after in order and before in order and before[1]==after[0]
        result = before[0], after[1]
        assert result in order
        return result

    strict_left = compose(('J0','J1'), ('H0','J0'))
    strict_right = compose(('H1','J1'), ('H0','H1'))
    assert strict_left == strict_right
    assert 'H0' != 'J0' and 'H1' != 'J1'

    print(json.dumps({
        'external_FF': 'identity, hence strict',
        'outer_E_and_transports': 'strict on the walking-2-cell base',
        'E_alpha': {'default_lax': True, 'strict_naturality': False},
        'transport_u_parameter': {'default_lax': transport_u_default_lax,
                                  'opposite_naturality': transport_u_oplax},
        'Homd_u_index_naturality': {
            'left': homd_left, 'right': homd_right,
            'lax_Q_required_cell_exists': True,
            'cart_Q_required_equality_holds': False,
            'reverse_cell_exists': False,
            'nonidentity_strict_transfor_control_accepts_both': True},
        'old_root_fibre_transpose': {
            'T_same_default_lax_exists': transpose_same_lax,
            'O_same_default_lax_exists': total_op_same_lax,
            'whole_coordinated_O_root_constructed': False},
        'scope': 'finite dimension-two necessary tests; not omega sufficiency or a native no-go theorem',
    }, indent=2))


if __name__ == '__main__':
    main()
