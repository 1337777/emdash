/* NF-1 receiver candidate. Definitions only; no new structural laws.
   Derive the conventional-lax admission from the existing default leg. */
require open emdash.emdash3_2_gray_transformation_graph;
require open emdash.emdash3_2_diagram_evaluation;

symbol nerve_default_lax_profile [A B : Cat]
  [F G : τ (Functor A B)] (epsilon : τ (@Transf A B F G))
  : τ (@IsLaxTransfor A B F G epsilon)
≔ λ Y : τ (Obj A), λ W : τ (Obj A), λ X : τ (Obj A),
  λ h : τ (Hom A W X),
  Struct_sigma
    (@eq_refl
      (Functor (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y)))
      (@strict_transfor_pre_naturality_lhs_func A B F G epsilon Y W X h))
    (@eq_refl
      (Hom (Functor_cat (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y)))
        (@strict_transfor_pre_naturality_lhs_func A B F G epsilon Y W X h)
        (@strict_transfor_pre_naturality_rhs_func A B F G epsilon Y W X h))
      (@strict_transfor_pre_naturality_transf A B F G epsilon Y W X h));

symbol nerve_walking_eval_transf (C : Cat)
  : τ (@Transf (Functor_oplax_cat WalkingArrow_cat C) C
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt))
≔ @diagram_oplax_evaluation_transf WalkingArrow_cat C
    walking_arrow_src walking_arrow_tgt walking_arrow_generator;

symbol nerve_walking_eval_lax (C : Cat)
  : τ (@LaxTransfor (Functor_oplax_cat WalkingArrow_cat C) C
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt))
≔ @make_lax_transfor (Functor_oplax_cat WalkingArrow_cat C) C _ _
    (nerve_walking_eval_transf C)
    (@nerve_default_lax_profile (Functor_oplax_cat WalkingArrow_cat C) C _ _
      (nerve_walking_eval_transf C));

symbol nerve_walking_observe_func (C : Cat)
  : τ (Functor (Functor_oplax_cat WalkingArrow_cat C) (@LaxArrow_cat C))
≔ @gray_transf_graph_func (Functor_oplax_cat WalkingArrow_cat C) C
    (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
    (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)
    (nerve_walking_eval_lax C);

// The underlying evaluator itself computes before profile admission.
assert [C : Cat] (F : τ (Functor WalkingArrow_cat C)) ⊢
  @tapp0_fapp0 _ _ _ _ (@OddDual_func WalkingArrow_cat C F)
    (nerve_walking_eval_transf C)
  ≡ @fapp1_fapp0 WalkingArrow_cat C F
      walking_arrow_src walking_arrow_tgt walking_arrow_generator;

// Use the existing whole carrier path instead of folding a component's syntax.
symbol nerve_walking_eval_component_path [C : Cat]
  (F : τ (Functor WalkingArrow_cat C))
  : τ (@= (Hom C (@fapp0 WalkingArrow_cat C F walking_arrow_src)
      (@fapp0 WalkingArrow_cat C F walking_arrow_tgt))
    (@tapp0_fapp0 _ _ _ _ (@OddDual_func WalkingArrow_cat C F)
      (@lax_transfor _ _ _ _ (nerve_walking_eval_lax C)))
    (@fapp1_fapp0 WalkingArrow_cat C F
      walking_arrow_src walking_arrow_tgt walking_arrow_generator))
≔ @eq_ap
    (@Transf (Functor_oplax_cat WalkingArrow_cat C) C
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt))
    (Hom C (@fapp0 WalkingArrow_cat C F walking_arrow_src)
      (@fapp0 WalkingArrow_cat C F walking_arrow_tgt))
    (λ eta : τ (@Transf (Functor_oplax_cat WalkingArrow_cat C) C
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)),
      @tapp0_fapp0 _ _ _ _ (@OddDual_func WalkingArrow_cat C F) eta)
    _ _
    (@make_lax_transfor_carrier_path _ _ _ _ (nerve_walking_eval_transf C)
      (@nerve_default_lax_profile _ _ _ _ (nerve_walking_eval_transf C)));

