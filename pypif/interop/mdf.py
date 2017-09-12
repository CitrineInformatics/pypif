from pypif.util.read_view import ReadView
from json import dumps


def pif_to_mdf_metadata(pif):
   """Convert a PIF into partial MDF record"""
   res = {}
   res["{source_name}"] = _to_user_defined(pif)
   return dumps(res)


def _to_user_defined(pif):
    """Read the systems in the PIF to populate the user-defined portion"""
    rv = ReadView(pif)
    res = {}
    for k in rv.keys():
        res[k] = rv[k].scalars[0].value
    return res 
