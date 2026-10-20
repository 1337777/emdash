#!/usr/bin/env python3
"""Non-library replay of the qualified strict-functor compatibility retirement.

Run only from production_owner_migration after the intermediate compatibility
phase. This rewrites explicitly inventoried legacy calls and declarations;
Lambdapi checks the resulting source. It is not a trusted elaborator/checker.
"""
from pathlib import Path
import hashlib
import re

# Bounded source-to-source migration. Lambdapi remains the type checker.
def code_mask(text):
    out=list(text);i=0;depth=0;quoted=False
    while i<len(text):
        if depth:
            if text.startswith('/*',i):out[i:i+2]='  ';depth+=1;i+=2;continue
            if text.startswith('*/',i):out[i:i+2]='  ';depth-=1;i+=2;continue
            if text[i]!='\n':out[i]=' '
            i+=1;continue
        if quoted:
            if text[i]=='\\' and i+1<len(text):out[i:i+2]='  ';i+=2;continue
            if text[i]=='"':quoted=False
            if text[i]!='\n':out[i]=' '
            i+=1;continue
        if text.startswith('/*',i):out[i:i+2]='  ';depth=1;i+=2;continue
        if text.startswith('//',i):
            e=text.find('\n',i);e=len(text) if e<0 else e;out[i:e]=' '*(e-i);i=e;continue
        if text[i]=='"':out[i]=' ';quoted=True
        i+=1
    assert not depth and not quoted
    return ''.join(out)

def decl_span(text,name):
    if not re.search(r'(?m)^(?:(?:constant|injective|protected) )?symbol '+re.escape(name)+r'\b',text):return None
    c=code_mask(text);m=re.search(r'(?m)^(?:(?:constant|injective|protected) )?symbol '+re.escape(name)+r'\b',c)
    if not m:return None
    e=c.index(';',m.start())+1
    assert 'begin' not in c[m.start():e],name
    return m.start(),e

def remove_decl(text,name):
    span=decl_span(text,name)
    if span:text=text[:span[0]]+text[span[1]:]
    return text,bool(span)

def arg_end(code,i):
    while i<len(code) and code[i].isspace():i+=1
    start=i
    assert i<len(code) and code[i] not in ');',code[max(0,i-70):i+70]
    if code[i] in '([{':
        stack=[{'(':')','[':']','{':'}'}[code[i]]];i+=1
        while stack:
            if code[i] in '([{':stack.append({'(':')','[':']','{':'}'}[code[i]])
            elif code[i] in ')]}':assert code[i]==stack.pop()
            i+=1
        return start,i
    while i<len(code) and not code[i].isspace() and code[i] not in '();[]{}':i+=1
    assert code[start:i] not in ('λ','Π','≔','↪','≡'),code[start:i]
    return start,i

def calls(text,name,explicit,implicit,build):
    total=0
    if name not in text:return text,total
    while True:
        c=code_mask(text);spans=[];skip=0
        for m in re.finditer(r'(?<![\w@])(@?)'+re.escape(name)+r'\b',c):
            if m.start()<skip:continue
            assert m.start()==0 or c[m.start()-1]!='.', ('qualified legacy call', name)
            i=m.end();args=[]
            for _ in range(explicit if m[1] else implicit):
                s,e=arg_end(c,i);args.append(text[s:e]);i=e
            spans.append((m.start(),i,build(args,bool(m[1]))));skip=i
        if not spans:return text,total
        for s,e,new in reversed(spans):text=text[:s]+new+text[e:]
        total+=len(spans)
        assert total<10000,name

def rename_code(text,mapping):
    c=code_mask(text);spans=[]
    for m in re.finditer(r'\b[A-Za-z_][A-Za-z_0-9]*\b',c):
        if m[0] in mapping:
            assert m.start()==0 or c[m.start()-1]!='.', ('qualified legacy name', m[0])
            spans.append((m.start(),m.end(),mapping[m[0]]))
    for s,e,v in reversed(spans):text=text[:s]+v+text[e:]
    return text

