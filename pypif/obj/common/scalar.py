from pypif.obj.common.pio import Pio


class Scalar(Pio):
    """
    Representation of a single scalar value that could represent an absolute point, an uncertain point,
    a range of values, a minimum, or a maximum.
    """

    def __init__(self, value=None, minimum=None, inclusive_minimum=None, maximum=None, inclusive_maximum=None,
                 uncertainty=None, approximate=None, **kwargs):
        """
        Constructor.

        :param value: Exact value for the point.
        :param minimum: Minimum value for the point.
        :apram inclusive_minimum: Whether the minimum is inclusive.
        :param maximum: Maximum value for the point.
        :param inclusive_maximum: Whether the maximum is inclusive.
        :param uncertainty: Isotropic uncertainty for the point.
        :param approximate: Whether the value is approximate.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Scalar, self).__init__(**kwargs)
        self.value = value
        self.minimum = minimum
        self.inclusive_minimum = inclusive_minimum
        self.maximum = maximum
        self.inclusive_maximum = inclusive_maximum
        self.uncertainty = uncertainty
        self.approximate = approximate
