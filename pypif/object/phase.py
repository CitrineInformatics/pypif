from pypif.object.core.chem.composition import Composition
from pypif.object.core.general.id import Id
from pypif.object.core.general.pio import Pio


class Phase(Pio):
    """
    Class to store information about a phase of a material.
    """

    def __init__(self, chemical_formula=None, composition=None, common_name=None, id=None, property=None,
                 reference=None, contact=None, license=None, **kwargs):
        """
        Constructor.

        :param chemical_formula: String with the chemical formulas of the phase.
        :param composition: One or more Composition objects that define the composition of the phase.
        :param common_name: One or more strings with common names of the phase.
        :param id: One or more Id objects that identify the phase.
        :param property: One or more Property objects with information about properties of the phase.
        :param reference: One or more Reference objects where information about the phase is published.
        :param contact: One or more Person objects with people to contact for information about the phase.
        :param license: One or more license objects with information about licenses that apply to the phase.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Phase, self).__init__(**kwargs)
        self._composition = None
        self._id = None
        self._reference = None
        self._contact = None
        self._license = None
        self.chemical_formula = chemical_formula
        self.composition = composition
        self.common_name = common_name
        self.id = id
        self.reference = reference
        self.contact = contact
        self.license = license

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
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, value):
        self._reference = self._get_object(Reference, value)

    @reference.deleter
    def reference(self):
        del self._reference

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = self._get_object(Person, value)

    @contact.deleter
    def contact(self):
        del self._contact

    @property
    def license(self):
        return self._license

    @license.setter
    def license(self, value):
        self._license = self._get_object(License, value)

    @license.deleter
    def license(self):
        del self._license
