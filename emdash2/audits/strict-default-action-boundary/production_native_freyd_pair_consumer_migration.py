"""Source-pinned original native pair and Freyd exactness consumers.

Preserve supplied model/normality and actual inverse data. Existing
canonical constant inclusions change presentation, not transformation laws.
"""
import hashlib
import re
from production_diagram_observation_migration import _atom

SOURCES = {'emdash3_2_commutative_algebra_freyd_adjunction_model_normality.lp': {'ambientConstantFunctor': 0,
                                                                       'ambientConstantTransf': 0,
                                                                       'freydComponent': 0,
                                                                       'freydDiagramCategory': 0,
                                                                       'initialOp': 0,
                                                                       'sha256': '48f3615989455aa11ce4dfe7a1776ee98f60f4717bcbecd47cfe4f967b22ee14'},
 'emdash3_2_commutative_algebra_freyd_arrow_equivalence_observations.lp': {'ambientConstantFunctor': 0,
                                                                           'ambientConstantTransf': 0,
                                                                           'freydComponent': 0,
                                                                           'freydDiagramCategory': 0,
                                                                           'initialOp': 0,
                                                                           'sha256': 'df829b9f4f3256edfa2f8f998e7946d17a5c5f54775d4866787b88044379dd25'},
 'emdash3_2_commutative_algebra_freyd_arrow_observations.lp': {'ambientConstantFunctor': 0,
                                                               'ambientConstantTransf': 0,
                                                               'freydComponent': 0,
                                                               'freydDiagramCategory': 0,
                                                               'initialOp': 0,
                                                               'sha256': 'fdc135daf004871a02bf72018970abafb70b23a211825adc7624bfc1332f9697'},
 'emdash3_2_commutative_algebra_freyd_diagram_observations.lp': {'ambientConstantFunctor': 0,
                                                                 'ambientConstantTransf': 0,
                                                                 'freydComponent': 0,
                                                                 'freydDiagramCategory': 0,
                                                                 'initialOp': 0,
                                                                 'sha256': '1d114539788d3dd6dee2c6ff836e1ee1350b5638dfb8919ad5bf393fb67b2cd5'},
 'emdash3_2_commutative_algebra_freyd_native_snake_diagram_exactness.lp': {'ambientConstantFunctor': 0,
                                                                           'ambientConstantTransf': 0,
                                                                           'freydComponent': 0,
                                                                           'freydDiagramCategory': 0,
                                                                           'initialOp': 0,
                                                                           'sha256': 'a68825eb275640eaacec0d8635d0c9658ea136d5179895709931cfbd4cdb06e4'},
 'emdash3_2_commutative_algebra_freyd_native_snake_exactness.lp': {'ambientConstantFunctor': 0,
                                                                   'ambientConstantTransf': 16,
                                                                   'freydComponent': 0,
                                                                   'freydDiagramCategory': 0,
                                                                   'initialOp': 0,
                                                                   'sha256': 'fdd20b2c65e2b3a8c99e4769c0afa48d78fec883703a8a7fbc984aacf4518c1b'},
 'emdash3_2_commutative_algebra_freyd_native_snake_inputs.lp': {'ambientConstantFunctor': 0,
                                                                'ambientConstantTransf': 5,
                                                                'freydComponent': 0,
                                                                'freydDiagramCategory': 0,
                                                                'initialOp': 2,
                                                                'sha256': 'a17430251bc1795fb91aa1b12accf04895409198c3acb953e5a0eaca1047f8f6'},
 'emdash3_2_commutative_algebra_freyd_native_snake_maps.lp': {'ambientConstantFunctor': 0,
                                                              'ambientConstantTransf': 10,
                                                              'freydComponent': 0,
                                                              'freydDiagramCategory': 0,
                                                              'initialOp': 0,
                                                              'sha256': 'd4d8020ecff38f76acecabaea68611f0e72f09492e80de1452ccc0f83be3915f'},
 'emdash3_2_commutative_algebra_freyd_native_snake_observations.lp': {'ambientConstantFunctor': 0,
                                                                      'ambientConstantTransf': 0,
                                                                      'freydComponent': 0,
                                                                      'freydDiagramCategory': 0,
                                                                      'initialOp': 0,
                                                                      'sha256': '74e163df00fa5b5e03060a30b553e4f61741497546cada4f8a952135d7ec1d03'},
 'emdash3_2_commutative_algebra_freyd_native_snake_pair_exactness.lp': {'ambientConstantFunctor': 0,
                                                                        'ambientConstantTransf': 0,
                                                                        'freydComponent': 0,
                                                                        'freydDiagramCategory': 0,
                                                                        'initialOp': 0,
                                                                        'sha256': '19bea35b1ef7c44c699dd5950af2982e24734d7df6ddb0aa3c81a12534cde0b8'},
 'emdash3_2_commutative_algebra_freyd_native_snake_pairs.lp': {'ambientConstantFunctor': 0,
                                                               'ambientConstantTransf': 413,
                                                               'freydComponent': 0,
                                                               'freydDiagramCategory': 0,
                                                               'initialOp': 0,
                                                               'sha256': '14f4cadfab137f894758780a798035c4de562fc6e14d60074df36eb11f076be2'},
 'emdash3_2_commutative_algebra_freyd_native_snake_point_exactness.lp': {'ambientConstantFunctor': 0,
                                                                         'ambientConstantTransf': 0,
                                                                         'freydComponent': 0,
                                                                         'freydDiagramCategory': 0,
                                                                         'initialOp': 0,
                                                                         'sha256': '9648a8801fbebcfca652e1994d0a23d98b3e62f4b56f6ca7a4830924da9eebb3'},
 'emdash3_2_commutative_algebra_freyd_observation_coherence.lp': {'ambientConstantFunctor': 0,
                                                                  'ambientConstantTransf': 0,
                                                                  'freydComponent': 0,
                                                                  'freydDiagramCategory': 0,
                                                                  'initialOp': 0,
                                                                  'sha256': '8fe528e0782ed1ae0709158a0836d3d86e110e46ae2e4fd2f1dcec1a45222ee8'},
 'emdash3_2_finite_arrow_tail_arrows.lp': {'ambientConstantFunctor': 0,
                                           'ambientConstantTransf': 0,
                                           'freydComponent': 0,
                                           'freydDiagramCategory': 0,
                                           'initialOp': 0,
                                           'sha256': '0edc8c681c636d79217f5ac7ad4882513dfc0b96cb6ac8850f049bfe513ce52e'},
 'emdash3_2_finite_family_paths.lp': {'ambientConstantFunctor': 0,
                                      'ambientConstantTransf': 0,
                                      'freydComponent': 0,
                                      'freydDiagramCategory': 0,
                                      'initialOp': 0,
                                      'sha256': '0c04b76eec3ae670f549ecf30b587aacd5a28b1ab3ecfc20f518c82584638372'},
 'emdash3_2_one_cat_constant_snake_inputs.lp': {'ambientConstantFunctor': 1,
                                                'ambientConstantTransf': 15,
                                                'freydComponent': 0,
                                                'freydDiagramCategory': 0,
                                                'initialOp': 3,
                                                'sha256': '63e09a560744c0e0feb697b7152ef6139dea5da4efc0826e0b472f72480cc9d5'},
 'emdash3_2_one_cat_native_snake_first_pair_path.lp': {'ambientConstantFunctor': 0,
                                                       'ambientConstantTransf': 0,
                                                       'freydComponent': 0,
                                                       'freydDiagramCategory': 0,
                                                       'initialOp': 1,
                                                       'sha256': '1b90b50e316b91ec797891d47260c444e5a44991935ed17c8c23c9aac369227a'},
 'emdash3_2_one_cat_native_snake_other_pair_paths.lp': {'ambientConstantFunctor': 0,
                                                        'ambientConstantTransf': 0,
                                                        'freydComponent': 0,
                                                        'freydDiagramCategory': 0,
                                                        'initialOp': 3,
                                                        'sha256': '20f44827e6cc454b15938cf74264f47ccfd1e66e89a6fbd691a8f63f1e024229'},
 'examples/freyd_native_snake_exactness.lp': {'ambientConstantFunctor': 0,
                                              'ambientConstantTransf': 0,
                                              'freydComponent': 0,
                                              'freydDiagramCategory': 0,
                                              'initialOp': 0,
                                              'sha256': '5b91c31736cbfc30f5ea0db5fdb0238d0c92f81d651b34781cfe1922c78df25a'},
 'examples/freyd_native_snake_observations.lp': {'ambientConstantFunctor': 0,
                                                 'ambientConstantTransf': 250,
                                                 'freydComponent': 2,
                                                 'freydDiagramCategory': 6,
                                                 'initialOp': 0,
                                                 'sha256': 'b49cf05e764b2e9299a819c4848b8a55b13c135b89d34865f0e7f4178648b2be'},
 'examples/freyd_native_snake_pair_exactness.lp': {'ambientConstantFunctor': 0,
                                                   'ambientConstantTransf': 0,
                                                   'freydComponent': 0,
                                                   'freydDiagramCategory': 0,
                                                   'initialOp': 0,
                                                   'sha256': '02997601cd877a4fb6d6ab64cb52b4168f65c5ffb9e7bb59812ff715d12584ca'}}

