from pypif.object.core.general.pio import Pio
from pypif.object.core.general.scalar import Scalar


class Value(Pio):
    """
    Information about a scalar, vector, or matrix, or a list of one of those.
    """

    def __init__(self, name=None, scalars=None, vectors=None, matrices=None, units=None, **kwargs):
        """
        Constructor.

        :param name: Name of the value.
        :param scalars: One or more Scalar objects.
        :param vectors: One or more lists of Scalar objects, each representing a vector.
        :param matrices: One of more lists of lists of Scalar objects, each representing a matrix with rows as the
        innermost lists.
        :param units: String with the units of the value.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Value, self).__init__(**kwargs)
        self._scalars = None
        self._vectors = None
        self._matrices = None
        self.name = name
        self.scalars = scalars
        self.vectors = vectors
        self.matrices = matrices
        self.units = units

    @property
    def scalars(self):
        return self._scalars

    @scalars.setter
    def scalars(self, value):
        self._scalars = self._get_object(Scalar, value)

    @scalars.deleter
    def scalars(self):
        del self._scalars

    @property
    def vectors(self):
        return self._vectors

    @vectors.setter
    def vectors(self, value):
        self._vectors = self._get_object(Scalar, value)

    @vectors.deleter
    def vectors(self):
        del self._vectors

    @property
    def matrices(self):
        return self._matrices

    @matrices.setter
    def matrices(self, value):
        self._matrices = self._get_object(Scalar, value)

    @matrices.deleter
    def matrices(self):
        del self._matrices
