"""Source-pinned original third native-snake exactness chain.

Original maps, inverse data and complete reviewers own qualification.
No new formal declaration, rule or caller assumption.
"""
import hashlib
import re
from pathlib import Path
from production_diagram_observation_migration import _atom, _point_readings
from production_selected_presentation_migration import map_calls
from production_introduced_input_migration import enc_walk

SOURCES = {'emdash3_2_one_cat_native_snake_third_covers.lp': {'counts': {'fapp0': 0,
                                                               'functorCarrier': 0,
                                                               'functorCategory': 28,
                                                               'initialOp': 14,
                                                               'shapeAction': 0,
                                                               'tapp0_fapp0': 0,
                                                               'transforCarrier': 0,
                                                               'walkingConstructor': 0},
                                                    'sha256': '0b6cb9e0daf8e0e495f6dcdcff284cd271b3b609224bc495f257ed20dbf16a3a',
                                                    'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                   'diagram_evaluation_transf': 0,
                                                                   'diagram_family_at_func': 0,
                                                                   'diagram_family_transf': 0,
                                                                   'one_cat_functor_category': 0,
                                                                   'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_third_exactness.lp': {'counts': {'fapp0': 0,
                                                                  'functorCarrier': 0,
                                                                  'functorCategory': 49,
                                                                  'initialOp': 5,
                                                                  'shapeAction': 0,
                                                                  'tapp0_fapp0': 0,
                                                                  'transforCarrier': 0,
                                                                  'walkingConstructor': 0},
                                                       'sha256': 'c80b4efd60a76638d55a0e896e2db0c23867cd4d53c17f2369f47b63b9b83ea3',
                                                       'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                      'diagram_evaluation_transf': 0,
                                                                      'diagram_family_at_func': 0,
                                                                      'diagram_family_transf': 0,
                                                                      'one_cat_functor_category': 0,
                                                                      'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_third_representatives.lp': {'counts': {'fapp0': 0,
                                                                        'functorCarrier': 0,
                                                                        'functorCategory': 11,
                                                                        'initialOp': 7,
                                                                        'shapeAction': 0,
                                                                        'tapp0_fapp0': 0,
                                                                        'transforCarrier': 0,
                                                                        'walkingConstructor': 0},
                                                             'sha256': '67aa96228427d22f03378951e60c7e6d88991d77faa4dc46d8ba1825e9dd0b25',
                                                             'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                            'diagram_evaluation_transf': 0,
                                                                            'diagram_family_at_func': 0,
                                                                            'diagram_family_transf': 0,
                                                                            'one_cat_functor_category': 0,
                                                                            'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_native_snake_third_covers.lp': {'counts': {'fapp0': 0,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 3,
                                                              'initialOp': 4,
                                                              'shapeAction': 0,
                                                              'tapp0_fapp0': 0,
                                                              'transforCarrier': 0,
                                                              'walkingConstructor': 0},
                                                   'sha256': 'e11a8d92766653f93576498419583a18ce3acf4d5e9c1103e3d95124364b34bb',
                                                   'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                  'diagram_evaluation_transf': 0,
                                                                  'diagram_family_at_func': 0,
                                                                  'diagram_family_transf': 0,
                                                                  'one_cat_functor_category': 0,
                                                                  'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_native_snake_third_exactness.lp': {'counts': {'fapp0': 0,
                                                                 'functorCarrier': 0,
                                                                 'functorCategory': 5,
                                                                 'initialOp': 4,
                                                                 'shapeAction': 0,
                                                                 'tapp0_fapp0': 0,
                                                                 'transforCarrier': 0,
                                                                 'walkingConstructor': 0},
                                                      'sha256': '4d4f35f943bd976d7caf47b7550ab1cd2989bd113494d9ae3354160eb43d3420',
                                                      'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                     'diagram_evaluation_transf': 0,
                                                                     'diagram_family_at_func': 0,
                                                                     'diagram_family_transf': 0,
                                                                     'one_cat_functor_category': 0,
                                                                     'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_native_snake_third_representatives.lp': {'counts': {'fapp0': 0,
                                                                       'functorCarrier': 0,
                                                                       'functorCategory': 0,
                                                                       'initialOp': 3,
                                                                       'shapeAction': 0,
                                                                       'tapp0_fapp0': 0,
                                                                       'transforCarrier': 0,
                                                                       'walkingConstructor': 0},
                                                            'sha256': '924eb0877288403b3d1f589682524ca82c22b71c44e332f7835e3805718e48ea',
                                                            'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                           'diagram_evaluation_transf': 0,
                                                                           'diagram_family_at_func': 0,
                                                                           'diagram_family_transf': 0,
                                                                           'one_cat_functor_category': 0,
                                                                           'sym_transf_tapp0_transf': 0}}}

def snake_third_cover_lift_view(text):
    fragment=Path(__file__).with_name('production_native_snake_third_zero_views.lpfragment').read_text()
    marker='// Lift κ_cp into the original image kernel on the original Q-arrow of b.'
    assert text.count(marker)==1
    edits=[]
    for owner,consumer in [('one_cat_native_snake_third_cover_image_lift','one_cat_kernel_family_lift'),('one_cat_native_snake_third_cover_image_reconstruction','one_cat_kernel_family_lift_ambient_reconstruction')]:
        m=re.search(r'(?m)^symbol '+owner+r'\b.*?;',text,re.S);assert m
        part=m.group();hits=list(re.finditer(r'@'+consumer+r'\b',part));assert len(hits)==1
        hit=hits[0];cursor=hit.end();args=[]
        for _ in range(12):a,cursor=_atom(part,cursor);args.append(a)
        assert args[:2]==['K','C'] and args[3:5]==['C1','t'] and args[6:8]==['T0','P']
        assert 'one_cat_native_snake_third_cover_image_zero' in args[11]
        args[11]='(@one_cat_native_snake_third_cover_image_zero_native K C C1 Prod t Add T0 P Q N A B X D b c h)'
        edits.append((m.start()+hit.start(),m.start()+cursor,'@'+consumer+' '+ '\n    '.join(args)))
    assert len(edits)==2
    for a,b,new in reversed(edits):text=text[:a]+new+text[b:]
    return text.replace(marker,fragment+'\n'+marker)


def migrate_native_snake_third_consumer(name,original):
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
 if name == 'emdash3_2_one_cat_native_snake_third_covers.lp':
  text=snake_third_cover_lift_view(text)
 decl=r'(?m)^(?:(?:protected|injective|constant) )?symbol\s+(\w+)'
 added=['one_cat_native_snake_third_cover_zero_target_path', 'one_cat_native_snake_third_cover_image_zero_native'] if name=='emdash3_2_one_cat_native_snake_third_covers.lp' else []
 assert [n for n in re.findall(decl,text) if n not in added]==re.findall(decl,original),name
 assert all(re.findall(decl,text).count(n)==1 for n in added)
 assert re.findall(r'(?m)^(assert(?:not)?)\b',original)==re.findall(r'(?m)^(assert(?:not)?)\b',text),name
 return text
