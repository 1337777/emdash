/* The old interchange/EH derivations now expose actual action profiles.
   Core EH objects, operations and unit observations are unchanged. */
require open emdash.emdash3_2_profiled_vertical_paths;

symbol hom_postcomp_representable_interchange_eq
  [B : Cat]
  [M N L : τ (Obj B)]
  [f g h : τ (Hom B N L)]
  (e_fg : τ (Hom (Hom_cat B N L) f g))
  (e_gh : τ (Hom (Hom_cat B N L) g h))
  (PE : τ (@IsStrictTransfor (Hom_cat B M N) (Hom_cat B M L) (@hom_postcomp_func B B (@id_func B) M N L f) (@hom_postcomp_func B B (@id_func B) M N L g) (@hom_postcomp_tele_transf B B (@id_func B) M N L f g e_fg)))
  (PN : τ (@IsPreStrictTransfor (Hom_cat B M N) (Hom_cat B M L) (@hom_postcomp_func B B (@id_func B) M N L g) (@hom_postcomp_func B B (@id_func B) M N L h) (@hom_postcomp_tele_transf B B (@id_func B) M N L g h e_gh)))
  [X Y Z : τ (Hom B M N)]
  (alpha : τ (Hom (Hom_cat B M N) X Y))
  (beta : τ (Hom (Hom_cat B M N) Y Z))
  : τ (
      @comp_fapp0
        (Hom_cat B M L)
        (@hom_postcomp_fapp0 B B (@id_func B) M N L f X)
        (@hom_postcomp_fapp0 B B (@id_func B) M N L g Y)
        (@hom_postcomp_fapp0 B B (@id_func B) M N L h Z)
        (@tapp1_fapp0
          (Hom_cat B M N)
          (Hom_cat B M L)
          (@hom_postcomp_func B B (@id_func B) M N L g)
          (@hom_postcomp_func B B (@id_func B) M N L h)
          Y
          Z
          (@hom_postcomp_tele_transf B B (@id_func B) M N L g h e_gh)
          beta)
        (@tapp1_fapp0
          (Hom_cat B M N)
          (Hom_cat B M L)
          (@hom_postcomp_func B B (@id_func B) M N L f)
          (@hom_postcomp_func B B (@id_func B) M N L g)
          X
          Y
          (@hom_postcomp_tele_transf B B (@id_func B) M N L f g e_fg)
          alpha)
      =
      @tapp1_fapp0
        (Hom_cat B M N)
        (Hom_cat B M L)
        (@hom_postcomp_func B B (@id_func B) M N L f)
        (@hom_postcomp_func B B (@id_func B) M N L h)
        X
        Z
        (@hom_postcomp_tele_transf
          B
          B
          (@id_func B)
          M
          N
          L
          f
          h
          (@comp_fapp0 (Hom_cat B N L) f g h e_gh e_fg))
        (@comp_fapp0 (Hom_cat B M N) X Y Z beta alpha))
// Preserve the original profiled vertical proof. Its final telescope
// comparison is the strict functor law of the actual whole ambient view.
// Abstract that law before specializing, so no stable-head comparison rule
// is needed after the two projection orders expose different normal forms.
≔ let A : Cat ≔ Hom_cat B N L in
  let C : Cat ≔ Hom_cat B M N in
  let D : Cat ≔ Hom_cat B M L in
  let Hf : τ (Functor C D) ≔ @hom_postcomp_func B B (@id_func B) M N L f in
  let Hg : τ (Functor C D) ≔ @hom_postcomp_func B B (@id_func B) M N L g in
  let Hh : τ (Functor C D) ≔ @hom_postcomp_func B B (@id_func B) M N L h in
  let U : τ (@Transf C D Hf Hg) ≔ @hom_postcomp_tele_transf B B (@id_func B) M N L f g e_fg in
  let V : τ (@Transf C D Hg Hh) ≔ @hom_postcomp_tele_transf B B (@id_func B) M N L g h e_gh in
  let W : τ (@Transf C D Hf Hh) ≔ @hom_postcomp_tele_transf B B (@id_func B) M N L f h
    (@comp_fapp0 A f g h e_gh e_fg) in
  let law : Π (J : τ (Functor A (Functor_cat C D))),
    τ (@= (@Transf C D (@fapp0 A (Functor_cat C D) J f) (@fapp0 A (Functor_cat C D) J h))
      (@comp_fapp0 (Functor_cat C D)
        (@fapp0 A (Functor_cat C D) J f) (@fapp0 A (Functor_cat C D) J g) (@fapp0 A (Functor_cat C D) J h)
        (@fapp1_fapp0 A (Functor_cat C D) J g h e_gh)
        (@fapp1_fapp0 A (Functor_cat C D) J f g e_fg))
      (@fapp1_fapp0 A (Functor_cat C D) J f h (@comp_fapp0 A f g h e_gh e_fg)))
  ≔ λ J : τ (Functor A (Functor_cat C D)),
    @eq_refl (@Transf C D (@fapp0 A (Functor_cat C D) J f) (@fapp0 A (Functor_cat C D) J h))
      (@fapp1_fapp0 A (Functor_cat C D) J f h (@comp_fapp0 A f g h e_gh e_fg)) in
  @eq_trans (Hom D (@fapp0 C D Hf X) (@fapp0 C D Hh Z))
    (@comp_fapp0 D (@fapp0 C D Hf X) (@fapp0 C D Hg Y) (@fapp0 C D Hh Z)
      (@tapp1_fapp0 C D Hg Hh Y Z V beta) (@tapp1_fapp0 C D Hf Hg X Y U alpha))
    (@tapp1_fapp0 C D Hf Hh X Z (@comp_fapp0 (Functor_cat C D) Hf Hg Hh V U)
      (@comp_fapp0 C X Y Z beta alpha))
    (@tapp1_fapp0 C D Hf Hh X Z W (@comp_fapp0 C X Y Z beta alpha))
    (@profiled_vertical_both_raw_path C D Hf Hg Hh U V PE PN X Y Z alpha beta)
    (@eq_ap (@Transf C D Hf Hh) (Hom D (@fapp0 C D Hf X) (@fapp0 C D Hh Z))
      (λ theta : τ (@Transf C D Hf Hh), @tapp1_fapp0 C D Hf Hh X Z theta
        (@comp_fapp0 C X Y Z beta alpha))
      (@comp_fapp0 (Functor_cat C D) Hf Hg Hh V U) W
      (law (@comp_cat_fapp0 A (Functor_cart_cat C D) (Functor_cat C D)
        (Functor_cart_include C D) (@hom_postcomp_tele_func B B (@id_func B) M N L))));

