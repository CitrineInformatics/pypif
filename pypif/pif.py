import json

from pypif.obj import *
from pypif.util.case import keys_to_snake_case
from pypif.util.pif_encoder import PifEncoder


def dump(pif, fp, **kwargs):
    """
    Convert a single Physical Information Object, or a list of such objects, into a JSON-encoded text file.

    :param pif: Object or list of objects to serialize.
    :param fp: File-like object supporting .write() method to write the serialized object(s) to.
    :param kwargs: Any options available to json.dump().
    """
    return json.dump(pif, fp, cls=PifEncoder, **kwargs)


def dumps(pif, **kwargs):
    """
    Convert a single Physical Information Object, or a list of such objects, into a JSON-encoded string.

    :param pif: Object or list of objects to serialize.
    :param kwargs: Any options available to json.dumps().
    """
    return json.dumps(pif, cls=PifEncoder, **kwargs)


def load(fp, **kwargs):
    """
    Convert content in a JSON-encoded text file to a Physical Information Object or a list of such objects.

    :param fp: File-like object supporting .read() method to deserialize from.
    :param kwargs: Any options available to json.load().
    :return: Single object derived from :class:`.Pio` or a list of such object.
    """
    return loado(json.load(fp, **kwargs))


def loads(s, **kwargs):
    """
    Convert content in a JSON-encoded string to a Physical Information Object or a list of such objects.

    :param s: String to deserialize.
    :param kwargs: Any options available to json.loads().
    :return: Single object derived from :class:`.Pio` or a list of such object.
    """
    return loado(json.loads(s, **kwargs))


def loado(obj):
    """
    Convert a dictionary or a list of dictionaries into a single Physical Information Object or a list of such objects.

    :param obj: Dictionary or list to convert to Physical Information Objects.
    :return: Single object derived from :class:`.Pio` or a list of such object.
    """
    if isinstance(obj, list):
        return [_dict_to_pio(i) for i in obj]
    elif isinstance(obj, dict):
        return _dict_to_pio(obj)
    else:
        raise ValueError('expecting list or dictionary as outermost structure')


def _dict_to_pio(d):
    """
    Convert a single dictionary object to a Physical Information Object.

    :param d: Dictionary to convert.
    :return: Single object derived from :class:`.Pio`.
    """
    d = keys_to_snake_case(d)
    if 'category' not in d:
        raise ValueError('Dictionary does not contains a category field: ' + ', '.join(d.keys()))
    elif d['category'] == 'system':
        return System(**d)
    elif d['category'] == 'system.chemical':
        return ChemicalSystem(**d)
    elif d['category'] == 'system.chemical.alloy':
        return Alloy(**d)
    elif d['category'] == 'system.chemical.alloy.phase':  # Legacy support
        return ChemicalSystem(**d)
    raise ValueError('Dictionary does not contain a valid top-level category: ' + str(d['category']))
