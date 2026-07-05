#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at position idx (without using pop()).

    If idx is negative or out of range, the list is unchanged.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
