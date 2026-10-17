# Terminal and initial embeddings in the corrected diagram profile

Date: 2026-10-16
Predecessor: `1513dd07`
Status: staged zero-arrow and supplied kernel/cokernel adjunction reviewers qualified; represented-comma consumer and public promotion remain open
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)

## Contract review and selected migration

The original TerminalObject classifier is opaque. Its public observations
provide a default-lax terminal_arrow_transf, canonical-arrow cuts and
contractibility of the Hom **object groupoid**. They do not supply a strict
transformation admission or a contraction of the entire Hom category.
The inspected CartesianCategory and AdditiveCategory constructors/projections
retain an existing TerminalObject; they do not strengthen its transformation.
The Freyd adjunction-model package also takes its dual terminal structure as
input. This is a source-boundary review, not an exhaustive model classification.

The migration retains that general terminal contract. Its arrow diagram now
uses the oplax coefficient required by a generally lax transfor:

```text
T  : TerminalObject(C,t)
J  = Arr(terminal_arrow_transf(T))
J  : C → Functor_oplax_cat(WalkingArrow_cat,C).
```

The original initial-arrow body used dimension-one Op_transf, which now
requires an actual strict transformation. The existing whole total duality
instead preserves the default lax profile. The corrected explicit input is:

```text
T₀ : TerminalObject(TotalOp_cat(C),t)
initial_arrow_transf(T₀)
   = TotalOp_transf(terminal_arrow_transf(T₀))
   : const(t) ⇒ id_C
I  = Arr(initial_arrow_transf(T₀))
   : C → Functor_oplax_cat(WalkingArrow_cat,C).
```

This changes the higher dual hypothesis; it is not an implicit conversion
from TerminalObject(Op_cat(C),t). No blanket terminal-transfor strictness,
ordinary-category assumption or new supplied comparison is introduced.
The original chosen terminal arrows remain the component values of the dual
initial transformation. Total duality's existing off-diagonal action uses the
appropriate old post endpoint, rather than incorrectly copying the old middle
action of an arbitrary lax transfor.

Both embeddings are still definitions through the original arrow-introduction
owner. Their whole source/target/differential and point observations retain
the selected input functors and transformations. The original zero-arrow
reviewer keeps all 18 positive and two negative assertions, with the actual
profile, decoded point functors and canonical mixed-arrow object classifiers.

## Core identity normalization

The initial mixed-action consumer exposed the precomposition counterpart of
the earlier postcomposition identity-tag issue. Total duality normalizes
`id_(TotalOp(C))` to `id_C` before the identity-input cut is selected. The
existing represented precomposition owner now wildcards that inferred
identity category. Its typed input determines the endpoints. The rule still
returns the same mapped arrow; no naturality cell is replaced by an identity.

The updated zero-arrow reviewer passes in 57.910s at 90s/2GiB with o=5,
warnings and subject reduction. The inherited core controls pass in 18.538s
with o=20 at the normal cap. Reordering the independent terminal-object import
did not solve the o=20 allocation failure and was reverted.

## Coupled supplied adjunctions

The kernel/cokernel structure declarations use the same oplax diagram
coefficient as J and I. Their selected K/Q functors, supplied adjunctions,
unit/counit-derived inclusion/projection maps, and transpose/untranspose mate
bodies are retained. Diagram variables are objects of that coefficient;
diagram-map variables are its Homs. The original mate reviewer retains all
16 positive and two negative observations, including whole Hom cancellation
and cancellation on arbitrary arrows.

These are supplied whole adjunction structures. This migration does not prove
their existence for every higher preadditive category, or silently identify
ordinary-lax and oplax diagram categories. At the ordinary-category semantic
interpretation the distinctions disappear; native comparisons still require
their actual qualified operations. Remaining original consumers must be
reviewed with those types, rather than importing a global profile equality.

## Preserve the coefficient and the chosen inverse

