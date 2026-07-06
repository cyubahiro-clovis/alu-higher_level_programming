#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Returns a new list with all occurances of search replaced."""
    return [replace if x == search else x for x in my_list]
