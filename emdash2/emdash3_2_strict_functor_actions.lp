/*
  Emdash v3.2: default functor action on equality-valued equivalences.

  Ordinary strict Functor inputs preserve the actual chosen inverse maps and
  their cancellation laws through native action. The mapped DefIso and Prof
  comparison owners are shared directly; no strict-object wrapper, separate
  admission certificate or detached composition law is consumed.
*/

require open emdash.emdash3_2_gray_profiles;

symbol functor_composition_path
  [A B : Cat]
  (S : τ (@Functor A B))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (@=
      (Hom B
        (@fapp0 A B (S) X)
        (@fapp0 A B (S) Z))
      (@fapp1_fapp0 A B (S) X Z
        (@comp_fapp0 A X Y Z g f))
      (@comp_fapp0
        B
        (@fapp0 A B (S) X)
        (@fapp0 A B (S) Y)
        (@fapp0 A B (S) Z)
        (@fapp1_fapp0 A B (S) Y Z g)
        (@fapp1_fapp0 A B (S) X Y f)))
≔ @eq_refl
    (Hom B
      (@fapp0 A B (S) X)
      (@fapp0 A B (S) Z))
    (@fapp1_fapp0 A B (S) X Z
      (@comp_fapp0 A X Y Z g f));

symbol omega_equiv_along_fmap_left_law
  [A B : Cat]
  (S : τ (@Functor A B))
  [x y : τ (Obj A)]
  [f : τ (Hom A x y)]
  (u : τ (@OmegaEquivAlong A x y f))
  : τ (@=
      (Hom B
        (@fapp0 A B (S) x)
        (@fapp0 A B (S) x))
      (@comp_fapp0
        B
        (@fapp0 A B (S) x)
        (@fapp0 A B (S) y)
        (@fapp0 A B (S) x)
        (@fapp1_fapp0 A B (S) y x
          (@omega_equiv_along_left_inv A x y f u))
        (@fapp1_fapp0 A B (S) x y f))
      (@id B (@fapp0 A B (S) x)))
≔ @eq_trans
    (Hom B
      (@fapp0 A B (S) x)
      (@fapp0 A B (S) x))
    (@comp_fapp0
      B
      (@fapp0 A B (S) x)
      (@fapp0 A B (S) y)
      (@fapp0 A B (S) x)
      (@fapp1_fapp0 A B (S) y x
        (@omega_equiv_along_left_inv A x y f u))
      (@fapp1_fapp0 A B (S) x y f))
    (@fapp1_fapp0 A B (S) x x
      (@comp_fapp0 A x y x
        (@omega_equiv_along_left_inv A x y f u)
        f))
    (@id B (@fapp0 A B (S) x))
    (@eq_sym
      (Hom B
        (@fapp0 A B (S) x)
        (@fapp0 A B (S) x))
      (@fapp1_fapp0 A B (S) x x
        (@comp_fapp0 A x y x
          (@omega_equiv_along_left_inv A x y f u)
          f))
      (@comp_fapp0
        B
        (@fapp0 A B (S) x)
        (@fapp0 A B (S) y)
        (@fapp0 A B (S) x)
        (@fapp1_fapp0 A B (S) y x
          (@omega_equiv_along_left_inv A x y f u))
        (@fapp1_fapp0 A B (S) x y f))
      (@functor_composition_path
        A B S x y x
        (@omega_equiv_along_left_inv A x y f u)
        f))
    (@eq_ap
      (Hom A x x)
      (Hom B
        (@fapp0 A B (S) x)
        (@fapp0 A B (S) x))
      (λ h : τ (Hom A x x),
        @fapp1_fapp0 A B (S) x x h)
      (@comp_fapp0 A x y x
        (@omega_equiv_along_left_inv A x y f u)
        f)
      (@id A x)
      (@omega_equiv_along_left_law A x y f u));

