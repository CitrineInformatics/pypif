from pypif.pif import loads, dumps
from pypif.obj.system import System
from pypif.obj.common import Property, Scalar, FileReference, ProcessStep, Value, Person, Name


def test_basic_round_robin():
    pif = System()
    pif.uid = "foo"
    pif2 = loads(dumps(pif))
    assert pif2.uid == pif.uid


def test_full_round_robin():
    pif = System(
        properties=[
            Property(name="foo", scalars=[Scalar(value=2.4), Scalar(value=2.5)]),
            Property(name="bar", scalars=[Scalar(value=2.4)]),
            Property(name="spam", files=[FileReference(relative_path="/tmp/file")])
        ],
        preparation=[ProcessStep(name="processed", details=[Value(name="temp", scalars=[Scalar(value=1.0)])])],
        contacts=[Person(name=Name(family="Einstein"))]
    )

    pif2 = loads(dumps(pif))
    assert pif2.as_dictionary() == pif.as_dictionary(), "PIF contents are not the same"
    assert pif.properties[0].scalars[0].value == pif2.properties[0].scalars[0].value
    assert pif.properties[1].scalars[0].value == pif2.properties[1].scalars[0].value
    assert pif.properties[2].files[0].relative_path == pif2.properties[2].files[0].relative_path
    assert pif.preparation[0].details[0].scalars[0].value == pif2.preparation[0].details[0].scalars[0].value
    assert pif.contacts[0].name.family == pif2.contacts[0].name.family
