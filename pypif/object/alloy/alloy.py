from pypif.object.chem import ChemicalSystem


class Alloy(ChemicalSystem):
    """
    Class to represent an alloy.
    """

    def __init__(self, chemical_formula=None, composition=None, common_names=None, ids=None, properties=None,
                 phases=None, references=None, contacts=None, licenses=None, **kwargs):
        """
        Constructor.

        :param chemical_formula: String with the chemical formula of the alloy.
        :param composition: List of :class:`.Composition` objects that describe the composition of the alloy.
        :param common_names: List of strings with common names of the alloy.
        :param ids: List of :class:`.Id` objects that identify the alloy.
        :param properties: List of :class:`.Property` objects with properties of the alloy.
        :param phases: List of :class:`.Phase` objects with the phases contained within the alloy.
        :param references: List of :class:`.Reference` objects where information about the alloy is published.
        :param contacts: List of :class:`.Person` objects with people to contact for information about the alloy.
        :param licenses: List of :class:`.License` objects with licensing information for data about the alloy.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Alloy, self).__init__(label='Alloy', chemical_formula=chemical_formula, composition=composition,
                                    common_names=common_names, ids=ids, properties=properties, references=references,
                                    contacts=contacts, licenses=licenses, **kwargs)
        self.phases = phases

    @property
    def phases(self):
        return self._sub_systems

    @phases.setter
    def phases(self, value):
        self._sub_systems = self._get_object(Alloy, value)

    @phases.deleter
    def phases(self):
        del self._sub_systems
