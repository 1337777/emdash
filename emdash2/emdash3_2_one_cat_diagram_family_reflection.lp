/* Whole reflection through the actual ordinary-target profile comparison,
   Cartesian exchange, and the original ordinary diagram reflection. */
require open emdash.emdash3_2_one_cat_diagram_map_paths;
require open emdash.emdash3_2_one_cat_adjunction_families;
require open emdash.emdash3_2_one_cat_transfor_profiles;

// Convert both mapping levels. The outer comparison admits maps into the
// ordinary mapping category; Cartesian postcomposition changes its codomain.
symbol one_cat_family_to_cart_func [B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (Functor (Functor_cat B (Functor_cat I C))
    (Functor_cart_cat B (Functor_cart_cat I C)))
≔ @comp_cat_fapp0 (Functor_cat B (Functor_cat I C))
    (Functor_cart_cat B (Functor_cat I C))
    (Functor_cart_cat B (Functor_cart_cat I C))
    (@comp_cat_cov_cart_func B (Functor_cat I C) (Functor_cart_cat I C)
      (@one_cat_mapping_to_cart_func I C C1))
    (@one_cat_mapping_to_cart_func B (Functor_cat I C)
      (@one_cat_functor_category I C C1));

symbol one_cat_family_from_cart_func [B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (Functor (Functor_cart_cat B (Functor_cart_cat I C))
    (Functor_cat B (Functor_cat I C)))
≔ @comp_cat_fapp0 (Functor_cart_cat B (Functor_cart_cat I C))
    (Functor_cart_cat B (Functor_cat I C))
    (Functor_cat B (Functor_cat I C))
    (@one_cat_mapping_from_cart_func B (Functor_cat I C)
      (@one_cat_functor_category I C C1))
    (@comp_cat_cov_cart_func B (Functor_cart_cat I C) (Functor_cat I C)
      (@one_cat_mapping_from_cart_func I C C1));

// The actual composite maps, with their original selected inverse factors.
symbol one_cat_family_from_to_path [B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (@= (Functor (Functor_cat B (Functor_cat I C)) (Functor_cat B (Functor_cat I C)))
    (@comp_cat_fapp0 _ _ _ (@one_cat_family_from_cart_func B I C C1)
      (@one_cat_family_to_cart_func B I C C1))
    (@id_func (Functor_cat B (Functor_cat I C))))
≔ let A0 : Cat ≔ Functor_cat B (Functor_cat I C) in
  let A1 : Cat ≔ Functor_cart_cat B (Functor_cat I C) in
  let A2 : Cat ≔ Functor_cart_cat B (Functor_cart_cat I C) in
  let a : τ (Functor A0 A1) ≔ @one_cat_mapping_to_cart_func B (Functor_cat I C) (@one_cat_functor_category I C C1) in
  let b : τ (Functor A1 A2) ≔ @comp_cat_cov_cart_func B (Functor_cat I C) (Functor_cart_cat I C) (@one_cat_mapping_to_cart_func I C C1) in
  let c : τ (Functor A2 A1) ≔ @comp_cat_cov_cart_func B (Functor_cart_cat I C) (Functor_cat I C) (@one_cat_mapping_from_cart_func I C C1) in
  let d : τ (Functor A1 A0) ≔ @one_cat_mapping_from_cart_func B (Functor_cat I C) (@one_cat_functor_category I C C1) in
  @eq_trans (Functor A0 A0)
    (@comp_cat_fapp0 A0 A2 A0 (@comp_cat_fapp0 A2 A1 A0 d c) (@comp_cat_fapp0 A0 A1 A2 b a))
    (@comp_cat_fapp0 A0 A1 A0 (@comp_cat_fapp0 A1 A2 A0 (@comp_cat_fapp0 A2 A1 A0 d c) b) a)
    (@id_func A0)
    (@comp_assoc Cat_cat A0 A1 A2 A0 (@comp_cat_fapp0 A2 A1 A0 d c) b a)
    (@eq_ap (Functor A1 A0) (Functor A0 A0)
      (λ z : τ (Functor A1 A0), @comp_cat_fapp0 A0 A1 A0 z a)
      (@comp_cat_fapp0 A1 A2 A0 (@comp_cat_fapp0 A2 A1 A0 d c) b)
      (@comp_cat_fapp0 A1 A1 A0 d (@comp_cat_fapp0 A1 A2 A1 c b))
      (@eq_sym (Functor A1 A0) _ _ (@comp_assoc Cat_cat A1 A2 A1 A0 d c b)));

symbol one_cat_family_to_from_path [B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (@= (Functor (Functor_cart_cat B (Functor_cart_cat I C)) (Functor_cart_cat B (Functor_cart_cat I C)))
    (@comp_cat_fapp0 _ _ _ (@one_cat_family_to_cart_func B I C C1)
      (@one_cat_family_from_cart_func B I C C1))
    (@id_func (Functor_cart_cat B (Functor_cart_cat I C))))
≔ let A0 : Cat ≔ Functor_cat B (Functor_cat I C) in
  let A1 : Cat ≔ Functor_cart_cat B (Functor_cat I C) in
  let A2 : Cat ≔ Functor_cart_cat B (Functor_cart_cat I C) in
  let a : τ (Functor A0 A1) ≔ @one_cat_mapping_to_cart_func B (Functor_cat I C) (@one_cat_functor_category I C C1) in
  let b : τ (Functor A1 A2) ≔ @comp_cat_cov_cart_func B (Functor_cat I C) (Functor_cart_cat I C) (@one_cat_mapping_to_cart_func I C C1) in
  let c : τ (Functor A2 A1) ≔ @comp_cat_cov_cart_func B (Functor_cart_cat I C) (Functor_cat I C) (@one_cat_mapping_from_cart_func I C C1) in
  let d : τ (Functor A1 A0) ≔ @one_cat_mapping_from_cart_func B (Functor_cat I C) (@one_cat_functor_category I C C1) in
  @eq_trans (Functor A2 A2)
    (@comp_cat_fapp0 A2 A0 A2 (@comp_cat_fapp0 A0 A1 A2 b a) (@comp_cat_fapp0 A2 A1 A0 d c))
    (@comp_cat_fapp0 A2 A1 A2 (@comp_cat_fapp0 A1 A0 A2 (@comp_cat_fapp0 A0 A1 A2 b a) d) c)
    (@id_func A2)
    (@comp_assoc Cat_cat A2 A1 A0 A2 (@comp_cat_fapp0 A0 A1 A2 b a) d c)
    (@eq_ap (Functor A1 A2) (Functor A2 A2)
      (λ z : τ (Functor A1 A2), @comp_cat_fapp0 A2 A1 A2 z c)
      (@comp_cat_fapp0 A1 A0 A2 (@comp_cat_fapp0 A0 A1 A2 b a) d)
      (@comp_cat_fapp0 A1 A1 A2 b (@comp_cat_fapp0 A1 A0 A1 a d))
      (@eq_sym (Functor A1 A2) _ _ (@comp_assoc Cat_cat A1 A0 A1 A2 b a d)));

// Ordinary exchange is the existing Cartesian exchange between those actual
// presentations. No second exchange primitive or pointwise map assembly.
symbol one_cat_family_exchange_func [B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (Functor (Functor_cat B (Functor_cat I C))
    (Functor_cat I (Functor_cat B C)))
≔ @comp_cat_fapp0 (Functor_cat B (Functor_cat I C))
    (Functor_cart_cat I (Functor_cart_cat B C))
    (Functor_cat I (Functor_cat B C))
    (@one_cat_family_from_cart_func I B C C1)
    (@comp_cat_fapp0 (Functor_cat B (Functor_cat I C))
      (Functor_cart_cat B (Functor_cart_cat I C))
      (Functor_cart_cat I (Functor_cart_cat B C))
      (@sym_func_func B I C) (@one_cat_family_to_cart_func B I C C1));

// Readable rungs of that actual whole functor.
symbol one_cat_family_exchange [B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (F : τ (Functor B (Functor_cat I C)))
  : τ (Functor I (Functor_cat B C))
≔ fapp0 (@one_cat_family_exchange_func B I C C1) F;

symbol one_cat_family_exchange_map [B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B (Functor_cat I C))]
  (h : τ (@Transf B (Functor_cat I C) F G))
  : τ (@Transf I (Functor_cat B C)
    (@one_cat_family_exchange B I C C1 F) (@one_cat_family_exchange B I C C1 G))
≔ @fapp1_fapp0 _ _ (@one_cat_family_exchange_func B I C C1) F G h;

symbol one_cat_family_exchange_at_func [B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (F : τ (Functor B (Functor_cat I C))) (i : τ (Obj I))
  : τ (Functor B C)
≔ fapp0 (@one_cat_family_exchange B I C C1 F) i;

symbol one_cat_family_exchange_map_at [B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B (Functor_cat I C))]
  (h : τ (@Transf B (Functor_cat I C) F G)) (i : τ (Obj I))
  : τ (@Transf B C (@one_cat_family_exchange_at_func B I C C1 F i)
    (@one_cat_family_exchange_at_func B I C C1 G i))
≔ @tapp0_fapp0 I (Functor_cat B C)
    (@one_cat_family_exchange B I C C1 F) (@one_cat_family_exchange B I C C1 G) i
    (@one_cat_family_exchange_map B I C C1 F G h);

// Ordinary observation of the two actual admissions. Compare them in order
// and apply existing component evaluation; do not expand strictness evidence
// or erase the strict-action view in runtime. This is a derived path, not a
// new operational argument or a pointwise definition of the whole exchange.
symbol one_cat_family_exchange_component_path [B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B (Functor_cat I C))]
  (h : τ (@Transf B (Functor_cat I C) F G)) (b : τ (Obj B)) (i : τ (Obj I))
  : τ (@= (Hom C (fapp0 (fapp0 F b) i) (fapp0 (fapp0 G b) i))
    (@tapp0_fapp0 B C _ _ b (@one_cat_family_exchange_map_at B I C C1 F G h i))
    (@tapp0_fapp0 I C (fapp0 F b) (fapp0 G b) i
      (@tapp0_fapp0 B (Functor_cat I C) F G b h)))
≔ let M : Cat ≔ Functor_cat I C in
  let h_adm : τ (@Transf B M F G) ≔ @strict_transfor B M F G
    (@fapp1_fapp0 _ _ (@one_cat_mapping_to_cart_func B M
      (@one_cat_functor_category I C C1)) F G h) in
  let outer : τ (@= (@Transf B M F G) h_adm h) ≔ @eq_refl (@Transf B M F G) h_adm in
  let Fb : τ (Functor I C) ≔ fapp0 F b in
  let Gb : τ (Functor I C) ≔ fapp0 G b in
  let hb_adm : τ (@Transf I C Fb Gb) ≔ @tapp0_fapp0 B M F G b h_adm in
  let hb : τ (@Transf I C Fb Gb) ≔ @tapp0_fapp0 B M F G b h in
  let inner_view : τ (@Transf I C Fb Gb) ≔ @strict_transfor I C Fb Gb
    (@fapp1_fapp0 _ _ (@one_cat_mapping_to_cart_func I C C1) Fb Gb hb_adm) in
  let inner : τ (@= (@Transf I C Fb Gb) inner_view hb_adm) ≔
    @eq_refl (@Transf I C Fb Gb) inner_view in
  @eq_ap (@Transf I C Fb Gb) (Hom C (fapp0 Fb i) (fapp0 Gb i))
    (λ eta : τ (@Transf I C Fb Gb), @tapp0_fapp0 I C Fb Gb i eta)
    inner_view hb
    (@eq_trans (@Transf I C Fb Gb) inner_view hb_adm hb inner
      (@eq_ap (@Transf B M F G) (@Transf I C Fb Gb)
        (λ eta : τ (@Transf B M F G), @tapp0_fapp0 B M F G b eta)
        h_adm h outer));

symbol one_cat_diagram_family_map_path [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B (Functor_cat WalkingArrow_cat C))]
  (h k : τ (@Transf B (Functor_cat WalkingArrow_cat C) F G))
  (p : τ (@= (@Transf B C
    (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 F walking_arrow_src)
    (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 G walking_arrow_src))
    (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 F G h walking_arrow_src)
    (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 F G k walking_arrow_src)))
  (q : τ (@= (@Transf B C
    (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 F walking_arrow_tgt)
    (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 G walking_arrow_tgt))
    (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 F G h walking_arrow_tgt)
    (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 F G k walking_arrow_tgt)))
  : τ (@= (@Transf B (Functor_cat WalkingArrow_cat C) F G) h k)
≔ let I : Cat ≔ WalkingArrow_cat in
  let X : Cat ≔ Functor_cat B (Functor_cat I C) in
  let Y : Cat ≔ Functor_cart_cat B (Functor_cart_cat I C) in
  let Z : Cat ≔ Functor_cart_cat I (Functor_cart_cat B C) in
  let W : Cat ≔ Functor_cat I (Functor_cat B C) in
  let L : τ (Functor X Y) ≔ @one_cat_family_to_cart_func B I C C1 in
  let R : τ (Functor Z W) ≔ @one_cat_family_from_cart_func I B C C1 in
  let LF : τ (Obj Y) ≔ fapp0 L F in
  let LG : τ (Obj Y) ≔ fapp0 L G in
  let SF : τ (Obj Z) ≔ @sym_func B I C LF in
  let SG : τ (Obj Z) ≔ @sym_func B I C LG in
  let Lh : τ (Hom Y LF LG) ≔ @fapp1_fapp0 X Y L F G h in
  let Lk : τ (Hom Y LF LG) ≔ @fapp1_fapp0 X Y L F G k in
  let Sh : τ (Hom Z SF SG) ≔ @sym_func_func_transf B I C LF LG Lh in
  let Sk : τ (Hom Z SF SG) ≔ @sym_func_func_transf B I C LF LG Lk in
  let observed : τ (@= (Hom W (fapp0 R SF) (fapp0 R SG))
      (@fapp1_fapp0 Z W R SF SG Sh) (@fapp1_fapp0 Z W R SF SG Sk)) ≔
    @one_cat_diagram_map_path (Functor_cat B C) (@one_cat_functor_category B C C1)
      (@one_cat_family_exchange B I C C1 F) (@one_cat_family_exchange B I C C1 G)
      (@one_cat_family_exchange_map B I C C1 F G h)
      (@one_cat_family_exchange_map B I C C1 F G k) p q in
  let exchanged : τ (@= (Hom Z SF SG) Sh Sk) ≔
    @functor_left_inverse_reflect_path Z W R
      (@one_cat_family_to_cart_func I B C C1)
      (@one_cat_family_to_from_path I B C C1) SF SG Sh Sk observed in
  let admitted_path : τ (@= (Hom Y LF LG) Lh Lk) ≔
    @eq_ap (Hom Z SF SG) (Hom Y LF LG)
      (λ alpha : τ (Hom Z SF SG), @sym_func_func_transf I B C SF SG alpha)
      Sh Sk exchanged in
  @functor_left_inverse_reflect_path X Y L
    (@one_cat_family_from_cart_func B I C C1)
    (@one_cat_family_from_to_path B I C C1) F G h k admitted_path;

// Ordinary-target version of the same walking-diagram family. The general
// transf_arrow_diagram_func keeps its oplax target; this existing OneCat
// consumer uses the actual ordinary exchange instead of equating profiles.
symbol one_cat_transf_arrow_diagram_func [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B C)] (eta : τ (@Transf B C F G))
  : τ (Functor B (Functor_cat WalkingArrow_cat C))
≔ @one_cat_family_exchange WalkingArrow_cat B C C1
    (@walking_arrow_func (Functor_cat B C) F G eta);

// Ordinary-target family observations through the already-qualified whole
// exchange. The general fixed evaluator and oplax shape evaluator retain
// their separate interfaces; no ordinary/oplax classifier equality is used.
require open emdash.emdash3_2_one_cat_action_paths;

symbol one_cat_diagram_family_evaluation_func [K I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (i : τ (Obj I))
  : τ (Functor (Functor_cat K (Functor_cat I C)) (Functor_cat K C))
≔ @comp_cat_fapp0 (Functor_cat K (Functor_cat I C))
    (Functor_cat I (Functor_cat K C)) (Functor_cat K C)
    (@fapp0_func I (Functor_cat K C) i)
    (@one_cat_family_exchange_func K I C C1);

// The shape arrow acts in the whole ordinary exchanged diagram, so K and
// every higher action remain internal. No naturality cell is supplied.
symbol one_cat_diagram_family_transf [K I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor K (Functor_cat I C)))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (@Transf K C
    (@one_cat_family_exchange_at_func K I C C1 D i)
    (@one_cat_family_exchange_at_func K I C C1 D j))
≔ @fapp1_fapp0 I (Functor_cat K C)
    (@one_cat_family_exchange K I C C1 D) i j u;

// The original whole endpoint-composition observation at this ordinary
// presentation. It uses the existing strict action of its evaluator.
symbol one_cat_diagram_family_exchange_comp_path [B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (i : τ (Obj I))
  (F G H : τ (Functor B (Functor_cat I C)))
  (g : τ (@Transf B (Functor_cat I C) G H))
  (f : τ (@Transf B (Functor_cat I C) F G))
  : τ (@= (@Transf B C
      (@one_cat_family_exchange_at_func B I C C1 F i)
      (@one_cat_family_exchange_at_func B I C C1 H i))
    (@one_cat_family_exchange_map_at B I C C1 F H
      (@comp_fapp0 (Functor_cat B (Functor_cat I C)) F G H g f) i)
    (@comp_fapp0 (Functor_cat B C)
      (@one_cat_family_exchange_at_func B I C C1 F i)
      (@one_cat_family_exchange_at_func B I C C1 G i)
      (@one_cat_family_exchange_at_func B I C C1 H i)
      (@one_cat_family_exchange_map_at B I C C1 G H g i)
      (@one_cat_family_exchange_map_at B I C C1 F G f i)))
≔ @one_cat_composition_path (Functor_cat B (Functor_cat I C))
    (Functor_cat B C) (@one_cat_functor_category B C C1)
    (@one_cat_diagram_family_evaluation_func B I C C1 i) F G H g f;

// Ordinary-target whole exchange into the native oplax diagram profile.
// Reuse the same two Cartesian admissions and symmetry as ordinary exchange,
// then apply the actual Cartesian-to-oplax inclusion. No profile equality.
symbol one_cat_family_oplax_exchange_func [A B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (Functor (Functor_cat A (Functor_cat B C))
      (Functor_cat B (Functor_oplax_cat A C)))
≔ @comp_cat_fapp0 (Functor_cat A (Functor_cat B C))
    (Functor_cart_cat B (Functor_oplax_cat A C))
    (Functor_cat B (Functor_oplax_cat A C))
    (Functor_cart_include B (Functor_oplax_cat A C))
    (@comp_cat_fapp0 (Functor_cat A (Functor_cat B C))
      (Functor_cart_cat B (Functor_cart_cat A C))
      (Functor_cart_cat B (Functor_oplax_cat A C))
      (@comp_cat_cov_cart_func B (Functor_cart_cat A C) (Functor_oplax_cat A C)
        (Functor_cart_oplax_include A C))
      (@comp_cat_fapp0 (Functor_cat A (Functor_cat B C))
        (Functor_cart_cat A (Functor_cart_cat B C))
        (Functor_cart_cat B (Functor_cart_cat A C))
        (@sym_func_func A B C) (@one_cat_family_to_cart_func A B C C1)));

symbol one_cat_family_oplax_exchange_map [A B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor A (Functor_cat B C))]
  (eta : τ (@Transf A (Functor_cat B C) F G))
  : τ (@Transf B (Functor_oplax_cat A C)
      (@diagram_family_shape_func A B C F) (@diagram_family_shape_func A B C G))
≔ @fapp1_fapp0 _ _ (@one_cat_family_oplax_exchange_func A B C C1) F G eta;

// Whole component after canonical ordinary-target admission and exchange.
// U may be an already classified square or a newly admitted ordinary map.
// Preserve its strict view until actual component projection; do not erase
// an arbitrary strict view to its raw underlying transformation.
// J,D are the evaluator's encoded parameters. Matching them directly also
// covers A,C that are already dualized; no inverse dual-pattern matching.
// lhs-audit: keep 1,5,6 -- ambient composition and paired fixed evaluators.
// Nested SR guards: retain the Cartesian source/native oplax target of
// postcomposition and the Cat_cat classifier of the actual DefIso admission.
rule @comp_prod_fapp1_fapp0 Cat_cat $B _ $C
    (Struct_sigma _ (@OddDual_func _ _ (@fapp0_func $J $D $a)))
    (Struct_sigma _ (@OddDual_func _ _ (@fapp0_func $J $D $a)))
    (Struct_sigma
      (@strict_transfor _ _ _ _
        (@hom_postcomp_fapp1_fapp0 Cat_cart Cat_cart (@id Cat_cat Cat_cart)
          $B (Functor_cart_cat $A $C) (OddDual_cat (Functor_cat $J $D))
          (@comp_fapp0 Cat_cat (Functor_cart_cat $A $C) _
            (OddDual_cat (Functor_cat $J $D))
            (@OddDual_func _ _ (Functor_cart_include $J $D))
            (@OddDual_func _ _ (OddDual_cart_func_func $A $C))) _ _
          (@sym_func_func_transf $A $B $C _ _
            (@hom_postcomp_fapp1_fapp0 Cat_cart Cat_cart (@id Cat_cat Cat_cart)
              $A (Functor_cat $B $C) (Functor_cart_cat $B $C)
              (@defiso_to Cat_cat (Functor_cat $B $C) (Functor_cart_cat $B $C)
                (@one_cat_mapping_comparison $B $C _)) $F $G $U))))
      (@id _ (@OddDual_func _ _ (@fapp0_func $J $D $a))))
  ↪ @tapp0_fapp0 $A (Functor_cat $B $C) $F $G $a
      (@strict_transfor $A (Functor_cat $B $C) $F $G $U);

// Direct proof-time reading of the admitted/native round trip. The existing
// exchange comparison and the native double-exchange projection do not
// chain once the latter side has already reduced to the original family.
// Keep the actual OneCat admission and the entire family D in this join.
unif_rule @comp_fapp0 Cat_cat _ _ _
    (@comp_fapp0 Cat_cat _ _ _
      (@OddDual_func _ _ (Functor_cart_include (OddDual_cat $I) (OddDual_cat $C)))
      (@OddDual_func _ _ (OddDual_cart_func_func $I $C)))
    (@sym_func $I $B $C
      (@comp_fapp0 Cat_cat _ _ _
        (@comp_fapp0 Cat_cat _ _ _
          (@defiso_to _ _ _ (@one_cat_mapping_comparison $B $C _))
          (@hom_precomp_along_func Cat_cat Cat_cat (@id Cat_cat Cat_cat) $C $B _ $D))
        (@OddDual_func _ _ (@diagram_evaluation_func (OddDual_cat $I) (OddDual_cat $C)))))
  ≡ $H
  ↪ [ $H ≡ $D ];

require open emdash.emdash3_2_one_cat_modifications;
// Ordinary target: the existing modification introduction assembles the
// already-computing components, and discreteness reflects it to a path.
symbol one_cat_oplax_exchange_at_path [A B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (F G : τ (Functor A (Functor_cat B C)))
  (eta : τ (@Transf A (Functor_cat B C) F G)) (a : τ (Obj A))
  : τ (@= (@Transf B C (fapp0 F a) (fapp0 G a))
      (@diagram_oplax_family_map_at B A C
        (@diagram_family_shape_func A B C F) (@diagram_family_shape_func A B C G)
        (@one_cat_family_oplax_exchange_map A B C C1 F G eta) a)
      (@tapp0_fapp0 A (Functor_cat B C) F G a eta))
≔ let X : τ (Functor B C) ≔ fapp0 F a in
  let Y : τ (Functor B C) ≔ fapp0 G a in
  let alpha : τ (@Transf B C X Y) ≔ @diagram_oplax_family_map_at B A C
      (@diagram_family_shape_func A B C F) (@diagram_family_shape_func A B C G)
      (@one_cat_family_oplax_exchange_map A B C C1 F G eta) a in
  let beta : τ (@Transf B C X Y) ≔ @tapp0_fapp0 A (Functor_cat B C) F G a eta in
  @hom_to_path (@Transf_cat B C X Y) ((@one_cat_functor_category B C C1) X Y)
    alpha beta (@one_cat_modification B C C1 X Y alpha beta
      (λ b : τ (Obj B), @path_to_hom (Hom_cat C (fapp0 X b) (fapp0 Y b))
        (@tapp0_fapp0 B C X Y b alpha) (@tapp0_fapp0 B C X Y b beta)
        (@eq_refl (Hom C (fapp0 X b) (fapp0 Y b)) (@tapp0_fapp0 B C X Y b beta))));

// Composition observation with the original endpoint maps. These are paths
// between already-formed whole transformations, never operational inputs.
symbol one_cat_oplax_exchange_comp_at_path [A B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (a : τ (Obj A))
  (F G H : τ (Functor A (Functor_cat B C)))
  (V : τ (@Transf A (Functor_cat B C) G H))
  (U : τ (@Transf A (Functor_cat B C) F G))
  : τ (@= (@Transf B C (fapp0 F a) (fapp0 H a))
      (@diagram_oplax_family_map_at B A C
        (@diagram_family_shape_func A B C F) (@diagram_family_shape_func A B C H)
        (@comp_fapp0 (Functor_cat B (Functor_oplax_cat A C))
          (@diagram_family_shape_func A B C F) (@diagram_family_shape_func A B C G)
          (@diagram_family_shape_func A B C H)
          (@one_cat_family_oplax_exchange_map A B C C1 G H V)
          (@one_cat_family_oplax_exchange_map A B C C1 F G U)) a)
      (@comp_fapp0 (Functor_cat B C) (fapp0 F a) (fapp0 G a) (fapp0 H a)
        (@tapp0_fapp0 A (Functor_cat B C) G H a V)
        (@tapp0_fapp0 A (Functor_cat B C) F G a U)))
≔ let X : τ (Functor B C) ≔ fapp0 F a in
  let Y : τ (Functor B C) ≔ fapp0 G a in
  let Z : τ (Functor B C) ≔ fapp0 H a in
  let EF : τ (Functor B (Functor_oplax_cat A C)) ≔ @diagram_family_shape_func A B C F in
  let EG : τ (Functor B (Functor_oplax_cat A C)) ≔ @diagram_family_shape_func A B C G in
  let EH : τ (Functor B (Functor_oplax_cat A C)) ≔ @diagram_family_shape_func A B C H in
  let EU : τ (@Transf B (Functor_oplax_cat A C) EF EG) ≔ @one_cat_family_oplax_exchange_map A B C C1 F G U in
  let EV : τ (@Transf B (Functor_oplax_cat A C) EG EH) ≔ @one_cat_family_oplax_exchange_map A B C C1 G H V in
  let u : τ (@Transf B C X Y) ≔ @diagram_oplax_family_map_at B A C EF EG EU a in
  let v : τ (@Transf B C Y Z) ≔ @diagram_oplax_family_map_at B A C EG EH EV a in
  let u0 : τ (@Transf B C X Y) ≔ @tapp0_fapp0 A (Functor_cat B C) F G a U in
  let v0 : τ (@Transf B C Y Z) ≔ @tapp0_fapp0 A (Functor_cat B C) G H a V in
  @eq_trans (@Transf B C X Z) _ (@comp_fapp0 (Functor_cat B C) X Y Z v u) _
    (@one_cat_oplax_family_evaluation_comp_path B A C C1 a EF EG EH EV EU)
    (@eq_trans (@Transf B C X Z) _ (@comp_fapp0 (Functor_cat B C) X Y Z v0 u) _
      (@eq_ap (@Transf B C Y Z) (@Transf B C X Z)
        (λ w : τ (@Transf B C Y Z), @comp_fapp0 (Functor_cat B C) X Y Z w u)
        v v0 (@one_cat_oplax_exchange_at_path A B C C1 G H V a))
      (@eq_ap (@Transf B C X Y) (@Transf B C X Z)
        (λ w : τ (@Transf B C X Y), @comp_fapp0 (Functor_cat B C) X Y Z v0 w)
        u u0 (@one_cat_oplax_exchange_at_path A B C C1 F G U a)));

// Shared ordinary-target views consumed by native input comparisons.
// Existing Cartesian exchange, after the actual OneCat admission of evaluation.
symbol one_cat_oplax_family_cart_func [K I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor K (Functor_oplax_cat I C)))
  : τ (Functor K (Functor_cart_cat I C))
≔ @sym_func I K C
    (@comp_cat_fapp0 I (Functor_cat K C) (Functor_cart_cat K C)
      (@one_cat_mapping_to_cart_func K C C1)
      (@diagram_oplax_family_shape_func K I C D));

// This is the existing native exchange comparison, used before specialization.
symbol one_cat_oplax_family_roundtrip [K I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor K (Functor_oplax_cat I C)))
  : τ (@= (Functor K (Functor_oplax_cat I C))
      (@comp_cat_fapp0 K (Functor_cart_cat I C) (Functor_oplax_cat I C)
        (Functor_cart_oplax_include I C) (@one_cat_oplax_family_cart_func K I C C1 D)) D)
≔ @eq_refl (Functor K (Functor_oplax_cat I C))
    (@comp_cat_fapp0 K (Functor_cart_cat I C) (Functor_oplax_cat I C)
      (Functor_cart_oplax_include I C) (@one_cat_oplax_family_cart_func K I C C1 D));


// Reflection through the existing Cartesian and ordinary whole comparisons.
symbol one_cat_oplax_diagram_map_path [C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [d e : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))]
  (h k : τ (Hom (Functor_oplax_cat WalkingArrow_cat C) d e))
  (p : τ (@= (Hom C
    (@fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)
    (@fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) e))
    (@fapp1_fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d e h)
    (@fapp1_fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d e k)))
  (q : τ (@= (Hom C
    (@fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)
    (@fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) e))
    (@fapp1_fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d e h)
    (@fapp1_fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d e k)))
  : τ (@= (Hom (Functor_oplax_cat WalkingArrow_cat C) d e) h k)
