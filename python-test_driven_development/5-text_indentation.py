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
    text = text.strip()
    if len(text) == 0:
        return
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
