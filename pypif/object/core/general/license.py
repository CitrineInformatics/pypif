from pypif.object.core.general.pio import Pio


class License(Pio):
    """
    Information about a license.
    """

    def __init__(self, name=None, description=None, url=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the license.
        :param description: String with the description of the license.
        :param url: String with the URL to the license.
        :param kwargs: Dictionary of field names not supported.
        """
        super(License, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.url = url
