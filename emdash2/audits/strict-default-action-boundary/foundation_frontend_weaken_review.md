# Weakening and reindexing frontend migration

Date: 2026-10-25. Focused/native qualification complete; higher frontend migration remains.

Family fibres and components now use the native `Cat_cart` coefficient.
Reindexing retains the existing `Pullback_catd_func` and section-pullback
projection ladder, including lax displayed maps over the fixed base.

The old frontend runtime-folded generic pullback along `Sigma_proj1_func`
into `Sigma_proj1_pullback_catd`. Native migration deliberately retired that
fold: the whole families compare at proof time and retain separate runtime
heads. Merely changing the coefficient made local TypeScript tests pass, but
would have preserved an unauthorized runtime equation. That candidate was
not retained.

Weakening now follows the production native owner `section_weaken_funcd`:

```text
section_weaken_funcd(R,E,s) : Functord(R,E)
section_weaken_funcd(R,E,s)[k] → Const_func(R[k],E[k],s[k])
section_weaken_funcd(R,E,s)[k][r] → s[k].
```

The existing native constant-functor carrier and object projection are
transferred at this first concrete consumer. The new slice has six native
declarations and seven native runtime clauses; it adds no mathematical
owner, native rule, equality payload or checker branch. The frontend lowering
is smaller and no longer needs the generic pullback-to-stable-family runtime
fold. The separate general Sigma/Pi proof comparison remains available.

Nine focused consumer/demo cases,21 metadata/transfer cases, typecheck and
changed-file lint pass.
The native test checks actual emitted weakening, its point value, reindexing
and its fibre component. A negative conversion check preserves the retired
fold boundary. It passes with subject reduction and warnings under60s/2GiB.
[Verification](foundation_frontend_weaken_verification.json) records source
hashes and the51.143s native receipt.

Next migrate varying-base Pi with its actual Cartesian diagram source and
inclusion into the fixed-base lax diagram category. The later displayed-chain
profile currently redeclares `Const_func`; it must reuse this earlier owner
when that profile is reached, just as the dependent-target layer must reuse
the earlier `fapp0_func`. Neither duplicate is silently requalified here.
