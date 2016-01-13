from pypif.obj.system.chemical.chemical_system import ChemicalSystem


class AlloyPhase(ChemicalSystem):
    """
    Representation of a single phase in an alloy.
    """

    def __init__(self, names=None, ids=None, chemical_formula=None, composition=None, properties=None,
                 preparation=None, references=None, contacts=None, licenses=None, **kwargs):
        """
        Constructor.

        :param names: List of strings with common names of the phase.
        :param ids: List of :class:`.Id` objects that identify the phase.
        :param chemical_formula: String with the chemical formula.
        :param composition: List of :class:`.Composition` objects that describe the composition of the phase.
        :param properties: List of :class:`.Property` objects with properties of the phase.
        :param preparation: List of :class:`.ProcessStep` objects with the preparation information of the phase.
        :param phases: List of :class:`.AlloyPhase` objects with the phases contained in the phase.
        :param references: List of :class:`.Reference` objects where information about the alloy is published.
        :param contacts: List of :class:`.Person` objects with people to contact for information about the alloy.
        :param licenses: List of :class:`.License` objects with licensing information for data about the alloy.
        :param kwargs: Dictionary of field names not supported.
        """
        super(AlloyPhase, self).__init__(names=names, ids=ids, chemical_formula=chemical_formula,
                                         composition=composition, properties=properties, preparation=preparation,
                                         references=references, contacts=contacts, licenses=licenses, **kwargs)
        self.category = 'system.chemical.alloy.phase'
