#!/usr/bin/env python3
"""Finite semantic checks for the old intrinsic Homd target and raw skew legs.

This is an independent ordinary-category model, not a Lambdapi proof or
an assertion that every specified input is constructible in the old kernel.
Thin categories have strict identity/composition and only identity higher
cells. No weak-category or non-strict-functor assumption is used.
"""
from itertools import product
import json


def thin_category(objects, nonidentity):
    relation = {(x, x) for x in objects} | set(nonidentity)
    assert all((x, z) in relation for x, y in relation
               for y2, z in relation if y == y2)
    return frozenset(relation)


def is_functor(source, target, mapping):
    return all((mapping[x], mapping[y]) in target for x, y in source)


def natural_transformation(source, target, first, second):
    # In thin categories, existence of all components plus functoriality
    # implies every naturality square commutes.
    return (is_functor(source, target, first)
            and is_functor(source, target, second)
            and all((first[x], second[x]) in target for x, _ in source))


def constant_sections():
    # Native Pi(const B) compares with Functor(K,B). Equivalently these are
    # Cat-valued transformations const(1)=>const(B). Their component at x
    # selects F[x], and their comparison at p:x->y is the ordinary F[p].
    # All functors here are strict: the categories are thin and ordinary.
    base = thin_category((0, 1), {(0, 1)})
    value = thin_category(('a', 'b'), {('a', 'b')})
    candidates = [dict(zip((0, 1), xs)) for xs in product(('a', 'b'), repeat=2)]
    functors = [f for f in candidates if is_functor(base, value, f)]
    strict_sections = [f for f in functors
                       if all(f[x] == f[y] for x, y in base)]
    directed = {0: 'a', 1: 'b'}
    assert directed in functors and directed not in strict_sections
    assert (len(functors), len(strict_sections)) == (3, 2)
    return {
        'ordinaryFunctorObjects': len(functors),
        'strictConstantFamilySections': len(strict_sections),
        'excludedFunctor': directed,
        'retainedArrow': 'a -> b',
        'qualification': 'Global strictness of Cat-valued transformations conflicts with the existing constant-section/functor identification; no duality is used.',
    }


def cat_valued_hom_detection():
    # F:[2]->Y is normal lax, where Y has one object and Hom_Y(*,*) is
    # the strict monoidal poset 0<1, with tensor=max and identity=0.
    # F(01)=F(12)=0 but F(02)=1. Its nonidentity compositor is 0->1.
    # H=Hom_Y(*,F(-)) is Cat-valued, with H(p)(a)=max(F(p),a).
    def action(i, j):
        assert i <= j
        return int((i, j) == (0, 2))

    for a, b, c in product(range(2), repeat=3):
        assert max(max(a, b), c) == max(a, max(b, c))
        assert max(0, a) == a == max(a, 0)
    for i, j, k, l in product(range(3), repeat=4):
        if i <= j <= k <= l:
            start = max(action(i, j), action(j, k), action(k, l))
            assert start <= max(action(i, k), action(k, l)) <= action(i, l)
            assert start <= max(action(i, j), action(j, l)) <= action(i, l)
            # Coherence follows from uniqueness of parallel 2-cells.
    for i in range(3):
        assert action(i, i) == 0
    composed = [max(action(1, 2), max(action(0, 1), a)) for a in range(2)]
    direct = [max(action(0, 2), a) for a in range(2)]
    assert composed == [0, 1] and direct == [1, 1]
    assert all(a <= b for a, b in zip(composed, direct))
    return {
        'normalLaxFunctorExists': True,
        'HqAfterHp': composed,
        'Hqp': direct,
        'evaluationAtIdentity': [composed[0], direct[0]],
        'CatValuedHomIsStrict': False,
        'qualification': 'The retained blended Hom action detects F composition. Declaring every Cat-valued functor strict would exclude this F or require changing that Hom constructor/interface.',
    }


