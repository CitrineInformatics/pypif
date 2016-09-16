from six import string_types
from pypif.obj.common.pio import Pio


class Pages(Pio):
    """
    Representation of the starting and ending pages of a reference.
    """

    def __init__(self, start=None, end=None, tags=None, **kwargs):
        """
        Constructor.

        :param start: String or integer with the starting page.
        :param end: String or integer with the ending page.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Pages, self).__init__(tags=tags, **kwargs)
        self._start = None
        self.start = start
        self._end = None
        self.end = end

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._validate_type('start', start, string_types, int)
        self._start = start

    @start.deleter
    def start(self):
        self._start = None

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        self._validate_type('end', end, string_types, int)
        self._end = end

    @end.deleter
    def end(self):
        self._end = None
