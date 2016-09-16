from six import string_types
from pypif.obj.common.pio import Pio


class Name(Pio):
    """
    Representation of the first and last name of a person.
    """

    def __init__(self, title=None, given=None, family=None, suffix=None, tags=None, **kwargs):
        """
        Constructor.

        :param title: Title of the person (e.g. Prof. or Dr.)
        :param given: Given (first) name of a person.
        :param family: Family (last) name of a person.
        :param suffix: Suffix of the person (e.g. Jr. or Sr.)
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Name, self).__init__(tags=tags, **kwargs)
        self._title = None
        self.title = title
        self._given = None
        self.given = given
        self._family = None
        self.family = family
        self._suffix = None
        self.suffix = suffix

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._validate_type('title', title, string_types)
        self._title = title

    @title.deleter
    def title(self):
        self._title = None

    @property
    def given(self):
        return self._given

    @given.setter
    def given(self, given):
        self._validate_type('given', given, string_types)
        self._given = given

    @given.deleter
    def given(self):
        self._given = None

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._validate_type('family', family, string_types)
        self._family = family

    @family.deleter
    def family(self):
        self._family = None

    @property
    def suffix(self):
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        self._validate_type('suffix', suffix, string_types)
        self._suffix = suffix

    @suffix.deleter
    def suffix(self):
        self._suffix = None
