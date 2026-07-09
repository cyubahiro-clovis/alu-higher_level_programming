#!/usr/bin/python3
def safe_print_integer(value):
    """Prints a value as an integer, returns True if printed."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
