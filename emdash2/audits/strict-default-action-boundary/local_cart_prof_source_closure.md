# Local Cartesian product-Prof view

This non-library replay isolates the next integration dependency selected in
[the living plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md):
use the existing Cartesian mapping category and its actual ambient inclusion
without narrowing public `ProfMap` or `Prof_hom`. The source builder itself
records no checker outcome.

The selected `composition_profile_consumer.lp` passes with 207 positive and
49 negative controls, including inherited controls, in receipt
`20261013T075039Z-98116017d0a34ad282057ba7bf7a09b4` (4.798 seconds,
401,632 KiB RSS). The separate point-projection controls pass in
`20261013T075303Z-ac9d4de92ad5430d984f104314be0407` (5.111 seconds,
398,336 KiB RSS). These guarded 90s/2GiB checks retain subject reduction.
[The verification record](local_cart_prof_verification.json) pins all
authoring/output hashes, immutable receipts, warning comparisons and failures.
This is bounded local-view qualification; canonical Cartesian admission,
expanded presentation-map inverses, the whole raw reindex bridge and
production integration remain open.

The source pins in `local_cart_prof_inputs.json` identify the checked
`cart_action` copy and the checked raw represented-counit replay. The builder
also checks the exact output hashes against their verification records. It
takes the Cartesian copy only up to the first public Prof declaration, then
imports the raw replay's unchanged production owner closure. Its first
consumer uses the already separate implication-reindex comparison variant.
The globally Cartesian Prof declarations, structural Q universe and proposed
implication/conjoint collapse from the Cartesian donor suffix are excluded.

The new definitions are exactly:

```text
S(A,B) = Cart(T(A) x B,Cat).
include : S(A,B) -> Prof_cat(A,B).
QHom(A,B) = Cart(A,Cart(T(B),Cat)).
curry : S(B,A) -> QHom(A,B).
uncurry : QHom(A,B) -> S(B,A).
reindex(F,G) : S(A,B) -> S(A',B').
```

`S` and `QHom` are transparent aliases. The inclusion is the existing
`cart_functor_include`. The two presentation maps use existing Cartesian
precomposition by product symmetry followed by ordinary Cartesian curry or
uncurry. Their opposite order of endpoints agrees with the selected Q Hom
convention. The local reindex functor uses `Prof_reindex_base_func` and the
same existing Cartesian precomposition. No new classifier, runtime rule,
equality/path argument, supplied inverse or strictness parameter occurs in
these definitions.

The root agent's first guarded check failed while forming the inclusion:
`Prof_cat A B` did not unify with `Functor_cat (T(A) x B) Cat`. The receipt
is `20261013T072341Z-1b0014b321ac4a6d933b8681ef1cabd1` (4.982 seconds,
395,208 KiB RSS, 90s/2GiB defaults). Existing proof-time comparisons through
`Catd_cat` did not compose transitively. The separately owned
`local_cart_prof_facade.lpfragment` now proposes their direct raw-category
comparison, retaining both endpoint constraints. It never equates Cartesian
and raw mapping categories, and the operational inclusion body is unchanged.
`local_view.lp` and its identical `no_facade_comparison.lp` preserve the
exact failed target as a removal control. This direct comparison is a
candidate until separately checked; the proposed variants use distinct
`facade_*` target names.

The facade-view definitions pass the root agent's bounded check
`20261013T072819Z-e3c5f5151fcd4c21bee62ceb3c4b0577` (4.763 seconds,
396,856 KiB RSS). The first consumer then fails at the first curry fibre
formula (`20261013T072856Z-69924023c2684170b7cf44ee611ee5a1`): ordinary
evaluation is stuck under the Cat-valued `hom_precomp_along_fapp0` head.
The donor's original curry point control checks only this unreduced stable
expression. The adjacent covariant `hom_postcomp_fapp0` owner already has
its generic Cat-valued `fapp0` projection; its precomposition counterpart is
absent. `local_cart_prof_precomp_projection.lpfragment` proposes exactly
that ordinary composition-evaluation projection at the precomposition owner
position. The separate `point_*` targets first add it. It does not fold
whole composition, assert naturality or change a mapping profile.

