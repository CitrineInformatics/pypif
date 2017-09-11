from pypif.obj.common.file_reference import FileReference
from pypif import pif

def test_round_robin():
    url = "https://citrination.com/datasets/1160/version/3/file/308882"
    path = "/tmp/foo.bar"
    fr = FileReference(url=url, relative_path=path)
    assert fr.relative_path == path, "Python object couldn't store relative path"
    assert fr.url == url, "Python object couldn't store URL"
    round_robin = pif.loads(pif.dumps(fr), class_=FileReference)
    assert round_robin.relative_path == path, "Relative path didn't survive json round robin"
    assert round_robin.url == url, "URL dind't survive json round robin"
