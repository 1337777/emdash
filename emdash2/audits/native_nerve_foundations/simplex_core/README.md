# Independent all-flags native triangle core

Date: 2026-10-28
Status: isolated native triangle, whole connecting map and derived raw modification qualified; whole triangle boundary identifications, geometric comparison and production gates remain open
Owner: [core-feasibility outline](../../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
Evidence: [exact sources, scopes and attempts](verification.json)

Current continuation: [terminal-join geometric successor](join/README.md),
with the [internal recursive native coefficients](recursive/README.md) retained.
Use `--mode join-core` for the latest isolated qualification or
`--mode recursive-core` for the native recursion. The preceding
[connecting map and modification](#whole-connecting-map-and-derived-modification--2026-10-28)
remain available, with their whole triangle boundary identifications open.

## Whole interface and native meaning

Write N(C)=LaxArrow_cat(C), T=Op_cat and O=TotalOp_cat. This slice supplies a
structural Cartesian internalization A of the existing native arrow operation:

```text
A : Cat_cart → Cat_cart,        A[C] = N(C)
P_C = PathOut_cat_func(C) : T(C) → Cat_cart
E_C = A ∘ P_C                 : T(C) → Cat_cart
T₂(C) = O(Σ_(O(C)) TotalOp_catd(E_C)).
```

Total fibre duality changes the base R(T(C)) to O(C). Both family and total
are actual internal terms. The category is independent of geometric simplex
shapes; it is not Path of an object record. At fixed x₀ its fibre is
N(PathOut_C(x₀)), so both outgoing edges and the triangle between them vary.
The outer Sigma additionally varies x₀, with its actual base transport.

The visible object data are

```text
x₀, x₁, x₂ : C
p₀₁ : x₀→x₁,   p₁₂ : x₁→x₂,   p₀₂ : x₀→x₂
α : p₁₂∘p₀₁ ⇒ p₀₂.
```

The [total](triangle_total.lpfragment) stores these using the old PathOut,
native-arrow and dependent-Hom constructors. The [plain-cell view](triangle_visible.lpfragment)
passes the same α directly into that classifier; it adds no equality argument
or separately declared filler. Changing α changes the stored triangle.

All three [edge projections](triangle_faces.lpfragment) are whole functors
T₂(C)→N(C), with the original 01, 02 and 12 object values. They are derived
by Cartesian family maps, total fibre duality and Sigma totalization. The
initial vertex projection is also whole. The old fixed-first-vertex category
has an actual whole Sigma-fibre inclusion into the new total.

## Structural input versus derived construction

The [arrow coefficient](arrow_coefficient.lpfragment) is a newly internalized
structural interface, not a theorem assembled solely from the old point
projections. Its projection ladder reuses the existing native N(C) and
CubicalArrow_func. Its action on strict Cartesian transformations retains
both original component arrows and the commuting square. Those component
arrows need not be identities or invertible. The ordinary lax-transformation
default is unchanged.

The two canonical source/target projection transformations are internalized
at that same coefficient owner. The family E_C, its total, three edge maps,
constructor views and consumers are derived from this structural interface
and existing kernel operations. No native/geometric inverse is supplied.

Public callers provide only the existing strict functor F. The older
CubicalArrow_func capability parameter is filled internally from
functor_is_strict(F), using actual derived inverse data; its arbitrary-P API
is not redesigned or erased. A stable canonical head projects to the same
checked capability fields when applied. This prevents premature expansion
of that evidence during whole-map comparisons.

## Concrete qualification

The [consumer](triangle_consumer.lpfragment) puts the actual directed Gray
interchanger into T₂(GrayWalkingSquare_cat), in its checked direction. Its
original readable cell and boundary edges are recovered. It is not inverted
or replaced by an identity. Generic constructor controls reject replacement
by another filler. The coefficient controls exercise changing-initial-vertex
transport, whole unit/composition comparisons and the original two-cell
components; a different strict transformation is rejected.

The final 44-input scope passes with subject reduction in **45.740s /
196,808 KiB**, at 180s / 2 GiB. The source is based directly on the production
kernel plus the two owner-position repairs below, without importing the
unfinished cubical moving-action candidate. The new replay is independent
of the cubical reverse-map replay chain.

An earlier whole-map qualification timed out at 180s with about 27 MB of
expanded diagnostic output. Stabilizing the canonical capability projection
and specifying proof endpoints gave a fresh 86.792s pass with about 3.8 MB
of output. No memory/time default was changed. The recipe and history retain
both observations; no isolated attribution to only one edit is claimed.

## Scoped generic repairs and remaining normalization

Two measured projection-order gaps were repaired only in the temporary full
kernel copy:

- [Constant composition](constant_family_composition.lpfragment) computes the
  old constant-functor beta after the input has selected its Const_catd head.
  The third triangle edge is the real consumer; constant/identity/noncollapse
  and whole-versus-preprojected controls pass.
- [Cartesian identity action](cartesian_identity_action.lpfragment) handles
  id_Cat_cart(C) after its tag becomes id_Cat_cat(C). It supplies the same
  strict identity law already used for dual-source joins, without changing
  transformation naturality.

The final warning inventory is 1,867 critical-pair reports / 178 replaceable
patterns, versus 1,797 / 178 in the original 27-source baseline. The native
coefficient adds 16 image/projection reports; the constant repair removes two;
the Cartesian identity join adds 56 constructor identity peaks. Relevant
whole/point comparisons and actual consumers pass, but broader typed
profile/duality overlap review and production promotion remain required.
The inferred-slot audit has no unreviewed compound slots. This is scoped
qualification, not a global confluence certificate.

The [pending runtime control](owner_controls_unit_pending.lpfragment) still
fails: the legacy capability-based native identity map does not reduce a
square literally to its original square. Its whole identity comparison
passes. This failed observation is retained separately as `unit-pending`;
it is not removed from the completion ledger or called a green aggregate.
The positive scope includes all preceding construction and repair checks.

## Genuine higher shape and whole parameter families

The [finite shape](higher_triangle_shape.lpfragment) S₂ now has three vertices,
short edges 01/12 and a genuine long Hom WalkingArrow. Composition of the
short edges selects its source; edge 02 selects its target. Its generator is
therefore κ:12∘01⇒02, rather than an equality of the two arrows. The short
Homs use distinct nominal singleton carriers, so a source identity cannot be
misread as a nonidentity short edge.

The [structural recursor](higher_triangle_recursion.lpfragment) realizes
(x₀,x₁,x₂,p₀₁,p₀₂,p₁₂,α) as S₂→C. Its stable whole-Hom projection ladder uses
constant functors on the short Homs and the existing walking-arrow recursor
on the long Hom. Its image of κ is the original α. This is an explicit
structural shape/elimination interface, not a proved mapping equivalence.
Neither a whole recursor η law nor a nerve inverse has been declared.

Applying that recursor in Functor_cat(K,C) and the existing mixed exchange
gives the [derived whole family constructor](higher_triangle_family.lpfragment):

```text
F₀,F₁,F₂ : K→C
e₀₁:F₀⇒F₁, e₁₂:F₁⇒F₂, e₀₂:F₀⇒F₂
φ:e₁₂∘e₀₁⇒e₀₂
───────────────────────────────────────
triangle_shape_family(...) : K→Functor_oplax_cat(S₂,C).
```

The e's are ordinary lax transformations. Exchange back recovers the whole
S₂→Functor_cat(K,C) recursor, including the original e and φ; another φ is
rejected. The concrete interchanger consumer also passes through the geometric
shape and recovers the same native triangle. No strict-transformation guard
or operational equality-proof argument is introduced.

The [object observation](higher_triangle_observation.lpfragment) reads an
S₂→C into T₂(C), and its composite with the recursor recovers the native
constructor. At C=Functor_cat(K,C′), this recovers whole diagram data as an
object of T₂(Functor_cat(K,C′)). It is **not** yet a functor K→T₂(C′), nor a
whole observer between the geometric and native mapping categories.
The [vertex comparisons](triangle_vertex_paths.lpfragment) additionally prove
that faces 01 and 02 have the same whole initial-vertex functor.

The selected 57-input scope passes with subject reduction in **76.099s /
279,792 KiB**, at 180s / 2 GiB. The same-import dependency baseline passes in
64.393s / 270,464 KiB. Their warning inventories are respectively 2,464 and
2,244 critical-pair reports, both with 181 replaceable patterns and no parser
issues. The 220 additional reports concern the private singleton unit and
composition rules, their source-identity joins, finite shape composition,
recursor action and interactions with existing dual/evaluation rules. Typed
unit/composition, whole/capped and cell-retention controls pass; broader
typed overlap review remains required before production. No global confluence
claim is made. The final qualification adds no warning-family change to the
preceding whole-family scope.

The inferred-slot audit has no unreviewed compound slots. The helper type
retains explicit C: Obj(C) alone does not reconstruct C. The first failed
implicit-C attempt remains in the evidence history. These additions change
no active production source and do not resolve the separate legacy
identity-square observation above.

## Derived whole coefficient and total comparisons

The whole source/target coefficient naturality equations are now proved by
[staged whiskering](whiskering_paths.lpfragment) and
[horizontal composition](horizontal_interchange.lpfragment), without any
new rewrite or unification rule. The argument first exposes the existing
postcomposition telescope's internal action, then specializes its transformation
to an identity. The two whiskering routes are compared through the strict
action of product composition, using explicit product carriers and the
existing precomposition comparison. The native consumer instantiates this
in Cat_cart, where the transformations are Cartesian; this is not an
unrestricted interchange contract for ordinary lax transformations.

Write P=PathOut_C, A=N_coeff, h:P⇒const(C) for the existing whole PathOut
projection, and s,t:A⇒id for the native-arrow coefficient projections.
The [coefficient proofs](coefficient_boundary_paths.lpfragment) give

```text
s_const(C) ∘ A[h] ≐ h ∘ s_P
t_const(C) ∘ A[h] ≐ h ∘ t_P.
```

These are equalities of entire Cartesian family maps. A control rejects
identifying h∘s_P with h∘t_P. No original filler or endpoint is erased.

The [totalization proofs](total_boundary_paths.lpfragment) then use the
actual existing functor

```text
Σ_coeff(R(K)) ∘ TotalOp_catd_func(K)
  : R(Cart(K,Cat_cart)) → Cat_cart.
```

The R on its source is necessary; the first unshifted-source attempt failed
and is retained in the history. Its arrow action is the existing Sigma map
of the total-dual Cartesian family map. Strict action proves preservation of
composition and transports both displayed equations to equalities between
the actual whole Sigma-map composites. This **does not yet identify them
with the third edge's literal endpoint maps**: constant projections and the
outer total-duality presentation still need to be assembled in that proof.

The 61-input comparison scope passes in **66.176s / 280,432 KiB**. Warning
categories, term heads, rule families and parser inventory match the previous
higher-triangle scope. Fourteen existing warnings move between source
locations because the coefficient now imports before the finite shape.
There are no new formal rules in this proof tranche.

## Constant cases needed by endpoint assembly

The next actual consumer isolates the expected formula

```text
π₂ ∘ Σ(const(F)) ≐ F ∘ π₂.
```

Its direct whole comparison initially fails. Four scoped constructor/unit
cases now pass in the temporary full core:

- [Sigma's constant-map second projection](constant_total_projection.lpfragment)
  reduces to F∘π₂. General displayed maps keep their existing owner.
- [Cartesian prewhiskering by a constant family](constant_prewhiskering.lpfragment)
  selects the constant transformation on the original component.
- [Total duality of a constant Cartesian map](total_dual_constant_map.lpfragment)
  gives the constant map on O(F), over R(K), paralleling the existing
  dimension-one case.
- [The constant-transformation unit](constant_transformation_unit.lpfragment)
  preserves the identity law of the existing strict weakening functor. An
  arbitrary endomorphism does not trigger it.

Prewhiskering's rule must be placed after the existing constant-composition
beta for subject reduction; the failed earlier placement is recorded.
The [interaction scope](constant_interactions.lpfragment) includes both
component orders, the relevant unit overlap, dual involution, retained map
data and noncollapse controls, together with all higher-triangle consumers.
It passes in **64.250s / 282,172 KiB** with subject reduction (65 inputs,
180s / 2 GiB). The full temporary-core inferred-slot audit has no unreviewed
compound slot.

The final warning inventory is 2,473 critical-pair reports / 181 replaceable
patterns, with no parser issues. Relative to the 2,464-report comparison
scope: prewhiskering adds two unit/component reports; the constant unit
removes two old capped-action reports and adds nine identity-erasure,
duality and transfor-projection reports. The typed consumers above pass.
Broader Terminal/Product/Q identity-erasure and dual-unit interaction review
remains required before production promotion. These candidates are not a
global confluence certificate or an installed production change.

## Whole endpoint proofs and native universal edges

Both [literal third-edge endpoint equalities](whole_endpoints.lpfragment)
are now proved as equalities of whole functors:

```text
src ∘ face₁₂ ≐ tgt ∘ face₀₁ = vertex₁
tgt ∘ face₁₂ ≐ tgt ∘ face₀₂ = vertex₂.
```

The [whole totalization compatibilities](cone_total_paths.lpfragment) supply
the proof. For a Cartesian map U:E⇒const(B), write
T(U)=O(π₂∘Σ(O_fib(U))). The two derived laws are

```text
T(V∘U) ≐ T(V) ∘ O(Σ(O_fib(U)))
T(const(F)∘U) ≐ F ∘ T(U).
```

They retain the original maps, shifted bases and intermediate totals. Apply
them to the already proved coefficient naturality equations. No endpoint
equation is postulated or installed as a rewrite. Arbitrary whole K-parameter
families preserve the comparison, and a control rejects identifying vertex₁
with vertex₂. This 67-input scope passes in **66.934s / 279,908 KiB**, with
all five warning inventories identical to the preceding constant scope.

The [native edge construction](universal_edges.lpfragment) then reuses the
existing native universal-arrow transformation. Its
[retained prefix](walking_universal_prefix.lpfragment) is checked under its
`native_nerve_realization_review` owner name used by the cubical replay;
the original source is pinned. Its previously qualified
[total-dual postcomposition units](../total_dual_postcomp_units.lpfragment)
are required by subject reduction and are carried at their existing owner
position. This does not import the unfinished moving-action experiment or
assume a walking inverse.

Fixed whiskering through the existing horizontal action, with an identity
first leg, forms edge₀₁ and edge₀₂ at the common vertex functors. It also
forms edge₁₂ at its original projected source and target. The
[component checks](universal_edge_controls.lpfragment) recover p₀₁, p₀₂ and
p₁₂. The original universal-arrow filler, identity and noncollapse checks
run inside their owning module, where their protected presentation helper
is available. The 70-input scope passes in **64.137s / 280,500 KiB**, with
subject reduction at 180s / 2 GiB. The 31 additional warning reports belong
to the reused total-dual postcomposition unit families; the final inventory
is 2,504 / 181, with no parser issues. Broader promotion review remains open.

The first shared-vertex type test for edge₁₂ failed: its whole endpoint
equalities were proved, but the checker did not automatically treat those
proofs as conversion. The generic comparison below now resolves that test. The
[original failed shared-type consumer](shared_edge_type_pending.lpfragment)
is retained separately. The first stable-precomposition spelling also failed
to type edge₀₁; existing fixed horizontal whiskering solves that earlier
presentation issue. No operational path cast, supplied equality proof or
triangle-specific endpoint unifier was used to hide that issue.

## Shared edge type and the remaining native modification

The [general totalized-projection theorem](cart_total_projection_path.lpfragment)
is now checked independently of the new comparison. For arbitrary admitted
E:K→Cat_cart, a Cartesian h:E⇒const(B), an endofunctor F of Cat_cart, and a
Cartesian U:F⇒id, it proves

```text
U[B] ∘ T(F[h]) ≐ T(h) ∘ O(Σ(O_fib(U[E]))).
```

Here U[E] is fixed prewhiskering, F[h] fixed postwhiskering, and T is the
already defined negative total projection. The proof composes the existing
Cartesian horizontal-action calculation and totalization compatibilities.
Its 71-input run passes **without** the new unifier, so the justification
does not depend on the inference rule being tested.

The [whole proof-time view](cartesian_total_projection_view.lpfragment)
implements that theorem at the Sigma projection owner in a temporary full
core. It matches stable R(T(-)) presentations and checks the actual E, F, h,
U-component, constant target and shifted bases. No new runtime rule, object
extensionality or triangle-specific endpoint equation is introduced. In
particular, ordinary lax transformations are not made Cartesian.

This view admits [edge₁₂ at the shared vertices](shared_universal_edge.lpfragment),
with its original p₁₂ component. The [generic controls](cart_total_projection_controls.lpfragment)
reject an unrelated family map and an unrelated component. Removing only
this comparison restores the edge-type failure, while its independent
mathematical proof still checks. There are no operational path casts or
equality-proof arguments.

All three native edges can now be passed to the checked higher-shape family
constructor. The [assembly outline](realizer_outline.lpfragment) makes the
one remaining input precise:

```text
Φ_C : β₁₂ ∘ β₀₁ ⇒ β₀₂
      (a modification over T₂(C), from vertex₀ to vertex₂)

native_triangle_realizer_from_modification(Φ_C)
  : T₂(C) → Functor_oplax_cat(S₂,C).
```

Exchange back recovers the entire supplied Φ_C, and another modification is
rejected. **This is an assembly skeleton, not the native realizer.** No
canonical Φ_C value is declared or assumed. The next construction must obtain
it from the native Sigma data, recover the stored α at each triangle, and
retain the actual higher action. Supplying a desired coherence cell would
not complete that task.

The final 74-input scope passes in **74.773s / 314,752 KiB** with subject
reduction at 180s / 2 GiB. The omission control fails at the intended type
in 66.065s. Warning counts remain 2,504 / 181; categories, term heads, rule
families and parser inventory match the no-new-comparison proof scope.
Location differences are exactly the core insertion's 41-line offset.
The full-core inferred-slot audit has no unreviewed compound slot; the
unifier's semantic argument-retention conditions were also reviewed manually.
Production integration and the prior overlap gates remain open.

## Canonical Sigma introduction and coefficient totalization

The next construction uses a general one-way comparison, with H an actual
Cartesian coefficient functor:

```text
κ_H(E) : Σ_K(H∘E) → H(Σ_K E),     H : Cat_cart → Cat_cart.
```

The [body](sigma_coefficient_total.lpfragment) postcomposes the existing lax
Sigma introduction E⇒const(ΣE) by H, then takes the constant-target Sigma
projection. It assumes neither colimit preservation nor an inverse. Fixed
horizontal whiskering gives the right whole source presentation; the first
stable-postcomposition spelling failed to align it. The native case H=N_coeff
gives **Σ_K N(E)→N(Σ_K E)** and sends an actual fibre arrow a to the native
arrow represented by (id_k,a). An unrelated arrow is rejected.

The [oplax-diagram instance](sigma_diagram_total.lpfragment) is definitionally
the same comparison at H(C)=Functor_oplax_cat(I,C). Its
[coefficient](oplax_coefficient.lpfragment) uses a new structural whole root
of the **existing** odd-dual Cartesian mapping action:

```text
Odd_coeff : EvenDual_cat(Cat_cart) → Cat_cart.
```

Object, whole-Hom and capped projections reuse OddDual_cat,
OddDual_cart_func_func and OddDual_func. The oplax coefficient is then a
defined composite. It retains the existing fixed postcomposition map, its
unit/composition and the original components of a strict transfor. This is a
structural internalization with projection qualification, not a newly proved
global duality-coherence theorem. The native-arrow instance needs no new
coefficient root. No default transformation profile changes.

The [Sigma-introduction owner](sigma_fibre_inclusion_owner.lpfragment) also
needed its canonical intrinsic action. The whole fixed-p Hom map is the
total dual of the existing inclusion into the appropriate Sigma–Hom fibre.
Its projections give

```text
fdapp1_int_hom(σ_intro(E),p)[α] = (p,α)
fdapp1_int_cell(σ_intro(E),p,u) = σ_transport(E,p,u).
```

The second line is the transported-identity projection of the first, not a
new supplied comparison cell. The fibre-Hom projections are its p=id case.
The ordinary-functor view of σ_intro(const(1)) additionally projects to the
canonical K→K×1 pairing, closing the constant-source overlap. These changes
remain in a temporary full copy of the existing one-way owner.

The [cell consumer](sigma_diagram_cell.lpfragment) carries a genuinely
directed 2-cell through a walking diagram in a representable fibre and
recovers that same cell in the total. The [qualification](sigma_diagram_qualification.lpfragment)
also retains a next-Hom cell, checks both fibre projection orders and actual
base-arrow extraction. The [overlap scope](sigma_intrinsic_overlap.lpfragment)
covers constant and terminal-source families and rejects changing the base
or fibre data. The [whole decoded diagram](sigma_diagram_consumers.lpfragment)
is compared with postcomposition by the native fibre inclusion, rather than
only inspected at its two endpoints.

Two small core refinements accompany these computations:

- [Cartesian-source postcomposition units](cartesian_postcomposition_units.lpfragment)
  recognize the identity after its category tag has reduced. The diagram
  coefficient's unit was the concrete failing consumer.
- [Sigma's identity constructor view](sigma_identity_constructor_view.lpfragment)
  compares stable id_Σ with the complete native pair (id_base,id_fibre).
  It retains both runtime presentations and does not assert arbitrary arrow
  eta. Its law is [proved independently](sigma_identity_derived.lpfragment)
  against the production core, without any audit insertion: Sigma elimination
  proves the constructor acts as a unit on every encoded loop arrow, then the
  ordinary category unit law identifies it with id_Σ. The focused derivation
  passes in 27.259s / 168,996 KiB; omitting only the inference view makes the
  reflexive presentation test fail.

The final 81-input scope passes in **66.809s / 308,176 KiB**, with subject
reduction at 180s / 2 GiB. Warnings are 2,539 / 181, with no parser issues,
versus 2,504 / 181 before this slice. The new reports concern the odd coefficient
projections, Cartesian postcomposition units, intrinsic identity-input and
constant-source overlaps, and fibre-Hom identity/composition observations.
The typed controls above pass, and the full-core/owner inferred-slot audits
have no unreviewed compound slots. Broader production and overlap review is
still required. A separate normal-form diagnostic timed out during imports;
it is not evidence of a normalization loop, and no resource default changed.

### Filler construction route to qualify next

Use the native-arrow instance of κ_H. The next needed comparison is
d_A:O(N(A))→N(O(A)). A concrete candidate is the native graph of the existing
TotalOp_transf applied to U_A; it needs no inverse of the walking comparison.
Qualify its whole Cartesian coefficient profile and projection behavior
before using it on the varying PathOut family. Do not apply fibrewise
TotalOp_funcd to an arbitrary lax map to bypass its actual type.

With those comparisons, the intended composite turns a native triangle into
a native arrow between faces 01 and 02. Its source projection should be the
identity and its target projection the existing edge 12. Applying the existing
intrinsic naturality of U_C would then give Φ_C, with the original α as its
component. These comparison/assembly steps are **not yet implemented** by
this Sigma slice. No canonical Φ value or native inverse is assumed.

## Replay and next core task

Run `python3 .../simplex_core/replay.py --mode qualification --assemble-only`
for exact reconstruction without another check. `baseline` selects the
unchanged-source import scope; `unit-pending` reproduces the failed literal
square observation. Without `--assemble-only`, the existing serial resource
guard and pinned checker are used. Active production sources are untouched.

`higher-qualification` reconstructs the checked higher shape, whole families,
observation and composition controls. `higher-dependencies` is its same-import
baseline; `higher-recursion` and `higher-family` retain the smaller checked
scopes. All modes verify exact imported bytes before invoking the checker.

Two subsequent direct-reflexivity attempts isolate the next boundary:

- `vertices-pending` fails to prove the third edge's whole source agreement
  (70.462s / 279,412 KiB). Its target-agreement declaration is not reached.
- `coefficient-boundary-pending` first forms the whole source-coefficient
  naturality square, but direct reflexivity does not join its two whiskering
  composites (46.728s / 192,864 KiB).

The second failed direct proof is superseded mathematically by the staged
proof in `boundary-qualification`; it remains a reproducible direct-reflexivity
limitation. `constant-total-pending` retains the failed constant Sigma
comparison without the new cases; `constant-qualification` assembles all four
scoped cases and their interaction consumers. `endpoints-qualification`
checks the now derived whole endpoint proofs. `universal-qualification`
checks the native edge constructions and original universal-arrow controls;
`shared-edge-pending` reproduces the earlier failed shared-type application.
The latter selects the exact older owner prefix before its appended controls.
All program and dependency hashes are checked. None of these scopes supplies
a desired nerve endpoint equality or inverse as an assumption.
`projection-law-proof` checks the general theorem without the new view;
`projection-qualification` checks its implementation, the actual shared edge
and the assembly skeleton; `projection-omission` removes only the comparison
and records the expected type failure.
`sigma-totalization` checks the coefficient maps, the completed introduction
projections and their native/diagram consumers. `sigma-unit-derived` checks
the independent production-core proof; `sigma-unit-view` and
`sigma-unit-omission` retain the focused inference comparison and omission.
The Sigma-inclusion owner is replaced only in the selected totalization
mode, with its original active-source pin and full emitted source retained.

Next construct the whole native/geometric comparison. The available whole
family realizer needs the native triangle's universal vertex functors, edge
transformations and modification as its inputs. Two outgoing-edge source
comparisons are checked, as are both literal third-edge endpoint equalities.
The shared edge₁₂ type now checks through the general totalized-projection
view. Next obtain the whole native universal filler, then the actual native
realizer and comparison laws. Pointwise observation and
T₂(Functor_cat(K,C)) data do not discharge those obligations. The ordinary
DirectedSimplex_cat(2) is not substituted for the genuine higher shape.

The uniform all-flags recursion still needs a whole coefficient operation
at each step, not the pointwise formula alone. The current slice establishes
its native degree-two construction, not the complete simplicial nerve,
geometric equivalence, common-index laws or degeneracies.


## Native total-duality comparison — 2026-10-28

The new [defined map](arrow_total_dual.lpfragment) is

```text
d_A : O(N(A)) → N(O(A))
d_A = graph(TotalOp_transf(U_A)).
```

It reuses the existing graph constructor, the canonical default-lax admission
from the cubical audit, and the native universal arrow U_A. Callers supply
only A. The old explicit admission remains internal; no comparison cell,
equality proof or nerve inverse is added to the interface.

The [consumer](arrow_total_dual_controls.lpfragment) checks the full reversed
native square, retaining the original directed filler α and swapping its
sides a,b. It also checks double reversal of that square and rejects replacing
α by an unrelated β. The reused structural graph endpoint projections give
whole functor equalities

```text
src_(O A) ∘ d_A ≐ O(tgt_A)
tgt_(O A) ∘ d_A ≐ O(src_A).
```

These endpoint beta contracts retain their previous structural status. They
are not inferred merely from agreeing objects. The new identity-input
[projection](total_dual_intrinsic_projection.lpfragment) computes the existing
extracted naturality of `TotalOp_transf(ε)` from the original extracted
naturality of ε, in the reversed Hom. Its [typed bodies](total_dual_intrinsic_body.lpfragment)
are definitions, not new cells. The inferred source and identity carrier stay
anonymous: O(N(A)) normalizes to a Sigma, so a literal O-source discriminator
prevented the intended native consumer from matching.

One [proof-time endpoint view](total_dual_boundary_view.lpfragment) relates
the ordinary off-diagonal action to the corresponding total-dual
postcomposition head. Its [independent staged proof](total_dual_boundary_proof.lpfragment)
passes on the unchanged production core, without this view or any audit core
insertion (35.027s / 168,188 KiB). It preserves every category, functor,
endpoint, acting arrow and transformation component. No operational proof
argument is introduced, and arbitrary lax naturality remains directed.

The selected 86-input scope passes in **82.454s / 592,776 KiB**, with subject
reduction and the explicit 180s/2GiB profile. The 2,609 critical-pair and 181
replaceable-variable warnings have the same category, term-head and
rule-family inventories as the same-import pre-change attempt; parser
inventory is clean. Locations shift with the inserted owner text. This is
not a confluence certificate. Removing only the intrinsic projection restores
the expected full-square failure (114.071s); the unchanged Sigma, triangle,
shape, family and original U consumers remain in the selected import scope.

The broader [whole post-naturality body](total_dual_whole_pending.lpfragment)
remains unadopted: its two whole endpoint-composite comparisons did not typecheck
in the recorded attempt. A proposed runtime dual-whiskering normalization
also disturbed an existing Sigma consumer and was rejected. Neither is in
the selected replay. The exact receipts/source snapshots are retained in
`verification.json`; these failures are computational qualification boundaries,
not a proof of semantic impossibility.

The [identity-transformation endpoint comparison](total_dual_retained_identity_pending.lpfragment)
also remains unresolved. It fails both with the candidate and on the unchanged
production core (33.761s / 167,972 KiB), before establishing a literal unit
normal form. The [bare F[p] presentation](total_dual_identity_pending.lpfragment)
failed in the candidate too. These are retained inference/overlap obligations;
this slice does not repair or assume them. `arrow-duality-unit-pending`
reproduces the production-core failure.

**Still open:** the Cartesian coefficient-level naturality of d, general
nonidentity-input/higher computation of the total-dual intrinsic action, the
connecting whole triangle arrow, and the canonical Φ. In particular, neither
the tested square involution nor d's declared functor type proves a whole
inverse or a whole naturality theorem. The next intended coefficient has
source `TotalOp_catd(N_coeff)` and target `N_coeff ∘ total_op_cart` over
R(Cat_cart). Qualify that whole interface before feeding its restriction and
the checked Σ(N∘E)→N(ΣE) map into the triangle construction. Do not declare Φ
as an input or infer this coefficient profile from point computations.

Replay with `--mode arrow-total-duality`, `arrow-duality-boundary-proof`, or
`arrow-duality-omission`. As before, `--assemble-only` verifies exact source
snapshots without launching a checker. All changes remain isolated audit
candidates; production owners, registration and frontend pins are untouched.


## Whole connecting map and derived modification — 2026-10-28

The [Cartesian coefficient owner](arrow_dual_coefficient.lpfragment) now
internalizes the preceding defined d_A:

```text
d : StrictTransfor(R(Cat_cart), Cat_cart,
                  TotalOp_catd(N_coeff), N_coeff ∘ total_op_cart).
```

Its strict parameter action is a **new structural admission**, with the
already defined d_A as component. It is not a theorem inferred from agreeing
objects. The [whole naturality comparison](arrow_dual_naturality.lpfragment)
is a consequence of that selected profile. Ordinary transformations elsewhere
remain lax. No external profile certificate or comparison is an argument of
the construction.

Restricting d along R(E), then applying existing Sigma maps and the checked
Σ(N∘E)→N(ΣE) comparison, gives the [defined negative-total map](negative_arrow_total.lpfragment):

```text
O(Σ_(R K) O_fib(N∘E)) → N(O(Σ_(R K) O_fib(E))).
```

At E=PathOut_C this is an actual whole functor L_C:T₂(C)→N(N(C)). On a native
triangle, its stored arrow is the square `(id_x₀, p₁₂, α)` from p₀₁ to p₀₂.
The [constructor consumer](triangle_connecting_controls.lpfragment) recovers
that complete square, not just its vertices.

Let a and b be L_C's actual whole source and target projections. The
[whole connecting transformation](triangle_connecting_transformation.lpfragment)
and [whole modification](triangle_raw_modification.lpfragment) are derived:

```text
τ_C : a ⇒ b
Ψ_C : tgt_C[τ_C] ∘ U_C[a] ⇒ U_C[b] ∘ src_C[τ_C].
```

Ψ_C uses the existing post/left naturality extraction, not a supplied filler.
Its [component consumer](triangle_raw_modification_controls.lpfragment)
recovers exactly the original α and rejects an unrelated β. Changed-family
and changed-postfunctor controls also pass.

**Ψ_C is not yet the required Φ_C.** The [direct whole endpoint attempt](triangle_connecting_endpoints_pending.lpfragment)
failed at a≐face01; the target proof was not reached. We still need both
whole endpoint identifications, src_C[τ_C]≐id_vertex0 and
tgt_C[τ_C]≐β₁₂. Component readback proves none of these whole equations.
The next work is the applicable generic Sigma cocone/projection reconstruction
and coefficient endpoint coherence. The earlier
[tautological Sigma source-generation contract](../sigma_generation_owner.lpfragment)
is relevant evidence, but is not already a theorem about this new cocone.
Do not restore arbitrary Pi/Sigma-section identification or introduce a
triangle-specific inverse to close the gap.

Two [family composition views](family_dual_composition_views.lpfragment)
allow the whole coefficient restriction to use its actual shifted families.
Their [independent proofs](family_dual_composition_proof.lpfragment) use the
existing family formation and ordinary associativity. They pass on the
unchanged production core in 35.052s / 168,432 KiB. Removing those two
views restores the expected family-typing failure (84.772s).

The expanded postcomposition consumer also exposed an overbroad matcher in
the preceding total-duality endpoint view. Its second head could match an
ordinary postcomposition case before the appropriate ordinary view. The
[selected guarded version](total_dual_boundary_view_guarded.lpfragment)
requires the actual R(T(F)) head and preserves every original argument.
The prior unguarded version remains only in its historical narrower replays
and the explicit failing `duality-view-broad-regression` mode. Reused
postcomposition component-owner dependencies are pinned from their existing
audit; no strictness assumption was added to make them pass.

The selected **94-input scope passes in 93.797s / 615,160 KiB**, with subject
reduction, 180s/2GiB limits and the existing GC profile. Its 2,612 critical-pair
and 181 replaceable-variable warnings have a clean parser inventory. Compared
with the 89-input connecting-map scope before adding postcomposition, four
locations are added and one removed (net +3), at the reused component-evaluation,
product-projection and modification-projection owners. Exact source-line
mapping and disposition are in `verification.json`; this is not a confluence
certificate. Active production sources and frontend pins remain unchanged.

Replay modes are `triangle-connecting`, `family-duality-proof`,
`family-duality-view-omission`, `triangle-endpoints-pending` and
`duality-view-broad-regression`. The two last modes retain their exact earlier
failed snapshots. The full native triangle realizer, its inverse comparisons,
general higher duality computation and production integration remain open.


## Operational arguments and recursive-feasibility priority

User clarification, 2026-10-28: advance the uniform core outline and its
nontrivial higher-dimensional consumers before completing all remaining
comparison and coherence proofs. The existing L_C and Ψ are the degree-two
construction evidence; their required whole boundary identifications remain
open. None is an equality-proof field of a nerve constructor. The operational
maps take categories, families and transformations. `*_path` values verify
comparisons separately; the intended interface does not pass them into
realizers as operational transports or boundary certificates.

The next priority is the uniform native simplex coefficient recursion and
the next higher-dimensional consumer, alongside the already constructed
Nat-recursive cubical maps. Keep enough whole typing and computation to
expose real blockers. Fix a boundary comparison when the recursive
construction needs its conversion; do not silently assume it, and do not
turn it into an extra proof argument. Arbitrary-dimensional realization and
inverse laws are still unproved.

A small [canonical-cocone observation](sigma_intro_reconstruction.lpfragment)
now proves that the totalized Sigma inclusion returns the original object
and an arbitrary constructor arrow (p,α), using the existing capped projection
view. No new rule was installed. The direct unstaged reflexivity attempt
failed; the staged proof passes (48.568s / 215,552 KiB, 4 inputs). It does
not prove the whole cocone unit or introduce a general Sigma eta rule.
Replay with `--mode sigma-cocone-observations`; this evidence is retained
without making completion of the whole unit a prerequisite to the recursive
outline review.
