#!/usr/bin/python3
"""This module supplies one function, text_indentation.

text_indentation(text) prints a text with two new lines after each
of the characters ., ? and :
"""


def text_indentation(text):
    """Print text with two new lines after each of ., ? and : characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    buffer = ""
    for char in text:
        buffer += char
        if char in ".?:":
            print(buffer.strip())
            print()
            buffer = ""
    if buffer.strip():
        print(buffer.strip(), end="")