symbol omega_equiv_along_fmap_right_law
  [A B : Cat]
  (S : τ (@Functor A B))
  [x y : τ (Obj A)]
  [f : τ (Hom A x y)]
  (u : τ (@OmegaEquivAlong A x y f))
  : τ (@=
      (Hom B
        (@fapp0 A B (S) y)
        (@fapp0 A B (S) y))
      (@comp_fapp0
        B
        (@fapp0 A B (S) y)
        (@fapp0 A B (S) x)
        (@fapp0 A B (S) y)
        (@fapp1_fapp0 A B (S) x y f)
        (@fapp1_fapp0 A B (S) y x
          (@omega_equiv_along_right_inv A x y f u)))
      (@id B (@fapp0 A B (S) y)))
≔ @eq_trans
    (Hom B
      (@fapp0 A B (S) y)
      (@fapp0 A B (S) y))
    (@comp_fapp0
      B
      (@fapp0 A B (S) y)
      (@fapp0 A B (S) x)
      (@fapp0 A B (S) y)
      (@fapp1_fapp0 A B (S) x y f)
      (@fapp1_fapp0 A B (S) y x
        (@omega_equiv_along_right_inv A x y f u)))
    (@fapp1_fapp0 A B (S) y y
      (@comp_fapp0 A y x y
        f
        (@omega_equiv_along_right_inv A x y f u)))
    (@id B (@fapp0 A B (S) y))
    (@eq_sym
      (Hom B
        (@fapp0 A B (S) y)
        (@fapp0 A B (S) y))
      (@fapp1_fapp0 A B (S) y y
        (@comp_fapp0 A y x y
          f
          (@omega_equiv_along_right_inv A x y f u)))
      (@comp_fapp0
        B
        (@fapp0 A B (S) y)
        (@fapp0 A B (S) x)
        (@fapp0 A B (S) y)
        (@fapp1_fapp0 A B (S) x y f)
        (@fapp1_fapp0 A B (S) y x
          (@omega_equiv_along_right_inv A x y f u)))
      (@functor_composition_path
        A B S y x y f
        (@omega_equiv_along_right_inv A x y f u)))
    (@eq_ap
      (Hom A y y)
      (Hom B
        (@fapp0 A B (S) y)
        (@fapp0 A B (S) y))
      (λ h : τ (Hom A y y),
        @fapp1_fapp0 A B (S) y y h)
      (@comp_fapp0 A y x y
        f
        (@omega_equiv_along_right_inv A x y f u))
      (@id A y)
      (@omega_equiv_along_right_law A x y f u));

symbol omega_equiv_along_fmap
  [A B : Cat]
  (S : τ (@Functor A B))
  [x y : τ (Obj A)]
  [f : τ (Hom A x y)]
  (u : τ (@OmegaEquivAlong A x y f))
  : τ (@OmegaEquivAlong
      B
      (@fapp0 A B (S) x)
      (@fapp0 A B (S) y)
      (@fapp1_fapp0 A B (S) x y f))
≔ @omega_equiv_along_intro
    B
    (@fapp0 A B (S) x)
    (@fapp0 A B (S) y)
    (@fapp1_fapp0 A B (S) x y f)
    (@fapp1_fapp0 A B (S) y x
      (@omega_equiv_along_left_inv A x y f u))
    (@fapp1_fapp0 A B (S) y x
      (@omega_equiv_along_right_inv A x y f u))
    (@omega_equiv_along_fmap_left_law A B S x y f u)
    (@omega_equiv_along_fmap_right_law A B S x y f u);

symbol omega_equiv_fmap_left_projection
  [A B : Cat]
  (S : τ (@Functor A B))
  [x y : τ (Obj A)]
  [f : τ (Hom A x y)]
  (u : τ (@OmegaEquivAlong A x y f))
  : τ (@=
      (Hom B
        (@fapp0 A B (S) y)
        (@fapp0 A B (S) x))
      (@omega_equiv_along_left_inv
        B
        (@fapp0 A B (S) x)
        (@fapp0 A B (S) y)
        (@fapp1_fapp0 A B (S) x y f)
        (@omega_equiv_along_fmap A B S x y f u))
      (@fapp1_fapp0 A B (S) y x
        (@omega_equiv_along_left_inv A x y f u)))
