"""Original kernel pullback and adjacent column profile migration; no new rules."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {'emdash3_2_one_cat_kernel_input_observation_paths.lp': ('5b8b51044467ec2fffadd888a55a716f14817ebaa36e9a1340d7138949db87c0',
                                                         'production_kernel_input_observation_paths.lpfragment'),
 'emdash3_2_one_cat_kernel_pullback_comparison.lp': ('778ce927d415b8a6cbde2372b3e6618408f9ffe16bfc65391d004be2f6b3a3e1',
                                                     'production_kernel_pullback_comparison.lpfragment'),
 'emdash3_2_one_cat_kernel_pullback_lifts.lp': ('7c6b406176a9f4a73d1b16614eb8933700d18904ed40494c422ee812190b2900',
                                                'production_kernel_pullback_lifts.lpfragment'),
 'emdash3_2_one_cat_kernel_pullback_universality.lp': ('e5a5dacc0770f4aa947d1e7082a9c5a05ccc5bf4bc91138ede5b84cebbcb7cc7',
                                                       'production_kernel_pullback_universality.lpfragment'),
 'emdash3_2_one_cat_zero_cone_column_inputs.lp': ('c7ad97c9f9363833a46d6ccad5a80d678cd8a0f49753ecf863e96058932bc448',
                                                  'production_zero_cone_column_inputs.lpfragment'),
 'emdash3_2_one_cat_zero_family_postcomposition_paths.lp': ('12fa9a2a25d031fb7d379e127b0f7eb71f913c47ce64704ea0516cb242d09689',
                                                            'production_zero_family_postcomposition_paths.lpfragment'),
 'examples/one_cat_kernel_pullback_universality.lp': ('1a3c14b098052ed44ee6acca739bc7e703a64d6392a1f12f61e61c2927c5bab9',
                                                      'production_reviewer_kernel_pullback_universality.lpfragment'),
 'examples/one_cat_zero_cone_column_inputs.lp': ('e44fe4ba54002c319cb0453f13bc00c902f7f0a9fbdd34aafd805ec42eaa15d1',
                                                 'production_reviewer_zero_cone_column_inputs.lpfragment')}


def finish_kernel_columns(path, text):
    if path not in SOURCES:
        return None
    pin, fragment = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == pin, path
    return (AUDIT / fragment).read_text()