≔ let I : Cat ≔ WalkingArrow_cat in
  let B : Cat ≔ Functor_oplax_cat I C in
  let V : Cat ≔ Functor_cart_cat I C in
  let W : Cat ≔ Functor_cat I C in
  let Q : τ (Functor B V) ≔ @one_cat_oplax_family_cart_func B I C C1 (@id_func B) in
  let R : τ (Functor V B) ≔ Functor_cart_oplax_include I C in
  let U : τ (Functor V W) ≔ @one_cat_mapping_from_cart_func I C C1 in
  let L : τ (Functor W V) ≔ @one_cat_mapping_to_cart_func I C C1 in
  let Qd : τ (Obj V) ≔ fapp0 Q d in
  let Qe : τ (Obj V) ≔ fapp0 Q e in
  let Qh : τ (Hom V Qd Qe) ≔ @fapp1_fapp0 B V Q d e h in
  let Qk : τ (Hom V Qd Qe) ≔ @fapp1_fapp0 B V Q d e k in
  let ordinary : τ (@= (Hom W (fapp0 U Qd) (fapp0 U Qe))
      (@fapp1_fapp0 V W U Qd Qe Qh) (@fapp1_fapp0 V W U Qd Qe Qk)) ≔
    @one_cat_diagram_map_path C C1 Qd Qe
      (@fapp1_fapp0 V W U Qd Qe Qh) (@fapp1_fapp0 V W U Qd Qe Qk) p q in
  let cart : τ (@= (Hom V Qd Qe) Qh Qk) ≔
    @functor_left_inverse_reflect_path V W U L
      (@eq_refl (Functor V V) (@comp_cat_fapp0 V W V L U))
      Qd Qe Qh Qk ordinary in
  @functor_left_inverse_reflect_path B V Q R
    (@one_cat_oplax_family_roundtrip B I C C1 (@id_func B)) d e h k cart;

