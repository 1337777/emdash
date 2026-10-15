# Native section action and constant-functor higher cells

Date: 2026-10-15
Status: staged original source checks through section 16e; later core and
coefficient coherence remain unqualified
Owner: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Predecessor: `95d73ac64928c10d3c055bc6e1bfd78d8337fceb`

## Existing Pi with the corrected index

Write T=Op_cat, R=CoAbove2_cat and O=TotalOp_cat. The coefficient Hom remains
Hom_Q(A,B)=Cart(A,P(B)), with P(I)=T(Functor_cat(I,T(Cat_cart))). This tranche
does not change the direct Homd y-binding, which is Transf(K,Q).

For s:Pi(E), let I=Hom_K(x,y) and H=homd_(id_E,x,s[x],y,s[y]). The original
section-action name now has the type

```text
piapp1_func(E,s,x,y) : Obj(Pi_cat(O_fib(H)))
O_fib(H) : Catd(O(I)).
```

Its body maps the existing terminal-source fdapp1 intrinsic P-arrow through
A_I:R(P(I))->Catd(O(I)). No new Pi constructor or separate naturality cell
is introduced. The original piapp1_fapp0 still computes the extracted
fdapp1_int_cell. The old positive Pi over T(I) is rejected for general E.

The first Hom of section_total_func now uses O of the recursive total over
O(I), with these same total-dual fibres. Expanding that route independently
computes the original structured total arrow (p,s[p]).

## A whole constant-family specialization

The old source provided only the point comparison between constant-section
action and ordinary F[p]. Its whole total-section projection comparison did
not propagate automatically through the first Hom: the generic action cut
erased the original comparison pattern. This is recorded as a failed check,
not treated as evidence for an unverified higher equation.

The new [constant-index constructor](production_homd_index.lpfragment) is a
derived whole functor. Put

```text
c_H = T_func(Const_catd(T(I),H)) : Obj(P(I)).
C_I,H : Functor_cat(I,H) -> Hom_P(I)(c_1,c_H).
```

C is constructed from the actual return map
B_I:Catd(O(I))->R(P(I)), its first Hom on the two constant families, and
the existing whole total-duality map. Callers supply an ordinary functor F;
they supply no equality certificate, chosen comparison or inverse witness.
The constant consumer computes

```text
A_I,1(C_I,H[F])  ->  O_func(F).
O_func(A_I,1(C_I,H[F]))  ->  F.
```

These are computations on whole functor objects. They do not by themselves
prove a general categorical equivalence or every higher parameter equation
for A_I and B_I. B_I now has a concrete core consumer, rather than remaining
only diagnostic support.

The [native constant-family specialization](production_constant_section_index.lpfragment)
sets the existing fdapp1_int_presheaf_arrow to

```text
C_(Hom_K(x,y)),(Hom_B(F[x],F[y]))[F_1(x,y)]
```

when its source and target families are const(1) and const(B). This is a
whole structural compatibility rule for that constructor; it is **not**
claimed to follow from the old point comparison. The existing lower
fdapp1_int_hom_func, fdapp1_int_hom_fapp0 and fdapp1_int_cell owners get the
same specialization so both projection orders compute. The obsolete
point-only unifier is removed, while its named theorem views remain.

Consequently the actual decoded section action reduces to F_1, and its
action on any alpha:p->q reduces to F[alpha]. Independently, the second-cell
image in the actual Sigma total has fibre F[alpha]. A loop-cell control for
F=id retains alpha rather than identifying it with identity.

F is a strict ordinary functor by the selected default. As a terminal-source
displayed section it remains lax across K: its comparison at p is F[p],
which may be nonidentity and noninvertible. These are different levels.

## Required normalization and profiles

The [coherence fragment](production_index_constant_coherence.lpfragment)
adds only the consumed constant/duality and fixed-postwhiskering laws:

- The canonical Cat_cart-valued constant-functor view normalizes to
  Const_catd. Its T/R, represented Hom, and ordinary postcomposition views
  retain their original constant meaning.
- Two fixed postwhiskerings combine, and identity postwhiskering returns
  the original transformation. Both other transformation legs are identities
  in these rules. A nonidentity second leg is explicitly retained by a
  negative control; unrestricted lax-square interchange is not added.
- The actual Cartesian coefficient duality and R of that same operation
  compose to identity. The same computation is recorded after the composite
  has already formed its TotalOp_catd head. Total duality of the identity
  coefficient family returns the original duality map.

The nonidentity [tdapp1 projection ladder](production_intrinsic_modification.lpfragment)
uses the same Q section, Cartesian fibre Hom and directed P index as fdapp1.
Its actual generic root component reaches tdapp1_int_cell(epsilon,p,u).
An arbitrary loop modification does not collapse to the identity case.

The [controls](production_section_action_controls.lpfragment) exercise these
whole constructions with the inherited foundation, section, Sigma, mixed
family, Homd, intrinsic and index consumers. The
[verification](production_section_action_verification.json) pins exact source,
resource, warning and source-preservation evidence. This remains a non-library
authoring checkpoint; the full emitted source stops at the first unmigrated
sigma_intro_transf component in section 17a.

## Remaining qualification gates

The complete foundations goal is not achieved. In particular:

1. Continue the original late evaluation/weakening and whole extracted-laxity
   owners with their actual profiles, then the remaining kernel/libraries.
2. Review pi_eval_transf before retagging its codomain. With lax section
   morphisms, evaluation across a base arrow has a lax naturality square in
   the section variable; it cannot simply be assumed Cartesian there. Its
   fixed-object evaluation is a separate, already available strict functor.
3. Qualify Q's consumed represented/conjoint composition and mixed-parameter
   coherence on the new directed-index arrows. In particular, do not assume
   that these operations provide strict Cartesian joint index evaluation.
   The walking-arrow constant-index map induced by id_I has unequal endpoint
   components; such a joint evaluation would force them to agree. Whether a
   proposed Q comparison entails that forbidden evaluation must be checked
   before accepting it. No general coend/balancing theory is prerequisite.
4. Qualify the remaining whole duality/inverse and parameter coherence, and
   complete the public source, reviewer, catalog, health and CI gates.

The passing source is evidence for its explicit types and computations. It
does not establish an unrestricted strict Cartesian model of Q, global
confluence, or a complete general A/B inverse theory.
