import json

import numpy as np


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
        if obj is None:
            return []
        elif isinstance(obj, list):
            return [i.as_dictionary() for i in obj]
        elif hasattr(obj, 'as_dictionary'):
            return obj.as_dictionary()
        elif isinstance(obj, (np.int_, np.intc, np.intp, np.int8, np.int16, np.int32,
                              np.int64, np.uint8, np.uint16, np.uint32, np.uint64)):
            return int(obj)
        elif isinstance(obj, (np.float_, np.float16, np.float32, np.float64)):
            return float(obj)
        return json.JSONEncoder.default(self, obj)
