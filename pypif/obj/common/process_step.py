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
        :param details: List of :class:`.Value` objects with the
        :param kwargs: Dictionary of field names not supported.
        """
        super(ProcessStep, self).__init__(**kwargs)

        # These are the members that have explicit getters and setters
        self._details = None

        # Set the values for this object
        self.name = name
        self.details = details

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        self._details = self._get_object(Value, value)

    @details.deleter
    def details(self):
        del self._details
