# Separate first-coordinate faces and degeneracies

Date: 2026-10-27
Status: qualified non-library split shape maps and all-degree whole geometric face-degeneracy identity; full index/native compatibility remains open
Owner: [native implementation outline](../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
Evidence: [tensor-split, first-faces and first-face-controls replays](reverse_verification.json)

## Split tensor maps

The [separate maps](tensor_split_coordinate.lpfragment) are defined by the
existing right closure:

```text
δₐ : B → A⊗ᴿB       = coevaluation(A,B)[a]
π  : A⊗ᴿB → B       = uncurry_R(const_A(id_B)).
```

The earlier structural target-naturality contract gives the whole
coevaluation square. Its component at a, followed by the existing
curry/uncurry path, proves π∘δₐ≐id_B. Reflection through those same inverse
operations proves δₐ∘π≐Cₐ, where Cₐ is the independently constructed
first-coordinate collapse. Thus these are actual separate maps, not merely
another name for the earlier endomorphism. No tensor-unit category
identification is required.

Both proofs retain whole B-functors. The only structural premise beyond the
older right closure is the [already recorded target naturality](right_closure_naturality_review.md).
This extension adds definitions and derived proofs, with no new primitive,
rewrite, unification rule or operational equality argument.

## Uniform geometric shapes

The [Nat-indexed construction](geometric_first_faces.lpfragment) uses the
existing shapes Q₀=Terminal and Qₙ₊₁=GrayCubePos_R(n). It defines

```text
δₐⁿ : Qₙ → Qₙ₊₁
πⁿ  : Qₙ₊₁ → Qₙ
πⁿ∘δₐⁿ ≐ id_Qₙ.
```

At n=0, δ is the actual constant endpoint map Terminal→WalkingArrow and π
is the constant map to Terminal. The existing terminal-contraction proof
supplies the whole shape identity. At successor n the maps are the split
tensor maps above, with the original right bracketing and coordinate order.
The endpoint a varies through a whole WalkingArrow→L(Qₙ,Qₙ₊₁) functor;
this is not a family declared solely by its object values.

Using G(A,C)=Functor_oplax_cat(A,C), fixed precomposition gives whole maps

```text
dₐⁿ : G(Qₙ₊₁,C) → G(Qₙ,C)       restriction along δₐⁿ
sⁿ  : G(Qₙ,C) → G(Qₙ₊₁,C)       precomposition along πⁿ

dₐⁿ ∘ sⁿ ≐ id_G(Qₙ,C).
```

The last statement is equality of whole functors at variable n. It follows
by the already checked oplax-precomposition composition law and the actual
shape identity. It also recovers an arbitrary whole parameter family
D:K→G(Qₙ,C); no objectwise functor extensionality is used.

For positive tensor steps, the opposite composite sⁿ∘dₐⁿ agrees with
restriction along the independent collapse Cₐ. It is not asserted to be a
second identity. Both actual walking endpoints satisfy the split identity.
The zero level remains G(Terminal,C); it is not replaced by C, and the
negative runtime-category control continues to reject that identification.

## Qualification and remaining scope

The split-map scope passes on 22 inputs in **75.662s / 309,036 KiB**.
The all-degree source passes on 77 inputs in **110.282s / 618,384 KiB**.
The final whole-collapse and actual zero/endpoint consumers pass on 78 inputs
in **99.461s / 629,996 KiB**. Subject reduction is enabled; the final scope
uses the explicit 300s / 2 GiB profile. All five warning inventory fields
match the prior mixed-diagram scope: 2,296 critical-pair reports, 181
replaceable patterns and no parser issues.

The original zero/successor shape computations and the retained endpoint
are checked directly. Exact replay assembly verifies all source hashes.
These sources remain non-library; no production promotion or broad aggregate
is implied by the focused evidence.

Only the first coordinate is handled here. Other-coordinate faces and
degeneracies, their cross-coordinate relations, common augmentation/index,
compatibility with the native encoder/decoder, the mixed and native inverse
proofs, and production qualification remain required. This is progress toward
the full cubical nerve, not a replacement of its acceptance contract.
