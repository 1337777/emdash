# Whole parameter action and positive geometric cube decoder

Date: 2026-10-27
Status: checked non-library construction; specialized normalization and production qualification remain open
Owner: [native implementation outline](../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
Evidence: [source closures, attempts, resources and warnings](postcomposition_verification.json)

## Construction boundary

The new ordinary-lax whole postcomposition owner is a **structural operation**:

```text
Pˡ(I,A,B) : Functor_cat(A,B)
          → Functor_cat(Functor_cat(I,A), Functor_cat(I,B)).
```

It is not a theorem derived from the old fixed-F operation. Its object and
component projections use the existing fixed postcomposition and
prewhiskering actions. The explicit ladder exposes the Hom map, image of a
transformation, and its higher component. It does not identify this interface
with the Cartesian joint-composition map.

The post/left comparison is extracted from the original internal action.
At δ:D⇒E and i:I its component is the existing comparison of α at δ[i].
The check rejects an unrelated comparison and rejects promotion of arbitrary
α to a strict transformation. The concrete walking-square consumer retains
the original interchanger. No comparison cell is a caller-supplied argument.

Write G(A,B)=Functor_oplax_cat(A,B), I=WalkingArrow, and Gᵢ(C)=G(I,C).
The opposite-profile map P is defined by OddDual action on Pˡ at the encoded
categories. With the previously checked coordinate family
q_B:B→G(I,GrayTensor_R(I,B)), the forward map is the actual composite

```text
λ(B,C) = precompose(q_B) ∘ P(I,GrayTensor_R(I,B),C)
       : G(GrayTensor_R(I,B),C) → G(B,Gᵢ(C)).
```

The fixed bracketing is unchanged. No tensor symmetry, inverse closure map,
or closure equivalence is declared.

## Recursion and geometric dimensions

Let Q₀=I and Qₖ₊₁=GrayTensor_R(I,Qₖ), so Qₖ has geometric dimension k+1.
Let W₀(C)=C and Wₙ₊₁(C)=Gᵢ(Wₙ(C)), with the already constructed
dₙ:Wₙ(C)→NCₙ(C). Actual recursive shift maps compare the two iteration orders:

```text
sₙ : Wₙ(Gᵢ(C)) → Wₙ₊₁(C)
tₙ : Wₙ₊₁(C) → Wₙ(Gᵢ(C)).
```

Both composites are proved equal to identity by Nat induction, using the
already derived fixed postcomposition composition law. These inverses do not
depend on either walking-arrow inverse. Proof hypotheses appear only in the
induction theorem, never in the operational shift maps.

The whole forward geometric recursion is:

```text
c₀(C) = id_Gᵢ(C)
cₖ₊₁(C) = sₖ₊₁(C) ∘ cₖ(Gᵢ(C)) ∘ λ(Qₖ,C)
Dₖ(C) = dₖ₊₁(C) ∘ cₖ(C) : G(Qₖ,C) → NCₖ₊₁(C).
```

This is internal Nat elimination, universally over C. The line and square
computations and whole Hom action at variable k check. It is a forward map
relative to Pˡ's structural interface, not a geometric equivalence. Geometric
degree zero, reverse closure, the encoder and both geometric inverse laws
remain required.

## Source and computational review

The production sources are unchanged. The isolated package extends the
qualified `6791ff17` replay with two insertions at the original core owners:

- Component evaluation of represented vertical composition has one shared
  defined body and whole/capped projection rules. The actual Functor_cat
  codomain selects the transformation profile. Both observation orders check.
- A proof-time comparison expresses the existing strict pre/right action in
  the stable postcomposition presentation. All original functor, component
  and arrow parameters remain constrained. It does not strictify post/left
  naturality.

The new parameter owner has measured carrier guards on image composition
and intrinsic identity extraction. The LHS audit reports no unreviewed
compound inferred slots. The new next-Hom component clause is a canonical
projection companion: generic action can project before the whole component
equation is used. Its direct ladder computes to existing prewhiskering action
and retains the original modification.

Two limits remain explicit:

1. The fully expanded surrounding composite's next-Hom projection does not
   runtime-normalize to that named action. The whole component equation and
   direct canonical ladder pass. A naive nondependent `eq_ap` proof also
   fails because its Hom endpoints vary; it is not retained as a theorem.
2. Specializing the concrete extracted-cell observer to `B=Cat_cart` fails
   endpoint normalization. The generic higher-component owner specializes to
   `tdapp0`, and its endpoint presentations are not joined by the current
   source. [The pending consumer](postcomposition_cart_pending.lpfragment)
   and exact failed receipt are retained. This is not a positive gate.

Neither failure is hidden by deleting its obligation or strengthening lax
naturality. Production promotion requires their appropriate dispositions.
They do not replace the independent missing native second inverse or justify
deferring the rest of the geometric construction indefinitely.

## Validation and warnings

The combined 54-input scope passed with subject reduction in **97.488s /
595,020 KiB**, under 180s / 2 GiB, serial execution, the 64 MiB file bound and
`OCAMLRUNPARAM=o=20,v=1024`. The extension is justified by unchanged imports
previously crossing 90 seconds and the already measured 108–132 second
consumer scopes. No default limit or tool policy changed.

The focused typed-reflexivity and wrong-arrow controls for the pre/right
unification comparison also pass in **71.555s**. They exercise proof-time
unification explicitly; runtime conversion alone would not test that rule.

Against the earlier 39-input interface boundary, the warning inventory has
2,180 critical-pair reports versus 2,164, with the same 181 replaceable-pattern
reports and no parser issues. The closures differ; this is a family review,
not an assertion of identical warnings or global confluence:

- Nine new capped-root action overlaps are covered by the two root projection
  orders and unit/composition consumers.
- Four image-identity overlaps involve the generic identity/product/terminal/Q
  presentations. The actual typed Functor_cat unit passes; unrestricted
  cross-classifier joins are not inferred from these syntactic overlaps.
- The new component evaluator changes Functor/product projection overlaps;
  its whole/capped consumer and the actual extracted-cell consumer pass.
- The Cat_cart higher-component overlap remains the failed specialization
  above, not a classified success.

`replay_postcomposition.py --assemble-only` verifies source and dependency
identity without rerunning Lambdapi. Its modes select the interaction,
decoder, shift-inverse, pre/right-view or combined scope. The retained failures
and source snapshots are separately labelled in the verification record.
To revisit the Cat_cart failure, copy its linked fragment into the assembled
package as `native_postcomposition_cart_pending.lp` and check that target with
the same guarded 180s / 2 GiB profile. It is excluded from the green modes;
the original failed receipt pins the earlier source before the new canonical
higher-component clause. No full-library
aggregate, frontend transfer, production promotion or final nerve gate is
claimed by this audit.
