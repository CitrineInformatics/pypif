from pypif.obj import System, Property

def test_create_system():
    pif = System()
    pif.uid = "10245"
    pif.names = ["example", "ex"]

def test_convert_to_dictionary():
    pif = System()
    pif.uid = "10245"
    pif.names = ["example", "ex"]
    d = pif._convert_to_dictionary(pif)
