#!/usr/bin/python3
"""Module that checks if an object is an instance or subclass instance."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or a subclass of it."""
    return isinstance(obj, a_class)
