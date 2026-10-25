require open emdash.emdash3_2_one_cat_diagram_family_reflection;
/* Categorical maps of the actual native adjacent inputs. */
require open emdash.emdash3_2_one_cat_diagram_map_equivalences;
require open emdash.emdash3_2_one_cat_zero_cone_map_equivalences;
require open emdash.emdash3_2_zero_arrow_diagram_observations;

// Original outgoing diagrams are compared by an actual transformation.
symbol native_pair_diagram_map [C : Cat] (S : τ (@PreadditiveCategory C))
 (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)] (T : τ (@TerminalObject C t))
 [a0 a1 : τ (Obj C)] [d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))]
 (h0 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a0) d0))
 (h1 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a1) d1))
 (c0 : τ (Hom C a0 a1))
 (c1 : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1)))
 (c2 : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)))
 (p : τ (@= (Hom C a0 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1)) (@comp_fapp0 C a0 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) c1
  (@terminal_arrow_test_incoming C t T a0 d0 h0)) (@comp_fapp0 C a0 a1 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@terminal_arrow_test_incoming C t T a1 d1 h1) c0)))
 (q : τ (@= (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)) (@comp_fapp0 C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1) c2
  (@terminal_arrow_test_outgoing C d0)) (@comp_fapp0 C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0)
  (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)
  (@terminal_arrow_test_outgoing C d1) c1)))
 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1)
≔ @fapp1_fapp0 (Functor_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@one_cat_diagram_oplax_include_func C C1) (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d0) (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d1) (@one_cat_original_diagram_map C C1 (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d0) (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d1) c1 c2
 (@path_to_hom (Hom_cat C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)) _ _ q));

// Original incoming comparison determines the native compatibility cell.
symbol native_pair_input_compatibility [C : Cat] (S : τ (@PreadditiveCategory C))
 (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)] (T : τ (@TerminalObject C t))
 [a0 a1 : τ (Obj C)] [d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))]
 (h0 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a0) d0))
 (h1 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a1) d1))
 (c0 : τ (Hom C a0 a1))
 (c1 : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1)))
 (c2 : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)))
 (p : τ (@= (Hom C a0 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1)) (@comp_fapp0 C a0 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) c1
  (@terminal_arrow_test_incoming C t T a0 d0 h0)) (@comp_fapp0 C a0 a1 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@terminal_arrow_test_incoming C t T a1 d1 h1) c0)))
 (q : τ (@= (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)) (@comp_fapp0 C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1) c2
  (@terminal_arrow_test_outgoing C d0)) (@comp_fapp0 C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0)
  (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)
  (@terminal_arrow_test_outgoing C d1) c1)))
 : τ (@= (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a0) d1) (@comp_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C
  (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a0) d0 d1
  (@native_pair_diagram_map C S C1 t T a0 a1 d0 d1 h0 h1 c0 c1 c2 p q) h0) (@comp_fapp0 (Functor_oplax_cat
  WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a0)
  (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a1) d1 h1 (@fapp1_fapp0
  C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a0 a1 c0)))
≔ @one_cat_oplax_diagram_map_path C C1 (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func
  C t T) a0) d1 (@comp_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a0) d0 d1 (@native_pair_diagram_map C S C1 t T a0 a1 d0 d1 h0 h1 c0
  c1 c2 p q) h0) (@comp_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a0) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a1) d1 h1 (@fapp1_fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a0 a1 c0)) p
 (@eq_trans _ _ _ _
  (@preadditive_terminal_to_zero_path C S t (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1) T
  (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a0) d1 (@comp_fapp0 (Functor_oplax_cat WalkingArrow_cat
  C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a0) d0 d1
  (@native_pair_diagram_map C S C1 t T a0 a1 d0 d1 h0 h1 c0 c1 c2 p q) h0)))
  (@eq_sym _ _ _ (@preadditive_terminal_to_zero_path C S t (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1) T (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a0) d1 (@comp_fapp0 (Functor_oplax_cat WalkingArrow_cat
  C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a0) (@fapp0 C
  (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a1) d1 h1 (@fapp1_fapp0 C
  (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a0 a1 c0))))));