≔ @eq_refl
    (Hom B
      (@fapp0 A B (S) y)
      (@fapp0 A B (S) x))
    (@fapp1_fapp0 A B (S) y x
      (@omega_equiv_along_left_inv A x y f u));

symbol omega_equiv_fmap_right_projection
  [A B : Cat]
  (S : τ (@Functor A B))
  [x y : τ (Obj A)]
  [f : τ (Hom A x y)]
  (u : τ (@OmegaEquivAlong A x y f))
  : τ (@=
      (Hom B
        (@fapp0 A B (S) y)
        (@fapp0 A B (S) x))
      (@omega_equiv_along_right_inv
        B
        (@fapp0 A B (S) x)
        (@fapp0 A B (S) y)
        (@fapp1_fapp0 A B (S) x y f)
        (@omega_equiv_along_fmap A B S x y f u))
      (@fapp1_fapp0 A B (S) y x
        (@omega_equiv_along_right_inv A x y f u)))
≔ @eq_refl
    (Hom B
      (@fapp0 A B (S) y)
      (@fapp0 A B (S) x))
    (@fapp1_fapp0 A B (S) y x
      (@omega_equiv_along_right_inv A x y f u));

// Ordinary evidence follows the default strict functor's existing action.
symbol iso_evidence_fmap [C D : Cat] (F : τ (Functor C D))
  [x y : τ (Obj C)] (i : τ (@IsoEvidence C x y))
  : τ (@IsoEvidence D (@fapp0 C D F x) (@fapp0 C D F y))
≔ Struct_sigma
    (@fapp1_fapp0 C D F x y (@iso_evidence_to C x y i))
    (Struct_sigma
      (@fapp1_fapp0 C D F y x (@iso_evidence_from C x y i))
      (Struct_sigma
        (@eq_ap (Hom C x x) (Hom D (@fapp0 C D F x) (@fapp0 C D F x))
          (λ h : τ (Hom C x x), @fapp1_fapp0 C D F x x h)
          (@comp_fapp0 C x y x (@iso_evidence_from C x y i) (@iso_evidence_to C x y i))
          (@id C x) (@iso_evidence_left C x y i))
        (@eq_ap (Hom C y y) (Hom D (@fapp0 C D F y) (@fapp0 C D F y))
          (λ h : τ (Hom C y y), @fapp1_fapp0 C D F y y h)
          (@comp_fapp0 C y x y (@iso_evidence_to C x y i) (@iso_evidence_from C x y i))
          (@id C y) (@iso_evidence_right C x y i))));

/* Mapped computational inverse owners for default strict functors. */

injective symbol defiso_fmap_to
  [C D : Cat]
  (F : τ (Functor C D))
  [x y : τ (Obj C)]
  (i : τ (@DefIso C x y))
  : τ (Hom D
      (@fapp0 C D F x)
      (@fapp0 C D F y));

injective symbol defiso_fmap_from
  [C D : Cat]
  (F : τ (Functor C D))
  [x y : τ (Obj C)]
  (i : τ (@DefIso C x y))
  : τ (Hom D
      (@fapp0 C D F y)
      (@fapp0 C D F x));

unif_rule
  @defiso_fmap_to $C $D $F $x $y $i
  ≡ @fapp1_fapp0 $C $D $F
      $x $y (@defiso_to $C $x $y $i)
  ↪ [ tt ≡ tt ];

unif_rule
  @defiso_fmap_from $C $D $F $x $y $i
  ≡ @fapp1_fapp0 $C $D $F
      $y $x (@defiso_from $C $x $y $i)
  ↪ [ tt ≡ tt ];

// The coefficient inclusion is identity on the actual functor objects.
// Read both retained mapped inverse heads after that first action has
// normalized, without erasing their computational cancellation owners.
unif_rule @defiso_fmap_to Cat_cart Cat_cat Cat_cart_include $A $B $i
  ≡ $F
  ↪ [ $F ≡ @defiso_to Cat_cart $A $B $i ];
