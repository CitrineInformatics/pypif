from six import string_types
from pypif.obj.common.pio import Pio


class FileReference(Pio):
    """
    Information about a file.
    """

    def __init__(self, relative_path=None, mime_type=None, sha256=None, md5=None, tags=None, **kwargs):
        """
        Constructor.

        :param relative_path: String with the relative path (from the location of this file) of the file.
        :param mime_type: String with the mime type of the file.
        :param sha256: String with the SHA-256 hash of the file.
        :param md5: String with the MD5 hash of the file.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(FileReference, self).__init__(tags=tags, **kwargs)
        self._relative_path = None
        self.relative_path = relative_path
        self._mime_type = None
        self.mime_type = mime_type
        self._sha256 = None
        self.sha256 = None
        self._md5 = None
        self.md5 = None

    @property
    def relative_path(self):
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        self._validate_type('relative_path', relative_path, string_types)
        self._relative_path = relative_path

    @relative_path.deleter
    def relative_path(self):
        self._relative_path = None

    @property
    def mime_type(self):
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        self._validate_type('mime_type', mime_type, string_types)
        self._mime_type = mime_type

    @mime_type.deleter
    def mime_type(self):
        self._mime_type = None

    @property
    def sha256(self):
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        self._validate_type('sha256', sha256, string_types)
        self._sha256 = sha256

    @sha256.deleter
    def sha256(self):
        self._sha256 = None

    @property
    def md5(self):
        return self._md5

    @md5.setter
    def md5(self, md5):
        self._validate_type('md5', md5, string_types)
        self._md5 = md5

    @md5.deleter
    def md5(self):
        self._md5 = None
