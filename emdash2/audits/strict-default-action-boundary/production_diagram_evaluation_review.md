# Varying-shape evaluation: the next profile boundary

Date: 2026-10-16
Status: source/semantic review; replacement interface not yet implemented or qualified
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Inventory: [explicit declaration-level consumers](production_diagram_evaluation_consumers.json)

## Observed failure and valid general operations

The current broader import stops at `diagram_evaluation_func` in
`emdash3_2_diagram_evaluation.lp`. Its old body exchanges the identity of
Functor_cat(I,C), but the migrated `sym_func` requires Cartesian mapping
categories. It must not be repaired by equating Functor_cat and Functor_cart_cat.

Fixed-point evaluation remains valid without that restriction:

```text
D = Functor_cat(I,C)
ev_i : D → C
D₀ : K → D
family_at_i(D₀) = ev_i ∘ D₀ : K → C.
```

The whole family-evaluation functor is postcomposition by ev_i. It retains
arbitrary lax transformations between D₀ and D₁. Use the existing fixed
`fapp0_func` and composition/whiskering owners; unrestricted exchange is not a
prerequisite for these operations.

## The comparison has the opposite direction

For a conventional lax η:F⇒G and u:i→j, the native comparison has direction

```text
G[u] ∘ η[i] ⇒ η[j] ∘ F[u].
```

A default-lax transformation ev_i⇒ev_j on D would demand the reverse direction.
Thus the unrestricted shape-evaluation transformation is oplax relative to
the retained default. Cartesian diagram maps remove that distinction, but
replacing every diagram category by Cart would lose general lax inputs to
fixed evaluation and other valid consumers.

The migration must distinguish the valid general fixed-evaluation operations,
the whole shape operation with its actual opposite transformation profile,
and existing Cartesian/ordinary-category specializations. A changed whole
profile is a mathematical correction; it is not permission to erase η's
noninvertible comparison or to supply its inverse as new caller data.

## Higher duality must be checked, not inferred from the square

The paper's `op` reverses odd dimensions; this branch's `Op_cat` reverses
dimension one only. Ara–Guetta §2, 35–38, distinguishes odd/even anti-monoidal
dualities from total duality and gives the corresponding lax/oplax Hom
comparisons. Replacing those dualities by transpose alone is not justified.
[Primary reference](https://arxiv.org/html/2503.08832v1#S2).

Accordingly, do not promote the tempting expression

```text
T(Functor_cat(T(A),T(B)))
```

to a qualified standard omega-oplax classifier. The existing Homd index uses
exactly a related literal presentation, P(I)=T(Functor_cat(I,T(Cat_cart))),
and its source explicitly disclaims a general equivalence with the usual
omega-category of oplax transformations. Preserve that qualification; this
review neither changes P nor establishes that its recorded native consumers
are invalid.

For the standard profile, write Odd for reversal of dimensions 1,3,5,... and
Even for reversal of dimensions 2,4,6,... .
Assuming the native Functor_cat realizes that conventional omega-lax Hom,
involutivity gives the following candidate native presentation:

```text
Oplax(A,B) ≃ Odd(Functor_cat(Odd(A),Odd(B))).
```

Objects are represented by Odd(F); they are not definitionally ordinary F.
The Hom between encoded F and G is Even applied to
Transf_cat(Odd(A),Odd(B),Odd(G),Odd(F)). Keeping that higher duality is essential.
Existing T/R/O names must not be reinterpreted. Any new odd/even owners need
native category/functor projection and interaction qualification first; use
clear names such as OddDual/EvenDual, not the paper's overloaded `op`.

A candidate whole evaluation then has shape

```text
Ev : I → Oplax(Functor_cat(I,C), C)
Ev[i] represents ev_i.
```

This remains a proposed interface. Qualify its whole mixed Hom action and
actual extracted noninvertible naturality, including the next higher action;
object beta and a declared type do not complete it. A primitive whole owner
with honest structural status and qualified projections is permitted. No
standalone laxity witness, resolution encoding or general tensor-coherence
library is a prerequisite merely to state this interface.

## Consumer migration and scope

The bounded textual inventory finds 123 explicit calls to shape-evaluation
operations in 55 declaration-bearing modules. 115 signatures mention OneCat
or IsNCat; the guard's actual target still requires per-consumer confirmation.
The eight remaining declarations are listed explicitly in the inventory.
This is not a proof of transitive consumer completeness.

OneCat-specialized conversions can use the existing strict-transfor admission
and qualified dual views where their hypotheses apply. Preserve all existing
ordinary-category guards. For general consumers, prefer actual pre/post
whiskering of an already supplied whole transformation over an unnecessary
arrow-family/exchange round trip. Inspect the source before asserting that
this works for any particular constructor.

Keep genuinely general diagram data and retained higher comparisons. In
particular, pointwise zero or identity components do not by themselves make
a general lax transformation strict. Do not silently replace such a map by
a canonical zero map, nor add a blanket OneCat restriction merely to pass.
The primary next slice is fixed evaluation plus a correctly profiled whole
shape interface and its real consumers. This remains foundational work; the
separate nerve/equivalence goal stays paused.