unif_rule @defiso_fmap_from Cat_cart Cat_cat Cat_cart_include $A $B $i
  ≡ $F
  ↪ [ $F ≡ @defiso_from Cat_cart $A $B $i ];

symbol defiso_fmap_to_path
  [C D : Cat]
  (F : τ (Functor C D))
  [x y : τ (Obj C)]
  (i : τ (@DefIso C x y))
  : τ (@=
      (Hom D
        (@fapp0 C D F x)
        (@fapp0 C D F y))
      (@defiso_fmap_to C D F x y i)
      (@fapp1_fapp0 C D F
        x y (@defiso_to C x y i)))
≔ @eq_refl
    (Hom D
      (@fapp0 C D F x)
      (@fapp0 C D F y))
    (@defiso_fmap_to C D F x y i);

symbol defiso_fmap_from_path
  [C D : Cat]
  (F : τ (Functor C D))
  [x y : τ (Obj C)]
  (i : τ (@DefIso C x y))
  : τ (@=
      (Hom D
        (@fapp0 C D F y)
        (@fapp0 C D F x))
      (@defiso_fmap_from C D F x y i)
      (@fapp1_fapp0 C D F
        y x (@defiso_from C x y i)))
≔ @eq_refl
    (Hom D
      (@fapp0 C D F y)
      (@fapp0 C D F x))
    (@defiso_fmap_from C D F x y i);

injective symbol defiso_fmap
  [C D : Cat]
  (F : τ (Functor C D))
  [x y : τ (Obj C)]
  (i : τ (@DefIso C x y))
  : τ (@DefIso
      D
      (@fapp0 C D F x)
      (@fapp0 C D F y));

rule @defiso_to
      $D _ _
      (@defiso_fmap $C $D $F $x $y $i)
  ↪ @defiso_fmap_to $C $D $F $x $y $i
with @defiso_from
      $D _ _
      (@defiso_fmap $C $D $F $x $y $i)
  ↪ @defiso_fmap_from $C $D $F $x $y $i;

rule @comp_fapp0
      _ _ _ _
      (@defiso_fmap_from $C $D $F $x $y $i)
      (@defiso_fmap_to $C $D $F $x $y $i)
  ↪ @id $D (@fapp0 $C $D $F $x)
with @comp_fapp0
      _ _ _ _
      (@defiso_fmap_to $C $D $F $x $y $i)
      (@defiso_fmap_from $C $D $F $x $y $i)
  ↪ @id $D (@fapp0 $C $D $F $y);

rule @hom_postcomp_fapp0
      $D $D (@id Cat_cat $D)
      _ _ _
      (@defiso_fmap_from $C $D $F $x $y $i)
      (@defiso_fmap_to $C $D $F $x $y $i)
  ↪ @id $D (@fapp0 $C $D $F $x)
with @hom_postcomp_fapp0
      $D $D (@id Cat_cat $D)
      _ _ _
      (@defiso_fmap_to $C $D $F $x $y $i)
      (@defiso_fmap_from $C $D $F $x $y $i)
  ↪ @id $D (@fapp0 $C $D $F $y);

rule @hom_postcomp_fapp0
      $D $D (@id Cat_cat $D)
      $W _ _
      (@defiso_fmap_from $C $D $F $x $y $i)
      (@hom_postcomp_fapp0
        $D $D (@id Cat_cat $D)
        $W _ _
        (@defiso_fmap_to $C $D $F $x $y $i)
        $f)
  ↪ $f
with @hom_postcomp_fapp0
      $D $D (@id Cat_cat $D)
      $W _ _
      (@defiso_fmap_to $C $D $F $x $y $i)
      (@hom_postcomp_fapp0
        $D $D (@id Cat_cat $D)
        $W _ _
        (@defiso_fmap_from $C $D $F $x $y $i)
        $g)
  ↪ $g;