symbol one_cat_diagram_oplax_include_func [C : Cat]
            (C1 : τ (IsNCat (cat_succ cat_zero) C))
            : τ (Functor (Functor_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C))
    ≔ @comp_cat_fapp0 (Functor_cat WalkingArrow_cat C) (Functor_cart_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)
                    (Functor_cart_oplax_include WalkingArrow_cat C)
                    (@one_cat_mapping_to_cart_func WalkingArrow_cat C C1);

// Whole family reflection from the retained whole endpoint paths.
// The fixed-diagram reflection and ordinary-target modification introduction
// supply the actual whole cell; no pointwise replacement of the result.
symbol one_cat_oplax_diagram_family_map_path [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C))]
  (h k : τ (@Transf B (Functor_oplax_cat WalkingArrow_cat C) F G))
  (p : τ (@= (@Transf B C
    (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) F)
    (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) G))
    (@diagram_oplax_family_map_at B WalkingArrow_cat C F G h walking_arrow_src)
    (@diagram_oplax_family_map_at B WalkingArrow_cat C F G k walking_arrow_src)))
  (q : τ (@= (@Transf B C
    (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) F)
    (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) G))
    (@diagram_oplax_family_map_at B WalkingArrow_cat C F G h walking_arrow_tgt)
    (@diagram_oplax_family_map_at B WalkingArrow_cat C F G k walking_arrow_tgt)))
  : τ (@= (@Transf B (Functor_oplax_cat WalkingArrow_cat C) F G) h k)
≔ let M : Cat ≔ Functor_oplax_cat WalkingArrow_cat C in
  let M1 : τ (IsNCat (cat_succ cat_zero) M) ≔ @one_cat_oplax_functor_category WalkingArrow_cat C C1 in
  @hom_to_path (@Transf_cat B M F G) ((@one_cat_functor_category B M M1) F G) h k
    (@one_cat_modification B M M1 F G h k
      (λ b : τ (Obj B),
        @path_to_hom (Hom_cat M (@fapp0 B M F b) (@fapp0 B M G b))
          (@tapp0_fapp0 B M F G b h) (@tapp0_fapp0 B M F G b k)
          (@one_cat_oplax_diagram_map_path C C1 (@fapp0 B M F b) (@fapp0 B M G b)
            (@tapp0_fapp0 B M F G b h) (@tapp0_fapp0 B M F G b k)
            (@eq_ap _ _
              (λ e : τ (@Transf B C
                (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) F)
                (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) G)),
                @tapp0_fapp0 B C _ _ b e) _ _ p)
            (@eq_ap _ _
              (λ e : τ (@Transf B C
                (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) F)
                (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) G)),
                @tapp0_fapp0 B C _ _ b e) _ _ q))));
