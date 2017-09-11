from pypif.obj.common.value import Value
from pypif import pif
import pytest


def test_basic():
    """Test that constructor arguments are saved"""
    foo = Value(name="foo", units="eV", tags=["tag1", "tag2"])
    assert foo.name == "foo"
    assert foo.units == "eV"
    assert len(foo.tags) == 2
    assert "tag1" in foo.tags
    assert "tag2" in foo.tags


def test_round_robin():
    foo = Value(name="foo", units="eV")
    assert foo.name == "foo", "Value object couldn't store name"
    assert foo.units == "eV", "Value object couldn't store units"
    round_robin = pif.loads(pif.dumps(foo), class_=Value)
    assert round_robin.name == "foo", "Name didn't survive json round robin"
    assert round_robin.units == "eV", "Units didn't survive json round robin"


@pytest.mark.xfail
def test_convert_scalar():
    """Test that scalars are made rigid"""
    foo = Value(scalars=1.2)
    assert foo.scalars[0].value == 1.2


@pytest.mark.xfail
def test_convert_setter():
    """Test that scalars are made rigid"""
    foo = Value()
    foo.scalars = 1.2
    assert foo.scalars[0].value == 1.2


@pytest.mark.xfail
def test_convert_vector():
    """Test that vectors are made rigid"""
    foo = Value(vectors=[1.2, 1.3])
    assert foo.vectors[0][1].value == 1.3


@pytest.mark.xfail
def test_convert_matrix():
    """Test that matrices are made rigid"""
    foo = Value(matrices=[[1.0, 2.0], [-2.0, 1.0]])
    assert foo.matrices[0][0][1].value == 2.0
    assert foo.matrices[0][1][0].value == -2.0
