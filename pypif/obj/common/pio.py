import numbers
from six import string_types
from pypif.util.serializable import Serializable


class Pio(Serializable):
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
        self._validate_list_type('tags', tags, string_types, numbers.Number)
        self._tags = tags

    @tags.deleter
    def tags(self):
        self._tags = None

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
                        '. Must be equal to None or one of the following types: ' + str(args))

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
                        '. Must be one of the following types: ' + str(args))

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
            for sub_obj in obj:
                self._validate_nested_list_type(name, sub_obj, nested_level - 1, *args)
