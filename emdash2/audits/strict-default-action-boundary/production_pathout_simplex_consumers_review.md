# Original PathOut, dependent-simplex and join consumers

Date: 2026-10-24
Status: qualified non-library continuation; production promotion remains pending
Predecessor: `bc97f7dd`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

This follows the [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md). Eight original owners and seven complete reviewers retain all 100 declarations and all 37 positive/six negative assertions. This is migration of existing work, not a resumption of the separate nerve-equivalence goal.

## Changes

The original whole PathOut transformation lift, dependent-simplex fourth-level observations, code/face constructions and join compatibility remain in their existing outline.

`join_map_extend_cross_component` now exposes the component returned by `tdapp0_fapp0` through the existing `strict_transfor` view. The component already has the classified strict-transformation type because its family coefficient is `Cat_cart`; the public accessor still returns the same ambient transformation type. No new profile argument or strictness premise is supplied by the caller.

`ordinal_join_terminal_func` uses the ordinary identity directly, removing its obsolete `strict_functor` view and `strict_identity` spelling. It is the same underlying map. Comments now distinguish the conventional pre/right-strict transfor leg from the retained post/left lax leg.

No primitive, rule, unifier, equality payload, extra proof parameter or new assertion polarity is introduced. The supplied whole `join_map_extend_cross_beta` remains supplied, and its shaped/base-action observations remain derived. The dimension-four module still retains its residual frame; this tranche does not claim a fully flattened top filler, new eta law, complete decoder or equivalence.

## Evidence

| Scope | Receipt | Result |
| --- | --- | --- |
| Untouched originals over the current foundation | `20261024T184352Z-0a0bb2220454428f9e8c3071c44731c5` | Passes PathOut/simplex owners; stops at classified versus ambient join-cross component. |
| Existing ambient component view | `20261024T184629Z-89d8592b11944c1b8b202b4f9dcd81fb` | Passes the component; reaches the retired functor wrapper. |
| Complete adapted original group | `20261024T184854Z-fcbe724a9245415e9d5d7fc9d1231204` | Passes all fifteen files. |
| Final emitted group | `20261024T185459Z-bc0117d1255c48a4bcfdf74627426789` | Cold pass, 51.166s / 187,608 KiB under 90s / 2 GiB. |

Checks retain subject reduction, `o=20,v=1024`, serial execution, file limits and no-swap containment. No compiled objects participate. The source-pinned recipe rejects changed baseline inputs; all emitted files match it. The eight owner LHS audits report no unreviewed generic inferred-slot candidates. All 1,670 warning occurrences are within reviewed contexts. No warning-silencing rule or global confluence claim is added.

The [verification](production_pathout_simplex_consumers_verification.json) carries all 1,180 predecessor inputs unchanged, together with the parent verification hash and its evidence chain. The added source closure checks fresh. The result covers 1,140 original LP sources (728 core/library and 412 complete reviewers), 1,196 qualified inputs, and 4,878 positive/711 negative assertions.

Remaining: 63 core/library files and 184 reviewers, five terminal Homd runtime obligations, R07/R12 and production qualification. Unrelated work remains excluded from this checkpoint.
