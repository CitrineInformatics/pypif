import numbers
from six import string_types
from pypif.obj.common.pio import Pio


class Id(Pio):
    """
    Information about a generic identifier.
    """

    def __init__(self, name=None, value=None, tags=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the identifier.
        :param value: String or number with the value of the identifier.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Id, self).__init__(tags=tags, **kwargs)
        self._name = None
        self.name = name
        self._value = None
        self.value = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._validate_type('name', name, string_types)
        self._name = name

    @name.deleter
    def name(self):
        self._name = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._validate_list_type('value', value, string_types, numbers.Number)
        self._value = value

    @value.deleter
    def value(self):
        self._value = None
