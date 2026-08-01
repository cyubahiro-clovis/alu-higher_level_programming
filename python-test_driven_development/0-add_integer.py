#!/usr/bin/python3
"""This module supplies one function, add_integer.

add_integer(a, b=98) returns the addition of its two arguments.
Both arguments must be integers or floats, and floats are casted
to integers before the addition is done.
"""


def add_integer(a, b=98):
    """Return the addition of a and b as an integer.

    Floats are casted to integers before adding them together.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    if a != a or a in (float('inf'), float('-inf')):
        raise ValueError("cannot convert float NaN to integer")
    if b != b or b in (float('inf'), float('-inf')):
        raise ValueError("cannot convert float NaN to integer")
    return int(a) + int(b)
