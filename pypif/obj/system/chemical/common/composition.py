from pypif.obj.common.pio import Pio
from pypif.obj.common.scalar import Scalar


class Composition(Pio):
    """
    Class to store information about an element in a composition vector using weight percents or atomic percents.
    """

    def __init__(self, element=None, actual_weight_percent=None, actual_atomic_percent=None, ideal_weight_percent=None,
                 ideal_atomic_percent=None, **kwargs):
        """
        Constructor.

        :param element: Symbol of the element.
        :param actual_weight_percent: Actual percentage of the weight of the chemical that is this element
        - :class:`.Scalar` object.
        :param actual_atomic_percent: Actual percentage of the atoms in the chemical that are this element
        - :class:`.Scalar` object.
        :param ideal_weight_percent: Ideal percentage of the weight of the chemical that is this element
        - :class:`.Scalar` object.
        :param ideal_atomic_percent: Ideal percentage of the atoms in the chemical that are this element
        - :class:`.Scalar` object.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Composition, self).__init__(**kwargs)
        
        # These are the members that have explicit getters and setters
        self._actual_weight_percent = None
        self._actual_atomic_percent = None
        self._ideal_weight_percent = None
        self._ideal_atomic_percent = None
        
        # Set the values for this object
        self.element = element
        self.actual_weight_percent = actual_weight_percent
        self.actual_atomic_percent = actual_atomic_percent
        self.ideal_weight_percent = ideal_weight_percent
        self.ideal_atomic_percent = ideal_atomic_percent
        
    @property
    def actual_weight_percent(self):
        return self._actual_weight_percent
        
    @actual_weight_percent.setter
    def actual_weight_percent(self, value):
        self._actual_weight_percent = self._get_object(Scalar, value)
    
    @actual_weight_percent.deleter
    def actual_weight_percent(self):
        del self._actual_weight_percent
    
    @property
    def actual_atomic_percent(self):
        return self._actual_atomic_percent
        
    @actual_atomic_percent.setter
    def actual_atomic_percent(self, value):
        self._actual_atomic_percent = self._get_object(Scalar, value)
    
    @actual_atomic_percent.deleter
    def actual_atomic_percent(self):
        del self._actual_atomic_percent
    
    @property
    def ideal_weight_percent(self):
        return self._ideal_weight_percent
        
    @ideal_weight_percent.setter
    def ideal_weight_percent(self, value):
        self._ideal_weight_percent = self._get_object(Scalar, value)
    
    @ideal_weight_percent.deleter
    def ideal_weight_percent(self):
        del self._ideal_weight_percent
    
    @property
    def ideal_atomic_percent(self):
        return self._ideal_atomic_percent
        
    @ideal_atomic_percent.setter
    def ideal_atomic_percent(self, value):
        self._ideal_atomic_percent = self._get_object(Scalar, value)
    
    @ideal_atomic_percent.deleter
    def ideal_atomic_percent(self):
        del self._ideal_atomic_percent
