from pypif.util.case import to_camel_case
from pypif.util.case import keys_to_snake_case


class Pio(object):
    """
    Base class for all physical information objects.
    """

    def __init__(self, **kwargs):
        """
        Constructor. This is used to set an fields on a pio that do not have first level support.

        :param kwargs: Dictionary of field names to values.
        """
        for i in kwargs.keys():
            setattr(self, i, kwargs[i])

    def as_pif_dictionary(self):
        """
        Convert this object to a dictionary with formatting appropriate for a PIF.

        :returns: Dictionary with the content of this object formatted for a PIF.
        """
        return {to_camel_case(i): Pio._convert_to_pif_dictionary(self.__dict__[i])
                for i in self.__dict__ if self.__dict__[i] is not None}

    @staticmethod
    def _convert_to_pif_dictionary(obj):
        """
        Convert obj to a dictionary with formatting appropriate for a PIF. This function attempts to treat obj as
        a Pio object and otherwise returns obj.

        :param obj: Object to convert to a dictionary.
        :returns: Input object as a dictionary or the original object.
        """
        if isinstance(obj, list):
            return [Pio._convert_to_pif_dictionary(i) for i in obj]
        elif hasattr(obj, 'as_pif_dictionary'):
            return obj.as_pif_dictionary()
        else:
            return obj

    @staticmethod
    def _get_object(class_, obj):
        """
        Helper function that returns an object, or if it is a dictionary, initializes it from class_.

        :param class_: Class to use to instantiate object.
        :param obj: Object to process.
        :return: One or more objects.
        """
        if isinstance(obj, list):
            return [Pio._get_object(class_, i) for i in obj]
        elif isinstance(obj, dict):
            return class_(**keys_to_snake_case(obj))
        else:
            return obj
