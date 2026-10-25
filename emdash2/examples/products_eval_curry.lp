/*
  Reviewer milestone: products, evaluation, curry, and uncurry.

  These checks show the Cartesian functional-programming layer: evaluation is a
  functor, fixed-point evaluation folds to object application, and curry/uncurry
  normalize through the generic hom-action owners.
*/

require open emdash.emdash3_2;

assert [A B : Cat] (F : τ (Functor A B)) (x : τ (Obj A)) ⊢
  fapp0 (@Eval_func A B) (Struct_sigma F x)
    ≡ fapp0 F x;

assert [A B : Cat] (x : τ (Obj A)) ⊢
  @comp_cat_fapp0
    (Functor_cart_cat A B)
    (Product_cat (Functor_cart_cat A B) A)
    B
    (@Eval_func A B)
    (@Eval_at_func A B x)
  ≡ @comp_cat_fapp0 (Functor_cart_cat A B) (Functor_cat A B) B
      (@fapp0_func A B x) (Functor_cart_include A B);

assert [A B C : Cat]
  (F : τ (Functor (Product_cat A B) C))
  (x : τ (Obj A))
  (y : τ (Obj B)) ⊢
  @fapp0 B C
    (@fapp0 A (Functor_cart_cat B C) (@curry_func A B C F) x)
    y
    ≡ @fapp0 B C
        (@fapp0
          A
          (Functor_cart_cat B C)
          (@hom_precomp_along_fapp0
            Cat_cart
            Cat_cart
            (@id Cat_cart Cat_cart)
            (Functor_cart_cat B C)
            A
            (Product_cat (Functor_cart_cat B A) (Functor_cart_cat B B))
            (@Product_pair_tele_func A B)
            (@hom_postcomp_func
              Cat_cart
              Cat_cart
              (@id Cat_cart Cat_cart)
              B
              (Product_cat A B)
              C
              F))
          x)
        y;

assert [A B C : Cat]
  (G : τ (Functor A (Functor_cart_cat B C)))
  (x : τ (Obj A))
  (y : τ (Obj B)) ⊢
  fapp0 (uncurry_func G) (Struct_sigma x y)
    ≡ @fapp0
        (Product_cat A B)
        C
        (@hom_postcomp_fapp0
          Cat_cart
          Cat_cart
          (@id Cat_cart Cat_cart)
          (Product_cat A B)
          (Product_cat (Functor_cart_cat B C) B)
          C
          (@Eval_func B C)
          (@Product_cat_fapp1_tapp0_func A (Functor_cart_cat B C) B G))
        (Struct_sigma x y);
