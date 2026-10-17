# Represented comma and zero-cone migration

Date: 2026-10-16
Predecessor: `a4c58fc8`
Status: original zero-cone map reviewer qualified in the staged package; broader migration remains open
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)

The original represented-comma constructor now exposes the actual canonical
Hom family's type:

```text
represented_comma_prof(F) : T(A) → Cart(B,Cat_cart)
represented_comma_prof(F)[a][b] = Hom_B(F[a],b).
```

The two-sided total already consumes this Cartesian family. The preceding
checkpoint's tentative hom_int_view route would forget the profile that
this consumer needs. No inclusion is needed here. The original Hom owner,
its composition with T(F), nested Sigma/total-duality construction, object
constructor and source/target projections remain in use.

ZeroArrowCone specializes this construction to the corrected terminal-arrow
embedding J:C→Functor_oplax_cat(WalkingArrow_cat,C). Diagram objects and maps
use this coefficient, and the whole vertex/differential observations use the
existing opposite-profile evaluator. This introduces no new ordinary-category
assumption, supplied naturality cell or lax/oplax category equality.

The native map still consists of the original data:

```text
(a, b, α),   α : b ∘ h₀ → h₁ ∘ F[a].
```

Directly elaborating that nested pair after substituting the alternating-dual
diagram target caused unwanted higher-category equations during unification.
Changing the readable Hom annotations alone did not fix them. The selected
implementation defines the same tuple once, with general A,B,F, as
represented_comma_map, then specializes that transparent definition in
zero_cone_native_map. Its body is literally Struct_sigma a (Struct_sigma b α).
There is no primitive map, new rewrite/unification rule, changed caller data
or operational equality transport. Both original source/target map projections
then compute to the supplied a and b.

A scoped OddDual precomposition comparison was investigated. It validated
the expected raw-composition reading and removed term-comparison failures,
but did not solve the remaining category constraints. The general tuple
definition makes that additional rule unnecessary for this consumer. It and
its temporary control driver were removed from the selected authoring recipe;
the diagnostic receipts retain the experiment. The diagram-evaluation source
is byte-identical to the preceding checkpoint.

The original reviewer retains both assertions. The final run passes with
subject reduction, warnings, 90s/2GiB, o=5 and the serial/no-swap guard in
57.389s. Existing core, zero-arrow, adjunction and weighted receipts are
reused only where every recorded input still matches. The
[verification record](production_zero_cone_verification.json) records exact
hashes, warning comparison, failed alternatives and the next import boundary.
No active library catalog or mathematical source pin is upgraded by this
non-library checkpoint. Public promotion and the remaining goal gates stay open.

The broader importer reaches one_cat_postcomp_adjunction's unit observation
in one_cat_adjunction_families (lines 21–25 of the unchanged original owner).
Its old whiskering RHS does not have the migrated Cartesian/strict-transfor
unit profile. The input already carries ordinary-target hypotheses; the next
slice must review those existing capabilities and retain its supplied J.
The failure is recorded, not bypassed with a mapping-category equality.
