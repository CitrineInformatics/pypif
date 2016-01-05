from pypif.object.core.general.id import Id
from pypif.object.core.general.rcl import Rcl
from pypif.object.core.general.property import Property
from pypif.object.core.chem.composition import Composition


class SimpleChemicalSystem(Rcl):
    """
    General representation of a simple chemical system.
    """

    def __init__(self, chemical_formula=None, composition=None, common_name=None, id=None, property=None,
                 reference=None, contact=None, license=None, **kwargs):
        """
        Constructor.

        :param chemical_formula: String with the chemical formula of the system.
        :param composition: List of :class:`.Composition` objects that describe the composition of the system.
        :param common_name: List of strings with common names of the system.
        :param id: List of :class:`.Id` objects that identify the system.
        :param property: List of :class:`.Property` objects with properties of the system.
        :param reference: List of :class:`.Reference` objects where information about the system is published.
        :param contact: List of :class:`.Person` objects with people to contact for information about the system.
        :param license: List of :class:`.License` objects with licensing information for data about the system.
        :param kwargs: Dictionary of field names not supported.
        """
        super(ChemicalSystem, self).__init__(reference=reference, contact=contact, license=license, **kwargs)

        # These are the members that have explicit getters and setters
        self._composition = None
        self._id = None
        self._property = None

        # Set the values for this object
        self.chemical_formula = chemical_formula
        self.composition = composition
        self.common_name = common_name
        self.id = id
        self.property = property

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
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = self._get_object(Id, value)

    @id.deleter
    def id(self):
        del self._id

    @property
    def property(self):
        return self._property

    @property.setter
    def property(self, value):
        self._property = self._get_object(Property, value)

    @property.deleter
    def property(self):
        del self._property
