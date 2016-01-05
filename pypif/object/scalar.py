from pypif.object.core.general.pio import Pio


class Scalar(Pio):
    """
    Class to store information about a single scalar value that could represent an absolute point, an uncertain point,
    a range of values, a minimum, or a maximum.
    """

    def __init__(self, value=None, minimum=None, maximum=None, uncertainty=None, **kwargs):
        """
        Constructor.

        :param value: Exact value for the point.
        :param minimum: Minimum value for the point.
        :param maximum: Maximum value for the point.
        :param uncertainty: Isotropic uncertainty for the point.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Scalar, self).__init__(**kwargs)
        self.value = value
        self.minimum = minimum
        self.maximum = maximum
        self.uncertainty = uncertainty
