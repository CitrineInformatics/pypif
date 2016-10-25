from pypif.util.serializable import Serializable


class Stats(Serializable):
    """
    Class to store stats for a single object.
    """

    def __init__(self, count=None):
        """
        Constructor.

        :param count: Integer with the count for this object.
        """
        self.count = count


class StatsWrapper(Serializable):
    """
    Class to store stats for a set of objects.
    """

    def __init__(self, count):
        """
        Constructor.

        :param count: Integer with the count for this object.
        """
        self.count = count
