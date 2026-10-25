require open emdash.emdash3_2;
// catalog-area: Native Hom profunctor curry comparisons
// Native Cartesian curry and Hom are compared before their ordinary inclusions.

assert [A B X : Cat] (F : τ (Functor A X)) (G : τ (Functor B X)) ⊢
 @eq_refl (Functor (Op_cat A) (Functor_cart_cat B Cat_cart))
   (@curry_func (Op_cat A) B Cat_cart (@Hom_prof_along A B X F G))
 : τ (@= (Functor (Op_cat A) (Functor_cart_cat B Cat_cart))
   (@curry_func (Op_cat A) B Cat_cart (@Hom_prof_along A B X F G))
   (@comp_cat_fapp0 (Op_cat A) (Op_cat X) (Functor_cart_cat B Cat_cart) (@hom_int X B G) (@Op_func A X F)));

assert [A B : Cat] (G : τ (Functor B A)) ⊢
 @eq_refl (Functor (Op_cat A) (Functor_cart_cat B Cat_cart))
   (@curry_func (Op_cat A) B Cat_cart (@Hom_prof_along A B A (@id_func A) G))
 : τ (@= (Functor (Op_cat A) (Functor_cart_cat B Cat_cart))
   (@curry_func (Op_cat A) B Cat_cart (@Hom_prof_along A B A (@id_func A) G))
   (@hom_int A B G));

assert [A : Cat] ⊢
 @eq_refl (Functor (Op_cat A) (Functor_cart_cat A Cat_cart))
   (@curry_func (Op_cat A) A Cat_cart (@Unit_prof A))
 : τ (@= (Functor (Op_cat A) (Functor_cart_cat A Cat_cart))
   (@curry_func (Op_cat A) A Cat_cart (@Unit_prof A)) (@hom_int A A (@id_func A)));

assertnot [A B X : Cat] (F : τ (Functor A X)) (G : τ (Functor B X)) (R : τ (Prof A B)) ⊢
 @eq_refl (Functor (Op_cat A) (Functor_cart_cat B Cat_cart))
   (@curry_func (Op_cat A) B Cat_cart R)
 : τ (@= (Functor (Op_cat A) (Functor_cart_cat B Cat_cart))
   (@curry_func (Op_cat A) B Cat_cart R)
   (@comp_cat_fapp0 (Op_cat A) (Op_cat X) (Functor_cart_cat B Cat_cart) (@hom_int X B G) (@Op_func A X F)));

assertnot [A B X : Cat] (F : τ (Functor A X)) (G : τ (Functor B X)) ⊢
 @curry_func (Op_cat A) B Cat_cart (@Hom_prof_along A B X F G)
 ≡ @comp_cat_fapp0 (Op_cat A) (Op_cat X) (Functor_cart_cat B Cat_cart) (@hom_int X B G) (@Op_func A X F);
