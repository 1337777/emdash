# Separate Cartesian coefficient: whole canonical family consumer

Date: 2026-10-14
Status: non-library native comparison checked; public migration remains open
Plan: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Design: [comparison matrix](../../../docs/EMDASH_FOUNDATION_PROFILE_DESIGN_MATRIX.md)
Evidence: [exact verification](cart_family_verification.json)
Replay: [single candidate](cart_family_replay.py)

## Implemented boundary

This continuation uses the existing Cartesian classifier pilot as a separate
coefficient. It retains public Hom_Cat=Functor_cat and the conventional lax
Transf default. Its declarations do not admit an arbitrary E:K->Cat to the
Cartesian family type or make every FF with Cartesian codomain strict.

The new [native owners](cart_family_core.lpfragment) provide

```text
iota_cart : Cat_cart → Cat
family_view(E) = iota_cart ∘ E

I_x : K → Cat_cart
I_x[y] = Hom_K(x,y)
family_view(I_x) ↪ hom_K(x,−)

transport(E,x,y,u) : Hom_K(x,y) → E[y]
transport(E,x,y,u)[p] ↪ E[p](u)

c_E(x,u) : StrictTransfor_{K,Cat_cart}(I_x,E)
c_E(x,u)[y] ↪ transport(E,x,y,u).
```

Category/functor objects and fapp/tapp operations are shared. Cartesian
higher Homs remain distinct from ambient lax modification categories.
The coefficient inclusion's first Hom is the existing whole Cartesian
mapping inclusion. The represented family's first Hom has the Cartesian
postcomposition profile, with a whole inclusion comparison to the existing
ordinary postcomposition telescope and a projection-order join on its
actual two-cell action.

The transport functor is a definition: fixed evaluation after the whole
E_1(x,y) action. The canonical map's base action is likewise a definition
using postcomposition in Cat_cart and the represented family's first Hom.
Its evaluation at q, then p, retains the established stable Hom-composition
index. This is a whole fixed-u map across y, not only a formula at y objects.

The coefficient, its inclusion, the stronger Cartesian Hom presentation and
the canonical strict map are structural owners. Their complete higher
coherence is not claimed to have been derived from the object beta rules.
No equality witness or independently supplied comparison is an operational
input. The whole source-u functor and corrected Q/Homd ladder under this
coefficient are still the next work.

## Actual higher-cell and naturality consumers

For variable E:K->Cat_cart, the two sides of E[alpha]'s fibre-naturality
square compute to the same term. The strictness is obtained from the
coefficient's mapping classifier and the existing native strict-transfor
view, not from a global rule on arbitrary Cat-valued transformations.

The represented-family test also recovers an actual base two-cell alpha
by evaluating its postcomposition transformation at the identity source
arrow. Thus this admission does not force E[alpha]'s components to be
identities. Whole-first and projection-first inclusion observations agree.

This consumer required importing the existing native postcomposition
component rule omitted from the earlier truncated prefix, and adding the
[projected unit-whiskering clause](cart_family_unit.lpfragment) at the
composition-action owner. The rule matches the identity higher arrow in
the first coordinate. A control with a variable higher endomorphism of
the identity 1-cell remains unreduced.

Installing that rule before the old precomposition comparison made its
formerly inferred Product_pair classifiers remain unsolved. Keeping only
the repeated outer endpoint did not fix this. The
[same proof-time comparison with explicit RHS classifiers](cart_family_precomp_reading.lpfragment)
restores the existing typed consumer. This changes inference information,
not the comparison's mathematical content, and retains the unit rule at
its actual owner rather than bypassing the affected declaration.

## Evidence and remaining scope

The final warning-enabled candidate passes with subject reduction enabled
in 1.586s and 155,196KiB maximum child RSS, under the normal 90s/2GiB limits.
Its focused consumers cover the family/inclusion, strict fibre naturality,
canonical y-map and actual two-cell recovery. Relevant negatives retain
the distinct public Hom, reject automatic Cartesian family admission,
reject automatic strict FF and preserve the nonidentity first-coordinate
case of the unit rule. No removal matrix was added.

The LHS audit has zero unreviewed slots. Critical-pair bodies change
740->897, with none removed. The verification inventories the added bodies
under unit whiskering, the imported Cartesian profile, coefficient
inclusion/units, represented Hom, strict-view naturality and canonical
transport. This is warning review plus the listed concrete consumers, not
complete symbolic-join certification.

The result supports the proposed coefficient's native usability. It does
not select a new public Functord or section classifier, finish the Homd
ladder, qualify the full Q theory, or solve the independent public-universe
Cartesian-composition counterexample. No production owner/check membership
changed. The remaining production carrier-relocation edits are outside
this checkpoint.

Replay after changing the coefficient, strict view, canonical Hom/transport
or shared composition/projection owners:

```bash
python3 audits/strict-default-action-boundary/cart_family_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/cart_family/candidate.lp
python3 scripts/audit_rule_lhs.py tmp/probes/cart_family/candidate.lp --strict
```
