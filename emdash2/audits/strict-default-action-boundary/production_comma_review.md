# Corrected comma sections and intrinsic laxity projection

Date: 2026-10-16
Predecessor: `294d5be1`
Status: original section 18zz and its comma/laxity consumers check; the full source next fails at the moving PathOut motive family
Owner: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_comma_verification.json)

## Existing comma construction with coordinated dualities

For F:A->B, put P_b(a)=Hom_B(F[a],b), so P_b:T(A)->Cat_cart.
The migrated definition is the negative total

```text
CommaFib_F[b] = O(Sigma_{O(A)} O(P_b)).
```

The inner total-fibre duality changes the parameter base from B to R(B).
The outer total-fibre duality restores B. CommaFib_catd is an actual whole
composition using hom_con_int, R, TotalOp_catd_func and the existing Sigma
total. Its object remains (a,h:F[a]->b). SelfComma_catd is still its pullback
along F. The canonical identity section retains object (u,id_Fu), transported
object (u,F[h]) and arrow (h,id_F[h]).

The covariant represented mirror now has base O(A) and fibre
O(PathOut(A,y)). Its existing object and arrow constructors remain; the old
T(A) base is not silently equated with O(A). This is migration of the late
extraction consumer, not a replacement for the direct Homd ladder.

Two required coefficient operations are exposed at their owning positions:

- [Sigma_coeff_func](production_sigma_coefficient.lpfragment) is the
  Cartesian restriction of totalization. It has the same Sigma objects and
  sends a classified strict diagram map to the existing sigma_map_func of
  its ambient view. The whole ambient-inclusion comparison checks. It is a
  canonical structural restriction, not a theorem derived merely from the
  raw Sigma_func signature; general lax Sigma-map inputs remain available.
- [TotalOp_funcd](production_total_op_parameter.lpfragment) is the total-dual
  analogue of Op_funcd for strict family maps. Its component is the total
  opposite of the original component functor. It supplies the actual map
  projection of TotalOp_catd_func needed by the comma construction.

The Cartesian restriction is consistent with the strict Grothendieck
functoriality in [Ara–Guetta v3, Proposition 94](https://arxiv.org/html/2503.08832v3#S7).
That result supplies semantic context, not a qualification of our native
formulas or a new general-model claim. The original direct family and
projection computations are checked separately here.

## Arbitrary intrinsic action uses the existing ladder

Write h_E for homd_int(id_E) and r_F for homd_int(FF) o FF. The original
projection endpoint names now have the actual corrected types:

```text
fdapp1_projection_source(E) = h_E : E -> H_E
fdapp1_projection_target(FF) = r_F : E -> H_E
eta : Transfd(r_F,h_E).
```

Since the x-fibre of H_E is T(S_E(x)), its u-component has the required
forward direction in S_E(x). The [projection definitions](production_comma_projection.lpfragment)
then use the existing Q component, Cartesian fibre Hom, weaker P-index
arrow and ordinary filler functor, in order. No Op_funcd of a raw lax FF is
used. Every rung takes the arbitrary eta and projects it; specializing eta
to fdapp1_int_transfd(FF) recovers the existing native action heads.

The public functord_laxity_transf remains a definition through the same
whole projection functor, evaluated on fdapp1_int_transfd. Its component is
the existing fdapp1_int_cell obtained at the transported identity. The
source-fibre arrow action still uses the identity graph's transported arrow.
No independent laxity witness, caller equality argument or global
strict-naturality equation is introduced.

## Presentation issues resolved at their original owners

The ordinary and displayed component-of-composition rules repeated inferred
source/target presentations in their LHSs. The arbitrary eta projection
exposed equivalent but differently presented Homd targets, so those rules
did not fire. Their inferred outer arguments are now underscores; the
actual composite still supplies all categories, endpoints and operands.
Their existing RHS computations are unchanged.

The projection endpoint bodies and eta binders retain the canonical
Homd_target_index_func image. A scalar conversion check initially failed
because the independently inferred eta binder types normalized through two
different target-family presentations. A diagnostic normalized both scalar
action bodies to exactly the same 16,971-character expression. Explicit
@Transfd binders at the original interface and in the diagnostic resolve
that mismatch. This did not require changing the source-fibre action,
strictifying FF or adding a new coherence rule.

The two already owned strict-functor/pre-right extraction rule fragments are
inserted after the comma section is migrated. They remain unique authoring
sources; the new comma fragment does not carry frozen duplicate copies.

## Checked boundary and continuation

The [reviewer](production_comma_controls.lpfragment) adapts the original
self-comma/mirror, arbitrary projection, extracted-cell and source-fibre
action checks. It additionally checks the whole Cartesian Sigma view and
total-dual map component. Negative controls reject a raw lax map as a
Cartesian input, strict naturality for arbitrary FF, and the old transpose-
only mirror base. All preceding foundation/Homd/profunctor/join controls are
included. Subject reduction, warnings, the normal serial 90-second/2-GiB
profile, 64-MiB file limit and OCAMLRUNPARAM=o=20 remain enabled.

The full emitted source preserves the original later declarations and next
fails at PathOutMotives_catd. Its older public-Cat PathOut family is being
fed to the now-Cartesian varying-base classifier. Review the canonical
PathOut family using the available Cartesian totalization restriction, then
continue the moving Pi/motive owners. Public/downstream integration, remaining
consumed compatibility checks and final gates are still required. This
checkpoint is a non-library authoring migration, not production promotion
or a complete omega-level model proof.

Replay from emdash2:

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py \
  --package-root tmp/probes/production_owner_migration/package \
  --no-colors --quiet comma_prefix.lp
python3 scripts/audit_rule_lhs.py --strict \
  tmp/probes/production_owner_migration/package/comma_prefix.lp
```
