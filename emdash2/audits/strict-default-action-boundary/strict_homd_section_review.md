# Represented Homd section and fixed-x source action

Date: 2026-10-14
Status: non-library raw-Q candidate; fixed-x ladder checked; outer root open
Plan: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [exact verification](strict_homd_section_verification.json)
Replay: [authoring replay](strict_homd_section_replay.py)

## Actual interface and ownership

Write T for the candidate's dimension-one `Op_cat`, I_x=Hom_K(x,−), and
ι for `sf_q_include`. Public Hom_Cat remains Functor_cat. The candidate Q
has the raw curried Hom with ordinary lax transformations at both levels:

```text
Hom_Q(A,B) = Functor_cat(A,Functor_cat(T(B),Cat))
ι(F)[a][b] = Hom_B(b,F[a]).
```

The whole first-Hom action of ι is defined by existing ordinary Hom and
fixed postcomposition. Its variable transformation component computes to
postcomposition by the original component η[a]; it is not replaced by a
strict-transfor carrier. Q itself remains a declared structural coefficient,
not a model constructed from a general profunctor tensor.

For a strict displayed map U:E⇒D, the structural represented mate has type

```text
sf_q_mate(U) : Transf_{K,Q}(ιD,ιE)
sf_q_mate(U)[y] = hom_con_int(U[y]).
```

This whole mate is declared with native projections. Its pre/right action
is a definition through Q postcomposition and the diagram's whole Hom
action. The complementary intrinsic comparison is not supplied as an input,
and has not yet been separately extracted/qualified in this prefix. No
generic mate functor on arbitrary higher modifications is assumed.

The identity Homd section is then an actual definition using the preceding
checkpoint's canonical strict map c_E(x,u):I_x⇒E:

```text
S_E(x) = Transf_{K,Q}(ιE,ιI_x)

homd_id_src_sec(E,x,u) := sf_q_mate(c_E(x,u)) : Obj(S_E(x)).
```

There is no primitive Pi, combined y/v/f base, or curry operation. The
experiment's `sf_` names are private candidate names, not a second public API.
The direct ladder below fixed x is:

| Native candidate | Type / computation |
| --- | --- |
| sf_homd_id_src_func(E,x) | T(E[x]) → S_E(x) |
| at u: sf_homd_id_src_sec(E,x,u) | Obj(S_E(x)), the whole transformation above |
| at y: sf_homd_id_tgt_func(E,x,u,y) | E[y] → Functor_cat(T(Hom_K(x,y)),Cat) |
| at v: sf_homd_id_(E,x,u,y,v) | T(Hom_K(x,y)) → Cat |
| at f | Hom_E[y](E[f](u),v) |

The fixed-x source functor and its first-Hom action are structural owners.
Their object projection uses the derived section, and their y/v/f action
projects to the existing whole precomposition functor along E[f](h).
Both intermediate transformation carriers are ordinary Transf. Identity
and composition are checked before and after the y/v projections. The
inner u/index naturality boundaries remain unequal in a typed negative
test, matching the earlier finite noncommuting square.

The whole y-arrow action at q:y→z computes, at v:E[y] and f:x→z, to

```text
Hom_E[z](E[f](u),E[q](v)).
```

Its whole/capped observations and identity action check; its next Hom
remains an ordinary transformation with the indicated q/r endpoints.
This does not claim that every higher action projection or its coherence
has been computed explicitly.

## Relative section by composition

For strict displayed FF:D⇒E, the Q diagram image is existing fixed
postcomposition applied to its native ambient view. The relative section is

```text
homd_rel_src_sec(FF,x,u)
  := homd_id_src_sec(E,x,u) ∘ ι(FF).
```

Its whole y-component computes to homd_id_tgt_func(E,x,u,y) ∘ FF[y], and
its leaf computes to Hom_E[y](E[f](u),FF[y](v)). Identity FF recovers the
identity section. These are definitions with inherited computation, not
another primitive FF-dependent Homd theory. A raw ambient FF is rejected
by this experimental strict displayed-map interface. The public Functord
default has not been migrated by this tranche.

