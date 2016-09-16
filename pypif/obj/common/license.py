from six import string_types
from pypif.obj.common.pio import Pio


class License(Pio):
    """
    Information about a license that applies to some item.
    """

    def __init__(self, name=None, description=None, url=None, tags=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the license.
        :param description: String with the description of the license.
        :param url: String with the URL to the license.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(License, self).__init__(tags=tags, **kwargs)
        self._name = None
        self.name = name
        self._description = None
        self.description = description
        self._url = None
        self.url = url

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
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._validate_type('description', description, string_types)
        self._description = description

    @description.deleter
    def description(self):
        self._description = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._validate_type('url', url, string_types)
        self._url = url

    @url.deleter
    def url(self):
        self._url = None
