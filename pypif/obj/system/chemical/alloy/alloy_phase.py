from pypif.obj.system.chemical.chemical_system import ChemicalSystem


class AlloyPhase(ChemicalSystem):
    """
    Representation of a single phase in an alloy.
    """

    def __init__(self, names=None, ids=None, chemical_formula=None, composition=None, properties=None,
                 preparation=None, sub_systems=None, references=None, contacts=None, licenses=None, **kwargs):
        """
        Constructor.

        :param names: List of strings with common names of the alloy phase.
        :param ids: List of dictionaries, strings, numbers, or :class:`.Id` objects that identify the alloy phase.
        :param chemical_formula: String with the chemical formula.
        :param composition: List of dictionaries or :class:`.Composition` objects that describe the composition of
                the alloy phase.
        :param properties: List of dictionaries or :class:`.Property` objects with properties of the alloy phase.
        :param preparation: List of dictionaries or :class:`.ProcessStep` objects with the preparation
                information of the alloy phase.
        :param sub_systems: List of dictionaries or :class:`.System` objects with the subsystems of the alloy phase.
        :param references: List of dictionaries or :class:`.Reference` objects where information about the alloy
                phase is published.
        :param contacts: List of dictionaries, strings, or :class:`.Person` objects with people to contact for
                information about the alloy phase.
        :param licenses: List of dictionaries, strings, or :class:`.License` objects with licensing information
                for data about the alloy phase.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(AlloyPhase, self).__init__(names=names, ids=ids, chemical_formula=chemical_formula,
                                         composition=composition, properties=properties, preparation=preparation,
                                         sub_systems=sub_systems, references=references, contacts=contacts,
                                         licenses=licenses, **kwargs)
        self.category = kwargs['category'] if 'category' in kwargs else 'system.chemical.alloy.phase'
