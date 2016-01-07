from pypif.object.core.general.license import License
from pypif.object.core.general.person import Person
from pypif.object.core.general.reference import Reference

from pypif.object.core.pio import Pio


class Rcl(Pio):
    """
    Base class for any objects that contain reference, contact, and license information.
    """

    def __init__(self, references=None, contacts=None, licenses=None, **kwargs):
        """
        Constructor.

        :param references: List of :class:`.Reference` objects where information about this item is published.
        :param contacts: List of :class:`.Person` objects with people that can be contacted for information about
        this item.
        :param licenses: List of :class:`.License` objects with licensing information for this item.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Rcl, self).__init__(**kwargs)

        # These members have explicit setters and getters
        self._references = None
        self._contacts = None
        self._licenses = None

        # Set the values for this object
        self._references = references
        self._contacts = contacts
        self._licenses = licenses

    @property
    def references(self):
        return self._references

    @references.setter
    def references(self, value):
        self._references = self._get_object(Reference, value)

    @references.deleter
    def references(self):
        del self._references

    @property
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, value):
        self._contacts = self._get_object(Person, value)

    @contacts.deleter
    def contacts(self):
        del self._contacts

    @property
    def licenses(self):
        return self._licenses

    @licenses.setter
    def licenses(self, value):
        self._licenses = self._get_object(License, value)

    @licenses.deleter
    def licenses(self):
        del self._licenses
