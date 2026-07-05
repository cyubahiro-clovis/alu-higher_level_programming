#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Returns a list of booleans: True where the value is a multiple of 2."""
    return [x % 2 == 0 for x in my_list]
