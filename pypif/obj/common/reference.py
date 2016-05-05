from pypif.obj.common.name import Name
from pypif.obj.common.pages import Pages
from pypif.obj.common.pio import Pio


class Reference(Pio):
    """
    Information about a referenced publication.
    """

    def __init__(self, doi=None, isbn=None, issn=None, url=None, title=None, publisher=None, journal=None, volume=None,
                 issue=None, year=None, pages=None, authors=None, editors=None, affiliations=None,
                 acknowledgements=None, references=None, **kwargs):
        """
        Constructor.

        :param doi: String with DOI of the published work
        :param isbn: String with ISBN of the published work
        :param issn: String with ISSN of the published work
        :param url: String with URL to the published work
        :param title: String with title of the published work.
        :param publisher: String with publisher of the work.
        :param journal: String with the journal in which the work was published.
        :param volume: String with the volume in which the work was published.
        :param issue: String with the issue in which the work was published.
        :param year: String with the year in which the work was published.
        :param pages: :class:`.Pages` object with the starting and ending pages for the published work.
        :param authors: List of :class:`.Name` objects with information about the authors.
        :param editors: List of :class:`.Name` objects with information about the editors.
        :param affiliations: List of strings with affiliations.
        :param acknowledgements: List of strings with acknowledgements.
        :param references: List of :class:`.Reference` objects with works cited by this published work.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Reference, self).__init__(**kwargs)

        # These members have explicit setters and getters
        self._pages = None
        self._authors = None
        self._editors = None
        self._references = None

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
        self.authors = authors
        self.editors = editors
        self.affiliations = affiliations
        self.acknowledgements = acknowledgements
        self.references = references

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
    def authors(self):
        return self._authors

    @authors.setter
    def authors(self, value):
        self._authors = self._get_object(Name, value)

    @authors.deleter
    def authors(self):
        del self._authors

    @property
    def editors(self):
        return self._editors

    @editors.setter
    def editors(self, value):
        self._editors = self._get_object(Name, value)

    @editors.deleter
    def editors(self):
        del self._editors

    @property
    def references(self):
        return self._references

    @references.setter
    def references(self, value):
        self._references = self._get_object(Reference, value)

    @references.deleter
    def references(self):
        del self._references
