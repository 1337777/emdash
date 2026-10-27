# Whole terminal-diagram reconstruction

Date: 2026-10-27
Status: qualified non-library degree-zero equivalence; production promotion remains open
Owner: [native implementation outline](../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
Evidence: [exact replay modes and receipts](reverse_verification.json)

## Result and retained maps

For G(A,B)=Functor_oplax_cat(A,B), the previously defined maps

```text
d₀ : G(Terminal,C) → C
e₀ : C → G(Terminal,C)
```

now have both whole inverse paths. The [constructed equivalence](geometric_zero_inverse.lpfragment)
retains e₀ as each selected inverse of d₀. The encoder and decoder bodies are
unchanged. A whole parameter family D:K→G(Terminal,C) is recovered by
(e₀∘d₀)∘D≐D; the proof does not infer whole equality from object components.
This completes the isolated geometric degree-zero inverse obligation. It does
not close positive-dimensional tensor closure, the native walking second
inverse, common-index action, degeneracies or production qualification.

## Derivation

[Terminal-valued functors](terminal_contraction.lpfragment) F,G:A→Terminal
have the actual forward and inverse transformations Terminal_obj because
Hom_(Functor_cat(A,Terminal))(F,G)=Terminal. Unit contractibility proves both
cancellation paths. The existing native `omega_cast_to_object_path` then gives
a path between the whole functor objects. This explicitly uses the kernel's
existing equivalence/object-path interface; it is not a new extensionality
principle or a claim that equivalence and equality coincide without that
interface.

At A=Terminal this yields c≐id, where c=Const_func(Terminal_obj). Applying
ordinary equality congruence to the fixed-precomposition operation gives
precompose(c)≐id on the whole mapping category. This construction passes
before adding any new comparison or duality rule.

The attempted generic identification of precompose(c) with the chosen
constant/evaluation composite fails in the prior source. The added
[structural whole beta](constant_precomposition_beta.lpfragment) is

```text
precompose(Const_(A,B)(b))
  ≐ CartInclude(A,C) ∘ Const_func_func(A,C) ∘ evaluate_b.
```

This is a comparison between existing whole owners, with A, B, C and b
retained. It applies to any constant shape map, not only the terminal
contraction. Its mathematical action sends F to const(F[b]) and a lax
transformation ε to const(ε[b]); normality makes its comparison on every
source arrow an identity because that arrow maps to id_b. The component ε[b]
remains arbitrary. This beta is supplied structural computation, not a theorem
derived from the earlier point projections. It installs no runtime terminal
eta or category identification.

Ordinary terminal mapping eta now follows by composing that beta with the
proved contraction. The paired [Odd/Even constant-functor rules](alternating_constant_beta.lpfragment)
then let the same proof use OddDual(Terminal). Finally, staged OddDual
composition gives e₀∘d₀≐id on G(Terminal,C). No equation
OddDual(Terminal)=Terminal is used. No operational map takes a path or inverse
law as an argument.

## Qualification and limits

The final **78-input** check passes with subject reduction in **110.775s /
618,504 KiB**, at explicit 300s / 2 GiB. It includes the preceding cube maps
and unit/noncollapse scope. New controls recover both chosen inverse maps,
a whole parameter family and the original lax component ε[b]; an unrelated
component and the wrong selected point are rejected. Whole next-Hom and
involution controls exercise both alternating-duality constant rules.

The warning inventory is 2,298 critical-pair reports / 181 replaceable
patterns, versus 2,292 / 181. Ten new reported peaks concern constant
projection, involution and the Cat_cart constant-family erasure; four prior
composition peaks join. The exercised whole-Hom/involution projections pass.
Erased Cat_cart-family runtime normalization remains a promotion review;
the aggregate warning count is not a confluence certificate. Both affected
owner files pass the inferred-slot audit, with the ordinary identity-family
guard explicitly documented.

Replay modes `terminal-contraction`, `constant-precomposition-pending` and
`terminal-inverse` preserve the original proof, failed pre-beta comparison and
final combined scope separately. The extra Unit-contractibility source is
copied from its pinned existing owner, not duplicated as a new foundation.
`--assemble-only` verifies exact source identity without repeating the checker.
Previous replay modes keep their original snapshots.
