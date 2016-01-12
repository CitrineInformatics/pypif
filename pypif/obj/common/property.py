from pypif.obj.common.method import Method
from pypif.obj.common.rcl import Rcl
from pypif.obj.common.value import Value


class Property(Value, Rcl):
    """
    Class to store information about a property and conditions under which it exists.
    """

    def __init__(self, name=None, scalars=None, vectors=None, matrices=None, units=None, conditions=None, method=None,
                 data_type=None, references=None, contacts=None, licenses=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the property.
        :param scalars: One or more Scalar objects.
        :param vectors: One or more lists of Scalar objects, each representing a vector.
        :param matrices: One of more lists of lists of Scalar objects, each representing a matrix with rows as the
        innermost lists.
        :param units: String with the units of the property.
        :param conditions: List of :class:`.Value` objects with the conditions at which the property exists.
        :param method: :class:`.Method` object describing the method used to get the property value.
        :param data_type: String set to either "Experimental" or "Computational" to set the broad category of data.
        :param references: List of :class:`.Reference` objects where information about the property is published.
        :param contacts: List of :class:`.Person` objects with people to contact for information about the property.
        :param licenses: List of :class:`.License` objects with licensing information for data about the property.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Property, self).__init__(name=name, scalars=scalars, vectors=vectors, matrices=matrices,
                                       units=units, **kwargs)
        super(Rcl, self).__init__(references=references, contacts=contacts, licenses=licenses)

        # These members have explicit setters and getters
        self._conditions = None
        self._method = None

        # Set the values for this object
        self.conditions = conditions
        self.method = method
        self.data_type = data_type

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        self._method = self._get_object(Method, value)

    @method.deleter
    def method(self):
        del self._method

    @property
    def conditions(self):
        return self._conditions

    @conditions.setter
    def conditions(self, value):
        self._conditions = self._get_object(Value, value)

    @conditions.deleter
    def conditions(self):
        del self._conditions
