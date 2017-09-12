from pypif.obj.common import Property, Scalar
from pypif.obj.system import System
from pypif.interop.mdf import _to_user_defined, _construct_new_key


def test_property_value():
    """Test that a simple property gets pulled out"""
    sys = System(properties=[Property(name="foo", scalars=[Scalar(value="bar")])])
    user_data = _to_user_defined(sys)
    assert user_data["foo"] == "bar"
   
 
def test_property_list():
    """Test that a property with a list of scalars gets pulled out"""
    sys = System(properties=[Property(name="foo", scalars=[Scalar(value="spam"), Scalar(value="eggs")])])
    user_data = _to_user_defined(sys)
    assert user_data["foo"] == ["spam", "eggs"] 


def test_property_vector():
    """Test that a vector gets pulled out"""
    sys = System(properties=[Property(name="foo", units="bar", vectors=[[Scalar(value="spam"), Scalar(value="eggs")]])])
    user_data = _to_user_defined(sys)
    assert user_data["foo_bar"] == ["spam", "eggs"] 


def test_construct_new_key():
    """Test the new key constructions"""
    assert _construct_new_key("foo") == "foo"
    assert _construct_new_key("foo", units="bar") == "foo_bar"
    assert _construct_new_key("foo bar") == "foo_bar"
    assert _construct_new_key("#foo", units="g/cm^3") == "_foo_g_cm_3"