// Functor-valued mapped inverses retain their whole owner through point
// cancellation, just as evaluated inverses do. Cat_cat is the actual target
// classifier here; the source coefficient and its inverse data remain intact.
rule @fapp0 _ _ (@defiso_fmap_from $C Cat_cat $F $x $y $I)
      (@fapp0 _ _ (@defiso_fmap_to $C Cat_cat $F $x $y $I) $a)
  ↪ $a
with @fapp0 _ _ (@defiso_fmap_to $C Cat_cat $F $x $y $I)
      (@fapp0 _ _ (@defiso_fmap_from $C Cat_cat $F $x $y $I) $a)
  ↪ $a;

rule @defiso_iso_evidence
      $D _ _
      (@defiso_fmap $C $D $F $x $y $i)
  ↪ @iso_evidence_fmap
      $C $D $F $x $y
      (@defiso_iso_evidence $C $x $y $i);

symbol defiso_fmap_to_beta
  [C D : Cat]
  (F : τ (Functor C D))
  [x y : τ (Obj C)]
  (i : τ (@DefIso C x y))
  : τ (@=
      (Hom D
        (@fapp0 C D F x)
        (@fapp0 C D F y))
      (@defiso_to
        D
        (@fapp0 C D F x)
        (@fapp0 C D F y)
        (@defiso_fmap C D F x y i))
      (@defiso_fmap_to C D F x y i))
≔ @eq_refl
    (Hom D
      (@fapp0 C D F x)
      (@fapp0 C D F y))
    (@defiso_fmap_to C D F x y i);

symbol defiso_fmap_cancel
  [C D : Cat]
  (F : τ (Functor C D))
  [x y : τ (Obj C)]
  (i : τ (@DefIso C x y))
  : τ (@=
      (Hom D
        (@fapp0 C D F x)
        (@fapp0 C D F x))
      (@comp_fapp0
        D
        (@fapp0 C D F x)
        (@fapp0 C D F y)
        (@fapp0 C D F x)
        (@defiso_fmap_from C D F x y i)
        (@defiso_fmap_to C D F x y i))
      (@id D (@fapp0 C D F x)))
≔ @eq_refl
    (Hom D
      (@fapp0 C D F x)
      (@fapp0 C D F x))
    (@id D (@fapp0 C D F x));

// Default functorial action on the existing whole comparison package.
symbol prof_comparison_fmap [A B A' B' : Cat]
  (F : τ (Functor (Prof_cat A B) (Prof_cat A' B')))
  [P Q : τ (Prof A B)] (i : τ (ProfComparison P Q))
  : τ (ProfComparison (@fapp0 _ _ F P) (@fapp0 _ _ F Q))
≔ @defiso_fmap (Prof_cat A B) (Prof_cat A' B') F P Q i;

// Proof-time join when strict functoriality folds F[q] o F[p] before the
// represented action sees the composite. Both operations have stable runtime
// owners; compare all actual data rather than ask unification to invent the
// intermediate general-F postcomposition presentation.
unif_rule @hom_postcomp_fapp0 $B $B (@id Cat_cat $B) $w _ _
      (@fapp1_fapp0 $A $B $F $x $z (@comp_fapp0 $A $x $y $z $q $p)) $r
  ≡ @hom_postcomp_fapp0 $B0 $B0 (@id Cat_cat $B0) $w0 _ _
      (@fapp1_fapp0 $A0 $B0 $F0 $y0 $z0 $q0)
      (@hom_postcomp_fapp0 $B0 $B0 (@id Cat_cat $B0) $w0 _ _
        (@fapp1_fapp0 $A0 $B0 $F0 $x0 $y0 $p0) $r0)
  ↪ [ $A ≡ $A0; $B ≡ $B0; $F ≡ $F0; $w ≡ $w0;
      $x ≡ $x0; $y ≡ $y0; $z ≡ $z0;
      $p ≡ $p0; $q ≡ $q0; $r ≡ $r0 ];
// Weighted-limit and adjunction actions use the same default owners.

