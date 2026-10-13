# Identity Homd owner and derived relative interface

This non-library owner-position migration starts from the pinned cart_action
source. It changes semantic ownership in a copied core, not production.
The [builder](homd_identity_migration.py) never runs Lambdapi; the
[verification record](homd_identity_verification.json) records exact checked
inputs, logs, settings, controls and warning differences.

The primitive package is `homd_id_int(E)` with direct x/u/y/v projections.
Its final f-indexed value is the early defined `homd_id_` leaf, using the
existing ordinary Hom and fibre transport. This early definition preserves
Sigma's source-order dependency without defining identity Homd through a
general-FF primitive. The old downstream identity aliases are replaced by
the earlier identity projection owners, rather than duplicated.

The public relative root has an actual body:

```text
homd_int(FF : D => E)
  := Homd_target_map(FF) o homd_id_int(E).
```

Its upper ladder names are defined observations of this whole composite.
The existing fixed-endpoint `homd_` helper substitutes the strict component
`FF[y]` into `homd_id_`. No general-FF Homd rewrite law or strictness witness
is introduced. Agreement of the whole relative projection with that helper
is a separate composition diagnostic; the user explicitly excluded a
complete relative normalization theory from identity-milestone acceptance.

The selected prefix passes 261 positive and 48 negative controls including
inherited tests. New controls observe the identity root through its entire
ladder, its directed 2-cell index action, and identity specialization of the
defined public root. Negatives reject the reversed index direction and
implicit strict-transfor classification of both arbitrary FF and the
identity root. Removing the first identity projection fails the leaf
computation. This does not infer strict naturality from identity ownership.

The normalized unjoinable-pair inventory is 952 before and 950 after, with
no added blocks; exact removed blocks are retained in the verification.
The static strict LHS audit has zero unreviewed clauses. All actual checker
runs retain warnings, subject reduction, the serial 90s/2GiB guard and the
recorded OCaml runtime profile. These checks do not establish confluence.

The complete copied source still fails at the pre-existing intrinsic-action
declaration requiring same-profile `Op_funcd` of raw FF. The identity split
does not give that map a strict-transfor type. The coefficient Q and its
contravariant represented lift also remain provisional dependencies. Thus
the passing direct identity ladder does not complete the foundational goal.

Replay from `emdash2`:

```bash
python3 audits/strict-default-action-boundary/homd_identity_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/homd_identity/selected_prefix.lp
```

The builder also emits `without_identity_projection.lp`, `full_source.lp`,
the former `legacy_ladder_boundary.lp`, and optional `relative_boundary.lp`.
Only the first two have checked failure receipts in this tranche; the latter
two remain separately unqualified. Replay after changes to the primitive
ladder, its leaf, target action, category/transfor projections, Q/lift owners
or the intrinsic-action dependency. Source-pin changes require review.
