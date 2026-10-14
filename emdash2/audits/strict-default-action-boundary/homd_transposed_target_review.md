# Whole Homd root with a transposed section target

Date: 2026-10-14
Status: non-library whole-root candidate checked; full foundations qualification open
Plan: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [exact verification](homd_transposed_target_verification.json)
Replay: [authoring replay](homd_transposed_target_replay.py)
Root: [declarations and projection owners](homd_transposed_target_root.lpfragment)

## Construction and corrected variance

E:K→Cat and its transports have the selected strict-functor default.
E[α] may still be a lax transformation. Write T=Op_cat for dimension-one
transpose, C₂=CoAt2_cat for reversal of exactly dimension two, and retain
the preceding candidate's raw curried Q. Public Hom_Cat=Functor_cat is
unchanged. Both Q design alternatives remain under review; this construction
uses the raw-Q candidate rather than silently substituting nested Cart.

Let I_x=Hom_K(x,−), C=Functor_cat(K,Q), and ιE denote the included diagram.
The preceding checkpoint already constructs the whole section category
and fixed-x source functor:

```text
S_E(x) = Hom_C(ιE,ιI_x) = Transf_{K,Q}(ιE,ιI_x)
h_E,x : T(E[x]) → S_E(x).
```

The represented x-package now has a whole native owner:

```text
Γ : C₂(K) → C
Γ[x] = ιI_x
Γ₁(x,x′) = h_{I_x,x′}
          : T(Hom_K(x,x′)) → Hom_C(ιI_x,ιI_x′).
```

Thus Γ's first Hom is the already checked Homd source functor specialized
to a representable family. Its arrow image at p:x→x′ is the represented
section for I_x at (x′,p). No generic contravariant functor on arbitrary
lax modifications is assumed. A two-cell α:p⇒q acts Γ[q]⇒Γ[p]; the next
Hom retains the original direction of a three-cell α⇒β. The controls
distinguish C₂ from both T and R=CoAbove2, and reject replacing Γ's source
by R(K).

The crucial coordinated change is to put T on the section target:

```text
S′_E = Hom_{C₂(C)}(ιE, C₂(Γ)(−)) : K → Cat
S′_E[x] = T(S_E(x)).
```

This is an actual definition through ordinary Hom and the ordinary strict
functor C₂(Γ), not a family specified only at objects. It works because
Hom_{C₂(C)}(a,b)=T(Hom_C(a,b)) and C₂(C₂(K))=K. The imported CoAt2 fragment
contains only category duality and its action on ordinary strict functors;
the old Cartesian mapping-category duality declarations are excluded.

The new structural identity root has the Lambdapi type

```text
sf_homd_id_int(E)
  : Transf_{K,Cat}(E,S′_E).
```

Its x-component is E[x]→T(S_E(x)). It projects to T(h_E,x), and transposing
that individual strict functor recovers h_E,x. Objects of T(S_E(x)) and
S_E(x) coincide, so applying the x-component to u gives the actual whole
y-section, with the existing direct y/v/f ladder. The categories are not
identified: a negative control rejects reading the x-component as
E[x]→S_E(x).

In particular, the **full identity-root** projection computes:

```text
root → x → u → y → v → f
     ↪ Hom_E[y](E[f](u),v).
```

There is no fibrewise T(E), larger y/v/f context, curry workaround,
primitive Pi, operational equality payload or supplied comparison cell.
The root is an ambient potentially lax transformation; it is not silently
admitted to the strict displayed-map classifier.

## Action checks and structural laws

The whole pre/right x-action is defined by fixed postcomposition with the
x′-component after E₁(x,x′). At p:x→x′ it sends u to the section at
(x′,E[p](u)). The actual target-family action on the canonical section
computes to the same object value. This is not a claim that the entire
two boundary functors agree or that the extracted comparison is identity.

At a nonidentity base two-cell α:p⇒q, evaluation at u computes to the
existing source-u action for E[α][u], with the appropriate reversed section
Hom. A variable endomorphism α does not reduce to identity. The diagnostic
uses a canonical Hom_cat return type; a bare Hom-alias comparison had
prematurely inverted the transposed source.

