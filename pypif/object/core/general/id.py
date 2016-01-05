from pypif.object.core.general.pio import Pio


class Id(Pio):
    """
    Class to store information about a generic identifier.
    """

    def __init__(self, name=None, value=None, **kwargs):
        """
        Constructor.

        :param name: Name of the identifier.
        :param value: Value of the identifier.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Id, self).__init__(**kwargs)
        self.name = name
        self.value = value
