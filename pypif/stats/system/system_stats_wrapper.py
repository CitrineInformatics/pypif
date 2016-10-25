from pypif.stats.common.stats_wrapper import Stats
from pypif.stats.common.stats_wrapper import StatsWrapper
from pypif.stats.common.field_stats import FieldStats
from pypif.stats.common.property_stats_wrapper import PropertyStatsWrapper


class SystemStats(Stats):
    """
    Class to store stats of a single system.
    """

    def __init__(self, count=None, names=None, chemicalFormula=None, properties=None):
        """
        Constructor.

        :param count: Number of systems of this type.
        :param names: Dictionary or :class:`.FieldStats` object with stats of the system names.
        :param chemicalFormula: Dictionary or :class:`.FieldStats` object with stats of the system chemical formula.
        :param properties: Dictionary or :class:`.PropertyStatsWrapper` object with stats of the system properties.
        """
        super(SystemStats, self).__init__(count=count)
        self.names = self._get_object(FieldStats, names)
        self.chemicalFormula = self._get_object(FieldStats, chemicalFormula)
        self.properties = self._get_object(PropertyStatsWrapper, properties)


class SystemStatsWrapper(StatsWrapper):
    """
    Class to store stats of systems.
    """

    def __init__(self, count=None, common=None):
        """
        Constructor.

        :param count: Number of systems.
        :param common: Dictionary or :class:`.SystemStats` object with the stats of the system.
        """
        super(SystemStatsWrapper, self).__init__(count=count)
        self.common = self._get_object(SystemStats, common)
