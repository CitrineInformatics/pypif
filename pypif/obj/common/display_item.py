from six import string_types
from pypif.obj.common.pio import Pio


class DisplayItem(Pio):
    """
    Representation of a display item (table or figure) in a referenced work.
    """

    def __init__(self, number=None, title=None, caption=None, tags=None, **kwargs):
        """
        Constructor.

        :param number: String with the number of the item in the referenced work.
        :param title: Title of the item.
        :param caption: Caption associated with the item.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(DisplayItem, self).__init__(tags=tags, **kwargs)
        self._number = None
        self.number = number
        self._title = None
        self.title = title
        self._caption = None
        self.caption = caption

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._validate_type('number', number, string_types)
        self._number = number

    @number.deleter
    def number(self):
        self._number = None

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
    def caption(self):
        return self._caption

    @caption.setter
    def caption(self, caption):
        self._validate_type('caption', caption, string_types)
        self._caption = caption

    @caption.deleter
    def caption(self):
        self._caption = None