ALIASES={
 'StrictFunctor':'Functor','StrictFunctor_cat':'Functor_cat',
 'strict_identity':'id_func','strict_constant_func':'Const_func',
 'strict_path_cat_func':'Path_cat_func','strict_path_sym_func':'Path_sym_func',
 'strict_prof_reindex_func':'Prof_reindex_func','strict_prof_imply_cov_func':'Prof_imply_cov_func',
 'StrictCommRingPsh':'CommRingPsh','StrictCommRingPsh_cat':'CommRingPsh_cat',
 'gray_curry_R_strict':'gray_curry_R_func','gray_uncurry_R_strict':'gray_uncurry_R_func',
 'gray_coevaluation_R_strict':'gray_coevaluation_R_func','gray_evaluation_R_strict':'gray_evaluation_R_func',
 'strict_iso_evidence_fmap':'iso_evidence_fmap','strict_prof_comparison_fmap':'prof_comparison_fmap',
 **{'strict_'+n:n for n in ['defiso_fmap_to','defiso_fmap_from','defiso_fmap_to_path','defiso_fmap_from_path','defiso_fmap','defiso_fmap_to_beta','defiso_fmap_cancel']},
}
RENAMES={
 'strict_functor_is_strict':'functor_is_strict',
 'strict_functor_composition_path':'functor_composition_path',
 'strict_omega_equiv_along_fapp1':'omega_equiv_along_fmap',
 'strict_omega_equiv_along_fapp1_left_law':'omega_equiv_along_fmap_left_law',
 'strict_omega_equiv_along_fapp1_right_law':'omega_equiv_along_fmap_right_law',
 'strict_omega_equiv_left_projection':'omega_equiv_fmap_left_projection',
 'strict_omega_equiv_right_projection':'omega_equiv_fmap_right_projection',
}
ERASED=['make_strict_functor','strict_functor','strict_functor_underlying','strict_functor_include_func','make_strict_functor_carrier_path','strict_identity_carrier_path','strict_comm_ring_psh','one_cat_strict_admission']
UNUSED_PROOFS=['identity_is_strict','prof_reindex_is_strict','prof_imply_cov_is_strict','path_sym_is_strict','constant_functor_is_strict','path_cat_func_is_strict','gray_curry_R_is_strict','gray_uncurry_R_is_strict']

def first_comment(text,replacement):
 s=text.index('/*');e=text.index('*/',s)+2;return text[:s]+replacement+text[e:]
def cleanup_retired_comments(name, t):
    if name=='emdash3_2_gray_profiles.lp':
        t=first_comment(t,'''/*
  Emdash v3.2: native compositor properties and transformation profiles.

  Public Functor is the strict map carrier. IsStrictFunctor and its evidence
  projections describe the existing extracted compositor; functor_is_strict
  supplies its canonical proof for default maps. They are property/evidence
  interfaces, not an additional map grammar or operational admission.

  GrayHom_lax uses ordinary functor objects and retains its LaxTransfor Homs.
  StrictTransfor and StrictFunctord remain genuine refinements of the default
  conventional-lax transformations and displayed maps.
*/''')
        if '// Transitional compatibility views:' in t:
            s=t.index('// Transitional compatibility views:');e=t.index('// Derived from the existing extracted compositor',s);t=t[:s]+t[e:]
        if '// The complete Hom profile agrees with the public ordinary mapping category.' in t:
            s=t.index('// The complete Hom profile agrees with the public ordinary mapping category.');e=t.index('// -----------------------------------------------------------------------------------------------\n// Whole strict-transfor property',s);t=t[:s]+t[e:]
    if name=='emdash3_2_strict_functor_actions.lp':
        t=first_comment(t,'''/*
  Emdash v3.2: default functor action on equality-valued equivalences.

  Ordinary strict Functor inputs preserve the actual chosen inverse maps and
  their cancellation laws through native action. The mapped DefIso and Prof
  comparison owners are shared directly; no strict-object wrapper, separate
  admission certificate or detached composition law is consumed.
*/''')
        s=t.index('// Legacy names are defined views of the single default action owner.');e=t.index('// Default functorial action on the existing whole comparison package.',s);t=t[:s]+t[e:]
        s=t.index('// Functorial image of a profunctor comparison under one classified carrier.');e=t.index('// Proof-time join when strict functoriality',s);t=t[:s]+t[e:]
        s=t.index('/*\n  Selected named strict packages');e=t.index('// Forward universal operation after reindexing',s);t=t[:s]+'// Weighted-limit and adjunction actions use the same default owners.\n\n'+t[e:]
    if name=='emdash3_2_commutative_algebra_presheaves.lp':
        if '// Compatibility spellings:' in t:
            s=t.index('// Compatibility spellings:');e=t.index('// The affine CommRing-valued presheaf',s);t=t[:s]+t[e:]
    if name=='emdash3_2_gray_right_closure.lp':
        t=t.replace('// Supplied semantic strictness of the existing whole curry operation.\n','').replace('// Supplied semantic strictness of the existing whole uncurry operation.\n','')
        t=t.replace('curry applied to the tensor identity package.', 'curry applied to the ordinary tensor identity.')
        t=t.replace('uncurry applied to the internal-Hom identity package.', 'uncurry applied to the ordinary internal-Hom identity.')
    if name=='emdash3_2_one_cat_functor_profiles.lp':t=t.replace('// Compatibility adapter: the default functor is already strict.', '// The ordinary map itself is the default strict carrier.')
    if name=='strict_wrapper_consumers_controls.lp':
        t=t[:t.index('// Ordinary ring presheaves pass directly through the compatibility view.')]
    t=re.sub(r'\n[ \t]*\n(?:[ \t]*\n)+','\n\n',t).rstrip()+'\n'
    return t

