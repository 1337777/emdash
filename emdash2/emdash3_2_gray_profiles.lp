/*
  Emdash v3.2: native compositor properties and transformation profiles.

  Public Functor is the strict map carrier. IsStrictFunctor and its evidence
  projections describe the existing extracted compositor; functor_is_strict
  supplies its canonical proof for default maps. They are property/evidence
  interfaces, not an additional map grammar or operational admission.

  GrayHom_lax uses ordinary functor objects and retains its LaxTransfor Homs.
  StrictTransfor and StrictFunctord remain genuine refinements of the default
  conventional-lax transformations and displayed maps.
*/

require open emdash.emdash3_2;

// Whole post/left source of the intrinsic functor compositor.
symbol strict_functor_compositor_lhs_func
  [A B : Cat]
  (F : τ (Functor A B))
  (X : τ (Obj A))
  [Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  : τ (Functor
      (Hom_cat A X Y)
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
≔ @functord_transport_lhs_func
    A
    (@hom_ A A (@id_func A) X)
    (@hom_ B A F (@fapp0 A B F X))
    (@fapp1_at_transf A B F X)
    Y Z g;

// Whole post/left target of the intrinsic functor compositor.
symbol strict_functor_compositor_rhs_func
  [A B : Cat]
  (F : τ (Functor A B))
  (X : τ (Obj A))
  [Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  : τ (Functor
      (Hom_cat A X Y)
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
≔ @functord_transport_rhs_func
    A
    (@hom_ A A (@id_func A) X)
    (@hom_ B A F (@fapp0 A B F X))
    (@fapp1_at_transf A B F X)
    Y Z g;

// Formal post/left endpoint of the extracted ordinary compositor.
symbol strict_functor_compositor_lhs
  [A B : Cat]
  (F : τ (Functor A B))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (Hom B (fapp0 F X) (fapp0 F Z))
≔ @fapp0
    (Hom_cat A X Y)
    (Hom_cat B (fapp0 F X) (fapp0 F Z))
    (@strict_functor_compositor_lhs_func A B F X Y Z g)
    f;

// Formal pre/right endpoint of the extracted ordinary compositor.
symbol strict_functor_compositor_rhs
  [A B : Cat]
  (F : τ (Functor A B))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (Hom B (fapp0 F X) (fapp0 F Z))
≔ @fapp0
    (Hom_cat A X Y)
    (Hom_cat B (fapp0 F X) (fapp0 F Z))
    (@strict_functor_compositor_rhs_func A B F X Y Z g)
    f;

/*
  Semantic strictness of one existing cell. The endpoint path is explicit, so
  the property remains meaningful after the global strict endpoint cuts are
  migrated. The second field constrains the existing cell; it does not supply
  another compositor.
*/
symbol IsStrictCell
  [C : Cat]
  [x y : τ (Obj C)]
  (cell : τ (Hom C x y))
  : Grpd
≔ `Σ_ p : τ (@= (Obj C) x y),
    @= (Hom C x y) cell (@path_to_hom C x y p);

symbol strict_cell_path
  [C : Cat]
  [x y : τ (Obj C)]
  [cell : τ (Hom C x y)]
  (e : τ (@IsStrictCell C x y cell))
  : τ (@= (Obj C) x y)
≔ sigma_Fst e;

symbol strict_cell_agreement
  [C : Cat]
  [x y : τ (Obj C)]
  [cell : τ (Hom C x y)]
  (e : τ (@IsStrictCell C x y cell))
  : τ (@= (Hom C x y)
      cell
      (@path_to_hom C x y (@strict_cell_path C x y cell e)))
≔ sigma_Snd e;

// Whole intrinsic compositor transformation before capping at f:X->Y.
symbol strict_functor_compositor_transf
  [A B : Cat]
  (F : τ (Functor A B))
  (X : τ (Obj A))
  [Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  : τ (Transf
      (@strict_functor_compositor_lhs_func A B F X Y Z g)
      (@strict_functor_compositor_rhs_func A B F X Y Z g))
≔ @tapp1_post_laxity_transf
    A B F F (@id (Functor_cat A B) F) X Y Z g;

// Normal strict-functor property over the whole intrinsic compositor. Capped
// evidence is derived below by component evaluation.
symbol IsStrictFunctor
  [A B : Cat]
  (F : τ (Functor A B))
  : Grpd
≔ @Pi_grpd
    (Obj A)
    (λ X : τ (Obj A),
      @Pi_grpd
        (Obj A)
        (λ Y : τ (Obj A),
          @Pi_grpd
            (Obj A)
            (λ Z : τ (Obj A),
              @Pi_grpd
                (Hom A Y Z)
                (λ g : τ (Hom A Y Z),
                  @IsStrictCell
                    (@Functor_cat
                      (Hom_cat A X Y)
                      (Hom_cat B
                        (@fapp0 A B F X)
                        (@fapp0 A B F Z)))
                    (@strict_functor_compositor_lhs_func
                      A B F X Y Z g)
                    (@strict_functor_compositor_rhs_func
                      A B F X Y Z g)
                    (@strict_functor_compositor_transf
                      A B F X Y Z g)))));

// Evaluating an equality-induced whole transformation agrees with the
// equality-induced arrow of the evaluated endpoint path.
symbol tapp0_path_to_hom
  [K D : Cat]
  [F G : τ (Functor K D)]
  (p : τ (@= (Functor K D) F G))
  (x : τ (Obj K))
  : τ (@=
      (Hom D (@fapp0 K D F x) (@fapp0 K D G x))
      (@tapp0_fapp0
        K D F G x
        (@path_to_hom (Functor_cat K D) F G p))
      (@path_to_hom
        D
        (@fapp0 K D F x)
        (@fapp0 K D G x)
        (@eq_ap
          (Functor K D)
          (Obj D)
          (λ H : τ (Functor K D), @fapp0 K D H x)
          F G p)))
≔ @ind_eqr
    (Functor K D)
    G
    (λ H : τ (Functor K D),
      λ q : τ (@= (Functor K D) H G),
        @=
          (Hom D (@fapp0 K D H x) (@fapp0 K D G x))
          (@tapp0_fapp0
            K D H G x
            (@path_to_hom (Functor_cat K D) H G q))
          (@path_to_hom
            D
            (@fapp0 K D H x)
            (@fapp0 K D G x)
            (@eq_ap
              (Functor K D)
              (Obj D)
              (λ J : τ (Functor K D), @fapp0 K D J x)
              H G q)))
    (@eq_refl
      (Hom D (@fapp0 K D G x) (@fapp0 K D G x))
      (@id D (@fapp0 K D G x)))
    F p;

// Endpoint path of the capped compositor, obtained by evaluating the whole
// strictness endpoint path at f.
symbol strict_functor_compositor_component_path
  [A B : Cat]
  [F : τ (Functor A B)]
  (strict : τ (@IsStrictFunctor A B F))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (@=
      (Hom B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@strict_functor_compositor_lhs A B F X Y Z g f)
      (@strict_functor_compositor_rhs A B F X Y Z g f))
≔ @eq_ap
    (Functor
      (Hom_cat A X Y)
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
    (Obj (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
    (λ H : τ (Functor
        (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))),
      @fapp0
        (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
        H f)
    (@strict_functor_compositor_lhs_func A B F X Y Z g)
    (@strict_functor_compositor_rhs_func A B F X Y Z g)
    (@strict_cell_path
      (@Functor_cat
        (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
      (@strict_functor_compositor_lhs_func A B F X Y Z g)
      (@strict_functor_compositor_rhs_func A B F X Y Z g)
      (@strict_functor_compositor_transf A B F X Y Z g)
      (strict X Y Z g));

// Capped compositor agreement, derived by evaluating the whole cell equality
// and then using tapp0_path_to_hom for its equality-induced target.
symbol strict_functor_compositor_component_agreement
  [A B : Cat]
  [F : τ (Functor A B)]
  (strict : τ (@IsStrictFunctor A B F))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (@=
      (Hom
        (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
        (@strict_functor_compositor_lhs A B F X Y Z g f)
        (@strict_functor_compositor_rhs A B F X Y Z g f))
      (@fapp1_compositor A B F X Y Z g f)
      (@path_to_hom
        (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
        (@strict_functor_compositor_lhs A B F X Y Z g f)
        (@strict_functor_compositor_rhs A B F X Y Z g f)
        (@strict_functor_compositor_component_path
          A B F strict X Y Z g f)))
≔ @eq_trans
    (Hom
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@strict_functor_compositor_lhs A B F X Y Z g f)
      (@strict_functor_compositor_rhs A B F X Y Z g f))
    (@fapp1_compositor A B F X Y Z g f)
    (@tapp0_fapp0
      (Hom_cat A X Y)
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@strict_functor_compositor_lhs_func A B F X Y Z g)
      (@strict_functor_compositor_rhs_func A B F X Y Z g)
      f
      (@path_to_hom
        (@Functor_cat
          (Hom_cat A X Y)
          (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
        (@strict_functor_compositor_lhs_func A B F X Y Z g)
        (@strict_functor_compositor_rhs_func A B F X Y Z g)
        (@strict_cell_path
          (@Functor_cat
            (Hom_cat A X Y)
            (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
          (@strict_functor_compositor_lhs_func A B F X Y Z g)
          (@strict_functor_compositor_rhs_func A B F X Y Z g)
          (@strict_functor_compositor_transf A B F X Y Z g)
          (strict X Y Z g))))
    (@path_to_hom
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@strict_functor_compositor_lhs A B F X Y Z g f)
      (@strict_functor_compositor_rhs A B F X Y Z g f)
      (@strict_functor_compositor_component_path
        A B F strict X Y Z g f))
    (@eq_ap
      (Hom
        (@Functor_cat
          (Hom_cat A X Y)
          (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
        (@strict_functor_compositor_lhs_func A B F X Y Z g)
        (@strict_functor_compositor_rhs_func A B F X Y Z g))
      (Hom
        (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
        (@strict_functor_compositor_lhs A B F X Y Z g f)
        (@strict_functor_compositor_rhs A B F X Y Z g f))
      (λ theta : τ (Hom
          (@Functor_cat
            (Hom_cat A X Y)
            (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
          (@strict_functor_compositor_lhs_func A B F X Y Z g)
          (@strict_functor_compositor_rhs_func A B F X Y Z g)),
        @tapp0_fapp0
          (Hom_cat A X Y)
          (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
          (@strict_functor_compositor_lhs_func A B F X Y Z g)
          (@strict_functor_compositor_rhs_func A B F X Y Z g)
          f theta)
      (@strict_functor_compositor_transf A B F X Y Z g)
      (@path_to_hom
        (@Functor_cat
          (Hom_cat A X Y)
          (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
        (@strict_functor_compositor_lhs_func A B F X Y Z g)
        (@strict_functor_compositor_rhs_func A B F X Y Z g)
        (@strict_cell_path
          (@Functor_cat
            (Hom_cat A X Y)
            (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
          (@strict_functor_compositor_lhs_func A B F X Y Z g)
          (@strict_functor_compositor_rhs_func A B F X Y Z g)
          (@strict_functor_compositor_transf A B F X Y Z g)
          (strict X Y Z g)))
      (@strict_cell_agreement
        (@Functor_cat
          (Hom_cat A X Y)
          (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
        (@strict_functor_compositor_lhs_func A B F X Y Z g)
        (@strict_functor_compositor_rhs_func A B F X Y Z g)
        (@strict_functor_compositor_transf A B F X Y Z g)
        (strict X Y Z g)))
    (@tapp0_path_to_hom
      (Hom_cat A X Y)
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@strict_functor_compositor_lhs_func A B F X Y Z g)
      (@strict_functor_compositor_rhs_func A B F X Y Z g)
      (@strict_cell_path
        (@Functor_cat
          (Hom_cat A X Y)
          (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
        (@strict_functor_compositor_lhs_func A B F X Y Z g)
        (@strict_functor_compositor_rhs_func A B F X Y Z g)
        (@strict_functor_compositor_transf A B F X Y Z g)
        (strict X Y Z g))
      f);

// Public capped strictness evidence projected from the whole property.
symbol strict_functor_compositor_evidence
  [A B : Cat]
  [F : τ (Functor A B)]
  (strict : τ (@IsStrictFunctor A B F))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (@IsStrictCell
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@strict_functor_compositor_lhs A B F X Y Z g f)
      (@strict_functor_compositor_rhs A B F X Y Z g f)
      (@fapp1_compositor A B F X Y Z g f))
≔ Struct_sigma
    (@strict_functor_compositor_component_path
      A B F strict X Y Z g f)
    (@strict_functor_compositor_component_agreement
      A B F strict X Y Z g f);

// Derived from the existing extracted compositor and strict default action.
symbol functor_is_strict
  [A B : Cat]
  (S : τ (@Functor A B))
  : τ (@IsStrictFunctor A B (S))
≔ λ X : τ (Obj A),
  λ Y : τ (Obj A),
  λ Z : τ (Obj A),
  λ g : τ (Hom A Y Z),
    Struct_sigma
      (@eq_refl
        (Functor
          (Hom_cat A X Y)
          (Hom_cat B
            (@fapp0 A B (S) X)
            (@fapp0 A B (S) Z)))
        (@strict_functor_compositor_lhs_func
          A B (S) X Y Z g))
      (@eq_refl
        (Hom
          (@Functor_cat
            (Hom_cat A X Y)
            (Hom_cat B
              (@fapp0 A B (S) X)
              (@fapp0 A B (S) Z)))
          (@strict_functor_compositor_lhs_func
            A B (S) X Y Z g)
          (@strict_functor_compositor_rhs_func
            A B (S) X Y Z g))
        (@strict_functor_compositor_transf
          A B (S) X Y Z g));

// -----------------------------------------------------------------------------------------------
// Whole strict-transfor property and stable ambient view
// -----------------------------------------------------------------------------------------------

// Whole post/left source of an ordinary transformation's intrinsic naturality
// cell. This is a readable alias of the existing displayed internal action.
symbol strict_transfor_naturality_lhs_func
  [A B : Cat]
  [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  (X : τ (Obj A))
  [Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  : τ (Functor
      (Hom_cat A X Y)
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B G Z)))
≔ @functord_transport_lhs_func
    A
    (@hom_ A A (@id_func A) X)
    (@hom_ B A G (@fapp0 A B F X))
    (@tapp1_at_transf A B F G X epsilon)
    Y Z g;

// Whole post/left target of the same intrinsic naturality cell.
symbol strict_transfor_naturality_rhs_func
  [A B : Cat]
  [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  (X : τ (Obj A))
  [Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  : τ (Functor
      (Hom_cat A X Y)
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B G Z)))
≔ @functord_transport_rhs_func
    A
    (@hom_ A A (@id_func A) X)
    (@hom_ B A G (@fapp0 A B F X))
    (@tapp1_at_transf A B F G X epsilon)
    Y Z g;

// Existing whole post/left cell under its strict-profile reading.
symbol strict_transfor_naturality_transf
  [A B : Cat]
  [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  (X : τ (Obj A))
  [Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  : τ (Transf
      (@strict_transfor_naturality_lhs_func
        A B F G epsilon X Y Z g)
      (@strict_transfor_naturality_rhs_func
        A B F G epsilon X Y Z g))
≔ @tapp1_post_laxity_transf
    A B F G epsilon X Y Z g;

// Post/left strictness is whole in the retained source arrow. The property
// constrains the existing cell and supplies no parallel naturality square.
symbol IsPostStrictTransfor
  [A B : Cat]
  [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  : Grpd
≔ @Pi_grpd
    (Obj A)
    (λ X : τ (Obj A),
      @Pi_grpd
        (Obj A)
        (λ Y : τ (Obj A),
          @Pi_grpd
            (Obj A)
            (λ Z : τ (Obj A),
              @Pi_grpd
                (Hom A Y Z)
                (λ g : τ (Hom A Y Z),
                  @IsStrictCell
                    (@Functor_cat
                      (Hom_cat A X Y)
                      (Hom_cat B
                        (@fapp0 A B F X)
                        (@fapp0 A B G Z)))
                    (@strict_transfor_naturality_lhs_func
                      A B F G epsilon X Y Z g)
                    (@strict_transfor_naturality_rhs_func
                      A B F G epsilon X Y Z g)
                    (@strict_transfor_naturality_transf
                      A B F G epsilon X Y Z g)))));

// Whole pre/right source, retaining q:X->Y while h:W->X is selected.
symbol strict_transfor_pre_naturality_lhs_func
  [A B : Cat]
  [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  (Y : τ (Obj A))
  [W X : τ (Obj A)]
  (h : τ (Hom A W X))
  : τ (Functor
      (Hom_cat A X Y)
      (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y)))
≔ @functord_transport_lhs_func
    (Op_cat A)
    (@hom_con A Y A (@id_func A))
    (@hom_con B (@fapp0 A B G Y) A F)
    (@tapp1_con_at_transf A B F G epsilon Y)
    X W h;

// Whole pre/right target of the same intrinsic cell.
symbol strict_transfor_pre_naturality_rhs_func
  [A B : Cat]
  [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  (Y : τ (Obj A))
  [W X : τ (Obj A)]
  (h : τ (Hom A W X))
  : τ (Functor
      (Hom_cat A X Y)
      (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y)))
≔ @functord_transport_rhs_func
    (Op_cat A)
    (@hom_con A Y A (@id_func A))
    (@hom_con B (@fapp0 A B G Y) A F)
    (@tapp1_con_at_transf A B F G epsilon Y)
    X W h;

// Existing whole pre/right cell under its strict-profile reading.
symbol strict_transfor_pre_naturality_transf
  [A B : Cat]
  [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  (Y : τ (Obj A))
  [W X : τ (Obj A)]
  (h : τ (Hom A W X))
  : τ (Transf
      (@strict_transfor_pre_naturality_lhs_func
        A B F G epsilon Y W X h)
      (@strict_transfor_pre_naturality_rhs_func
        A B F G epsilon Y W X h))
≔ @tapp1_pre_laxity_transf
    A B F G epsilon Y W X h;

// Pre/right strictness is a second skew evidence family over the existing
// pre/right cell. It does not postulate a new cell.
symbol IsPreStrictTransfor
  [A B : Cat]
  [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  : Grpd
≔ @Pi_grpd
    (Obj A)
    (λ Y : τ (Obj A),
      @Pi_grpd
        (Obj A)
        (λ W : τ (Obj A),
          @Pi_grpd
            (Obj A)
            (λ X : τ (Obj A),
              @Pi_grpd
                (Hom A W X)
                (λ h : τ (Hom A W X),
                  @IsStrictCell
                    (@Functor_cat
                      (Hom_cat A X Y)
                      (Hom_cat B
                        (@fapp0 A B F W)
                        (@fapp0 A B G Y)))
                    (@strict_transfor_pre_naturality_lhs_func
                      A B F G epsilon Y W X h)
                    (@strict_transfor_pre_naturality_rhs_func
                      A B F G epsilon Y W X h)
                    (@strict_transfor_pre_naturality_transf
                      A B F G epsilon Y W X h)))));

// Full strictness carries evidence for both existing skew whole cells.
symbol IsStrictTransfor
  [A B : Cat]
  [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  : Grpd
≔ @Product_grpd
    (@IsPostStrictTransfor A B F G epsilon)
    (@IsPreStrictTransfor A B F G epsilon);

// Conventional orientation names: a lax square retains the post/left cell
// and makes the pre/right leg strict; oplax reverses that choice.
symbol IsLaxTransfor
  [A B : Cat]
  [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  : Grpd
≔ @IsPreStrictTransfor A B F G epsilon;

symbol IsOplaxTransfor
  [A B : Cat]
  [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  : Grpd
≔ @IsPostStrictTransfor A B F G epsilon;

/*
  Only the oplax property is active. An exact `OplaxTransfor` Sigma package,
  stable `oplax_transfor` ambient view, higher subcategory, and mirror Gray
  hom are deferred until a concrete consumer requires post/left computation
  while retaining the pre/right cell. Raw ambient transfors do not acquire
  that computation implicitly.
*/

// Opaque full-image classifier for conventional lax transfors. Admission
// evidence constrains the existing pre/right cell and is not projected.
injective symbol LaxTransfor
  [A B : Cat]
  (F G : τ (Functor A B))
  : Grpd;

// Admission constructor; deliberately non-injective so certificate choice is
// unobservable while the ambient carrier remains a unification obligation.
symbol make_lax_transfor
  [A B : Cat]
  [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  (lax : τ (@IsLaxTransfor A B F G epsilon))
  : τ (@LaxTransfor A B F G);

// Stable conventional-lax ambient view. The profile head retains pre/right
// computation while leaving the post/left cell directed and observable.
injective symbol lax_transfor
  [A B : Cat]
  [F G : τ (Functor A B)]
  (L : τ (@LaxTransfor A B F G))
  : τ (Transf F G);

// Explicit raw observation for consumers intentionally leaving the profile.
injective symbol lax_transfor_underlying
  [A B : Cat]
  [F G : τ (Functor A B)]
  (L : τ (@LaxTransfor A B F G))
  : τ (Transf F G);

rule @lax_transfor_underlying _ _ _ _
      (@make_lax_transfor _ _ _ _ $epsilon _)
  ↪ $epsilon;

unif_rule
  @lax_transfor_underlying $A $B $F $G $L
  ≡ @lax_transfor $A $B $F $G $L
  ↪ [ tt ≡ tt ];

unif_rule
  @lax_transfor $A $B $F $G
    (@make_lax_transfor $A $B $F $G $epsilon _)
  ≡ $epsilon
  ↪ [ tt ≡ tt ];

unif_rule
  @make_lax_transfor $A $B $F $G $epsilon _
  ≡ @make_lax_transfor $A $B $F $G $theta _
  ↪ [ $epsilon ≡ $theta ];

// Transparent typed interface to the proof-time carrier comparison.
symbol make_lax_transfor_carrier_path
  [A B : Cat]
  [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  (lax : τ (@IsLaxTransfor A B F G epsilon))
  : τ (@=
      (Transf F G)
      (@lax_transfor A B F G
        (@make_lax_transfor A B F G epsilon lax))
      epsilon)
≔ @eq_refl
    (Transf F G)
    (@lax_transfor A B F G
      (@make_lax_transfor A B F G epsilon lax));

// Full higher subcategory on conventional lax-transfor objects. Its higher
// homs are the existing ambient modifications and subsequent iterated cells.
injective symbol LaxTransfor_cat
  [A B : Cat]
  [F G : τ (Functor A B)]
  : Cat;

rule Obj (@LaxTransfor_cat $A $B $F $G)
  ↪ @LaxTransfor $A $B $F $G;

rule Hom_cat (@LaxTransfor_cat $A $B $F $G) $L $M
  ↪ Hom_cat
      (@Transf_cat $A $B $F $G)
      (@lax_transfor $A $B $F $G $L)
      (@lax_transfor $A $B $F $G $M);

// Whole inclusion of the profiled hom category into the ambient transfor
// category. Point and hom action only forget evidence; no cell is rebuilt.
injective symbol lax_transfor_include_func
  [A B : Cat]
  [F G : τ (Functor A B)]
  : τ (Functor
      (@LaxTransfor_cat A B F G)
      (@Transf_cat A B F G));

rule @fapp0 _ _ (@lax_transfor_include_func $A $B $F $G) $L
  ↪ @lax_transfor $A $B $F $G $L;

rule @fapp1_func _ _
      (@lax_transfor_include_func $A $B $F $G) $L $M
  ↪ @id_func
      (Hom_cat
        (@Transf_cat $A $B $F $G)
        (@lax_transfor $A $B $F $G $L)
        (@lax_transfor $A $B $F $G $M));

// Direct capped projection joins evaluation of the whole inclusion action.
rule @fapp1_fapp0 _ _
      (@lax_transfor_include_func _ _ _ _) _ _ $Theta
  ↪ $Theta;

// Gray internal hom: strict functor objects and conventional lax-transfor
// arrows. This is intentionally distinct from StrictFunctor_cat, whose homs
// contain every ambient transfor.
injective symbol GrayHom_lax
  (A B : Cat)
  : Cat;

rule Obj (@GrayHom_lax $A $B)
  ↪ @Functor $A $B;

rule Hom_cat (@GrayHom_lax $A $B) $S $T
  ↪ @LaxTransfor_cat
      $A $B
      ($S)
      ($T);

// Whole Gray-hom inclusion into the ambient functor category.
injective symbol grayhom_lax_include_func
  (A B : Cat)
  : τ (Functor
      (@GrayHom_lax A B)
      (@Functor_cat A B));

rule @fapp0 _ _ (@grayhom_lax_include_func $A $B) $S
  ↪ $S;

rule @fapp1_func _ _
      (@grayhom_lax_include_func $A $B) $S $T
  ↪ @lax_transfor_include_func
      $A $B
      ($S)
      ($T);

rule @fapp1_fapp0 _ _
      (@grayhom_lax_include_func $A $B) $S $T $L
  ↪ @lax_transfor
      $A $B
      ($S)
      ($T)
      $L;

// Whole pre/right naturality for the conventional lax profile. The
// post/left cell remains the retained directed comparison.
rule @comp_fapp0
      Cat_cat _ _ _
      (@hom_precomp_along_func
        $A $B $F (@fapp0 $A $B $G $Y) $W $X $h)
      (@tapp1_func
        $A $B $F $G $X $Y
        (@lax_transfor $A $B $F $G $L))
  ↪ @comp_fapp0
      Cat_cat _ _ _
      (@tapp1_func
        $A $B $F $G $W $Y
        (@lax_transfor $A $B $F $G $L))
      (@hom_precomp_along_func $A $A (@id_func $A) $Y $W $X $h);

// Capped pre/right naturality under the same one-sided profile.
rule @comp_fapp0
      $B _ _ _
      (@tapp1_fapp0
        $A $B $F $G $X $Y
        (@lax_transfor $A $B $F $G $L)
        $f)
      (@fapp1_fapp0 $A $B $F $W $X $h)
  ↪ @tapp1_fapp0
      $A $B $F $G $W $Y
      (@lax_transfor $A $B $F $G $L)
      (@comp_fapp0 $A $W $X $Y $f $h);

// Stable proof-time pre/right reading of the off-diagonal action.
unif_rule
  @tapp1_fapp0
    $A $B $F $G $X $Y
    (@lax_transfor $A $B $F $G $L)
    $g
  ≡ @hom_precomp_along_fapp0
      $B $B $IdB $GY $FX $FY $Fg $epsilonY
  ↪ [
    $IdB ≡ (@id Cat_cat $B);
    $GY ≡ (@fapp0 $A $B $G $Y);
    $FX ≡ (@fapp0 $A $B $F $X);
    $FY ≡ (@fapp0 $A $B $F $Y);
    $Fg ≡ (@fapp1_fapp0 $A $B $F $X $Y $g);
    $epsilonY ≡ (@tapp0_fapp0
      $A $B $F $G $Y
      (@lax_transfor $A $B $F $G $L))
  ];

// Cat-valued pre/right projection for the same profile.
rule @fapp0 _ _
      (@tapp0_fapp0
        $K Cat_cat $E $D $y
        (@lax_transfor $K Cat_cat $E $D $L))
      (@fapp0 _ _
        (@fapp1_fapp0 $K Cat_cat $E $x $y $p)
        $u)
  ↪ @fapp0 _ _
      (@tapp1_fapp0
        $K Cat_cat $E $D $x $y
        (@lax_transfor $K Cat_cat $E $D $L)
        $p)
      $u;

/*
  Exact whole-cell identity for the conventional lax profile.

  This mirrors the strict-functor compositor rule: the existing deep
  `fdapp1_comma_projection_transf` remains the semantic owner and computes to
  identity only when its transfor is viewed through `lax_transfor`.  The
  shared base K is inferred to the contravariant base from the stable
  tapp1_con owner; no reducible Op(A) pattern or parallel cell is introduced.
*/
rule @fdapp1_comma_projection_transf
      $K _ _
      (@tapp1_con_at_transf
        $A $B $F $G
        (@lax_transfor $A $B $F $G $L)
        $Y)
      (@fdapp1_int_transfd
        $K _ _
        (@tapp1_con_at_transf
          $A $B $F $G
          (@lax_transfor $A $B $F $G $L)
          $Y))
      $X $W $h
  ↪ @id
      (@Functor_cat
        (Hom_cat $A $X $Y)
        (Hom_cat
          $B
          (@fapp0 $A $B $F $W)
          (@fapp0 $A $B $G $Y)))
      (@strict_transfor_pre_naturality_lhs_func
        $A $B $F $G
        (@lax_transfor $A $B $F $G $L)
        $Y $W $X $h);

// Every classified lax object canonically satisfies its semantic property.
// Both fields compute by reflexivity; no admission certificate is recovered.
symbol lax_transfor_is_lax
  [A B : Cat]
  [F G : τ (Functor A B)]
  (L : τ (@LaxTransfor A B F G))
  : τ (@IsLaxTransfor A B F G (@lax_transfor A B F G L))
≔ λ Y : τ (Obj A),
  λ W : τ (Obj A),
  λ X : τ (Obj A),
  λ h : τ (Hom A W X),
    Struct_sigma
      (@eq_refl
        (Functor
          (Hom_cat A X Y)
          (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y)))
        (@strict_transfor_pre_naturality_lhs_func
          A B F G (@lax_transfor A B F G L) Y W X h))
      (@eq_refl
        (Hom
          (@Functor_cat
            (Hom_cat A X Y)
            (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y)))
          (@strict_transfor_pre_naturality_lhs_func
            A B F G (@lax_transfor A B F G L) Y W X h)
          (@strict_transfor_pre_naturality_rhs_func
            A B F G (@lax_transfor A B F G L) Y W X h))
        (@strict_transfor_pre_naturality_transf
          A B F G (@lax_transfor A B F G L) Y W X h));

symbol strict_transfor_strictness_intro
  [A B : Cat]
  [F G : τ (Functor A B)]
  [epsilon : τ (Transf F G)]
  (post : τ (@IsPostStrictTransfor A B F G epsilon))
  (pre : τ (@IsPreStrictTransfor A B F G epsilon))
  : τ (@IsStrictTransfor A B F G epsilon)
≔ @Product_pair_grpd
    (@IsPostStrictTransfor A B F G epsilon)
    (@IsPreStrictTransfor A B F G epsilon)
    post pre;

symbol strict_transfor_post_evidence
  [A B : Cat]
  [F G : τ (Functor A B)]
  [epsilon : τ (Transf F G)]
  (strict : τ (@IsStrictTransfor A B F G epsilon))
  : τ (@IsPostStrictTransfor A B F G epsilon)
≔ sigma_Fst strict;

symbol strict_transfor_pre_evidence
  [A B : Cat]
  [F G : τ (Functor A B)]
  [epsilon : τ (Transf F G)]
  (strict : τ (@IsStrictTransfor A B F G epsilon))
  : τ (@IsPreStrictTransfor A B F G epsilon)
≔ sigma_Snd strict;

// Evaluating a whole strict cell gives strictness of its existing component.
// This is a reusable projection theorem, not a second pointwise property.
symbol strict_cell_tapp0_evidence
  [K D : Cat]
  [F G : τ (Functor K D)]
  [theta : τ (Transf F G)]
  (e : τ (@IsStrictCell (@Functor_cat K D) F G theta))
  (x : τ (Obj K))
  : τ (@IsStrictCell
      D
      (@fapp0 K D F x)
      (@fapp0 K D G x)
      (@tapp0_fapp0 K D F G x theta))
≔ Struct_sigma
    (@eq_ap
      (Functor K D)
      (Obj D)
      (λ H : τ (Functor K D), @fapp0 K D H x)
      F G
      (@strict_cell_path (@Functor_cat K D) F G theta e))
    (@eq_trans
      (Hom D (@fapp0 K D F x) (@fapp0 K D G x))
      (@tapp0_fapp0 K D F G x theta)
      (@tapp0_fapp0
        K D F G x
        (@path_to_hom
          (@Functor_cat K D) F G
          (@strict_cell_path (@Functor_cat K D) F G theta e)))
      (@path_to_hom
        D
        (@fapp0 K D F x)
        (@fapp0 K D G x)
        (@eq_ap
          (Functor K D)
          (Obj D)
          (λ H : τ (Functor K D), @fapp0 K D H x)
          F G
          (@strict_cell_path (@Functor_cat K D) F G theta e)))
      (@eq_ap
        (Hom (@Functor_cat K D) F G)
        (Hom D (@fapp0 K D F x) (@fapp0 K D G x))
        (λ alpha : τ (Hom (@Functor_cat K D) F G),
          @tapp0_fapp0 K D F G x alpha)
        theta
        (@path_to_hom
          (@Functor_cat K D) F G
          (@strict_cell_path (@Functor_cat K D) F G theta e))
        (@strict_cell_agreement (@Functor_cat K D) F G theta e))
      (@tapp0_path_to_hom
        K D F G
        (@strict_cell_path (@Functor_cat K D) F G theta e)
        x));

// Public capped evidence, obtained by evaluating the whole property at f.
symbol strict_transfor_naturality_evidence
  [A B : Cat]
  [F G : τ (Functor A B)]
  [epsilon : τ (Transf F G)]
  (strict : τ (@IsStrictTransfor A B F G epsilon))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (@IsStrictCell
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B G Z))
      (@fapp0
        (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F X) (@fapp0 A B G Z))
        (@strict_transfor_naturality_lhs_func
          A B F G epsilon X Y Z g)
        f)
      (@fapp0
        (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F X) (@fapp0 A B G Z))
        (@strict_transfor_naturality_rhs_func
          A B F G epsilon X Y Z g)
        f)
      (@tapp1_post_laxity_cell A B F G epsilon X Y Z g f))
≔ @strict_cell_tapp0_evidence
    (Hom_cat A X Y)
    (Hom_cat B (@fapp0 A B F X) (@fapp0 A B G Z))
    (@strict_transfor_naturality_lhs_func
      A B F G epsilon X Y Z g)
    (@strict_transfor_naturality_rhs_func
      A B F G epsilon X Y Z g)
    (@strict_transfor_naturality_transf
      A B F G epsilon X Y Z g)
    ((@strict_transfor_post_evidence A B F G epsilon strict) X Y Z g)
    f;

// Capped pre/right evidence for the one-sided lax-arrow profile.
symbol pre_strict_transfor_naturality_evidence
  [A B : Cat]
  [F G : τ (Functor A B)]
  [epsilon : τ (Transf F G)]
  (pre : τ (@IsPreStrictTransfor A B F G epsilon))
  [W X Y : τ (Obj A)]
  (h : τ (Hom A W X))
  (q : τ (Hom A X Y))
  : τ (@IsStrictCell
      (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y))
      (@fapp0
        (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y))
        (@strict_transfor_pre_naturality_lhs_func
          A B F G epsilon Y W X h)
        q)
      (@fapp0
        (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y))
        (@strict_transfor_pre_naturality_rhs_func
          A B F G epsilon Y W X h)
        q)
      (@tapp1_pre_laxity_cell A B F G epsilon W X Y h q))
≔ @strict_cell_tapp0_evidence
    (Hom_cat A X Y)
    (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y))
    (@strict_transfor_pre_naturality_lhs_func
      A B F G epsilon Y W X h)
    (@strict_transfor_pre_naturality_rhs_func
      A B F G epsilon Y W X h)
    (@strict_transfor_pre_naturality_transf
      A B F G epsilon Y W X h)
    (pre Y W X h)
    q;

// Public full-strict reading delegates to the pre/right evidence projection.
symbol strict_transfor_pre_naturality_evidence
  [A B : Cat]
  [F G : τ (Functor A B)]
  [epsilon : τ (Transf F G)]
  (strict : τ (@IsStrictTransfor A B F G epsilon))
  [W X Y : τ (Obj A)]
  (h : τ (Hom A W X))
  (q : τ (Hom A X Y))
  : τ (@IsStrictCell
      (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y))
      (@fapp0
        (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y))
        (@strict_transfor_pre_naturality_lhs_func
          A B F G epsilon Y W X h)
        q)
      (@fapp0
        (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y))
        (@strict_transfor_pre_naturality_rhs_func
          A B F G epsilon Y W X h)
        q)
      (@tapp1_pre_laxity_cell A B F G epsilon W X Y h q))
≔ @pre_strict_transfor_naturality_evidence
    A B F G epsilon
    (@strict_transfor_pre_evidence A B F G epsilon strict)
    W X Y h q;

// Opaque full-image classifier for full strict transfors.
// Carrier/view relocated to the core owner.

// Admission constructor; evidence choice is not observable.
symbol make_strict_transfor
  [A B : Cat]
  [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  (p : τ (@IsStrictTransfor A B F G epsilon))
  : τ (@StrictTransfor A B F G);

// Stable full-strict ambient view.
// Carrier/view relocated to the core owner.

// Explicit raw observation.
injective symbol strict_transfor_underlying
  [A B : Cat]
  [F G : τ (Functor A B)]
  (U : τ (@StrictTransfor A B F G))
  : τ (Transf F G);

rule @strict_transfor_underlying _ _ _ _
      (@make_strict_transfor _ _ _ _ $epsilon _)
  ↪ $epsilon;

unif_rule
  @strict_transfor_underlying $A $B $F $G $U
  ≡ @strict_transfor $A $B $F $G $U
  ↪ [ tt ≡ tt ];

unif_rule
  @strict_transfor $A $B $F $G
    (@make_strict_transfor $A $B $F $G $epsilon _)
  ≡ $epsilon
  ↪ [ tt ≡ tt ];

unif_rule
  @make_strict_transfor $A $B $F $G $epsilon _
  ≡ @make_strict_transfor $A $B $F $G $theta _
  ↪ [ $epsilon ≡ $theta ];

// Admission respects the existing Cartesian identity and composition.
// These are constructor comparisons for the full-image classifier, not an
// identification with the ambient lax mapping category or new inverse laws.
unif_rule @make_strict_transfor $A $B $F $F
    (@id (Functor_cat $A $B) $F) _
  ≡ @id (Functor_cart_cat $A $B) $F
  ↪ [ tt ≡ tt ];

// lhs-audit: keep 1 -- the ordinary/Cartesian mapping classifiers are actual profile discriminators.
unif_rule @make_strict_transfor $A $B $F $H
    (@comp_fapp0 (Functor_cat $A $B) _ $G _ $eta $epsilon) _
  ≡ @comp_fapp0 (Functor_cart_cat $A $B) _ $G1 _ $V $U
  ↪ [ $G ≡ $G1;
      $eta ≡ @strict_transfor $A $B $G $H $V;
      $epsilon ≡ @strict_transfor $A $B $F $G $U ];

// Transparent typed carrier comparison.
symbol make_strict_transfor_carrier_path
  [A B : Cat]
  [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  (p : τ (@IsStrictTransfor A B F G epsilon))
  : τ (@=
      (Transf F G)
      (@strict_transfor A B F G
        (@make_strict_transfor A B F G epsilon p))
      epsilon)
≔ @eq_refl
    (Transf F G)
    (@strict_transfor A B F G
      (@make_strict_transfor A B F G epsilon p));

// Core-independent strict post action is owned by the nucleus.

// Whole pre/right strict naturality guarded by the same full profile.
rule @comp_fapp0
      Cat_cat _ _ _
      (@hom_precomp_along_func
        $A $B $F (@fapp0 $A $B $G $Y) $W $X $h)
      (@tapp1_func
        $A $B $F $G $X $Y
        (@strict_transfor $A $B $F $G $U))
  ↪ @comp_fapp0
      Cat_cat _ _ _
      (@tapp1_func
        $A $B $F $G $W $Y
        (@strict_transfor $A $B $F $G $U))
      (@hom_precomp_along_func $A $A (@id_func $A) $Y $W $X $h);

// Capped pre/right naturality under the evidence-bearing view.
rule @comp_fapp0
      $B _ _ _
      (@tapp1_fapp0
        $A $B $F $G $X $Y
        (@strict_transfor $A $B $F $G $U)
        $f)
      (@fapp1_fapp0 $A $B $F $W $X $h)
  ↪ @tapp1_fapp0
      $A $B $F $G $W $Y
      (@strict_transfor $A $B $F $G $U)
      (@comp_fapp0 $A $W $X $Y $f $h);

// Profile-guarded proof-time pre/right reading of off-diagonal action.
unif_rule
  @tapp1_fapp0
    $A $B $F $G $X $Y
    (@strict_transfor $A $B $F $G $U)
    $g
  ≡ @hom_precomp_along_fapp0
      $B $B $IdB $GY $FX $FY $Fg $epsilonY
  ↪ [
    $IdB ≡ (@id Cat_cat $B);
    $GY ≡ (@fapp0 $A $B $G $Y);
    $FX ≡ (@fapp0 $A $B $F $X);
    $FY ≡ (@fapp0 $A $B $F $Y);
    $Fg ≡ (@fapp1_fapp0 $A $B $F $X $Y $g);
    $epsilonY ≡ (@tapp0_fapp0
      $A $B $F $G $Y
      (@strict_transfor $A $B $F $G $U))
  ];

// Cat-valued pre/right projection guarded by the strict-transfor view.
rule @fapp0 _ _
      (@tapp0_fapp0
        $K Cat_cat $E $D $y
        (@strict_transfor $K Cat_cat $E $D $U))
      (@fapp0 _ _
        (@fapp1_fapp0 $K Cat_cat $E $x $y $p)
        $u)
  ↪ @fapp0 _ _
      (@tapp1_fapp0
        $K Cat_cat $E $D $x $y
        (@strict_transfor $K Cat_cat $E $D $U)
        $p)
      $u;

// Exact post/left whole-cell identity under the full strict profile.
rule @fdapp1_comma_projection_transf
      $A _ _
      (@tapp1_at_transf
        $A $B $F $G $X
        (@strict_transfor $A $B $F $G $U))
      (@fdapp1_int_transfd
        $A _ _
        (@tapp1_at_transf
          $A $B $F $G $X
          (@strict_transfor $A $B $F $G $U)))
      $Y $Z $g
  ↪ @id
      (@Functor_cat
        (Hom_cat $A $X $Y)
        (Hom_cat
          $B
          (@fapp0 $A $B $F $X)
          (@fapp0 $A $B $G $Z)))
      (@strict_transfor_naturality_lhs_func
        $A $B $F $G
        (@strict_transfor $A $B $F $G $U)
        $X $Y $Z $g);

// Exact pre/right whole-cell identity reuses the stable contravariant owner.
rule @fdapp1_comma_projection_transf
      $K _ _
      (@tapp1_con_at_transf
        $A $B $F $G
        (@strict_transfor $A $B $F $G $U)
        $Y)
      (@fdapp1_int_transfd
        $K _ _
        (@tapp1_con_at_transf
          $A $B $F $G
          (@strict_transfor $A $B $F $G $U)
          $Y))
      $X $W $h
  ↪ @id
      (@Functor_cat
        (Hom_cat $A $X $Y)
        (Hom_cat
          $B
          (@fapp0 $A $B $F $W)
          (@fapp0 $A $B $G $Y)))
      (@strict_transfor_pre_naturality_lhs_func
        $A $B $F $G
        (@strict_transfor $A $B $F $G $U)
        $Y $W $X $h);

// Canonical full strictness over the two existing skew whole cells.
symbol strict_transfor_is_strict
  [A B : Cat]
  [F G : τ (Functor A B)]
  (U : τ (@StrictTransfor A B F G))
  : τ (@IsStrictTransfor A B F G
      (@strict_transfor A B F G U))
≔ @strict_transfor_strictness_intro
    A B F G
    (@strict_transfor A B F G U)
    (λ X : τ (Obj A),
      λ Y : τ (Obj A),
      λ Z : τ (Obj A),
      λ g : τ (Hom A Y Z),
        Struct_sigma
          (@eq_refl
            (Functor
              (Hom_cat A X Y)
              (Hom_cat B (@fapp0 A B F X) (@fapp0 A B G Z)))
            (@strict_transfor_naturality_lhs_func
              A B F G (@strict_transfor A B F G U) X Y Z g))
          (@eq_refl
            (Hom
              (@Functor_cat
                (Hom_cat A X Y)
                (Hom_cat B (@fapp0 A B F X) (@fapp0 A B G Z)))
              (@strict_transfor_naturality_lhs_func
                A B F G (@strict_transfor A B F G U) X Y Z g)
              (@strict_transfor_naturality_rhs_func
                A B F G (@strict_transfor A B F G U) X Y Z g))
            (@strict_transfor_naturality_transf
              A B F G (@strict_transfor A B F G U) X Y Z g)))
    (λ Y : τ (Obj A),
      λ W : τ (Obj A),
      λ X : τ (Obj A),
      λ h : τ (Hom A W X),
        Struct_sigma
          (@eq_refl
            (Functor
              (Hom_cat A X Y)
              (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y)))
            (@strict_transfor_pre_naturality_lhs_func
              A B F G (@strict_transfor A B F G U) Y W X h))
          (@eq_refl
            (Hom
              (@Functor_cat
                (Hom_cat A X Y)
                (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y)))
              (@strict_transfor_pre_naturality_lhs_func
                A B F G (@strict_transfor A B F G U) Y W X h)
              (@strict_transfor_pre_naturality_rhs_func
                A B F G (@strict_transfor A B F G U) Y W X h))
            (@strict_transfor_pre_naturality_transf
              A B F G (@strict_transfor A B F G U) Y W X h)));

/* API-04V: vertical accumulation is profile-specific. The left formula
   requires the later transfor's pre/right profile; the right formula needs
   the earlier transfor's post/left profile. Full-strict views provide both.
   The outer codomain B is a real ambient-composition guard: coincident
   Hom types in another presentation do not identify its composition owner.
   No opaque oplax classifier is introduced for this bounded migration. */

// Later lax_transfor view supplies the pre/right leg.
rule @comp_fapp0 $B _ _ _
      (@tapp0_fapp0 _ _ _ _ $Y (@lax_transfor $A $B $G $H $V))
      (@tapp1_fapp0 $A $B $F $G $X $Y $epsilon $f)
  ↪ @tapp1_fapp0 $A $B $F $H $X $Y
      (@comp_fapp0 (Functor_cat $A $B) $F $G $H (@lax_transfor $A $B $G $H $V) $epsilon) $f;

// Later strict_transfor view supplies the pre/right leg.
rule @comp_fapp0 $B _ _ _
      (@tapp0_fapp0 _ _ _ _ $Y (@strict_transfor $A $B $G $H $V))
      (@tapp1_fapp0 $A $B $F $G $X $Y $epsilon $f)
  ↪ @tapp1_fapp0 $A $B $F $H $X $Y
      (@comp_fapp0 (Functor_cat $A $B) $F $G $H (@strict_transfor $A $B $G $H $V) $epsilon) $f;

// Earlier full-strict view supplies the post/left leg.
rule @comp_fapp0 $B _ _ _
      (@tapp1_fapp0 $A $B $G $H $X $Y $eta $f)
      (@tapp0_fapp0 _ _ _ _ $X (@strict_transfor $A $B $F $G $U))
  ↪ @tapp1_fapp0 $A $B $F $H $X $Y
      (@comp_fapp0 (Functor_cat $A $B) $F $G $H $eta (@strict_transfor $A $B $F $G $U)) $f;

// Both legs for simultaneous accumulation of p and q.
rule @comp_fapp0 $B _ _ _
      (@tapp1_fapp0 _ _ _ _ $Y $Z (@lax_transfor $A $B $G $H $V) $q)
      (@tapp1_fapp0 _ _ _ _ $X $Y (@strict_transfor $A $B $F $G $U) $p)
  ↪ @tapp1_fapp0 $A $B $F $H $X $Z
      (@comp_fapp0 (Functor_cat $A $B) $F $G $H (@lax_transfor $A $B $G $H $V) (@strict_transfor $A $B $F $G $U))
      (@comp_fapp0 $A $X $Y $Z $q $p);

// Both legs for simultaneous accumulation of p and q.
rule @comp_fapp0 $B _ _ _
      (@tapp1_fapp0 _ _ _ _ $Y $Z (@strict_transfor $A $B $G $H $V) $q)
      (@tapp1_fapp0 _ _ _ _ $X $Y (@strict_transfor $A $B $F $G $U) $p)
  ↪ @tapp1_fapp0 $A $B $F $H $X $Z
      (@comp_fapp0 (Functor_cat $A $B) $F $G $H (@strict_transfor $A $B $G $H $V) (@strict_transfor $A $B $F $G $U))
      (@comp_fapp0 $A $X $Y $Z $q $p);

// -----------------------------------------------------------------------------------------------
// Strict displayed-functor profile over the existing directed laxity cell
// -----------------------------------------------------------------------------------------------

// Strictness constrains the public whole-in-fibre-object cell at every base
// arrow; it does not store a second naturality transformation.
symbol IsStrictFunctord
  [K : Cat]
  [E D : τ (Catd K)]
  (FF : τ (Functord E D))
  : Grpd
≔ @Pi_grpd
    (Obj K)
    (λ x : τ (Obj K),
      @Pi_grpd
        (Obj K)
        (λ y : τ (Obj K),
          @Pi_grpd
            (Hom K x y)
            (λ p : τ (Hom K x y),
              @IsStrictCell
                (@Functor_cat
                  (Fibre_cat E x)
                  (Fibre_cat D y))
                (@functord_transport_lhs_func K E D FF x y p)
                (@functord_transport_rhs_func K E D FF x y p)
                (@functord_laxity_transf K E D FF x y p))));

// Opaque full-image classifier for strict displayed functors.
injective symbol StrictFunctord
  [K : Cat]
  (E D : τ (Catd K))
  : Grpd;

// Admission constructor; evidence choice is not observable.
symbol make_strict_functord
  [K : Cat]
  [E D : τ (Catd K)]
  (FF : τ (Functord E D))
  (p : τ (@IsStrictFunctord K E D FF))
  : τ (@StrictFunctord K E D);

// Stable strict displayed-functor view.
injective symbol strict_functord
  [K : Cat]
  [E D : τ (Catd K)]
  (S : τ (@StrictFunctord K E D))
  : τ (Functord E D);

// Explicit raw observation.
injective symbol strict_functord_underlying
  [K : Cat]
  [E D : τ (Catd K)]
  (S : τ (@StrictFunctord K E D))
  : τ (Functord E D);

rule @strict_functord_underlying _ _ _
      (@make_strict_functord _ _ _ $FF _)
  ↪ $FF;

unif_rule
  @strict_functord_underlying $K $E $D $S
  ≡ @strict_functord $K $E $D $S
  ↪ [ tt ≡ tt ];

unif_rule
  @strict_functord $K $E $D
    (@make_strict_functord $K $E $D $FF _)
  ≡ $FF
  ↪ [ tt ≡ tt ];

unif_rule
  @make_strict_functord $K $E $D $FF _
  ≡ @make_strict_functord $K $E $D $GG _
  ↪ [ $FF ≡ $GG ];

// Transparent typed carrier comparison.
symbol make_strict_functord_carrier_path
  [K : Cat]
  [E D : τ (Catd K)]
  (FF : τ (Functord E D))
  (p : τ (@IsStrictFunctord K E D FF))
  : τ (@=
      (Functord E D)
      (@strict_functord K E D
        (@make_strict_functord K E D FF p))
      FF)
≔ @eq_refl
    (Functord E D)
    (@strict_functord K E D
      (@make_strict_functord K E D FF p));

// Capped strictness is component evaluation of the existing whole cell.
symbol strict_functord_laxity_evidence
  [K : Cat]
  [E D : τ (Catd K)]
  [FF : τ (Functord E D)]
  (strict : τ (@IsStrictFunctord K E D FF))
  [x y : τ (Obj K)]
  (p : τ (Hom K x y))
  (u : τ (Obj (Fibre_cat E x)))
  : τ (@IsStrictCell
      (Fibre_cat D y)
      (@fapp0
        (Fibre_cat E x) (Fibre_cat D y)
        (@functord_transport_lhs_func K E D FF x y p) u)
      (@fapp0
        (Fibre_cat E x) (Fibre_cat D y)
        (@functord_transport_rhs_func K E D FF x y p) u)
      (@tapp0_fapp0
        (Fibre_cat E x) (Fibre_cat D y)
        (@functord_transport_lhs_func K E D FF x y p)
        (@functord_transport_rhs_func K E D FF x y p)
        u
        (@functord_laxity_transf K E D FF x y p)))
≔ @strict_cell_tapp0_evidence
    (Fibre_cat E x)
    (Fibre_cat D y)
    (@functord_transport_lhs_func K E D FF x y p)
    (@functord_transport_rhs_func K E D FF x y p)
    (@functord_laxity_transf K E D FF x y p)
    (strict x y p)
    u;

// Compatibility observations for the strict displayed profile. The selected
// conventional-lax default already fixes the pre/right leg for every FF;
// the former profile-only target/right unifiers are therefore redundant.
symbol strict_functord_transport_rhs_tele_path
  [K : Cat]
  [E D : τ (Catd K)]
  (S : τ (@StrictFunctord K E D))
  (x y : τ (Obj K))
  : τ (@=
      (Functor
        (Hom_cat K x y)
        (Functor_cart_cat (Fibre_cat E x) (Fibre_cat D y)))
      (@tapp1_func K Cat_cart E D x y
        (@strict_functord K E D S))
      (@functord_transport_rhs_tele_func
        K E D (@strict_functord K E D S) x y))
≔ @eq_refl
    (Functor
      (Hom_cat K x y)
      (Functor_cart_cat (Fibre_cat E x) (Fibre_cat D y)))
    (@tapp1_func K Cat_cart E D x y
      (@strict_functord K E D S));

symbol strict_functord_transport_rhs_path
  [K : Cat]
  [E D : τ (Catd K)]
  (S : τ (@StrictFunctord K E D))
  [x y : τ (Obj K)]
  (p : τ (Hom K x y))
  : τ (@=
      (Functor (Fibre_cat E x) (Fibre_cat D y))
      (@tapp1_fapp0 K Cat_cart E D x y
        (@strict_functord K E D S) p)
      (@functord_transport_rhs_func
        K E D (@strict_functord K E D S) x y p))
≔ @eq_sym
    (Functor (Fibre_cat E x) (Fibre_cat D y))
    (@functord_transport_rhs_func K E D (@strict_functord K E D S) x y p)
    (@functord_transport_func K E D (@strict_functord K E D S) x y p)
    (@functord_transport_rhs_agrees K E D (@strict_functord K E D S) x y p);
