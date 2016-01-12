from pypif.obj.common.pio import Pio


class Name(Pio):
    """
    Representation of the first and last name of a person.
    """

    def __init__(self, title=None, given=None, family=None, suffix=None, **kwargs):
        """
        Constructor.

        :param title: Title of the person (e.g. Prof. or Dr.)
        :param given: Given (first) name of a person.
        :param family: Family (last) name of a person.
        :param suffix: Suffix of the person (e.g. Jr. or Sr.)
        :param kwargs: Dictionary of field names not supported.
        """
        super(Name, self).__init__(**kwargs)
        self.title = title
        self.given = given
        self.family = family
        self.suffix = suffix