def check():
    base = thin_category((0, 1), {(0, 1)})
    fibre = thin_category(('u', 'v'), set())
    target = thin_category(('a', 'b'), {('a', 'b')})
    first = {'u': 'a', 'v': 'a'}
    second = {'u': 'b', 'v': 'a'}
    assert natural_transformation(fibre, target, first, second)
    assert not natural_transformation(fibre, target, second, first)

    # E and D are constant strict families on 0->1. FF has the above strict
    # component functors and noninvertible normal-lax comparison first=>second.
    # There is no pair of composable nonidentity base arrows; unit/coherence
    # conditions reduce to identities and thin-category commutativity.
    assert (0, 1) in base and (1, 1) in base
    assert len([a for a in base if a == (0, 1)]) == 1
    assert len([a for a in base if a == (1, 1)]) == 1

    # At y=1, pre_p:Hom_K(1,1)->Hom_K(0,1) is the unique isomorphism between
    # terminal categories. Hence the target section transport preserves this
    # local fibre, independently of a presentation of companion composition.
    left_hom = int((first['u'], second['v']) in target)
    right_hom = int((second['u'], second['v']) in target)
    assert (left_hom, right_hom) == (1, 0)
    assert not (left_hom == 0 or right_hom > 0)
    # This does not refute the bare raw two-skew type. The local oplax
    # choice M=L has 1->1<-Empty. It refutes the added forward-lax reading.
    apex = left_hom
    assert (left_hom == 0 or apex > 0)
    assert (right_hom == 0 or apex > 0)

    # The actual desired intrinsic laxity still exists: evaluate instead at
    # v=E[p](u)=u and the identity filler. Its output is a->b.
    assert (first['u'], second['u']) in target
    assert (second['u'], first['u']) not in target

    # Enumerate the small example's normal-lax component pairs. Two of the
    # nine valid pairs reject the purported ordinary-lax whole target.
    maps = [dict(zip(('u', 'v'), values))
            for values in product(('a', 'b'), repeat=2)]
    valid = [(f, g) for f in maps for g in maps
             if natural_transformation(fibre, target, f, g)]
    bad = [(f, g) for f, g in valid
           if any((f[u], g[v]) in target and (g[u], g[v]) not in target
                  for u in ('u', 'v') for v in ('u', 'v'))]
    assert (len(valid), len(bad)) == (9, 2)
    strict_pairs = [(f, g) for f, g in valid if f == g]
    assert len(strict_pairs) == 4
    assert not any(pair in strict_pairs for pair in bad)

    # A separate raw two-skew-leg example. L->M and R->M do not provide L->R.
    # Constant source 1 and target fork a->c<-b supply strict component
    # functors and coherent thin skew legs. This is not a model of all
    # repository intrinsic-action/closure contracts, nor an admission proof
    # for its raw Transf. It is distinct from the normal-lax subcase above.
    fork = thin_category(('a', 'b', 'c'), {('a', 'c'), ('b', 'c')})
    assert ('a', 'c') in fork and ('b', 'c') in fork
    assert ('a', 'b') not in fork and ('b', 'a') not in fork

    return {
        'status': 'finite semantic checks pass',
        'ordinaryLaxWholeTarget': {
            'normalLaxComponentPairs': len(valid),
            'strictComponentPairs': len(strict_pairs),
            'pairsWithImpossibleTargetAction': len(bad),
            'leftHomCardinality': left_hom,
            'rightHomCardinality': right_hom,
            'requiredDirection': 'nonempty -> empty',
            'identityModificationDoesNotRepairTarget': True,
            'desiredForwardLaxityStillExists': 'a -> b',
            'localRawOplaxLegsExist': '1 -> 1 <- Empty',
        },
        'rawTwoSkewLegs': {
            'post': 'a -> c', 'pre': 'b -> c',
            'forwardComparison': 'a -> b absent',
        },
        'allCatValuedTransforsStrict': constant_sections(),
        'allCatValuedFunctorsStrict': cat_valued_hom_detection(),
        'qualification': [
            'Refutes the stated ordinary-lax x packaging, not Homd or intrinsic laxity in a corrected profile.',
            'Does not refute the bare raw two-skew Functord type; its local oplax legs exist.',
            'The reverse empty-to-nonempty component exists; this alone does not construct a whole oplax omega package.',
            'Raw two-skew transfors and conventional normal-lax transfors are distinct input doctrines.',
            'The fork is not a model of the full repository Transf interface and does not justify narrowing every raw FF.',
            'No kernel consistency, profile admission, or computational implementation is certified.',
        ],
    }


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
