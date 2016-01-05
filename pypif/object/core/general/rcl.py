from pypif.object.core.general.pio import Pio
from pypif.object.core.general.person import Person
from pypif.object.core.general.license import License
from pypif.object.core.general.reference import Reference


class Rcl(Pio):
    """
    Base class for any objects that contain reference, contact, and license information.
    """

    def __init__(self, reference=None, contact=None, license=None, **kwargs):
        """
        Constructor.

        :param reference: List of :class:`.Reference` objects where information about this item is published.
        :param contact: List of :class:`.Person` objects with people that can be contacted for information about
        this item.
        :param license: List of :class:`.License` objects with licensing information for this item.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Rcl, self).__init__(**kwargs)

        # These members have explicit setters and getters
        self._reference = None
        self._contact = None
        self._license = None

        # Set the values for this object
        self._reference = reference
        self._contact = contact
        self._license = license

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
