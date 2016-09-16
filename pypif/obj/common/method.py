from six import string_types
from pypif.obj.common.instrument import Instrument
from pypif.obj.common.pio import Pio
from pypif.obj.common.software import Software


class Method(Pio):
    """
    Information about a method used in obtaining a property value.
    """

    def __init__(self, name=None, instruments=None, software=None, tags=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the method.
        :param instruments: List of dictionaries or :class:`.Instrument` objects used in the method.
        :param software: List of dictionaries or :class:`.Software` objects used in the method.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Method, self).__init__(tags=tags, **kwargs)
        self._name = None
        self.name = name
        self._instruments = None
        self.instruments = instruments
        self._software = None
        self.software = software

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._validate_type('name', name, string_types)
        self._name = name

    @property
    def instruments(self):
        return self._instruments

    @instruments.setter
    def instruments(self, instruments):
        self._validate_list_type('instruments', instruments, dict, Instrument)
        self._instruments = self._get_object(Instrument, instruments)

    @instruments.deleter
    def instruments(self):
        self._instruments = None

    @property
    def software(self):
        return self._software

    @software.setter
    def software(self, software):
        self._validate_list_type('software', software, dict, Software)
        self._software = self._get_object(Software, software)

    @software.deleter
    def software(self):
        self._software = None
