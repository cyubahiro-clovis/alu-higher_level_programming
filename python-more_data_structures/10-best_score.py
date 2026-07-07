#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns the key with the biggest integer value, or None."""
    if not a_dictionary:
        return None
    best_key = None
    for key in a_dictionary:
        if best_key is None:
            best_key = key
        elif a_dictionary[key] > a_dictionary[best_key]:
            best_key = key
    return best_key
