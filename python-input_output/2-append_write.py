#!/usr/bin/python3
"""Module that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """Appends text to a UTF8 file and returns the characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
