#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides two integers; prints the result in the finally block."""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
