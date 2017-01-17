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

def new_keypair(key, value, ambig, unambig):
    if key in ambig:
        return

    if key in unambig:
        ambig.append(key)
        unambig.remove(key)
        return

    unambig[key] = value
    return


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

        def foo_foo(gah, gahh):
            print("bar")

        self.unambig = {}
        self.ambig = set()

        for k in system.__dict__:
            added = False
            if isinstance(getattr(system, k), list):
                for t, name in self.inlines:
                    if isinstance(getattr(system, k)[0], t):
                        parsed = {}
                        for x in getattr(system, k):
                            new_key = getattr(x, name)
                            new_val = ReadView(x)
                            parsed[new_key] = new_val
                            new_keypair(new_key, new_val, self.ambig, self.unambig)
                            for kk, vv in new_val.unambig.items():
                                new_keypair(kk, vv, self.ambig, self.unambig)
                        setattr(self, k[1:], parsed)
                        added = True
                        break
                if not added:
                    setattr(self, k[1:], getattr(system, k))
            else:
                for t, name in self.inlines:
                    if isinstance(getattr(system, k), t):
                        new_key = getattr(system, k)[name]
                        new_val = ReadView(getattr(system, k))
                        new_keypair(new_key, new_val, self.ambig, self.unambig)
                        setattr(self, k[1:], {new_key: new_val})
                        for kk, vv in new_val.unambig.items():
                            new_keypair(kk, vv, self.ambig, self.unambig)
                        added = True
                        break
                if not added:
                    setattr(self, k[1:], getattr(system, k))

    def keys(self):
        return self.unambig.keys()

    def __getitem__(self, key):
        if key not in self.unambig:
            raise KeyError(key + " not defined unambiguously")
        return self.unambig[key]
