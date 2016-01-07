from pypif.object.core.id import Id
from pypif.object.core.rcl import Rcl
from pypif.object.chem.composition import Composition
from pypif.object.core.property import Property


class ChemicalSystem(Rcl):
    """
    General representation of a chemical system.
    """

    def __init__(self, label=None, chemical_formula=None, composition=None, common_names=None, ids=None,
                 properties=None, sub_systems=None, references=None, contacts=None, licenses=None, **kwargs):
        """
        Constructor.

        :param label: String with the label of the system. This is used in converting to/from explicit
        representations of the chemical systems.
        :param chemical_formula: String with the chemical formula of the system.
        :param composition: List of :class:`.Composition` objects that describe the composition of the system.
        :param common_names: List of strings with common names of the system.
        :param ids: List of :class:`.Id` objects that identify the system.
        :param properties: List of :class:`.Property` objects with properties of the system.
        :param sub_systems: List of :class:`.Property` objects with the subsystems of the system.
        :param references: List of :class:`.Reference` objects where information about the system is published.
        :param contacts: List of :class:`.Person` objects with people to contact for information about the system.
        :param licenses: List of :class:`.License` objects with licensing information for data about the system.
        :param kwargs: Dictionary of field names not supported.
        """
        super(ChemicalSystem, self).__init__(references=references, contacts=contacts, licenses=licenses, **kwargs)

        # These are the members that have explicit getters and setters
        self._composition = None
        self._ids = None
        self._properties = None
        self._sub_systems = None

        # Set the values for this object
        self.label = label
        self.chemical_formula = chemical_formula
        self.composition = composition
        self.common_names = common_names
        self.ids = ids
        self.properties = properties
        self.sub_systems = sub_systems

    @property
    def composition(self):
        return self._composition

    @composition.setter
    def composition(self, value):
        self._composition = self._get_object(Composition, value)

    @composition.deleter
    def composition(self):
        del self._composition

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
    def sub_systems(self):
        return self._sub_systems

    @sub_systems.setter
    def sub_systems(self, value):
        self._sub_systems = self._get_object(ChemicalSystem, value)

    @sub_systems.deleter
    def sub_systems(self):
        del self._sub_systems
