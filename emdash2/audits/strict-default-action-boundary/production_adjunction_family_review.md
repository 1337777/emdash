# Ordinary-target adjunction-family migration

Date: 2026-10-16
Predecessor: `d5bd294c`
Status: original owner and complete reviewer qualified in the staged package
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)

The unit/counit mismatch was in the selected postcomposition helper, not in
the public unit/counit classifiers. Both unit_adj_transf and counit_adj_transf
still return ordinary lax transformations. The short
comp_cat_cov_func_func_transf name now selects the Cartesian coefficient and
strict input transformations, whereas this original adjunction is between
ordinary Functor_cat(B,R) and Functor_cat(B,L).

The two existing unit/counit projection rules now use the existing generic
hom_postcomp_tele_transf at Cat_cat directly. Their supplied J, chosen F/G,
ordinary-target hypotheses, ordinary mapping endpoints, components and
further action are retained. There is no new strictness admission, wrapper,
unit/counit constructor or profile equality. The original reviewer uses that
same generic owner in its four direct observations of the whole cells.

The first real component check exposed a second issue: the inverse-preserving
runtime orientation expands represented postcomposition by a composite into
two successive represented cuts. The old proof-time raw-composition view
does not transitively match their associated raw form. A direct comparison
at the existing postcomposition owner now expresses

```text
q∗(p∗g) ≐ (q ∘ p) ∘ g.
```

Every endpoint and operand is retained in residual constraints. This is an
identity-family associativity view; no runtime orientation changes, no
arbitrary functor strictness axiom and no transformed naturality cell are
introduced. The actual reviewer failed without it. A typed-reflexivity
consumer and a different-arrow negative control additionally qualify the
generic form. The existing inverse cuts remain the runtime owners.

The original reviewer retains all 16 positive/four negative assertions:
whole and point inverse cancellation, next Hom action, whole unit/counit,
components, nonidentity transformation action and semantic views. It passes
in 27.365s. The affected core controls pass in 18.365s; the shared weighted
and inverse-action reviewer passes in 23.798s. These runs use the normal
90s/2GiB cap with o=20, warnings, subject reduction and serial/no-swap guards.
The exact core and reviewer warning-body multisets are unchanged. Generic
LHS audits report zero unreviewed slots; the new comparison selects the
literal identity functor and leaves inferred classifier positions open.

The [verification record](production_adjunction_family_verification.json)
retains exact source/log hashes and the failed-before evidence. The broader
import now reaches StrictTransfdPointwiseOmegaAlong in
strict_pointwise_equivalences: tdapp0_fapp0 returns a component in the
Cartesian coefficient Hom, while the old pointwise-equivalence statement
uses the ordinary functor category. Review the selected inverse-data profile
and its callers together; a forgetful view alone cannot supply a Cartesian
inverse from an arbitrary ordinary inverse. This is the next unqualified
consumer, not a new restriction on all FF or all Cat-valued transfors.

The related old-helper inventory has one other original library occurrence,
in one_cat_family_naturality_paths, plus the original diagnostics. It remains
a consumer to review at its actual source position. Public promotion,
remaining migration, wrapper retirement and final gates remain open.
