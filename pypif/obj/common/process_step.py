from six import string_types
from pypif.obj.common.pio import Pio
from pypif.obj.common.value import Value
from pypif.obj.common.software import Software
from pypif.obj.common.instrument import Instrument


class ProcessStep(Pio):
    """
    Information about a single step in a processing pipeline.
    """

    def __init__(self, name=None, details=None, instruments=None, software=None, tags=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the process step.
        :param details: List of dictionaries or :class:`.Value` objects with the details of the step.
        :param instruments: List of dictionaries or :class:`.Instrument` objects.
        :param software: List of dictionaries or :class:`.Software` objects.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(ProcessStep, self).__init__(tags=tags, **kwargs)
        self._name = None
        self.name = name
        self._details = None
        self.details = details
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

    @name.deleter
    def name(self):
        self._name = None

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        self._validate_list_type('details', details, dict, Value)
        self._details = self._get_object(Value, details)

    @details.deleter
    def details(self):
        self._details = None

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
