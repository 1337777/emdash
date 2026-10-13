#!/usr/bin/env python3
"""Qualify existing native source action on identity Homd; no checker run."""
import hashlib
import json
from pathlib import Path
import subprocess

def main():
    audit=Path(__file__).resolve().parent; root=audit.parents[1]
    digest=lambda data:hashlib.sha256(data).hexdigest()
    prior_path=audit/'foundation_assembly_verification.json'
    prior=json.loads(prior_path.read_text())
    donor=root/'tmp/probes/foundation_assembly/combined_controls.lp'
    source=donor.read_text()
    assert digest(source.encode())==prior['outputs'][donor.name]
    revision='f8af1fca472657ff1598c639eb29c0566e7b2ec0'
    prod=subprocess.check_output(['git','show',revision+':emdash2/emdash3_2.lp'],cwd=root).decode()
    end=prod.index('// First-class whole path for the ambient left/source presentation.')
    start=prod.rfind('unif_rule',0,end)
    native=prod[start:end]
    assert '@tapp1_func $K Cat_cat' in native
    paths=[Path(__file__),prior_path,donor,root/'lambdapi.pkg']
    def read(name):
        p=audit/name;paths.append(p);body=p.read_text()
        # Retain the checked x-consumer separator bytes after EOF hygiene.
        if name.startswith('homd_x_consumer_'):
            body=body.rstrip('\n')+'\n\n'
        return body
    post=read('homd_native_action_post_view.lpfragment')
    src=read('homd_native_action_source_view.lpfragment')
    late_src=read('homd_native_action_source_late_facade.lpfragment')
    controls=read('homd_native_action_controls.lpfragment')
    post_anchor='// Proof-time identity-family comparison with ordinary raw composition.\nunif_rule @hom_postcomp_fapp0'
    src_anchor='// 6c. Constant/opposite transfors and Cat-valued composition projections'
    assert source.count(post_anchor)==source.count(src_anchor)==1
    with_post=source.replace(post_anchor,post+'\n'+post_anchor)
    selected=with_post.replace(src_anchor,late_src+'\n'+src_anchor)
    identity=read('homd_x_consumer_identity_action_boundary.lpfragment')
    target=read('homd_x_consumer_target_controls.lpfragment')
    y=read('homd_x_consumer_section_y_comparison.lpfragment')
    right=read('homd_x_consumer_right_route_leaf.lpfragment')
    outputs={
      'original_source_view.lp':source.replace(src_anchor,native+'\n'+src_anchor)+'\n'+identity,
      'source_view.lp':selected+'\n'+identity+'\n'+controls,
      'target_view.lp':selected+'\n'+target,
      'y_view.lp':selected+'\n'+y,
      'combined_controls.lp':selected+'\n'+controls+'\n'+identity+'\n'+target+'\n'+y+'\n'+right,
    }
    outputs['without_post_view.lp']=outputs['combined_controls.lp'].replace(post,'')
    outputs['without_source_view.lp']=outputs['combined_controls.lp'].replace(late_src,'')
    outputs['early_combined_controls.lp']=outputs['combined_controls.lp'].replace(late_src,src)
    outputs['early_without_post.lp']=outputs['early_combined_controls.lp'].replace(post,'')
    outputs['early_without_source.lp']=outputs['early_combined_controls.lp'].replace(src,'')
    out=root/'tmp/probes/homd_native_action';out.mkdir(parents=True,exist_ok=True)
    for name,text in outputs.items():(out/name).write_text(text)
    (out/'lambdapi.pkg').write_bytes((root/'lambdapi.pkg').read_bytes())
    manifest={'status':'non-library native source-action qualification; no strict naturality or tensor derivation',
      'sourceInputs':{str(p.relative_to(root)):digest(p.read_bytes()) for p in paths},
      'productionRevision':revision,'nativeSourceActionSha256':digest(native.encode()),
      'outputs':{n:digest(t.encode()) for n,t in outputs.items()}}
    manifest['outputs']['lambdapi.pkg']=digest((root/'lambdapi.pkg').read_bytes())
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print('Prepared native Homd source/target action comparisons; no checker run.')

if __name__=='__main__':main()
