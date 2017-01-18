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
from pypif.obj import System as Subsystem
from pypif.pif import dumps


def new_keypair(key, value, ambig, unambig):
    """
    Check new keypair against existing unambiguous dict

    :param key: of pair
    :param value: of pair
    :param ambig: set of keys with ambig decoding
    :param unambig: set of keys with unambig decoding
    :return:
    """
    if key in ambig:
        return

    if key in unambig and value != unambig[key]:
            ambig.add(key)
            del unambig[key]
            return

    unambig[key] = value
    return


def add_child_ambig(child_ambig, child_unambig, ambig, unambig):
    """
    Add information about decodings of a child object

    :param child_ambig: ambiguous set from child
    :param child_unambig: unambiguous set from child
    :param ambig: set of keys storing ambig decodings
    :param unambig: dictionary storing unambiguous decodings
    :return:
    """
    for k in child_ambig:
        ambig.add(k)
        del unambig[k]

    for k, v in child_unambig.items():
        new_keypair(k, v, ambig, unambig)

    return


class ReadView():

    def __init__(self, system):
        """
        Setup a ReadView by recursing through the pif objects

        :param system: to process into a ReadView; doesn't need to be a system
        """

        self.raw = system

        # List of classes to generate an index from
        self.inlines = [
            (Subsystem, "uid"),
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

        # dictionary of unambiguous short keys
        self.unambig = {}
        # set of keys where there is ambiguity
        self.ambig = set()

        # iterate over the members of the system
        for k in system.__dict__:
            added = False

            # check if list
            if isinstance(getattr(system, k), list):
                for t, name in self.inlines:
                    # check if we know how to decode the type
                    if isinstance(getattr(system, k)[0], t):
                        # populate a dictionary
                        parsed = {}
                        for x in getattr(system, k):
                            # define a key
                            new_key = getattr(x, name)
                            new_val = ReadView(x)
                            parsed[new_key] = new_val
                            new_keypair(new_key, new_val, self.ambig, self.unambig)
                            add_child_ambig(new_val.ambig, new_val.unambig, self.ambig, self.unambig)
                        # set the property in the readview to point to the dictionary
                        setattr(self, k[1:], parsed)
                        added = True
                        break
                if not added:
                    # just mirror the property
                    setattr(self, k[1:], getattr(system, k))
            else:
                # Same logic as above, but not wrapped in a list
                for t, name in self.inlines:
                    if isinstance(getattr(system, k), t):
                        new_key = getattr(getattr(system, k), name)
                        new_val = ReadView(getattr(system, k))
                        new_keypair(new_key, new_val, self.ambig, self.unambig)
                        add_child_ambig(new_val.ambig, new_val.unambig, self.ambig, self.unambig)
                        setattr(self, k[1:], {new_key: new_val})
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

    def __ne__(self, other):
        if not isinstance(other, ReadView):
            return True

        return dumps(other.raw) != dumps(self.raw)

    def __eq__(self, other):
        return not self.__ne__(other)