#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral string to an integer."""
    if not isinstance(roman_string, str):
        return 0
    values = {'I': 1, 'V': 5, 'X': 10,
              'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    n = len(roman_string)
    for i in range(n):
        current = values[roman_string[i]]
        if i + 1 < n and current < values[roman_string[i + 1]]:
            total -= current
        else:
            total += current
    return total
