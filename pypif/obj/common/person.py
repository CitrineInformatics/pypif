from pypif.obj.common.name import Name

from pypif.obj.common.pio import Pio


class Person(Pio):
    """
    Information about a person.
    """

    def __init__(self, name=None, email=None, orcid=None, **kwargs):
        """
        Constructor.

        :param name: :class:`.Name` object for the person.
        :param email: String with the email address of the person.
        :param orcid: String with the `ORCID <a href="http://orcid.org">ORCID</a>`_ identifier of the person.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Person, self).__init__(**kwargs)

        # These members have explicit setters and getters
        self._name = None

        # Set the values for this object
        self.name = name
        self.email = email
        self.orcid = orcid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._get_object(Name, value)

    @name.deleter
    def name(self):
        del self._name
