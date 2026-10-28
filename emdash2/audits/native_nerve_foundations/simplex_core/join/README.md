# Terminal join and the geometric successor

Date: 2026-10-28
Status: qualified isolated cone construction and cross-section action; whole successor comparison remains open
Parent: [native simplex core](../README.md)
Evidence: [source-pinned replay and receipts](../verification.json)

## Constructed maps

The [join cross profile](cross_profile.lpfragment) extracts a directed cell
from the existing `join_cross_transf`, for every S and p:s→t:

```text
J(S) = Join_cat(Terminal_cat,S)
c_s : apex → right(s)
κ_p : right(p) ∘ c_s ⇒ c_t.
```

κ is an intrinsic-action projection, not a new declared filler. At S equal
to the walking arrow this constructs an actual strict functor from the
previous HigherTriangle shape to J(S). No ordinary truncation, associativity
of join shapes, or inverse is inferred from the old simplex module's prose.

The [generic cone extension](cone_extension.lpfragment) goes in the other
direction of the construction:

```text
x : C,  D : S → PathOut_C(x)
cone(x,D) : J(S) → C.
```

Its right branch is `Sigma_proj1 ∘ D`. Its whole cross datum is the
tautological Sigma section `sigma_functord_sec(id)`, pulled back along
`D ∘ projection₂`. The existing `join_elim_func` consumes that one section.
There are no operational equality proofs, boundary certificates or separately
supplied naturality cells. The construction is uniform in S and C; its value
is a whole functor. This does not yet internalize the operation as a functor
between the entire parameter categories of diagrams and cones.

For the walking-arrow diagram in PathOut determined by
`p₀₁`, `p₀₂`, `p₁₂` and `α : p₁₂ ∘ p₀₁ ⇒ p₀₂`, the cross section's extracted
naturality computes to the original α. [The consumer](cone_action.lpfragment)
checks this for arbitrary C and rejects replacing α by an unrelated β of
the same type. The resulting `J(I) → HigherTriangle` recovers all three
vertices and its two cross edges. Both maps are constructed; no equivalence
between the shapes has been established.

## Minimal owner refinements

1. The [constant-left represented Hom view](constant_left_hom_view.lpfragment)
   compares `Prof_reindex(Unit_prof(C),const(x),G)` with
   `hom_(G ∘ projection₂,x)`. This is an explicit structural partial-evaluation
   interface, not a theorem inferred from object agreement. It retains G,
   x, all bases and the actual product projection. The existing both-constant
   case agrees; substituting another x is rejected.
2. The [Sigma reindexing view](projection_reindex_view.lpfragment) has an
   [independent proof](projection_reindex_proof.lpfragment) on the unchanged
   production core. The operational section retains the literal
   `Sigma_proj1_pullback_catd` head; only the external represented-family
   presentation is compared at proof time. An earlier attempt to retype the
   section too early hid its component guard. A generic same-Pullback-head
   comparison also failed because injective decomposition ran first.
3. The [section pullback action](section_pullback_action.lpfragment) refines
   the existing whole intrinsic Hom, capped action and transported-identity
   projections by the original section's action at F[p]. It preserves that
   action's nonidentity comparison. Its constant-family specialization selects
   the existing ordinary composite, joining ordinary functor evaluation with
   the section presentation. No new stable-head constructor is introduced.

The whole/capped projections and constant-family interaction have
[focused controls](section_reindex_controls.lpfragment). Removing only the
three intrinsic-action refinements restores the original-α computation
failure. The rule-LHS audit finds no reconstructible compound inferred slot;
manual review also checks the retained actual maps and the two projection
orders. These are temporary full-owner refinements, not production promotion.

## Exact qualification boundary

The selected 24-input scope passes in **44.715s / 181,124 KiB**, with subject
reduction, the explicit 180s/2GiB ceiling and `OCAMLRUNPARAM=o=20,v=1024`.
The same existing-owner dependency baseline has 19 inputs and passes in
51.299s. Both report 2,002 critical-pair and 178 replaceable-variable warnings;
mapped source locations, term heads and rule families are identical, with no
parser issues. This is not a confluence certificate. The independent
production-core reindex proof passes in 37.476s.

The [actual cell-image attempt](cell_image_pending.lpfragment) is deliberately
separate. It forms the strict-functor Hom image of the join's own extracted κ.
Its mapped composite boundary does not yet convert to the named triangle
composite, so the comparison with `triangle_kappa` fails at the type boundary.
This is **not** the passing supplied-cross α computation above. The existing
`join_map_extend_cross_beta` is a structural propositional higher-constructor
contract; it has not been silently promoted to runtime computation or proved
from these checks. No equality argument is added to the cone map.

Replay from the root with the parent `replay.py` and modes `join-core`,
`join-dependencies`, `join-projection-proof`, `join-action-omission`, or
`join-cell-image-pending`. The last two intentionally fail at their recorded
checks. The manifest retains exact failed predecessors and input snapshots;
authoring errors are distinguished from semantic and computational evidence.

## Next whole interface

Write G_S(C) for the existing oplax diagram category and P_C for the whole
PathOut family. The next candidate to qualify is

```text
S⁻_(T C)(G_S ∘ P_C) → G_(J(S))(C).
```

Its object computation should be the cone extension above, with the existing
Odd-dual diagram encoding respected. The whole action in the apex and diagram,
its orientation, and a genuine next-dimensional consumer remain to be
constructed; the displayed signature is not an implemented map or a supplied
universality assumption. This continues the internal native Step recursion.
The old `DirectedSimplex_cat` appends a terminal vertex, while this constructor
prepends one; a shape/rebracketing comparison must be explicit if both are used.

Keep the cell-image conversion and required inverse/index laws recorded, but
do not postpone this whole successor feasibility assessment until every
triangle boundary proof is complete. No degeneracy expansion or comprehensive
join/profunctor theory is needed before that concrete consumer.
