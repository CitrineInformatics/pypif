from six import string_types
from pypif.obj.common.name import Name
from pypif.obj.common.pio import Pio


class Person(Pio):
    """
    Information about a person.
    """

    def __init__(self, name=None, email=None, orcid=None, tags=None, **kwargs):
        """
        Constructor.

        :param name: :class: Dictionary or `.Name` object for the person.
        :param email: String with the email address of the person.
        :param orcid: String with the `ORCID <a href="http://orcid.org">ORCID</a>`_ identifier of the person.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Person, self).__init__(tags=tags, **kwargs)
        self._name = None
        self.name = name
        self._email = None
        self.email = email
        self._orcid = None
        self.orcid = orcid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._validate_type('name', name, dict, Name)
        self._name = self._get_object(Name, name)

    @name.deleter
    def name(self):
        self._name = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._validate_type('email', email, string_types)
        self._email = email

    @email.deleter
    def email(self):
        self._email = None

    @property
    def orcid(self):
        return self._orcid

    @orcid.setter
    def orcid(self, orcid):
        self._validate_type('orcid', orcid, string_types)
        self._orcid = orcid

    @orcid.deleter
    def orcid(self):
        self._orcid = None
