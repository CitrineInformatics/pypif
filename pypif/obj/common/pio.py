import numbers
from pypif.util.case import to_camel_case
from pypif.util.case import keys_to_snake_case


class Pio(object):
    """
    Base class for all physical information objects.
    """

    def __init__(self, tags=None, **kwargs):
        """
        Constructor. This is used to set an fields on a pio that do not have first level support.

        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of field names to values.
        """
        self._tags = None
        self.tags = tags
        for i in kwargs.keys():
            setattr(self, i, kwargs[i])

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags):
        self._validate_list_type('tags', tags, basestring, numbers.Number)
        self._tags = tags

    @tags.deleter
    def tags(self):
        self._tags = None

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

    def _validate_type(self, name, obj, *args):
        """
        Helper function that checks the input object type against each in a list of classes. This function
        also allows the input value to be equal to None.

        :param name: Name of the object.
        :param obj: Object to check the type of.
        :param args: List of classes.
        :raises TypeError: if the input object is not of any of the allowed types.
        """
        if obj is None:
            return
        for arg in args:
            if isinstance(obj, arg):
                return
        raise TypeError(self.__class__.__name__ + '.' + name + ' is of type ' + type(obj).__name__ +
                        '. Must be equal to None or one of the following types: ' +
                        ', '.join([arg.__name__ for arg in args]))

    def _validate_type_not_null(self, name, obj, *args):
        """
        Helper function that checks the input object type against each in a list of classes.

        :param name: Name of the object.
        :param obj: Object to check the type of.
        :param args: List of classes.
        :raises TypeError: if the input object is not of any of the allowed types.
        """
        for arg in args:
            if isinstance(obj, arg):
                return
        raise TypeError(self.__class__.__name__ + '.' + name + ' is of type ' + type(obj).__name__ +
                        '. Must be one of the following types [' +
                        ', '.join([arg.__name__ for arg in args]) + ']')

    def _validate_list_type(self, name, obj, *args):
        """
        Helper function that checks the input object type against each in a list of classes, or if the input object
        is a list, each value that it contains against that list.

        :param name: Name of the object.
        :param obj: Object to check the type of.
        :param args: List of classes.
        :raises TypeError: if the input object is not of any of the allowed types.
        """
        if obj is None:
            return
        if isinstance(obj, list):
            for i in obj:
                self._validate_type_not_null(name,  i, *args)
        else:
            self._validate_type(name, obj, *args)

    def _validate_nested_list_type(self, name, obj, nested_level, *args):
        """
        Helper function that checks the input object as a list then recursively until nested_level is 1.

        :param name: Name of the object.
        :param obj: Object to check the type of.
        :param nested_level: Integer with the current nested level.
        :param args: List of classes.
        :raises TypeError: if the input object is not of any of the allowed types.
        """
        if nested_level <= 1:
            self._validate_list_type(name, obj, *args)
        else:
            if obj is None:
                return
            if not isinstance(obj, list):
                raise TypeError(self.__class__.__name__ + '.' + name + ' contains value of type ' +
                                type(obj).__name__ + ' where a list is expected')
            self._validate_nested_list_type(name, obj, nested_level - 1, *args)
