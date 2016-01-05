from pypif.object.core.general.pio import Pio


class Composition(Pio):
    """
    Class to store information about an element in a composition vector using weight percents or atomic percents.
    """

    def __init__(self, element=None, weight_percent=None, atomic_percent=None, **kwargs):
        """
        Constructor.

        :param element: Symbol of the element.
        :param weight_percent: Percentage of the weight of the material that is this element.
        :param atomic_percent: Percentage of the atoms in the material that are this element.
        :param kwargs: Dictionary of field names not supported.
        """
        super(Composition, self).__init__(**kwargs)
        self.element = element
        self.weight_percent = weight_percent
        self.atomic_percent = atomic_percent
