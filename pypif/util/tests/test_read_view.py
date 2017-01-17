from pypif.obj import System, Property
from pypif.util.read_view import ReadView

def test_read_view():
    pif = System()
    pif.uid = "10245"
    pif.names = ["example", "ex"]
    pif.properties = [Property(name="foo", scalars=1.0), Property(name="bar", scalars=2.0)]
    r = ReadView(pif)
    assert r.uid == pif.uid
    assert r.names == pif.names
    assert r.properties["foo"].scalars == 1.0
    assert r.properties["bar"].scalars == 2.0

def test_nested_read_view():
    pif = System()
    pif.uid = "10245"
    pif.names = ["example", "ex"]
    pif.properties = [Property(name="foo", scalars=1.0), Property(name="bar", scalars=2.0)]
    pif2 = System(sub_systems = [pif,])
    r = ReadView(pif2)
    assert r.sub_systems["10245"].uid == pif.uid
    assert r.sub_systems["10245"].names == pif.names
    assert r.sub_systems["10245"].properties["foo"].scalars == 1.0
    assert r.sub_systems["10245"].properties["bar"].scalars == 2.0
    assert r["foo"].scalars == 1.0
    assert r["bar"].scalars == 2.0