symbol nerve_walking_observe_object_path [C : Cat]
  (F : τ (Functor WalkingArrow_cat C))
  : τ (@= (Obj (@LaxArrow_cat C))
      (@fapp0 _ _ (nerve_walking_observe_func C) (@OddDual_func WalkingArrow_cat C F))
      (@lax_edge C
        (@fapp0 WalkingArrow_cat C F walking_arrow_src)
        (@fapp0 WalkingArrow_cat C F walking_arrow_tgt)
        (@fapp1_fapp0 WalkingArrow_cat C F
          walking_arrow_src walking_arrow_tgt walking_arrow_generator)))
≔ @eq_ap
    (Hom C (@fapp0 WalkingArrow_cat C F walking_arrow_src)
      (@fapp0 WalkingArrow_cat C F walking_arrow_tgt))
    (Obj (@LaxArrow_cat C))
    (λ u : τ (Hom C (@fapp0 WalkingArrow_cat C F walking_arrow_src)
      (@fapp0 WalkingArrow_cat C F walking_arrow_tgt)),
      @lax_edge C (@fapp0 WalkingArrow_cat C F walking_arrow_src)
        (@fapp0 WalkingArrow_cat C F walking_arrow_tgt) u)
    _ _ (@nerve_walking_eval_component_path C F);

// The admission does not additionally grant post/left strict naturality.
assertnot [A B : Cat] [F G : τ (Functor A B)]
  (epsilon : τ (@Transf A B F G)) ⊢
  @nerve_default_lax_profile A B F G epsilon
  : τ (@IsStrictTransfor A B F G epsilon);

// Whole square observation at arbitrary oplax input maps. The filler is the
// existing internal-action cell, not a separately supplied square.
symbol nerve_walking_observe_square [C : Cat]
  [F G : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))]
  (eta : τ (Hom (Functor_oplax_cat WalkingArrow_cat C) F G))
  : τ (Hom (@LaxArrow_cat C)
      (@fapp0 _ _ (nerve_walking_observe_func C) F)
      (@fapp0 _ _ (nerve_walking_observe_func C) G))
≔ @fapp1_fapp0 _ _ (nerve_walking_observe_func C) F G eta;

assert [C : Cat]
  [F G : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))]
  (eta : τ (Hom (Functor_oplax_cat WalkingArrow_cat C) F G)) ⊢
  @nerve_walking_observe_square C F G eta
  ≡ @lax_square C
      (@fapp0 _ _ (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) F)
      (@fapp0 _ _ (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) G)
      (@fapp0 _ _ (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) F)
      (@fapp0 _ _ (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) G)
      (@tapp0_fapp0 _ _ _ _ F (@lax_transfor _ _ _ _ (nerve_walking_eval_lax C)))
      (@tapp0_fapp0 _ _ _ _ G (@lax_transfor _ _ _ _ (nerve_walking_eval_lax C)))
      (@fapp1_fapp0 _ _ (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) F G eta)
      (@fapp1_fapp0 _ _ (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) F G eta)
      (@gray_transf_standard_cell (Functor_oplax_cat WalkingArrow_cat C) C
        (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
        (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)
        (nerve_walking_eval_lax C) F G eta);

// The full next Hom remains the action of the same constructed observer.
symbol nerve_walking_observe_modification_func [C : Cat]
  [F G : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))]
  (eta theta : τ (Hom (Functor_oplax_cat WalkingArrow_cat C) F G))
  : τ (Functor
      (Hom_cat (Hom_cat (Functor_oplax_cat WalkingArrow_cat C) F G) eta theta)
      (Hom_cat
        (Hom_cat (@LaxArrow_cat C)
          (@fapp0 _ _ (nerve_walking_observe_func C) F)
          (@fapp0 _ _ (nerve_walking_observe_func C) G))
        (@nerve_walking_observe_square C F G eta)
        (@nerve_walking_observe_square C F G theta)))
