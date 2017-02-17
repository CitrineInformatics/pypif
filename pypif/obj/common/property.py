from six import string_types
from pypif.obj.common.method import Method
from pypif.obj.common.rcl import Rcl
from pypif.obj.common.value import Value
from warnings import warn


class Property(Value, Rcl):
    """
    Class to store information about a property and conditions under which it exists.
    """

    def __init__(self, name=None, scalars=None, vectors=None, matrices=None, files=None, units=None, conditions=None,
                 methods=None, data_type=None, references=None, contacts=None, licenses=None, tags=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the property.
        :param scalars: One or more dictionaries, strings, numbers, or :class:`.Scalar` objects.
        :param vectors: One or more lists of dictionaries, strings, numbers, or :class:`.Scalar` objects,
                each representing a vector.
        :param matrices: One of more lists of lists of dictionaries, strings, numbers, or :class:`.Scalar` objects,
                each representing a matrix with rows as the innermost lists.
        :param files: One of more dictionaries, strings, or :class:`.FileReference` objects.
        :param units: String with the units of the property.
        :param conditions: List of dictionaries or :class:`.Value` objects with the conditions at which the
                property exists.
        :param methods: List of dictionary or :class:`.Method` object describing the method used to get the property value.
        :param data_type: String containing "EXPERIMENTAL", "COMPUTATIONAL", "FIT", or "MACHINE_LEARNING" to set the
                broad category of data.
        :param references: List of dictionaries or :class:`.Reference` objects where information about the
                property is published.
        :param contacts: List of dictionaries, strings, or :class:`.Person` objects with people to contact for
                information about the property.
        :param licenses: List of dictionaries, strings, or :class:`.License` objects with licensing information
                for the property.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        # The order of the constructors is important here. The second constructor could overwrite values set during
        # the first if there is overlap.
        Value.__init__(self, name=name, scalars=scalars, vectors=vectors, matrices=matrices, files=files,
                       units=units, tags=tags, **kwargs)
        self.references = references
        self.contacts = contacts
        self.licenses = licenses
        self._conditions = None
        self.conditions = conditions
        if 'method' in kwargs:
            self.methods = method
        self._methods = None
        self.methods = methods
        self._data_type = None
        self.data_type = data_type



    @property
    def conditions(self):
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        self._validate_list_type('conditions', conditions, dict, Value)
        self._conditions = self._get_object(Value, conditions)

    @conditions.deleter
    def conditions(self):
        self._conditions = None

    @property
    def method(self):
        warn("method has been deprecated in favor of methods")
        return self._methods

    @method.setter
    def method(self, method):
        warn("method has been deprecated in favor of methods")
        self.methods = method

    @method.deleter
    def method(self):
        warn("method has been deprecated in favor of methods")
        del self.methods

    @property
    def methods(self):
        return self._methods

    @methods.setter
    def methods(self, methods):
        self._validate_list_type('methods', methods, dict, Method)
        self._methods = self._get_object(Method, methods)

    @methods.deleter
    def methods(self):
        self._methods = None

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        self._validate_type('data_type', data_type, string_types)
        self._data_type = data_type

    @data_type.deleter
    def data_type(self):
        self._data_type = None
