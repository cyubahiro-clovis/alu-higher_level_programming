#!/usr/bin/python3
def no_c(my_string):
    """Returns a new string with all 'c' and 'C' characters removed."""
    new_string = ""
    for char in my_string:
        if char != "c" and char != "C":
            new_string += char
    return new_string
