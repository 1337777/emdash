# Identity Homd x consumer audit

Current status: the right-route ordinary leaf passes; target raw-postcomposition,
its y-component proof, and the actual native source-action comparison fail
their positive obligations. The optional stronger L=R diagnostic remains
unrun. The checked successor is recorded in
[the native-action closure](homd_native_action_source_closure.md); original
source and failure evidence are preserved here. This audit adds no runtime
rules, unification clauses, declarations, or operational proof parameters.
The donor is the checked foundation assembly
`combined_controls.lp` with SHA-256
`d7337feeb94a35be9edef287262092ed2c8cc840fe324784ed580ae7667a3cc7`.
The recipe pins that file and its verification record; it does not regenerate
or change the predecessor assembly.

For arbitrary p:x→x′, the existing definition of `Homd_target_catd(E)`
gives its whole x-action through `hom_postcomp_tele_cart_func`, and its
capped x-action through `hom_postcomp_func`. On the actual section
`homd_id_src_sec(E,x,u)`, runtime retains `hom_postcomp_fapp0`.
The generic existing proof-time comparison reads this as
Γ[p] composed vertically with that section, where Γ is `ProfRep_cov_int`.
The full/capped projection orders and reversed CoAt2 direction of an
arbitrary base 2-cell are tested, with the unreversed direction rejected.

The y-component of this whole section comparison is obtained with generic
`eq_ap`; no new component computation is assumed. Its right endpoint is
κ(pre_p(y)) composed with `homd_id_tgt_func(E,x,u,y)`, where
pre_p(y):Hom_K(x′,y)→Hom_K(x,y) is the existing ordinary-Hom precomposition
functor. This observation consumes the represented lift's declared whole
transformation and its companion component projection. It does not consume
or certify a new lift identity, composition, triangle, or extracted-laxity
law. The donor separately checks the actual represented lift's nonidentity
y-arrow action against its R body.

The independently checked other route uses only
`homd_id_src_func(E,x′) ∘ Op(E[p])`. Applying it to u and following the
existing y/v/q′ projections yields the direct ordinary Hom
`Hom_E[y](E[q′∘p](u),v)`, using strict functoriality of E. A changed source
object u′ is rejected. This passing leaf consumer is not an
identification of whole sections.

The actual action boundary and optional equality diagnostic are separate:

- `identity_action_boundary.lp` compares the actual native
  `tapp1_func(homd_id_int)` with the source/left route
  `Homd_target(E)[p] ∘ homd_id_src_func(E,x)`, packaged using existing
  Cartesian fixed prewhiskering. The checked donor has no identity-Homd
  x-action projection implementing this comparison.
- `route_coherence_boundary.lp` asks the stronger equality of the resulting
  transported canonical section with `homd_id_src_sec(E,x′,E[p](u))`.
  This optional positive diagnostic is not a required ambient Homd law:
  the actual required datum is native laxity from the first route to the
  second. It supplies no comparison argument and installs no rule.

The later production Cat-valued native-action owner identifies ambient
`tapp1_func` with the source/left route; the right route requires its
guarded strict comparison. Consequently, a runtime rule assigning the right
route to this ambient primitive would require a separate compatibility
argument. Merely computing the ordinary leaf on that route does not provide
one. The later native laxity extraction is outside this checked prefix; the
audit does not invent a replacement cell. The general relative `homd_int(FF)` remains the defined target-side
composite with the identity primitive, and its arbitrary raw FF retains its
original ambient profile.

Run `homd_x_consumer_migration.py --check-authoring` to check the exact
recipe pins and `--check-evidence` to check any recorded receipt/log/output
hashes. The recipe never invokes Lambdapi. Root owns all serial checks and
their classification; failed positive obligations are not negative tests.

The original receipt results are:

- `target_controls.lp`: failed at the typed raw-postcomposition comparison,
  `20261013T171539Z-87edda652f6d496fa688dd10a016ac8e`.
- `section_y_comparison.lp`: failed at the same whole comparison supplied to
  `eq_ap`, `20261013T171554Z-8f468ff4978f45dfad03a61324a625b1`.
- `right_route_leaf.lp`: passed with its source-object perturbation negative,
  `20261013T171610Z-297bde87f746435ab1268fca7f8a2eda`.
- `identity_action_boundary.lp`: failed at the whole native source-action
  comparison, `20261013T171624Z-7aa8c106750840c19797f1ed60428763`.
