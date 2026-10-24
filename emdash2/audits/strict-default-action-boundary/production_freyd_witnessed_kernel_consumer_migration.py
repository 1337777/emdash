"""Source-pinned original witnessed Freyd kernels and cokernels.

Retain raw agreements, selected weak-kernel data and all-test witnessed laws.
This helper initially preserves the complete original source unchanged.
"""
import hashlib

SOURCES = {'emdash3_2_commutative_algebra_finite_free_weak_pullbacks.lp': '82ed562b9534add05b0029f5bb242244c081756eaa6bfcbbd9d88af34e222d37',
 'emdash3_2_commutative_algebra_freyd_cokernels.lp': '1585839ab909f18219ce39d4cc000fc68fe37f5a29194100b1b9842855f31f90',
 'emdash3_2_commutative_algebra_freyd_kernel_choices.lp': 'b78574fd20e847521f2e731c0ba6bea4e4379aa2b270b7c80c6e5723fa3ef1ef',
 'emdash3_2_commutative_algebra_freyd_kernel_compatibility.lp': '595a58383727e8cb8507fb132e5080ef3ef849aa95f4419fdfe29fb4f896fc3f',
 'emdash3_2_commutative_algebra_freyd_kernels.lp': '9a551ef00703c33cc6b94a4eead49b75bb3764720776155ef328e568380d58f2',
 'emdash3_2_commutative_algebra_freyd_selected_kernel_embedding.lp': '3c67e27ce4d0dfdadf84c9124ca5d2560043ae91b94ebce24557369ddda1a05b',
 'emdash3_2_commutative_algebra_freyd_selected_kernel_lifting.lp': '183bb7c5ecc36e5dfe4561fb76ec9065f01c8501406177b4f0546dc252eac3d1',
 'emdash3_2_commutative_algebra_freyd_selected_kernel_uniqueness.lp': '47de85150e96ba94a1ea448ece80cbf94eb0bcd87f2380805c862a0e513dbcce',
 'emdash3_2_commutative_algebra_freyd_witnessed_preabelian.lp': '80a493b2cd59289684ef4e65a45d15613a337bee84b18ee44362be81ab009305',
 'examples/commutative_ring_freyd_cokernels.lp': '291a11fc388d0ba77b1027a36cf3316394ab1b5fa2d42f9737d937e6a93abb0e',
 'examples/commutative_ring_freyd_kernel_choices.lp': '1eae53b2257a244a19b56ffbdb33528d86c0acd8bda879db085420493ea064a7',
 'examples/commutative_ring_freyd_kernels.lp': '1bcd987f187bc5bd7c67dec89ab9a64f1ce7d530b4868c2de395d0050ea0e0df',
 'examples/commutative_ring_freyd_selected_kernel_embedding.lp': '7ffd5a9d192ad097f19961c259927a82dd5c5b17662a657d4f0e26200ccddc73',
 'examples/commutative_ring_freyd_selected_kernel_lifting.lp': 'edb2619dc55e0ec6788aee59af4ccccba5bed430a2c4cc421c241f42dcf07069',
 'examples/commutative_ring_freyd_selected_kernel_uniqueness.lp': '231615a2944ed3f76309551bfcc737265933df09a495a8994d39c5a379179a14',
 'examples/commutative_ring_freyd_witnessed_preabelian.lp': '0671c9617be06c085f847838e3cb56880c108584402a8635592a252c6179d802',
 'examples/computational_weak_pullbacks.lp': '8bb29919c09453d1ef14a918edfbb26b7fee32d863a022a024e9749c6c0ce0e1'}

def migrate_freyd_witnessed_kernel_consumer(name, original):
    if name not in SOURCES:
        return None
    assert hashlib.sha256(original.encode()).hexdigest() == SOURCES[name], name
    return original
