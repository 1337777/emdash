/* Proof-time views of native whole-family adjunction mates.
   The comparison helpers preserve the existing runtime owners.
   Congruence is sufficient: corresponding operands and endpoints must
   compare. This does not assert mathematical injectivity of composition.
   Whole formula agreement and reconstruction are derived through the
   original Hom comparison and its same selected inverse. */
require open emdash.emdash3_2_one_cat_adjunction_families;

// Same actual functor and argument; compare only their classifier presentations.
// This is sufficient congruence, not injectivity of functor application.
// lhs-audit: keep 1,2 -- both classifier presentations are explicit subcomparisons.
unif_rule @fapp0 $A $B $F $x ≡ @fapp0 $A0 $B0 $F $x
  ↪ [ $A ≡ $A0; $B ≡ $B0 ];

// Sufficient congruence for the same component observation. Parent
// presentations and the actual transfor must compare; no injectivity is claimed.
// lhs-audit: keep 1,2,5 -- the base, target and evaluation point are shared.
unif_rule @tapp0_fapp0 $A $B $F $G $x $eta
  ≡ @tapp0_fapp0 $A $B $F0 $G0 $x $eta0
  ↪ [ $F ≡ $F0; $G ≡ $G0; $eta ≡ $eta0 ];

// Congruence for a pair of Cat horizontal actions in a whole mate formula.
// Both operand heads are guarded so the generic associativity rule remains
// the owner when either operand is itself a vertical composite.
unif_rule @comp_fapp0 (Functor_cat $B $C) $A $D $E
    (@comp_prod_fapp1_fapp0 Cat_cat $Xg $Yg $Zg $pg $qg $g)
    (@comp_prod_fapp1_fapp0 Cat_cat $Xf $Yf $Zf $pf $qf $f)
  ≡ @comp_fapp0 (Functor_cat $B0 $C0) $A0 $D0 $E0
    (@comp_prod_fapp1_fapp0 Cat_cat $Xg0 $Yg0 $Zg0 $pg0 $qg0 $g0)
    (@comp_prod_fapp1_fapp0 Cat_cat $Xf0 $Yf0 $Zf0 $pf0 $qf0 $f0)
  ↪ [ $B ≡ $B0; $C ≡ $C0; $A ≡ $A0; $D ≡ $D0; $E ≡ $E0;
      (@comp_prod_fapp1_fapp0 Cat_cat $Xg $Yg $Zg $pg $qg $g)
        ≡ (@comp_prod_fapp1_fapp0 Cat_cat $Xg0 $Yg0 $Zg0 $pg0 $qg0 $g0);
      (@comp_prod_fapp1_fapp0 Cat_cat $Xf $Yf $Zf $pf $qf $f)
        ≡ (@comp_prod_fapp1_fapp0 Cat_cat $Xf0 $Yf0 $Zf0 $pf0 $qf0 $f0) ];

// Congruence for the same horizontal action and the same two actual cells.
// Only the endpoint presentations may differ. In particular this does not
// decompose an equality between different whiskering factorizations.
// lhs-audit: keep 1,2,3,4 -- the common category triple and shared cell payloads guard this congruence case.
unif_rule @comp_prod_fapp1_fapp0 Cat_cat $B $C $D $fg $fg'
    (@Struct_sigma _ _ $alpha $beta)
  ≡ @comp_prod_fapp1_fapp0 Cat_cat $B $C $D $hk $hk'
      (@Struct_sigma _ _ $alpha $beta)
  ↪ [ $fg ≡ $hk; $fg' ≡ $hk' ];

/* Inactive broad view: unrestricted horizontal-action
   congruence intercepts reindexing across different factorizations.
   Restore only with guards qualified against both whole adjunction
   observations and arbitrary-parameter diagram reindexing.

// Same Cat horizontal-action shape. Every pair and endpoint is compared.
unif_rule @comp_prod_fapp1_fapp0 Cat_cat $B $C $D $fg $fg' $theta
  ≡ @comp_prod_fapp1_fapp0 Cat_cat $B0 $C0 $D0 $hk $hk' $psi
  ↪ [ $B ≡ $B0; $C ≡ $C0; $D ≡ $D0;
      $fg ≡ $hk; $fg' ≡ $hk'; $theta ≡ $psi ];
*/

