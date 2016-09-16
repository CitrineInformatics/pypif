from six import string_types
from pypif.obj.system.system import System
from pypif.obj.system.chemical.common.composition import Composition


class ChemicalSystem(System):
    """
    Representation of a general chemical system.
    """

    def __init__(self, uid=None, names=None, ids=None, source=None, quantity=None, chemical_formula=None,
                 composition=None, properties=None, preparation=None, sub_systems=None, references=None,
                 contacts=None, licenses=None, tags=None, **kwargs):
        """
        Constructor.

        :param uid: String with the permanent ID for this record.
        :param names: List of strings with common names of the chemical system.
        :param ids: List of dictionaries, strings, numbers, or :class:`.Id` objects that identify the system.
        :param source: Dictionary, string, or :class:`.Source` object with the source of the system.
        :param quantity: Dictionary or :class:`.Quantity` object with the quantity of the system.
        :param chemical_formula: String with the chemical formula.
        :param composition: List of dictionaries or :class:`.Composition` objects that describe the composition of
                the chemical system.
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
        super(ChemicalSystem, self).__init__(uid=uid, names=names, ids=ids, source=source, quantity=quantity,
                                             properties=properties, preparation=preparation, sub_systems=sub_systems,
                                             references=references, contacts=contacts, licenses=licenses, tags=tags,
                                             **kwargs)
        self._chemical_formula = None
        self.chemical_formula = chemical_formula
        self._composition = None
        self.composition = composition
        self.category = kwargs['category'] if 'category' in kwargs else 'system.chemical'

    @property
    def chemical_formula(self):
        return self._chemical_formula

    @chemical_formula.setter
    def chemical_formula(self, chemical_formula):
        self._validate_type('chemical_formula', chemical_formula, string_types)
        self._chemical_formula = chemical_formula

    @chemical_formula.deleter
    def chemical_formula(self):
        self._chemical_formula = None

    @property
    def composition(self):
        return self._composition

    @composition.setter
    def composition(self, composition):
        self._validate_list_type('composition', composition, dict, Composition)
        self._composition = self._get_object(Composition, composition)

    @composition.deleter
    def composition(self):
        self._composition = None
