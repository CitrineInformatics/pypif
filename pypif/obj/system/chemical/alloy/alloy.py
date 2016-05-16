from pypif.obj.system.system import System
from pypif.obj.system.chemical.chemical_system import ChemicalSystem
from pypif.obj.system.chemical.alloy.alloy_phase import AlloyPhase


class Alloy(ChemicalSystem):
    """
    Information about an alloy.
    """

    def __init__(self, names=None, ids=None, chemical_formula=None, composition=None, properties=None,
                 preparation=None, sub_systems=None, phases=None, references=None, contacts=None,
                 licenses=None, tags=None, **kwargs):
        """
        Constructor.

        :param names: List of strings with common names of the alloy.
        :param ids: List of dictionaries, strings, numbers, or :class:`.Id` objects that identify the alloy.
        :param chemical_formula: String with the chemical formula.
        :param composition: List of dictionaries or :class:`.Composition` objects that describe the composition of
                the alloy.
        :param properties: List of dictionaries or :class:`.Property` objects with properties of the alloy.
        :param preparation: List of dictionaries or :class:`.ProcessStep` objects with the preparation
                information of the alloy.
        :param sub_systems: List of dictionaries or :class:`.System` objects with the subsystems of the alloy.
        :param phases: List of dictionaries or :class:`.AlloyPhase` objects with the phases of the alloy.
        :param references: List of dictionaries or :class:`.Reference` objects where information about the alloy
                is published.
        :param contacts: List of dictionaries, strings, or :class:`.Person` objects with people to contact for
                information about the alloy.
        :param licenses: List of dictionaries, strings, or :class:`.License` objects with licensing information
                for data about the alloy.
        :param tags: List of strings or numbers that are tags for this object.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Alloy, self).__init__(names=names, ids=ids, chemical_formula=chemical_formula, composition=composition,
                                    properties=properties, preparation=preparation, sub_systems=sub_systems,
                                    references=references, contacts=contacts, licenses=licenses, tags=tags, **kwargs)
        self.phases = phases
        self.category = kwargs['category'] if 'category' in kwargs else 'system.chemical.alloy'

    @property
    def phases(self):
        if isinstance(self._sub_systems, AlloyPhase):
            return self._sub_systems
        elif isinstance(self._sub_systems, list):
            return [i for i in self._sub_systems if isinstance(i, AlloyPhase)]
        else:
            return None

    @phases.setter
    def phases(self, phases):
        self._validate_list_type('phases', phases, dict, AlloyPhase)
        phases = self._get_object(AlloyPhase, phases)
        if isinstance(self._sub_systems, list) and isinstance(phases, list):
            self._sub_systems.extend(phases)
        elif isinstance(self._sub_systems, System) and isinstance(phases, list):
            self._sub_systems = [self._sub_systems] + phases
        elif isinstance(self._sub_systems, list) and isinstance(phases, System):
            self._sub_systems = self._sub_systems + [phases]
        elif isinstance(self._sub_systems, System) and isinstance(phases, System):
            self._sub_systems = [self._sub_systems, phases]
        elif self._sub_systems is None:
            self._sub_systems = phases
        elif phases is not None:
            raise RuntimeError('Cannot combine phases')

    @phases.deleter
    def phases(self):
        if isinstance(self._sub_systems, AlloyPhase):
            self._sub_systems = None
        elif isinstance(self._sub_systems, list):
            self._sub_systems = [i for i in self._sub_systems if not isinstance(i, AlloyPhase)]
