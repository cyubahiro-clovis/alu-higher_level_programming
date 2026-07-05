#!/usr/bin/python3
def print_reserved_list_integer(my_list=[]):
    """Prints all integers of a list in reserve order, one per line."""
    for i in my_list[::-1]:
        print("{:d}".format(i))
