from pypif.stats.common.stats_wrapper import Stats
from pypif.stats.common.stats_wrapper import StatsWrapper
from pypif.stats.common.field_stats import FieldStats


class PropertyStats(Stats):
    """
    Class to store stats about a single property.
    """

    def __init__(self, count=None, name=None, value=None, units=None):
        """
        Constructor.

        :param count: Count for this object.
        :param name: Dictionary or :class:`.FieldStats` object with stats of the property name.
        :param value: Dictionary or :class:`.FieldStats` object with stats of the property value.
        :param units: Dictionary or :class:`.FieldStats` object with stats of the property units.
        """
        super(PropertyStats, self).__init__(count=count)
        self.name = self._get_object(FieldStats, name)
        self.value = self._get_object(FieldStats, value)
        self.units = self._get_object(FieldStats, units)


class PropertyStatsWrapper(StatsWrapper):
    """
    Class to store stats about a set of properties.
    """

    def __init__(self, count=None, common=None):
        """
        Constructor.

        :param count: Count of properties.
        :param common: List of Dictionary or :class:`.PropertyStats` objects with stats of the properties.
        """
        super(PropertyStatsWrapper, self).__init__(count=count)
        self.common = self._get_object(PropertyStats, common)
