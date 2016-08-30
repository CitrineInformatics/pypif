from pypif.util.case import to_camel_case


class Serializable(object):
    """
    Base class for objects that can be serialized.
    """

    def as_dictionary(self):
        """
        Convert this object to a dictionary with formatting appropriate for a PIF.

        :returns: Dictionary with the content of this object formatted for a PIF.
        """
        return {to_camel_case(i): Serializable._convert_to_dictionary(self.__dict__[i])
                for i in self.__dict__ if self.__dict__[i] is not None}

    @staticmethod
    def _convert_to_dictionary(obj):
        """
        Convert obj to a dictionary with formatting appropriate for a PIF. This function attempts to treat obj as
        a Pio object and otherwise returns obj.

        :param obj: Object to convert to a dictionary.
        :returns: Input object as a dictionary or the original object.
        """
        if isinstance(obj, list):
            return [Serializable._convert_to_dictionary(i) for i in obj]
        elif hasattr(obj, 'as_dictionary'):
            return obj.as_dictionary()
        else:
            return obj