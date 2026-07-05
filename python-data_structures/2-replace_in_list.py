#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position (like C).

    Does nothing and returns the original list if idx is negative
    or out of range.
    """
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
