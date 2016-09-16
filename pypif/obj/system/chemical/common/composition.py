import numbers
from six import string_types
from pypif.obj.common.pio import Pio
from pypif.obj.common.scalar import Scalar


class Composition(Pio):
    """
    Class to store information about an element in a composition vector using weight percents or atomic percents.
    """

    def __init__(self, element=None, actual_weight_percent=None, actual_atomic_percent=None, ideal_weight_percent=None,
                 ideal_atomic_percent=None, tags=None, **kwargs):
        """
        Constructor.

        :param element: Symbol of the element.
        :param actual_weight_percent: Actual percentage of the weight of the chemical that is this element
                - dictionary, string, number, or :class:`.Scalar` object.
        :param actual_atomic_percent: Actual percentage of the atoms in the chemical that are this element
                - dictionary, string, number, or :class:`.Scalar` object.
        :param ideal_weight_percent: Ideal percentage of the weight of the chemical that is this element
                - dictionary, string, number, or :class:`.Scalar` object.
        :param ideal_atomic_percent: Ideal percentage of the atoms in the chemical that are this element
                - dictionary, string, number, or :class:`.Scalar` object.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Composition, self).__init__(tags=tags, **kwargs)
        self._element = None
        self.element = element
        self._actual_weight_percent = None
        self.actual_weight_percent = actual_weight_percent
        self._actual_atomic_percent = None
        self.actual_atomic_percent = actual_atomic_percent
        self._ideal_weight_percent = None
        self.ideal_weight_percent = ideal_weight_percent
        self._ideal_atomic_percent = None
        self.ideal_atomic_percent = ideal_atomic_percent

    @property
    def element(self):
        return self._element

    @element.setter
    def element(self, element):
        self._validate_type('element', element, string_types)
        self._element = element

    @element.deleter
    def element(self):
        self._element = None
        
    @property
    def actual_weight_percent(self):
        return self._actual_weight_percent
        
    @actual_weight_percent.setter
    def actual_weight_percent(self, actual_weight_percent):
        self._validate_type('actual_weight_percent', actual_weight_percent, dict, string_types,
                            numbers.Number, Scalar)
        self._actual_weight_percent = self._get_object(Scalar, actual_weight_percent)
    
    @actual_weight_percent.deleter
    def actual_weight_percent(self):
        self._actual_weight_percent = None
    
    @property
    def actual_atomic_percent(self):
        return self._actual_atomic_percent
        
    @actual_atomic_percent.setter
    def actual_atomic_percent(self, actual_atomic_percent):
        self._validate_type('actual_atomic_percent', actual_atomic_percent, dict, string_types,
                            numbers.Number, Scalar)
        self._actual_atomic_percent = self._get_object(Scalar, actual_atomic_percent)
    
    @actual_atomic_percent.deleter
    def actual_atomic_percent(self):
        self._actual_atomic_percent = None
    
    @property
    def ideal_weight_percent(self):
        return self._ideal_weight_percent
        
    @ideal_weight_percent.setter
    def ideal_weight_percent(self, ideal_weight_percent):
        self._validate_type('ideal_weight_percent', ideal_weight_percent, dict, string_types,
                            numbers.Number, Scalar)
        self._ideal_weight_percent = self._get_object(Scalar, ideal_weight_percent)
    
    @ideal_weight_percent.deleter
    def ideal_weight_percent(self):
        self._ideal_weight_percent = None
    
    @property
    def ideal_atomic_percent(self):
        return self._ideal_atomic_percent
        
    @ideal_atomic_percent.setter
    def ideal_atomic_percent(self, ideal_atomic_percent):
        self._validate_type('ideal_atomic_percent', ideal_atomic_percent, dict, string_types,
                            numbers.Number, Scalar)
        self._ideal_atomic_percent = self._get_object(Scalar, ideal_atomic_percent)
    
    @ideal_atomic_percent.deleter
    def ideal_atomic_percent(self):
        self._ideal_atomic_percent = None
