# Delayed Hom inversion and the whole native u-action type boundary

Status: the selected non-library `precomp_selected.lp` passes the actual
direct/full/capped native u-action controls, derived h-parameter family and
higher-action formation, and tested identity/composition observations. It is
not promoted. The h-family is an actual composite; no theorem identifies it
as a whole functor with the ordinary precomposition family. The initial
`delayed_cat.lp` pass and all failed variants remain separate evidence below.

## Observed discrepancy

The initial `fullcap_source_controls.lp` passes the actual source action
after applying it to an arbitrary nonidentity h. In contrast,
`normalized_leaf_law_controls.lp` fails its first whole-functor comparison:
the checker reports u0 versus u1 while comparing these domain categories:

```text
Hom_cat (Op_cat A) u1 u0
Hom_cat A u0 u1
```

The existing opposite rule makes these categories convertible. Their direct
equality passes diagnostic D1. Diagnostic D2 then reproduces the type failure
for an arbitrary `F : Functor (Op_cat A) B`, without any Homd symbol:

```text
fapp1_func F u1 u0
  : Functor (Hom_cat A u0 u1)
      (Hom_cat B (F[u1]) (F[u0]))
```

Thus the issue belongs to generic Hom-category inversion, not the
`homd_id_src_func` projection. The passing capped result omits the source
Hom-category from its final type and does not establish the whole-action
type comparison.

## Exact checker source

The inspected source checkout is
`/home/user1/.opam/default/.opam-switch/sources/lambdapi`, at clean commit
`db4f7809961b8c107247613067fb567491fb0b84`. This matches the checker revision
in the receipts; the different checkout listed in the local resource index
was not used for this diagnosis.

The receipts report binary
`/home/user1/.opam/default/bin/lambdapi`, version
`3.0.0-90-gdb4f780`, SHA-256
`ab493adeb0d79e58fa16c0965e1cb0e5194e212093119dc58f8e401f326c2c0a`.

Paths below are relative to that exact source checkout.

| Primary source | Relevant lines | SHA-256 |
| --- | --- | --- |
| `src/core/unif.ml` | 174–182, 339–349, 374–412, 434–436 | `61868480435de922c6dc0534ff0cefde4d7ffe0d2f73c22164f703130ae60d55` |
| `src/core/eval.ml` | 121–186 | `88f732a7fb911b0f77f09f420f0ce390a64d092f6dcfe5c7869f80775a6be8b3` |
| `src/handle/query.ml` | 215–237 | `a98bc19eadd43f2cc37a67af831fdb4514a7660fab599f40300794bc91d947db` |
| `doc/commands.rst` | 454–462, 544–558 | `62a2dc60d39aaee3d26e8989b597c238b939e5200dce5f05d490ade80ac798cb` |

A conversion assertion first infers both term types and unifies those types
before comparing the terms themselves (`query.ml`). The unifier initially
uses `NoRw` and `NoExpand`; equal injective heads are decomposed immediately
(`unif.ml`, lines 374–412). User-defined rewrite normalization follows only
in the later branch, lines 434–436.

With `Hom_cat` declared injective, the unifier therefore splits the two
displayed domain categories before applying opposite reversal. It creates
the erroneous endpoint problem u1=u0. Term normalization can still reach the
correct common action head: that does not repair a failure in the earlier
type-unification stage.

The `injective` property is a trusted argumentwise inversion instruction,
not merely a normalization hint; the checker documentation leaves its
verification to the user. The existing equation
`Hom_cat (Op_cat A) x y ↪ Hom_cat A y x` prevents using that unconditional
argumentwise inversion before normalization.

## Why removal alone is insufficient

The tested `noinj_cat.lp` changes only `Hom_cat` from injective to an
ordinary symbol. It fails subject reduction before reaching Homd, at the
existing off-diagonal postcomposition action rule
`tapp1_func(hom_postcomp_tele_transf(...))`, lines 11214–11283.

The final unresolved constraint compares two Hom-categories with the same
outer category. Their endpoints are respectively raw composites and stable
`hom_postcomp_fapp0` terms. The existing endpoint comparisons could solve
those endpoint constraints, but removing native inversion leaves no rule
that exposes them from the whole residual Hom-category constraint.
The checker ends with `Unable to prove type preservation`. This is a genuine
regression of the removal-only source, not a negative control or a reason to
disable subject reduction.

The passing candidate retains the ordinary declaration and adds a sufficient
residual inference branch at the existing Hom owner:

```text
symbol Hom_cat : Π (A : Cat) (X_A Y_A : τ (Obj A)), Cat;

unif_rule Hom_cat $A $x $y ≡ Hom_cat $B $u $v
  ↪ [ $A ≡ $B; $x ≡ $u; $y ≡ $v ];
```

For a noninjective head, the checker reaches rewrite weak-head normalization,
then tests full convertibility before invoking custom unification
(`unif.ml`, lines 339–349 and 174–182). Hence the opposite case converts
before inversion. Residual ordinary Hom-category comparisons still expose
their endpoint constraints, restoring the existing postcomposition
subject-reduction proof. The branch supplies sufficient constraints to
solve a residual inference problem; it is not a new runtime equation or a
global semantic claim that arbitrary Hom categories determine their inputs.

