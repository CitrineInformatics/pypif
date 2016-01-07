from pypif.object.core.general.pio import Pio


class Software(Pio):
    """
    Information about a software application.
    """

    def __init__(self, name=None, version=None, producer=None, url=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the software.
        :param version: String with the version of the software.
        :param producer: String with the name of the producer of the software.
        :param url: URL to the software website.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Software, self).__init__(**kwargs)
        self.name = name
        self.version = version
        self.producer = producer
        self.url = url
