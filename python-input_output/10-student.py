#!/usr/bin/python3
"""Module that defines a Student class with a filtered json output."""


class Student:
    """Represents a student with a first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student with a name and an age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation, filtered by attrs."""
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
