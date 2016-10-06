from six import string_types
from pypif.obj.common.display_item import DisplayItem
from pypif.obj.common.name import Name
from pypif.obj.common.pages import Pages
from pypif.obj.common.pio import Pio


class Reference(Pio):
    """
    Information about a referenced publication.
    """

    def __init__(self, doi=None, isbn=None, issn=None, url=None, title=None, publisher=None, journal=None, volume=None,
                 issue=None, year=None, figure=None, table=None, pages=None, authors=None, editors=None,
                 affiliations=None, acknowledgements=None, references=None, tags=None, **kwargs):
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
        :param figure: Dictionary or :class:`.DisplayItem` object with the figure to reference.
        :param table: Dictionary or :class:`.DisplayItem` object with the table to reference.
        :param pages: String, integer, dictionary, or :class:`.Pages` object with the starting and ending pages for
                the published work.
        :param authors: List of strings, dictionaries, or :class:`.Name` objects with information about the authors.
        :param editors: List of strings, dictionaries, or :class:`.Name` objects with information about the editors.
        :param affiliations: List of strings with affiliations.
        :param acknowledgements: List of strings with acknowledgements.
        :param references: List of dictionaries or :class:`.Reference` objects with works cited by this published work.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Reference, self).__init__(tags=tags, **kwargs)
        self._doi = None
        self.doi = doi
        self._isbn = None
        self.isbn = isbn
        self._issn = None
        self.issn = issn
        self._url = None
        self.url = url
        self._title = None
        self.title = title
        self._publisher = None
        self.publisher = publisher
        self._journal = None
        self.journal = journal
        self._volume = None
        self.volume = volume
        self._issue = None
        self.issue = issue
        self._year = None
        self.year = year
        self._figure = None
        self.figure = figure
        self._table = None
        self.table = table
        self._pages = None
        self.pages = pages
        self._authors = None
        self.authors = authors
        self._editors = None
        self.editors = editors
        self._affiliations = None
        self.affiliations = affiliations
        self._acknowledgements = None
        self.acknowledgements = acknowledgements
        self._references = None
        self.references = references

    @property
    def doi(self):
        return self._doi

    @doi.setter
    def doi(self, doi):
        self._validate_type('doi', doi, string_types)
        self._doi = doi

    @doi.deleter
    def doi(self):
        self._doi = None

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        self._validate_type('isbn', isbn, string_types)
        self._isbn = isbn

    @isbn.deleter
    def isbn(self):
        self._isbn = None

    @property
    def issn(self):
        return self.issn

    @issn.setter
    def issn(self, issn):
        self._validate_type('issn', issn, string_types)
        self._issn = issn

    @issn.deleter
    def issn(self):
        self._issn = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._validate_type('url', url, string_types)
        self._url = url

    @url.deleter
    def url(self):
        self._url = None

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
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        self._validate_type('publisher', publisher, string_types)
        self._publisher = publisher

    @publisher.deleter
    def publisher(self):
        self._publisher = None

    @property
    def journal(self):
        return self._journal

    @journal.setter
    def journal(self, journal):
        self._validate_type('journal', journal, string_types)
        self._journal = journal

    @journal.deleter
    def journal(self):
        self._journal = None

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        self._validate_type('volume', volume, string_types)
        self._volume = volume

    @volume.deleter
    def volume(self):
        self._volume = None

    @property
    def issue(self):
        return self._issue

    @issue.setter
    def issue(self, issue):
        self._validate_type('issue', issue, string_types)
        self._issue = issue

    @issue.deleter
    def issue(self):
        self._issue = None

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._validate_type('year', year, string_types)
        self._year = year

    @year.deleter
    def year(self):
        self._year = None

    @property
    def figure(self):
        return self._figure

    @figure.setter
    def figure(self, figure):
        self._validate_type('figure', figure, dict, DisplayItem)
        self._figure = self._get_object(DisplayItem, figure)

    @figure.deleter
    def figure(self):
        self._figure = None

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, table):
        self._validate_type('table', table, dict, DisplayItem)
        self._table = self._get_object(DisplayItem, table)

    @table.deleter
    def table(self):
        self._table = None

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        self._validate_type('pages', pages, string_types, int, dict, Pages)
        self._pages = self._get_object(Pages, pages)

    @pages.deleter
    def pages(self):
        self._pages = None

    @property
    def authors(self):
        return self._authors

    @authors.setter
    def authors(self, authors):
        self._validate_list_type('authors', authors, string_types, dict, Name)
        self._authors = self._get_object(Name, authors)

    @authors.deleter
    def authors(self):
        self._authors = None

    @property
    def editors(self):
        return self._editors

    @editors.setter
    def editors(self, editors):
        self._validate_list_type('editors', editors, string_types, dict, Name)
        self._editors = self._get_object(Name, editors)

    @editors.deleter
    def editors(self):
        self._editors = None

    @property
    def affiliations(self):
        return self._affiliations

    @affiliations.setter
    def affiliations(self, affiliations):
        self._validate_list_type('affiliations', affiliations, string_types)
        self._affiliations = affiliations

    @affiliations.deleter
    def affiliations(self):
        self._affiliations = None

    @property
    def acknowledgements(self):
        return self._acknowledgements

    @acknowledgements.setter
    def acknowledgements(self, acknowledgements):
        self._validate_list_type('acknowledgements', acknowledgements, string_types)
        self._acknowledgements = acknowledgements

    @acknowledgements.deleter
    def acknowledgements(self):
        self._acknowledgements = None

    @property
    def references(self):
        return self._references

    @references.setter
    def references(self, references):
        self._validate_list_type('references', references, dict, Reference)
        self._references = self._get_object(Reference, references)
