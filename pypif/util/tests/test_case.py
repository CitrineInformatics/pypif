from pypif.util.case import to_snake_case


def test_to_snake_case():
    assert to_snake_case("relativePath") == "relative_path"