"""Original constant-transformation comparison and native Freyd row paths."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {'examples/one_cat_constant_transformation_views.lp': ('8680d08e5a7e417bc26df930bee43c2256856dc512a6f58c10afeaf61e9d4daf', 'production_constant_transformation_reviewer.lpfragment'), 'emdash3_2_commutative_algebra_freyd_native_row_paths.lp': ('02bd35fc8abcebe0908df82f60a80b04e415a4638120be81a1adb86ef15f7030', 'production_freyd_row_paths.lpfragment'), 'emdash3_2_one_cat_constant_transformation_views.lp': ('fbe17f556222d5a532f40ab9b4e938cb43b413f08a7cb428f280cf535b66cf7e', 'production_constant_transformation_views.lpfragment')}


def finish_constant_rows(path, text):
    if path not in SOURCES:
        return None
    pin, fragment = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == pin, path
    return (AUDIT / fragment).read_text()
