from six import string_types
from pypif.obj.common.pio import Pio


class Source(Pio):
    """
    Information about the source of a system.
    """

    def __init__(self, producer=None, url=None, tags=None, **kwargs):
        """
        Constructor.

        :param producer: String with the name of the producer.
        :param url: String with the URL to the source of the system.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Source, self).__init__(tags=tags, **kwargs)
        self._producer = None
        self.producer = producer
        self._url = None
        self.url = url

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
