import numbers
from six import string_types
from pypif.obj.common.pio import Pio
from pypif.obj.common.scalar import Scalar


class Value(Pio):
    """
    Information about a scalar, vector, or matrix, or a list of one of those.
    """

    def __init__(self, name=None, scalars=None, vectors=None, matrices=None, units=None, tags=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the value.
        :param scalars: One or more dictionaries, strings, numbers, or :class:`.Scalar` objects.
        :param vectors: One or more lists of dictionaries, strings, numbers, or :class:`.Scalar` objects,
                each representing a vector.
        :param matrices: One of more lists of lists of dictionaries, strings, numbers, or :class:`.Scalar` objects,
                each representing a matrix with rows as the innermost lists.
        :param units: String with the units of the value.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Value, self).__init__(tags=tags, **kwargs)
        self._name = None
        self.name = name
        self._scalars = None
        self.scalars = scalars
        self._vectors = None
        self.vectors = vectors
        self._matrices = None
        self.matrices = matrices
        self._units = None
        self.units = units

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
    def scalars(self):
        return self._scalars

    @scalars.setter
    def scalars(self, scalars):
        self._validate_list_type('scalars', scalars, dict, string_types, numbers.Number, Scalar)
        self._scalars = self._get_object(Scalar, scalars)

    @scalars.deleter
    def scalars(self):
        self._scalars = None

    @property
    def vectors(self):
        return self._vectors

    @vectors.setter
    def vectors(self, vectors):
        self._validate_nested_list_type('vectors', vectors, 2, dict, string_types, numbers.Number, Scalar)
        self._vectors = self._get_object(Scalar, vectors)

    @vectors.deleter
    def vectors(self):
        self._vectors = None

    @property
    def matrices(self):
        return self._matrices

    @matrices.setter
    def matrices(self, matrices):
        self._validate_nested_list_type('matrices', matrices, 3, dict, string_types, numbers.Number, Scalar)
        self._matrices = self._get_object(Scalar, matrices)

    @matrices.deleter
    def matrices(self):
        self._matrices = None

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, units):
        self._validate_type('units', units, string_types)
        self._units = units

    @units.deleter
    def units(self):
        self._units = None
