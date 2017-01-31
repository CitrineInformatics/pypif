from pypif.pif import loads, dumps
from pypif.obj.system import System
from pypif.obj.common.property import Property


def test_basic_round_robin():
    pif = System()
    pif.uid = "foo"
    pif2 = loads(dumps(pif))
    assert pif2.uid == pif.uid


def test_full_round_robin():
    pif = System()
    pif.properties = [Property(name="foo", scalars=[2.4, 2.5]), Property(name="bar", scalars=2.4)]
    pif2 = loads(dumps(pif))
    assert pif.properties[0].scalars[0].value == pif2.properties[0].scalars[0].value
