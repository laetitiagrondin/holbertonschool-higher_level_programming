#!/usr/bin/python3
"""
Defines a function append_write
that appends a string at the end of a text file (UTF8)
and returns the number of characters added.
"""

def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        nb_characters_added = f.write(text)
    return nb_characters_added
