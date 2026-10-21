"""Original whole kernel input, lift and reconstruction migration."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {'emdash3_2_one_cat_kernel_family_projection_paths.lp': ('93b40fc7fb1dc9bd7f575d3c3cc77fb891dbdebb1f42f849f0d80a8401207b8e',
                                                         'production_kernel_projection_paths.lpfragment'),
 'emdash3_2_one_cat_kernel_family_inputs.lp': ('94626de3bfbbb27b429efe521a809b3a45e6c40d9337fa0f69a31ed71ba78f68',
                                               'production_kernel_family_inputs.lpfragment'),
 'emdash3_2_one_cat_kernel_family_lift.lp': ('71258ec2d79d73f787a3f67aaee11fd909d713a13ff5e50d658b7f71f6cf06f3',
                                             'production_kernel_family_lift.lpfragment'),
 'emdash3_2_one_cat_kernel_precomposition.lp': ('f6425c531e96a7a025209e3ce0f6f82eaa61219331e733c0ba68dcb8ed6c3f77',
                                                'production_kernel_precomposition.lpfragment'),
 'emdash3_2_one_cat_kernel_family_reconstruction.lp': ('95d7006ed2954caf31e55b619844163fa60e3ce970d946d4aca94761dccf71ce',
                                                       'production_kernel_reconstruction.lpfragment'),
 'examples/one_cat_kernel_family_lift.lp': ('ac80e79bdfe7ee453a02bc86aa1ecd6c9d1a5f48630bb905e047a01ab2afa78d',
                                            'production_kernel_lift_reviewer.lpfragment'),
 'examples/one_cat_kernel_precomposition.lp': ('2d77f75aaba00ecff191e0e2363a91dbc7ca08461a4dfea31fd1c14dc59960b1',
                                               'production_kernel_precomposition_reviewer.lpfragment'),
 'examples/one_cat_kernel_family_reconstruction.lp': ('79fbd33dee7770fd757137a3039768042ac3a3ddb375e4cd56e4854ad5d3855e',
                                                      'production_kernel_reconstruction_reviewer.lpfragment')}


def finish_kernel_reconstruction(path, text):
    if path not in SOURCES:
        return None
    pin, fragment = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == pin, path
    return (AUDIT / fragment).read_text()
