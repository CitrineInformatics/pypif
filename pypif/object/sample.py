from pypif.object.core.general.pio import Pio


class Sample(Pio):
    """
    Class to store information about a sample, which could contain multiple phases of a material.
    """

    def __init__(self, chemical_formula=None, composition=None, common_name=None, id=None, property=None,
                 reference=None, contact=None, license=None, **kwargs):
        super(Sample, self).__init__(**kwargs)
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