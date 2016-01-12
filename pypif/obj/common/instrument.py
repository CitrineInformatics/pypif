from pypif.obj.common.pio import Pio


class Instrument(Pio):
    """
    Information about an instrument used to take a measurement.
    """

    def __init__(self, name=None, model=None, producer=None, url=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the instrument.
        :param model: String with the model of the instrument.
        :param producer: String with the name of the producer of the instrument.
        :param url: URL to the instrument website.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Instrument, self).__init__(**kwargs)
        self.name = name
        self.model = model
        self.producer = producer
        self.url = url
