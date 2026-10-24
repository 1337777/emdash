"""Source-pinned original finite-tail and native-snake result assembly.

Original structural beta rules, actual annotations/maps and complete
reviewers own qualification. No new categorical theorem or rule is supplied.
"""
import hashlib
import re
from production_diagram_observation_migration import _atom, _point_readings
from production_selected_presentation_migration import map_calls
from production_introduced_input_migration import enc_walk

SOURCES = {'emdash3_2_finite_arrow_tail_append.lp': {'counts': {'fapp0': 0,
                                                      'functorCarrier': 0,
                                                      'functorCategory': 0,
                                                      'initialOp': 0,
                                                      'shapeAction': 0,
                                                      'tapp0_fapp0': 0,
                                                      'transforCarrier': 0,
                                                      'walkingConstructor': 0},
                                           'originalRules': 0,
                                           'sha256': 'eedea38f18424977141a50aa0eedc00fec8ee8e96a10b20236aa535d15e08ca9',
                                           'wholeViews': {'diagram_evaluation_at_func': 0,
                                                          'diagram_evaluation_transf': 0,
                                                          'diagram_family_at_func': 0,
                                                          'diagram_family_transf': 0,
                                                          'one_cat_functor_category': 0,
                                                          'sym_transf_tapp0_transf': 0}},
 'emdash3_2_finite_arrow_tails.lp': {'counts': {'fapp0': 0,
                                                'functorCarrier': 0,
                                                'functorCategory': 0,
                                                'initialOp': 0,
                                                'shapeAction': 0,
                                                'tapp0_fapp0': 0,
                                                'transforCarrier': 0,
                                                'walkingConstructor': 0},
                                     'originalRules': 4,
                                     'sha256': 'a3ad6566cca0ef18f01feaa18cd5d5cda57320a71bef15b0a2ec13791a533f19',
                                     'wholeViews': {'diagram_evaluation_at_func': 0,
                                                    'diagram_evaluation_transf': 0,
                                                    'diagram_family_at_func': 0,
                                                    'diagram_family_transf': 0,
                                                    'one_cat_functor_category': 0,
                                                    'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_six_term_result.lp': {'counts': {'fapp0': 0,
                                                                  'functorCarrier': 0,
                                                                  'functorCategory': 0,
                                                                  'initialOp': 6,
                                                                  'shapeAction': 0,
                                                                  'tapp0_fapp0': 0,
                                                                  'transforCarrier': 0,
                                                                  'walkingConstructor': 0},
                                                       'originalRules': 0,
                                                       'sha256': '31e5f3fa417e5c14f8cccb6960826c96651d982104ba492ee93cfdccd9e10fa0',
                                                       'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                      'diagram_evaluation_transf': 0,
                                                                      'diagram_family_at_func': 0,
                                                                      'diagram_family_transf': 0,
                                                                      'one_cat_functor_category': 0,
                                                                      'sym_transf_tapp0_transf': 0}},
 'examples/finite_arrow_tails.lp': {'counts': {'fapp0': 0,
                                               'functorCarrier': 0,
                                               'functorCategory': 0,
                                               'initialOp': 0,
                                               'shapeAction': 0,
                                               'tapp0_fapp0': 0,
                                               'transforCarrier': 0,
                                               'walkingConstructor': 0},
                                    'originalRules': 0,
                                    'sha256': '0ecfd16bcafd391ef27ced0f8a4467435f89d0de5bc161105eb1500eff6c6430',
                                    'wholeViews': {'diagram_evaluation_at_func': 0,
                                                   'diagram_evaluation_transf': 0,
                                                   'diagram_family_at_func': 0,
                                                   'diagram_family_transf': 0,
                                                   'one_cat_functor_category': 0,
                                                   'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_native_snake_six_term_result.lp': {'counts': {'fapp0': 0,
                                                                 'functorCarrier': 0,
                                                                 'functorCategory': 0,
                                                                 'initialOp': 6,
                                                                 'shapeAction': 0,
                                                                 'tapp0_fapp0': 0,
                                                                 'transforCarrier': 0,
                                                                 'walkingConstructor': 0},
                                                      'originalRules': 0,
                                                      'sha256': 'c5af28576b339f72697d1afec0eff06aa554bf0670f5236bdc052f10e48d1a1e',
                                                      'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                     'diagram_evaluation_transf': 0,
                                                                     'diagram_family_at_func': 0,
                                                                     'diagram_family_transf': 0,
                                                                     'one_cat_functor_category': 0,
                                                                     'sym_transf_tapp0_transf': 0}}}

def migrate_native_snake_result_consumer(name,original):
 if name not in SOURCES:return None
 spec=SOURCES[name];assert hashlib.sha256(original.encode()).hexdigest()==spec['sha256']
 text=original;B='(Functor_oplax_cat WalkingArrow_cat C)'
 for pattern,replacement,key in (
  (r'\bFunctor_cat(?=\s+WalkingArrow_cat\s+C\b)','Functor_oplax_cat','functorCategory'),
  (r'\(Functor\s+WalkingArrow_cat\s+C\s*\)','(Obj '+B+')','functorCarrier'),
  (r'@Transf\s+WalkingArrow_cat\s+C\b','@Hom '+B,'transforCarrier'),
  (r'\bOp_cat(?=\s+C\b)','TotalOp_cat','initialOp')):
  text,count=re.subn(pattern,replacement,text);assert count==spec['counts'][key],(name,key,count)
 text=_point_readings(text,(spec['counts']['fapp0'],spec['counts']['tapp0_fapp0']))
 for head,arity,corrected in (
  ('diagram_family_at_func',3,'diagram_oplax_family_at_func'),
  ('diagram_family_transf',3,'diagram_oplax_family_transf'),
  ('diagram_evaluation_at_func',2,'diagram_oplax_evaluation_at_func'),
  ('diagram_evaluation_transf',2,'diagram_oplax_evaluation_transf'),
  ('sym_transf_tapp0_transf',3,'diagram_oplax_family_map_at'),
  ('one_cat_functor_category',2,'one_cat_oplax_functor_category')):
  edits=[]
  for match in re.finditer(r'@'+head+r'\b',text):
   cursor,args=match.end(),[]
   for _ in range(arity):a,cursor=_atom(text,cursor);args.append(a)
   if args[-2:]!=['WalkingArrow_cat','C']:continue
   edits.append((match.start(),match.end()))
  assert len(edits)==spec['wholeViews'][head],(name,head)
  for lo,hi in reversed(edits):text=text[:lo]+'@'+corrected+text[hi:]
 def arrow(args):
  d,x,y,f=args
  return f'@tapp0_fapp0 {B} C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C {x}) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C {y}) {d} (@diagram_oplax_evaluation_transf WalkingArrow_cat C {x} {y} {f})'
 text,count=map_calls(text,'fapp1_fapp0',4,arrow);assert count==spec['counts']['shapeAction']
 text=enc_walk(text)
 decl=r'(?m)^(?:(?:protected|injective|constant) )?symbol\s+(\w+)'
 assert re.findall(decl,original)==re.findall(decl,text),name
 assert re.findall(r'(?m)^(assert(?:not)?)\b',original)==re.findall(r'(?m)^(assert(?:not)?)\b',text),name
 if spec['originalRules']:assert original==text,name
 return text