def finish_strict_wrapper_retirement(root: Path, package: Path, outputs: dict) -> dict:
    paths=sorted({root/n for n in outputs if (root/n).is_relative_to(package) and n.endswith('.lp')})
    report={'renamedImplementations':RENAMES,'replacedAliases':ALIASES,'erasedViews':ERASED,'removedUnusedProofs':UNUSED_PROOFS,'changes':[]}
    removed_counts={};alltexts={}
    for q in paths:
        old=q.read_text();t=old
        relevant=list(ALIASES)+ERASED+UNUSED_PROOFS+list(RENAMES)
        if not any(n in old for n in relevant):
            alltexts[q]=t
            continue
        active=set(re.findall(r'\b[A-Za-z_][A-Za-z_0-9]*\b',code_mask(old)))
        if not active.intersection(relevant):
            alltexts[q]=t
            continue
        # Move the actual co/evaluation definition to its ordinary public owner.
        if q.name=='emdash3_2_gray_right_closure.lp':
            for prefix in ['gray_coevaluation_R','gray_evaluation_R']:
                a,b=decl_span(t,prefix+'_strict');body=t[a:b].split('≔',1)[1]
                c,d=decl_span(t,prefix+'_func');sig=t[c:d].split('≔',1)[0]
                t=t[:c]+sig+'≔'+body+t[d:]
        for n in list(ALIASES)+ERASED+UNUSED_PROOFS:
            t,removed=remove_decl(t,n)
            if removed:removed_counts[n]=removed_counts.get(n,0)+1
        for n in ['strict_functor','strict_functor_underlying']:
            t,_=calls(t,n,3,1,lambda a,e:a[-1])
        t,_=calls(t,'make_strict_functor',4,2,lambda a,e:a[-2])
        t,_=calls(t,'strict_functor_include_func',2,2,lambda a,e:'(@id_func (@Functor_cat '+a[0]+' '+a[1]+'))')
        t,_=calls(t,'make_strict_functor_carrier_path',4,2,lambda a,e:'(@eq_refl (Functor '+a[0]+' '+a[1]+') '+a[2]+')' if e else '(eq_refl '+a[0]+')')
        t,_=calls(t,'strict_identity_carrier_path',1,1,lambda a,e:'(@eq_refl (Functor '+a[0]+' '+a[0]+') (@id_func '+a[0]+'))')
        t,_=calls(t,'strict_comm_ring_psh',2,1,lambda a,e:a[-1])
        t,_=calls(t,'one_cat_strict_admission',4,2,lambda a,e:a[-1])
        t=rename_code(t,{**ALIASES,**RENAMES})
        t=cleanup_retired_comments(q.name,t)
        if t!=old:
            q.write_text(t);report['changes'].append({'file':str(q.relative_to(package)),'beforeSha256':hashlib.sha256(old.encode()).hexdigest(),'afterSha256':hashlib.sha256(t.encode()).hexdigest()})
        alltexts[q]=t
    retired=set(ALIASES)|set(ERASED)|set(UNUSED_PROOFS)|set(RENAMES)
    for q,t in alltexts.items():
        possible={n for n in retired if n in t}
        if possible:
            active=set(re.findall(r'\b[A-Za-z_][A-Za-z_0-9]*\b',code_mask(t)))
            assert not (possible & active),(str(q.relative_to(package)),sorted(possible & active))
    report['removedDeclarationCounts']=removed_counts
    assert len(removed_counts)==39 and all(n==1 for n in removed_counts.values()), removed_counts
    return report
