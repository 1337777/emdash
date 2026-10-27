# Mixed-diagram reconstruction and the remaining internalization

Date: 2026-10-27
Status: qualified non-library reconstruction for each complete diagram; whole internal exchange inverse remains open
Owner: [native implementation outline](../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
Evidence: [mixed-diagram replay mode](reverse_verification.json)

Write L(A,B)=Functor_cat(A,B), G(A,B)=Functor_oplax_cat(A,B), and use the
already constructed whole maps

```text
M : L(K,G(I,C)) → G(I,L(K,C))
Y : G(I,L(K,C)) → L(K,G(I,C)).
```

The [new proofs](mixed_diagram_roundtrip.lpfragment) establish

```text
Y[M[D]] ≐ D     for every complete D : K → G(I,C),
M[Y[E]] ≐ E     for every encoded E : Obj(G(I,L(K,C))).
```

Each equality concerns a whole K- or I-diagram, retaining its arrow and higher
action. It is stronger than an equality after choosing k and i. It is still
an object-level path in the category of diagrams: these proofs do not yet
assemble the whole equalities Y∘M≐id and M∘Y≐id of the internal mapping
functors. In particular, they are not used as an unrestricted functor
extensionality principle.

The reciprocal object readback follows from the earlier mixed-exchange
readback at the swapped Odd-dual parameters and the existing whole duality /
shape comparison. Both paths then follow by staging the two existing
whole double-exchange laws. There is no new primitive, rewrite, unification
rule or supplied inverse path in this extension. The path arguments occur
only in proof definitions; no operational map gains a proof payload.

The 66-input check passes with subject reduction in **143.274s / 619,500 KiB**
at 300s / 2 GiB. The warning inventory is 2,296 critical-pair reports / 181
replaceable patterns, with no new family or parser issue against the preceding
zero-inverse qualification. Two inherited raw-profile reports are absent
because the smaller scope does not import their consumer. This is not a new
confluence result. `replay_reverse.py --mode mixed-diagram --assemble-only`
verifies the exact package.

The [existing whole-evaluation obligation](exchange_cancellation_review.md)
remains the root internalization boundary. The new result narrows the missing
proof to compatible action as diagrams themselves vary; it does not establish
that this action is wrong or that a mathematical redesign is required.
[Ara–Guetta v1, §21](https://arxiv.org/html/2503.08832v1#S2) gives the corresponding
mixed lax/oplax internal-Hom isomorphism, supporting the semantic target.
The receiver still needs its own whole proof with its actual maps.

The existing right closure provides its two inverse paths at a different
profile. Reusing those paths alone does not prove compatibility of the
constructed mixed evaluator and structural postcomposition owner. No new
mixed inverse is postulated to bridge that gap. Continue that proof while
advancing the independent shape operations required by the same-index nerve.
