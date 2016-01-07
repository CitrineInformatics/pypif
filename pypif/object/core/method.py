from pypif.object.core.instrument import Instrument
from pypif.object.core.software import Software

from pypif.object.core.pio import Pio


class Method(Pio):
    """
    Information about a method used in obtaining a property value.
    """

    def __init__(self, name=None, instruments=None, software=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the method.
        :param instruments: List of :class:`.Instrument` objects used in the method.
        :param software: List of :class:`.Software` objects used in the method.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Method, self).__init__(**kwargs)

        # These members have explicit setters and getters
        self._instruments = None
        self._software = None

        # Set the values for this object
        self.name = name
        self.instruments = instruments
        self.software = software

    @property
    def instruments(self):
        return self._instruments

    @instruments.setter
    def instruments(self, value):
        self._instruments = self._get_object(Instrument, value)

    @instruments.deleter
    def instruments(self):
        del self._instruments

    @property
    def software(self):
        return self._software

    @software.setter
    def software(self, value):
        self._software = self._get_object(Software, value)

    @software.deleter
    def software(self):
        del self._software
