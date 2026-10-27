# Intrinsic unit normality

Date: 2026-10-27
Status: qualified non-library unit computation; production and broader identity-overlap review remain open
Owner: [native implementation outline](../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
Evidence: [unit replay modes](reverse_verification.json)

## Meaning and historical boundary

A normal lax functor preserves identities strictly while its composition
comparison can remain nonidentity. The pre-migration baseline `f8af1fca`
already contains F[idₓ]↝id_F[x] and ε[idₓ]↝εₓ. This observation does not
certify every old extracted unit law. Current public functors are strict,
so their composition law is strict too.

For a transformation ε:F⇒G, distinguish:

```text
off-diagonal action:       ε[idₓ] ↝ εₓ
naturality comparison:     λ_ε(idₓ) ↝ id_εₓ.
```

The component εₓ need not be identity. A comparison along a nonidentity arrow
need not be identity or invertible. Direction, coherent units and strict
naturality are different conditions. The standard transformation definition
includes an identity-cell axiom; its lax version is obtained by duality.
See [Ara–Maltsiniotis, §§1.9 and 1.12](https://webusers.imj-prg.fr/~georges.maltsiniotis/ps/joint.pdf#page=24).
No additional default `NormalTransfor` classifier is introduced. This repair
implements the selected conventional profile's unit computation; it does not
derive the entire coherence theory from the choice of one strict leg.

## Implemented computation

Existing intrinsic displayed-action owners now compute at identity bases:

```text
fdapp1_int_hom_func(FF,idₓ,u,v) ↝ (FF[x])₁(u,v)
fdapp1_int_hom_fapp0(FF,idₓ,a) ↝ FF[x][a]
fdapp1_int_cell(FF,idₓ,u) ↝ id_FF[x](u)
functord_laxity_transf(FF,idₓ) ↝ id_FF[x].
```

These are rules on the original extraction ladder, not separately supplied
unit cells. Whole extraction matches the actual `fdapp1_int_transfd(FF)`.
The identity displayed-map join recognizes the actual identity modification
of `homd_id_int` in its Functord category. An arbitrary supplied modification
is not erased.

Terminal-source joins handle `id_Terminal(x)↝Terminal_obj` while retaining x
and equal endpoints; they use no Unit-object eta. The represented
postcomposition and tapp1 owners need the same erased-identity cases. The
named private postcomposition cell has its corresponding unit projection,
with the measured identity-carrier guard required for subject reduction.

## Qualification

The final 73-input check passes with subject reduction in **158.920s /
621,372 KiB**, at explicit 300s / 2 GiB. It covers whole/capped agreement,
next-Hom fibre action, canonical and neutral terminal points, identity-map
and postcomposition projection orders, and the prior nonidentity interchanger.
It rejects collapse of an independently supplied modification. An ordinary
functor interpreted between constant families still returns its actual base
arrow, including a general loop; it is not confused with an identity displayed
map. The earlier all-degree cube-map consumers remain included.

Warnings are 2,292 critical-pair reports and 181 replaceable patterns, versus
2,230/181 before this extension, with no parser issues. Added families concern
identity projections and intrinsic unit-rung overlaps. The selected generic,
terminal and constructor joins are checked. Erased identities of other
dual/product presentations retain their promotion-review obligation; a generic
typed unit theorem is not global runtime confluence. The inferred-slot audit
has no unreviewed compound slots; owner-specific guards were reviewed too.

`replay_reverse.py --mode unit-normality --assemble-only` reconstructs the
exact package. `unit-owners` selects the smaller ordinary unit consumer.
Previous modes keep their original snapshots. No production source, frontend
profile or manuscript artifact is promoted here.

## Remaining reconstruction

Unit normality alone does not prove terminal-diagram eta, mixed-exchange
cancellation or the native walking inverse. The subsequent
[terminal reconstruction](terminal_inverse_review.md) now derives the zero
inverse using actual omega-equivalence data, the existing object-path view,
and a generic whole constant-precomposition beta. Mixed-exchange cancellation
and native walking reconstruction remain open.
