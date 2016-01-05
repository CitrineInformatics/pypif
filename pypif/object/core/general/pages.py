from pypif.object.core.general.pio import Pio


class Pages(Pio):
    """
    Start and end pages for a reference.
    """

    def __init__(self, start=None, end=None, **kwargs):
        """
        Constructor.

        :param start: String with the starting page.
        :param end: String with the ending page.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Pages, self).__init__(**kwargs)
        self.start = start
        self.end = end