The generic projection exposes a competing reduction of the existing Unit
curry representation. In receipt
`20261013T073247Z-4e3912bdd43f4cf8bf59ae8d57179917`, its capped
representation-action rule fails subject reduction because the new route
ends at `Unit_C o (Const_x,id_C)` while its old endpoint is `hom_(id_C,x)`.
The `joined_*` variants add the precise literal Unit/paired-section join
at the representation partial-evaluation owner, before the affected action
rules. This is the same whole represented Hom selected by the existing
`representation_projection.lpfragment`; its body and higher owners are
retained. The original failing point target remains byte-exact.

The joined first consumer reaches the later inclusion identity check before
failing (`20261013T073759Z-072736b69a5d49fbbf98091836a12939`). All preceding
raw-counit and local-profile controls pass in that run. The inclusion's
computed identity is at `Functor_cat(base,Cat)`; the proposed runtime RHS
used `Prof_cat(A,B)`. Their facade comparison is proof-time, so this runtime
assertion is stronger than that agreement. `joined_profile_consumer.lp`
instead proposes typed reflexivity observations for identity and composition
under the same comparison. These are reviewer assertions only; no path is
passed to an operational map. The runtime identity gap is retained in
`joined_first_consumer.lp` and its smaller standalone inclusion boundary.

The first-consumer controls cover shared objects, raw-map preservation and
rejection, the actual included arrow, whole Hom inclusion, a variable next
cell, presentation fibre formulas and the shared object reindexing formula.
A distinct inverse target tests the two object round trips and both
independently expanded variable-map round trips. Failure of an inverse
observation must be retained separately from type formation and component
success; this builder does not repair such a failure with an inverse axiom.

Build without invoking the checker:

```bash
python3 audits/strict-default-action-boundary/local_cart_prof_migration.py --check-authoring
python3 audits/strict-default-action-boundary/local_cart_prof_migration.py
```

The emitted files under `tmp/probes/local_cart_prof/` are, in dependency order:

1. `owner_prefix.lp`: checked Cartesian prefix plus raw Prof owner closure.
2. `local_view.lp`: only the new local definition bodies.
3. `first_consumer.lp`: the existing raw counit comparison variant and the
   new local controls.
4. `inverse_boundary.lp`: the four separate presentation inverse obligations.
5. `no_facade_comparison.lp`: the failed raw-facade comparison removal control.
6. `facade_view.lp`, `facade_first_consumer.lp`, and
   `facade_inverse_boundary.lp`: the corresponding proposed direct-facade
   comparison variants; the first consumer adds native inclusion identity,
   composition and endpoint/noncollapse controls.
7. `facade_reindex_boundary.lp`: the separate whole-object and included-map
   comparisons needed to connect local precomposition to `Prof_reindex` and
   `Prof_reindex_transf` in the actual represented counit construction.
8. The `point_*` counterparts add the proposed stable precomposition point
   projection; `no_precomp_projection.lp` is byte-identical to the failed
   `facade_first_consumer.lp` removal target.
9. The `joined_*` counterparts add the Unit partial-evaluation join;
   `no_representation_join.lp` is byte-identical to the failed
   `point_first_consumer.lp`. The `*_projection_controls.lp` targets check
   both identity cuts, precomposition accumulation and noncollapse.
10. `joined_profile_consumer.lp` uses typed inclusion identity/composition
    observations across the proof-time raw facade. The stronger runtime
    assertions remain in `joined_inclusion_runtime_boundary.lp`.
11. `composition_profile_consumer.lp` is the selected passing first consumer.
    `composition_projection_controls.lp` checks the point projection
    separately; `composition_inverse_boundary.lp` and
    `composition_reindex_boundary.lp` retain the stronger open obligations.
