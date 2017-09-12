from pypif.util.read_view import ReadView
from pypif.obj.common import Value
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

    # make a read view to flatten the heirarchy
    rv = ReadView(pif)
    res = {}
    # Iterate over the keys in the read view
    for k in rv.keys():
        name, value = _extract_key_value(rv[k].raw)
        # add any objects that can be extracted
        if name and value is not None:
            res[name] = value
    return res


def _extract_key_value(obj):
    """Extract the value from the object and make a descriptive key"""

    # Parse a Value object, which includes Properties
    if isinstance(obj, Value):
        key = obj.name
        value = None
        if obj.scalars and len(obj.scalars) == 1:
            value = obj.scalars[0].value
        elif obj.scalars:
            value =  [x.value for x in obj.scalars]
        elif obj.vectors and len(obj.vectors) == 1:
            value = [x.value for x in obj.vectors[0]]
        
    return key, value

