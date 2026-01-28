#!/usr/bin/python3
"""
Defines a class Square.
"""


class Square:
    """
    A class that represents a square with a private size attribute.
    """
    def __init__(self, size=0):
        """
        Function Description:
        - Initializes a Square instance with a private size attribute.

        Parameter:
        - size: an integer that is the size of the square, 0 by default.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