Q right-represented composition and its stable postcomposition observation
share the ordinary source-reindexing result P∘F. Units and represented
composition of two ordinary functors check. General Q composition, its
whole higher action/coherence, and the original broader lift remain open.

## Measured implementation issues

The represented Q composition clause needed its actual curried codomain
as an elaboration guard: leaving it inferred silently selected the wrong
middle category in the emitted RHS. A normal-form probe exposed the
difference, and the whole composition assertion catches it.

The y-action uses the stable ordinary Hom postcomposition owner, so its
represented-input cut is specified there as well as at raw Q composition.
Fixed Cat postcomposition gets a direct component projection through the
existing generic Hom-action head; this avoids introducing a dependency on
joint Cartesian evaluation. The named inclusion's diagram-value fold joins
the identity image with the selected diagram normal form, allowing the
relative identity computation.

The first u-action diagnostic used Hom abbreviations which prematurely
inverted the transposed source. Canonical Obj(Hom_cat(...)) binders repaired
the diagnostic without changing operational rules. Intermediate u-action
composition rules separately required explicit mapping-category guards for
subject reduction. These measured guards are annotated in the source.

## Both Q alternatives remain open

The direct Cart substitution test keeps public Cat unchanged and replaces
only Q's Hom by nested Cartesian classifiers. It fails at the definition
of the existing raw representation: its inner mapping target is not the
Cartesian target. A genuine Cart implementation needs its canonical Cart
representation/admission and higher-action interfaces; this failed literal
substitution does not test such an adapted implementation.

The [finite profile comparison](strict_fibcov_review.md#what-strict-ff-does-not-settle)
still gives the substantive constraint: the prescribed u/index projection
for a noncommuting E[α] fits lax Q, while inner Cart would require that
square to commute strictly. Keeping strict FF does not impose this extra
condition on E. Neither a silent family restriction nor an exclusive Q
selection is made here.

## Validation boundary and next root

The final candidate passes **96 positive / 33 negative assertions**,
including the 65/27 donor. Twelve variants fail as intended: eight at
consumer assertions, two at dependent subject-reduction checks, and two
at definition formation (Cart substitution and missing index transpose).
The final run took 1.755s and 171,336KiB maximum child RSS, serially with
subject reduction enabled under the default 90s/2GiB profile.

The LHS audit reports zero unreviewed slots. Warnings change 742→815.
The 73 added bodies have exact hashes, participant heads and owner-group
records. They concern projected Q units, represented composition/inclusion
and fixed-x source-action projection orders. The listed observations check
concrete joins; complete symbolic join certification is not claimed.

This establishes checked whole-y and fixed-x u/y/v/f behavior **under the
declared Q/mate contracts**. It is not the complete homd_id_int root, a
full coefficient-model theorem, intrinsic-cell qualification, Sigma-Hom
integration, or production promotion. Legacy joint Cartesian contracts
remain in the donor, so local negative tests do not certify consistency.

The next root candidate moves T to the represented section target. If
Γ:CoAt2(K)→C is the correctly profiled represented x-package and
C=Functor_cat(K,Q), then the category-level duality identity gives

```text
S'_E = Hom_{CoAt2(C)}(ιE, CoAt2(Γ)(−)) : K → Cat
S'_E[x] = T(S_E(x)).

candidate homd_id_int(E) : Transf_{K,Cat}(E,S'_E)
candidate x-component   : E[x] → T(S_E(x)).
```

Here CoAt2 appears because reversing dimension 2 of C reverses dimension 1
of its Hom category. This is a coordinated proposed root presentation;
it avoids forming T(E) as a same-default family. It has **not** been checked
as a native root construction. Γ, its higher action, root naturality and
the connection to the checked fixed-x owner must be tested next. The source
component can be transposed at each fixed x using the ordinary strict-functor
duality to recover T(E[x])→S_E(x); this does not transpose a whole arbitrary
Cat-valued family. The root must retain its required ambient transformation
profile even if the external FF classifier is strict.

Replay all variants serially after relevant changes:

```bash
python3 audits/strict-default-action-boundary/strict_homd_section_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_homd_section/candidate.lp
python3 scripts/audit_rule_lhs.py tmp/probes/strict_homd_section/candidate.lp --strict
```
