from pypif.obj.common.id import Id
from pypif.obj.common.property import Property
from pypif.obj.common.rcl import Rcl
from pypif.obj.common.value import Value


class System(Rcl):
    """
    Base representation for all systems.
    """

    def __init__(self, categories=None, names=None, ids=None, properties=None, processing=None,
                 sub_systems=None, references=None, contacts=None, licenses=None, **kwargs):
        """
        Constructor.

        :param categories: List of strings with the categories of the system, from broad to specific.
        :param names: List of strings with common names of the system.
        :param ids: List of :class:`.Id` objects that identify the system.
        :param properties: List of :class:`.Property` objects with properties of the system.
        :param processing: List of :class:`.Value` objects with the processing information of the system.
        :param sub_systems: List of :class:`.System` objects with the subsystems of the system.
        :param references: List of :class:`.Reference` objects where information about the system is published.
        :param contacts: List of :class:`.Person` objects with people to contact for information about the system.
        :param licenses: List of :class:`.License` objects with licensing information for data about the system.
        :param kwargs: Dictionary of field names not supported.
        """
        super(System, self).__init__(references=references, contacts=contacts, licenses=licenses, **kwargs)

        # These are the members that have explicit getters and setters
        self._ids = None
        self._properties = None
        self._processing = None
        self._sub_systems = None

        # Set the values for this object
        self.categories = categories
        self.names = names
        self.ids = ids
        self.properties = properties
        self.processing = processing
        self.sub_systems = sub_systems

    @property
    def ids(self):
        return self._ids

    @ids.setter
    def ids(self, value):
        self._ids = self._get_object(Id, value)

    @ids.deleter
    def ids(self):
        del self._ids

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        self._properties = self._get_object(Property, value)

    @properties.deleter
    def properties(self):
        del self._properties

    @property
    def processing(self):
        return self._processing

    @processing.setter
    def processing(self, value):
        self._processing = self._get_object(Value, value)

    @processing.deleter
    def processing(self):
        del self._processing

    @property
    def sub_systems(self):
        return self._sub_systems

    @sub_systems.setter
    def sub_systems(self, value):
        self._sub_systems = self._get_object(System, value)

    @sub_systems.deleter
    def sub_systems(self):
        del self._sub_systems
