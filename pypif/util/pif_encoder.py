import json
from pypif.util.case import to_snake_case


class PifEncoder(json.JSONEncoder):
    """
    Class to convert physical information objects to json.
    """

    def default(self, obj):
        """
        Convert an object to a form ready to dump to json.

        :param obj: Object being serialized. The type of this object must be one of the following: None; a single
        object derived from the Pio class; or a list of objects, each derived from the Pio class.
        :return: List of dictionaries, each representing a physical information object, ready to be serialized.
        """
        mod_obj = [] if obj is None else obj if isinstance(obj, list) else [obj]
        return [{to_snake_case(i.__class__.__name__): i.as_pif_dictionary()} for i in mod_obj]
