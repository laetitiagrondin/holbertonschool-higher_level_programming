#!/usr/bin/python3
"""
Defines a function read_file that
reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout.
    """
    with open(filename, "r", encoding="utf-8") as f:
        read_text = f.read()
    print(read_text, end="")
