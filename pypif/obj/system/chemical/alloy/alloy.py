from pypif.obj.system.chemical.chemical_system import ChemicalSystem
from pypif.obj.system.chemical.alloy.alloy_phase import AlloyPhase


class Alloy(ChemicalSystem):
    """
    Information about an alloy.
    """

    def __init__(self, names=None, ids=None, chemical_formula=None, composition=None, properties=None,
                 preparation=None, phases=None, references=None, contacts=None, licenses=None, **kwargs):
        """
        Constructor.

        :param names: List of strings with common names of the alloy.
        :param ids: List of :class:`.Id` objects that identify the alloy.
        :param chemical_formula: String with the chemical formula.
        :param composition: List of :class:`.Composition` objects that describe the composition of the alloy.
        :param properties: List of :class:`.Property` objects with properties of the alloy.
        :param preparation: List of :class:`.ProcessStep` objects with the preparation information of the alloy.
        :param phases: List of :class:`.AlloyPhase` objects with the phases contained in the alloy.
        :param references: List of :class:`.Reference` objects where information about the alloy is published.
        :param contacts: List of :class:`.Person` objects with people to contact for information about the alloy.
        :param licenses: List of :class:`.License` objects with licensing information for data about the alloy.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Alloy, self).__init__(names=names, ids=ids, chemical_formula=chemical_formula, composition=composition,
                                    properties=properties, preparation=preparation, references=references,
                                    contacts=contacts, licenses=licenses, **kwargs)
        self.phases = phases
        self.category = 'system.chemical.alloy'

    @property
    def phases(self):
        return self._sub_systems

    @phases.setter
    def phases(self, value):
        self._sub_systems = self._get_object(AlloyPhase, value)

    @phases.deleter
    def phases(self):
        del self._sub_systems
