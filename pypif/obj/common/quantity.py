from pypif.obj.common.pio import Pio
from pypif.obj.common.scalar import Scalar


class Quantity(Pio):
    """
    Information about the quantity of a system.
    """

    def __init__(self, actual_mass_fraction=None, actual_volume_fraction=None, actual_number_fraction=None,
                 ideal_mass_fraction=None, ideal_volume_fraction=None, ideal_number_fraction=None, tags=None, **kwargs):
        """
        Constructor.
        
        :param actual_mass_fraction: Dictionary or :class:`.Scalar` object with the actual fraction of the total mass 
                made up by this system.
        :param actual_volume_fraction: Dictionary or :class:`.Scalar` object with the actual fraction of the total 
                volume made up by this system.
        :param actual_number_fraction: Dictionary or :class:`.Scalar` object with the actual fraction of the total 
                numeric quantity made up by this system.
        :param ideal_mass_fraction: Dictionary or :class:`.Scalar` object with the ideal fraction of the total mass 
                made up by this system.
        :param ideal_volume_fraction: Dictionary or :class:`.Scalar` object with the ideal fraction of the total 
                volume made up by this system.
        :param ideal_number_fraction: Dictionary or :class:`.Scalar` object with the ideal fraction of the total 
                numeric quantity made up by this system.
        :param tags: List of tags that apply to the quantity.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Quantity, self).__init__(tags=tags, **kwargs)
        self._actual_mass_fraction = None
        self.actual_mass_fraction = actual_mass_fraction
        self._actual_volume_fraction = None
        self.actual_volume_fraction = actual_volume_fraction
        self._actual_number_fraction = None
        self.actual_number_fraction = actual_number_fraction
        self._ideal_mass_fraction = None
        self.ideal_mass_fraction = ideal_mass_fraction
        self._ideal_volume_fraction = None
        self.ideal_volume_fraction = ideal_volume_fraction
        self._ideal_number_fraction = None
        self.ideal_number_fraction = ideal_number_fraction

    @property
    def actual_mass_fraction(self):
        return self._actual_mass_fraction
    
    @actual_mass_fraction.setter
    def actual_mass_fraction(self, actual_mass_fraction):
        self._validate_type('actual_mass_fraction', actual_mass_fraction, dict, Scalar)
        self._actual_mass_fraction = self._get_object(Scalar, actual_mass_fraction)
    
    @actual_mass_fraction.deleter
    def actual_mass_fraction(self):
        self._actual_mass_fraction = None

    @property
    def actual_volume_fraction(self):
        return self._actual_volume_fraction

    @actual_volume_fraction.setter
    def actual_volume_fraction(self, actual_volume_fraction):
        self._validate_type('actual_volume_fraction', actual_volume_fraction, dict, Scalar)
        self._actual_volume_fraction = self._get_object(Scalar, actual_volume_fraction)

    @actual_volume_fraction.deleter
    def actual_volume_fraction(self):
        self._actual_volume_fraction = None

    @property
    def actual_number_fraction(self):
        return self._actual_number_fraction

    @actual_number_fraction.setter
    def actual_number_fraction(self, actual_number_fraction):
        self._validate_type('actual_number_fraction', actual_number_fraction, dict, Scalar)
        self._actual_number_fraction = self._get_object(Scalar, actual_number_fraction)

    @actual_number_fraction.deleter
    def actual_number_fraction(self):
        self._actual_number_fraction = None

    @property
    def ideal_mass_fraction(self):
        return self._ideal_mass_fraction

    @ideal_mass_fraction.setter
    def ideal_mass_fraction(self, ideal_mass_fraction):
        self._validate_type('ideal_mass_fraction', ideal_mass_fraction, dict, Scalar)
        self._ideal_mass_fraction = self._get_object(Scalar, ideal_mass_fraction)

    @ideal_mass_fraction.deleter
    def ideal_mass_fraction(self):
        self._ideal_mass_fraction = None

    @property
    def ideal_volume_fraction(self):
        return self._ideal_volume_fraction

    @ideal_volume_fraction.setter
    def ideal_volume_fraction(self, ideal_volume_fraction):
        self._validate_type('ideal_volume_fraction', ideal_volume_fraction, dict, Scalar)
        self._ideal_volume_fraction = self._get_object(Scalar, ideal_volume_fraction)

    @ideal_volume_fraction.deleter
    def ideal_volume_fraction(self):
        self._ideal_volume_fraction = None

    @property
    def ideal_number_fraction(self):
        return self._ideal_number_fraction

    @ideal_number_fraction.setter
    def ideal_number_fraction(self, ideal_number_fraction):
        self._validate_type('ideal_number_fraction', ideal_number_fraction, dict, Scalar)
        self._ideal_number_fraction = self._get_object(Scalar, ideal_number_fraction)

    @ideal_number_fraction.deleter
    def ideal_number_fraction(self):
        self._ideal_number_fraction = None