// Associativity with represented inner postcomposition. Compare whole
// composites before their potentially different intermediate categories.
unif_rule @comp_fapp0 Cat_cat $B $L $R $G
    (@hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $B $C $L $F $A)
  ≡ @comp_fapp0 Cat_cat $B1 $L1 $R1 $H $X
  ↪ [ $B1 ≡ $B; $R1 ≡ $R;
      (@comp_fapp0 Cat_cat $B $C $R (@comp_fapp0 Cat_cat $C $L $R $G $F) $A)
        ≡ (@comp_fapp0 Cat_cat $B1 $L1 $R1 $H $X) ];

// Companion view: (G∘F)∗X compares with G∘(F∗X), retaining every operand.
unif_rule @hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $B $A $C
    (@comp_fapp0 Cat_cat $A $D $C $G $F) $X
  ≡ @comp_fapp0 Cat_cat $B $D $C $G
    (@hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $B $A $D $F $X)
  ↪ [ tt ≡ tt ];

// The output composite of precomposition and a postcomposition view may
// expose different intermediate categories. Compare their complete composites.
// lhs-audit: keep 1,2,3,4,5,6 -- identity Cat action and complete endpoints are retained.
unif_rule @hom_precomp_along_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat)
    $Z $W $X $h (@comp_fapp0 Cat_cat $X $M $Z $q $p)
  ≡ @hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat)
      $W1 $X1 $Z1 $q1 $h1
  ↪ [ $W1 ≡ $W; $Z1 ≡ $Z;
      (@comp_fapp0 Cat_cat $W $X $Z (@comp_fapp0 Cat_cat $X $M $Z $q $p) $h)
        ≡ (@comp_fapp0 Cat_cat $W1 $X1 $Z1 $q1 $h1) ];

// Companion for represented precomposition of a visible composite.
// This is associativity in Cat, with the identity ambient action. The
// composite argument is a discriminator, mirroring the guarded post-view.
unif_rule @hom_precomp_along_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat)
    $D $A $C (@comp_fapp0 Cat_cat $A $B $C $G $H) $F
  ≡ @comp_fapp0 Cat_cat $A1 $B1 $D1
    (@comp_fapp0 Cat_cat $B2 $C2 $D2 $F1 $G1) $H1
  ↪ [ $A1 ≡ $A; $B1 ≡ $B; $D1 ≡ $D;
      $B2 ≡ $B; $C2 ≡ $C; $D2 ≡ $D;
      $F1 ≡ $F; $G1 ≡ $G; $H1 ≡ $H ];

// Sigma's capped action may project before its represented postcomposition
// view is compared. This exposes the same sigma_map, not a naturality law.
unif_rule @hom_postcomp_fapp0 Cat_cat (@Catd_cat $K) (@Sigma_func $K)
    $W $E $D $FF $G
  ≡ @comp_fapp0 Cat_cat $W1 $X1 $Y1 (@sigma_map_func $K1 $E1 $D1 $FF1) $G1
  ↪ [ $K1 ≡ $K; $E1 ≡ $E; $D1 ≡ $D; $FF1 ≡ $FF; $G1 ≡ $G;
      $W1 ≡ $W; $X1 ≡ (@Sigma_cat $K $E); $Y1 ≡ (@Sigma_cat $K $D) ];

// The corresponding view after totalization of family reindexing. Both
// factors and every endpoint are checked; no composition of FF is expanded.
unif_rule @hom_precomp_along_fapp0 (@Catd_cat $K) Cat_cat
    (@comp_fapp0 Cat_cat _ _ _ (@Sigma_func $A) (@Pullback_catd_func $A $K $F))
    $Z $E $D $FF $G
  ≡ @comp_fapp0 Cat_cat $W1 $X1 $Z1 $G1 (@sigma_map_func $A1 $E1 $D1 $PFF)
  ↪ [ $A1 ≡ $A; $G1 ≡ $G; $Z1 ≡ $Z;
      $E1 ≡ (@Pullback_catd $A $K $E $F); $D1 ≡ (@Pullback_catd $A $K $D $F);
      $W1 ≡ (@Sigma_cat $A (@Pullback_catd $A $K $E $F));
      $X1 ≡ (@Sigma_cat $A (@Pullback_catd $A $K $D $F));
      $PFF ≡ (@fapp1_fapp0 (@Catd_cat $K) (@Catd_cat $A) (@Pullback_catd_func $A $K $F) $E $D $FF) ];

