from six import string_types
from pypif.obj.common.license import License
from pypif.obj.common.person import Person
from pypif.obj.common.pio import Pio
from pypif.obj.common.reference import Reference


class Rcl(Pio):
    """
    Base class for any objects that contain reference, contact, and license information.
    """

    def __init__(self, references=None, contacts=None, licenses=None, tags=None, **kwargs):
        """
        Constructor.

        :param references: List of dictionaries or :class:`.Reference` objects where information about this
                item is published.
        :param contacts: List of dictionaries, strings, or :class:`.Person` objects with people that can be
                contacted for information about this item.
        :param licenses: List of dictionaries, strings, or :class:`.License` objects with licensing information
                for this item.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Rcl, self).__init__(tags=tags, **kwargs)
        self._references = None
        self.references = references
        self._contacts = None
        self.contacts = contacts
        self._licenses = None
        self.licenses = licenses

    @property
    def references(self):
        return self._references

    @references.setter
    def references(self, references):
        self._validate_list_type('references', references, dict, Reference)
        self._references = self._get_object(Reference, references)

    @references.deleter
    def references(self):
        self._references = None

    @property
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        self._validate_list_type('contacts', contacts, dict, string_types, Person)
        self._contacts = self._get_object(Person, contacts)

    @contacts.deleter
    def contacts(self):
        self._contacts = None

    @property
    def licenses(self):
        return self._licenses

    @licenses.setter
    def licenses(self, licenses):
        self._validate_list_type('licenses', licenses, dict, string_types, License)
        self._licenses = self._get_object(License, licenses)

    @licenses.deleter
    def licenses(self):
        self._licenses = None
