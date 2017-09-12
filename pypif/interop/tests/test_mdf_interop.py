from pypif.obj.common import Property, Scalar, Person, Name, License, Reference, Value
from pypif.obj.system import System, ChemicalSystem
from pypif.interop.mdf import _to_user_defined, _construct_new_key, _to_meta_data


test_pif = ChemicalSystem(
    chemical_formula="CH4",
    names = ["methane", "fart"],
    contacts = [Person(name=Name(given="Albert", family="Einstein")), Person(name=Name(given="Adam", family="Min"), email="admin@citrine.io")],
    references = [Reference(doi="doi", authors=[Name(given="Captain", family="Marvel")])],
    licenses = [License(url="url")],
    tags = ["too long", "didn't read"],
    properties = [
        Property(name="foo", scalars=[Scalar(value="bar")]),
        Property(name="spam", scalrs=[Scalar(value="eggs")])
    ]
)


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


def test_condition():
    """Test that conditions are flattened and added"""
    condition = Value(name="spam", scalars=[Scalar(value="eggs")])
    sys = System(properties=[
        Property(name="foo", scalars=[Scalar(value="bar")], conditions=[condition])
    ])
    user_data = _to_user_defined(sys)
    assert user_data["spam"] == "eggs"


def test_construct_new_key():
    """Test the new key constructions"""
    assert _construct_new_key("foo") == "foo"
    assert _construct_new_key("foo", units="bar") == "foo_bar"
    assert _construct_new_key("foo bar") == "foo_bar"
    assert _construct_new_key("#foo", units="g/cm^3") == "_foo_g_cm_3"


def test_to_meta_data():
    meta_data = _to_meta_data(test_pif)
    assert meta_data == {
        "title": "methane",
        "composition": "CH4",
        "acl": ["public"],
        "data_contact": [{
            "given_name": "Albert",
            "family_name": "Einstein"
            },{
            "given_name": "Adam",
            "family_name": "Min",
            "email": "admin@citrine.io"
            }],
        "data_contributor": [{}],
        "citation": ["doi"],
        "author": [{
            "given_name": "Captain",
            "family_name": "Marvel"
            }],
        "license": "url",
        "tags": ["too long", "didn't read"],
        "links": {
            #landing_page
            "publication": ["doi"]
            }
        }

