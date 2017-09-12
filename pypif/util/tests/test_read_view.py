from pypif.obj import System, Property, Scalar, Value, Method, Software
from pypif.util.read_view import ReadView


def test_read_view():
    """Test that properties are passed through to the readview"""
    pif = System()
    pif.uid = "10245"
    pif.names = ["example", "ex"]
    pif.properties = [Property(name="foo", scalars=[Scalar(value=1.0)]), Property(name="bar", scalars=[Scalar(value=2.0)])]
    r = ReadView(pif)
    assert r.uid == pif.uid
    assert r.names == pif.names
    assert r.properties["foo"].scalars[0].value == 1.0
    assert r.properties["bar"].scalars[0].value == 2.0


def test_unambig():
    """Test that properties are mirrored in a top level dic"""
    pif = System()
    pif.properties = [Property(name="foo", scalars=[Scalar(value=1.0)]), Property(name="bar", scalars=[Scalar(value=2.0)])]
    r = ReadView(pif)
    assert r["foo"].scalars[0].value == 1.0
    assert r["bar"].scalars[0].value == 2.0


def test_nested_read_view():
    """Test that nested Pios (system here) are recursively processed"""
    pif = System()
    pif.uid = "10245"
    pif.properties = [Property(name="foo", scalars=[Scalar(value=1.0)]), Property(name="bar", scalars=[Scalar(value=2.0)])]
    pif2 = System(sub_systems=[pif])
    r = ReadView(pif2)
    assert r.sub_systems["10245"].uid == pif.uid
    assert r["10245"].uid == pif.uid
    assert r.sub_systems["10245"].properties["foo"].scalars[0].value == 1.0
    assert r.sub_systems["10245"].properties["bar"].scalars[0].value == 2.0
    assert r["foo"].scalars[0].value == 1.0
    assert r["bar"].scalars[0].value == 2.0


def test_condition_elevation():
    """Test that read views elevate conditions"""
    condition = Value(name="spam", scalars=[Scalar(value="eggs")])
    pif = System(properties=[
        Property(name="foo", scalars=[Scalar(value="bar")], conditions=[condition])
    ])
    r = ReadView(pif)
    assert r["foo"].scalars[0].value == "bar", "Didn't elevate property key"
    assert r["spam"].scalars[0].value == "eggs", "Didn't elevate condition key"


def test_ambiguity():
    """Test that ambiguous keys are removed from the top level dict"""
    pif = System()
    pif.uid = "10245"
    pif.properties = [Property(name="foo", scalars=[Scalar(value=1.0)]), Property(name="bar", scalars=[Scalar(value=2.0)])]
    pif2 = System(sub_systems = [pif,], properties=[Property(name="foo", scalars=[Scalar(value=10.0)])])
    r = ReadView(pif2)
    assert r.properties["foo"].scalars[0].value == 10.0
    assert r.sub_systems["10245"].properties["foo"].scalars[0].value == 1.0
    assert "foo" not in r.keys()
    assert r.sub_systems["10245"]["foo"].scalars[0].value == 1.0
    assert r["bar"].scalars[0].value == 2.0


def test_multiple_instances():
    """Test that keys that show up in different places with the same value are kept"""
    pif = System()
    pif.uid = "10245"
    pif.properties = [Property(name="foo", scalars=[Scalar(value=1.0)]), Property(name="bar", scalars=[Scalar(value=2.0)])]
    pif2 = System(sub_systems = [pif,], properties=[Property(name="bar", scalars=[Scalar(value=2.0)])])
    r = ReadView(pif2)
    assert r.properties["bar"].scalars[0].value == 2.0
    assert r.sub_systems["10245"].properties["bar"].scalars[0].value == 2.0
    assert r["bar"].scalars[0].value == 2.0


def test_method_software():
    """Testing that method and software names are elevated"""
    method = Method(name="spam", software=[Software(name="magic")])
    pif = System(properties=[
        Property(name="foo", scalars=[Scalar(value="bar")], methods=[method])
    ])
    r = ReadView(pif)
    assert r["foo"].scalars[0].value == "bar", "Didn't elevate property key"
    assert "spam" in r.keys(), "Expected spam in keys"
    assert "magic" in r.keys(), "Expected magic in keys"
