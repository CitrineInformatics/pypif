from pypif.obj.common import Property, Scalar
from pypif.obj.system import System
from pypif.interop.mdf import _to_user_defined


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
    sys = System(properties=[Property(name="foo", vectors=[[Scalar(value="spam"), Scalar(value="eggs")]])])
    user_data = _to_user_defined(sys)
    assert user_data["foo"] == ["spam", "eggs"] 