The existing `Obj(Hom_cat(...))` inference helper is unchanged. The
`Hom` facade remains injective in this candidate; its direct opposite-type
boundary is a separate test, not covered by this declaration change.

## Exact run evidence

All targets below are under `emdash2/tmp/probes/homd_u_action/`; receipts
and logs are under `emdash2/logs/check-runs/`.

| Target | Result | Receipt id |
| --- | --- | --- |
| `fullcap_source_controls.lp` | Pass: capped formation and both source-action projection orders | `20261013T174709Z-acf7f2ed70614402b5c57cf36180d6f7` |
| `normalized_leaf_law_controls.lp` | Failed positive: first whole-functor type comparison | `20261013T174813Z-e28bb5ef6c4d48b0b40be51a8bdb9b93` |
| `type_boundary.lp` | D1 passes; D2 fails before D3/D4 | `20261013T175257Z-51412546f6624eed97f5d89e37eb0d1b` |
| `noinj_cat.lp` | Failed subject reduction at existing generic postcomposition | `20261013T175402Z-ef19304662ca4ddeadf6f21b8d171d9b` |
| `delayed_cat.lp` | Pass: full owner prefix and D1–D4 | `20261013T175502Z-662eb96e6e0b48d5bc5efe226c25e569` |

The successful D1–D4 cover the actual opposite Hom-category conversion,
generic whole `fapp1_func` type, concrete Homd whole expected type after
source/target projections, and typed whole equality with
`homd_id_u_func` in the shared classifier. This is a whole-functor consumer,
not a capped surrogate.

The delayed candidate uses the default 90-second/2-GiB profile; it passes in
12.473 seconds with 682708 KiB maximum child RSS. The removal-only target
fails in 2.551 seconds with 161032 KiB maximum child RSS. No checker was run
as part of writing this note.

| Evidence | SHA-256 |
| --- | --- |
| `fullcap_source_controls.lp` | `f4d4dabf9bfdc2b5fc31323d76cabe942219c692d25ac30817f7dd6379608e7e` |
| `normalized_leaf_law_controls.lp` | `7411f6b64e1c6016552bb5fa284998dd24f316d19461fc500e69824f847bb7c9` |
| `type_boundary.lp` | `a8548ab1d5f45604a683f4ab9b2692fc749df194b5f5087eda8f0159c7f8aadd` |
| `noinj_cat.lp` | `55055b035c357e2464488c07a859f97ab2dfcb3eef66829e2c2a99fcf5169704` |
| `delayed_cat.lp` | `39a51162609540eb4db66f0a04f37ac41562a7a22d0a5a44fc0b44ddf7833e59` |
| removal-only receipt JSON | `4ac73b0e80476bb302bd4624da990094d8f2f14e3c45f5de74867e8c46e6a1b9` |
| removal-only checker log | `31ac99894cca1d876ebb3b510f915c7a5124ebe17cd48676bd999c7e4455e146` |
| delayed candidate receipt JSON | `078aba4e3875a6c0e2062b3764a3afe47d3dd03786dbe48525c3c1f29bd458de` |
| delayed candidate checker log | `8eae43865b417b987c0af578b8312c946dbed6922fc064f81d16e1eab7d243f0` |

## Follow-up facade boundaries

The later `facade_type.lp` run retains the passing delayed Hom-category
candidate. Its generic `h : Hom A u0 u1` observation at
`Hom (Op_cat A) u1 u0` passes, but its subsequent direct concrete capped
Homd observation fails at lines 18794–18799. Receipt:
`20261013T175607Z-8efc08a4a1d44000b17e41e7b0fb6e9f`.
This distinguishes the generic facade observation from the concrete cap;
neither the earlier full/capped pass nor D1–D4 settles this boundary.

`delayed_facade.lp` additionally removes injectivity from the `Hom` facade.
It fails subject reduction at the existing identity-family postcomposition
telescope composition rule, lines 7836–7852. The residual problem is
`Obj(Transf_cat A B F G)` against `Obj(Hom_cat C X Y)` with an unknown
composition category. Receipt:
`20261013T175648Z-419196def558405b917ae4728333aceb`.

The subsequently retired inference candidate reconstructed the ambient
functor category from that mixed pair of residual heads:

```text
unif_rule Obj (@Transf_cat $A $B $F $G)
  ≡ Obj (Hom_cat $C $X $Y)
  ↪ [ $C ≡ Functor_cat $A $B; $X ≡ $F; $Y ≡ $G ];
```

This is a sufficient inference branch of the existing
`Hom_cat (Functor_cat A B) F G ↪ Transf_cat F G` computation, not an
injectivity claim. Its category condition retains the ambient `Functor_cat`
profile and does not admit a raw transfor into `Functor_cart_cat`. However,
it commits to the wrong presentation when the residual category already has
another valid representation. With the early existing Obj/Transf helper,
`delayed_early_complete.lp` passes the earlier subject-reduction point but
regresses the inherited Pi/constant-family comparison at lines 10704–10708:
it forces `Functor_cat K A` against
`Transf_cat K Cat_cat (Const_catd K Terminal_cat) (Const_catd K A)`.
Receipt `20261013T180058Z-ec5f749e4ccc452290aa4975bd831591` records that
failed positive. The broad mixed-head bridge is retired and is absent from
the selected source.

