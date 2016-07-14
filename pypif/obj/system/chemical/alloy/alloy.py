from pypif.obj.system.chemical.chemical_system import ChemicalSystem


class Alloy(ChemicalSystem):
    """
    Information about an alloy.
    """

    def __init__(self, uid=None, names=None, ids=None, source=None, quantity=None, chemical_formula=None,
                 composition=None, properties=None, preparation=None, sub_systems=None, phases=None,
                 references=None, contacts=None, licenses=None, tags=None, **kwargs):
        """
        Constructor.

        :param uid: String with the permanent ID for this record.
        :param names: List of strings with common names of the alloy.
        :param ids: List of dictionaries, strings, numbers, or :class:`.Id` objects that identify the alloy.
        :param source: Dictionary, string, or :class:`.Source` object with the source of the alloy.
        :param quantity: Dictionary or :class:`.Quantity` object with the quantity of the alloy.
        :param chemical_formula: String with the chemical formula.
        :param composition: List of dictionaries or :class:`.Composition` objects that describe the composition of
                the alloy.
        :param properties: List of dictionaries or :class:`.Property` objects with properties of the alloy.
        :param preparation: List of dictionaries or :class:`.ProcessStep` objects with the preparation
                information of the alloy.
        :param sub_systems: List of dictionaries or :class:`.System` objects with the subsystems of the alloy.
        :param phases: List of dictionaries or :class:`.AlloyPhase` objects with the phases of the alloy.
        :param references: List of dictionaries or :class:`.Reference` objects where information about the alloy
                is published.
        :param contacts: List of dictionaries, strings, or :class:`.Person` objects with people to contact for
                information about the alloy.
        :param licenses: List of dictionaries, strings, or :class:`.License` objects with licensing information
                for data about the alloy.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Alloy, self).__init__(uid=uid, names=names, ids=ids, source=source, quantity=quantity,
                                    chemical_formula=chemical_formula, composition=composition, properties=properties,
                                    preparation=preparation, sub_systems=sub_systems, references=references,
                                    contacts=contacts, licenses=licenses, tags=tags, **kwargs)
        self.phases = phases
        self.category = kwargs['category'] if 'category' in kwargs else 'system.chemical.alloy'

    @property
    def phases(self):
        return self._sub_systems

    @phases.setter
    def phases(self, phases):
        self.sub_systems = phases

    @phases.deleter
    def phases(self):
        del self.sub_systems
