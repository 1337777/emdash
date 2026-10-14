#!/usr/bin/env python3
"""Emit the represented whole-y Homd section on the strict-map donor.

NON-LIBRARY. Q and its strict-map mate are structural contracts. This is not
the outer Homd root or a qualification of all Q composition and coherence.
"""
import hashlib
import json
from pathlib import Path
import runpy


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def omit(source, marker):
    assert source.count(marker)==1, marker
    start=source.index(marker)
    return source[:start]+source[source.index(';',start)+1:]


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    evidence = audit/'strict_fibcov_verification.json'
    donor = json.loads(evidence.read_text())
    for name, expected in donor['authoringInputs'].items():
        assert sha(root/name) == expected, name
    runpy.run_path(str(audit/'strict_fibcov_replay.py'),run_name='__main__')
    source = root/'tmp/probes/strict_fibcov/candidate.lp'
    assert sha(source)==donor['outputs']['candidate.lp']
    body = source.read_text()
    files=('strict_homd_section_q.lpfragment','strict_homd_section_owner.lpfragment',
           'strict_homd_section_controls.lpfragment',
           'strict_homd_section_relative.lpfragment','strict_homd_section_relative_controls.lpfragment',
           'strict_homd_section_whiskering.lpfragment',
           'strict_homd_section_u.lpfragment','strict_homd_section_u_controls.lpfragment',
           'strict_homd_section_lax_controls.lpfragment',
           'strict_homd_section_cart_boundary.lpfragment')
    parts={name:(audit/name).read_text() for name in files}
    owner='// Native one-leg controls.'
    assert body.count(owner)==1
    out=root/'tmp/probes/strict_homd_section';out.mkdir(parents=True,exist_ok=True)
    q=parts[files[0]];mate=parts[files[1]];u=parts[files[6]];whisker=parts[files[5]]
    no_action=omit(omit(mate,'rule @tapp1_func'),'rule @tapp1_fapp0')
    joins='// The same source laws after component evaluation erased the whole map.'
    assert u.count(joins)==1
    hom='rule Hom_cat sf_q_cat $A $B\n  ↪ Functor_cat $A (Functor_cat (Op_cat $B) Cat_cat);'
    assert q.count(hom)==1
    cart=parts[files[9]]+'\n'+q.replace(hom,
        'rule Hom_cat sf_q_cat $A $B\n  ↪ sf_q_cart_map_cat $A (sf_q_cart_map_cat (Op_cat $B) Cat_cat);')
    wrong=q.replace(hom,
        'rule Hom_cat sf_q_cat $A $B\n  ↪ Functor_cat $A (Functor_cat $B Cat_cat);')
    variants={
        'candidate.lp':(q,mate,u,whisker,True),
        'no_mate_component.lp':(q,omit(mate,'rule @tapp0_fapp0'),u,whisker,True),
        'no_mate_component_group.lp':(q,omit(mate,'rule @tapp0_fapp0'),'',whisker,False),
        'no_mate_action.lp':(q,no_action,u,whisker,True),
        'no_right_rep_composition.lp':(omit(q,'rule @comp_fapp0 sf_q_cat $A $B $C $P'),mate,u,whisker,True),
        'no_stable_rep_cut.lp':(omit(q,'rule @hom_postcomp_fapp0 sf_q_cat sf_q_cat (@id Cat_cat sf_q_cat) $A $B $C $P'),mate,u,whisker,True),
        'no_diagram_fold.lp':(omit(q,'rule @hom_postcomp_fapp0 Cat_cat Cat_cat'),mate,u,whisker,True),
        'no_fixed_whiskering.lp':(q,mate,u,'',True),
        'no_u_leaf.lp':(q,mate,omit(u,'rule @tapp0_fapp0 _ _ _ _ $f'),whisker,True),
        'no_u_joins.lp':(q,mate,u[:u.index(joins)],whisker,True),
        'no_source_beta.lp':(q,mate,omit(u,'rule fapp0 (@sf_homd_id_src_func'),whisker,True),
        'cart_direct_substitution.lp':(cart,mate,u,whisker,True),
        'wrong_index_duality.lp':(wrong,mate,u,whisker,True),
    }
    outputs={}
    for name,(qv,mv,uv,wv,with_u) in variants.items():
        candidate=body.replace(owner,'\n'.join((wv,qv,mv,parts[files[3]],uv))+'\n'+owner)
        controls=(2,4,7,8) if with_u else (2,4)
        candidate+='\n'+'\n'.join(parts[files[i]] for i in controls)
        target=out/name;target.write_text(candidate);outputs[name]=sha(target)
    (out/'lambdapi.pkg').write_bytes((root/'lambdapi.pkg').read_bytes())
    authors=[Path(__file__)]+[audit/n for n in files]
    (out/'manifest.json').write_text(json.dumps({
        'status':'unqualified represented whole-y Homd section candidate',
        'donorEvidence':str(evidence.relative_to(root)),'donorEvidenceSha256':sha(evidence),
        'authoringInputs':{str(p.relative_to(root)):sha(p) for p in authors},
        'outputs':outputs,
    },indent=2)+'\n')
    print('Emitted represented whole-y Homd section candidate.')


if __name__=='__main__':
    main()
