from pypif.obj.common.pio import Pio
from pypif.obj.common.value import Value


class ProcessStep(Pio):
    """
    Information about a single step in a processing pipeline.
    """

    def __init__(self, name=None, details=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the process step.
        :param details: List of dictionaries or :class:`.Value` objects with the details of the step.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(ProcessStep, self).__init__(**kwargs)
        self._name = None
        self.name = name
        self._details = None
        self.details = details

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._validate_type('name', name, basestring)
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