The represented mate gets its canonical representable identity and
composition projections. These are explicit structural computation laws,
not theorems derived from an independent general Q tensor. Together with
the preceding canonical transport-map computation, they give Γ's identity
and a typed composition comparison. That comparison needs one scoped
proof-time reading of the stable Hom-composition index; an unrelated base
arrow remains unequal. Runtime retains the stable index form.

Two whole Hom-action observations are also implemented: Hom postcomposition
under C₂ becomes T of the original Hom functor, and reindexing along the
named Γ exposes its actual image arrow. The corresponding identity-family
precomposition observation is used by the relative root.

## General FF and the strict wrapper

Under this Q contract, external FF need not be strict for the relative-root
construction. A raw FF:D⇒E has its covariant diagram image ιFF. Ordinary
represented precomposition in C₂(C), indexed along C₂(Γ), defines

```text
Homd_target_transf(FF) : S′_E ⇒ S′_D

homd_transf_int(FF)
  := Homd_target_transf(FF) ∘ homd_id_int(E)
   : Transf_{K,Cat}(E,S′_D).
```

The experimental strict-FF names are wrappers applying this same construction
to the native inclusion of an admitted strict displayed map. They do not
introduce another primitive Homd theory. Raw FF remains rejected by
StrictTransfor and by the explicitly strict wrapper's input type.

After x/u projection, the general relative root agrees **proof-time** with
the actual compositional section

```text
h_E(x,u) ∘ ιFF : S_D(x).
```

That defined section view computes through y/v/f to
Hom_E[y](E[f](u),FF[y](v)), without any strict-naturality equation for FF.
Identity strict FF also recovers the identity section directly after root
x/u projection. The literal lower projections of the raw relative root
are not separately claimed to normalize all the way to this leaf: the
checked whole-section comparison uses the existing stable precomposition
versus raw-composition reading.

This removes the preceding *typing/construction* reason to require strict
external FF for Homd. It does not settle strict Sigma-map admission or
change the public Functord default. The donor still has the ambient
Catd/Functord facade. If that facade is narrowed, the Hom_int target action
must use the appropriate ambient inclusion rather than the old automatic
identification. Intrinsic ordinary lax internalizations must remain admitted.

## Validation and remaining work

The final candidate passes **122 positive / 42 negative assertions**,
including the 96/33 donor. Thirteen adverse variants fail as intended:
ten at consumer assertions, two at dependent subject-reduction/variance
checks, and one at root formation. In particular, the untwisted target
reintroduces the unsolved constraint C₂(K)=K; replacing Γ's source by R(K)
gives O(Hom_K) where the actual first-Hom owner needs T(Hom_K).

The final warning-enabled run took 3.255s and 180,992KiB maximum child RSS
under the default 90s/2GiB profile, serially with subject reduction enabled.
The LHS audit reports zero unreviewed slots. Warnings change 815→898;
all 83 added bodies have hashes, participant heads and owner groups in the
verification. Complete symbolic join certification is not claimed.

The signed whole interface and the listed computation now have a native
candidate. The following remain required before the goal is complete:

- intrinsic comparison-cell extraction under this root, including the
  retained noninvertible action rather than only its endpoint types;
- complete Q/mate composition and higher coherence, and the coupled joint
  evaluation/composition and whole-duality qualification;
- corrected Sigma-Hom formation/action and its actual admission profile;
- public owner migration, downstream consumers and the required full gates.

Q, Γ, the mate and Homd root remain explicit structural owners in this
experiment. This is not a derivation of an independent coefficient model.
The donor also retains known legacy joint Cartesian contracts. Passing
local negatives is not a global consistency certificate, and no production
owner or check membership changed in this tranche.

Replay from emdash2, then run the verification's variants serially:

```bash
python3 audits/strict-default-action-boundary/homd_transposed_target_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/homd_transposed_target/candidate.lp
python3 scripts/audit_rule_lhs.py tmp/probes/homd_transposed_target/candidate.lp --strict
```
