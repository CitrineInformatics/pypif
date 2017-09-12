from pypif.util.read_view import ReadView
from json import dumps


def pif_to_mdf_record(pif):
   """Convert a PIF into partial MDF record"""
   res = {}
   res["mdf"] = _to_meta_data(pif)
   res["{source_name}"] = _to_user_defined(pif)
   return dumps(res)


def _to_meta_data(pif):
    """Convert the meta-data from the PIF into MDF"""
    return {}


def _to_user_defined(pif):
    """Read the systems in the PIF to populate the user-defined portion"""
    rv = ReadView(pif)
    res = {}
    for k in rv.keys():
        res[k] = rv[k].scalars[0].value
    return res
