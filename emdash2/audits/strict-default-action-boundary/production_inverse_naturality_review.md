# Native inverse endpoint paths and whole action readings

Date: 2026-10-17
Predecessor: `f2e56729`
Status: native component and whole inverse endpoint paths checked; extracted-cell agreement and Cartesian admission remain open
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_inverse_naturality_verification.json)

The native property IsStrictCell is not just an equation between endpoints.
It consists of a path p between them and agreement of the existing cell with
path_to_hom(p). IsStrictTransfor applies this condition to the existing whole
post/left and pre/right comparison transformations. The finite strict-2-
category example in the preceding review concerns literal strict naturality;
it does not by itself refute this native path-based admission contract.

The new proof-only observations derive, from the existing equality-valued
inverse laws and associativity, an endpoint path for the same selected left
inverses. Writing eta_x : F[x] → G[x] and l_x for its selected left inverse:

```
eta_y ∘ F[p] = G[p] ∘ eta_x
F[p] ∘ l_x = l_y ∘ G[p].
```

The selected left inverse's right-cancellation law is first derived using
the existing omega_equiv_candidate_left_to_right theorem. The square proof
uses the actual inverse laws and explicit associativity paths. Its instance
at a classified forward transfor obtains the forward square internally.
No new primitive, cancellation axiom, or operational proof argument is added.
These are equality observations, not new inverse-map constructors.
The classified forward transfor will be the canonical fibre comparison;
the original displayed matching map is not required to become strict.

Lifting this calculation to the original whole naturality endpoints exposed
two missing whole proof-time readings: the conventional pre/right tapp1_func
view and postcomposition through the actual image F[g]. Their counterparts
at components already compute. The new comparisons retain both runtime heads,
the supplied transformation, F and the selected arrow. Their original-owner
placement passes the inherited core/curry regression plus two positive and
three negative controls (276 positives/73 negatives). In particular the
post/left reading remains unavailable for a general lax transfor, a wrong
image is rejected, and runtime conversion does not unfold the whole head.
Warning bodies remain exactly the preceding core's 1995 bodies.

The component proof and its whole-in-f version both check. The latter states
equality between the original strict_transfor_naturality_lhs_func and
strict_transfor_naturality_rhs_func of the actual inherited inverse owner.
It uses typed whole-view congruences and explicit associativity paths, rather
than additional global associativity normalizers. The seven proof definitions
are derived terms; no new inverse or cancellation constructor is postulated.

The separate inverse_post_admission_boundary.lp attempts to form
IsPostStrictTransfor using this endpoint path and reflexivity for the second
field. It fails precisely at comparison of the path's Core-inclusion image
with the original fdapp1_comma_projection_transf. This is a failed positive
obligation, not a successful negative control or a proof that admission is
impossible. A different endpoint path or a nontrivial cell-agreement proof
may be needed. The actual Cartesian admission and whole inverse laws remain
required; no new equation identifying those two cells is installed.

The original locality lower prefix also passes again with the new whole
readings: three original positives and the existing coefficient noncoercion
control. Its warning bodies match the preceding 2397-body import. Other
library receipts remain historical until their affected integration gates
are rerun; changed core bytes are not silently treated as unchanged inputs.

Next inspect the inherited whole inverse cancellation paths and the native
intrinsic action on composition as possible sources of the cell agreement.
Reflection of path-image cells through the actual Hom-equivalence action is
one possible derived route to review; no such reflection theorem is assumed.
Those whole cancellation paths are opaque in the original assembly owner;
there is no component beta identifying them with the individual laws in
u[x]. Do not assume that their induced endpoint path is the particular
pointwise-law path constructed in this tranche.
Do not replace that missing derivation with a supplied comparison, a fresh
inverse, or the unselected generic Cartesian assembly contract.

The rejected Cartesian arbitrary-choice assembly is still absent. A user
preference question about permitting an explicitly marked additional assembly
assumption is pending; the selected route continues to require derived
admission. No absence of a reply selects the assumption route.

The endpoint target exhausted the 2GiB import cap in about 23s. With measured
host headroom (about 16GiB available), the existing 300s/4GiB/o=20 profile
reached the actual associativity presentation diagnostic and then checked the
component proof in about 24s. The whole-reading core regression passed in
about 18s at 240s/2GiB/o=20. The final whole endpoint proof and admission
boundary took about 25s each, and the locality-prefix check about 30s, at
300s/4GiB/o=20. Resource defaults, subject reduction and serial/file/no-swap
guards remain unchanged.
