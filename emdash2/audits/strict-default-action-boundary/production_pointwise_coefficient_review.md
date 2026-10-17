# Displayed pointwise-equivalence coefficient

Date: 2026-10-16
Predecessor: `b94125df`
Status: assembly owner and focused inherited observations qualified; downstream producer integration open
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)

In the selected foundation, tdapp0_fapp0(eta,x) is a component in
Cart(E[x],D[x]). StrictTransfdPointwiseOmegaAlong now asks for the chosen
pointwise OmegaEquivAlong in that same category. Both inverse-component
projection rules use it too. The names, arguments, selected left/right
inverses, whole Transfd outputs and cancellation-law owners are retained.
The ordinary StrictTransfPointwiseOmegaAlong branch is unchanged.

This changes the meaning of the pointwise data to the actual fibre coefficient;
it is not an inclusion of arbitrary ordinary inverse data into Cart. The new
negative control explicitly rejects that attempted substitution after forgetting
the forward component. FF and GG remain the default lax Functord maps across
the base. No blanket strictness of Cat-valued transfors is added.

The existing file already labels pointwise-to-whole assembly as a primitive
assumption, with its semantic replacement deferred. That qualification is
retained. These checks establish its corrected typing and selected-component
computation; they do not derive the assembly principle or settle its semantics.

All ten original observations are retained in the focused owner driver.
The two displayed inverse observations use Cart. The former negative for
functor composition becomes positive under the strict default, while the
ordinary transfor-naturality negative is retained. With the new coefficient
negative the focused driver has nine positive/two negative assertions and
passes in 18.899s at 90s/2GiB/o=20 with subject reduction and warnings.
The owner emits no critical-pair reports; its LHS audit has zero unreviewed
slots. Core, adjunction-family and weighted/inverse receipts still match all
their inputs, so unchanged checks are not repeated.

The original reviewer remains staged with its full imports. Its direct-cover
route currently fails earlier at yoneda_psh_func in presheaves: the canonical
Cartesian Hom needs its existing ordinary-family view for Psh. Therefore the
focused driver is not reported as a successful full reviewer run.

There is one actual library producer of StrictTransfdPointwiseOmegaAlong,
direct_cover_completion_restriction_glue_transfd_pointwise_omega. Its current
body calls an ordinary functor-category equivalence assembled from fibrewise
data. Its component-transfor declaration also predates the Cartesian fibre
profile. Both must be reviewed together with the chosen inverses; a forgetful
view alone is insufficient. This producer remains an explicit migration
obligation, not an already-admitted use of the changed coefficient.

The main broader import has advanced to comma_graph_source_catd in
represented_comma_families, where the old T(B) base conflicts with the
corrected O(B) identity-graph family. Review the coupled source/middle/target
families and total-dual action while retaining the allowed laxness of the
original graph input. No T(B)=O(B) equality is admitted.

The [verification record](production_pointwise_coefficient_verification.json)
records both failed integration boundaries, current hashes and the focused
result. Remaining original library migration, public promotion, strict-wrapper
retirement and final catalog/health/CI/source-pin gates remain required.
