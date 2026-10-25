# Frontend integration of the strict-functor and duality migration

Date: 2026-10-25
Status: active source review; implementation pending
Owner: R14 of the [foundations plan](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Scope: migrate existing TypeScript consumers to the qualified native source;
no new mathematical profile, generic-checker redesign or resumed bulk transfer.

## Starting evidence

The native source promotion is checkpoint `57e627b9`. All 1,388 original
registered LP files have source-check coverage on the supported checker;
production health and final CI remain separate ongoing gates. The active
core hash is `70b7a550b6d932dcfca561300b3ac0cf37f28dfca14afc2429249141eff5182e`.

A fresh guarded `export -o lp` succeeds with that source and the supported
binary `94dc55766ec793e137cba7936f40e56074f4d92a02259cae8de9474c65e4677f`.
Its SHA-256 is
`5fe27c717a83f950431cf61a806a493499f3b03635310c63dcf3c9b751c327cd`:
2,111 commands, including 899 symbols, 11 inductives, 1,033 runtime-rule
commands and 153 proof-time-rule commands. Export acquisition is not a
TypeScript-transfer qualification. Exact local acquisition evidence is at
`emdash2/tmp/probes/kernel_boundary_continuation/fresh_canonical/`.

The focused baseline has 14 passing tests and one live-authority hash failure
in the generic declaration-compiler suite. The old dependent-target suite
passes against its old typed snapshots. That pass does not establish agreement
with the new native source. No source-pin check has been weakened or updated.

The [owner inventory](../emdash2/audits/strict-default-action-boundary/foundation_frontend_owner_inventory.json)
compares complete source commands for the names selected by 59 exported
transfer modules. Of 150 names, 92 symbol commands are unchanged modulo
whitespace, 54 changed, one disappeared, and three have no symbol command in
either source (inductive/constructor or local mirror). This is an inventory,
not 150 semantic qualifications. Prefix provenance can stay unchanged while
the declaration's actual type changes; review complete declarations.

## Migration order and acceptance

| Slice | Actual change to review and implement | Required evidence |
| --- | --- | --- |
| F01: shared categorical coefficients and directed telescope | Add the native `Cat_cart`/`Functor_cart_cat` dependencies through the existing generic transfer mechanisms. Migrate the Sigma telescope's coefficient and transport body. Retain public `Cat_cat` and ordinary `Functor_cat` as distinct owners. | Complete selected declaration/rule correspondence, generic compilation, actual telescope consumer, wrong-coefficient rejection, and native conformance. No new generic checker semantics. |
| F02: Cartesian structural operations | Evaluation, constant abstraction, exchange, diagonal and Cartesian curry/uncurry now use `Functor_cart_cat`. Adapt their existing consumers, preserving ordinary functor objects and the actual mapping-category distinction. | Existing structural/binder consumers and their projection computations; reject an unqualified lax mapping-category input where the native owner requires Cartesian maps. |
| F03: displayed families and varying-base sections | Migrate `Catd`, fibre/transport actions, displayed structure, `Catd_cat_func`, and the Pi ladder. `Catd_cat_func[K]` is Cartesian diagrams; fixed-base `Catd_cat K` still admits lax displayed maps. Pi's varying-base component includes those Cartesian diagrams into the fixed-base category. | Full existing dependent-target consumer with the actual inclusion, its fibre computation and higher-use boundary. Preserve lax section semantics and proof-time/runtime distinctions. |
| F04: corrected duality and dependent Hom | Migrate the existing mixed/action consumers to shifted opposite families, `TotalOp_catd`, and the new Homd root/section/index ladder. `Homd_target_section_catd` is removed; its old Pi presentation cannot be retained as an opaque alias for the new section category. | Whole transferred types, retained leaf/higher computations and inverse data; selected negative variance controls; actual native counterparts. No old profile silently relabelled as current. |
| F05: source acquisition and integration | Reconcile selected canonical ordinals, exact command hashes, policy/linkage and profile reviews after their semantics are migrated. Review affected extension pins individually. | Focused suites per slice; typecheck/lint; one full TypeScript gate after the changed shared boundary is green; affected bounded native conformance; owning integration gates. |

F01 begins with the existing generic continuation compiler and the current
`directed_1a_proposal.ts`/`directed_1b_proposal.ts` snapshots. Their Sigma
family parameter changes from `Const_catd K Cat_cat` to
`Const_catd K Cat_cart`. Do not globally reinterpret the existing
`category-of-categories` owner as `Cat_cart`. Additional native coefficient
declarations belong to the reviewed continuation/transfer data; the generic
LF machinery and frozen MVP boundary need no category-specific algorithm.

The first ordinary structural consumers are in
`categorical_structural_transfer.ts`. Their 15-declaration scope contains
six changed native commands. The old `Functor_cat` signatures of `Eval_func`,
`Const_func_func`, `sym_func_func`, `diag_func_func`, `curry_func_func` and
`uncurry_func_func` cannot be certified by changing a source digest.

For the dependent-target consumer, the required input is now
`G : Functor(K,Op(Cat_cart))`. Both `Pi_int_funcd[K]` and
`Pi_pullback_funcd(G)[k]` compose the fixed-base Pi functor with
`Functor_cart_include`. Preserve this whole composition; pointwise agreement
of family objects does not identify the diagram categories.

## Constraints

- Follow the native source and its existing migration outline. Do not add
  new Lambdapi rules to make an old frontend type pass.
- Preserve fail-closed source/command/profile checks. Update pins only for
  the reviewed selected scope, with exact canonical acquisition evidence.
- Distinguish definitionally equal spelling changes such as `Hom` versus
  `Obj(Hom_cat)` from actual coefficient, variance and transformation-profile
  changes. A raw text difference is not automatically a semantic difference.
- Preserve frozen-profile history; record the revised active continuation
  contract instead of silently granting a historical release broader scope.
- Reuse the generic LF compiler, runtime/proof separation and module linkage.
  Do not restore the retired category-specific feasibility API.
- Keep native checker runs serial with production health. If the dispatcher
  is briefly held for a needed acquisition, allow its current guarded child
  to finish, resume it afterward, and record that scheduling time separately
  from the child's actual execution receipt.
- Book/article revisions and legacy nerve integration remain subsequent
  stages of the consolidated plan.
