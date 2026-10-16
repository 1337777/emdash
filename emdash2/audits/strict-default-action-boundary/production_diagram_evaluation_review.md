# Varying-shape evaluation: the next profile boundary

Date: 2026-10-16
Status: staged evaluation owner, original reviewer and exact intrinsic-comparison beta qualified; downstream profile migration remains open
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Inventory: [explicit declaration-level consumers](production_diagram_evaluation_consumers.json)

## Intrinsic comparison continuation after ba5fd3ed

The [native comparison implementation](production_diagram_evaluation_naturality.lpfragment)
now specifies evaluation's canonical intrinsic action at the existing
`fdapp1_comma_projection_transf` owner. Its argument must be the canonical
`fdapp1_int_transfd` of the same evaluation transformation; the clause does
not rewrite an arbitrary supplied internal action. The right-hand side is
derived from eta's original `tapp1_post_laxity_cell`, canonical Hom action
and prewhiskering by the component functor theta ↦ theta[j].

For eta:F⇒G, theta:G⇒H and u:i→j, the whole comparison is

```text
theta[j] ∘ G[u] ∘ eta[i] ⇒ theta[j] ∘ eta[j] ∘ F[u].
```

The original eta cell is retained. Canonical Hom action is strict in theta;
eta itself still has the ordinary, unrestricted default-lax Transf type.
EvenDual's action on **Cartesian** mapping categories moves this whole
canonical transformation into evaluation's required Even-dual presentation.
This is a structural duality operator on strict transformations, not a
same-profile duality for arbitrary lax transformations. No profile property,
comparison cell, inverse or equality proof is added to the caller's inputs.
The projected identity and composition clauses of this same duality functor
are checked against its whole action; a reversed-composition negative is
retained. The composition clause keeps its measured Cartesian-category
subject-reduction guard, without restricting eta.

The actual native beta, its identity-theta component and its next whole Hom
action pass the [owning-position controls](production_diagram_evaluation_naturality_controls.lpfragment).
In particular, extracting the cell from the evaluation transformation now
computes to eta's **original extracted cell**. The wrong-shape-arrow and
strict-naturality-collapse controls fail as intended. This closes the precise
comparison-beta gap left by ba5fd3ed; it does not assert global confluence or
complete all downstream migration.

The mixed action's old semantic body is retained as
`diagram_evaluation_mixed_body`. Its public projection now has a stable head:
objects compute to the same tapp1 value, while the complete Hom action
computes through that original body. This change has a concrete consumer:
the existing exchange-of-composite rules otherwise distribute the whole body
into several composites before the intrinsic endpoints can be compared.
The failed full endpoint consumer and the successful stable projection are
recorded in the [new verification](production_diagram_evaluation_naturality_verification.json).
There is no auxiliary Sigma-composition owner or new equality payload.

Two narrowly scoped proof-time comparisons relate the actual source/target
transport composites to their canonical whiskering presentations. They keep
the diagram functors, eta, u, both shape endpoints and H; they do not compare
the source of eta's lax square with its target. The native beta is a
**constructor computation** for the declared evaluation owner. It is not
presented as a theorem derivable from object beta alone.

The original evaluator reviewer and focused controls pass on this source as
well. The core is byte-identical to the previous qualified core; its evidence
is carried forward rather than rerun. Both current evaluator checks retain
subject reduction, warnings, serial execution and the 90s/2GiB guard.

The next original owner is still `transf_arrow_diagram_func`. Its direct
replacement candidate can use the already implemented whole family-shape
operation on the walking diagram of eta:

```text
Arr(eta) = family_shape(walking_arrow_func(F,G,eta))
         : K → Functor_oplax_cat(WalkingArrow_cat,C).
```

Evaluation of oplax diagrams can in turn be obtained from the existing root
by applying OddDual to its version at OddDual(I), OddDual(C). Review that
whole type and its actual source/target/differential projections before
changing the original caller contracts. Ordinary and general callers retain
the scope distinctions in the inventory; do not globally identify the two
mapping profiles to keep old source text unchanged.

## Implemented continuation after 11dcd003

The [profile fragment](production_diagram_evaluation_profile.lpfragment) now
replaces the original module's evaluation declarations in the full generated
package. It retains all nine original names. The original Cartesian-exchange
rule block is retained with its actual Cartesian types, and the three
[observation helpers](production_diagram_evaluation_helpers.lpfragment) now
use actual fixed evaluation or opposite-profile prewhiskering. The
[original reviewer](production_diagram_evaluation_reviewer.lpfragment) retains
all ten positive and three negative observations with those corrected types.
The [focused controls](production_diagram_evaluation_controls.lpfragment)
also check the duality distinction, root laws and retained directed boundary.
[Verification](production_diagram_evaluation_verification.json) records exact
inputs, receipts, warning changes, rejected variants and remaining limitations.

