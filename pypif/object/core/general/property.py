from pypif.object.value import Value


class Property(Value):
    """
    Class to store information about a property and conditions under which it exists.
    """

    def __init__(self, name=None, scalar=None, vector=None, matrix=None, units=None, condition=None, method=None,
                 data_type=None, reference=None, contact=None, license=None, **kwargs):
        """
        Constructor.

        :param name:
        :param scalar:
        :param vector:
        :param matrix:
        :param units:
        :param condition:
        :param method:
        :param data_type:
        :param reference:
        :param contact:
        :param license:
        :param kwargs:
        """
        super(Property, self).__init__(**kwargs)
