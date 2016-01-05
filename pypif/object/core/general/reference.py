from pypif.object.core.general.pio import Pio
from pypif.object.core.general.name import Name
from pypif.object.core.general.pages import Pages


class Reference(Pio):
    """
    Information about a reference.
    """

    def __init__(self, doi=None, isbn=None, issn=None, url=None, title=None, publisher=None, journal=None, volume=None,
                 issue=None, year=None, pages=None, author=None, editor=None, reference=None, **kwargs):
        """
        Constructor.

        :param doi: String with the DOI of the reference.
        :param isbn: String with the ISBN of the reference.
        :param issn: String with the ISSN of the reference.
        :param url: String with the URL of the reference.
        :param title: String with the title of the reference.
        :param publisher: String with the publisher of the reference.
        :param journal: String with the name of the journal that the reference is published in.
        :param volume: String with the volume of the reference.
        :param issue: String with the issue of the reference.
        :param year: String with the year in which the reference was published.
        :param pages: :class:`.Pages` object with the starting and ending pages for the reference.
        :param author: List of :class:`.Name` objects with information about the authors.
        :param editor: List of :class:`.Name` objects with information about the editors.
        :param reference: List of :class:`.Reference` objects with information about works that this reference
        references.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Reference, self).__init__(**kwargs)

        # These members have explicit setters and getters
        self._pages = None
        self._author = None
        self._editor = None
        self._reference = None

        # Set the values for this object
        self.doi = doi
        self.isbn = isbn
        self.issn = issn
        self.url = url
        self.title = title
        self.publisher = publisher
        self.journal = journal
        self.volume = volume
        self.issue = issue
        self.year = year
        self.pages = pages
        self.author = author
        self.editor = editor
        self.reference = reference

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        self._pages = self._get_object(Pages, value)

    @pages.deleter
    def pages(self):
        del self._pages

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = self._get_object(Name, value)

    @author.deleter
    def author(self):
        del self._author

    @property
    def editor(self):
        return self._editor

    @editor.setter
    def editor(self, value):
        self._editor = self._get_object(Name, value)

    @editor.deleter
    def editor(self):
        del self._editor

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, value):
        self._reference = self._get_object(Reference, value)

    @reference.deleter
    def reference(self):
        del self._reference
