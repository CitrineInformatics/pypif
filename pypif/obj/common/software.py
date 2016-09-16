from six import string_types
from pypif.obj.common.pio import Pio


class Software(Pio):
    """
    Information about a software application.
    """

    def __init__(self, name=None, version=None, producer=None, url=None, tags=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the software.
        :param version: String with the version of the software.
        :param producer: String with the name of the producer of the software.
        :param url: URL to the software website.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Software, self).__init__(tags=tags, **kwargs)
        self._name = None
        self.name = name
        self._version = None
        self.version = version
        self._producer = None
        self.producer = producer
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
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        self._validate_type('version', version, string_types)
        self._version = version

    @version.deleter
    def version(self):
        self._version = None

    @property
    def producer(self):
        return self._producer

    @producer.setter
    def producer(self, producer):
        self._validate_type('producer', producer, string_types)
        self._producer = producer

    @producer.deleter
    def producer(self):
        self._producer = None

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
