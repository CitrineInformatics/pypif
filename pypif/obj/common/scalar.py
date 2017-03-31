import numbers
from six import string_types
from pypif.obj.common.pio import Pio


class Scalar(Pio):
    """
    Representation of a single scalar value that could represent an absolute point, an uncertain point,
    a range of values, a minimum, or a maximum.
    """

    def __init__(self, value=None, minimum=None, inclusive_minimum=None, maximum=None, inclusive_maximum=None,
                 uncertainty=None, approximate=None, tags=None, **kwargs):
        """
        Constructor.

        :param value: String or number with the value for the point.
        :param minimum: String or number with the minimum value for the point.
        :apram inclusive_minimum: Boolean with whether the minimum is inclusive.
        :param maximum: String or number with the maximum value for the point.
        :param inclusive_maximum: Boolean with whether the maximum is inclusive.
        :param uncertainty: String or number with the  isotropic uncertainty for the point.
        :param approximate: Boolean with whether the value is approximate.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Scalar, self).__init__(tags=tags, **kwargs)
        self._value = None
        self.value = value
        self._minimum = None
        self.minimum = minimum
        self._inclusive_minimum = None
        self.inclusive_minimum = inclusive_minimum
        self._maximum = None
        self.maximum = maximum
        self._inclusive_maximum = None
        self.inclusive_maximum = inclusive_maximum
        self._uncertainty = None
        self.uncertainty = uncertainty
        self._approximate = None
        self.approximate = approximate

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._validate_type('value', value, string_types, numbers.Number)
        self._value = value

    @value.deleter
    def value(self):
        self._value = None

    @property
    def minimum(self):
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        self._validate_type('minimum', minimum, string_types, numbers.Number)
        self._minimum = minimum

    @minimum.deleter
    def minimum(self):
        self._minimum = None

    @property
    def inclusive_minimum(self):
        return self._inclusive_minimum

    @inclusive_minimum.setter
    def inclusive_minimum(self, inclusive_minimum):
        self._validate_type('inclusive_minimum', inclusive_minimum, bool)
        self._inclusive_minimum = inclusive_minimum
    
    @inclusive_minimum.deleter
    def inclusive_minimum(self):
        self._inclusive_minimum = None

    @property
    def maximum(self):
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        self._validate_type('maximum', maximum, string_types, numbers.Number)
        self._maximum = maximum

    @maximum.deleter
    def maximum(self):
        self._maximum = None

    @property
    def inclusive_maximum(self):
        return self._inclusive_maximum

    @inclusive_maximum.setter
    def inclusive_maximum(self, inclusive_maximum):
        self._validate_type('inclusive_maximum', inclusive_maximum, bool)
        self._inclusive_maximum = inclusive_maximum

    @inclusive_maximum.deleter
    def inclusive_maximum(self):
        self._inclusive_maximum = None

    @property
    def uncertainty(self):
        return self._uncertainty

    @uncertainty.setter
    def uncertainty(self, uncertainty):
        self._validate_type('uncertainty', uncertainty, string_types, numbers.Number)
        self._uncertainty = uncertainty

    @uncertainty.deleter
    def uncertainty(self):
        self._uncertainty = None

    @property
    def approximate(self):
        return self._approximate

    @approximate.setter
    def approximate(self, approximate):
        self._validate_type('approximate', approximate, bool)
        self._approximate = approximate

    @approximate.deleter
    def approximate(self):
        self._approximate = None
