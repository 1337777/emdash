# Canonical transport map in the strict displayed-map classifier

Date: 2026-10-14
Status: non-library whole-family consumer; full Homd still incomplete
Plan: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [exact verification](strict_fibcov_verification.json)
Replay: [native replay](strict_fibcov_replay.py)
Model: [finite profile comparison](strict_fibcov_profile_model.py)

## Implemented consumer

The preceding strict displayed-map classifier now has a canonical whole-map
consumer needed by identity Homd. Write I_x = Hom_K(x,−). The new structural
constructor is

```text
sf_fibcov(E,x,u) : sf_family_map_cat(I_x,E)

sf_family_map_view(sf_fibcov(E,x,u))[y]
  = fib_cov_tapp0_func(E,x,y,u) : Hom_K(x,y) → E[y].
```

The component is the existing defined functor
`eval_u ∘ E₁(x,y)`, copied from the pinned native source, not a new object-only
transport operation. Its f-value is E[f](u), and its first-Hom action retains
the component E[α][u] for a variable base two-cell α:f⇒g. No rule classifies
E[α] as a strict transformation.

The constructor admits an entire strict displayed map. Its native strict
view is used by the existing transformation projections. This is a declared
structural admission with checked projections, not a theorem inferred from
the object formula. No naturality proof, path, or separately supplied
comparison cell is an input.

The whole y-arrow action is a definition through existing Hom and fixed
postcomposition:

```text
sf_fibcov_action(E,x,u,y,z)
  : Hom_K(y,z) → Functor_cat(Hom_K(x,y),E[z])

q ↦ fib_cov(E,x,z,u) ∘ postcompose(q).
```

Both full and capped tapp1 projections use that owner. The variable
base-two-cell action remains available as an ordinary transformation.
Reading its value at p as E[qp](u) is a typed proof-time comparison; the
ordinary Hom owner retains its stable postcomposition head at runtime.

For FF:D⇒E admitted to the strict displayed-map category, the new whole
constructor computation is

```text
FF ∘ sf_fibcov(D,x,u)
  ↪ sf_fibcov(E,x,FF[x](u)).
```

This acts before selecting y. Identity and composed FF inputs check.
Inclusion-first and component-first observations compare with the same law.
The latter compares entire Hom_K(x,y)-indexed functors, not just their
object values. Three narrow proof-time readings close the measured
inclusion, component and evaluated-index projection paths. Raw ambient FF
does not receive the strict comparison. Distinct u values remain distinct.

## What strict FF does not settle

The latest user instruction explicitly keeps both nested-Cart Q and lax Q
open. Public Hom_Cat(A,B)=Functor_cat(A,B) remains unchanged. The finite
comparison uses the same family data for both coefficient proposals:

```text
E[p]=H, E[q]=J, E[α]=ε : H⇒J

J[h] ∘ ε[0] ⇒ ε[1] ∘ H[h]
```

The two boundary paths are distinct and the cell has no reverse. E and its
transports are strict on the walking-2-cell base; the external FF can be
id_E throughout. Thus strict external FF does not remove this example.

For the prescribed Homd u/v/f projections, the index naturality comparison
has exactly this forward direction. Lax Q accommodates this necessary
local comparison; inner Cart would require equality of its two paths.
A commuting ordinary diamond supplies a positive Cart control with
nonidentity transformation components. The extra restriction concerns
naturality, not whether components must be identities.

| Candidate | Result for this consumer | Remaining qualification |
| --- | --- | --- |
| Q with both mapping levels lax | Required directed cell exists; its reverse does not | Full coefficient and whole root still need construction |
| Q with both mapping levels Cart | Noncommuting example is excluded | Stronger family admission is required for these projections; this test does not establish omega-level sufficiency |

The same finite model isolates a second issue. Moving u through the raw
transport `f ↦ E[f](u)` gives the opposite naturality orientation. It must
not be promoted blindly to an ordinary default-lax functor into the
strict-map category. Taking the contravariant Hom changes the local
orientation back to the required Homd one. This cancellation is a reason to
check the composite construction, not to postulate a generic whole lift
with incorrectly profiled intermediate action.

Likewise, the old outer root's fibrewise dimension-one transpose of E
requires a reversed naturality square, even after reversing the base
two-cell. The square is absent in this example. Total O reverses the cell
as well and passes this local test, consistent with the previously checked
total-duality owner. A coordinated total-O root and its section target have
**not** been constructed by this experiment. The finite model does not
prove that every possible Homd interface is impossible.

## Validation and limits

The candidate passes **65 positive and 27 negative assertions**, including
the donor's 54/22, plus three new typed comparison definitions. Seven removal
variants fail at their intended assertions or typed definitions. The
subject-reduction-enabled final run took 1.519 seconds and 147,220 KiB
maximum child RSS with the normal 90s/2GiB profile. All checks were serial.
The finite model checks the free locally posetal 2-category's composition
and noninvertibility using the existing finite checker.

The LHS audit has zero unreviewed slots. Warnings change from 740 to 742.
The two added symbolic overlaps are recorded with their full bodies and
hashes: canonical family composition against stable represented composition,
and against generic higher-component projection. Their complete symbolic
joins are not certified. The proof-time readings introduce no additional
runtime critical pairs.

This is the first canonical whole-family consumer of the strict displayed
classifier on the current public-universe donor. It is **not** the full
Homd y-section or x/u root, a completed Q coefficient, or a public
Catd/Functord migration. The exact identity of the extracted intrinsic
strictness cell is not newly qualified in this prefix. Existing legacy
joint Cartesian contracts also remain in the donor; passing local negative
controls do not certify global consistency. No production source or check
membership changed in this tranche.

## Next consumer and replay

Continue from this admitted canonical map to its represented Homd section.
Compare the two Q profiles at the required higher u/index action, retaining
the direct y/v/f telescope. Do not copy the old fibrewise-T root declaration
or the old nested-Cart higher lift without the profile checks above. An
alternative outer root may need a coordinated duality of both its source
and section target; changing only its source is insufficient.

From emdash2:

```bash
python3 audits/strict-default-action-boundary/strict_fibcov_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_fibcov/candidate.lp
python3 scripts/audit_rule_lhs.py tmp/probes/strict_fibcov/candidate.lp --strict
python3 audits/strict-default-action-boundary/strict_fibcov_profile_model.py
```

Replay the verification's removal variants serially after any relevant
source change. Replays pin the donor, native excerpts and authoring files.
Generated LP, logs and receipts remain ignored; retained authoring inputs,
review and exact verification form the checkpoint.