The implemented interface is:

```text
ev_i                         : Functor_cat(I,C) → C
family_eval_i                : [K,[I,C]] → [K,C]
family_at_i(D)                = ev_i ∘ D

Functor_oplax_cat(A,B)        = Odd(Functor_cat(Odd(A),Odd(B)))
Transf_oplax_cat(F,G)         = Hom_Functor_oplax(Odd(F),Odd(G))
Ev                           : I → Functor_oplax_cat(Functor_cat(I,C),C)
Ev[i]                        = Odd(ev_i)
diagram_evaluation_transf(u)  : Transf_oplax(ev_i,ev_j)
family_shape(D)               = oplax_precomp(D) ∘ Ev
diagram_family_transf(D,u)    : Transf_oplax(ev_i ∘ D,ev_j ∘ D).
```

`ev_i` is the existing `fapp0_func`; family evaluation is existing ordinary
postcomposition. Its object agrees proof-time with the direct composition
used by `family_at_i`. Using the direct whole composite avoids placing the
two distinct represented pre/postcomposition normal forms underneath Odd.
The general fixed-evaluation input has not been narrowed to Cart or OneCat.

OddDual_cat and EvenDual_cat reverse alternating dimensions. Their recursive
Hom actions, involutions and strict-functor actions are native declarations
and rules. They do not change existing T/R/O names. Functor_oplax_cat is a
defined dual presentation, not an identification of its object classifier
with Functor(A,B). The whole Ev is a **declared structural owner** replacing
the invalid symmetry body; it has not been described as derived from the
previous Cartesian symmetry.

The mixed functor in eta is derived by two component evaluations of
`tapp1_int_func_transf`, followed by Cartesian exchange of that particular
Cart-valued family. Its object is the original `tapp1_fapp0(eta,u)`, and the
next Hom remains available. The encoded evaluation transformation's mixed
functor is Even applied to this actual derived functor. A whole component
projection of the root Hom action computes to F's full Hom functor. This
avoids an unqualified identification of Even(Transf) with Transf merely to
feed a capped modification into the ordinary component projector.

The existing intrinsic extractor applied to the encoded evaluation
transformation has the correctly directed boundary

```text
G[u] ∘ eta[i] ⇒ eta[j] ∘ F[u].
```

The two sides remain computationally distinct for variable eta. No comparison
cell or inverse is supplied by the caller. At that checkpoint the boundary
check did not yet establish reduction to eta's original extracted cell.
The subsequent native beta above now qualifies that reduction and the next
whole action. Global confluence and a complete standard omega-oplax
interpretation of every old internal-action owner are not claimed.

One core rule has a measured inferred-slot repair: the identity-input cut for
represented postcomposition now uses `id _ X`, because duality can erase the
identity's category annotation first. The represented owner still determines
that category. A narrow proof-time Odd-postcomposition reading exposes the
same raw source boundary; it does not equate the two sides of the lax square.
The previous shape-reindex comparison is adapted to the actual nested
prewhiskering projections, comparing every factor, endpoint and shape arrow.

This remains a generated, non-library migration. Public sources, source pins,
catalog and health snapshots have not been replaced. General downstream
callers must consume the opposite transformation profile, or recover their
already-supplied default transformation directly. Ordinary-target callers
need a justified conversion using their existing hypothesis, rather than a
global identification of lax and oplax Homs.

The broader original import now passes this owner and stops at
`transf_arrow_diagram_func` in `emdash3_2_arrow_diagram_families.lp`. Its old
body applies Cartesian exchange to a general lax transformation's walking
diagram. It needs the corresponding profile correction, not Cart=Functor.
The direction of its resulting family and the original OneCat consumers
must be reviewed before changing callers. The eight general declarations
in the inventory are not automatically ordinary-target declarations.

Replay from emdash2:

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20,v=1024 \
  python3 scripts/run_lambdapi.py \
  --package-root tmp/probes/production_owner_migration/package \
  --no-colors --quiet diagram_evaluation_profile_controls.lp
