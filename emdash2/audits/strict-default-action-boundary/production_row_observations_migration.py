"""Original whole row cancellation and zero-cone observation migration."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {'emdash3_2_one_cat_short_exact_family_cancellation.lp': ('cc420bf24b159c9e4002f245b7b1fa2af2a51102af7ae44e06c4ace6e55691dc',
                                                          'production_row_cancellation.lpfragment'),
 'emdash3_2_one_cat_zero_cone_row_families.lp': ('d23eba56d01ab9b187da75366743694294b9b3c04adbe0d92c968837df13e55d',
                                                 'production_zero_cone_rows.lpfragment'),
 'examples/one_cat_short_exact_family_cancellation.lp': ('49db3ea16a89c25884c1171a51394f3cd6e338f270514d40ac79ae36c64e4227',
                                                         'production_row_cancellation_reviewer.lpfragment')}


def finish_row_observations(path, text):
    if path not in SOURCES:
        return None
    pin, fragment = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == pin, path
    return (AUDIT / fragment).read_text()