// Proof-time constant precomposition; the source and selected value are retained.
unif_rule @hom_precomp_along_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $C $A _ _
    (@Const_func _ _ $t)
  ≡ @Const_func $A $C $t
  ↪ [ tt ≡ tt ];

// Proof-time constant postcomposition through its represented-action owner.
// Cat/id is the actual represented-action discriminator; retain B, C and t.
unif_rule @hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $B _ $C
    (@Const_func _ _ $t) _
  ≡ @Const_func $B $C $t
  ↪ [ tt ≡ tt ];

// Sufficient congruence for a composite of two whole shape-arrow observations.
// Guard both operands so generic associativity remains the owner of composites.
unif_rule @comp_fapp0 (Functor_cat $B $C) $X $Y $Z
    (@sym_tapp1_fapp0_transf $Bg $Ig $Cg $Dg $ig $jg $ug)
    (@sym_tapp1_fapp0_transf $Bf $If $Cf $Df $if $jf $uf)
  ≡ @comp_fapp0 (Functor_cat $B0 $C0) $X0 $Y0 $Z0
    (@sym_tapp1_fapp0_transf $Bg0 $Ig0 $Cg0 $Dg0 $ig0 $jg0 $ug0)
    (@sym_tapp1_fapp0_transf $Bf0 $If0 $Cf0 $Df0 $if0 $jf0 $uf0)
  ↪ [ $B ≡ $B0; $C ≡ $C0; $X ≡ $X0; $Y ≡ $Y0; $Z ≡ $Z0;
      (@sym_tapp1_fapp0_transf $Bg $Ig $Cg $Dg $ig $jg $ug)
        ≡ (@sym_tapp1_fapp0_transf $Bg0 $Ig0 $Cg0 $Dg0 $ig0 $jg0 $ug0);
      (@sym_tapp1_fapp0_transf $Bf $If $Cf $Df $if $jf $uf)
        ≡ (@sym_tapp1_fapp0_transf $Bf0 $If0 $Cf0 $Df0 $if0 $jf0 $uf0) ];

// Companion associativity view with represented outer postcomposition.
// The actual Q,G,F and every endpoint are the same on both sides.
unif_rule @hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $B $D $C $Q
    (@comp_fapp0 Cat_cat $B $A $D $G $F)
  ≡ @comp_fapp0 Cat_cat $B $A $C (@comp_fapp0 Cat_cat $A $D $C $Q $G) $F
  ↪ [ tt ≡ tt ];

// Compare represented postcomposition of a composite with its associated raw form.
// Guard the composite argument so paired-family reindexing keeps its own views.
// Endpoints and the entire original composite are checked in the residual.
unif_rule @hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat)
    $A $B $C $G (@comp_fapp0 Cat_cat $A $M $B $X $U)
  ≡ @comp_fapp0 Cat_cat $A0 $B0 $C0 $H $Y
  ↪ [ $A ≡ $A0; $C ≡ $C0;
      (@comp_cat_fapp0 $A $B $C $G (@comp_fapp0 Cat_cat $A $M $B $X $U))
        ≡ (@comp_cat_fapp0 $A0 $B0 $C0 $H $Y) ];