The facade target source hashes are respectively
`0332f03fe1b7f74ec0e32c127b719b4a36509154eb3f274b976c709eac0e0d9d`
and `462e09f71066a99802d3b2e04971db42ec97fbf6841b14130d40c5639d8455b5`.
Their checker log hashes are respectively
`9a7615cb9d98b5e72a62a8cfea68cc3e47bbe782892f4435aa0a62a4d4a1a3b1`
and `92442bed1f1e1bcb19374dcb8cd3645c9b0b4a35480888a254f918e50853a483`.

## Selected explicit-index successor

The native trace from `facade_debug.lp`, receipt
`20261013T175834Z-6383933757614a6d9adc5d38176febeb`, shows the concrete cap
failure with unresolved implicit base arguments in `Fibre_cat`. Its final
constraint contains distinct metavariables in those base positions before
premature `Hom` endpoint decomposition produces u1=u0.

`explicit_fibre_facade.lp` keeps `Hom` injective and uses explicit
`@Fibre_cat K E x` base indices in the diagnostic. It passes, including the
direct concrete cap, with the delayed `Hom_cat` correction alone. The
implicit-facade form remains a failed authoring/inference boundary; it is
not repaired by a generic reverse bridge.

`normalization_laws.lp` then passes the original native direct/full/capped
u-action controls and laws with the new consumers' fibre base indices
explicit. The original whole h-family definition is retained as an actual
composite of generic evaluation, Cartesian inclusions and source action;
its application and higher-action formation pass. This does not identify
that composite with a whole precomposition functor by extensionality.

`normalization_all.lp` adds the two-factor leaf observation and fails at
lines 18935–18943: precomposition along `E[f]` applied to a composite is
stuck against two nested precompositions. `precomp_default.lp` restores the
two formerly identity-only accumulation rules to general default-strict F,
at both functor and point levels. It gets past the two-factor observation
but fails the new fully implicit ambient-transfor composition diagnostic at
lines 18975–18977. The selected variant writes the actual category and
endpoints in that diagnostic:

```text
@comp_fapp0 (Functor_cat A B) F G H eta epsilon
  : τ (@Transf A B F H)
```

`precomp_selected.lp` passes. Its selected differences are exactly:

- ordinary `Hom_cat` plus delayed same-head inference;
- retained injective `Hom` with explicit fibre base indices in new consumers;
- the two general precomposition accumulation rules justified by the selected
  strict-default F interface;
- explicit ambient composition category/endpoints in the new diagnostic.

No mixed Obj/Transf inverse bridge or Homd-only conversion is selected.

| Target | Result | Receipt id | Source SHA-256 |
| --- | --- | --- | --- |
| `delayed_early_complete.lp` | Failed inherited Pi comparison; retired bridge | `20261013T180058Z-ec5f749e4ccc452290aa4975bd831591` | `dd9a2a7a784a28c54e32c3a54c45a5f833e5ba3bb16a8973dc8e8c1c1397823f` |
| `explicit_fibre_facade.lp` | Pass | `20261013T180223Z-0a2830d11a624e388d82c7abf79f0b2c` | `4a3040b4c6e885e7b4ff3ad8f228c87be1136246b931e8f00769090a00ccd3e9` |
| `normalization_laws.lp` | Pass | `20261013T180330Z-88fed9a5cdb04a009067f901ca2d5d6a` | `ff1bafd5248f8f7f9ce4c31c390c9635cff77b4605260e8d266d5485b227a90d` |
| `normalization_all.lp` | Failed two-factor precomposition observation | `20261013T180447Z-b23d1c7e4f7c4b09a7f1fbb255b776e8` | `440f8f241fe12da103ace8e380d004330b6f322d57a27f8cbbc22bb351553a39` |
| `precomp_default.lp` | Failed fully implicit ambient composition | `20261013T180626Z-858c50d128fb4cf7bef88a38c8931f84` | `8d7c55f685e48a12dc72a699c2003a2bc1ed65aeae3fdd5092df158884615968` |
| `precomp_selected.lp` | Pass | `20261013T180722Z-53aff743905a4303bdc6a7fbbb99bc2b` | `fecdf8984e2243aec9c458c4b79174cfc2fd0ac927d9fe15841bc42cf17a073d` |

The selected run completes in 13.784 seconds. Its log SHA-256 is
`f266b402041d77649f5860ddd167078b6a22eada8e10b6b3b628d64d1f2e778d`.
Source/log hashes were read and verified against the receipts without a new
checker run. Warning comparison and promotion remain separate work. The
provisional Q/global Cartesian Prof profile and remaining Homd/lift
coherence boundaries are unchanged by these bounded observations.
