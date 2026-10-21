"""Original constant-chain and native row-zero profile migration; no new rules."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {'emdash3_2_commutative_algebra_freyd_native_row_zeros.lp': ('e1f68219467f2e32f98c005a0acc2cc7333dad3e48f99b2d48615b61031891c6',
                                                             'production_freyd_row_zeros.lpfragment'),
 'emdash3_2_one_cat_constant_chain_zeros.lp': ('99ff7f3927c7fcf0f4ee8b79d8d5fda192854333b234cd6533573f6fd7055b30',
                                               'production_constant_chain_zeros.lpfragment'),
 'examples/one_cat_constant_chain_zeros.lp': ('51ab599a539874539c8237d01dbb1f5fcad656348363059b04b01d79f0bcf23c',
                                              'production_constant_chain_reviewer.lpfragment')}


def finish_constant_chain(path, text):
    if path not in SOURCES:
        return None
    pin, fragment = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == pin, path
    return (AUDIT / fragment).read_text()
