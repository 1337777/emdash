# Native nerve implementation outline

Date: 2026-10-27
Status: active construction outline; checked pieces and open obligations are distinguished below
Owner: [native adaptation plan](EMDASH_NATIVE_NERVE_FOUNDATIONS_ADAPTATION_PLAN.md)
Scope: the full NF-1–NF-CLOSE goal, without assuming its missing inverse or closure laws

## Working order — core feasibility first

User clarification, 2026-10-27: the motivating question is whether both nerve
ideas are expressible in principle in the foundations, not whether a
comprehensive nerve library can be built immediately. The recent cubical
face/degeneracy work is retained, but further expansion waits behind the core
constructions below. No unfinished inverse is supplied to make a skeleton pass.

| Core | Present evidence | Decisive remaining feasibility slice |
| --- | --- | --- |
| Cubical | Whole native/geometric maps at every dimension; both zero inverses; variable-dimensional iterated-walking retraction; nonidentity higher-cell consumers. | Whole native walking reconstruction and mixed-evaluation/positive closure cancellation with the actual maps. |
| Simplicial | Qualified earlier flagged low-dimensional simplex/PathOut machinery and selected geometric shapes. | Independent all-flags triangle total with a whole varying-vertex family, directed filler and actual mapping comparisons; then test the uniform recursion/higher step. |
| Computational foundation | Installed corrected-duality Homd ladder and strict defaults; bounded whole-functor proof consumers. | Keep new core operations internal and usable; identify actual owner/profile gaps rather than count point checks. |

Next implementation order:

1. Form the whole family for the independent simplicial triangle and its
   Sigma total, using current T/R/O bases and the admitted coefficient. Expose
   the existing Homd/Sigma projections and a nonidentity triangle
   filler. Do not define the total as a geometric mapping category or Path of
   an object package.
2. Construct the corresponding whole mapping/universality interface in both
   directions. Use the first real reconstruction/beta consumer to decide what
   is missing. Sketch the dimension-three and Nat-recursive continuation with
   assumptions and unresolved interfaces labelled.
3. Return to the exact cubical walking/mixed-evaluator gaps, using their
   already constructed maps and whole diagram readbacks. Keep attempts
   bounded and require a result that changes the remaining core interface.
4. Compare the two core constructions against the feasibility gate below.
   Resume common-index, other-coordinate and degeneracy work afterward, in
   the amount needed for the agreed follow-through. Book/frontend/promotion
   work remains at its separate recorded integration boundary.

A credible feasibility result needs more than attractive signatures: whole
parameterization, actual maps in both directions, a nontrivial higher-cell
consumer, the minimal boundary/face compatibility needed to identify the
nerve-shaped construction, relevant reconstruction computation/comparison,
and a clear remaining proof boundary. Generic supplied structural laws must
be named as such. Neither a newly postulated nerve inverse nor object-only readbacks
prove the intended equivalence.

The core still factors geometrically as

```text
geometric tensor diagrams ⇄ iterated oplax walking diagrams ⇄ native cubes.
```

The full NF outcomes remain recorded in the parent plan; this is a priority
and assessment boundary, not a claim that the unfinished full goal is achieved.
The [pending face-order experiment](../emdash2/audits/native_nerve_foundations/pending_face_order/README.md)
must not be promoted from its self-selected local order. Native address
numbering versus the decoder's curry order needs a concrete square-boundary
comparison before selecting a common-index interpretation.

## Concrete map construction through iterated walking diagrams

Write I=WalkingArrow, G_I(C)=Functor_oplax_cat(I,C), and N(C)=LaxArrow_cat(C).
The existing whole maps are Observe_C:G_I(C)→N(C) and
Realize_C:N(C)→G_I(C). Their first composite Realize_C∘Observe_C≐id is qualified in the isolated prefix. The
second inverse remains open.

For an actual strict F:A→B, fixed oplax postcomposition has the defined body

```text
G_I(F) = OddDual_func(comp_cat_cov_func(OddDual_func(F)))
       : G_I(A) → G_I(B).
```

Each internal source and target retains its encoded Odd-dual category.
OddDual is the existing diagram-profile reversal of odd dimensions; it is
distinct from the T/R/O operations of the native total presentation. This
uses fixed postcomposition; it assumes no Cartesian joint composition of
arbitrary lax transformations.

Define independent iterates by ordinary internal Nat recursion:

```text
W₀(C) = C                   NC₀(C) = C
Wₙ₊₁(C) = G_I(Wₙ(C))        NCₙ₊₁(C) = N(NCₙ(C)).

d₀ = id_C                   e₀ = id_C
dₙ₊₁ = Observe_NCₙ(C) ∘ G_I(dₙ)
eₙ₊₁ = G_I(eₙ) ∘ Realize_NCₙ(C).
```

These are whole functors `dₙ:Wₙ(C)→NCₙ(C)` and `eₙ:NCₙ(C)→Wₙ(C)`, with
ordinary first/next-Hom action. They need neither walking inverse as an input,
nor an external strictness or pseudo certificate. They do not change the
existing `CubicalArrow_func(F,P)` interface: that operation is simply not
needed to form these particular composites.

At degree two the maps are concrete:

```text
G_I(G_I(C)) --G_I(Observe_C)--> G_I(N(C)) --Observe_N(C)--> N(N(C))
N(N(C)) --Realize_N(C)--> G_I(N(C)) --G_I(Realize_C)--> G_I(G_I(C)).
```

The [whole first round trip](../emdash2/audits/native_nerve_foundations/README.md#whole-first-round-trip-at-every-dimension)
is now derived by Nat induction: `eₙ ∘ dₙ ≐ id_Wₙ(C)`. It also recovers whole
K-parameter families and the original tensor coevaluation diagram. The
composition comparison uses a staged proof of the existing Odd-dual action;
the earlier literal-reflexivity failure is superseded, with no new rule. The
44-input consumer passes in 131.887s / 595,104 KiB. The reverse round trip still
needs the second walking inverse; no operational map acquires a proof argument.

The [recursion and square consumer](../emdash2/audits/native_nerve_foundations/README.md#whole-iterated-walking-cube-maps-and-implementation-outline)
are checked in a 38-input scope. All six degree-zero/one/two computations and
whole first/next-Hom types at variable n pass. The tensor coevaluation is an
actual decoded input, with a path to the square of its original coordinate
family. The final check takes 116.183s / 583,852 KiB at 180s / 2 GiB, with no new
rule or unifier and unchanged warning inventories. The later first round trip
is recorded above; the reverse inverse and equality with the separately named
interchanger constant are not claimed.

## Full cubical bridge and its remaining interfaces

Let Q₁=I and Qₙ₊₁=I⊗ᴿQₙ at the existing fixed bracketing. Q₀=Terminal is a
separate geometric case; W₀(C)=C does not prove the terminal-diagram theorem.
Let GCₙ(C)=Functor_oplax_cat(Qₙ,C), retaining the current profile unless the
actual whole closure establishes a necessary correction.

| Piece | Required interface and body | Open obligation |
| --- | --- | --- |
| Walking-first closure | `λₙ:GCₙ₊₁(C) ⇄ G(Qₙ,G_I(C)):ρₙ` | Both maps are constructed. Reverse ρ uses mixed exchange and existing right uncurry; neither inverse law is assumed. Whole exchange cancellation and closure laws remain open. |
| Repeated currying | `cₙ:GCₙ(C) ⇄ Wₙ(C):uₙ` | Both recursions check at every positive dimension. The iteration-shift inverses are derived; c/u inverse laws still depend on closure. |
| Geometric/native maps | `Dₙ=dₙ∘cₙ`, `Eₙ=uₙ∘eₙ` in positive degrees; actual terminal maps at zero | Both maps are now implemented at every n, with whole Hom action. Their inverse laws remain required. No primitive equivalence is introduced. |
| Geometric degree zero | `Functor_oplax_cat(Terminal,C) ⇄ C` | Actual evaluation/constant maps now have both derived whole inverse paths with retained inverse data. Production and warning qualification remain separate. |
| Common face index | Both nerves over the existing selected augmented cube index | Establish whole restriction/shape action and natural comparison, with original coordinate order. |
| Degeneracies | Extend the same two diagrams by identity insertion | Face-degeneracy and degeneracy-degeneracy laws, and compatibility of D/E with them. |

The donor's forward-curry candidate uses Cartesian joint composition on its
oplax mapping categories and supplied profile admissions. That construction
is not imported into the receiver. The receiver needs the actual mixed-profile
exchange/closure, with the declared right tensor's order retained.

The first tensor consumer is the existing walking-square coevaluation. The
whole W₂/NC₂ maps consume its curried diagram. The new parameter owner also
retains the named nonidentity interchanger. Recover all required boundary/shape
comparisons in the selected direction; do not infer tensor symmetry or invert
a filler.

## Geometric parameter action and forward decoder

The fixed functor G_I(F) and its composition law do not by themselves provide
its whole action on oplax transformations in F. The current
`comp_cat_cov_func_func` has Cartesian source and target mapping categories;
it is not the required general parameter action. The checked interface
consumer explicitly rejects that substitution.

The new structural ordinary-lax postcomposition owner defines, by OddDual
action, the strict functor

```text
P(I,A,B) : G(A,B) → G(G(I,A),G(I,B)).
```

Its object at an encoded F is the encoded fixed postcomposition G_I(F).
At D:I→A, its Hom component in alpha is the existing whole precomposition
by D. In the encoded ordinary-lax view, the extracted post/left cell at delta
now projects to the original alpha-comparison at delta[i]. Its canonical
higher-component ladder, image units/composition and noncollapse controls
also pass. No comparison is requested as caller-supplied data.

The raw nested composite projection and Cat_cart specialization retain the
[precise limits in the review](../emdash2/audits/native_nerve_foundations/postcomposition_review.md).
This structural owner has not been promoted to production or claimed as a
theorem derived from the old fixed-F interface.

For Q=GrayTensor_R(I,B) and the already constructed coevaluation
q_B:B→G(I,Q), the implemented forward closure is the concrete composite

```text
λ(B,C) = precompose_oplax(q_B) ∘ P(I,Q,C)
       : G(Q,C) → G(B,G(I,C)).
```

The [former conditional consumer](../emdash2/audits/native_nerve_foundations/oplax_postcomp_interface.lpfragment)
is now instantiated by the actual P. With Qₖ=GrayCubePos_R(k), of geometric
dimension k+1, the internal recursion is:

```text
sₙ : Wₙ(G_I(C)) ⇄ Wₙ₊₁(C) : tₙ
c₀(C) = id_G_I(C)
cₖ₊₁(C) = sₖ₊₁(C) ∘ cₖ(G_I(C)) ∘ λ(Qₖ,C)
Dₖ(C) = dₖ₊₁(C) ∘ cₖ(C) : G(Qₖ,C) → NCₖ₊₁(C).
```

Both s/t inverse laws are derived by Nat induction independently of the
walking inverses. The whole decoder, line/square computations, variable-k
Hom action and parameter-owner interactions pass together in 97.488s /
595,020 KiB, with subject reduction at 180s / 2 GiB.
[Exact replay and evidence](../emdash2/audits/native_nerve_foundations/postcomposition_verification.json)
retain the new rules, failed alternatives and warning boundaries.

The reverse closure map and encoder are now constructed as described below.
Both positive-dimensional closure round trips and the native second inverse
remain open; the later degree-zero proof below is now checked. Do not substitute the Cartesian
joint-composition/admission route retained in the legacy donor or let either
local normalization limit become the sole continuation.

Semantic cross-check: Ara–Guetta v1, §21 describes mixed lax/oplax exchange;
Proposition 36 and Remark 38 relate it to odd/even duality, which reverses
tensor-factor order. These facts support investigating the stated profiles,
not identifying different kernel mapping categories or assuming the missing
maps. The precise argument order must follow the receiver's declared right
closure. [Primary reference](https://arxiv.org/html/2503.08832v1#S2).

## Reverse through whole mixed exchange

Write L(A,B)=Functor_cat(A,B), while G retains the opposite transformation
profile above. The [derived mixed exchange](../emdash2/audits/native_nerve_foundations/reverse_review.md)
has type `M(K,I,C):L(K,G(I,C))→G(I,L(K,C))`. For a whole
D:K→G(B,G(I,C)), two shape exchanges and M give I→L(B,L(K,C)). Canonical
admission into the older explicit lax profile allows existing right uncurry
to produce GrayTensor_R(I,B)→L(K,C). One final shape exchange produces
K→G(GrayTensor_R(I,B),C).

Apply that whole operation to the identity on G(B,G(I,C)). This constructs
ρ(I,B,C) with its parameter action, without a new tensor-action or reverse-map
primitive. Internal Nat recursion now gives:

```text
u₀(C) = id_G_I(C)
uₖ₊₁(C) = ρ(I,Qₖ,C) ∘ uₖ(G_I(C)) ∘ tₖ₊₁(C)
Eₖ(C) = uₖ(C) ∘ eₖ₊₁(C) : NCₖ₊₁(C) → G(Qₖ,C).
```

The final 61-input check passes in 85.162s / 583,624 KiB, including the
preceding forward construction, whole-family readbacks and profile projections.
The complete mixed-exchange object readback is proved by staging existing
OddDual functoriality; no new rule is needed for that proof. A whole fixed-D
evaluation comparison is part of the structural postcomposition interface,
with typed-reflexivity and wrong-D controls.

The [whole reindexing/reflection extension](../emdash2/audits/native_nerve_foundations/exchange_cancellation_review.md)
now reduces the first cancellation to one whole evaluation equation. Writing
S=L(K,G(I,C)), its two sides are K→G(S,G(I,C)):

```text
pre_G(M) ∘ P_G(I,L(K,C),C) ∘ ε_K(C) ≐ ε_K(G(I,C)).
```

The reduction passes in a 65-input scope; the actual proof of this remaining
equation still fails. Its named equality type has no supplied inhabitant,
and no operational map takes an equality argument. Next derive this
compatibility, both exchange cancellations and the closure inverse laws,
then use them in the cube recursions. The existing walking first
round trip can support one geometric inverse independently of the second
walking inverse. Preserve the latter, the checked degree-zero maps/inverses,
and the remaining same-index action and degeneracy requirements. The [replay record](../emdash2/audits/native_nerve_foundations/reverse_verification.json)
separates the passing constructions from the pending inverse attempt.

The [new diagram round trips](../emdash2/audits/native_nerve_foundations/mixed_diagram_reconstruction_review.md)
prove Y[M[D]]≐D and M[Y[E]]≐E for every complete K/I diagram. They use the
existing whole double exchange and staged duality, with no new rule. These
are paths at objects of the mapping category; assembling the corresponding
whole endofunctor equalities remains required. Do not invoke objectwise
functor extensionality to turn this result into the missing internal inverse.

## Degree zero and the uniform dimension interface

The [zero construction](../emdash2/audits/native_nerve_foundations/geometric_degree_zero_review.md)
uses actual evaluation and constant-diagram maps G(Terminal,C)⇄C. Their first
whole round trip is derived from the structural constant/evaluation beta and
OddDual composition. It also recovers whole arbitrary parameter families.
The [terminal reconstruction](../emdash2/audits/native_nerve_foundations/terminal_inverse_review.md)
now proves the reverse whole round trip using actual terminal-valued
equivalence data, the existing object-path view and a structural
constant-precomposition beta. The original direct-reflexivity attempt remains
failed evidence; no eta axiom replaces it. The final 78-input scope passes in
110.775s / 618,504 KiB, including whole K-family reconstruction.

The complete index family and maps are now internal Nat eliminations:

```text
Shape₀ = Terminal                 Shapeₙ₊₁ = GrayCubePos_R(n)
Decodeₙ : G(Shapeₙ,C) → CubicalLevel(C,n)
Encodeₙ : CubicalLevel(C,n) → G(Shapeₙ,C).
```

The zero/successor equations and variable-n whole Hom actions pass in the
69-input qualification (108.523s / 615,940 KiB). This is dimension indexing,
not yet a common-index nerve equivalence. No tensor unit comparison or
mapping-category identification is assumed. The new whole zero proof uses
these same maps. Preserve the independent mixed-evaluator and native inverse
goals; neither follows from the zero case.

The [intrinsic unit-normality continuation](../emdash2/audits/native_nerve_foundations/intrinsic_unit_normality_review.md)
qualifies identity-base computation through the existing Homd ladder while
preserving nonidentity laxity. Broader erased-identity overlap qualification
and production promotion remain open. The zero inverse proof is now checked;
next return to positive-dimensional mixed-evaluator compatibility and native
whole-section reconstruction, keeping the independent branch below in scope.

## Shape action through the existing right closure

The [first-factor action](../emdash2/audits/native_nerve_foundations/tensor_left_action_review.md)
now supplies the whole functor

```text
T_left(A,D,B) : L(A,D) → L(A⊗ᴿB,D⊗ᴿB),
tensor_left(F) = uncurry_R(coevaluation(D,B) ∘ F).
```

Its body is postcomposition, canonical profile admission, right uncurry and
inclusion. The original 16-input scope qualifies identity and whole curried
readback without a new primitive or rule.

The [right-closure naturality extension](../emdash2/audits/native_nerve_foundations/right_closure_naturality_review.md)
now explicitly supplies the generic whole target-naturality path for the
canonical curry interface. This is a structural contract beyond the prior
fixed-parameter beta/eta; it is not mislabelled as a derived theorem.
Coevaluation naturality, source naturality for each complete input diagram
and first-factor tensor composition are derived from that contract.

A whole A-parameter family of first-coordinate collapses now consumes the
composition theorem, retaining the complete B-row. Absorption, idempotence
and source/target walking endpoint instances pass. The final 21-input scope
takes 94.662s / 312,820 KiB, with unchanged warning inventories and no new
rewrite/unification rule. No operational map receives a proof argument.

The [split first-coordinate maps](../emdash2/audits/native_nerve_foundations/geometric_first_faces_review.md)
now use coevaluation and uncurry of the constant identity to define actual
δₐ:B→A⊗ᴿB and π:A⊗ᴿB→B. They satisfy π∘δₐ≐id and δₐ∘π≐Cₐ by derived
proofs. Internal Nat elimination extends them over every current geometric
shape, with literal endpoint/terminal maps at zero.

Fixed oplax precomposition gives whole geometric faces dₐⁿ and degeneracies
sⁿ, with dₐⁿ∘sⁿ≐id on G(Qₙ,C) at variable n. This also recovers whole
K-parameter families. The opposite composite has its independent collapse
reading at positive tensor steps. The final 78-input check passes in
99.461s / 629,996 KiB, with no new rules and unchanged warning inventories.
The zero category remains G(Terminal,C), not a runtime alias of C.

Whole source-naturality assembly, the other tensor factor/coordinates,
cross-coordinate face/degeneracy relations, common augmentation/index and
native encoder/decoder compatibility remain required. Continue those actual
shape and comparison operations alongside mixed-evaluation and native
whole-section reconstruction; the first-coordinate law is not the full index.

## Independent simplicial branch

Keep the user-selected higher simplex shapes. Strict maps from ordinary
ordinals are not substituted for arbitrary triangles with nonidentity fillers.
The native construction remains independent of those geometric shapes.
A candidate recursion is

```text
NS₀(C) = C
NSₙ₊₁(C) = O(Σ_(O(C)) O_fib(x ↦ NSₙ(PathOut_C(x)))).
```

The displayed family in this expression is an obligation: it needs whole
Cartesian parameter action for NSₙ, not a pointwise assignment at x. At n=0
it recovers the existing native edge total. At the next step its fixed-x
consumer is N(PathOut_C(x)), the triangle category with original filler data.
Use that concrete consumer to qualify the whole varying-x family before
claiming independent all-flags totals at arbitrary dimension.

| Piece | Required result |
| --- | --- |
| Native parameter action | Form the whole family above using admitted Cat_cart maps and corrected T/R/O bases. No object-only family declaration. |
| Higher shape recursion | Selected Sₙ and its whole terminal-join/cone mapping interface, with actual triangle/tetrahedron cells. |
| Native/geometric maps | Whole `NSₙ(C) ⇄ G(Sₙ,C)` maps and actual inverse data; do not define NS by the geometric mapping category. |
| Same index and augmentation | A common augmented simplex index, with n-simplexes having n+1 vertices and the augmentation checked separately. |
| Degeneracies | Identity insertion in both descriptions, all required simplicial relations and comparison compatibility. |

## Qualification and return to reconstruction

The Wₙ/NCₙ map formation and degree-two consumer are checked using qualified
`85b30c5e`, independently of the unfinished normalization experiment. The G_I
composition comparison and first recursive round trip are also derived.
Both all-degree geometric maps and both iteration-shift inverses
now check relative to the recorded structural owners. Continue with whole
exchange and geometric inverse proofs. The exact whole-section reconstruction equation remains required;
scalar readbacks do not replace it.

The actual native moving-cell/map investigation has positive focused evidence,
but its total-dual constant-family overlap is not fully qualified. Preserve its
[source/receipt recovery](../emdash2/audits/native_nerve_foundations/actual_action_pending/README.md) separately and do not silently promote those rules to
make this skeleton pass. The eager total-Hom family rewrite is unadopted.

Every required whole inverse, higher-cell and same-index comparison remains
an acceptance gate. Supplied structural interfaces, derived constructions,
proof-time comparisons and runtime computation must retain their separate
labels. Source promotion, frontend Pi/Sigma adaptation, health/final CI and
book/article updates for new results remain the parent goal's final stages.
Connections, permutations, general tensor monoidality and Kan/Segal/Rezk
results remain outside this continuation.