// Forward universal operation after reindexing the limit comparison along M.
symbol weighted_limit_cov_push
  [B J J' : Cat]
  [F : τ (Functor J B)]
  [W : τ (Prof J' J)]
  [L : τ (Functor J' B)]
  (isl : τ (@IsWeightedLimit_cov_comp B J J' F W L))
  [I : Cat]
  (M : τ (Functor I B))
  [R : τ (Prof I J')]
  (r : τ (ProfMap
      R
      (@Prof_imply_cov
        I J' J
        (@Hom_prof_along I J B M F)
        W)))
  : τ (ProfMap R (@Hom_prof_along I J' B M L))
≔ @prof_comparison_push
    I J'
    _
    _
    (@prof_comparison_fmap
      B J' I J'
      (@Prof_reindex_func B I J' J' M (@id_func J'))
      _
      _
      isl)
    R
    r;

// Inverse universal operation after reindexing the limit comparison along M.
symbol weighted_limit_cov_pull
  [B J J' : Cat]
  [F : τ (Functor J B)]
  [W : τ (Prof J' J)]
  [L : τ (Functor J' B)]
  (isl : τ (@IsWeightedLimit_cov_comp B J J' F W L))
  [I : Cat]
  (M : τ (Functor I B))
  [R : τ (Prof I J')]
  (s : τ (ProfMap R (@Hom_prof_along I J' B M L)))
  : τ (ProfMap
      R
      (@Prof_imply_cov
        I J' J
        (@Hom_prof_along I J B M F)
        W))
≔ @prof_comparison_pull
    I J'
    _
    _
    (@prof_comparison_fmap
      B J' I J'
      (@Prof_reindex_func B I J' J' M (@id_func J'))
      _
      _
      isl)
    R
    s;

// Reindexed adjunction mate: Hom_B(LM,F) ≃ Hom_A(M,RF).
symbol Adjunction_hom_prof_comparison_along
  [A B : Cat]
  [Ladj : τ (Functor A B)]
  [Radj : τ (Functor B A)]
  (adj : τ (@Adjunction A B Ladj Radj))
  [I K : Cat]
  (M : τ (Functor I A))
  (F : τ (Functor K B))
  : τ (ProfComparison
      (@Hom_prof_along
        I K B
        (@comp_cat_fapp0
          I A B
          Ladj
          M)
        F)
      (@Hom_prof_along
        I K A
        M
        (@comp_cat_fapp0
          K B A
          Radj
          F)))
≔ @prof_comparison_fmap
    A B I K
    (@Prof_reindex_func A I B K M F)
    _
    _
    (@Adjunction_hom_prof_comparison A B Ladj Radj adj);

/*
  Computational right-adjoint preservation.

  This parallel API composes three certified comparisons:

    1. the inverse adjunction mate through fixed-weight implication;
    2. the given weighted-limit comparison reindexed along the left adjoint;
    3. the adjunction mate at the candidate limit.

  Its beta/eta laws are inherited from `prof_comparison_push/pull`; no
  theorem-specific fold or cancellation rule is added to ordinary equipment
  composition.
*/
symbol right_adjoint_weighted_limit_comp_step1
  [B J J' A : Cat]
  [Ladj : τ (Functor A B)]
  [Radj : τ (Functor B A)]
  [W : τ (Prof J' J)]
  [F : τ (Functor J B)]
  (adj : τ (@Adjunction A B Ladj Radj))
  : τ (ProfComparison
      (@Prof_imply_cov
        A J' J
        (@Hom_prof
          J A
          (@comp_cat_fapp0
            J B A
            Radj
            F))
        W)
      (@Prof_imply_cov
        A J' J
        (@Hom_prof_along
          A J B
          Ladj
          F)
        W))
≔ @prof_comparison_fmap
    A J A J'
    (@Prof_imply_cov_func A J' J W)
    _
    _
    (@prof_comparison_sym
      A J
      _
      _
      (@Adjunction_hom_prof_comparison_along
        A B Ladj Radj adj
        A J
        (@id_func A)
        F));

// Preservation step 2: reindex the supplied weighted-limit comparison along L.
symbol right_adjoint_weighted_limit_comp_step2
  [B J J' A : Cat]
  [Ladj : τ (Functor A B)]
  [Radj : τ (Functor B A)]
  [W : τ (Prof J' J)]
  [F : τ (Functor J B)]
  [L : τ (Functor J' B)]
  (isl : τ (@IsWeightedLimit_cov_comp B J J' F W L))
  (adj : τ (@Adjunction A B Ladj Radj))
  : τ (ProfComparison
      (@Prof_imply_cov
        A J' J
        (@Hom_prof_along
          A J B
          Ladj
          F)
        W)
      (@Hom_prof_along
        A J' B
        Ladj
        L))
≔ @prof_comparison_fmap
    B J' A J'
    (@Prof_reindex_func
      B A J' J'
      Ladj
      (@id_func J'))
    _
    _
    isl;

// Preservation step 3: apply the adjunction mate to the candidate limit L.
symbol right_adjoint_weighted_limit_comp_step3
  [B J J' A : Cat]
  [Ladj : τ (Functor A B)]
  [Radj : τ (Functor B A)]
  [L : τ (Functor J' B)]
  (adj : τ (@Adjunction A B Ladj Radj))
  : τ (ProfComparison
      (@Hom_prof_along
        A J' B
        Ladj
        L)
      (@Hom_prof
        J' A
        (@comp_cat_fapp0
          J' B A
          Radj
          L)))
≔ @Adjunction_hom_prof_comparison_along
    A B Ladj Radj adj
    A J'
    (@id_func A)
    L;

// Composite certificate that a right adjoint preserves the weighted limit.
symbol right_adjoint_preserves_weighted_limit_cov_comp
  [B J J' A : Cat]
  [Ladj : τ (Functor A B)]
  [Radj : τ (Functor B A)]
  [W : τ (Prof J' J)]
  [F : τ (Functor J B)]
  [L : τ (Functor J' B)]
  (isl : τ (@IsWeightedLimit_cov_comp B J J' F W L))
  (adj : τ (@Adjunction A B Ladj Radj))
  : τ (@IsWeightedLimit_cov_comp
      A J J'
      (@comp_cat_fapp0
        J B A
        Radj
        F)
      W
      (@comp_cat_fapp0
        J' B A
        Radj
        L))
≔ @prof_comparison_comp
    A J'
    _ _ _
    (@right_adjoint_weighted_limit_comp_step3
      B J J' A Ladj Radj L adj)
    (@prof_comparison_comp
      A J'
      _ _ _
      (@right_adjoint_weighted_limit_comp_step2
        B J J' A Ladj Radj W F L isl adj)
      (@right_adjoint_weighted_limit_comp_step1
        B J J' A Ladj Radj W F adj));

// Preserve the original T-weighted colimit interface using its whole Hom
// comparison. Product-swap profunctor duality needs no total-opposite
// adjunction and introduces no new unit/counit transformation profile.
// The three preservation steps remain implication, reindexing, and mate.

// Product-swap duality maps the actual comparison with the default action.
protected symbol prof_comparison_op
  [A B : Cat] [P Q : τ (Prof A B)]
  (i : τ (@ProfComparison A B P Q))
  : τ (@ProfComparison (Op_cat B) (Op_cat A)
      (@Op_prof A B P) (@Op_prof A B Q))
≔ @prof_comparison_fmap A B (Op_cat B) (Op_cat A)
    (@Op_prof_func A B) P Q i;

// Whole represented-Hom transpose: the product endpoints swap; the Hom
// fibre is unchanged because Op_cat reverses dimension one only.
unif_rule @Op_prof $A $B
    (@Prof_reindex $X $A $X $B (@Unit_prof $X) $F $G)
  ≡ @Prof_reindex $X0 $B0 $X1 $A0 (@Unit_prof $X2) $G0 $F0
  ↪ [ $X0 ≡ Op_cat $X; $X1 ≡ Op_cat $X; $X2 ≡ Op_cat $X;
      $B0 ≡ Op_cat $B; $A0 ≡ Op_cat $A;
      $G0 ≡ @Op_func $B $X $G; $F0 ≡ @Op_func $A $X $F ];
unif_rule @Op_prof $X $X (@Unit_prof $X) ≡ @Unit_prof $Y
  ↪ [ $Y ≡ Op_cat $X ];

// Only the whole Hom comparison is transposed here. This is not an
// opposite adjunction package with new unit/counit transformation profiles.
protected symbol adjunction_transpose_hom_comparison
  [A B : Cat] [L : τ (Functor A B)] [R : τ (Functor B A)]
  (adj : τ (@Adjunction A B L R))
  : τ (@ProfComparison (Op_cat B) (Op_cat A)
      (@Hom_prof_along (Op_cat B) (Op_cat A) (Op_cat A)
        (@Op_func B A R) (@id_func (Op_cat A)))
      (@Hom_prof_along (Op_cat B) (Op_cat A) (Op_cat B)
        (@id_func (Op_cat B)) (@Op_func A B L)))
≔ @prof_comparison_op A B _ _
    (@prof_comparison_sym A B _ _
      (@Adjunction_hom_prof_comparison A B L R adj));

protected symbol adjunction_transpose_hom_comparison_along
  [A B : Cat] [L : τ (Functor A B)] [R : τ (Functor B A)]
  (adj : τ (@Adjunction A B L R))
  [I K : Cat] (M : τ (Functor I (Op_cat B)))
  (F : τ (Functor K (Op_cat A)))
  : τ (@ProfComparison I K
      (@Hom_prof_along I K (Op_cat A)
        (@comp_cat_fapp0 I (Op_cat B) (Op_cat A) (@Op_func B A R) M) F)
      (@Hom_prof_along I K (Op_cat B) M
        (@comp_cat_fapp0 K (Op_cat A) (Op_cat B) (@Op_func A B L) F)))
≔ @prof_comparison_fmap (Op_cat B) (Op_cat A) I K
    (@Prof_reindex_func (Op_cat B) I (Op_cat A) K M F)
    _ _ (@adjunction_transpose_hom_comparison A B L R adj);

symbol left_adjoint_preserves_weighted_colimit_con
  [A J J' B : Cat]
  [Ladj : τ (Functor A B)]
  [Radj : τ (Functor B A)]
  [F : τ (Functor J A)]
  [W : τ (Prof J J')]
  [L : τ (Functor J' A)]
  (isc : τ (@WeightedColimit_con A J J' F W L))
  (adj : τ (@Adjunction A B Ladj Radj))
  : τ (@WeightedColimit_con
      B J J'
      (@comp_cat_fapp0 J A B Ladj F)
      W
      (@comp_cat_fapp0 J' A B Ladj L))
≔ @prof_comparison_comp (Op_cat B) (Op_cat J') _ _ _
    (@adjunction_transpose_hom_comparison_along A B Ladj Radj adj
      (Op_cat B) (Op_cat J') (@id_func (Op_cat B)) (@Op_func J' A L))
    (@prof_comparison_comp (Op_cat B) (Op_cat J') _ _ _
      (@prof_comparison_fmap (Op_cat A) (Op_cat J') (Op_cat B) (Op_cat J')
        (@Prof_reindex_func (Op_cat A) (Op_cat B) (Op_cat J') (Op_cat J')
          (@Op_func B A Radj) (@id_func (Op_cat J')))
        _ _ isc)
      (@prof_comparison_fmap (Op_cat B) (Op_cat J) (Op_cat B) (Op_cat J')
        (@Prof_imply_cov_func (Op_cat B) (Op_cat J') (Op_cat J)
          (@Op_prof J J' W))
        _ _
        (@prof_comparison_sym (Op_cat B) (Op_cat J) _ _
          (@adjunction_transpose_hom_comparison_along A B Ladj Radj adj
            (Op_cat B) (Op_cat J) (@id_func (Op_cat B)) (@Op_func J A F)))));
