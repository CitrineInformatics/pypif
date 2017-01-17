from pypif.obj.common.property import Property
from pypif.obj.common.quantity import Quantity
from pypif.obj.common.display_item import DisplayItem 
from pypif.obj.common.id import Id
from pypif.obj.common.instrument import Instrument
from pypif.obj.common.license import License
from pypif.obj.common.method import Method
from pypif.obj.common.software import Software
from pypif.obj.common.source import Source
from pypif.obj.common.value import Value
from pypif.obj.common.reference import Reference
from pypif.obj import System as subsystem

class ReadView():

    def __init__(self, system):
        self.inlines = [
            (subsystem, "uid"),
            (Property, "name"),
            (Quantity, "name"),
            (Id, "name"),
            (Instrument, "name"),
            (License, "name"),
            (Method, "name"),
            (Value, "name"),
            (Software, "name"),
            (Source, "producer"),
            (DisplayItem, "title"),
            (Reference, "doi"),
        ]

        for k in system.__dict__:
            added = False
            if isinstance(getattr(system, k), list):
                for t, name in self.inlines:
                    if isinstance(getattr(system, k)[0], t):
                        setattr(self, k[1:], {getattr(x, name) : ReadView(x) for x in getattr(system, k)})
                        added = True
                        break
                if not added:
                    setattr(self, k[1:], getattr(system, k))
            else:
                for t, name in self.inlines:
                    if isinstance(getattr(system, k), t):
                        setattr(self, k[1:], {getattr(system, k)[name] : ReadView(getattr(system, k))})
                        added = True
                        break
                if not added:
                    setattr(self, k[1:], getattr(system, k))