≔ @fapp1_func _ _
    (@fapp1_func _ _ (nerve_walking_observe_func C) F G) eta theta;

// The raw default does not turn a noncommuting post/left square into an equality.
assertnot [A B : Cat] [F G : τ (Functor A B)]
  (epsilon : τ (@Transf A B F G)) [x y : τ (Obj A)]
  (p : τ (Hom A x y)) ⊢
  @comp_fapp0 B (@fapp0 A B F x) (@fapp0 A B G x) (@fapp0 A B G y)
    (@fapp1_fapp0 A B G x y p) (@tapp0_fapp0 A B F G x epsilon)
  ≡ @comp_fapp0 B (@fapp0 A B F x) (@fapp0 A B F y) (@fapp0 A B G y)
    (@tapp0_fapp0 A B F G y epsilon) (@fapp1_fapp0 A B F x y p);

// Walking-first coevaluation from the current mixed exchange. The public
// strict default eliminates all legacy strict-object admission premises.
symbol nerve_walking_left_coevaluation (B : Cat)
  : τ (Functor B
      (Functor_oplax_cat WalkingArrow_cat (@GrayTensor_R WalkingArrow_cat B)))
≔ @diagram_family_shape_func WalkingArrow_cat B (@GrayTensor_R WalkingArrow_cat B)
    (@comp_cat_fapp0 WalkingArrow_cat
      (@GrayHom_lax B (@GrayTensor_R WalkingArrow_cat B))
      (Functor_cat B (@GrayTensor_R WalkingArrow_cat B))
      (@grayhom_lax_include_func B (@GrayTensor_R WalkingArrow_cat B))
      (@gray_coevaluation_R_func WalkingArrow_cat B));

// An actual whole native edge family in the tensor, including B's arrows
// and modifications. At B=I this is a whole walking-square consumer.
symbol nerve_tensor_coordinate_family (B : Cat)
  : τ (Functor B (@LaxArrow_cat (@GrayTensor_R WalkingArrow_cat B)))
≔ @comp_cat_fapp0 B
    (Functor_oplax_cat WalkingArrow_cat (@GrayTensor_R WalkingArrow_cat B))
    (@LaxArrow_cat (@GrayTensor_R WalkingArrow_cat B))
    (nerve_walking_observe_func (@GrayTensor_R WalkingArrow_cat B))
    (nerve_walking_left_coevaluation B);

// Decode only the object diagram for its original generator observation.
symbol nerve_tensor_coordinate_diagram [B : Cat] (b : τ (Obj B))
  : τ (Functor WalkingArrow_cat (@GrayTensor_R WalkingArrow_cat B))
≔ @OddDual_func (OddDual_cat WalkingArrow_cat)
    (OddDual_cat (@GrayTensor_R WalkingArrow_cat B))
    (@fapp0 _ _ (nerve_walking_left_coevaluation B) b);

// The two endpoint edges are the original outer-coordinate tensor arrows.
assert ⊢ @nerve_walking_observe_object_path GrayWalkingSquare_cat
    (@nerve_tensor_coordinate_diagram WalkingArrow_cat walking_arrow_src)
  : τ (@= (Obj (@LaxArrow_cat GrayWalkingSquare_cat))
      (@fapp0 _ _ (nerve_tensor_coordinate_family WalkingArrow_cat) walking_arrow_src)
      (@lax_edge GrayWalkingSquare_cat gray_square_obj00 gray_square_obj10
        gray_square_outer_src_arrow));

assert ⊢ @nerve_walking_observe_object_path GrayWalkingSquare_cat
    (@nerve_tensor_coordinate_diagram WalkingArrow_cat walking_arrow_tgt)
  : τ (@= (Obj (@LaxArrow_cat GrayWalkingSquare_cat))
      (@fapp0 _ _ (nerve_tensor_coordinate_family WalkingArrow_cat) walking_arrow_tgt)
      (@lax_edge GrayWalkingSquare_cat gray_square_obj01 gray_square_obj11
        gray_square_outer_tgt_arrow));
