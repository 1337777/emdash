# Whole intrinsic composition of two lax displayed maps

Date: 2026-10-16
Predecessor: `1ac8e002`
Status: checked native two-map composition and its projection ladder; whole unit/associativity, expanded cell factorization, general coefficient coherence and full migration remain open
Owner: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [exact verification](production_intrinsic_composite_verification.json)

## Construction and computation

For admitted E, D, C : K -> Cat_cart, let FF : E => D and GG : D => C
be arbitrary default lax displayed transformations. Write H_E for the Homd
target family, m_F for Homd_target_map(FF), h_E for the ordinary view of the
identity Homd root, and eta_F for the existing intrinsic modification:

```text
m_F : H_D -> H_E
r_F = homd_int(FF) o FF
eta_F : r_F => h_E

W_F = Hom_(Catd(K))(FF, m_F)
eta_(GG o FF) = eta_F o W_F[eta_G].
```

The target-map comparison m_(GG o FF) = m_F o m_G checks for both ordinary
diagram composition and the public Catd composition. It uses native strict
Hom source action and fixed postwhiskering. The whole modification body
uses the actual two intrinsic modifications; there is no new supplied cell.
The two small [endpoint comparisons](production_intrinsic_composite_views.lpfragment)
constrain the actual target map, families and displayed operands.

Before adding a native-composite rule, the independent whole body was
checked through x/u, y, v, p and the entire filler functor. The
[native root computation](production_intrinsic_composite.lpfragment) now uses
that same body. The [projection-order computations](production_intrinsic_composite_projection.lpfragment)
join the existing component heads to it:

```text
Phi_(GG o FF)(p,u,v)
  = Phi_GG(p, FF[x](u), FF[y](v)) o Phi_FF(p,u,v).
```

The [reviewer](production_intrinsic_composite_controls.lpfragment) starts
from the whole constructed modification and compares the native root,
section, y-component, index and filler observations. It also checks an
arbitrary higher filler and rejects its collapse to identity.

At the transported identity, the checked result is precisely:

```text
lambda_(GG o FF)(p,u)
  = Phi_GG(p, FF[x](u), FF[y](E[p](u)))[lambda_FF(p,u)].
```

This retains the first extracted cell as actual input to the second
intrinsic action. The further equality with
GG[y][lambda_FF(p,u)] o lambda_GG(p,FF[x](u)) is still to be qualified from
the intrinsic action's fibre-variable naturality. It is not claimed as an
already checked expansion here.

## Necessary owner changes

The [rigid Hom next action](production_hom_next_action.lpfragment) uses the
existing precomposition/postcomposition factorization. Hom_func and its
object head remain stable; its next Hom exposes the existing whiskering
owners. Displayed fixed whiskering uses the original composition action
with an identity in the other argument. The ordinary view of Cartesian
horizontal composition keeps both actual strict transformation inputs.
The component observation of fixed prewhiskering has matching object and
next-Hom projections. No unrestricted lax interchange equation is added.

The [represented image](production_homd_core.lpfragment) is now a stable
Homd_coeff_rep head. Its whole represented functor remains the existing
defined Cartesian postcomposition functor. Object and higher observations
use its actual body, with a guarded proof-time whole agreement. Source
reindexing retains the represented head through repeated composition. The
[Q reindexing owner](production_q_reindex.lpfragment) recognizes that same
head; no general coend or factorization-quotient operations are introduced.

An inferred endpoint in the initial represented rule incorrectly recovered
C as P(C). The selected rule explicitly matches the normalized P(C) target;
the previous failing normal forms and receipts are retained in the evidence.
Inlining the entire section projection also lost the T(S) orientation in
subject-reduction inference. The two typed intermediate **definitions**
fdapp1_int_comp_section and fdapp1_int_comp_index resolve this. They are
ordinary projections of the shared defined whole body, not independent
primitives or caller arguments.

The experimental generic Catd/ordinary-diagram composition unifier was
removed after the full focused reviewer passed without it. The prior
extra target-family and Sigma fibre-composition experiments remain
unselected.

## Validation and limits

The final generated intrinsic_composite_prefix.lp passes with subject
reduction and warnings enabled in 7.829 seconds, under the unchanged
90-second / 2-GiB / 64-MiB serial resource profile. Its 192 positive and 45
negative assertions include the inherited corpus; the new reviewer adds
12 positive and two negative assertions. These counts describe coverage,
not semantic completeness. The strict LHS audit reports zero unreviewed
clauses or slots.

At the same original-source boundary, warning comparison records 1629 to
1829 critical-pair reports, with 215 added and 15 removed. The evidence
records exact groups and body hashes. They concern represented image/body
and constant/unit observations, rigid next-Hom action, fixed whiskering,
Cartesian inclusion/component observations, and the native composite's
interactions with generic composition and its projection ladder. The
whole-to-filler and higher-action consumers qualify the stated computation.
Whole identity/associativity overlaps, mapped-composite interactions and
general Q/mate coherence are **not** certified by these passing consumers.
No global confluence or unrestricted Q model is claimed.

The full generated source retains the original downstream declarations and
still fails at the old coefficient of Op_prof in section 18b. Production
source has not been promoted. Next qualify the whole intrinsic unit and
associativity comparisons and the expanded extracted-cell formula, then
continue the original later owners, including fdapp1_projection_target.
Whole duality/inverse compatibility, public diagnostics, downstream review,
catalog, health and CI remain required.

Replay from emdash2:

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py \
  --package-root tmp/probes/production_owner_migration/package \
  --no-colors --quiet intrinsic_composite_prefix.lp
python3 scripts/audit_rule_lhs.py --strict \
  tmp/probes/production_owner_migration/package/intrinsic_composite_prefix.lp
```
