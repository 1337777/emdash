# Varying-base Pi frontend migration

Date: 2026-10-25. Focused/native and generic regression qualification passes;
complete TypeScript integration remains unfinished.

The frontend follows the actual native interface:

```text
Catd_cat_func : Op(Cat_cart) → Cat_cart
Catd_cat_func[K] = Cart(K,Cat_cart)
Pi_func(K) : Catd_cat(K) → Cat_cart
Pi_int_funcd[K] = Pi_func(K) ∘ Functor_cart_include(K,Cat_cart)
Pi_pullback_funcd(G)[k] = Pi_func(G[k]) ∘ Functor_cart_include(G[k],Cat_cart).
```

The input is `G : K → Op(Cat_cart)`. Cartesian diagram maps form the
varying-base source; fixed-base displayed maps and sections keep their lax
profile. The transparent `Catd_cat_func` body is the native `hom_con` body,
not a new primitive. The earlier `fapp0_func` declaration is reused.
The ordinary `Functor_cat` owners remain distinct. The complete component
composite and its inclusion survive the projection; the fibre computes to
`Pi(G[k],M)` through the inclusion's existing object action.

The native inclusion projection has wildcard inferred source/target slots.
Keeping those slots rigid in the transfer incorrectly blocked computation
when composition retained the proof-equal `Catd_cat` codomain. The corrected
transfer uses native wildcards with typed subject-checking witnesses; it does
not add a second fold or change runtime category equality.

## Required generic subject-checking integration

The old subject-proof path compared only the final inferred types. RHS
inference still demanded runtime conversion for every inner argument. The
native composite's inclusion therefore exposed a concrete missing capability:
`Functor_cat(K,Cat_cart)` must compare with `Catd_cat(K)` inside composition.

A per-rule `allowArgumentConversion: true` opt-in now permits closed RHS
argument comparisons using the existing checked proof program. The opaque
declaration extension is validated as before. Argument and final-subject
proof-rule IDs are combined and must exactly match the selected expectation.
LHS checking, ordinary Core checking and runtime normalization are unchanged.
Open local-binder comparisons are rejected by this path. No category-specific
branch, new equation, external oracle or operational proof payload is added.

The independent generic fixture demonstrates an inner argument mismatch,
its rejection without the opt-in, successful checking with exactly the named
proof rule, and retained runtime non-conversion. All16 generic runtime tests
pass. The Pi transfer has11 declarations/11 runtime clauses:9 direct subject
checks and2 checks using the existing category-presentation proof rule.
Six consumer/demo tests pass. The native test checks the emitted dependent
target, its computed fibre, both whole component composites, and the
non-identification of Cartesian and lax diagram categories. It passes with
warnings and subject reduction at60s/2GiB.

[Verification](foundation_frontend_pi_verification.json) records exact inputs,
failures and native evidence. Workspace, registration, typecheck and lint pass. The full TypeScript gate
stops while loading the unmigrated displayed-evaluation profile: its stable
Functor_catd fibre rule still uses Cat_cat and the former ordinary mapping
category. No whole-suite pass is claimed. The additional generic proof/mixed
and metadata scope passes45 tests, with one optional native test skipped.
Migrate displayed evaluation and the later Homd/mixed profiles before retrying
the full gate. The native kernel was unchanged throughout this slice.
