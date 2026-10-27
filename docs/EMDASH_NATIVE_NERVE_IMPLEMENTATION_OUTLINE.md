# Native nerve implementation outline

Date: 2026-10-27
Status: active construction outline; checked pieces and open obligations are distinguished below
Owner: [native adaptation plan](EMDASH_NATIVE_NERVE_FOUNDATIONS_ADAPTATION_PLAN.md)
Scope: the full NF-1–NF-CLOSE goal, without assuming its missing inverse or closure laws

## Working order

The user requested broader construction progress while a local reconstruction
comparison remains unresolved. Build and test the maps that do not depend on
that comparison, then return to the exact proof obligations they expose.
Keep one local normalization question bounded by its actual consumer; do not
make the entire implementation wait on an individual scalar comparison.

The walking maps already support a concrete intermediate cubical construction.
It separates two tasks that were previously discussed together:

```text
geometric tensor diagrams ⇄ iterated oplax walking diagrams ⇄ native cubes.
```

The middle category is not a redefinition of either endpoint. The geometric
bridge still requires the correctly ordered tensor closure and its inverses.
This factorization does not weaken any same-index, degeneracy or higher-cell
requirement in the parent plan.

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

The first round trip should follow from the existing first walking inverse
and composition/unit compatibility of G_I. The reverse round trip also needs
the second walking inverse. A literal reflexivity attempt for composition
compatibility currently stops at Odd-dual distribution versus the represented
postcomposition normal form; that is an explicit reusable comparison
obligation, not a reason to postpone the map definitions.

The [recursion and square consumer](../emdash2/audits/native_nerve_foundations/README.md#whole-iterated-walking-cube-maps-and-implementation-outline)
are checked in a 38-input scope. All six degree-zero/one/two computations and
whole first/next-Hom types at variable n pass. The tensor coevaluation is an
actual decoded input, with a path to the square of its original coordinate
family. The final check takes 116.183s / 583,852 KiB at 180s / 2 GiB, with no new
rule or unifier and unchanged warning inventories. Inverse laws and equality
with the separately named interchanger constant are not claimed.

## Full cubical bridge and its remaining interfaces

Let Q₁=I and Qₙ₊₁=I⊗ᴿQₙ at the existing fixed bracketing. Q₀=Terminal is a
separate geometric case; W₀(C)=C does not prove the terminal-diagram theorem.
Let GCₙ(C)=Functor_oplax_cat(Qₙ,C), retaining the current profile unless the
actual whole closure establishes a necessary correction.

| Piece | Required interface and body | Open obligation |
| --- | --- | --- |
| Walking-first closure | `λₙ:GCₙ₊₁(C) ⇄ G(Qₙ,G_I(C)):ρₙ` | Construct the whole maps with the correct argument order. Current right Gray closure cannot simply be relabelled, and legacy Cartesian composition/admission assumptions are not imported. |
| Repeated currying | `cₙ:GCₙ(C) ⇄ Wₙ(C):uₙ` | Iterate the actual λ/ρ maps and qualify the needed iteration/shift comparisons. Preserve noninvertible cells and higher mapping action. |
| Geometric/native maps | `Dₙ=dₙ∘cₙ`, `Eₙ=uₙ∘eₙ` | These expressions supply the architecture, not missing c/u bodies or inverse proofs. No primitive equivalence is introduced. |
| Geometric degree zero | `Functor_oplax_cat(Terminal,C) ⇄ C` | Actual evaluation/constant maps and whole reconstruction at the selected profile. |
| Common face index | Both nerves over the existing selected augmented cube index | Establish whole restriction/shape action and natural comparison, with original coordinate order. |
| Degeneracies | Extend the same two diagrams by identity insertion | Face-degeneracy and degeneracy-degeneracy laws, and compatibility of D/E with them. |

The donor's forward-curry candidate uses Cartesian joint composition on its
oplax mapping categories and supplied profile admissions. That construction
is not imported into the receiver. The receiver needs the actual mixed-profile
exchange/closure, with the declared right tensor's order retained.

The first tensor consumer is the existing walking-square coevaluation. The
whole W₂/NC₂ maps can consume its curried diagram before a general λ is
finished. Recover its original boundary edges and interchanger in the
selected direction; do not infer tensor symmetry or invert a filler.

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
`85b30c5e`, independently of the unfinished normalization experiment. Next resolve the reusable G_I composition comparison
and test the whole walking-first tensor bridge. The exact whole-section
reconstruction equation remains required; scalar readbacks do not replace it.

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
