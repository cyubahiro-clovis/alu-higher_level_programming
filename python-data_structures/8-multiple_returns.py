#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple: (length of sentence, first character).

    If the sentence is empty, the first character is None.
    """
    length = len(sentence)
    if length == 0:
        first = None
    else:
        first = sentence[0]
    return (length, first)
