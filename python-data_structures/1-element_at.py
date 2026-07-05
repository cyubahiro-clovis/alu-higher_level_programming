#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list, safely (like C)

    Returns None if idx is negative or out of range.
    """
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
