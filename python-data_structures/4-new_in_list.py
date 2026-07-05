#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element at a position without changing the original.

    Returns a copy of the list. If idx is negative or out of range,
    the copy is returned unchanged.
    """
    new_list = my_list[:]
    if idx < 0:
        return new_list
    if idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