// Keep the original source/diagram objects and whole map data.
symbol native_pair_input_map [C : Cat] (S : τ (@PreadditiveCategory C))
 (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)] (T : τ (@TerminalObject C t))
 [a0 a1 : τ (Obj C)] [d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))]
 (h0 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a0) d0))
 (h1 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a1) d1))
 (c0 : τ (Hom C a0 a1))
 (c1 : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1)))
 (c2 : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)))
 (p : τ (@= (Hom C a0 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1)) (@comp_fapp0 C a0 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) c1
  (@terminal_arrow_test_incoming C t T a0 d0 h0)) (@comp_fapp0 C a0 a1 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@terminal_arrow_test_incoming C t T a1 d1 h1) c0)))
 (q : τ (@= (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)) (@comp_fapp0 C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1) c2
  (@terminal_arrow_test_outgoing C d0)) (@comp_fapp0 C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0)
  (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)
  (@terminal_arrow_test_outgoing C d1) c1)))
 : τ (Hom (@ZeroArrowCone_cat C t T) (@zero_arrow_cone_obj C t T a0 d0 h0) (@zero_arrow_cone_obj C t T a1
  d1 h1))
≔ @zero_cone_native_map C t T a0 a1 d0 d1 h0 h1 c0 (@native_pair_diagram_map C S C1 t T a0 a1 d0 d1 h0 h1
  c0 c1 c2 p q)
 (@path_to_hom (Hom_cat (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a0) d1) (@comp_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C
  (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a0) d0 d1
  (@native_pair_diagram_map C S C1 t T a0 a1 d0 d1 h0 h1 c0 c1 c2 p q) h0) (@comp_fapp0 (Functor_oplax_cat
  WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a0)
  (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a1) d1 h1 (@fapp1_fapp0
  C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a0 a1 c0))
  (@native_pair_input_compatibility C S C1 t T a0 a1 d0 d1 h0 h1 c0 c1 c2 p q));

// All three original equivalences act on the complete native input.
symbol native_pair_input_equiv [C : Cat] (S : τ (@PreadditiveCategory C))
 (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)] (T : τ (@TerminalObject C t))
 [a0 a1 : τ (Obj C)] [d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))]
 (h0 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a0) d0))
 (h1 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) a1) d1))
 (c0 : τ (Hom C a0 a1))
 (c1 : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1)))
 (c2 : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)))
 (p : τ (@= (Hom C a0 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1)) (@comp_fapp0 C a0 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) c1
  (@terminal_arrow_test_incoming C t T a0 d0 h0)) (@comp_fapp0 C a0 a1 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@terminal_arrow_test_incoming C t T a1 d1 h1) c0)))
 (q : τ (@= (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)) (@comp_fapp0 C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1) c2
  (@terminal_arrow_test_outgoing C d0)) (@comp_fapp0 C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0)
  (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)
  (@terminal_arrow_test_outgoing C d1) c1)))
 (U0 : τ (@OmegaEquivAlong C a0 a1 c0))
 (U1 : τ (@OmegaEquivAlong C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) c1))
 (U2 : τ (@OmegaEquivAlong C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1) c2))
 : τ (@OmegaEquivAlong (@ZeroArrowCone_cat C t T) (@zero_arrow_cone_obj C t T a0 d0 h0)
  (@zero_arrow_cone_obj C t T a1 d1 h1) (@native_pair_input_map C S C1 t T a0 a1 d0 d1 h0 h1 c0 c1 c2 p
  q))
≔ @one_cat_zero_cone_map_equiv C C1 t T a0 a1 d0 d1 h0 h1 (@native_pair_input_map C S C1 t T a0 a1 d0 d1
  h0 h1 c0 c1 c2 p q) U0
 (@one_cat_omega_equiv_fmap (Functor_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@one_cat_oplax_functor_category WalkingArrow_cat C C1) (@one_cat_diagram_oplax_include_func C C1) (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d0) (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d1) (@one_cat_original_diagram_map C C1 (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d0) (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d1) c1 c2
 (@path_to_hom (Hom_cat C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)) _ _ q)) (@one_cat_diagram_map_equiv C C1 (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d0) (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d1) (@one_cat_original_diagram_map C C1 (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d0) (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d1) c1 c2
 (@path_to_hom (Hom_cat C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)) _ _ q)) U1 U2));
