# Frontend Cartesian coefficient and Sigma telescope

Date: 2026-10-25. Status: qualified focused implementation; full frontend
migration and integration gates remain open.

The existing continuation now includes `Cat_cart` as one native opaque
declaration. It retains the separate public `Cat_cat` owner and the frozen
MVP. The Sigma telescope parameter, its transparent transport body, fibre
decoding and section evaluation use the migrated coefficient. The earlier
20 + 9 declaration / 10-rule continuation becomes 20 + 10 / 12 rules.

The two added runtime consequences are:

```text
τ(Obj Cat_cart) → τ(Obj Cat_cat)
τ(Hom Cat_cart A B) →* τ(Functor A B)
```

They use the existing native object/Hom projections and transparent
classifiers. They do not identify `Cat_cart` with `Cat_cat`, or Cartesian
mapping categories with lax mapping categories. A new consumer rejects a
`Functor K Cat_cat` where an admitted `Catd K` family is required.

No generic LF checker, runtime compiler, proof engine, intrinsic Core owner
schema or frozen MVP changed. The retained older catalog adapter needed
nullary reference construction/matching for the new constant; generic transfer
already supported that form. Generic and catalog declarations and all twelve
runtime rules agree, including their existing near-miss controls.

The historical review decisions remain identified as historical provenance.
`foundations_migration_authority.ts` records the later user-authorized
migration and its native checkpoint separately. The active continuation
manifest is recomputed from the revised data; no older approval is claimed
to have approved the additional coefficient in July.

Validation:

- Focused consumers: 49 passed, with four opt-in native checks skipped.
- All four native checks separately pass: nested telescope, total transport,
  combined section evaluation, and rejection of a mismatched section family.
  The failed checker receipt for the last case is the expected rejection,
  not a timeout or accepted source. Subject reduction remains enabled.
- Metadata/review scope: 85 passed. The combined 150-test scope has 145 passes,
  four native opt-in skips and one obsolete expected opaque-declaration count.
  Correcting that expected count from eight to nine passes its focused replay;
  the other results are carried forward rather than repeated unchanged.
- Root typecheck and changed-file lint pass. The two selected continuation
  source/export/version pins are updated after native conformance. Reversing
  only those three literal metadata updates reproduces the native-run source
  hashes; no mathematical TypeScript body changed after that run.

[Exact verification](foundation_frontend_coefficient_verification.json)
retains the source hashes, manifest counts, native receipts and validation
scope. This does not update or qualify the remaining structural, displayed,
Homd or scale-acquisition profiles. Their source pins remain review signals.
The next consumer is the native Cartesian structural mapping category in
`categorical_structural_transfer.ts`, as recorded in the
[frontend subplan](../../../docs/EMDASH_FOUNDATIONS_FRONTEND_MIGRATION_PLAN.md).

The required broader `check:ts` attempt passes workspace validation, test
registration, typecheck and lint, then stops during test-module loading at the
still-unmigrated `Fibre_func` declaration in `categorical_dependent_transfer.ts`.
No complete TypeScript test pass is claimed. The next local edit changes that
declaration's fibre coefficient to `Cat_cart`; its two-owner transfer and
dependent-composition successor compile, but its source-pin/consumer
qualification remains a separate continuation. That in-progress edit is
excluded from this coefficient/telescope checkpoint.

The serial native-validation window also rechecked affine glue with the
same 3GiB memory cap and a 180-second deadline. It passed unchanged in
82.590s/637,388KiB, below its original 90-second limit. The earlier 90-second
timeout remains recorded; no registry/resource-policy change is justified by
these two observations alone. Retry that original failed health target after
the current run. The dispatcher is resumed, and its held target's child
receipt retains the actual checker time independently of scheduling delay.