12. The `without_raw_facade.lp`, `without_precomp_projection.lp`,
    `without_representation_projection.lp`, and
    `without_composition_congruence.lp` targets each remove exactly one named
    fragment from the selected source. The earlier `no_*` aliases preserve
    their historical stage-specific failures.

The typed identity observation passes; the subsequent typed composition
observation fails in `20261013T074232Z-9010f5d9e98140e38e037432b2c9e42b`.
`comp_fapp0` is non-injective, and its existing sufficient congruence covers
two literal ordinary functor category endpoints, so the whole-category
facade comparison does not itself compare these opaque composite terms.
The `composition_*` variants add a local proof-time sufficient congruence
across raw Prof and ordinary functor facades, comparing all endpoints and
both actual arrows in side conditions. This cannot infer arrows from equal
composites. The failed `joined_profile_consumer.lp` stays byte-exact.

The separate inverse target passes both object round trips, then fails its
first independently expanded transformation round trip in
`20261013T075308Z-6e3dd3ef02d842059956cc0255ac8796` (4.989 seconds,
398,804 KiB RSS). The reverse transformation assertion is not reached.
The whole-reindex target fails its first whole-object comparison in
`20261013T075314Z-5978c7b66b124c6a97a327b428691c4b` (4.878 seconds,
398,568 KiB RSS); its included-map comparison is not reached. The passing
local fibre formulas do not discharge either failure.

The selected warning stream contains 879 normalized unjoinable critical
pairs versus 877 in the complete declaration stream preceding the facade
consumer failure. Exactly two pairs are added, with no removals: `sigma_Fst`
and `sigma_Snd` of Cat-valued stable precomposition evaluate a product-valued
functor before or after projecting it. Their exact term/reduct/rule blocks
and hashes are retained in the verification record as open projection-order
obligations. This diagnostic comparison is not a confluence certificate.
The strict inferred-slot audit reports zero unreviewed rule clauses.

All four exact single-removal targets fail at the intended dependency. Each
differs from the selected passing source only by its named fragment; the
verification record contains the exact input and log hashes.

| Removed fragment | Observed boundary | Receipt |
| --- | --- | --- |
| Raw-category facade comparison | Inclusion cannot identify its raw target with the ambient functor category. | `20261013T080213Z-8ecaa35c2e2b489b8fec8f95666ea682` |
| Precomposition point projection | The first curry fibre computation fails. | `20261013T080219Z-a87f659c4349497eaa8af121114d9a44` |
| Unit representation projection join | The inherited representation action fails subject reduction at its whole Hom endpoints. | `20261013T080224Z-e5b7fa5a9b64400aaac42905f15af773` |
| Raw-composition sufficient congruence | The typed inclusion composition observation fails. | `20261013T080229Z-4757250e0ad84417b9e03f7d9a5ed9eb` |

These checks use the normal guarded 90s/2GiB profile and take 4.616–4.960
seconds at 384,944–401,884 KiB RSS. They establish that each candidate
fragment is used by this bounded replay; they do not close the separate
inverse, whole-reindex or product-projection overlap obligations.

The checker must run serially through the repository guard with subject
reduction enabled. Source emission and Python authoring validation do not
qualify any Lambdapi declaration or assertion.

The canonical raw counit still has the existing closed-core body
`eval(reindex(lambda(coyoneda(Unit)),id,F))`. Its source owners return raw
`ProfMap`; the local inclusion runs in the opposite direction. Therefore
adding this local view does not derive Cartesian admission of that map. The
negative control for its implicit admission records the missing owner
qualification, not a mathematical claim that the canonical map is non-strict.
The next admission obligation must qualify the actual canonical co-Yoneda
and closed operations at their existing owners, or derive the corresponding
profile proof internally. Arbitrary raw maps must remain rejected, and no
second independent profunctor tensor/closed theory follows from this view.
The first-consumer fibre reindexing formula does not establish that last
whole bridge; the dedicated reindex target records it separately. Even a
successful classified lift would not make the original raw term acquire a
Cartesian type automatically, so its implicit-admission negative can remain
valid after such a lift is constructed.
