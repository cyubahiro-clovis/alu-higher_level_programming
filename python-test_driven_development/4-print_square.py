#!/usr/bin/python3
"""This module supplies one function, print_square.

print_square(size) prints a square of the given size using the
character #.
"""


def print_square(size):
    """Print a square of the given size with the character #."""
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
