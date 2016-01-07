from pypif.object.core.general.pio import Pio


class Id(Pio):
    """
    Information about a generic identifier.
    """

    def __init__(self, name=None, value=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the identifier.
        :param value: String with the value of the identifier.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Id, self).__init__(**kwargs)
        self.name = name
        self.value = value
