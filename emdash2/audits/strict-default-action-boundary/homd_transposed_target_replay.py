#!/usr/bin/env python3
"""Emit the coordinated transposed-target Homd root candidate.

NON-LIBRARY. Uses only CoAt2 on categories and ordinary strict functors;
the old Cartesian mapping-category duality declarations are excluded.
"""
import hashlib
import json
from pathlib import Path
import runpy


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def omit(source, marker):
    assert source.count(marker)==1,marker
    start=source.index(marker)
    return source[:start]+source[source.index(';',start)+1:]


def main():
    audit=Path(__file__).resolve().parent;root=audit.parents[1]
    evidence=audit/'strict_homd_section_verification.json';donor=json.loads(evidence.read_text())
    for name,expected in donor['authoringInputs'].items():assert sha(root/name)==expected,name
    runpy.run_path(str(audit/'strict_homd_section_replay.py'),run_name='__main__')
    source=root/'tmp/probes/strict_homd_section/candidate.lp'
    assert sha(source)==donor['outputs']['candidate.lp']
    body=source.read_text()
    files=('co_at2_category.lpfragment','co_at2_functor.lpfragment',
           'homd_transposed_target_root.lpfragment','homd_transposed_target_controls.lpfragment',
           'homd_transposed_target_coherence.lpfragment','homd_transposed_target_action_controls.lpfragment',
           'homd_transposed_target_readings.lpfragment',
           'homd_transposed_target_relative.lpfragment','homd_transposed_target_relative_controls.lpfragment')
    parts={n:(audit/n).read_text() for n in files}
    end='// Whole Cartesian mapping-category action'
    assert parts[files[1]].count(end)==1
    cofunctor=parts[files[1]][:parts[files[1]].index(end)]
    assert 'Functor_cart_cat' not in cofunctor
    cat_owner='// Path categories internalize HoTT equality as a groupoidal category.'
    functor_owner='// The same strict functor with dimensions 2 and above reversed.'
    owner='// Native one-leg controls.'
    for marker in (cat_owner,functor_owner,owner):assert body.count(marker)==1,marker
    assert 'injective symbol CoAt2_cat' not in body
    body=body.replace(cat_owner,parts[files[0]]+'\n'+cat_owner)
    body=body.replace(functor_owner,cofunctor+'\n'+functor_owner)
    out=root/'tmp/probes/homd_transposed_target';out.mkdir(parents=True,exist_ok=True)
    root_part=parts[files[2]];coherence=parts[files[4]];readings=parts[files[6]];relative=parts[files[7]]
    no_action=omit(omit(root_part,'rule @tapp1_func'),'rule @tapp1_fapp0')
    no_mate_comp=omit(omit(coherence,'rule @comp_fapp0'),'rule @hom_postcomp_fapp0')
    marker='symbol sf_homd_target_catd'
    start=root_part.index(marker);stop=root_part.index(';',start)+1
    untwisted=root_part[:start]+'''symbol sf_homd_target_catd [K : Cat] (E : τ (Functor K Cat_cat))
  : τ (Functor (CoAt2_cat K) Cat_cat)
≔ @hom_ (Functor_cat K sf_q_cat) (CoAt2_cat K)
    (sf_homd_rep_int K) (@sf_q_diagram K E);'''+root_part[stop:]
    old=': τ (Functor (CoAt2_cat K) (Functor_cat K sf_q_cat));'
    assert root_part.count(old)==1
    wrong_source=root_part.replace(old,': τ (Functor (CoAbove2_cat K) (Functor_cat K sf_q_cat));')
    variants={
        'candidate.lp':(root_part,coherence,readings,relative),
        'no_gamma_object.lp':(omit(root_part,'rule fapp0 (sf_homd_rep_int'),coherence,readings,relative),
        'no_gamma_hom.lp':(omit(root_part,'rule @fapp1_func'),coherence,readings,relative),
        'no_gamma_capped.lp':(omit(root_part,'rule @fapp1_fapp0'),coherence,readings,relative),
        'no_root_component.lp':(omit(root_part,'rule @tapp0_fapp0'),coherence,readings,relative),
        'no_root_action.lp':(no_action,coherence,readings,relative),
        'no_representable_unit.lp':(root_part,omit(coherence,'rule @sf_q_mate'),readings,relative),
        'no_mate_composition.lp':(root_part,no_mate_comp,readings,relative),
        'no_dual_hom_action.lp':(root_part,omit(coherence,'rule @hom_postcomp_func _ _ (@CoAt2_func'),readings,relative),
        'no_gamma_reindexing.lp':(root_part,omit(coherence,'rule @hom_postcomp_func _ _ (sf_homd_rep_int'),readings,relative),
        'no_index_reading.lp':(root_part,coherence,'',relative),
        'no_dual_precomposition.lp':(root_part,coherence,readings,omit(relative,'rule @hom_precomp_along_func')),
        'untwisted_target.lp':(untwisted,coherence,readings,relative),
        'wrong_gamma_source.lp':(wrong_source,coherence,readings,relative),
    }
    outputs={}
    for name,(rp,cp,rd,rel) in variants.items():
        candidate=body.replace(owner,'\n'.join((rp,cp,rd,rel))+'\n'+owner)
        candidate+='\n'+'\n'.join(parts[files[i]] for i in (3,5,8))
        target=out/name;target.write_text(candidate);outputs[name]=sha(target)
    (out/'lambdapi.pkg').write_bytes((root/'lambdapi.pkg').read_bytes())
    authors=[Path(__file__)]+[audit/n for n in files]
    (out/'manifest.json').write_text(json.dumps({
        'status':'unqualified coordinated whole Homd root candidate',
        'donorEvidence':str(evidence.relative_to(root)),'donorEvidenceSha256':sha(evidence),
        'authoringInputs':{str(p.relative_to(root)):sha(p) for p in authors},
        'coAt2StrictFunctorExcerptSha256':hashlib.sha256(cofunctor.encode()).hexdigest(),
        'outputs':outputs,
    },indent=2)+'\n')
    print('Emitted coordinated transposed-target Homd root candidate.')


if __name__=='__main__':main()