symbol EH_vcomp_to_shared_middle
  [B : Cat]
  (x : τ (Obj B))
  (alpha beta : τ (Obj (@EH_2End B x)))
  (PB : τ (@IsStrictTransfor (Hom_cat B x x) (Hom_cat B x x) (@id_func (Hom_cat B x x)) (@id_func (Hom_cat B x x)) (@hom_postcomp_tele_transf B B (@id_func B) x x x (@id B x) (@id B x) beta)))
  : τ (
      @EH_vcomp B x beta alpha
      =
      @EH_hcomp B x beta alpha)
≔ @profiled_vertical_post_raw_path (Hom_cat B x x) (Hom_cat B x x) (@id_func (Hom_cat B x x)) (@id_func (Hom_cat B x x)) (@id_func (Hom_cat B x x)) (@id (Functor_cat (Hom_cat B x x) (Hom_cat B x x)) (@id_func (Hom_cat B x x))) (@hom_postcomp_tele_transf B B (@id_func B) x x x (@id B x) (@id B x) beta) (@strict_transfor_pre_evidence (Hom_cat B x x) (Hom_cat B x x) (@id_func (Hom_cat B x x)) (@id_func (Hom_cat B x x)) (@hom_postcomp_tele_transf B B (@id_func B) x x x (@id B x) (@id B x) beta) PB) (@id B x) (@id B x) alpha;

symbol EH_swapped_vcomp_to_shared_middle
  [B : Cat]
  (x : τ (Obj B))
  (alpha beta : τ (Obj (@EH_2End B x)))
  (PB : τ (@IsStrictTransfor (Hom_cat B x x) (Hom_cat B x x) (@id_func (Hom_cat B x x)) (@id_func (Hom_cat B x x)) (@hom_postcomp_tele_transf B B (@id_func B) x x x (@id B x) (@id B x) beta)))
  : τ (
      @EH_vcomp B x alpha beta
      =
      @EH_hcomp B x beta alpha)
≔ @profiled_vertical_pre_raw_path (Hom_cat B x x) (Hom_cat B x x) (@id_func (Hom_cat B x x)) (@id_func (Hom_cat B x x)) (@id_func (Hom_cat B x x)) (@hom_postcomp_tele_transf B B (@id_func B) x x x (@id B x) (@id B x) beta) (@id (Functor_cat (Hom_cat B x x) (Hom_cat B x x)) (@id_func (Hom_cat B x x))) PB (@id B x) (@id B x) alpha;

symbol EH_comm
  [B : Cat]
  (x : τ (Obj B))
  (alpha beta : τ (Obj (@EH_2End B x)))
  (PB : τ (@IsStrictTransfor (Hom_cat B x x) (Hom_cat B x x) (@id_func (Hom_cat B x x)) (@id_func (Hom_cat B x x)) (@hom_postcomp_tele_transf B B (@id_func B) x x x (@id B x) (@id B x) beta)))
  : τ (
      @EH_vcomp B x beta alpha
      =
      @EH_vcomp B x alpha beta)
≔ @eq_trans
    (Hom (Hom_cat B x x) (@id B x) (@id B x))
    (@EH_vcomp B x beta alpha)
    (@EH_hcomp B x beta alpha)
    (@EH_vcomp B x alpha beta)
    (@EH_vcomp_to_shared_middle B x alpha beta PB)
    (eq_sym (@EH_swapped_vcomp_to_shared_middle B x alpha beta PB));