FREYD='(@CommRingFreydPresentation_cat R)'

def migrate_native_freyd_pair_consumer(name,original):
 if name not in SOURCES:return None
 spec=SOURCES[name];assert hashlib.sha256(original.encode()).hexdigest()==spec['sha256']
 text=original
 text,count=re.subn(r'\bOp_cat\b','TotalOp_cat',text);assert count==spec['initialOp'],name
 text,count=re.subn(r'\bFunctor_cat(?=\s+WalkingArrow_cat\s+\(@CommRingFreydPresentation_cat\s+R\))','Functor_oplax_cat',text);assert count==spec['freydDiagramCategory'],name
 count=0
 while hits:=list(re.finditer(r'@tapp0_fapp0\s+WalkingArrow_cat\s+\(@CommRingFreydPresentation_cat\s+R\)',text)):
  m=hits[-1];i=m.end();args=[]
  for _ in range(4):a,i=_atom(text,i);args.append(a)
  d,e,x,u=args
  new=f'@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat {FREYD}) {FREYD} (@diagram_oplax_evaluation_at_func WalkingArrow_cat {FREYD} {x}) {d} {e} {u}'
  text=text[:m.start()]+new+text[i:];count+=1
 assert count==spec['freydComponent'],name
 count=0
 while hits:=list(re.finditer(r'@Const_transf\b',text)):
  m=hits[-1];i=m.end();args=[]
  for _ in range(5):a,i=_atom(text,i);args.append(a)
  K,C,x,y,p=args;assert ' '.join(C.split()) in ('C',FREYD),(name,C)
  raw='(@CONST_TRANSF_ORIGINAL '+' '.join(args)+')'
  new=f'@strict_transfor {K} {C} (@Const_func {K} {C} {x}) (@Const_func {K} {C} {y}) {raw}'
  text=text[:m.start()]+new+text[i:];count+=1
 assert count==spec['ambientConstantTransf'],name
 text=text.replace('@CONST_TRANSF_ORIGINAL','@Const_transf')
 count=0
 while hits:=list(re.finditer(r'@Const_func_func\b',text)):
  m=hits[-1];i=m.end();args=[]
  for _ in range(2):a,i=_atom(text,i);args.append(a)
  K,C=args;assert (K,C)==('K','C'),(name,args)
  raw='(@CONST_FUNC_ORIGINAL '+' '.join(args)+')'
  new=f'@comp_cat_fapp0 {C} (Functor_cart_cat {K} {C}) (Functor_cat {K} {C}) (Functor_cart_include {K} {C}) {raw}'
  text=text[:m.start()]+new+text[i:];count+=1
 assert count==spec['ambientConstantFunctor'],name
 text=text.replace('@CONST_FUNC_ORIGINAL','@Const_func_func')
 decl=r'(?m)^(?:(?:protected|injective|constant) )?symbol\s+(\w+)'
 assert re.findall(decl,original)==re.findall(decl,text),name
 assert re.findall(r'(?m)^(assert(?:not)?)\b',original)==re.findall(r'(?m)^(assert(?:not)?)\b',text),name
 return text
