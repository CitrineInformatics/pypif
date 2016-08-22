from pypif.obj.common.pio import Pio
from pypif.obj.common.scalar import Scalar


class Quantity(Pio):
    """
    Information about the quantity of a system.
    """

    def __init__(self, actual_mass_percent=None, actual_volume_percent=None, actual_number_percent=None,
                 ideal_mass_percent=None, ideal_volume_percent=None, ideal_number_percent=None, tags=None, **kwargs):
        """
        Constructor.
        
        :param actual_mass_percent: Dictionary or :class:`.Scalar` object with the actual percent of the total mass 
                made up by this system.
        :param actual_volume_percent: Dictionary or :class:`.Scalar` object with the actual percent of the total 
                volume made up by this system.
        :param actual_number_percent: Dictionary or :class:`.Scalar` object with the actual percent of the total 
                numeric quantity made up by this system.
        :param ideal_mass_percent: Dictionary or :class:`.Scalar` object with the ideal percent of the total mass 
                made up by this system.
        :param ideal_volume_percent: Dictionary or :class:`.Scalar` object with the ideal percent of the total 
                volume made up by this system.
        :param ideal_number_percent: Dictionary or :class:`.Scalar` object with the ideal percent of the total 
                numeric quantity made up by this system.
        :param tags: List of tags that apply to the quantity.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Quantity, self).__init__(tags=tags, **kwargs)
        self._actual_mass_percent = None
        self.actual_mass_percent = actual_mass_percent
        self._actual_volume_percent = None
        self.actual_volume_percent = actual_volume_percent
        self._actual_number_percent = None
        self.actual_number_percent = actual_number_percent
        self._ideal_mass_percent = None
        self.ideal_mass_percent = ideal_mass_percent
        self._ideal_volume_percent = None
        self.ideal_volume_percent = ideal_volume_percent
        self._ideal_number_percent = None
        self.ideal_number_percent = ideal_number_percent

    @property
    def actual_mass_percent(self):
        return self._actual_mass_percent
    
    @actual_mass_percent.setter
    def actual_mass_percent(self, actual_mass_percent):
        self._validate_type('actual_mass_percent', actual_mass_percent, dict, Scalar)
        self._actual_mass_percent = self._get_object(Scalar, actual_mass_percent)
    
    @actual_mass_percent.deleter
    def actual_mass_percent(self):
        self._actual_mass_percent = None

    @property
    def actual_volume_percent(self):
        return self._actual_volume_percent

    @actual_volume_percent.setter
    def actual_volume_percent(self, actual_volume_percent):
        self._validate_type('actual_volume_percent', actual_volume_percent, dict, Scalar)
        self._actual_volume_percent = self._get_object(Scalar, actual_volume_percent)

    @actual_volume_percent.deleter
    def actual_volume_percent(self):
        self._actual_volume_percent = None

    @property
    def actual_number_percent(self):
        return self._actual_number_percent

    @actual_number_percent.setter
    def actual_number_percent(self, actual_number_percent):
        self._validate_type('actual_number_percent', actual_number_percent, dict, Scalar)
        self._actual_number_percent = self._get_object(Scalar, actual_number_percent)

    @actual_number_percent.deleter
    def actual_number_percent(self):
        self._actual_number_percent = None

    @property
    def ideal_mass_percent(self):
        return self._ideal_mass_percent

    @ideal_mass_percent.setter
    def ideal_mass_percent(self, ideal_mass_percent):
        self._validate_type('ideal_mass_percent', ideal_mass_percent, dict, Scalar)
        self._ideal_mass_percent = self._get_object(Scalar, ideal_mass_percent)

    @ideal_mass_percent.deleter
    def ideal_mass_percent(self):
        self._ideal_mass_percent = None

    @property
    def ideal_volume_percent(self):
        return self._ideal_volume_percent

    @ideal_volume_percent.setter
    def ideal_volume_percent(self, ideal_volume_percent):
        self._validate_type('ideal_volume_percent', ideal_volume_percent, dict, Scalar)
        self._ideal_volume_percent = self._get_object(Scalar, ideal_volume_percent)

    @ideal_volume_percent.deleter
    def ideal_volume_percent(self):
        self._ideal_volume_percent = None

    @property
    def ideal_number_percent(self):
        return self._ideal_number_percent

    @ideal_number_percent.setter
    def ideal_number_percent(self, ideal_number_percent):
        self._validate_type('ideal_number_percent', ideal_number_percent, dict, Scalar)
        self._ideal_number_percent = self._get_object(Scalar, ideal_number_percent)

    @ideal_number_percent.deleter
    def ideal_number_percent(self):
        self._ideal_number_percent = None
