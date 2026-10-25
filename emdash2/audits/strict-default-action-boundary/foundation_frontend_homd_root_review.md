# Native Homd target, relative root and higher-action frontend

Date: 2026-10-25. This source-defined target/root and next-Hom interface slice
is qualified; the lower Homd/mixed frontend migration is still incomplete.

The former Pi/edge/presheaf body of `Homd_target_catd` is replaced by its actual
native Q-valued construction. Its checked body uses `Homd_coeff_diagram`, the
represented package, ordinary represented Hom and `CoAt2_func`. The native
relative root keeps its actual target-index annotations:

```text
R_D = Homd_target_index_func(K)[Homd_coeff_diagram(D)]
homd_rel_cart_int(FF) = Homd_target_map(FF) ∘ homd_id_int(E)
homd_int(FF : Functord D E) : Functord E R_D
```

`homd_int` is a checked defined ordinary view of that composite. It is no
longer an opaque injective primitive or a map out of `Op_catd(E)`. General lax
FF remains admitted. The three existing higher-action owners now target the
native transformation **from the relative composite to the identity root**.
Their generic object and whole-Hom projection rules are retained, and the
rich frontend reports those actual endpoints.

The source-prior duality fragment transfers the existing `CoAt2_cat` and
`CoAt2_func` signatures with five native projections. The independent Op,
Cartesian Hom and shifted-family utility types are updated to their actual
native profiles. `Op_funcd` now has its native strict-map carrier; the higher
Homd action no longer tries to apply it to an arbitrary lax FF.

## Computation and dependency ownership

Existing Cartesian precomposition already computes to ordinary functor
composition at the identity-family head. Transferring its existing object
projection sequence before the relative definitions lets the generic checker
validate their actual target-index annotations. No new proof comparison or
generic checker capability was needed. `hom_precomp_along_fapp0`, identities,
fixed evaluation and Cartesian views reuse their earlier qualified owners.
The relative roots are checked after the source-prior signatures and native
projection rules, following the repository's existing staged transfer pattern.

The foundation has23 declarations:10 checked bodies and13 signature views,
with four local runtime clauses. The higher layer has three declarations and
two projection rules. `Homd_target_con_func` remains an explicitly
signature-only view of a native defined operation; this slice does not qualify
its full action or claim the lower y/v/f ladder and leaf computations are
transferred. Those remain part of F04 and must use their actual native bodies
and index classifier, not the retired Pi presentation.

## Evidence and remaining integration

Sixteen focused interface/consumer tests pass. Two native tests independently
check the whole dual map and variance, all selected declaration types and
implemented bodies, the actual emitted whole/next-Hom consumer, and rejection
of general FF at the stricter transpose carrier. They retain warnings and
subject reduction under60s/2GiB. The initial emission missed an earlier Catd
backend reference; using the complete authoritative linkage fixes the fixture,
without changing mathematics. [Acquisition](foundation_frontend_homd_acquisition.json)
pins current canonical declarations separately from historical D-019/D-021
records. [Verification](foundation_frontend_homd_root_verification.json) records
exact inputs, receipts and the unresolved boundary.

Workspace, registration, typecheck and lint pass. The complete TypeScript gate
now stops at the old same-base opposite-section type in mixed-nest `Hom_catd`.
That owner, the lower Homd computations and remaining profiles must migrate
before whole frontend qualification. The native kernel was unchanged.
