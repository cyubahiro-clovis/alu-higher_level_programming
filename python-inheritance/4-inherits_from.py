#!/usr/bin/python3
"""Module that checks if an object inherits from a given class."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class inherited from a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
