import numbers
from six import string_types
from pypif.obj.common.id import Id
from pypif.obj.common.process_step import ProcessStep
from pypif.obj.common.property import Property
from pypif.obj.common.quantity import Quantity
from pypif.obj.common.rcl import Rcl
from pypif.obj.common.source import Source


class System(Rcl):
    """
    Base representation for all systems.
    """

    def __init__(self, uid=None, names=None, ids=None, source=None, quantity=None, properties=None, preparation=None,
                 sub_systems=None, references=None, contacts=None, licenses=None, tags=None, **kwargs):
        """
        Constructor.

        :param uid: String with the permanent ID for this record.
        :param names: List of strings with common names of the system.
        :param ids: List of dictionaries, strings, numbers, or :class:`.Id` objects that identify the system.
        :param source: Dictionary, string, or :class:`.Source` object with the source of the system.
        :param quantity: Dictionary or :class:`.Quantity` object with the quantity of the system.
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
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(System, self).__init__(references=references, contacts=contacts, licenses=licenses, tags=tags, **kwargs)
        self._uid = None
        self.uid = uid
        self._names = None
        self.names = names
        self._ids = None
        self.ids = ids
        self._source = None
        self.source = source
        self._quantity = None
        self.quantity = quantity
        self._properties = None
        self.properties = properties
        self._preparation = None
        self.preparation = preparation
        self._sub_systems = None
        self.sub_systems = sub_systems
        self.category = kwargs['category'] if 'category' in kwargs else 'system'

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        self._validate_type('uid', uid, string_types)
        self._uid = uid

    @uid.deleter
    def uid(self):
        self._uid = None

    @property
    def names(self):
        return self._names

    @names.setter
    def names(self, names):
        self._validate_list_type('names', names, string_types)
        self._names = names

    @names.deleter
    def names(self):
        self._names = None

    @property
    def ids(self):
        return self._ids

    @ids.setter
    def ids(self, ids):
        self._validate_list_type('ids', ids, dict, string_types, numbers.Number, Id)
        self._ids = self._get_object(Id, ids)

    @ids.deleter
    def ids(self):
        self._ids = None

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, source):
        self._validate_type('source', source, dict, string_types, Source)
        self._source = self._get_object(Source, source)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._validate_type('quantity', quantity, dict, Quantity)
        self._quantity = self._get_object(Quantity, quantity)

    @quantity.deleter
    def quantity(self):
        self._quantity = None

    @source.deleter
    def source(self):
        self._source = None

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