```

## Original failure and valid general operations

The pre-continuation broader import stopped at `diagram_evaluation_func` in
`emdash3_2_diagram_evaluation.lp`. Its old body exchanges the identity of
Functor_cat(I,C), but the migrated `sym_func` requires Cartesian mapping
categories. It must not be repaired by equating Functor_cat and Functor_cart_cat.

Fixed-point evaluation remains valid without that restriction:

```text
D = Functor_cat(I,C)
ev_i : D → C
D₀ : K → D
family_at_i(D₀) = ev_i ∘ D₀ : K → C.
```

The whole family-evaluation functor is postcomposition by ev_i. It retains
arbitrary lax transformations between D₀ and D₁. Use the existing fixed
`fapp0_func` and composition/whiskering owners; unrestricted exchange is not a
prerequisite for these operations.

## The comparison has the opposite direction

For a conventional lax η:F⇒G and u:i→j, the native comparison has direction

```text
G[u] ∘ η[i] ⇒ η[j] ∘ F[u].
```

A default-lax transformation ev_i⇒ev_j on D would demand the reverse direction.
Thus the unrestricted shape-evaluation transformation is oplax relative to
the retained default. Cartesian diagram maps remove that distinction, but
replacing every diagram category by Cart would lose general lax inputs to
fixed evaluation and other valid consumers.

The migration must distinguish the valid general fixed-evaluation operations,
the whole shape operation with its actual opposite transformation profile,
and existing Cartesian/ordinary-category specializations. A changed whole
profile is a mathematical correction; it is not permission to erase η's
noninvertible comparison or to supply its inverse as new caller data.

## Higher duality must be checked, not inferred from the square

The paper's `op` reverses odd dimensions; this branch's `Op_cat` reverses
dimension one only. Ara–Guetta §2, 35–38, distinguishes odd/even anti-monoidal
dualities from total duality and gives the corresponding lax/oplax Hom
comparisons. Replacing those dualities by transpose alone is not justified.
[Primary reference](https://arxiv.org/html/2503.08832v1#S2).

Accordingly, do not promote the tempting expression

```text
T(Functor_cat(T(A),T(B)))
```

to a qualified standard omega-oplax classifier. The existing Homd index uses
exactly a related literal presentation, P(I)=T(Functor_cat(I,T(Cat_cart))),
and its source explicitly disclaims a general equivalence with the usual
omega-category of oplax transformations. Preserve that qualification; this
review neither changes P nor establishes that its recorded native consumers
are invalid.

For the standard profile, write Odd for reversal of dimensions 1,3,5,... and
Even for reversal of dimensions 2,4,6,... .
Assuming the native Functor_cat realizes that conventional omega-lax Hom,
involutivity gives the following candidate native presentation:

```text
Oplax(A,B) ≃ Odd(Functor_cat(Odd(A),Odd(B))).
```

Objects are represented by Odd(F); they are not definitionally ordinary F.
The Hom between encoded F and G is Even applied to
Transf_cat(Odd(A),Odd(B),Odd(G),Odd(F)). Keeping that higher duality is essential.
Existing T/R/O names must not be reinterpreted. Any new odd/even owners need
native category/functor projection and interaction qualification first; use
clear names such as OddDual/EvenDual, not the paper's overloaded `op`.

The selected whole evaluation has shape

```text
Ev : I → Oplax(Functor_cat(I,C), C)
Ev[i] represents ev_i.
```

The implementation and remaining qualification are distinguished above.
Object beta and a declared type do not complete the intrinsic comparison.
A primitive whole owner with honest structural status and qualified
projections is permitted. No standalone laxity witness, resolution encoding
or general tensor-coherence library is a prerequisite merely to state it.

## Consumer migration and scope

The bounded textual inventory finds 123 explicit calls to shape-evaluation
operations in 55 declaration-bearing modules. 115 signatures mention OneCat
or IsNCat; the guard's actual target still requires per-consumer confirmation.
The eight remaining declarations are listed explicitly in the inventory.
This is not a proof of transitive consumer completeness.

OneCat-specialized conversions can use the existing strict-transfor admission
and qualified dual views where their hypotheses apply. Preserve all existing
ordinary-category guards. For general consumers, prefer actual pre/post
whiskering of an already supplied whole transformation over an unnecessary
arrow-family/exchange round trip. Inspect the source before asserting that
this works for any particular constructor.

Keep genuinely general diagram data and retained higher comparisons. In
particular, pointwise zero or identity components do not by themselves make
a general lax transformation strict. Do not silently replace such a map by
a canonical zero map, nor add a blanket OneCat restriction merely to pass.
The primary next slice is fixed evaluation plus a correctly profiled whole
shape interface and its real consumers. This remains foundational work; the
separate nerve/equivalence goal stays paused.
