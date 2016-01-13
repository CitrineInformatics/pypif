from pypif.obj.common.id import Id
from pypif.obj.common.process_step import ProcessStep
from pypif.obj.common.property import Property
from pypif.obj.common.rcl import Rcl


class System(Rcl):
    """
    Base representation for all systems.
    """

    def __init__(self, names=None, ids=None, properties=None, preparation=None, sub_systems=None, references=None,
                 contacts=None, licenses=None, **kwargs):
        """
        Constructor.

        :param names: List of strings with common names of the system.
        :param ids: List of :class:`.Id` objects that identify the system.
        :param properties: List of :class:`.Property` objects with properties of the system.
        :param preparation: List of :class:`.ProcessStep` objects with the preparation information of the system.
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
        self._preparation = None
        self._sub_systems = None

        # Set the values for this object
        self.names = names
        self.ids = ids
        self.properties = properties
        self.preparation = preparation
        self.sub_systems = sub_systems
        self.category = kwargs['category'] if 'category' in kwargs else 'system'

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
    def preparation(self):
        return self._preparation

    @preparation.setter
    def preparation(self, value):
        self._preparation = self._get_object(ProcessStep, value)

    @preparation.deleter
    def preparation(self):
        del self._preparation

    @property
    def sub_systems(self):
        return self._sub_systems

    @sub_systems.setter
    def sub_systems(self, value):
        self._sub_systems = self._get_object(System, value)

    @sub_systems.deleter
    def sub_systems(self):
        del self._sub_systems
