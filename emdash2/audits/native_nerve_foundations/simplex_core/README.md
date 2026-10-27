# Independent all-flags native triangle core

Date: 2026-10-27
Status: qualified isolated native construction and consumers; geometric comparison and one legacy runtime normalization remain open
Owner: [core-feasibility outline](../../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
Evidence: [exact sources, scopes and attempts](verification.json)

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

## Replay and next core task

Run `python3 .../simplex_core/replay.py --mode qualification --assemble-only`
for exact reconstruction without another check. `baseline` selects the
unchanged-source import scope; `unit-pending` reproduces the failed literal
square observation. Without `--assemble-only`, the existing serial resource
guard and pinned checker are used. Active production sources are untouched.

Next construct a genuine directed triangle shape and its whole comparison
maps. The existing ordinary DirectedSimplex_cat(2) cannot encode arbitrary α
under strict functors. A minimal proposed shape has three vertices, generating
edges 01/12/02 and a generating cell 12∘01⇒02; its 0→2 Hom is WalkingArrow,
with composition selecting the source endpoint. This shape and its mapping
universality are not yet implemented or assumed here.

The uniform all-flags recursion still needs a whole coefficient operation
at each step, not the pointwise formula alone. The current slice establishes
its native degree-two construction, not the complete simplicial nerve,
geometric equivalence, common-index laws or degeneracies.
