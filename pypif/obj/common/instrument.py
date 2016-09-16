from six import string_types
from pypif.obj.common.pio import Pio


class Instrument(Pio):
    """
    Information about an instrument used to take a measurement.
    """

    def __init__(self, name=None, model=None, producer=None, url=None, tags=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the instrument.
        :param model: String with the model of the instrument.
        :param producer: String with the name of the producer of the instrument.
        :param url: URL to the instrument website.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Instrument, self).__init__(tags=tags, **kwargs)
        self._name = None
        self.name = name
        self._model = None
        self.model = model
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
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._validate_type('model', model, string_types)
        self._model = model

    @model.deleter
    def model(self):
        self._model = None

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
