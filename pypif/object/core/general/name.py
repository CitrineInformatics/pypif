from pypif.object.core.general.pio import Pio


class Name(Pio):
    """
    First and last name of a person.
    """

    def __init__(self, given=None, family=None, **kwargs):
        """
        Constructor.

        :param given: Given (first) name of a person.
        :param family: Family (last) name of a person.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Name, self).__init__(**kwargs)
        self.given = given
        self.family = family
