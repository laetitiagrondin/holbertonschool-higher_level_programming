#!/usr/bin/python3
"""
Module that prints a square with the character.
"""


def print_square(size):
    """
    Function Description:
    - Write a function that prints a square with the character #.
    - Prototype: def print_square(size).
    - size must be an integer, otherwise,
        raise a TypeError exception with the message:
        "size must be an integer".
    - if size is less than 0,
        raise a ValueError exception with the message:
        "size must be >= 0".
    - if size is a float and is less than 0,
        raise a TypeError exception with the message
        "size must be an integer".

    Parameters:
    - size: integer which is the size length of the square.

    Returns:
    - This function does not return.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
