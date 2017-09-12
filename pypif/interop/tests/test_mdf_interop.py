from pypif.obj.common import Property, Scalar
from pypif.obj.system import System
from pypif.interop.mdf import _to_user_defined


def test_property_value():
    """Test that a simple property gets pulled out"""
    sys = System(properties=[Property(name="foo", scalars=[Scalar(value="bar")])])
    user_data = _to_user_defined(sys)
    assert user_data["foo"] == "bar"
    
  