The adjunction mate's original Hom comparison is now a comparison of
Cat_cart-valued families. Its category is Catd(Base), whose objects are
functors Base→Cat_cart and whose transformations remain lax. It is not
Cart(Base,Cat_cart). The migrated component therefore evaluates the existing
comparison in Cat_cart and applies the existing Cat_cart_include through
defiso_fmap. Its public result remains DefIso(Cat_cat,HL,HR), with the same
chosen forward and inverse maps.

The mapped inverse must remain the runtime owner. An attempted early fold
to the bare evaluated component caused the original generic cancellation
rule to reconstruct a Cat_cat-valued family endpoint for a Cat_cart-valued
family. That fold was removed. The original defiso_evaluation_points module
is byte-identical to the baseline. Two point-cancellation projections of
the existing mapped inverse handle the concrete functor-valued consumer;
they retain the selected inverse package. Four narrowly scoped proof-time
comparisons give the original adjunction unit/counit bodies at whole and
point level. Typed reflexivity in the original reviewer exercises these
comparisons. No caller proof, new inverse or coefficient equality is supplied.

The original generic mate reviewer retains 17 positive/seven negative checks;
only the constant-source negative's coefficient annotation changes to keep
it well typed. The kernel/cokernel reviewer retains 16 positive/two negative
checks, including whole and arbitrary-arrow inverse cancellation. A focused
initial-action projection joins the capped route; negative controls reject
a dimension-one-only terminal hypothesis, unsupported terminal strict-profile
admission, and cancellation with a different inverse package. The shared
weighted/inverse-action reviewer also passes unchanged (20 positive/six negative).

## Validation and warning review

The [verification record](production_zero_arrow_verification.json) retains
exact input and log hashes, resources, failed experiments and next boundary.
The final green receipts all rehash to the emitted package. Core and the two
changed extension rule owners have zero unreviewed LHS audit candidates.
Manual owner review retains Cat_cat on the mapped point cut as the actual
functor-valued target and Cat_cart on the component comparison as the actual
coefficient. Neither is an inferred reducible endpoint discriminator.

The core warning comparison is 1955→1947: eight added and sixteen removed
reports belong to the relaxed identity-category pattern and its identity,
composition and mapped-action overlaps. The shared strict-action owner has
34 reports before and after; two bodies change through the earlier inherited
postcomposition identity pattern, and neither new mapped point cut adds a
critical-pair report. The new terminal import and unchanged evaluated-inverse
module introduce their own inherited overlap families. Their consumed
observations pass; this is not a claim of global confluence or an attempt to
solve unrelated warnings by adding rules.

## Resource record and next qualification

The adjunction/mate reviewer exceeded 2 GiB with o=5 while importing the
existing DefIso point module. The final target-specific 3,072 MiB check
passes in 29.696s with o=20; the host had 16,357 MiB available before launch.
Reported child maximum RSS is 1,984,780 KiB (distinct from the guard's memory
ceiling and address-space accounting). The generic mate reviewer passes in
27.019s at 2GiB/o=20, zero-arrow controls in 55.889s at 2GiB/o=5, and the
weighted regression in 25.863s at 2GiB/o=20. All retain the 90-second deadline,
source-only loading, warnings, subject reduction, serial execution and
MemorySwapMax=0. Defaults are unchanged. This follows the user's existing
authorization for measured bounded adjustments. The larger limit diagnoses
and contains import cost; it is not a performance graduation claim.

The broader gray_profiles reviewer now reaches represented_comma_prof in
zero_arrow_cones. Its old body passes hom_int directly where Catd(B) is
expected; the strict Hom owner now lands in Cart(B,Cat_cart), and its existing
hom_int_view is the whole inclusion into Catd(B). Review that original
consumer together with its zero-arrow diagram profile. The failed broader
run is a recorded next boundary, not a green integration claim. Do not add
a Cart/Catd equality, infer OneCat from preadditivity or identify lax/oplax
diagram categories globally.

Public promotion and the remaining kernel/library migration, wrapper
retirement and final catalog/health/CI/source-pin gates remain required.
The separate nerve goal remains paused.
