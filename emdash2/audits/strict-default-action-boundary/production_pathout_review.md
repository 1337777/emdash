# Moving PathOut families and full staged-core check

Date: 2026-10-16
Predecessor: `6788b36c`
Status: the complete emitted core and focused inherited/PathOut consumers check; profile-extension and downstream migration remain incomplete
Owner: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_pathout_verification.json)

## Canonical formation profiles

The existing PathOut_cat_func is now the actual composite of hom_int(id_Z)
and Sigma_coeff_func(Z), with type T(Z)->Cat_cart. Its total objects and
transport functors are the same original constructors. This supplies the
profile required by the already selected varying-base motive classifier:

```text
PathOutMotives_Z[x] = Cart(PathOut_Z(x),Cat_cart).
```

The existing Pi_func(K) now lands in Cat_cart. Its intended construction is
the terminal-source Hom of Catd(K), so its formation has the canonical
represented-Hom profile. This changes neither the section objects nor the
maps admitted by Catd(K): Pi still uses the default lax terminal-source
transformation category and Pi_func still accepts general lax displayed
maps. No second Pi operation or strict-section classifier is introduced.
Pi_int_funcd, Pi_pullback_funcd and the existing section-pullback comparison
use that same formation target. Their components restrict motive parameters
through the existing Cartesian-diagram inclusion.

The source uses the established structural Pi owner and its projections;
this checkpoint does not claim to derive a new whole Pi/Hom inverse theorem
from object agreement alone. The original general-map section postcomposition
and nonidentity constant-section controls remain in the checked suite.

## Moving and fixed-source path induction stay distinct

The fixed-source PathInd_func still has its ordinary lax displayed-map
interface over all admitted motives. The moving package's component is its
restriction to Cartesian motive maps. Its ordinary view is computed through
the existing prewhiskering operation and the original PathInd_func; there
is no new eliminator or separately supplied coherence cell.

The [migrated original section](production_pathout.lpfragment) keeps the
same path_ind_sec, path_ind_func_fapp0, PathInd_transfd and PathInd_funcd
owners. Both the direct moving telescope and the Sigma-total observation
compute to path_ind_func_fapp0 at (x,E), then to path_ind_sec at u. The
fixed-source theorem is not promoted to StrictTransfor on arbitrary lax
motive maps; a negative control checks that distinction.

The motive-transport alias now uses its actual whole Pullback_catd body.
A proof-time comparison against the internal motive action is restricted
to the concrete Sigma_coeff_func o hom_int constructor. An attempted
generic Cart-valued precomposition comparison interfered with the earlier
Pi dual-action consumer and was not selected. No runtime expansion of all
represented precomposition or supplied equality argument is introduced.

The existing path-category transport/J comparisons now use the admitted
coefficient's literal-reflexivity identity view. Fibre covariance enters
ordinary displayed slots through its existing strict_transfor inclusion.
The original transitivity reviewer still computes to represented
precomposition and ordinary composition. Nested telescope negative sections
now use total fibre duality over R(K), consistently with Hom_catd.

## Unit computation at the original Hom-action owner

The original Eckmann–Hilton unit proofs exposed identity whiskering after
composition had projected to comp_prod_fapp1_fapp0. The selected
[unit computations](production_identity_whiskering.lpfragment) return the
other actual 2-cell only when the whiskering 1-cell and its 2-cell are both
literal identities in the same category. They are ordinary identity
whiskering, not an interchange theorem or a strictness rule for arbitrary
transformations. Controls retain an independent nonidentity 2-cell in either
coordinate.

A broader proof-time candidate with a variable result caused allocation
failure before reaching the consumer, under the normal o=20/2-GiB profile.
It is not selected. The constructor-guarded runtime rules check under the
normal limits and preserve the inherited constant-section and lax-map
noncollapse controls. No resource-limit increase was used.

## Evidence and next integration boundary

The entire emitted emdash3_2.lp now checks, including its original later
equality/skeleton section. The separate full-core-plus-controls target also
checks: it includes all inherited foundation, Homd, comma and profunctor
controls, the moving PathOut consumers, the original transitivity reviewer,
and the new profile/noncollapse controls. Subject reduction and warnings
remain enabled, with the serial 90-second/2-GiB, 64-MiB-file profile and
OCAMLRUNPARAM=o=20. The strict LHS audit has no unreviewed compound slots.
Exact input hashes, receipts and warning changes are in the verification.

This is a full staged-core result, not production promotion or complete
migration qualification. The staged examples/gray_profiles.lp run next
failed inside emdash3_2_gray_profiles.lp at
strict_functord_transport_rhs_tele_path: it still applies Cat_cat and
Functor_cat annotations to the now-Cartesian family/action interface. That
failure was observed before the final comment-only source cleanup; its
receipt preserves the exact older snapshot. The final core and consumer
receipts cover the final source bytes.

Continue with the profile module's actual displayed-map consumers, then
the remaining extension/diagnostic dependency closure and retirement of
redundant strict-functor wrappers. Preserve genuine strict-transfor profiles
and default lax transformations. Public source promotion, current
catalog/health/CI qualification and remaining consumed compatibility checks
are still required. The separate application goal remains paused.

Replay from emdash2:

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py \
  --package-root tmp/probes/production_owner_migration/package \
  --no-colors --quiet emdash3_2.lp
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py \
  --package-root tmp/probes/production_owner_migration/package \
  --no-colors --quiet pathout_controls.lp
```