// Observation of a whole family mate in the original whiskering formula.
symbol one_cat_adjunction_family_transpose_agrees [B R L : Cat]
  (R1 : τ (IsNCat (cat_succ cat_zero) R))
  (L1 : τ (IsNCat (cat_succ cat_zero) L))
  [F : τ (Functor R L)] [G : τ (Functor L R)]
  (J : τ (@Adjunction R L F G))
  (A : τ (Functor B R)) (D : τ (Functor B L))
  (h : τ (@Transf B L (@comp_cat_fapp0 B R L F A) D))
  : τ (@= (@Transf B R A (@comp_cat_fapp0 B L R G D))
      (@fapp0 (Hom_cat (Functor_cat B L) (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D) (Hom_cat (Functor_cat B R) A
        (@fapp0 _ _ (@comp_cat_cov_func B L R G) D)) (@one_cat_adjunction_family_transpose_func B R L R1 L1 F G J A D)
        h)
      (@comp_fapp0 (Functor_cat B R) A
        (@comp_cat_fapp0 B L R G (@comp_cat_fapp0 B R L F A))
        (@comp_cat_fapp0 B L R G D)
        (@fapp0 _ _ (@comp_cat_cov_fapp1_func B L R G (@comp_cat_fapp0 B R L F A) D) h)
        (@fapp0 _ _ (@comp_cat_con_fapp1_func B R R A (@id_func R) (@comp_cat_fapp0 R L R G F))
          (@unit_adj_transf R L F G J))))
≔ @eq_trans (Obj (Hom_cat (Functor_cat B R) A (@comp_cat_fapp0 B L R G D))) _ _ _
        (@eq_ap (Functor (Hom_cat (Functor_cat B L) (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D) (Hom_cat (Functor_cat B R) A
  (@fapp0 _ _ (@comp_cat_cov_func B L R G) D))) (Obj (Hom_cat (Functor_cat B R) A (@fapp0 _ _ (@comp_cat_cov_func B L R
  G) D)))
    (λ M : τ (Functor (Hom_cat (Functor_cat B L) (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D) (Hom_cat (Functor_cat B
      R) A (@fapp0 _ _ (@comp_cat_cov_func B L R G) D))), @fapp0 (Hom_cat (Functor_cat B L) (@fapp0 _ _
      (@comp_cat_cov_func B R L F) A) D) (Hom_cat (Functor_cat B R) A (@fapp0 _ _ (@comp_cat_cov_func B L R G) D)) M h)
    (@one_cat_adjunction_family_transpose_func B R L R1 L1 F G J A D)
    (@adjunction_transpose_semantic_func (Functor_cat B R) (Functor_cat B L)
      (@comp_cat_cov_func B R L F) (@comp_cat_cov_func B L R G)
      (@one_cat_postcomp_adjunction B R L R1 L1 F G J) A D)
    (@adjunction_transpose_semantic_path (Functor_cat B R) (Functor_cat B L)
      (@comp_cat_cov_func B R L F) (@comp_cat_cov_func B L R G)
      (@one_cat_postcomp_adjunction B R L R1 L1 F G J) A D))
        (@eq_ap (Obj (Hom_cat (Functor_cat B R) A (@comp_cat_fapp0 B R R (@comp_cat_fapp0 R L R G F) A))) (Obj (Hom_cat (Functor_cat B R) A (@comp_cat_fapp0 B L R G D))) (λ v : τ (Obj (Hom_cat (Functor_cat B R) A (@comp_cat_fapp0 B R R (@comp_cat_fapp0 R L R G F) A))), @comp_fapp0 (Functor_cat B R) A (@comp_cat_fapp0 B R R (@comp_cat_fapp0 R L R G F) A) (@comp_cat_fapp0 B L R G D) (@fapp0 _ _ (@comp_cat_cov_fapp1_func B L R G (@comp_cat_fapp0 B R L F A) D) h) v) _ _
          (@eq_sym _ _ _ (@hom_precomp_along_fapp1_comp_prod_path Cat_cat Cat_cat (@id_func Cat_cat) R B R A (@id_func R) (@comp_cat_fapp0 R L R G F) (@unit_adj_transf R L F G J))));

// Observation of a whole family mate in the original whiskering formula.
symbol one_cat_adjunction_family_untranspose_agrees [B R L : Cat]
  (R1 : τ (IsNCat (cat_succ cat_zero) R))
  (L1 : τ (IsNCat (cat_succ cat_zero) L))
  [F : τ (Functor R L)] [G : τ (Functor L R)]
  (J : τ (@Adjunction R L F G))
  (A : τ (Functor B R)) (D : τ (Functor B L))
  (h : τ (@Transf B R A (@comp_cat_fapp0 B L R G D)))
  : τ (@= (@Transf B L (@comp_cat_fapp0 B R L F A) D)
      (@fapp0 (Hom_cat (Functor_cat B R) A (@fapp0 _ _ (@comp_cat_cov_func B L R G) D)) (Hom_cat (Functor_cat B L)
        (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D) (@one_cat_adjunction_family_untranspose_func B R L R1 L1 F G J A
        D) h)
      (@comp_fapp0 (Functor_cat B L) (@comp_cat_fapp0 B R L F A)
        (@comp_cat_fapp0 B R L F (@comp_cat_fapp0 B L R G D)) D
        (@fapp0 _ _ (@comp_cat_con_fapp1_func B L L D (@comp_cat_fapp0 L R L F G) (@id_func L))
          (@counit_adj_transf R L F G J))
        (@fapp0 _ _ (@comp_cat_cov_fapp1_func B R L F A (@comp_cat_fapp0 B L R G D)) h)))
≔ @eq_trans (Obj (Hom_cat (Functor_cat B L) (@comp_cat_fapp0 B R L F A) D)) _ _ _
        (@eq_ap (Functor (Hom_cat (Functor_cat B R) A (@fapp0 _ _ (@comp_cat_cov_func B L R G) D)) (Hom_cat (Functor_cat B L)
  (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D)) (Obj (Hom_cat (Functor_cat B L) (@fapp0 _ _ (@comp_cat_cov_func B R L
  F) A) D))
    (λ M : τ (Functor (Hom_cat (Functor_cat B R) A (@fapp0 _ _ (@comp_cat_cov_func B L R G) D)) (Hom_cat (Functor_cat B
      L) (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D)), @fapp0 (Hom_cat (Functor_cat B R) A (@fapp0 _ _
      (@comp_cat_cov_func B L R G) D)) (Hom_cat (Functor_cat B L) (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D) M h)
    (@one_cat_adjunction_family_untranspose_func B R L R1 L1 F G J A D)
    (@adjunction_untranspose_semantic_func (Functor_cat B R) (Functor_cat B L)
      (@comp_cat_cov_func B R L F) (@comp_cat_cov_func B L R G)
      (@one_cat_postcomp_adjunction B R L R1 L1 F G J) A D)
    (@adjunction_untranspose_semantic_path (Functor_cat B R) (Functor_cat B L)
      (@comp_cat_cov_func B R L F) (@comp_cat_cov_func B L R G)
      (@one_cat_postcomp_adjunction B R L R1 L1 F G J) A D))
        (@eq_ap (Obj (Hom_cat (Functor_cat B L) (@comp_cat_fapp0 B L L (@comp_cat_fapp0 L R L F G) D) D)) (Obj (Hom_cat (Functor_cat B L) (@comp_cat_fapp0 B R L F A) D)) (λ v : τ (Obj (Hom_cat (Functor_cat B L) (@comp_cat_fapp0 B L L (@comp_cat_fapp0 L R L F G) D) D)), @comp_fapp0 (Functor_cat B L) (@comp_cat_fapp0 B R L F A) (@comp_cat_fapp0 B L L (@comp_cat_fapp0 L R L F G) D) D v (@fapp0 _ _ (@comp_cat_cov_fapp1_func B R L F A (@comp_cat_fapp0 B L R G D)) h)) _ _
          (@eq_sym _ _ _ (@hom_precomp_along_fapp1_comp_prod_path Cat_cat Cat_cat (@id_func Cat_cat) L B L D (@comp_cat_fapp0 L R L F G) (@id_func L) (@counit_adj_transf R L F G J))));

// Whole reconstruction for the raw formula, derived through the same inverse.
symbol one_cat_adjunction_family_transpose_reconstruction [B R L : Cat]
  (R1 : τ (IsNCat (cat_succ cat_zero) R))
  (L1 : τ (IsNCat (cat_succ cat_zero) L))
  [F : τ (Functor R L)] [G : τ (Functor L R)]
  (J : τ (@Adjunction R L F G))
  (A : τ (Functor B R)) (D : τ (Functor B L))
  (h : τ (@Transf B L (@comp_cat_fapp0 B R L F A) D))
  : τ (@= (@Transf B L (@comp_cat_fapp0 B R L F A) D) (@fapp0 (Hom_cat (Functor_cat B R) A (@fapp0 _ _
    (@comp_cat_cov_func B L R G) D)) (Hom_cat (Functor_cat B L) (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D)
    (@one_cat_adjunction_family_untranspose_func B R L R1 L1 F G J A D) (@comp_fapp0 (Functor_cat B R) A
        (@comp_cat_fapp0 B L R G (@comp_cat_fapp0 B R L F A))
        (@comp_cat_fapp0 B L R G D)
        (@fapp0 _ _ (@comp_cat_cov_fapp1_func B L R G (@comp_cat_fapp0 B R L F A) D) h)
        (@fapp0 _ _ (@comp_cat_con_fapp1_func B R R A (@id_func R) (@comp_cat_fapp0 R L R G F))
          (@unit_adj_transf R L F G J)))) h)
≔ @eq_sym (Obj (Hom_cat (Functor_cat B L) (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D)) h (@fapp0 (Hom_cat
  (Functor_cat B R) A (@fapp0 _ _ (@comp_cat_cov_func B L R G) D)) (Hom_cat (Functor_cat B L) (@fapp0 _ _
  (@comp_cat_cov_func B R L F) A) D) (@one_cat_adjunction_family_untranspose_func B R L R1 L1 F G J A D) (@comp_fapp0
  (Functor_cat B R) A
        (@comp_cat_fapp0 B L R G (@comp_cat_fapp0 B R L F A))
        (@comp_cat_fapp0 B L R G D)
        (@fapp0 _ _ (@comp_cat_cov_fapp1_func B L R G (@comp_cat_fapp0 B R L F A) D) h)
        (@fapp0 _ _ (@comp_cat_con_fapp1_func B R R A (@id_func R) (@comp_cat_fapp0 R L R G F))
          (@unit_adj_transf R L F G J))))
    (@eq_ap (Obj (Hom_cat (Functor_cat B R) A (@fapp0 _ _ (@comp_cat_cov_func B L R G) D))) (Obj (Hom_cat (Functor_cat B
      L) (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D))
      (λ k : τ (Obj (Hom_cat (Functor_cat B R) A (@fapp0 _ _ (@comp_cat_cov_func B L R G) D))), @fapp0 (Hom_cat
        (Functor_cat B R) A (@fapp0 _ _ (@comp_cat_cov_func B L R G) D)) (Hom_cat (Functor_cat B L) (@fapp0 _ _
        (@comp_cat_cov_func B R L F) A) D) (@one_cat_adjunction_family_untranspose_func B R L R1 L1 F G J A D) k)
      (@fapp0 (Hom_cat (Functor_cat B L) (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D) (Hom_cat (Functor_cat B R) A
        (@fapp0 _ _ (@comp_cat_cov_func B L R G) D)) (@one_cat_adjunction_family_transpose_func B R L R1 L1 F G J A D)
        h) (@comp_fapp0 (Functor_cat B R) A
        (@comp_cat_fapp0 B L R G (@comp_cat_fapp0 B R L F A))
        (@comp_cat_fapp0 B L R G D)
        (@fapp0 _ _ (@comp_cat_cov_fapp1_func B L R G (@comp_cat_fapp0 B R L F A) D) h)
        (@fapp0 _ _ (@comp_cat_con_fapp1_func B R R A (@id_func R) (@comp_cat_fapp0 R L R G F))
          (@unit_adj_transf R L F G J)))
      (@one_cat_adjunction_family_transpose_agrees B R L R1 L1 F G J A D h));

// Whole reconstruction for the raw formula, derived through the same inverse.
symbol one_cat_adjunction_family_untranspose_reconstruction [B R L : Cat]
  (R1 : τ (IsNCat (cat_succ cat_zero) R))
  (L1 : τ (IsNCat (cat_succ cat_zero) L))
  [F : τ (Functor R L)] [G : τ (Functor L R)]
  (J : τ (@Adjunction R L F G))
  (A : τ (Functor B R)) (D : τ (Functor B L))
  (h : τ (@Transf B R A (@comp_cat_fapp0 B L R G D)))
  : τ (@= (@Transf B R A (@comp_cat_fapp0 B L R G D)) (@fapp0 (Hom_cat (Functor_cat B L) (@fapp0 _ _ (@comp_cat_cov_func
    B R L F) A) D) (Hom_cat (Functor_cat B R) A (@fapp0 _ _ (@comp_cat_cov_func B L R G) D))
    (@one_cat_adjunction_family_transpose_func B R L R1 L1 F G J A D) (@comp_fapp0 (Functor_cat B L) (@comp_cat_fapp0 B
    R L F A)
        (@comp_cat_fapp0 B R L F (@comp_cat_fapp0 B L R G D)) D
        (@fapp0 _ _ (@comp_cat_con_fapp1_func B L L D (@comp_cat_fapp0 L R L F G) (@id_func L))
          (@counit_adj_transf R L F G J))
        (@fapp0 _ _ (@comp_cat_cov_fapp1_func B R L F A (@comp_cat_fapp0 B L R G D)) h))) h)
≔ @eq_sym (Obj (Hom_cat (Functor_cat B R) A (@fapp0 _ _ (@comp_cat_cov_func B L R G) D))) h (@fapp0 (Hom_cat
  (Functor_cat B L) (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D) (Hom_cat (Functor_cat B R) A (@fapp0 _ _
  (@comp_cat_cov_func B L R G) D)) (@one_cat_adjunction_family_transpose_func B R L R1 L1 F G J A D) (@comp_fapp0
  (Functor_cat B L) (@comp_cat_fapp0 B R L F A)
        (@comp_cat_fapp0 B R L F (@comp_cat_fapp0 B L R G D)) D
        (@fapp0 _ _ (@comp_cat_con_fapp1_func B L L D (@comp_cat_fapp0 L R L F G) (@id_func L))
          (@counit_adj_transf R L F G J))
        (@fapp0 _ _ (@comp_cat_cov_fapp1_func B R L F A (@comp_cat_fapp0 B L R G D)) h)))
    (@eq_ap (Obj (Hom_cat (Functor_cat B L) (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D)) (Obj (Hom_cat (Functor_cat B
      R) A (@fapp0 _ _ (@comp_cat_cov_func B L R G) D)))
      (λ k : τ (Obj (Hom_cat (Functor_cat B L) (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D)), @fapp0 (Hom_cat
        (Functor_cat B L) (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D) (Hom_cat (Functor_cat B R) A (@fapp0 _ _
        (@comp_cat_cov_func B L R G) D)) (@one_cat_adjunction_family_transpose_func B R L R1 L1 F G J A D) k)
      (@fapp0 (Hom_cat (Functor_cat B R) A (@fapp0 _ _ (@comp_cat_cov_func B L R G) D)) (Hom_cat (Functor_cat B L)
        (@fapp0 _ _ (@comp_cat_cov_func B R L F) A) D) (@one_cat_adjunction_family_untranspose_func B R L R1 L1 F G J A
        D) h) (@comp_fapp0 (Functor_cat B L) (@comp_cat_fapp0 B R L F A)
        (@comp_cat_fapp0 B R L F (@comp_cat_fapp0 B L R G D)) D
        (@fapp0 _ _ (@comp_cat_con_fapp1_func B L L D (@comp_cat_fapp0 L R L F G) (@id_func L))
          (@counit_adj_transf R L F G J))
        (@fapp0 _ _ (@comp_cat_cov_fapp1_func B R L F A (@comp_cat_fapp0 B L R G D)) h))
      (@one_cat_adjunction_family_untranspose_agrees B R L R1 L1 F G J A D h));
