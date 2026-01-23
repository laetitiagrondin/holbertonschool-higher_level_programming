#!/usr/bin/python3
"""
This module provides a function to print a text with proper indentation.
The text is split into lines, and two new lines are printed after each
occurrence of the characters '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Function Description:
    - Write a function that prints a text with 2 new lines
        after each of these characters: ".", "?" and ":".
    - Prototype: def text_indentation(text).
    - text must be a string, otherwise,
        raise a TypeError exception with the message:
        "text must be a string".
    - There should be no space at the beginning
    or at the end of each printed line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip() + char)
            print()
            line = ""
        else:
            line += char
    if line:
        print(line.strip(), end="")
