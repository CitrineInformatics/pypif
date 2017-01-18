from pypif.obj.common.value import Value


def test_basic():
    """Test that constructor arguments are saved"""
    foo = Value(name="foo", units="eV", tags=["tag1", "tag2"])
    assert foo.name == "foo"
    assert foo.units == "eV"
    assert len(foo.tags) == 2
    assert "tag1" in foo.tags
    assert "tag2" in foo.tags

