# General lax-FF Homd frontend endpoint

Date: 2026-10-26. Continuation of `3779a156`; native source is unchanged.
The [acquisition](foundation_frontend_homd_relative_acquisition.json) pins the
existing native owners and computations used here. The
[verification](foundation_frontend_homd_relative_verification.json) records
exact input snapshots and the final execution results.

## Actual relative construction

The TypeScript consumer starts with an arbitrary
`FF : Transf(K,Cat_cart,D,E)`, constructs `homd_int(FF)`, then observes its
source component, whole y-section, target functor and presheaf. The presheaf
agrees with the public `homd_` endpoint and its f-value computes to:

```
Hom_E[y](E[f](u), FF[y](v)).
```

Each rung is inferred independently in the existing generic checker. The
test also rejects applying the strict-transfor inclusion to this arbitrary
lax FF. Thus the relative test does not obtain its computation by replacing
FF with an identity or requiring a stricter input. The independent identity
root test and wrong-family rejection remain.

The computation follows the native owners: represented Hom action,
Cartesian prewhiskering, dimension-two-dual precomposition, composition with
the canonical mate, ordinary transformation components, and right represented
composition in Q. The last operation is ordinary source reindexing of the
curried coefficient. No general profunctor composition library or new
mathematical equation is introduced.

## Transfer ownership and rule review

The shared precomposition fragment now also carries the native represented
Hom and postcomposition action ladder needed by this consumer. It is
installed before mixed Homd. Later prewhiskering consumers reuse that
declaration/runtime prefix; their existing identity-family proof comparison
is checked at their actual extended declaration prefix.

Two represented-source declarations and four projection rules previously
owned locally by PathOut move into the shared fragment, preserving their
old Core names. The transparent Transf-classifier projection moves from
PathInd to the same earlier layer. The remaining library code consumes these
owners once. Dependency entries, name routing and local rule-group numbering
are updated for the relocation. Historical approval snapshots remain frozen.

LHS inferred-slot annotations retain the actual stable postcomposition
endpoints instead of assuming their raw-composition spelling. The mate
precomposition rule likewise uses the native inferred diagram slots and
recovers the families from the mate constructor. Neither change installs
runtime equality between arbitrary presentations. `Homd_coeff_rep_func`
receives its actual checked definition; its stable represented object is
retained for the native Q composition cut.

No generic checker case, operational equality-proof argument, supplied
comparison cell, global naturality equality or native kernel rule is added.

## Evidence and remaining boundary

The initial symbolic general-FF endpoint reaches equality in986 steps. The
actual typed root-to-leaf consumer then passes in the mixed frontend suite.
Native conformance checks33 positive assertions and two negative controls,
including both whole ladders and rejection of strict FF admission.

The first native whole lambda comparison for `Homd_coeff_rep_func` failed
inferred-type unification. The exact body checks under an explicitly typed
temporary alias, and its whole function equality passes. The native emitter
uses that form; this is an audit observation, not a new operational owner.
The successful guarded replay takes42.619s and169,032KiB at90s/2GiB with
subject reduction. Its1,886 imported warning blocks are unchanged from the
preceding qualified native check. Later exact-emitter and downstream results
belong to the verification record; no full aggregate pass is implied here.

The final native emitter produces byte-identical input to that typed replay
and passes freshly in51.705s at168,212KiB within60s/2GiB. Focused identity and
relative consumers, ordinary whiskering, mixed source action, both PathInd
scopes and PathOut pass at the recorded executions. A final PathOut metadata
expectation was corrected for the relocated declarations/rules and its owning
compilation test passes. Typecheck and lint pass; the later edit changes only
those expected policy/rule counts. No broad aggregate was repeated for this
source-data transfer; the preceding failed aggregate remains explicit.

This closes the previously missing identity/general-FF endpoint bridge in
the frontend. Remaining higher-action consumers, PathOut transitivity,
authoring/source-review failures, production health and final integration
still require qualification. The last complete TypeScript aggregate remains
the47-failure snapshot, with subsequent focused evidence recorded separately.
Book/article and adapted legacy nerve stages retain their dependency gates.
