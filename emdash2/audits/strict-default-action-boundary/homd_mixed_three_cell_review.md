# Mixed third-dimensional Homd action

Date: 2026-10-14
Status: semantic obstruction to the current double-Gray-lax interpretation;
transported inner mapping profile proposed, not yet implemented
Plan: [foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Model: [finite three-cell calculation](homd_mixed_three_cell_model.py)

## Scope of the correction

The candidates at `56509f7b` and `bf1e8d6b` have the recorded Lambdapi
typing/computation evidence. That evidence does not establish the standard
Gray-lax semantics of their structural Q and source-u declarations. The
following finite strict 3-category shows that the proposed source-u functor
cannot have those semantics with both nested mapping categories interpreted
as ordinary Gray-lax internal Homs and the recorded component values.

This affects the identity Homd already. E and its transports are strict,
E's image of a base 2-cell is lax, and external FF can be the identity.
It is not an argument for stricter external FF or a restriction to an
ordinary base. The old nested-Cart alternative still fails its earlier
dimension-two test. Neither unchanged candidate is therefore qualified for
all the currently required E inputs.

No kernel Empty derivation is claimed. In particular, choosing one strict
leg for a raw transfor does not by itself establish that all its higher
cells implement the standard Gray internal Hom. The obstruction below is
to that intended interpretation with the stated Homd component operations.

## Conventions and reference facts

Write L(A,B) for the standard lax Gray internal Hom and P(A,B) for its
oplax counterpart. For the reference tensor ⊗, strict functors satisfy

```text
maps(A ⊗ B,C) ≅ maps(A,P(B,C)) ≅ maps(B,L(A,C)).
```

Thus a lax n-transformation on A is a strict map A⊗Dₙ→C. This is the
convention of [Ara–Guetta v1, paragraph 21](https://arxiv.org/html/2503.08832v1#S2).
It gives the project's chosen first comparison direction
G[h]ε[u] ⇒ ε[u′]F[h]. The model uses
∂(a⊗b)=∂a⊗b+(−1)^dim(a) a⊗∂b on globe tensors; see
[Steiner v2, Example 3.10 and Proposition 7.2](https://arxiv.org/pdf/math/0403237v2).

T reverses dimension one only. It is not anti-monoidal for this tensor in
all dimensions; odd/even duals have that property, whereas total dual is
monoidal. These reference distinctions are in Ara–Guetta paragraphs 35–38.
The counterexample and repair derivation below are our calculations, not a
claim that either paper states a theorem about this repository's Homd.

## Explicit finite model

Let A be the walking 2-cell θ:h₀⇒h₁ between arrows 0→1. Take two strict
functors F,G:A→C and a lax transformation ε:F⇒G. Its components are
e₀:F0→G0 and e₁:F1→G1. Put

```text
Lᵢ = G[hᵢ] e₀
Rᵢ = e₁ F[hᵢ]
βᵢ : Lᵢ ⇒ Rᵢ
a  = G[θ] e₀ : L₀ ⇒ L₁
b  = e₁ F[θ] : R₀ ⇒ R₁.

t = b ∘ β₀
s = β₁ ∘ a
κ : t ⇛ s.
```

The executable model names these 2-cells `eps0`, `eps1`, `Ftheta`,
`Gtheta`, respectively.

C has four objects F0,F1,G0,G1. Its nontrivial Homs are the walking
categories on F[θ] and G[θ], the singleton Homs on the two components,
and C(F0,G1). The latter is the finite strict 2-category with objects
L₀,L₁,R₀,R₁, the four displayed edges, and the single generating
2-cell κ:t⇒s. It has no 2-cell s⇒t. The two outer whiskerings embed
the walking Homs as a and b. There are no three composable nonidentity
arrows between the four objects. Inner strictness and whiskering are
checked by the reused finite-2-category enumerator; outer associativity
is otherwise just the identity laws. This defines a strict 3-category,
extended to a strict omega-category by identity higher cells.

The boundary of θ⊗α in A⊗D₁ is s−t, so ε with comparison κ is a
lawful standard lax transformation. Here α is the arrow of D₁.
Use it as the image E[α] of the walking base 2-cell f⇒g, with transports
E[f]=F and E[g]=G. There is no nontrivial base-composition constraint.

At fixed y and v=G1, let

```text
Pᵤ(f) = Hom_C(F[u],v)
Pᵤ(g) = Hom_C(G[u],v)
Pᵤ : T(I) → Cat,     I = Hom_K(x,y).
```

The prescribed u-action of hᵢ is a lax transformation Hᵢ:P₁⇒P₀. At
f and g it is precomposition by F[hᵢ] and G[hᵢ]. Its comparison at
αᵀ:g→f, evaluated at id_v, must be βᵢ:Lᵢ⇒Rᵢ. Those are the unique
2-cells with those boundaries, so a different choice cannot repair this
example.

Now θ must give a lax 2-transformation H₀⇒H₁. Its f/g components
are likewise forced by F[θ] and G[θ]. A lax 2-transformation uses
T(I)⊗D₂. Its mixed generator has boundary t−s, so this demands
the missing 3-cell s⇛t. The script calculates both signs and enumerates
the directed cells. Allowing an inverse to κ removes this particular
obstruction; that is a control, not an admitted extra assumption on E.

## A targeted mapping-profile correction

The issue can be expressed without guessing more dimension reversals.
For strict A,B define the transported mapping category

```text
M(A,B) = T(P(T(A),T(B))).
```

Its objects correspond to the same strict functors A→B. It has ordinary
component evaluation, but its higher transformation convention differs
from L(A,B). By dualizing strict maps and using the oplax closure,

```text
maps(Z,M(A,B))
 ≅ maps(T(Z),P(T(A),T(B)))
 ≅ maps(T(Z) ⊗ T(A),T(B))
 ≅ maps(T(T(Z) ⊗ T(A)),B).
```

These are strict-map bijections; no claim of an unqualified equivalence
between the default lax mapping categories is being inserted. Equivalently,
M is the internal Hom for the tensor obtained by transporting the
opposite tensor through T. Its closure exists in all dimensions by this
construction. This establishes the proposed local mapping profile, not
the whole Q coefficient or its composition.

For the actual transport action I→L(A,C), uncurry gives A⊗I→C.
Apply T and then the strict representable Hom T(C)→Cat at a fixed v.
The resulting map T(A⊗I)→Cat curries, using M, to

```text
T(A) → M(T(I),Cat).
```

Thus the required local source-u package has an all-dimensional semantic
construction with the same object values. It does not need a reverse κ.
The proof uses only strict functor duality and the two Gray closures.
No equality witnesses, supplied comparison cells or a weak resolution of A
are inputs.

The representable Hom can here be read in the strict Cartesian coefficient
universe. Compatibility of this construction with the retained public lax
universe is part of the whole coefficient qualification below; the closure
argument does not identify a Gray universe with a strict omega-category.

The next coefficient candidate to assess is therefore

```text
Hom_Q(A,B) = L(A,M(T(B),Cat)).
```

This changes the inner higher profile, not the leaf category or the
ordinary strict-functor interpretation of a fixed-v/f projection. The
whole y-section, covariant inclusion, represented mates, Q composition,
outer root and intrinsic action must still be checked together. Do not
declare this modified Q complete merely from the local closure argument,
or silently alter the public default Transf. Both earlier Q alternatives
remain comparison evidence, with their now explicit admission limitations.

## Reproduction and next work

From emdash2:

```bash
python3 audits/strict-default-action-boundary/homd_mixed_three_cell_model.py
```

The test passes when it finds κ and proves the reverse absent; it is not
a positive test of the old Q candidate. No Lambdapi owner changed, so the
previous native receipts stay valid for their exact conditional contracts.
The recorded run passes with model SHA-256
`019e8f45d028870c2cc45b50fa94a16582b22f5fbe76baf0f21dae32d0425188`.
Next implement/qualify M's native object and component views and apply
them to this same source-u consumer before rebuilding the whole ladder.
Keep the existing direct telescope and reusable whole-root construction;
do not add an arbitrary whole-u extractor with the refuted old profile.
