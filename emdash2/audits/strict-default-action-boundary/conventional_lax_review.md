# Conventional lax default with the retained public Cat universe

Date: 2026-10-14
Status: native owner candidates checked; not promoted; closure and duality integration remain open
Owner: [living foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [exact checks and warning comparison](conventional_lax_verification.json)

## Selected meaning

The user selected conventional lax transformations as the default, retaining
the pre/right extracted leg as identity and the post/left leg as directed:

```text
L_p = G[p] o epsilon[x]
R_p = epsilon[y] o F[p]
M_p = epsilon[p]

M_p = R_p, with the pre/right cell an identity
L_p => R_p remains potentially noninvertible.
```

This is uniform for ordinary and Cat-valued transformations. Functord remains
their displayed presentation. There is no new StrictTransfor premise,
lax_transfor wrapper, standalone laxity witness or operational proof payload.
Functor objects are strict by the selected migration, and
Hom_cat(Cat_cat,A,B)=Functor_cat(A,B) is retained.

The old raw two-leg default is not the selected public doctrine anymore.
This permits using the conventional lax profile as the target of the native
action migration; it does not prove that all existing raw operations have
that profile. In particular, neither Cartesian joint evaluation nor the
old same-profile dimension-one transpose is justified by this decision.

## Native owner checks

The [replay](conventional_lax_replay.py) starts from the exact main pin
f8af1fca472657ff1598c639eb29c0566e7b2ec0. It restores the existing strict-functor
owner rules, then uses the existing conventional-lax profile's pre/right
action pattern without a carrier wrapper. The
[intrinsic rule](conventional_lax_intrinsic.lpfragment) acts on
fdapp1_comma_projection_transf of tapp1_con_at_transf, exactly the extracted
whole pre/right cell owner. It returns the identity at the existing left
endpoint; no new comparison cell is declared.

| Check | Result | Scope |
| --- | --- | --- |
| Ordinary prefix baseline | 3 positive / 6 negative | Public Hom and strict functor action, without default pre rules |
| Ordinary candidate | 7 positive / 2 negative | Whole/capped pre computation; post conversion and typed-reflexivity negatives |
| Remove default pre rules | Expected failure | First positive pre computation |
| Full-snapshot intrinsic owner | 9 positive / 3 negative | Extracted pre cell is identity; post cell is still derived and an identity does not inhabit its general type |
| Remove intrinsic identity rule | Expected failure | The extracted pre-cell identity assertion |

All runs used subject reduction, 90 seconds, 2 GiB memory and 64 MiB file
limits. The warning-enabled ordinary and full intrinsic runs took 3.737s
and 13.832s. LHS audits report zero unreviewed inferred slots.

These are owner checks, not a full foundation qualification. The ordinary
prefix omits the old same-profile transpose and does not implement its
replacement. The full-snapshot variant retains known legacy opposite and
Cartesian operations; its successful typing cannot certify their semantics
or noncollapse. An attempted native equality via the old transpose failed
with endpoint/category unification obligations and is recorded as an
unqualified attempt, not a checked adverse theorem.

Warning comparison: the ordinary candidate adds 62 critical-pair reports
to the 433-report baseline. Their classes are whole endpoint projection,
opposite/terminal composition, source-action projection, structural
off-diagonal projection, identity components and vertical composition.
Typed projection-order qualification remains open; the count is not a
confluence result. Adding the deep intrinsic identity rule changes none of
the 913 full-snapshot critical-pair bodies. Exact bodies and classifications
are in the verification JSON. No kernel rule is promoted by these results.

Replay when the ordinary action, intrinsic extraction, duality or joint
composition owners change:

```bash
python3 audits/strict-default-action-boundary/conventional_lax_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 EMDASH_TYPECHECK_TIMEOUT=90s OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/conventional_lax_default/ordinary.lp
EMDASH_LAMBDAPI_WARNINGS=1 EMDASH_TYPECHECK_TIMEOUT=90s OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/conventional_lax_default/full_intrinsic.lp
```

## Typed projection-order comparisons

The [projection replay](conventional_lax_projection_replay.py) retains the
exact preceding candidates and adds two proof-time readings of tapp1_fapp0
against ordinary composition. The ordinary reading keeps the common
codomain as a discriminator. Its opposite-codomain counterpart accounts
for composition having already reversed the factor order. Neither changes
runtime normal forms or supplies an operational proof argument.

Four typed eq_refl definitions now check after earlier projections:

- F is the identity, so F[p] has reduced to p;
- F is a composite, so its action is a nested pair of actions;
- the transformation is a vertical composite, whose component has reduced;
- the codomain is Op_cat(B), whose composition has already reversed.

The last declaration needed explicit source/codomain arguments on its
object observations. Obj(Op_cat B)=Obj(B) does not preserve enough information
for every omitted argument to be inferred correctly. This was an observation
typing correction, not a new equation between B and Op_cat B or its endpoints.

The ordinary slice passes the four definitions and its 7 positive/3 negative
assertions; the full snapshot passes the same definitions and 9 positive/4
negative assertions. The additional negative rejects post strictness in an
opposite codomain. Removing the ordinary reading fails the identity-source
consumer; removing the opposite reading fails the opposite-codomain consumer.
Both readers are therefore required for these consumers. Exact evidence is
in [the projection verification](conventional_lax_projection_verification.json).

Critical-pair bodies are unchanged: 495 in the ordinary slice and 913 in the
full snapshot. The full LHS audit still has zero unreviewed slots. These
typed comparisons do not close every earlier constructor or whole-action
projection case, and they do not qualify the legacy opposite operator or
joint Cartesian contracts. The inherited legacy-op equality attempt remains
an unqualified endpoint/category inference failure. No rule is promoted.

## The joint-action boundary also reaches Sigma maps

The [finite strict 2-category checker](mixed_family_profile_models.py) now
records the same noncommuting lax square at a concrete Sigma consumer. Let
K and C be walking arrows, with constant families D=const(C), E=const(B).
Choose strict H,J:C->B and a conventional lax comparison epsilon:H=>J with
distinct boundary paths

```text
J[h] o epsilon[0] => epsilon[1] o H[h].
```

These are the component functors and comparison of a conventional lax
displayed map FF:D=>E over K. Both families and every fibre transport are
strict. The existing constant-Sigma contract gives Sigma(D)=K x C and
Sigma(E)=K x B. A total map with the existing prescribed object values must
send the two factorizations of the same mixed source arrow to the two paths
above. In the chosen B, each of the four target edges is unique, and those
composites are distinct. No strict functor with those object values exists.

This is a finite semantic counterexample to the combination of constant
Sigma as product, arbitrary conventional lax FF, and the current strict
sigma_map_func output contract. It does not refute the total of a strict
family or its identity dependent Hom. It shows that moving every Functor
to the strict default requires reviewing Sigma's functoriality as well as
Eval/comp_prod. Selecting one strict leg of FF does not make its other
comparison strictly natural in fibre variables.

The correction must live in the actual joint-action/total-map interface.
Do not hide it by restoring global Cat-valued strictness, discarding lax FF
at an unrelated input, or supplying independent laxity cells. The old
intrinsic extractor also uses these total-map owners, so their corrected
dependencies are part of the Homd migration, not a detached downstream task.
