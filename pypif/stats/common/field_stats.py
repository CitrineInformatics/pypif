from pypif.stats.common.stats_wrapper import Stats


class TermAndCount(Stats):
    """
    Class to store information about a single term.
    """

    def __init__(self, count=None, term=None):
        """
        Information about a single term and its count.

        :param count: Total count for this term.
        :param term: String with the term to save.
        """
        super(TermAndCount, self).__init__(count=count)
        self.term = term


class FieldStats(Stats):
    """
    Class to store stats for a single field.
    """

    def __init__(self, count=None, numeric_count=None, min=None, max=None, terms=None):
        """
        Constructor.

        :param count: Total count for this field.
        :param numeric_count: Number of numeric values for this field.
        :param min: Minimum of the numeric values for this field.
        :param max: Maximum of the numeric values for this field.
        :param terms: List of dictionaries or :class:`.TermAndCount` objects with stats about terms.
        """
        super(FieldStats, self).__init__(count=count)
        self.numeric_count = numeric_count
        self.min = min
        self.max = max
        self.terms = self._get_object(TermAndCount, terms)
