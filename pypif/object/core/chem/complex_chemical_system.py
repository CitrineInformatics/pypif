from pypif.object.core.chem.simple_chemical_system import ChemicalSystem


class ComplexChemicalSystem(ChemicalSystem):
    """
    Abstract representation of more complex chemical systems that may be made of many subsystems.
    """

    def __init__(self, label=None, chemical_formula=None, composition=None, common_name=None, id=None, property=None,
                 sub_system=None, reference=None, contact=None, license=None, **kwargs):
        """
        Constructor.

        :param label: String with the label for the system. This is used to convert between more definite
        representations of chemical systems.
        :param chemical_formula: String with the chemical formula of the system.
        :param composition: List of :class:`.Composition` objects that describe the composition of the system.
        :param common_name: List of strings with common names of the system.
        :param id: List of :class:`.Id` objects that identify the system.
        :param property: List of :class:`.Property` objects with properties of the system.
        :param sub_system: List of :class:`.ComplexChemicalSystem` objects with subsystems of this system.
        :param reference: List of :class:`.Reference` objects where information about the system is published.
        :param contact: List of :class:`.Person` objects with people to contact for information about the system.
        :param license: List of :class:`.License` objects with licensing information for data about the system.
        :param kwargs: Dictionary of field names not supported.
        """
        super(ComplexChemicalSystem, self):
