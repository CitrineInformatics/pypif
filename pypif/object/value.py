from pypif.object.core.general.pio import Pio
from scalar import Scalar


class Value(Pio):
    """
    Class to store information about the name, value, and units of some value.
    """

    def __init__(self, name=None, scalar=None, vector=None, matrix=None, units=None, **kwargs):
        """
        Constructor.

        :param name: Name of the value.
        :param scalar: One or more Scalar objects.
        :param vector: One or more lists of Scalar objects, each representing a vector.
        :param matrix: One of more lists of lists of Scalar objects, each representing a matrix with rows as the
        innermost lists.
        :param units: String with the units of the value.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Value, self).__init__(**kwargs)
        self._scalar = None
        self._vector = None
        self._matrix = None
        self.name = name
        self.scalar = scalar
        self.vector = vector
        self.matrix = matrix
        self.units = units

    @property
    def scalar(self):
        return self._scalar

    @scalar.setter
    def scalar(self, value):
        self._scalar = self._get_object(Scalar, value)

    @scalar.deleter
    def scalar(self):
        del self._scalar

    @property
    def vector(self):
        return self._vector

    @vector.setter
    def vector(self, value):
        self._vector = self._get_object(Scalar, value)

    @vector.deleter
    def vector(self):
        del self._vector

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = self._get_object(Scalar, value)

    @matrix.deleter
    def matrix(self):
        del self._matrix
