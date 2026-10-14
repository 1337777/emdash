#!/usr/bin/env python3
"""Emit the defined general-FF action on Cartesian-family Homd targets."""
import hashlib
import json
from pathlib import Path
import runpy


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    audit=Path(__file__).resolve().parent;root=audit.parents[1]
    evidence=audit/'cart_homd_root_verification.json';donor=json.loads(evidence.read_text())
    for path,h in donor['authoringInputs'].items():assert sha(root/path)==h,path
    runpy.run_path(str(audit/'cart_homd_root_replay.py'),run_name='__main__')
    source=root/'tmp/probes/cart_homd_root/candidate.lp'
    assert sha(source)==donor['outputSha256']
    owner=audit/'cart_homd_relative.lpfragment';controls=audit/'cart_homd_relative_controls.lpfragment'
    action=audit/'cart_homd_intrinsic.lpfragment';action_controls=audit/'cart_homd_intrinsic_controls.lpfragment'
    body=source.read_text();marker='// Native one-leg controls.'
    assert body.count(marker)==1
    out=root/'tmp/probes/cart_homd_relative';out.mkdir(parents=True,exist_ok=True)
    target=out/'candidate.lp';target.write_text(body.replace(marker,owner.read_text()+'\n'+action.read_text()+'\n'+marker)
      +'\n'+controls.read_text()+'\n'+action_controls.read_text())
    (out/'lambdapi.pkg').write_bytes((root/'lambdapi.pkg').read_bytes())
    (out/'manifest.json').write_text(json.dumps({
      'status':'non-library general-FF relative Homd and intrinsic-action projection',
      'donorEvidence':str(evidence.relative_to(root)),'donorEvidenceSha256':sha(evidence),
      'authoringInputs':{str(p.relative_to(root)):sha(p) for p in (Path(__file__).resolve(),owner,controls,action,action_controls)},
      'outputSha256':sha(target),
    },indent=2)+'\n')
    print('Emitted one general-FF Homd target-action candidate.')


if __name__=='__main__':main()
