# Native inverse cancellation and extracted-cell boundary

Date: 2026-10-18 (UTC)
Predecessor: `f18c2ecd`
Status: cancellation/reflection prerequisites checked; actual inverse strictness and whole locality remain open
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_inverse_cancellation_verification.json)

This continuation addresses the original locality consumer's need for an
inverse in the Cartesian mapping category. It does not change the Homd
ladder, require arbitrary displayed maps to become strict, or select a new
inverse-assembly assumption.

The original whole left/right inverse laws imply that their composites have
the native strict-transfor property: transport the identity's property along
those laws. This uses the whole paths supplied by the inherited assembly,
without identifying them with the component cancellation paths in `u[x]`.

Two further derived proofs map and reflect `IsStrictCell`. Mapping uses the
existing `path_to_hom_fapp1_agrees` theorem and retains the actual cell's
agreement field. Reflection uses the equivalence's actual selected left
inverse and its whole cancellation law. It is not an additional Core
reflection axiom and does not infer strictness from endpoint equality alone.

A single selected proof-time view at the original internal-action owner
exposes the fixed-source action of `xi o strict(eta)` as represented
precomposition by `eta[X]` after the original action of `xi`. The earlier
factor is classified strict; the later factor remains lax. Its whole and
whole-in-source-arrow comparisons check. Controls reject a raw earlier
factor and replacement of the retained component. This is an explicit
whole computation contract, not a theorem inferred from scalar beta rules.
There is no new runtime rule or inverse primitive.

Combining this view with the original whole left cancellation law proves
strictness of the represented composite's actual extracted action. To cancel
the represented factor, two derived equivalences are now available:

- fixed precomposition by an equivalence, retaining its original inverse
  choices in the contravariantly swapped order;
- fixed postcomposition by an equivalence on ordinary lax mapping categories.

The latter varies only one slot. It does not supply unrestricted Cartesian
joint composition for two varying lax transformations. Both derivations map
the existing inverse laws through the original Hom owners.

Two further proof-time views use the existing rigid `Hom_func` to compare
its two pre/postcomposition factorizations when the target arrow is the
actual image `H[p]`. They preserve the source arrow and mapped base arrow;
negative controls reject either substitution. Together with the internal
composition view, the core regression passes 276 positive/77 negative
assertions plus its derived proof definitions. Critical-pair warning bodies
are unchanged from `f18c2ecd`; the owning LHS audit has no unreviewed slots.

The remaining positive obligation is the **whole** extracted-cell equality
for a canonical represented map `A` and a general lax displayed map `L`:

```
kappa_(A o L)(p) = postcompose(A[y])[kappa_L(p)].
```

The current reflexivity attempt fails at this equality. Endpoint
presentations are no longer the remaining final goal. A pointwise version
is already supplied by the existing intrinsic composition and classified
action projections; it does not automatically give equality of the whole
transformations. The staged core already defines `fdapp1_int_comp_transfd`
from the original two intrinsic modifications and computes its full filler
functor as their composite. The next step is to connect its existing whole
body to the canonical `fdapp1_comma_projection_transf` extraction, retaining
the intrinsic modification argument. Do not install a new independent
laxity cell or an arbitrary-modification collapse merely to close the probe.

The passing reflection/cancellation prerequisites make a derived admission
route concrete. They do not yet prove that the original inverse belongs to
the Cartesian category. The complete locality theorem, other library
integration, wrapper retirement, public promotion, and final qualification
gates remain required. This is staged authoring evidence, not production
promotion or a consistency certificate.

The core regression and whiskering-equivalence target each pass in about
25 seconds under 240s/2GiB with `o=20`. The represented-cell boundary fails
in about 30 seconds under that same limit, rather than timing out. The
combined inverse/cancellation import uses the previously reviewed
300s/4GiB/o=20 profile; about 15GiB of host memory was available before its
fresh run. Exact outcomes, input hashes and warning comparisons are recorded
in the verification. Subject reduction, serial execution and file/no-swap
limits remain enabled; normal resource defaults remain unchanged.
