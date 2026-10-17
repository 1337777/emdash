# Canonical internal action and the comma middle section

Date: 2026-10-17
Predecessor: `a4b774e4`
Status: canonical admission, middle section and its first nonidentity action qualified; full graph incomplete
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)

## Canonical profile and actual views

For any ordinary lax eta:F⇒G, tapp1_int_cart_func provides the canonical
internal action in the Cartesian x-profile:

```text
eta ↦ Theta_eta
Theta_eta : Hom_Cart(T(A),Catd(A))(I_A, I_(F,G)).
```

Its inner y-components remain the original tapp1_at_transf(eta,x), and their
values are the original tapp1_func(eta,x,y). The whole ordinary inclusion,
its next Hom action, ordinary point view and the existing identity shortcut
are checked. Generic Theta is not silently admitted, and the negative
ordinary-naturality check for eta still fails as intended.

Sigma_parameter_funcd refines Sigma applied to a map that is strict in an
outer parameter L. The component maps over K can still be ordinary lax
Functord maps. Its output is a whole Cartesian map between the admitted
total families; its component is the existing sigma_map_func(U[x]).
It does not declare a Cat_cart-valued Sigma functor on all Catd(K), or a
Cartesian functor on every higher variation of U.

These are declared canonical profile refinements, in the same role as the
existing Sigma_coeff_func. Their ordinary views and computations are
qualified here; they are not proofs of strictness for arbitrary raw maps.
No extra comparison cell, equation proof or naturality certificate is a
caller argument. In particular, the canonical input is still the original
ordinary lax eta.

Forgetting the Sigma refinement through Cat_cart_include now computes to
the original ordinary Sigma image of the same U. The other whiskering leg
must be the literal identity of inclusion. An earlier proof-time-only view
passed in isolation but collided with a later library congruence comparison.
The constructor projection avoids that comparison-order problem and retains
the selected families and map. Its nonidentity-other-leg negative is retained.

## Derived middle section and directed action

The original comma helpers now apply TotalOp_funcd to this admitted Sigma
map, then compose it with the existing hom_identity_graph_sec over O(B).
The resulting whole middle section computes at x to (x,eta[x]). For
p:x→y, its action over y→x in O(B) is the opposite of the inner Sigma arrow

```text
(p, lambda_eta(p)),
lambda_eta(p) : G[p] ∘ eta[x] → eta[y] ∘ F[p].
```

The checked filler is literally
tapp1_post_laxity_cell(eta,x,x,y,p,id_x), extracted by the existing machinery.
It is not supplied as an independent square. The whole section type,
component, ordinary Sigma view, arrow conversion and typed-reflexivity
carrier comparison all pass. The original post/left cell remains retained.

Two measured proof-time gaps were repaired at their existing owners:

- mapped precomposition by F[p] has a direct comparison with tapp1(eta,p);
  the original p is supplied by that existing action, not inferred from F[p];
- Obj(Sigma(K,E)) has a sufficient congruence comparison retaining both K
  and the whole E. Obj remains non-injective. This propagates an already
  justified endpoint comparison through the Sigma carrier.

The action test uses the existing Sigma-Hom normal form as its canonical
carrier. Normal-form traces isolated the endpoint difference before the
congruence change. Negative controls retain the mapped arrow, whole family,
ordinary lax naturality, and the strict outer-parameter admission boundary.

## Qualification and remaining work

The [verification](production_comma_admission_verification.json) records
exact input/log hashes, projection-order failures and final results. The
current core controls, six positive/three negative canonical-profile checks,
three positive/three negative Sigma-parameter checks, and five middle-section
checks pass with subject reduction. Core/focused times are about 19–25s at
90s/2GiB/o=20. The original comma import prefix takes about 34s under its
existing reviewed 90s/3GiB profile; host headroom was inspected.

There are three additional core critical-pair reports at the new forgetting
projection, involving inherited Path_cat, Terminal_cat and Homd_coeff_cat
identity normalization. Importing the old profile module adds its existing
StrictFunctor_cat identity-tag overlap. These are recorded overlap families;
the consumed identity and nonidentity-other-leg cases pass. No global
confluence conclusion is asserted. LHS review has no unreviewed candidates.

Replay after a relevant internal-action, inclusion, Sigma or section-owner
change: regenerate with production_owner_migration.py, then run the affected
internal_x_profile_controls.lp, sigma_parameter_profile_controls.lp,
inverse_core_controls.lp or comma_graph_middle_prefix.lp through the bounded
runner with the profiles above. The full represented-comma file remains an
expected failure at the recorded next boundary until that migration lands.

The full source now reaches comma_graph_basechange_source_catd: the old
Cat_cat-valued composition is being used as an admitted Cat_cart family.
Next review the Cartesian represented family, restricted pullback/total
formation, and the actual whole base-change transformation together. Keep
the existing G and sigma_pullback_total_func components. Its total-dual map
and the remaining section/totalization/inverse comparisons still need migration.

The later generic-Theta signatures and ordinary eta wrappers also remain to
be wired to the valid x-profile. The external one_cat_transf_from_hom_action
consumer already has an ordinary-target hypothesis; preserve that admission
and its original Hom comparison rather than adding a strictness requirement
on arbitrary eta. Complete original reviewers, other library routes, wrapper
retirement, public promotion and final gates remain required.
