# Strict displayed maps with ambient sections: native comparison

Date: 2026-10-14
Status: non-library classifier/action comparison; public default not changed
Plan: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [exact verification](strict_displayed_maps_verification.json)
Replay: [strict_displayed_maps_replay.py](strict_displayed_maps_replay.py)

## Tested interface

The user's proposed strict Functord can be represented internally without
making every Cat-valued Transf strict. The comparison uses probe-only names
so it does not silently select or migrate the public default:

```text
Obj(sf_family_cat(K)) = Functor(K,Cat)
Hom_sf_family(E,D) = sf_family_map_cat(E,D)
Obj(sf_family_map_cat(E,D)) = StrictTransfor(K,Cat,E,D).
```

The strict carrier and stable strict_transfor view are copied exactly from
the native pinned profile declarations. No operational equality/naturality
proof accompanies an FF variable. The whole inclusion is

```text
sf_family_include(K) : sf_family_cat(K) → Functor_cat(K,Cat).
```

Its first Hom is the whole map sf_family_map_include. Its object projection
is strict_transfor(FF), and higher cells between admitted maps use the
ambient modification category between their views. Thus this comparison
restricts map objects without replacing every higher Hom by a Cartesian
one. The inclusion, its projections and canonical category structure are
declared structural operators, not theorems derived from matching objects.

For an admitted FF, the two naturality routes compute to the same whole
fibre functor:

```text
D[p] o FF[x] = FF[y] o E[p].
```

The new runtime clause is restricted both to the native strict view and to
Cat-valued transformations. It is not the rejected codomain-only global
strictness rule. Identity/composition views and canonical constant sections
are also checked. The exact identity of the extracted intrinsic laxity cell
is not newly qualified in this prefix; full Homd/extraction integration
still needs its actual owner tests.

## Why sections remain on the ambient side

The comparison section category is a definition:

```text
sf_section_cat(E) := Transf_cat(K,Cat,const(1),E).
```

It introduces no primitive Pi. The native constant-family object comparison
and component rule are relocated unchanged from the source pin. Arbitrary
ordinary functors F:K→A remain sections of const(A), and evaluation computes
to F[x]. The identity diagram of categories is an explicit nonconstant
consumer. It is rejected as a strict displayed map. Canonical constant
sections have a direct strict constructor and their inclusion evaluates to
the original constant-functor carrier.

The higher-cell observation initially failed because a bare comparison of
reducible Hom aliases attempted to identify the strict family-map category
with the ambient Transf category. Stating the variable modification in
their common canonical Hom classifier fixes that diagnostic typing; no
cast, category equality or new unification rule was added.

This is evidence for separating strict maps and ambient sections, not
permission to keep the current public Functord/Transf and Pi/Functord
identifications after redefining Functord. Those public comparisons and
their actual consumer closure still require migration if this option is
selected. The intrinsic extractor's ordinary lax internalizations must
remain on the ambient side as well.

## Checks and qualifications

The final warning-enabled candidate passes **54 positive and 22 negative
assertions**, including the Gray-evaluator donor. The new classifier slice
contributes 12 positives and six negatives. It checks variable-FF naturality
as a whole functor equality, inclusion projection and category identity/
composition, retained modification data, and the section separation above.

Seven variants fail at their intended assertions: removing strict
naturality, the map-action projection group, the capped higher projection,
the identity view or the constant view; adding automatic reverse admission;
and changing sections to the strict-map classifier. A separate variant
removing only the map's object projection fails subject reduction of the
higher projection. That last failure records a typing dependency; it is not
counted as an assertion-level semantic counterexample.

The final check took 4.517s and 141,996 KiB maximum child RSS, under the normal
90s/2GiB profile with subject reduction enabled. All checks were serial.
The LHS audit reports zero unreviewed slots and 23 annotated slots in 16
clauses. Warnings increase from 667 to 740: 73 added bodies, none removed.
The verification records each added body's hash and owner family. Restricting
the new naturality clause to its actual Cat-valued consumer avoided five
reports from the initially broader candidate. Complete symbolic joins are
not certified by this inventory.

The experiment retains the donor's public Catd/Functord facade and adds
distinct probe classifiers; it therefore does not claim a completed public
rename or downstream migration. Neither the full identity Homd root, lax Q,
general Sigma, whole inverse/coherence nor the independent Cartesian
composition boundary is settled. The donor has known legacy contracts;
local negative checks are not a global consistency certificate. No production
source, check membership or default meaning has changed.

## Replay trigger

Replay after changes to the native strict carrier, constant-section rules,
donor, or candidate fragments. From emdash2:

```bash
python3 audits/strict-default-action-boundary/strict_displayed_maps_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_displayed_maps/candidate.lp
python3 scripts/audit_rule_lhs.py \
  tmp/probes/strict_displayed_maps/candidate.lp --strict
```

Run the verification's adverse variants serially and distinguish assertion
failures from the one expected subject-reduction failure. The replay pins
native excerpts and candidate inputs; generated sources and logs stay ignored.
