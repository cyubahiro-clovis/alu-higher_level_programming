#!/usr/bin/python3
"""Module that describes an object with a serializable dictionary."""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON."""
    return obj.__dict__
