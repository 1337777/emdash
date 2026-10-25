# Mixed total-duality and direct Homd frontend migration

Date: 2026-10-25. This tranche follows the promoted native kernel. It adds no
Lambdapi owner/rule, operational proof parameter, or generic checker rule.
The [execution record](foundation_frontend_mixed_homd_verification.json) and
[source acquisition](foundation_frontend_mixed_homd_acquisition.json) pin this
scope; full frontend integration remains open.

## Native declarations retained

`Hom_catd(E,X,Y)` takes X in `Pi_cat(TotalOp_catd(E))` over `CoAbove2_cat(K)`
and Y in `Pi_cat(E)` over K. `Transf_catd` has the same total-dual negative
section of `Functor_catd(A,B)`. Its fibre is the actual Hom of
`Functor_cart_cat`, not an arbitrary ordinary transformation category.
The five transferred declarations include the native total dual and total
family prerequisite. Ten existing runtime clauses expose their objects,
Homs, involution and mixed-family fibres.

The old nine-owner action transfer was tied to the removed
`Homd_target_section_catd` and opaque versions of the old projection ladder.
It is replaced by the current ten native declarations, nine with checked
bodies. `hom_con` and `hom_` reuse predecessor owners instead of being
redeclared. The lower ladder is now literally:

```text
P(I) = Op_cat(Functor_cat(I,Op_cat(Cat_cart)))
S_D(x) = Hom_(Functor_cat(K,Q))(diagram(D),diagram(Hom_K(x,-)))
homd_src_func(FF,x) : E[x] → Op_cat(S_D(x))
homd_src_sec(FF,x,u) : Obj(S_D(x))
homd_tgt_func(FF,x,u,y) : D[y] → P(Hom_K(x,y))
homd_index_presheaf(H) : Op_cat(I) → Cat_cart
homd_(FF,x,u,y,v)[f] = Hom_E[y](E[f](u),FF[y](v))
```

Here FF remains a general lax displayed map D⇒E. The source section is the
actual Cartesian component of the defined relative root; its y-projection
is an actual component in Q. There is no enlarged y/v/f context or new Pi.

Source-prior runtime clauses supply the native Q object/Hom projections,
represented object action, ordinary dual action, Cartesian inclusion arrow
action and mixed constructor projections. The generic fapp1/tapp0 object
projections are retained explicitly because the component definition consumes
them. The old identity and hom_int clauses reuse inherited rules. The old
root-to-alias folds are replaced by the native checked definitions; the old
pointwise presheaf target is not retained as an alternative normal form.

## Frontend metadata

`oppositeDisplayedFamily(E)` keeps its meaning `Op_catd(E)` and now records
its actual `CoAt2_cat(K)` base. `totalOppositeDisplayedFamily(E)` is a separate
native constructor with `CoAbove2_cat(K)` base. Negative Hom/Transf-section
fixtures now use the latter.

Object use compares the selected runtime `Obj` classifiers while retaining
the categories in the terms. The rich classifier reifier recognizes the
selected R/C2 object-preserving dual heads, just as it already recognized T.
This preserves recursive displayed-map metadata under the total dual without
identifying the categories or their higher Homs. Ordinary profiles keep their
previous default path. Final generic LF checking still checks the unchanged
term; no coercion is emitted. The public method is inventoried in text parity
as a direct category/family constructor, not a new text syntax.

## Qualification and remaining obligations

All 28 focused tests pass, including the serial native check of all 22 selected
runtime clauses and the emitted signatures/bodies. The native receipt is
`20261025T221828Z-0c75319045904c5d937449245c1cc41b`: 20.849s, 169,024KiB,
60s/2GiB, supported checker, warnings and subject reduction enabled. No native
source changed, so the previous core/library receipts remain applicable.
Workspace, registration, typecheck and lint pass. The full TypeScript attempt
stops at the later direct-mixed target-postcomposition rule recorded below.

The native conformance source checks emitted signatures/bodies, each selected
runtime projection, the actual emitted public root, every lower projection,
and the final presheaf-to-endpoint and endpoint-to-Hom comparisons. Negative
controls reject the former transpose negative section, unshifted total-family
base, and category identifications which would erase higher variance.

The generic TypeScript controls check the root component, source-u component,
y-component, and independent endpoint leaf. Recursive consumers retain eight
named Hom levels and two mixed-root actions. This does not yet qualify the
complete TypeScript comparison

```text
homd_index_presheaf(homd_tgt_func(FF,x,u,y)[v]) ≐ homd_(FF,x,u,y,v).
```

That comparison passes in the native kernel. The exact transferred-runtime
replay returns `not-equal` at a 1,024-step comparison budget (wave264), so it
remains a required transfer obligation. In particular the existing signature-only view of
`Homd_target_con_func` and the represented coefficient action must be completed
where that comparison consumes them. The earlier test's literal final
pointwise projection is superseded by this corrected P-index expression, not
silently dropped. It remains in F04 acceptance.

The next aggregate failure is the old coefficient/profile in
`categorical_direct_mixed_introduction_transfer.ts`, at its target
postcomposition rule. Later direct mixed introduction/source-action profiles,
all remaining source-pin reviews, production health and final integration
remain required. Book/article and legacy nerves remain subsequent stages.
