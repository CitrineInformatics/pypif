from pypif.obj.chem.chemical_system import ChemicalSystem


class Phase(ChemicalSystem):
    """
    Class to represent a single phase in an alloy.
    """

    def __init__(self, chemical_formula=None, composition=None, common_names=None, ids=None, properties=None,
                 references=None, contacts=None, licenses=None, **kwargs):
        """
        Constructor.

        :param chemical_formula: String with the chemical formula of the system.
        :param List of :class:`.Composition` objects that describe the composition of the system.
        :param common_names: List of strings with common names of the system.
        :param ids: List of :class:`.Id` objects that identify the system.
        :param properties: List of :class:`.Property` objects with properties of the system.
        :param references: List of :class:`.Reference` objects where information about the system is published.
        :param contacts: List of :class:`.Person` objects with people to contact for information about the system.
        :param licenses: List of :class:`.License` objects with licensing information for data about the system.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Phase, self).__init__(label='Phase', chemical_formula=chemical_formula, composition=composition,
                                    common_names=common_names, ids=ids, properties=properties, references=references,
                                    contacts=contacts, licenses=licenses, **kwargs)
