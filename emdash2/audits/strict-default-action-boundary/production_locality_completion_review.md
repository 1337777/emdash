# Cartesian pointwise equivalence and original locality integration

Date: 2026-10-18 (UTC)
Predecessor: `5319dcc2`
Status: Cartesian whole equivalence and original locality checked; central diagnostic migration remains open
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_locality_completion_verification.json)

The admitted inverse maps now carry cancellation paths in the actual
`Functor_cart_cat`, so `pointwise_cart_omega_along` constructs the required
whole Cartesian equivalence. Equality induction lifts the original ordinary
inverse laws between admitted constructors. Two constructor-scoped
proof-time comparisons identify admission of an identity/composite with the
existing Cartesian identity/composite. Both composite operands are compared
with their actual ordinary views. No general admission retraction, arbitrary
path reflection, category equality, or new inverse-assembly assumption is
installed.

The derivations now live in the staged original
`emdash3_2_strict_pointwise_equivalences.lp` owner. It imports the existing
profile and Eq1 proof machinery. Its ordinary primitive inverse maps,
component beta rules and supplied whole laws are preserved byte-for-byte.
Removing the added derived block/imports and reverting the three previously
migrated displayed coefficient annotations recovers the original file
exactly. The new Cartesian result is derived relative to those inherited
ordinary assembly contracts, rather than a new pointwise assembly primitive.

The original locality fibre-equivalence owner now returns an equivalence in
its actual Cartesian coefficient and uses `pointwise_cart_omega_along` on
the existing classified fibre transformation. The retained-member evidence
and both inverse choices are unchanged. The outer matching map remains lax.
The subsequent displayed assembly and final ordinary locality statements
retain their original construction and public types. The complete
`locality_profile_controls.lp` passes, including the final
`direct_cover_completion_is_topology_local` consumer.

The wider profile reviewer reached one additional stable-head comparison in
`comma_pre_cell_omega`: the conventional pre/right computation after both Hom
and transfor action have capped. Its direct proof-time comparison preserves
the two input arrows and the transformation, and leaves the post/left leg
lax. The original profile reviewer then passes all 59 positive/13 negative
assertions. The Cartesian equivalence controls preserve both selected
inverse maps, reject replacing either composition operand, and retain the
existing rejection of ordinary inverse data in the Cartesian slot.

The joint profile/locality gate passes with one shared import closure. This
checks the actual migrated module and original consumer, rather than only
the independently emitted proof fragments. The core regression also passes
276 positive/79 negative assertions. Source-only replay, subject reduction
and the owner-position rule audit remain enabled. Selected core/profile
warning bodies are unchanged; the larger import inventory is recorded
separately and is not a confluence certificate.

The real `emdash3_2_checks.lp` and its entire original import closure are now
staged. Its first observed failure is the whole
`one_cat_diagram_family_transf_reindex_path` in `emdash3_2_diagram_evaluation.lp`.
The proposed oplax reindexing proof currently tries to force the arbitrary
parameter category B to `Functor_cat I C`, and D to an identity. Neither
restriction is part of the required contract. This is a failed positive
integration obligation, not a semantic counterexample or a reason to omit
the central diagnostics.

Next review the actual whole precomposition identity

```
oplax_precomp(F) o oplax_precomp(D) = oplax_precomp(D o F)
```

and its first-Hom observation against the existing fixed-precomposition
owners. Preserve the arbitrary source parameter and original ordinary-target
guard. The original pre-migration proof was reflexivity for its former
ordinary precomposition presentation; the corrected opposite-profile proof
still requires the corresponding whole comparison. Do not specialize D to
an identity, restrict B to a mapping category, or replace the whole claim by
point components.

The isolated Cartesian laws pass at the reviewed 300s/4GiB/o=20 profile.
The complete profile/Cartesian controls take about 53s under that profile.
The coupled profile/locality closure takes about 123s at 600s/4GiB/o=5,
with maximum child RSS about 3.27GiB. A live sample recorded 99.9% CPU and
about 2.73GiB RSS while processing the broader import; this is import/proof
cost, not a core 123-second check. The standalone core regression takes about
26s at 240s/2GiB/o=20. The central diagnostic failure takes about 104s under
the same 600s/4GiB/o=5 integration profile and reaches an actual type boundary.
Normal defaults, file limits, serial execution and no-swap containment remain
unchanged. About 15GiB of host memory was available before the larger run.

The migration remains staged. Central and remaining library qualification,
redundant strict-functor-wrapper retirement, production promotion, and final
catalogue/health/CI/source-pin review remain required. The separate
application-equivalence goal is not resumed.
