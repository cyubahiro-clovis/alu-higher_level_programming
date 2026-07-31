#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """Represents the base geometry of a shape."""

    def area(self):
        """Raises an exception because area is not implemented."""
        raise Exception("area() is not implemented")
