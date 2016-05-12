import numbers
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
        :param ids: List of dictionaries, strings, numbers, or :class:`.Id` objects that identify the system.
        :param properties: List of dictionaries or :class:`.Property` objects with properties of the system.
        :param preparation: List of dictionaries or :class:`.ProcessStep` objects with the preparation
                information of the system.
        :param sub_systems: List of dictionaries or :class:`.System` objects with the subsystems of the system.
        :param references: List of dictionaries or :class:`.Reference` objects where information about the system
                is published.
        :param contacts: List of dictionaries, strings, or :class:`.Person` objects with people to contact for
                information about the system.
        :param licenses: List of dictionaries, strings, or :class:`.License` objects with licensing information
                for data about the system.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(System, self).__init__(references=references, contacts=contacts, licenses=licenses, **kwargs)
        self._names = None
        self.names = names
        self._ids = None
        self.ids = ids
        self._properties = None
        self.properties = properties
        self._preparation = None
        self.preparation = preparation
        self._sub_systems = None
        self.sub_systems = sub_systems
        self.category = kwargs['category'] if 'category' in kwargs else 'system'

    @property
    def names(self):
        return self._names

    @names.setter
    def names(self, names):
        self._validate_list_type('names', names, basestring)
        self._names = names

    @names.deleter
    def names(self):
        self._names = None

    @property
    def ids(self):
        return self._ids

    @ids.setter
    def ids(self, ids):
        self._validate_list_type('ids', ids, dict, basestring, numbers.Number, Id)
        self._ids = self._get_object(Id, ids)

    @ids.deleter
    def ids(self):
        self._ids = None

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, properties):
        self._validate_list_type('properties', properties, dict, Property)
        self._properties = self._get_object(Property, properties)

    @properties.deleter
    def properties(self):
        self._properties = None

    @property
    def preparation(self):
        return self._preparation

    @preparation.setter
    def preparation(self, preparation):
        self._validate_list_type('preparation', preparation, dict, ProcessStep)
        self._preparation = self._get_object(ProcessStep, preparation)

    @preparation.deleter
    def preparation(self):
        self._preparation = None

    @property
    def sub_systems(self):
        return self._sub_systems

    @sub_systems.setter
    def sub_systems(self, sub_systems):
        self._validate_list_type('sub_systems', sub_systems, dict, System)
        self._sub_systems = self._get_object(System, sub_systems)

    @sub_systems.deleter
    def sub_systems(self):
        self._sub_systems = None
