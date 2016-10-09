import re


_first_camel_case_regex = re.compile('(.)([A-Z][^A-Z]+)')
_second_camel_case_regex = re.compile('([^A-Z_])([A-Z])')


def to_camel_case(snake_case_string):
    """
    Convert a string from snake case to camel case. For example, "some_var" would become "someVar".

    :param snake_case_string: Snake-cased string to convert to camel case.
    :returns: Camel-cased version of snake_case_string.
    """
    parts = snake_case_string.lstrip('_').split('_')
    return parts[0] + ''.join([i.title() for i in parts[1:]])


def to_capitalized_camel_case(snake_case_string):
    """
    Convert a string from snake case to camel case with the first letter capitalized. For example, "some_var"
    would become "SomeVar".

    :param snake_case_string: Snake-cased string to convert to camel case.
    :returns: Camel-cased version of snake_case_string.
    """
    parts = snake_case_string.split('_')
    return ''.join([i.title() for i in parts])


def to_snake_case(camel_case_string):
    """
    Convert a string from camel case to snake case. From example, "someVar" would become "some_var".

    :param camel_case_string: Camel-cased string to convert to snake case.
    :return: Snake-cased version of camel_case_string.
    """
    first_pass = _first_camel_case_regex.sub(r'\1_\2', camel_case_string)
    return _second_camel_case_regex.sub(r'\1_\2', first_pass).lower()


def keys_to_snake_case(camel_case_dict):
    """
    Make a copy of a dictionary with all keys converted to snake case. This is just calls to_snake_case on
    each of the keys in the dictionary and returns a new dictionary.

    :param camel_case_dict: Dictionary with the keys to convert.
    :type camel_case_dict: Dictionary.

    :return: Dictionary with the keys converted to snake case.
    """
    return dict((to_snake_case(key), value) for (key, value) in camel_case_dict.items())
