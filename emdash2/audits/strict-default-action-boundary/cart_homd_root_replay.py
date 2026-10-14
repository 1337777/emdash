#!/usr/bin/env python3
"""Emit the Cartesian-family whole x-root candidate at its owning position."""
import hashlib
import json
from pathlib import Path
import runpy


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    audit=Path(__file__).resolve().parent;root=audit.parents[1]
    evidence=audit/'cart_homd_section_verification.json'
    donor=json.loads(evidence.read_text())
    for path,h in donor['authoringInputs'].items():assert sha(root/path)==h,path
    runpy.run_path(str(audit/'cart_homd_section_replay.py'),run_name='__main__')
    source=root/'tmp/probes/cart_homd_section/candidate.lp'
    assert sha(source)==donor['outputSha256']
    body=source.read_text()
    cat=audit/'co_at2_category.lpfragment';fun=audit/'co_at2_functor.lpfragment'
    fun_text=fun.read_text();stop='// Whole Cartesian mapping-category action'
    assert fun_text.count(stop)==1
    fun_excerpt=fun_text[:fun_text.index(stop)]
    owner=audit/'cart_homd_root.lpfragment';controls=audit/'cart_homd_root_controls.lpfragment'
    additions=[('// Path categories internalize HoTT equality as a groupoidal category.',cat.read_text()),
      ('// The same strict functor with dimensions 2 and above reversed.',fun_excerpt),
      ('// Native one-leg controls.',owner.read_text())]
    assert 'injective symbol CoAt2_cat' not in body
    for marker,text in additions:
        assert body.count(marker)==1,marker
        body=body.replace(marker,text+'\n'+marker)
    out=root/'tmp/probes/cart_homd_root';out.mkdir(parents=True,exist_ok=True)
    target=out/'candidate.lp';target.write_text(body+'\n'+controls.read_text())
    (out/'lambdapi.pkg').write_bytes((root/'lambdapi.pkg').read_bytes())
    (out/'manifest.json').write_text(json.dumps({
      'status':'non-library Cartesian-family whole x-root candidate',
      'donorEvidence':str(evidence.relative_to(root)),'donorEvidenceSha256':sha(evidence),
      'authoringInputs':{str(p.relative_to(root)):sha(p) for p in (Path(__file__).resolve(),cat,fun,owner,controls)},
      'coAt2StrictFunctorExcerptSha256':hashlib.sha256(fun_excerpt.encode()).hexdigest(),
      'outputSha256':sha(target),
    },indent=2)+'\n')
    print('Emitted one Cartesian-family whole x-root candidate.')


if __name__=='__main__':main()
