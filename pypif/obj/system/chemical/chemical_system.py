from pypif.obj.system.system import System
from pypif.obj.system.chemical.common.composition import Composition


class ChemicalSystem(System):
    """
    Representation of a general chemical system.
    """

    def __init__(self, names=None, ids=None, chemical_formula=None, composition=None, properties=None,
                 processing=None, sub_systems=None, references=None, contacts=None, licenses=None, **kwargs):
        """
        Constructor.

        :param names: List of strings with common names of the chemical system.
        :param ids: List of :class:`.Id` objects that identify the chemical system.
        :param chemical_formula: String with the chemical formula.
        :param composition: List of :class:`.Composition` objects that describe the composition of the chemical system.
        :param properties: List of :class:`.Property` objects with properties of the chemical system.
        :param processing: List of :class:`.Value` objects with the processing information of the chemical system.
        :param sub_systems: List of :class:`.ChemicalSystem` objects with the subsystems of the chemical system.
        :param references: List of :class:`.Reference` objects where information about the system is published.
        :param contacts: List of :class:`.Person` objects with people to contact for information about the system.
        :param licenses: List of :class:`.License` objects with licensing information for data about the system.
        :param kwargs: Dictionary of field names not supported.
        """
        super(ChemicalSystem, self).__init__(names=names, ids=ids, properties=properties, processing=processing,
                                             references=references, contacts=contacts, licenses=licenses, **kwargs)

        # These are the members that have explicit getters and setters
        self._composition = None

        # Set the values for this object
        self.chemical_formula = chemical_formula
        self.composition = composition
        self.sub_systems = sub_systems
        self.category = 'system.chemical'

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
    def sub_systems(self):
        return self._sub_systems

    @sub_systems.setter
    def sub_systems(self, value):
        self._sub_systems = self._get_object(ChemicalSystem, value)

    @sub_systems.deleter
    def sub_systems(self):
        del self._sub_systems
